import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// dice-mod: in de echte Obsidian. Een klik (of Enter) rolt niet opnieuw maar opent een venster
// met de tekst die in de notitie komt. Replace schrijft die tekst in plaats van de code.
// Elke test die het bestand verandert heeft een eigen notitie, zodat de tests elkaar niet raken.
// Het venster komt uit src/ui/dice-mod.ts (ReplaceCodeModal): titel "Replace the dice code?",
// de tekst in <pre><code>, knoppen "Cancel" en "Replace".
const SHOTS = "screenshots";
const LEAF = ".workspace-leaf.mod-active";
const ZWS = String.fromCharCode(0x200b);
const TITEL = "Replace the dice code?";
const CODE = "`dice-mod: 3d100 + 12`";
const VORM = /^3d100 \+ 12 -> \[(\d+), (\d+), (\d+)\] \+ 12 -> (\d+)$/;
// Met de instelling diceModFormula uit (src/main.ts, RollwrightSettings) valt de formule weg.
const VORM_ZONDER = /^\[(\d+), (\d+), (\d+)\] \+ 12 -> (\d+)$/;
// De codes en de notities staan bewust zo dat de vervangtekst geen backslash krijgt
// (src/rollers/modify.ts, fitReplacement): geen backtick of | in de uitkomst, geen tabelregel,
// en "Worp: " of "Kleur: " voor de code, zodat hij niet aan het begin van een regel staat.
// Zo is de tekst in het bestand precies de tekst uit het venster.

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
				old: value?.getAttribute("data-e2e-oud") === "1",
				error: r.getAttribute("data-rollwright-error") ?? "",
			};
		}), `${LEAF} ${view}`, ZWS);
}

async function waitForRolls(view, n) {
	let last = [];
	await browser.waitUntil(async () => {
		last = await readRolls(view);
		return last.length === n && last.every((r) => r.value !== "" || r.error !== "");
	}, { timeout: 20000, timeoutMsg: `geen ${n} uitkomsten in ${view}` }).catch((e) => {
		console.log("WORPEN TOT NU:", JSON.stringify(last));
		throw e;
	});
	for (const r of last) expect(r.error).toBe("");
	return last;
}

/** Zet een merkteken op de uitkomst van worp i, zodat te zien is of er een nieuwe komt. */
async function markeer(view, i) {
	await browser.execute((sel, i) => {
		document.querySelectorAll(`${sel} .rollwright-roll`)[i]?.querySelector(".rollwright-value")?.setAttribute("data-e2e-oud", "1");
	}, `${LEAF} ${view}`, i);
}

async function klik(view, i) {
	await browser.execute((sel, i) => {
		document.querySelectorAll(`${sel} .rollwright-roll`)[i]?.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true }));
	}, `${LEAF} ${view}`, i);
}

/** Het open vervangvenster van Rollwright, of null. */
async function readVenster() {
	return browser.execute((titel) => {
		const container = Array.from(document.querySelectorAll(".modal-container"))
			.find((c) => (c.querySelector(".modal-title")?.textContent ?? "").trim() === titel);
		if (!container) return null;
		return {
			titel: (container.querySelector(".modal-title")?.textContent ?? "").trim(),
			tekst: container.querySelector("pre code")?.textContent ?? null,
			knoppen: Array.from(container.querySelectorAll("button")).map((b) => (b.textContent ?? "").trim()),
			cta: (container.querySelector("button.mod-cta")?.textContent ?? "").trim(),
		};
	}, TITEL);
}

async function waitForVenster() {
	let venster = null;
	await browser.waitUntil(async () => {
		venster = await readVenster();
		return venster !== null && venster.tekst !== null;
	}, { timeout: 10000, timeoutMsg: "het vervangvenster ging niet open" });
	console.log("VENSTER:", JSON.stringify(venster));
	expect(venster.knoppen).toContain("Cancel");
	expect(venster.knoppen).toContain("Replace");
	return venster;
}

