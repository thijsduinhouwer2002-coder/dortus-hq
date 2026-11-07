import { browser, expect } from "@wdio/globals";
import * as fs from "fs";
import { klikWorp } from "./klik-hulp.mjs";

// Worpen op blokken (secties) en regels van een andere notitie, in de echte Obsidian.
// Sectiewerpen.md rolt op Bron.md. Elk blok in Bron.md heeft een eigen woord, zodat te zien is
// welk blok of welke regel er kwam.
const SHOTS = "screenshots";
const LEAF = ".workspace-leaf.mod-active";
const ZWS = String.fromCharCode(0x200b);

// Blokken van Bron.md zoals de plugin ze ziet: frontmatter en de horizontale lijn tellen niet mee.
const BLOKKEN = {
	kop1: ["Alfa"],
	alinea1: ["Bravo"],
	kop2: ["Charlie"],
	alinea2: ["Delta"],
	lijst: ["Foxtrot", "Golf"],
	alinea3: ["Hotel", "India"],
};
const ALINEAS = ["alinea1", "alinea2", "alinea3"];
const ALLE_WOORDEN = Object.values(BLOKKEN).flat();
const NOOIT = ["Geheimyaml", "soort"];

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
				hr: value?.querySelector("hr") !== null && value !== null,
				nested: value?.querySelectorAll(".rollwright-roll").length ?? 0,
				codes: Array.from(value?.querySelectorAll("code") ?? []).map((c) => (c.textContent ?? "").split(zws).join("")),
				paragraphs: value?.querySelectorAll("p").length ?? 0,
			};
		}), `${LEAF} ${view}`, ZWS);
}

async function waitForRolls(view, n) {
	let last = [];
	await browser.waitUntil(async () => {
		last = await readRolls(view);
		return last.length >= n && last.every((r) => r.value !== "" || r.error !== "" || r.hr);
	}, { timeout: 20000, timeoutMsg: `geen ${n} uitkomsten in ${view}` }).catch((e) => {
		console.log("WORPEN TOT NU:", JSON.stringify(last));
		throw e;
	});
	return last;
}

/** Welke woorden van Bron.md staan in de tekst. */
function woorden(text) {
	return ALLE_WOORDEN.filter((w) => text.includes(w));
}

/** Klopt de tekst met precies één blok uit de lijst? Geeft de naam van dat blok. */
function eenBlok(text, toegestaan) {
	const gezien = woorden(text);
	return toegestaan.find((naam) => {
		const w = BLOKKEN[naam];
		return w.every((x) => gezien.includes(x)) && gezien.every((x) => w.includes(x));
	});
}

/** Hoe vaak elk woord voorkomt: twee keer dezelfde regel trekken mag (met teruglegging, zoals bij tabellen). */
function woordenGeteld(text) {
	return ALLE_WOORDEN.flatMap((w) => Array(text.split(w).length - 1).fill(w));
}

function checkRegel(r, aantal, wat) {
	const gezien = woordenGeteld(r.value);
	// Een losse lijn (***) telt sinds 7 nov niet meer als regel: een regelworp toont nooit een lijn.
	console.log(`${wat}: woorden ${JSON.stringify(gezien)}, lijn ${r.hr}`);
	expect(r.hr).toBe(false);
	expect(gezien.length).toBe(aantal);
}

const AANTAL = 10;

