import * as path from "path";

// End-to-end test van Rollwright in de echte Obsidian.
// Draait op GitHub Actions (zie .github/workflows/rollwright-e2e.yml), niet in de Claude-omgeving.
export const config = {
	runner: "local",
	framework: "mocha",
	specs: ["./specs/skin-tegels.e2e.mjs"],
	maxInstances: 1,
	capabilities: [{
		browserName: "obsidian",
		browserVersion: "latest",
		"wdio:obsidianOptions": {
			installerVersion: "earliest",
			plugins: [".."],
			vault: "vaults/test",
		},
	}],
	services: ["obsidian"],
	reporters: ["obsidian"],
	cacheDir: path.resolve(".obsidian-cache"),
	mochaOpts: { ui: "bdd", timeout: 120000 },
	logLevel: "warn",
};
