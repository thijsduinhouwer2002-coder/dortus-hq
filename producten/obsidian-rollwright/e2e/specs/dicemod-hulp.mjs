import { browser, expect } from "@wdio/globals";

// Gedeelde hulp voor de dice-mod specs (dicemod-live.e2e.mjs en dicemod-lezen.e2e.mjs).
// Dit bestand heet bewust niet *.e2e.mjs, zodat wdio het niet als spec draait.
// dice-mod: in de echte Obsidian. Een klik (of Enter) rolt niet opnieuw maar opent een venster
// met de tekst die in de notitie komt. Replace schrijft die tekst in plaats van de code.
// Elke test die het bestand verandert heeft een eigen notitie, zodat de tests elkaar niet raken.
// Het venster komt uit src/ui/dice-mod.ts (ReplaceCodeModal): titel "Replace the dice code?",
// de tekst in <pre><code>, knoppen "Cancel" en "Replace".
export const SHOTS = "screenshots";
export const LEAF = ".workspace-leaf.mod-active";
const ZWS = String.fromCharCode(0x200b);
const TITEL = "Replace the dice code?";
export const CODE = "`dice-mod: 3d100 + 12`";
const VORM = /^3d100 \+ 12 -> \[(\d+), (\d+), (\d+)\] \+ 12 -> (\d+)$/;
// Met de instelling diceModFormula uit (src/main.ts, RollwrightSettings) valt de formule weg.
export const VORM_ZONDER = /^\[(\d+), (\d+), (\d+)\] \+ 12 -> (\d+)$/;
// De codes en de notities staan bewust zo dat de vervangtekst geen backslash krijgt
// (src/rollers/modify.ts, fitReplacement): geen backtick of | in de uitkomst, geen tabelregel,
// en "Worp: " of "Kleur: " voor de code, zodat hij niet aan het begin van een regel staat.
// Zo is de tekst in het bestand precies de tekst uit het venster.

export async function openNote(path, mode) {
	await browser.executeObsidian(async ({ app }, path, mode) => {
		const file = app.vault.getAbstractFileByPath(path);
		if (!file) throw new Error(`notitie ${path} niet gevonden`);
		const leaf = app.workspace.getLeaf(false);
		const state = mode === "preview" ? { mode: "preview" } : { mode: "source", source: false };
		await leaf.openFile(file, { state });
		app.workspace.setActiveLeaf(leaf, { focus: true });
	}, path, mode);
}

export async function readRolls(view) {
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

export async function waitForRolls(view, n) {
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
export async function markeer(view, i) {
	await browser.execute((sel, i) => {
		document.querySelectorAll(`${sel} .rollwright-roll`)[i]?.querySelector(".rollwright-value")?.setAttribute("data-e2e-oud", "1");
	}, `${LEAF} ${view}`, i);
}

export async function klik(view, i) {
	await browser.execute((sel, i) => {
		document.querySelectorAll(`${sel} .rollwright-roll`)[i]?.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true }));
	}, `${LEAF} ${view}`, i);
}

/** Het open vervangvenster van Rollwright, of null. */
export async function readVenster() {
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

export async function waitForVenster() {
	let venster = null;
	await browser.waitUntil(async () => {
		venster = await readVenster();
		return venster !== null && venster.tekst !== null;
	}, { timeout: 10000, timeoutMsg: "het vervangvenster ging niet open" }).catch(async (e) => {
		const meldingen = await browser.execute(() => Array.from(document.querySelectorAll(".notice")).map((n) => (n.textContent ?? "").trim()));
		const focus = await browser.execute(() => `${document.activeElement?.tagName}.${document.activeElement?.className}`);
		console.log("GEEN VENSTER. MELDINGEN:", JSON.stringify(meldingen), "FOCUS:", focus);
		throw e;
	});
	console.log("VENSTER:", JSON.stringify(venster));
	expect(venster.knoppen).toContain("Cancel");
	expect(venster.knoppen).toContain("Replace");
	return venster;
}

export async function waitVensterDicht() {
	await browser.waitUntil(async () => (await readVenster()) === null, { timeout: 10000, timeoutMsg: "het vervangvenster bleef open" });
}

export async function knop(tekst) {
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
export async function leesBestand(path) {
	return browser.executeObsidian(async ({ app }, path) => {
		const file = app.vault.getAbstractFileByPath(path);
		if (!file) throw new Error(`notitie ${path} niet gevonden`);
		return app.vault.read(file);
	}, path);
}

/** Wacht tot de notitie op schijf deze inhoud heeft. Live Preview bewaart pas na een korte tijd. */
export async function waitForBestand(path, verwacht, wat, bewaar = true) {
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
	}, { timeout: 15000, timeoutMsg: `${path} kreeg niet de verwachte inhoud (${wat})` }).catch(async (e) => {
		console.log(`${path} NU:`, JSON.stringify(last));
		console.log(`${path} VERWACHT:`, JSON.stringify(verwacht));
		// Om te zien waar het misgaat: staat de wijziging wel in de editor, en welke melding gaf de plugin?
		const extra = await browser.executeObsidian(({ app }) => ({
			editor: app.workspace.activeEditor?.editor?.getValue() ?? null,
			meldingen: Array.from(document.querySelectorAll(".notice")).map((n) => (n.textContent ?? "").trim()),
			worpen: document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll").length,
		}));
		console.log(`${path} EDITOR EN MELDINGEN:`, JSON.stringify(extra));
		throw e;
	});
	return last;
}

/** Controleert de vorm van de tekst en dat het totaal de som plus 12 is. */
export function checkVorm(tekst, vorm = VORM) {
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
export async function laatsteWorp() {
	return browser.executeObsidian(({ app }) => JSON.stringify(app.plugins.plugins.rollwright?.settings?.history?.[0] ?? null));
}

/**
 * Leest het bestand steeds opnieuw, zo lang als ms, en eist dat het gelijk blijft.
 * Zo valt ook een schrijfactie op die pas even later komt.
 */
export async function blijftGelijk(path, voor, ms = 1000) {
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
export async function vervang(view, path, shot, vorm = VORM) {
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
	// Staat dezelfde worp (met merkteken) er nog vlak voor Replace? Zo niet, dan tekende de editor hem opnieuw.
	console.log("ZELFDE WORP VOOR REPLACE:", await browser.execute(() => document.querySelector(".workspace-leaf.mod-active [data-e2e-oud]") !== null));
	await knop("Replace");
	// Meldingen verdwijnen na een paar seconden, dus meteen na Replace lezen.
	await browser.waitUntil(async () => browser.execute(() => document.querySelector(".modal-container") === null), { timeout: 5000, timeoutMsg: "na Replace bleef het venster open (.modal-container is er nog)" });
	const direct = await browser.executeObsidian(({ app }) => ({
		meldingen: Array.from(document.querySelectorAll(".notice")).map((n) => (n.textContent ?? "").trim()),
		editor: app.workspace.activeEditor?.editor?.getValue()?.split("\n")[4] ?? null,
		worpInEditor: document.querySelector(".workspace-leaf.mod-active .cm-content .rollwright-roll")?.isConnected ?? false,
	}));
	console.log("DIRECT NA REPLACE:", JSON.stringify(direct));
	await waitVensterDicht();
	const verwacht = voor.replace(CODE, venster.tekst);
	const bestand = await waitForBestand(path, verwacht, "na Replace", view === ".markdown-source-view");
	console.log(`${path} NA:`, JSON.stringify(bestand));
	expect(bestand.includes(CODE)).toBe(false);
	return { voor, na: bestand, tekst: venster.tekst };
}