function check(rolls) {
	expect(rolls.length).toBe(AANTAL);
	// De laatste worp verwijst naar een block id dat niet bestaat: die moet een fout geven.
	const fout = rolls[9];
	console.log("FOUT BIJ ^bestaatniet:", JSON.stringify(fout.error));
	expect(fout.error).toContain("bestaatniet");
	for (const r of rolls.slice(0, 9)) {
		expect(r.error).toBe("");
		for (const n of NOOIT) expect(r.value.includes(n)).toBe(false);
		// Een code in een getrokken blok rolt niet opnieuw.
		expect(r.nested).toBe(0);
	}
	const [blok, alinea, kop2, regel, vast, tweeRegels, tweeAlineas, lijstpunt, kop1] = rolls;

	const b = eenBlok(blok.value, Object.keys(BLOKKEN));
	console.log("BLOK:", b, JSON.stringify(blok.value));
	expect(b).not.toBe(undefined);
	expect(blok.hr).toBe(false);

	const a = eenBlok(alinea.value, ALINEAS);
	console.log("ALINEA:", a);
	expect(a).not.toBe(undefined);

	expect(eenBlok(kop2.value, ["kop2"])).toBe("kop2");

	checkRegel(regel, 1, "REGEL");
	// Een regel is één regel: van de alinea Hotel/India komt nooit alles tegelijk.
	expect(regel.value.includes("Hotel") && regel.value.includes("India")).toBe(false);

	expect(eenBlok(vast.value, ["alinea2"])).toBe("alinea2");
	console.log("CODES IN VAST BLOK:", JSON.stringify(vast.codes));
	expect(vast.codes).toContain("dice: 1d6");

	checkRegel(tweeRegels, 2, "TWEE REGELS");

	// Twee alinea's: elk woord hoort bij een alinea, en er zijn twee <p> in de uitkomst.
	const tw = woorden(tweeAlineas.value);
	console.log("TWEE ALINEA'S:", JSON.stringify(tw), "p:", tweeAlineas.paragraphs);
	for (const w of tw) expect(ALINEAS.some((n) => BLOKKEN[n].includes(w))).toBe(true);
	expect(tweeAlineas.paragraphs).toBe(2);

	// Eén lijstpunt, niet de hele lijst.
	const lp = woorden(lijstpunt.value);
	console.log("LIJSTPUNT:", JSON.stringify(lp));
	expect(lp.length).toBe(1);
	expect(BLOKKEN.lijst).toContain(lp[0]);

	expect(eenBlok(kop1.value, ["kop1"])).toBe("kop1");
}

/** Zet een merkteken op de uitkomst van worp i, zodat te zien is wanneer er een nieuwe staat. */
async function markeer(view, i) {
	await browser.execute((sel, i) => {
		document.querySelectorAll(`${sel} .rollwright-roll`)[i]?.querySelector(".rollwright-value")?.setAttribute("data-e2e-oud", "1");
	}, `${LEAF} ${view}`, i);
}

async function ctrlKlik(view, i) {
	await browser.execute((sel, i) => {
		const el = document.querySelectorAll(`${sel} .rollwright-roll`)[i];
		el?.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true, ctrlKey: true }));
	}, `${LEAF} ${view}`, i);
}

async function markdownTabs() {
	return browser.executeObsidian(({ app }) => app.workspace.getLeavesOfType("markdown").map((l) => l.view?.file?.path ?? ""));
}

async function sluitBron() {
	await browser.executeObsidian(({ app }) => {
		for (const leaf of app.workspace.getLeavesOfType("markdown")) {
			if (leaf.view?.file?.path === "Bron.md") leaf.detach();
		}
	});
}

/** Ctrl-klik op worp i: Bron.md opent in een nieuw tabblad en de uitkomst blijft precies gelijk. */
async function checkCtrlKlik(view, i, shot) {
	const voor = (await readRolls(view))[i].value;
	const historieVoor = await laatsteWorp();
	const tabsVoor = await markdownTabs();
	// Merk het tabblad waarin geklikt wordt, zodat het na het openen van Bron.md terug te vinden is.
	await browser.executeObsidian(({ app }) => {
		for (const el of document.querySelectorAll("[data-e2e-tab]")) el.removeAttribute("data-e2e-tab");
		app.workspace.getMostRecentLeaf()?.view?.containerEl.setAttribute("data-e2e-tab", "1");
	});
	await markeer(view, i);
	await ctrlKlik(view, i);
	let tabs = [];
	await browser.waitUntil(async () => {
		tabs = await markdownTabs();
		return tabs.includes("Bron.md");
	}, { timeout: 5000, timeoutMsg: "Bron.md ging niet open" }).catch((e) => {
		console.log("NA CTRL-KLIK:", JSON.stringify(tabs));
		throw e;
	});
	console.log(`NA CTRL-KLIK OP WORP ${i} (${view}):`, JSON.stringify(tabs), "eerst:", JSON.stringify(tabsVoor));
	expect(tabs.length).toBe(tabsVoor.length + 1);
	await browser.saveScreenshot(`${SHOTS}/${shot}`);
	// Geen nieuwe worp: de laatste regel in de geschiedenis is dezelfde als voor de klik.
	const historieNa = await laatsteWorp();
	console.log("LAATSTE WORP IN GESCHIEDENIS VOOR EN NA:", historieVoor, historieNa);
	expect(historieNa).toBe(historieVoor);
	// Terug naar het tabblad waarin geklikt werd: de uitkomst is dezelfde.
	await sluitBron();
	await browser.executeObsidian(({ app }) => {
		const leaf = app.workspace.getLeavesOfType("markdown").find((l) => l.view?.containerEl.hasAttribute("data-e2e-tab"));
		if (leaf) app.workspace.setActiveLeaf(leaf, { focus: true });
	});
	const rolls = await waitForRolls(view, AANTAL);
	console.log("UITKOMST VOOR EN NA:", JSON.stringify(voor), JSON.stringify(rolls[i].value), "zelfde element:", rolls[i].old);
	expect(rolls[i].value).toBe(voor);
}