async function waitVensterDicht() {
	await browser.waitUntil(async () => (await readVenster()) === null, { timeout: 10000, timeoutMsg: "het vervangvenster bleef open" });
}

async function knop(tekst) {
	const gevonden = await browser.execute((titel, tekst) => {
		const container = Array.from(document.querySelectorAll(".modal-container"))
			.find((c) => (c.querySelector(".modal-title")?.textContent ?? "").trim() === titel);
		const button = Array.from(container?.querySelectorAll("button") ?? []).find((b) => (b.textContent ?? "").trim() === tekst);
		button?.click();
		return button !== undefined;
	}, TITEL, tekst);
	expect(gevonden).toBe(true);
}

/** De inhoud van een notitie zoals hij op schijf staat. */
async function leesBestand(path) {
	return browser.executeObsidian(async ({ app }, path) => {
		const file = app.vault.getAbstractFileByPath(path);
		if (!file) throw new Error(`notitie ${path} niet gevonden`);
		return app.vault.read(file);
	}, path);
}

/** Wacht tot de notitie op schijf deze inhoud heeft. Live Preview bewaart pas na een korte tijd. */
async function waitForBestand(path, verwacht, wat, bewaar = true) {
	let last = null;
	// Alleen in Live Preview: daar staat de wijziging eerst in de editor. In de leesweergave schrijft
	// de plugin zelf naar schijf, en een save van de view zou oude tekst kunnen terugschrijven.
	if (bewaar) {
		await browser.executeObsidian(async ({ app }) => {
			await app.workspace.activeLeaf?.view?.save?.();
		});
	}
	await browser.waitUntil(async () => {
		last = await leesBestand(path);
		return last === verwacht;
	}, { timeout: 15000, timeoutMsg: `${path} kreeg niet de verwachte inhoud (${wat})` }).catch((e) => {
		console.log(`${path} NU:`, JSON.stringify(last));
		console.log(`${path} VERWACHT:`, JSON.stringify(verwacht));
		throw e;
	});
	return last;
}

/** Controleert de vorm van de tekst en dat het totaal de som plus 12 is. */
function checkVorm(tekst, vorm = VORM) {
	const m = vorm.exec(tekst);
	console.log("VORM:", JSON.stringify(tekst), "past:", m !== null);
	expect(m).not.toBe(null);
	const stenen = [m[1], m[2], m[3]].map(Number);
	for (const s of stenen) {
		expect(s).toBeGreaterThanOrEqual(1);
		expect(s).toBeLessThanOrEqual(100);
	}
	const som = stenen.reduce((a, b) => a + b, 0);
	console.log("STENEN:", JSON.stringify(stenen), "SOM + 12:", som + 12, "TOTAAL:", m[4]);
	expect(Number(m[4])).toBe(som + 12);
	return Number(m[4]);
}

/** De laatste worp in de geschiedenis van Rollwright, als tekst. */
async function laatsteWorp() {
	return browser.executeObsidian(({ app }) => JSON.stringify(app.plugins.plugins.rollwright?.settings?.history?.[0] ?? null));
}

/**
 * Leest het bestand steeds opnieuw, zo lang als ms, en eist dat het gelijk blijft.
 * Zo valt ook een schrijfactie op die pas even later komt.
 */
async function blijftGelijk(path, voor, ms = 1000) {
	const start = Date.now();
	let afwijking = null;
	let keer = 0;
	await browser.waitUntil(async () => {
		const nu = await leesBestand(path);
		keer++;
		if (nu !== voor) {
			afwijking = nu;
			return true;
		}
		return Date.now() - start >= ms;
	}, { timeout: ms + 10000, interval: 100, timeoutMsg: `${path} kon niet gelezen worden` });
	console.log(`${path} ${keer} keer gelezen in ${Date.now() - start} ms, afwijking:`, JSON.stringify(afwijking));
	expect(afwijking).toBe(null);
}

