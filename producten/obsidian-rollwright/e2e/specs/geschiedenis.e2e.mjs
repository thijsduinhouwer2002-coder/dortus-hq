import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// Bewaart de geschiedenis dezelfde worp als de notitie laat zien? In de echte Obsidian.
// Geschiedenis.md heeft vier codes: een groot getal, een worp met label, een tabelworp op
// Namen.md (20 namen) en nog een gewone worp. Na elke klik moet de nieuwste regel in de
// geschiedenis (de instellingen en het paneel) gelijk zijn aan wat de notitie toont.
const SHOTS = "screenshots";
const LEAF = ".workspace-leaf.mod-active";
const PANEEL = '.workspace-leaf-content[data-type="rollwright-history"]';
const NOTITIE = "Geschiedenis.md";
const AANTAL = 4;
const ZWS = String.fromCharCode(0x200b);

async function openNote(path, mode) {
	await browser.executeObsidian(async ({ app }, path, mode) => {
		const file = app.vault.getAbstractFileByPath(path);
		if (!file) throw new Error(`notitie ${path} niet gevonden`);
		const leaf = app.workspace.getLeaf(false);
		const state = mode === "preview" ? { mode: "preview" } : { mode: "source", source: false };
		await leaf.openFile(file, { state });
		app.workspace.setActiveLeaf(leaf, { focus: true });
	}, path, mode);
}

async function readRolls(view) {
	return browser.execute((sel, zws) => Array.from(document.querySelectorAll(`${sel} .rollwright-roll`))
		.filter((r) => !r.parentElement?.closest(".rollwright-roll"))
		.map((r) => {
			const value = r.querySelector(".rollwright-value");
			return {
				value: (value?.textContent ?? "").split(zws).join("").trim(),
				label: (r.querySelector(".rollwright-label")?.textContent ?? "").trim(),
				old: value?.getAttribute("data-e2e-oud") === "1",
				error: r.getAttribute("data-rollwright-error") ?? "",
			};
		}), `${LEAF} ${view}`, ZWS);
}

async function waitForRolls(view, n) {
	let last = [];
	await browser.waitUntil(async () => {
		last = await readRolls(view);
		return last.length >= n && last.every((r) => r.value !== "" || r.error !== "");
	}, { timeout: 20000, timeoutMsg: `geen ${n} uitkomsten in ${view}` }).catch((e) => {
		console.log("WORPEN TOT NU:", JSON.stringify(last));
		throw e;
	});
	return last;
}

/** De geschiedenis zoals de plugin hem bewaart, nieuwste eerst. */
async function history() {
	return browser.executeObsidian(({ app }) => (app.plugins.plugins.rollwright?.settings?.history ?? []).map((h) => ({ result: h.result, formula: h.formula, source: h.source })));
}

/** Wat het geschiedenispaneel toont, nieuwste eerst. */
async function paneel() {
	return browser.execute((sel) => Array.from(document.querySelectorAll(`${sel} .rollwright-history-item`)).map((item) => ({
		result: (item.querySelector(".rollwright-history-result")?.textContent ?? "").trim(),
		formula: (item.querySelector(".rollwright-history-formula")?.textContent ?? "").trim(),
	})), PANEEL);
}

async function maakLeegEnOpenPaneel() {
	await browser.executeObsidian(async ({ app }) => {
		const plugin = app.plugins.plugins.rollwright;
		await plugin.clearHistory();
		await plugin.openHistory();
	});
	await browser.waitUntil(async () => browser.execute((sel) => document.querySelector(`${sel} .rollwright-history-empty`) !== null, PANEEL), {
		timeout: 5000, timeoutMsg: "het geschiedenispaneel toont geen lege geschiedenis",
	});
	expect((await history()).length).toBe(0);
}

/** Klik op worp i zoals de andere specs, en wacht tot er een nieuwe uitkomst staat. */
async function klik(view, i) {
	await browser.execute((sel, i) => {
		document.querySelectorAll(`${sel} .rollwright-roll`)[i]?.querySelector(".rollwright-value")?.setAttribute("data-e2e-oud", "1");
	}, `${LEAF} ${view}`, i);
	const aantalVoor = (await history()).length;
	await browser.execute((sel, i) => document.querySelectorAll(`${sel} .rollwright-roll`)[i]?.click(), `${LEAF} ${view}`, i);
	let rolls = [];
	await browser.waitUntil(async () => {
		rolls = await readRolls(view);
		return rolls[i] !== undefined && !rolls[i].old && rolls[i].value !== "";
	}, { timeout: 5000, timeoutMsg: `na een klik op worp ${i} kwam er geen nieuwe uitkomst` });
	// De geschiedenis wordt na de worp bewaard; wacht tot de nieuwe regel er is en het paneel hem toont.
	await browser.waitUntil(async () => {
		const h = await history();
		const p = await paneel();
		return h.length === aantalVoor + 1 && p.length === h.length;
	}, { timeout: 5000, timeoutMsg: `na een klik op worp ${i} kwam er geen nieuwe regel in de geschiedenis` });
	expect(rolls[i].error).toBe("");
	return rolls[i];
}