/** De laatste worp in de geschiedenis van Rollwright, als tekst. */
async function laatsteWorp() {
	return browser.executeObsidian(({ app }) => JSON.stringify(app.plugins.plugins.rollwright?.settings?.history?.[0] ?? null));
}

describe("Rollwright: secties en regels in de echte Obsidian", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
	});

	it("in de leesweergave komt elke worp uit het goede blok of de goede regel", async function () {
		await openNote("Sectiewerpen.md", "preview");
		const rolls = await waitForRolls(".markdown-reading-view", AANTAL);
		console.log("SECTIEWERPEN LEZEN:", JSON.stringify(rolls));
		await browser.saveScreenshot(`${SHOTS}/s1-secties-lezen.png`);
		check(rolls);
	});

	it("vijftien keer klikken op de regelworp geeft steeds één regel, en verschillende", async function () {
		const seen = new Set();
		for (let i = 0; i < 15; i++) {
			const before = (await readRolls(".markdown-reading-view"))[3];
			await klikWorp(`${LEAF} .markdown-reading-view`, 3, { markeer: true });
			let rolls = [];
			await browser.waitUntil(async () => {
				rolls = await readRolls(".markdown-reading-view");
				return rolls[3] !== undefined && !rolls[3].old && (rolls[3].value !== "" || rolls[3].hr);
			}, { timeout: 5000, timeoutMsg: "na een klik bleef de regelworp leeg" });
			checkRegel(rolls[3], 1, `KLIK ${i + 1}`);
			seen.add(woorden(rolls[3].value)[0]);
			if (i === 0) console.log("VOOR DE EERSTE KLIK:", JSON.stringify(before.value));
		}
		console.log("REGELS GEZIEN:", JSON.stringify([...seen]));
		// Acht regels (de lijn telt niet) en zestien worpen: steeds dezelfde regel is vrijwel onmogelijk.
		expect(seen.size).toBeGreaterThan(1);
	});

	it("in Live Preview hetzelfde", async function () {
		await openNote("Sectiewerpen.md", "source");
		const rolls = await waitForRolls(".markdown-source-view", AANTAL);
		console.log("SECTIEWERPEN LIVE PREVIEW:", JSON.stringify(rolls));
		await browser.saveScreenshot(`${SHOTS}/s2-secties-live-preview.png`);
		check(rolls);
	});

	it("Ctrl-klik in lezen opent Bron.md in een nieuw tabblad en rolt niet", async function () {
		await openNote("Sectiewerpen.md", "preview");
		await waitForRolls(".markdown-reading-view", AANTAL);
		// Worp 0 (een willekeurig blok) heeft meer uitkomsten, dus een nieuwe worp zou te zien zijn.
		await checkCtrlKlik(".markdown-reading-view", 0, "s3-ctrl-klik-lezen.png");
	});

	it("Ctrl-klik in Live Preview doet hetzelfde", async function () {
		await openNote("Sectiewerpen.md", "source");
		await waitForRolls(".markdown-source-view", AANTAL);
		await checkCtrlKlik(".markdown-source-view", 3, "s4-ctrl-klik-live-preview.png");
	});
});