/** Klikt op de enige worp, kiest Replace en geeft de tekst uit het venster terug. */
async function vervang(view, path, shot, vorm = VORM) {
	const voor = await leesBestand(path);
	console.log(`${path} VOOR:`, JSON.stringify(voor));
	expect(voor).toContain(CODE);
	const rolls = await waitForRolls(view, 1);
	console.log("WORP VOOR KLIK:", JSON.stringify(rolls));
	await markeer(view, 0);
	await klik(view, 0);
	const venster = await waitForVenster();
	await browser.saveScreenshot(`${SHOTS}/${shot}`);
	// Een klik rolt niet opnieuw: de uitkomst is nog dezelfde, en het totaal in het venster is wat er staat.
	const na = await readRolls(view);
	expect(na[0].old).toBe(true);
	expect(na[0].value).toBe(rolls[0].value);
	const totaal = checkVorm(venster.tekst, vorm);
	expect(String(totaal)).toBe(rolls[0].value);
	await knop("Replace");
	await waitVensterDicht();
	const verwacht = voor.replace(CODE, venster.tekst);
	const bestand = await waitForBestand(path, verwacht, "na Replace", view === ".markdown-source-view");
	console.log(`${path} NA:`, JSON.stringify(bestand));
	expect(bestand.includes(CODE)).toBe(false);
	return { voor, na: bestand, tekst: venster.tekst };
}

