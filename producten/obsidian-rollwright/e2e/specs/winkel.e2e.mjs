import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// Winkelplaatjes voor README en lancering: een Engelse demonotitie zonder testnamen in beeld.
// Plaatjes: winkel-*.png (licht en donker), via de workflow naar tak `schermen`. Daan keurt ze.
const SHOTS = "screenshots";
const NOTE = "Demo/Session 12.md";
const LEAF = ".workspace-leaf.mod-active";
const AANTAL = 5;

async function open(mode) {
	await browser.executeObsidian(async ({ app }, path, mode) => {
		const file = app.vault.getAbstractFileByPath(path);
		if (!file) throw new Error(`notitie ${path} niet gevonden`);
		const leaf = app.workspace.getLeaf(false);
		const state = mode === "preview" ? { mode: "preview" } : { mode: "source", source: false };
		await leaf.openFile(file, { state });
		app.workspace.setActiveLeaf(leaf, { focus: true });
	}, NOTE, mode);
}

async function worpen(view) {
	return browser.execute((sel) => Array.from(document.querySelectorAll(`${sel} .rollwright-roll`))
		.filter((r) => !r.parentElement?.closest(".rollwright-roll"))
		.map((r) => ({ tekst: (r.textContent ?? "").trim(), fout: r.getAttribute("data-rollwright-error") ?? "" })), `${LEAF} ${view}`);
}

async function wacht(view) {
	let w = [];
	await browser.waitUntil(async () => {
		w = await worpen(view);
		return w.length >= AANTAL && w.every((r) => r.tekst !== "");
	}, { timeout: 20000, timeoutMsg: `geen ${AANTAL} uitkomsten in ${view}` }).catch((e) => {
		console.log("WORPEN TOT NU:", JSON.stringify(w));
		throw e;
	});
	return w;
}

async function thema(donker) {
	await browser.execute((donker) => {
		document.body.classList.toggle("theme-dark", donker);
		document.body.classList.toggle("theme-light", !donker);
	}, donker);
	await browser.pause(300);
}

async function plaatjes(naam) {
	await thema(false);
	await browser.saveScreenshot(`${SHOTS}/${naam}.png`);
	await thema(true);
	await browser.saveScreenshot(`${SHOTS}/${naam}-donker.png`);
	await thema(false);
}

describe("Rollwright: winkelplaatjes", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		// Linker zijpaneel dicht: dan staan de testnotities niet in beeld.
		await browser.executeObsidian(({ app }) => app.workspace.leftSplit?.collapse());
	});

	it("leesweergave met worpen, tabel en lijst", async function () {
		await open("preview");
		const w = await wacht(".markdown-reading-view");
		console.log("WINKEL LEZEN:", JSON.stringify(w));
		for (const r of w) expect(r.fout).toBe("");
		expect(w[4].tekst.split(",").length).toBe(3);
		await plaatjes("winkel-1-lezen");
	});

	it("Live Preview hetzelfde", async function () {
		await open("source");
		const w = await wacht(".markdown-source-view");
		console.log("WINKEL LIVE PREVIEW:", JSON.stringify(w));
		for (const r of w) expect(r.fout).toBe("");
		await plaatjes("winkel-2-live-preview");
	});

	it("geschiedenis rechts na een paar klikken", async function () {
		await open("preview");
		await wacht(".markdown-reading-view");
		// Het paneel openen maakt het paneel actief; daarna de notitie weer actief, anders vindt LEAF geen worpen.
		await browser.executeObsidian(async ({ app }) => {
			const note = app.workspace.getMostRecentLeaf();
			await app.plugins.plugins.rollwright.openHistory();
			if (note) app.workspace.setActiveLeaf(note, { focus: true });
		});
		await browser.waitUntil(async () => browser.execute(() => document.querySelector('.workspace-leaf-content[data-type="rollwright-history"]') !== null),
			{ timeout: 5000, timeoutMsg: "het geschiedenispaneel opende niet" });
		for (const i of [0, 2, 1, 3]) {
			await browser.execute((sel, i) => document.querySelectorAll(`${sel} .rollwright-roll`)[i]?.click(), `${LEAF} .markdown-reading-view`, i);
			await browser.pause(300);
		}
		let items = 0;
		await browser.waitUntil(async () => {
			items = await browser.execute(() => document.querySelectorAll(".rollwright-history-item").length);
			return items >= 4;
		}, { timeout: 5000 }).catch(() => {});
		console.log("WINKEL GESCHIEDENIS ITEMS:", items);
		expect(items).toBeGreaterThanOrEqual(4);
		await plaatjes("winkel-3-geschiedenis");
	});
});
