"""Last-resort LinkedIn reads through Linked API (https://linkedapi.io/docs/). See docs/research-recipe.md, step 7.

Linked API runs each workflow in a cloud browser signed in to the owner's own LinkedIn account, one workflow at a
time, within the account's working hours and action limits (set in the Linked API platform). This client only
reads: it refuses any workflow containing an action outside READ_ONLY_ACTIONS, so a research agent can never send
a message, a connection request, a reaction, a comment or a post from the owner's account.

Tokens come from two environment variables and are never written to the repo:
  LINKEDAPI_TOKEN                  the linked-api-token (Linked API account)
  LINKEDAPI_IDENTIFICATION_TOKEN   the identification-token (the connected LinkedIn account)

Usage (prints the workflow completion as JSON):
  python scripts/linkedin.py check
  python scripts/linkedin.py company <company-url> [--posts N]
  python scripts/linkedin.py founders <company-url>
  python scripts/linkedin.py person <person-url> [--experience] [--posts N] [--since ISO-TIME]
  python scripts/linkedin.py search-companies "<term>" [--limit N]
  python scripts/linkedin.py search-posts "<term>" [--mentioning "Norte Ventures"] [--limit N]
  python scripts/linkedin.py post <post-url>
  python scripts/linkedin.py run <workflow.json>
  python scripts/linkedin.py result <workflow-id>

Exit codes: 0 completed, 1 error or failed workflow, 2 workflow refused (not read-only), 3 parked or still
running (outside working hours or timed out; fetch it later with `result <workflow-id>`).
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

BASE_URL = "https://api.linkedapi.io"
TOKEN_ENV = "LINKEDAPI_TOKEN"
IDENTIFICATION_ENV = "LINKEDAPI_IDENTIFICATION_TOKEN"
MAX_NESTING = 5  # Linked API rejects workflows nested deeper than this
POLL_SECONDS = 5
TIMEOUT_SECONDS = 900

# Actions that only read LinkedIn. Everything else (messages, connection requests, invitations, reactions,
# comments, posts, reposts, endorsements, Sales Navigator lists, Recruiter projects) is refused.
READ_ONLY_ACTIONS = {
    "st.searchCompanies", "st.searchPeople", "st.searchPosts",
    "st.openCompanyPage", "st.retrieveCompanyEmployees", "st.retrieveCompanyDMs", "st.retrieveCompanyPosts",
    "st.openPersonPage", "st.retrievePersonExperience", "st.retrievePersonEducation", "st.retrievePersonPosts",
    "st.openPost",
    "st.doForCompanies", "st.doForPeople", "st.doForPosts",
}


def check_workflow(workflow, depth=1):
    """Return a list of reasons this workflow may not run; empty if every action, at every depth, only reads."""
    if isinstance(workflow, list):
        return [e for action in workflow for e in check_workflow(action, depth)]
    if not isinstance(workflow, dict):
        return [f"not an action object: {workflow!r}"]
    errors = []
    action = workflow.get("actionType")
    if not action:
        errors.append("an action has no actionType")
    elif action not in READ_ONLY_ACTIONS:
        errors.append(f"{action} is not a read-only action, so it is refused")
    if depth > MAX_NESTING:
        errors.append(f"workflow is nested deeper than {MAX_NESTING} levels")
    if "then" in workflow:
        errors += check_workflow(workflow["then"], depth + 1)
    return errors


def build_workflow(command, args):
    """The workflow for one of the read commands. args is a dict of that command's options."""
    if command == "company":
        workflow = {"actionType": "st.openCompanyPage", "companyUrl": args["url"], "basicInfo": True}
        if args.get("posts"):
            workflow["then"] = {"actionType": "st.retrieveCompanyPosts", "limit": args["posts"]}
        return workflow
    if command == "founders":
        return {"actionType": "st.openCompanyPage", "companyUrl": args["url"], "basicInfo": True, "then": [
            {"actionType": "st.retrieveCompanyEmployees", "label": title.lower(), "limit": 10, "filter": {"position": title}}
            for title in ("Founder", "Fundador")
        ]}
    if command == "person":
        workflow = {"actionType": "st.openPersonPage", "personUrl": args["url"], "basicInfo": True}
        children = []
        if args.get("experience"):
            children.append({"actionType": "st.retrievePersonExperience"})
        if args.get("posts"):
            posts = {"actionType": "st.retrievePersonPosts", "limit": args["posts"]}
            if args.get("since"):
                posts["since"] = args["since"]
            children.append(posts)
        if children:
            workflow["then"] = children
        return workflow
    if command == "search-companies":
        return {"actionType": "st.searchCompanies", "term": args["term"], "limit": args.get("limit", 5)}
    if command == "search-posts":
        workflow = {"actionType": "st.searchPosts", "term": args["term"], "limit": args.get("limit", 10)}
        if args.get("mentioning"):
            workflow["filter"] = {"mentioningCompanies": list(args["mentioning"])}
        return workflow
    if command == "post":
        return {"actionType": "st.openPost", "postUrl": args["url"], "basicInfo": True}
    raise ValueError(f"unknown command {command!r}")


