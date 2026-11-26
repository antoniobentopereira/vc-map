// Reactive navigation state shared between the router (main.ts) and the Svelte shell.
export const nav = $state({ lens: "float", card: null as string | null });