describe("Rollwright: dice-mod met Replace in de echte Obsidian", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
	});

	afterEach(async function () {
		// Een venster dat open bleef na een mislukte test mag de volgende niet raken.
		if ((await readVenster()) !== null) {
			await browser.keys(["Escape"]);
			await browser.pause(300);
		}
	});

	it("Live Preview: Replace schrijft precies de tekst uit het venster, de rest blijft gelijk", async function () {
		await openNote("Vervangen.md", "source");
		const { voor, na, tekst } = await vervang(".markdown-source-view", "Vervangen.md", "m1-venster-live-preview.png");
		// Alleen de code (met backticks) is vervangen; de regels ervoor en erna zijn gelijk.
		const i = voor.indexOf(CODE);
		expect(na.slice(0, i)).toBe(voor.slice(0, i));
		expect(na.slice(i + tekst.length)).toBe(voor.slice(i + CODE.length));
		const editor = await browser.executeObsidian(({ app }) => app.workspace.activeEditor?.editor?.getValue() ?? null);
		expect(editor).toBe(na);
		await browser.saveScreenshot(`${SHOTS}/m2-na-replace-live-preview.png`);
	});

	it("Live Preview: Ctrl-Z zet de code terug", async function () {
		await openNote("Ongedaan.md", "source");
		const { voor } = await vervang(".markdown-source-view", "Ongedaan.md", "m3-venster-ongedaan.png");
		// Een echte toets: de editor krijgt de focus en Obsidian moet Ctrl-Z zelf als ongedaan maken lezen.
		const gefocust = await browser.executeObsidian(({ app }, sel) => {
			app.workspace.activeEditor?.editor?.focus();
			return document.activeElement?.closest(`${sel} .cm-content`) !== null && document.activeElement !== null;
		}, LEAF);
		console.log("EDITOR GEFOCUST:", gefocust, "EDITOR NU:", JSON.stringify(await browser.executeObsidian(({ app }) => app.workspace.activeEditor?.editor?.getValue() ?? null)));
		expect(gefocust).toBe(true);
		await browser.keys(["Control", "z"]);
		const terug = await waitForBestand("Ongedaan.md", voor, "na Ctrl-Z");
		console.log("Ongedaan.md NA CTRL-Z:", JSON.stringify(terug));
		expect(terug).toContain(CODE);
		// De code toont weer een worp.
		await waitForRolls(".markdown-source-view", 1);
		await browser.saveScreenshot(`${SHOTS}/m4-na-ctrl-z.png`);
	});

	it("Cancel en Escape laten het bestand gelijk", async function () {
		await openNote("Annuleren.md", "source");
		const voor = await leesBestand("Annuleren.md");
		console.log("Annuleren.md VOOR:", JSON.stringify(voor));
		const rolls = await waitForRolls(".markdown-source-view", 1);
		const historieVoor = await laatsteWorp();
		await markeer(".markdown-source-view", 0);

		await klik(".markdown-source-view", 0);
		await waitForVenster();
		await knop("Cancel");
		await waitVensterDicht();

		await klik(".markdown-source-view", 0);
		await waitForVenster();
		await browser.saveScreenshot(`${SHOTS}/m5-venster-voor-escape.png`);
		await browser.keys(["Escape"]);
		await waitVensterDicht();

		// Bewaar wat de editor heeft, en lees dan een seconde lang steeds het bestand: het blijft gelijk.
		await browser.executeObsidian(async ({ app }) => {
			await app.workspace.activeLeaf?.view?.save?.();
		});
		await blijftGelijk("Annuleren.md", voor);
		const na = await leesBestand("Annuleren.md");
		console.log("Annuleren.md NA:", JSON.stringify(na));
		expect(na).toBe(voor);
		// Geen nieuwe worp: hetzelfde element met merkteken, dezelfde uitkomst, niets nieuws in de geschiedenis.
		const rollsNa = await readRolls(".markdown-source-view");
		console.log("WORP VOOR EN NA:", JSON.stringify(rolls[0]), JSON.stringify(rollsNa[0]));
		expect(rollsNa.length).toBe(1);
		expect(rollsNa[0].old).toBe(true);
		expect(rollsNa[0].value).toBe(rolls[0].value);
		const historieNa = await laatsteWorp();
		console.log("LAATSTE WORP IN GESCHIEDENIS VOOR EN NA:", historieVoor, historieNa);
		expect(historieNa).toBe(historieVoor);
		const editor = await browser.executeObsidian(({ app }) => app.workspace.activeEditor?.editor?.getValue() ?? null);
		expect(editor).toBe(voor);
		await waitForRolls(".markdown-source-view", 1);
	});

	it("Live Preview zonder formule: Replace schrijft alleen uitkomst en totaal", async function () {
		// De instelling heet diceModFormula (src/main.ts, regel 35; src/ui/settings.ts, regel 126-127).
		// Alleen in het geheugen uit, niet op schijf; de plugin leest hem bij de klik (src/ui/dice-mod.ts).
		const eerst = await browser.executeObsidian(({ app }) => {
			const plugin = app.plugins.plugins.rollwright;
			const oud = plugin.settings.diceModFormula;
			plugin.settings.diceModFormula = false;
			return oud;
		});
		console.log("diceModFormula WAS:", eerst);
		try {
			await openNote("Zonder formule.md", "source");
			const { na, tekst } = await vervang(".markdown-source-view", "Zonder formule.md", "m10-venster-zonder-formule.png", VORM_ZONDER);
			expect(na).toContain(`Worp: ${tekst} en dan verder.`);
			expect(na.includes("3d100")).toBe(false);
		} finally {
			await browser.executeObsidian(({ app }, oud) => {
				app.plugins.plugins.rollwright.settings.diceModFormula = oud;
			}, eerst);
		}
	});

	it("Leesweergave: Replace verandert het bestand direct", async function () {
		await openNote("Vervangen lezen.md", "preview");
		const { na } = await vervang(".markdown-reading-view", "Vervangen lezen.md", "m6-venster-lezen.png");
		expect(na).toContain("Worp: 3d100 + 12 -> [");
		await browser.saveScreenshot(`${SHOTS}/m7-na-replace-lezen.png`);
	});

	it("dice-mod op een tabel schrijft alleen de uitkomst, en Tabellen.md blijft gelijk", async function () {
		const tabelVoor = await browser.executeObsidian(async ({ app }) => {
			const stat = await app.vault.adapter.stat("Tabellen.md");
			return { tekst: await app.vault.adapter.read("Tabellen.md"), mtime: stat?.mtime ?? null, size: stat?.size ?? null };
		});
		console.log("Tabellen.md VOOR: grootte", tabelVoor.size, "mtime", tabelVoor.mtime);
		await openNote("Tabel vervangen.md", "source");
		const path = "Tabel vervangen.md";
		const code = "`dice-mod: [[Tabellen^kleuren]]`";
		const voor = await leesBestand(path);
		console.log(`${path} VOOR:`, JSON.stringify(voor));
		const rolls = await waitForRolls(".markdown-source-view", 1);
		console.log("TABELWORP:", JSON.stringify(rolls));
		await klik(".markdown-source-view", 0);
		const venster = await waitForVenster();
		await browser.saveScreenshot(`${SHOTS}/m8-venster-tabel.png`);
		// Alleen de uitkomst, één kleur uit de tabel, zonder formule of pijl.
		expect(["Rood", "Blauw", "Groen"]).toContain(venster.tekst);
		expect(venster.tekst).toBe(rolls[0].value);
		await knop("Replace");
		await waitVensterDicht();
		const na = await waitForBestand(path, voor.replace(code, venster.tekst), "na Replace op tabel");
		console.log(`${path} NA:`, JSON.stringify(na));
		const regel = na.split("\n").find((r) => r.startsWith("Kleur: "));
		expect(regel).toBe(`Kleur: ${venster.tekst} en dan verder.`);
		expect(na.split("\n").length).toBe(voor.split("\n").length);
		const tabelNa = await browser.executeObsidian(async ({ app }) => {
			const stat = await app.vault.adapter.stat("Tabellen.md");
			return { tekst: await app.vault.adapter.read("Tabellen.md"), mtime: stat?.mtime ?? null, size: stat?.size ?? null };
		});
		console.log("Tabellen.md NA: grootte", tabelNa.size, "mtime", tabelNa.mtime);
		expect(tabelNa.tekst).toBe(tabelVoor.tekst);
		expect(tabelNa.size).toBe(tabelVoor.size);
		expect(tabelNa.mtime).toBe(tabelVoor.mtime);
	});

	it("Enter op de gefocuste worp rolt niet opnieuw maar opent het venster", async function () {
		// src/ui/widget.ts: een keydown met Enter roept dezelfde handeling aan als een klik.
		// In de leesweergave, zodat de editor de toets niet als nieuwe regel kan lezen.
		await openNote("Enter.md", "preview");
		const view = ".markdown-reading-view";
		const voor = await leesBestand("Enter.md");
		console.log("Enter.md VOOR:", JSON.stringify(voor));
		const rolls = await waitForRolls(view, 1);
		const historieVoor = await laatsteWorp();
		await markeer(view, 0);
		const focus = await browser.execute((sel) => {
			const el = document.querySelector(`${sel} .rollwright-roll`);
			el?.focus();
			return document.activeElement === el;
		}, `${LEAF} ${view}`);
		console.log("WORP GEFOCUST:", focus);
		expect(focus).toBe(true);
		await browser.keys(["Enter"]);
		await browser.pause(300);
		const venster = await waitForVenster();
		await browser.saveScreenshot(`${SHOTS}/m9-venster-enter.png`);
		const na = await readRolls(view);
		console.log("WORP VOOR EN NA ENTER:", JSON.stringify(rolls[0]), JSON.stringify(na[0]));
		expect(na[0].old).toBe(true);
		expect(na[0].value).toBe(rolls[0].value);
		expect(String(checkVorm(venster.tekst))).toBe(rolls[0].value);
		const historieNa = await laatsteWorp();
		console.log("LAATSTE WORP IN GESCHIEDENIS VOOR EN NA:", historieVoor, historieNa);
		expect(historieNa).toBe(historieVoor);
		await knop("Cancel");
		await waitVensterDicht();
		const bestand = await leesBestand("Enter.md");
		console.log("Enter.md NA:", JSON.stringify(bestand));
		expect(bestand).toBe(voor);
	});
});