def _tokens():
    token, identification = os.environ.get(TOKEN_ENV), os.environ.get(IDENTIFICATION_ENV)
    if not token or not identification:
        sys.exit(f"Set {TOKEN_ENV} and {IDENTIFICATION_ENV} (Linked API tokens from app.linkedapi.io) first.")
    return token, identification


def _request(method, path, body=None):
    token, identification = _tokens()
    data = json.dumps(body).encode("utf-8") if body is not None else None
    request = urllib.request.Request(BASE_URL + path, data=data, method=method, headers={
        "linked-api-token": token, "identification-token": identification, "content-type": "application/json"})
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code == 429 and attempt == 0:  # tooManyRequests: wait and retry once
                time.sleep(60)
                continue
            try:
                return json.load(error)
            except ValueError:
                return {"success": False, "error": {"type": f"http{error.code}", "message": str(error)}}


def _wait(workflow_id):
    """Poll until the workflow completes or fails. Returns (exit code, response)."""
    deadline = time.monotonic() + TIMEOUT_SECONDS
    while True:
        response = _request("GET", f"/workflows/{workflow_id}")
        if not response.get("success"):
            return 1, response
        result = {"workflowId": workflow_id, **response["result"]}
        status = result.get("workflowStatus")
        if status == "completed":
            return 0, result
        if status == "failed":
            return 1, result
        if result.get("pendingReason") == "outsideWorkingHours" or time.monotonic() > deadline:
            return 3, result  # parked until the account's working hours, or still queued: fetch it later
        time.sleep(POLL_SECONDS)


def run(workflow):
    errors = check_workflow(workflow)
    if errors:
        return 2, {"refused": errors}
    response = _request("POST", "/workflows", workflow)
    if not response.get("success"):
        return 1, response
    workflow_id = response["result"]["workflowId"]
    # Printed before waiting, so an interrupted run still leaves the id for `result <workflow-id>`.
    print(f"workflowId: {workflow_id}", file=sys.stderr, flush=True)
    return _wait(workflow_id)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check")
    company = sub.add_parser("company")
    company.add_argument("url")
    company.add_argument("--posts", type=int, default=0)
    sub.add_parser("founders").add_argument("url")
    person = sub.add_parser("person")
    person.add_argument("url")
    person.add_argument("--experience", action="store_true")
    person.add_argument("--posts", type=int, default=0)
    person.add_argument("--since")
    companies = sub.add_parser("search-companies")
    companies.add_argument("term")
    companies.add_argument("--limit", type=int, default=5)
    posts = sub.add_parser("search-posts")
    posts.add_argument("term")
    posts.add_argument("--mentioning", action="append", default=[])
    posts.add_argument("--limit", type=int, default=10)
    sub.add_parser("post").add_argument("url")
    sub.add_parser("run").add_argument("file")
    sub.add_parser("result").add_argument("workflow_id")
    args = parser.parse_args(argv)

    if args.command == "check":
        response = _request("GET", "/account")
        code = 0 if response.get("success") else 1
    elif args.command == "result":
        code, response = _wait(args.workflow_id)
    elif args.command == "run":
        with open(args.file, encoding="utf-8") as f:
            code, response = run(json.load(f))
    else:
        code, response = run(build_workflow(args.command, vars(args)))
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(response, ensure_ascii=False, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
