import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// Een notitie die op zichzelf rolt mag Obsidian niet laten vastlopen.
// In een uitkomst wordt geen nieuwe worp gezet (defuseRolls en de controle in reading-view.ts),
// dus het aantal worpen blijft gelijk aan het aantal codes in de notitie en groeit niet.
const SHOTS = "screenshots";
const LEAF = ".workspace-leaf.mod-active";

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

/** Telt de worpen in de actieve notitie, en hoeveel daarvan binnen een uitkomst staan. */
async function count(view) {
	return browser.execute((sel) => {
		const rolls = Array.from(document.querySelectorAll(`${sel} .rollwright-roll`));
		return {
			rolls: rolls.length,
			nested: document.querySelectorAll(`${sel} .rollwright-value .rollwright-roll`).length,
			errors: document.querySelectorAll(`${sel} .rollwright-error`).length,
			values: rolls.map((r) => (r.querySelector(".rollwright-value")?.textContent ?? "").replace(/​/g, "")),
		};
	}, `${LEAF} ${view}`);
}

/** Meet hoe snel Obsidian antwoordt: een vastgelopen venster antwoordt niet. */
async function answerTime() {
	const start = Date.now();
	await browser.executeObsidian(({ app }) => app.vault.getMarkdownFiles().length);
	return Date.now() - start;
}

async function waitForValue(view) {
	await browser.waitUntil(async () => {
		const c = await count(view);
		return c.rolls > 0 && c.values.every((v) => v.trim() !== "");
	}, { timeout: 20000, timeoutMsg: `geen uitkomst in ${view}` });
}

/** Opent de notitie, wacht op de uitkomst en kijkt na 3 seconden of er niets bij kwam. */
async function checkStable(path, mode, view, shot) {
	await openNote(path, mode);
	await waitForValue(view);
	const first = await count(view);
	await browser.pause(3000);
	const later = await count(view);
	const ms = await answerTime();
	console.log(`${path} (${mode}) EERST:`, JSON.stringify(first));
	console.log(`${path} (${mode}) NA 3 SECONDEN:`, JSON.stringify(later));
	console.log(`${path} (${mode}) OBSIDIAN ANTWOORDT IN MS:`, ms);
	await browser.saveScreenshot(`${SHOTS}/${shot}.png`);
	expect(later.rolls).toBe(first.rolls);
	expect(later.errors).toBe(0);
	expect(ms).toBeLessThan(5000);
	return later;
}

/** Vijf keer klikken: elke klik rendert de notitie opnieuw in de uitkomst. */
async function clickFive(view) {
	const before = await count(view);
	for (let i = 0; i < 5; i++) {
		await browser.execute((sel) => document.querySelector(`${sel} .rollwright-roll`)?.click(), `${LEAF} ${view}`);
		await browser.pause(400);
	}
	await browser.pause(1000);
	const after = await count(view);
	const ms = await answerTime();
	console.log("NA VIJF KLIKKEN:", JSON.stringify(after), "ANTWOORDT IN MS:", ms);
	expect(after.rolls).toBe(before.rolls);
	expect(after.nested).toBe(0);
	expect(after.errors).toBe(0);
	expect(ms).toBeLessThan(5000);
}

describe("Rollwright: een notitie die op zichzelf rolt", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
	});

	it("dice: [[Zichzelf]] in de leesweergave: één worp, de eigen code rolt niet nog eens", async function () {
		const c = await checkStable("Zichzelf.md", "preview", ".markdown-reading-view", "z1-zichzelf-lezen");
		expect(c.rolls).toBe(1);
		expect(c.nested).toBe(0);
		// De notitie heeft één blok, dus de uitkomst is die regel zelf, met de code als tekst.
		expect(c.values[0]).toContain("Ik rol op mezelf");
		expect(c.values[0]).toContain("Zichzelf");
	});

	it("klikken op dice: [[Zichzelf]] laat Obsidian niet vastlopen", async function () {
		await clickFive(".markdown-reading-view");
	});

	it("dice: [[Zichzelf]] in Live Preview: één worp, niets erbij", async function () {
		const c = await checkStable("Zichzelf.md", "source", ".markdown-source-view", "z2-zichzelf-live-preview");
		expect(c.rolls).toBe(1);
		expect(c.nested).toBe(0);
		await clickFive(".markdown-source-view");
	});

	it("dice: [[Zichzelf ingevoegd]] met ![[Zichzelf ingevoegd]] in dezelfde notitie", async function () {
		const c = await checkStable("Zichzelf ingevoegd.md", "preview", ".markdown-reading-view", "z3-zichzelf-ingevoegd");
		// De eigen code plus hoogstens wat Obsidian zelf invoegt; nooit iets binnen een uitkomst.
		expect(c.rolls).toBeGreaterThanOrEqual(1);
		expect(c.rolls).toBeLessThan(10);
		expect(c.nested).toBe(0);
		await clickFive(".markdown-reading-view");
	});

	it("dice: #npc in een notitie met die tag", async function () {
		const c = await checkStable("Npc.md", "preview", ".markdown-reading-view", "z4-tag-zichzelf");
		expect(c.rolls).toBe(1);
		expect(c.nested).toBe(0);
		expect(c.values[0]).toContain("eigen tag");
		await clickFive(".markdown-reading-view");
	});
});
