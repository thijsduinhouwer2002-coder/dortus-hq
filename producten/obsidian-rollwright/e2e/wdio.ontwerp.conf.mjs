import * as path from "path";

// Ontwerptest van Daan: alleen schermafbeeldingen, licht, donker, populaire thema's, smal venster, instellingen.
// Draait op GitHub Actions via .github/workflows/rollwright-ontwerp.yml.
export const config = {
	runner: "local",
	framework: "mocha",
	specs: ["./ontwerp/v2.e2e.mjs"],
	maxInstances: 1,
	capabilities: [{
		browserName: "obsidian",
		browserVersion: "latest",
		"wdio:obsidianOptions": {
			installerVersion: "earliest",
			plugins: [".."],
			themes: [
				// Blue Topaz valt af: zijn versienummer (2026110301) kan de launcher niet lezen.
				{ name: "Minimal", enabled: false },
				{ name: "AnuPpuccin", enabled: false },
				{ name: "Things", enabled: false },
				{ name: "Border", enabled: false },
			],
			vault: "vaults/ontwerp",
		},
	}],
	services: ["obsidian"],
	reporters: ["obsidian"],
	cacheDir: path.resolve(".obsidian-cache"),
	mochaOpts: { ui: "bdd", timeout: 180000 },
	logLevel: "warn",
};