async function vergelijk(view, wat) {
	const formules = [];
	for (let i = 0; i < AANTAL; i++) {
		const getoond = await klik(view, i);
		const [nieuwste] = await history();
		const [inPaneel] = await paneel();
		console.log(`GESCHIEDENIS: notitie=${JSON.stringify(getoond.value)} geschiedenis=${JSON.stringify(nieuwste.result)} paneel=${JSON.stringify(inPaneel.result)} formule=${JSON.stringify(nieuwste.formula)} label=${JSON.stringify(getoond.label)} (${wat}, worp ${i})`);
		expect(nieuwste.result).toBe(getoond.value);
		expect(inPaneel.result).toBe(getoond.value);
		expect(inPaneel.formula).toBe(nieuwste.formula);
		expect(nieuwste.source).toBe(NOTITIE);
		formules.push(nieuwste.formula);
	}
	console.log(`FORMULES IN DE GESCHIEDENIS (${wat}):`, JSON.stringify(formules));
	expect(formules[0]).toBe("1d1000000");
	expect(formules[1]).toContain("1d20 + 5");
	expect(formules[2]).toContain("Namen^namen");
	expect(formules[3]).toBe("2d6 + 3");
	// Na vier klikken staan de vier worpen in de geschiedenis, nieuwste boven.
	const h = await history();
	expect(h.map((x) => x.formula).reverse()).toEqual(formules);
}

async function vierKeer(view, wat) {
	const getoond = [];
	// Worp 2 is de tabelworp: 20 namen, dus vier keer dezelfde naam valt meteen op.
	for (let k = 0; k < 4; k++) getoond.push((await klik(view, 2)).value);
	const boven = (await history()).slice(0, 4).map((x) => x.result);
	const inPaneel = (await paneel()).slice(0, 4).map((x) => x.result);
	console.log(`GESCHIEDENIS VIER KEER (${wat}): notitie=${JSON.stringify(getoond)} geschiedenis=${JSON.stringify(boven)} paneel=${JSON.stringify(inPaneel)}`);
	expect([...boven].reverse()).toEqual(getoond);
	expect([...inPaneel].reverse()).toEqual(getoond);
}

describe("Rollwright: de geschiedenis bewaart de worp die de notitie toont", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
	});

	it("in de leesweergave, elke code apart", async function () {
		await maakLeegEnOpenPaneel();
		await openNote(NOTITIE, "preview");
		const rolls = await waitForRolls(".markdown-reading-view", AANTAL);
		console.log("GESCHIEDENIS.MD LEZEN:", JSON.stringify(rolls));
		expect(rolls.length).toBe(AANTAL);
		await vergelijk(".markdown-reading-view", "lezen");
		await browser.saveScreenshot(`${SHOTS}/g1-geschiedenis-lezen.png`);
	});

	it("in de leesweergave, vier keer dezelfde code", async function () {
		await vierKeer(".markdown-reading-view", "lezen");
		await browser.saveScreenshot(`${SHOTS}/g2-geschiedenis-vier-keer-lezen.png`);
	});

	it("in Live Preview, elke code apart", async function () {
		await maakLeegEnOpenPaneel();
		await openNote(NOTITIE, "source");
		const rolls = await waitForRolls(".markdown-source-view", AANTAL);
		console.log("GESCHIEDENIS.MD LIVE PREVIEW:", JSON.stringify(rolls));
		expect(rolls.length).toBe(AANTAL);
		await vergelijk(".markdown-source-view", "live preview");
		await browser.saveScreenshot(`${SHOTS}/g3-geschiedenis-live-preview.png`);
	});

	it("in Live Preview, vier keer dezelfde code", async function () {
		await vierKeer(".markdown-source-view", "live preview");
		await browser.saveScreenshot(`${SHOTS}/g4-geschiedenis-vier-keer-live-preview.png`);
	});
});
