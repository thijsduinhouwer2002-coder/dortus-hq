import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// Daan punt 5 en 8: Parchment in donker is donker perkament, en een fout heeft in elke skin de gewone letter.
// De skin is alleen CSS (klasse op body), dus de test zet de klassen zelf, zoals Obsidian en de plugin doen.
const SHOTS = "screenshots";
const LEAF = ".workspace-leaf.mod-active .markdown-reading-view";

async function zet(skin, donker) {
	await browser.execute((skin, donker) => {
		for (const c of Array.from(document.body.classList)) if (c.startsWith("rollwright-skin-")) document.body.classList.remove(c);
		document.body.classList.add(`rollwright-skin-${skin}`);
		document.body.classList.toggle("theme-dark", donker);
		document.body.classList.toggle("theme-light", !donker);
	}, skin, donker);
	await browser.pause(300);
}

async function meet() {
	return browser.execute((sel) => {
		const rolls = Array.from(document.querySelectorAll(`${sel} .rollwright-roll`));
		const gewoon = rolls.find((r) => !r.classList.contains("rollwright-error"));
		const fout = rolls.find((r) => r.classList.contains("rollwright-error"));
		const alinea = document.querySelector(`${sel} p`);
		const stijl = (el) => (el ? { bg: getComputedStyle(el).backgroundColor, kleur: getComputedStyle(el).color, letter: getComputedStyle(el).fontFamily } : null);
		return { gewoon: stijl(gewoon), fout: stijl(fout), alinea: stijl(alinea) };
	}, LEAF);
}

describe("Rollwright: skins in licht en donker (Daan punt 5 en 8)", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.executeObsidian(async ({ app }) => {
			const file = app.vault.getAbstractFileByPath("Skins.md");
			if (!file) throw new Error("Skins.md niet gevonden");
			const leaf = app.workspace.getLeaf(false);
			await leaf.openFile(file, { state: { mode: "preview" } });
			app.workspace.setActiveLeaf(leaf, { focus: true });
		});
		await browser.waitUntil(async () => {
			const m = await meet();
			return m.gewoon !== null && m.fout !== null;
		}, { timeout: 15000, timeoutMsg: "geen gewone worp en geen fout in Skins.md" });
		// Daans ontwerp geeft een crit (in donker) bewust een eigen letterkleur, en een crit of fumble een eigen
		// achtergrond. Deze spec meet de skin, dus gooit hij opnieuw tot de gewone worp echt gewoon is.
		for (let poging = 0; poging < 20; poging++) {
			const bijzonder = await browser.execute((sel) => {
				const r = Array.from(document.querySelectorAll(`${sel} .rollwright-roll`)).find((x) => !x.classList.contains("rollwright-error"));
				const klassen = ["rollwright-crit", "rollwright-fumble", "rollwright-roll-max", "rollwright-roll-min"];
				if (!r || !klassen.some((k) => r.classList.contains(k))) return false;
				r.click();
				return true;
			}, LEAF);
			if (!bijzonder) break;
			console.log(`SKINS: gewone worp was een crit of fumble, opnieuw gegooid (poging ${poging + 1})`);
			await browser.pause(700);
		}
	});

	after(async function () {
		await zet("classic", false);
	});

	it("Parchment in licht blijft licht perkament", async function () {
		await zet("parchment", false);
		const m = await meet();
		console.log("PARCHMENT LICHT:", JSON.stringify(m));
		await browser.saveScreenshot(`${SHOTS}/skins-parchment-licht.png`);
		expect(m.gewoon.bg).toBe("rgb(239, 226, 192)");
		expect(m.gewoon.letter).toContain("Georgia");
	});

	it("Parchment in donker is donker perkament met lichte letters", async function () {
		await zet("parchment", true);
		const m = await meet();
		console.log("PARCHMENT DONKER:", JSON.stringify(m));
		await browser.saveScreenshot(`${SHOTS}/skins-parchment-donker.png`);
		expect(m.gewoon.bg).toBe("rgb(58, 47, 30)");
		expect(m.gewoon.kleur).toBe("rgb(240, 226, 192)");
		expect(m.gewoon.letter).toContain("Georgia");
	});

	it("een fout heeft in Parchment de letter van de tekst, net als in Classic", async function () {
		for (const donker of [false, true]) {
			await zet("parchment", donker);
			const p = await meet();
			await zet("classic", donker);
			const c = await meet();
			console.log(`FOUT ${donker ? "DONKER" : "LICHT"}: parchment ${p.fout.letter} / classic ${c.fout.letter} / alinea ${p.alinea.letter}`);
			expect(p.fout.letter).not.toContain("Georgia");
			expect(p.fout.letter).toBe(c.fout.letter);
		}
	});
});
