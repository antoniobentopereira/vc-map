import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from linkedin import build_workflow, check_workflow  # noqa: E402


class CheckWorkflowTest(unittest.TestCase):
    def test_read_only_actions_pass_at_any_depth(self):
        workflow = {"actionType": "st.searchCompanies", "term": "Norma", "then": {
            "actionType": "st.doForCompanies", "then": {"actionType": "st.openCompanyPage", "basicInfo": True}}}
        self.assertEqual(check_workflow(workflow), [])
        self.assertEqual(check_workflow([{"actionType": "st.openPersonPage", "personUrl": "https://x"}] * 2), [])

    def test_an_action_that_writes_is_refused_at_the_root(self):
        errors = check_workflow({"actionType": "st.sendConnectionRequest", "personUrl": "https://x"})
        self.assertEqual(len(errors), 1)
        self.assertIn("st.sendConnectionRequest", errors[0])

    def test_an_action_that_writes_is_refused_when_nested(self):
        workflow = {"actionType": "st.openPersonPage", "personUrl": "https://x", "then": [
            {"actionType": "st.retrievePersonExperience"},
            {"actionType": "st.retrievePersonPosts", "then": {"actionType": "st.doForPosts", "then": {"actionType": "st.reactToPost", "type": "like"}}},
        ]}
        errors = check_workflow(workflow)
        self.assertEqual(len(errors), 1)
        self.assertIn("st.reactToPost", errors[0])

    def test_missing_action_type_and_deep_nesting_are_refused(self):
        self.assertIn("actionType", check_workflow({"personUrl": "https://x"})[0])
        deep = {"actionType": "st.openPost", "postUrl": "https://x"}
        for _ in range(5):
            deep = {"actionType": "st.doForPosts", "then": deep}
        self.assertTrue(any("5 levels" in e for e in check_workflow(deep)))

    def test_not_an_action_object(self):
        self.assertEqual(len(check_workflow("st.openPost")), 1)


class BuildWorkflowTest(unittest.TestCase):
    def test_every_command_builds_a_read_only_workflow(self):
        cases = [
            ("company", {"url": "https://www.linkedin.com/company/x", "posts": 5}),
            ("founders", {"url": "https://www.linkedin.com/company/x"}),
            ("person", {"url": "https://www.linkedin.com/in/x", "experience": True, "posts": 20, "since": "2021-01-01T00:00:00Z"}),
            ("search-companies", {"term": "Norma tax", "limit": 5}),
            ("search-posts", {"term": "Carbonext Series A", "mentioning": ["Norte Ventures"], "limit": 10}),
            ("post", {"url": "https://www.linkedin.com/posts/x"}),
        ]
        for command, args in cases:
            self.assertEqual(check_workflow(build_workflow(command, args)), [], command)

    def test_founders_uses_one_employees_action_and_a_chosen_title(self):
        # Linked API rejects two actions of the same type in one `then` array (invalidWorkflow).
        url = "https://www.linkedin.com/company/x"
        default = build_workflow("founders", {"url": url})["then"]
        self.assertIsInstance(default, dict)
        self.assertEqual(default["filter"]["position"], "Founder")
        portuguese = build_workflow("founders", {"url": url, "position": "Fundador"})["then"]
        self.assertEqual(portuguese["filter"]["position"], "Fundador")

    def test_optional_parts_are_left_out(self):
        self.assertNotIn("then", build_workflow("company", {"url": "https://www.linkedin.com/company/x", "posts": 0}))
        self.assertNotIn("filter", build_workflow("search-posts", {"term": "x", "mentioning": [], "limit": 10}))


if __name__ == "__main__":
    unittest.main()


class WorkflowIdTest(unittest.TestCase):
    """A started workflow's id is never lost, so a parked or interrupted one can be fetched later."""

    def setUp(self):
        import io
        from unittest import mock
        import linkedin
        responses = iter([
            {"success": True, "result": {"workflowId": "wf-123"}},
            {"success": True, "result": {"workflowStatus": "running", "pendingReason": "outsideWorkingHours"}},
        ])
        self.stderr = io.StringIO()
        patches = [mock.patch.object(linkedin, "_request", lambda *a, **k: next(responses)),
                   mock.patch.object(sys, "stderr", self.stderr)]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)
        self.linkedin = linkedin

    def test_a_parked_workflow_returns_its_id(self):
        code, result = self.linkedin.run(build_workflow("company", {"url": "https://www.linkedin.com/company/x", "posts": 0}))
        self.assertEqual(code, 3)
        self.assertEqual(result["workflowId"], "wf-123")

    def test_the_id_is_printed_as_soon_as_the_workflow_starts(self):
        self.linkedin.run(build_workflow("company", {"url": "https://www.linkedin.com/company/x", "posts": 0}))
        self.assertIn("wf-123", self.stderr.getvalue())
