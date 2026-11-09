import * as path from "path";

// Ontwerptest van Daan: alleen schermafbeeldingen, licht, donker, populaire thema's, smal venster, instellingen.
// Draait op GitHub Actions via .github/workflows/rollwright-ontwerp.yml.
export const config = {
	runner: "local",
	framework: "mocha",
	specs: ["./ontwerp/beweging.e2e.mjs"],
	maxInstances: 1,
	capabilities: [{
		browserName: "obsidian",
		browserVersion: "latest",
		"wdio:obsidianOptions": {
			installerVersion: "latest", // 8 nov: de AppImage van 1.5.8 (earliest) gaf op GitHub steeds 504
			plugins: [".."],
			// Geen thema's: deze test gebruikt ze niet, en Minimal was 8 nov 08:46 niet te downloaden.
			vault: "vaults/ontwerp",
		},
	}],
	services: ["obsidian"],
	reporters: ["obsidian"],
	cacheDir: path.resolve(".obsidian-cache"),
	mochaOpts: { ui: "bdd", timeout: 180000 },
	logLevel: "warn",
};
