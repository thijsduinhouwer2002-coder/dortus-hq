import * as path from "path";

// End-to-end test van Rollwright in de echte Obsidian.
// Draait op GitHub Actions (zie .github/workflows/rollwright-e2e.yml), niet in de Claude-omgeving.
/** Zet de reeks terug naar het begin; na een herstart van Obsidian zet hij de functie opnieuw. */
async function zaai() {
	try {
		await browser.execute(() => {
			window.__dortusZaad = 20261119;
			if (!window.__dortusRandom) {
				window.__dortusRandom = () => {
					let a = (window.__dortusZaad = (window.__dortusZaad + 0x6d2b79f5) | 0);
					let t = Math.imul(a ^ (a >>> 15), 1 | a);
					t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
					return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
				};
				Math.random = window.__dortusRandom;
			}
		});
	} catch (e) {
		console.log(`ZAAD NIET GEZET: ${e}`);
	}
}

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
	// (mulberry32), zodat de schermafbeeldingen van run tot run gelijk blijven en de beeldvergelijking alleen echte
	// veranderingen ziet. Voor elke test gaat de reeks terug naar het begin (alleen de stand, de functie blijft),
	// zodat een verschil in het aantal worpen eerder in de spec niet doorwerkt. Specs die zelf Math.random
	// vastzetten (crit, classic) bewaren en herstellen deze reeks zoals eerst de echte.
	before: async function () {
		await zaai();
	},
	beforeTest: async function () {
		await zaai();
	},
};
