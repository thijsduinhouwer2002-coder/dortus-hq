import * as path from "path";

// End-to-end test van Rollwright in de echte Obsidian.
// Draait op GitHub Actions (zie .github/workflows/rollwright-e2e.yml), niet in de Claude-omgeving.
export const config = {
	runner: "local",
	framework: "mocha",
	specs: ["./specs/**/*.e2e.mjs"],
	maxInstances: 1,
	capabilities: [{
		browserName: "obsidian",
		// Week-test (roestronde R4): OBSIDIAN_APP en OBSIDIAN_INSTALLER kiezen een andere versie, bijvoorbeeld latest/latest.
		browserVersion: process.env.OBSIDIAN_APP || "latest",
		"wdio:obsidianOptions": {
			installerVersion: process.env.OBSIDIAN_INSTALLER || "earliest",
			plugins: [".."],
			vault: "vaults/test",
		},
	}],
	services: ["obsidian"],
	reporters: ["obsidian"],
	cacheDir: path.resolve(".obsidian-cache"),
	mochaOpts: { ui: "bdd", timeout: 120000 },
	logLevel: "warn",
	// Vast zaad voor de dobbelstenen (roestronde R4): Math.random in het Obsidian-venster wordt een vaste reeks
	// (mulberry32), één keer per specbestand, zodat de schermafbeeldingen van run tot run gelijk blijven en de
	// beeldvergelijking alleen echte veranderingen ziet. Specs die zelf Math.random vastzetten (crit, classic)
	// bewaren en herstellen deze reeks zoals eerst de echte.
	before: async function () {
		try {
			await browser.execute(() => {
				let a = 20261119;
				Math.random = () => {
					a = (a + 0x6d2b79f5) | 0;
					let t = Math.imul(a ^ (a >>> 15), 1 | a);
					t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
					return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
				};
			});
			console.log("ZAAD GEZET");
		} catch (e) {
			console.log(`ZAAD NIET GEZET: ${e}`);
		}
	},
};
