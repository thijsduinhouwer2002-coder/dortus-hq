import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// Winkelplaatjes voor README en lancering: een Engelse demonotitie zonder testnamen in beeld.
// Plaatjes: winkel-*.png (licht en donker), via de workflow naar tak `schermen`. Daan keurt ze.
const SHOTS = "screenshots";
const NOTE = "Demo/Session 12.md";
const LEAF = ".workspace-leaf.mod-active";
const AANTAL = 6;
// Volgorde van de worpen in Demo/Session 12.md.
const LOOT = 4;
const TOLWACHTER = 5;
// De regels van Demo/Toll keeper.md (|line trekt er twee, met teruglegging).
const ZINNEN = [
	"Two coppers to cross, and mind the third plank.",
	"Nobody has come back from the north road this week.",
	"The bandits pay me more than you do.",
	"Rain is coming. You can smell it on the water.",
	"I saw a light under the bridge last night.",
];

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

/** Hoeveel verschillende zinnen van de tolwachter in een uitkomst staan. */
function zinnen(tekst) {
	return ZINNEN.filter((z) => tekst.includes(z)).length;
}

/**
 * Loot en de tolwachter trekken met teruglegging; voor een winkelplaatje willen we drie verschillende
 * dingen en twee verschillende zinnen. Klik op de worp die nog dubbel is, tot beide kloppen.
 */
async function lootVerschillend(view) {
	const sel = `${LEAF} ${view}`;
	for (let poging = 0; poging < 40; poging++) {
		const w = await wacht(view);
		const lootGoed = new Set(w[LOOT].tekst.split(",").map((s) => s.trim())).size === 3;
		const zinnenGoed = zinnen(w[TOLWACHTER].tekst) === 2;
		if (lootGoed && zinnenGoed) return w;
		await browser.execute((sel, i) => {
			const r = Array.from(document.querySelectorAll(`${sel} .rollwright-roll`)).filter((e) => !e.parentElement?.closest(".rollwright-roll"))[i];
			r?.querySelector(".rollwright-value")?.setAttribute("data-e2e-oud", "1");
			r?.click();
		}, sel, lootGoed ? TOLWACHTER : LOOT);
		await browser.pause(300);
	}
	throw new Error("loot of de tolwachter bleef dubbel");
}

/** De tolwachter staat als blok onder de regel (Daan punt 1), zodat het plaatje ook een blokuitkomst laat zien (Daan W2). */
async function tolwachterIsBlok(view) {
	return browser.execute((sel, i) => {
		const r = Array.from(document.querySelectorAll(`${sel} .rollwright-roll`)).filter((e) => !e.parentElement?.closest(".rollwright-roll"))[i];
		return r?.classList.contains("rollwright-roll-block") ?? false;
	}, `${LEAF} ${view}`, TOLWACHTER);
}

async function thema(donker) {
	await browser.execute((donker) => {
		document.body.classList.toggle("theme-dark", donker);
		document.body.classList.toggle("theme-light", !donker);
	}, donker);
	await browser.pause(300);
}

// Plaatjes voor de lijst op community.obsidian.md: die wil 1200 bij 800 pixels.
// browser.setWindowSize werkt niet in Obsidian, dus via Chrome DevTools (Emulation) een venster van 1200 bij 800 nabootsen.
async function cdp(cmd, params) {
	const o = browser.options;
	const basis = `${o.protocol ?? "http"}://${o.hostname ?? "localhost"}:${o.port}${(o.path ?? "/").replace(/\/?$/, "/")}`;
	const res = await fetch(`${basis}session/${browser.sessionId}/goog/cdp/execute`, {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify({ cmd, params }),
	});
	const tekst = await res.text();
	if (!res.ok) throw new Error(`cdp ${cmd}: ${res.status} ${tekst.slice(0, 300)}`);
	return tekst;
}

async function lijstPlaatje(naam) {
	await cdp("Emulation.setDeviceMetricsOverride", { width: 1200, height: 800, deviceScaleFactor: 1, mobile: false });
	try {
		await browser.pause(500);
		const maat = await browser.execute(() => `${window.innerWidth}x${window.innerHeight}`);
		console.log(`WINKEL LIJST MAAT (${naam}):`, maat);
		expect(maat).toBe("1200x800");
		await browser.action("pointer").move({ x: 300, y: 790, origin: "viewport" }).perform();
		await browser.pause(200);
		const onderMuis = await browser.execute(() => Array.from(document.querySelectorAll(".rollwright-roll:hover, .rollwright-history-item:hover")).length);
		console.log(`WINKEL LIJST ONDER DE MUIS (${naam}):`, onderMuis);
		expect(onderMuis).toBe(0);
		await browser.saveScreenshot(`${SHOTS}/${naam}.png`);
	} finally {
		// Altijd terug naar het gewone venster, ook als een eis hierboven faalt.
		await cdp("Emulation.clearDeviceMetricsOverride", {});
		await browser.pause(300);
	}
}

async function plaatjes(naam, { focusWeg = true, lijst = true } = {}) {
	// Geen focusrand of cursor in beeld, behalve waar de cursor juist de code moet tonen.
	if (focusWeg) await browser.execute(() => (document.activeElement instanceof HTMLElement ? document.activeElement.blur() : undefined));
	// De muis van Xvfb staat midden in het scherm, precies op de buit, en :hover gaf een paarse rand (Daan W6a).
	// Zet hem in de lege strook onderaan en eis dat geen worp of geschiedenisregel meer onder de muis zit.
	await browser.action("pointer").move({ x: 300, y: 790, origin: "viewport" }).perform();
	await browser.pause(200);
	const onderMuis = await browser.execute(() => Array.from(document.querySelectorAll(".rollwright-roll:hover, .rollwright-history-item:hover")).length);
	console.log(`WINKEL ONDER DE MUIS (${naam}):`, onderMuis);
	expect(onderMuis).toBe(0);
	await thema(false);
	await browser.saveScreenshot(`${SHOTS}/${naam}.png`);
	await thema(true);
	await browser.saveScreenshot(`${SHOTS}/${naam}-donker.png`);
	if (lijst) await lijstPlaatje(`lijst-${naam.replace(/^winkel-/, "")}-donker`);
	await thema(false);
	if (lijst) await lijstPlaatje(`lijst-${naam.replace(/^winkel-/, "")}`);
}

describe("Rollwright: winkelplaatjes", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		// Linker zijpaneel dicht: dan staan de testnotities niet in beeld.
		await browser.executeObsidian(({ app }) => app.workspace.leftSplit?.collapse());
		// Inline titel uit: anders staat de titel twee keer in beeld (bestandsnaam en de kop in de notitie).
		await browser.executeObsidian(({ app }) => app.vault.setConfig("showInlineTitle", false));
		// Statusbalk weg: het rode Sync-icoon leest als een fout (Daan W3).
		// browser.setWindowSize werkt niet in Obsidian (Electron: Browser.getWindowForTarget onbekend, run 42373505254).
		await browser.execute(() => {
			const s = document.createElement("style");
			s.id = "winkel-stijl";
			s.textContent = ".status-bar { display: none !important; }";
			document.head.appendChild(s);
		});
	});

	after(async function () {
		await browser.executeObsidian(({ app }) => app.vault.setConfig("showInlineTitle", true));
	});

	it("leesweergave met worpen, tabel en lijst", async function () {
		await open("preview");
		const w = await lootVerschillend(".markdown-reading-view");
		console.log("WINKEL LEZEN:", JSON.stringify(w));
		const titels = await browser.execute((sel) => Array.from(document.querySelectorAll(`${sel} .inline-title`)).filter((e) => e.offsetParent !== null).length, LEAF);
		console.log("WINKEL INLINE TITELS ZICHTBAAR:", titels);
		expect(titels).toBe(0);
		for (const r of w) expect(r.fout).toBe("");
		expect(w[LOOT].tekst.split(",").length).toBe(3);
		expect(zinnen(w[TOLWACHTER].tekst)).toBe(2);
		const blok = await tolwachterIsBlok(".markdown-reading-view");
		console.log("WINKEL TOLWACHTER ALS BLOK (LEZEN):", blok);
		expect(blok).toBe(true);
		await plaatjes("winkel-1-lezen");
	});

	it("Live Preview hetzelfde", async function () {
		await open("source");
		const w = await lootVerschillend(".markdown-source-view");
		console.log("WINKEL LIVE PREVIEW:", JSON.stringify(w));
		for (const r of w) expect(r.fout).toBe("");
		const blok = await tolwachterIsBlok(".markdown-source-view");
		console.log("WINKEL TOLWACHTER ALS BLOK (LIVE PREVIEW):", blok);
		expect(blok).toBe(true);
		// Cursor op de regel van Perception: Live Preview toont daar de code, de rest de uitkomst (Daan W1).
		const regel = await browser.executeObsidian(({ app }) => {
			const editor = app.workspace.activeEditor?.editor;
			const n = editor ? Array.from({ length: editor.lineCount() }, (_, i) => i).find((i) => editor.getLine(i).startsWith("Perception")) : undefined;
			if (editor === undefined || n === undefined) return "";
			editor.focus();
			editor.setCursor({ line: n, ch: editor.getLine(n).length });
			return editor.getLine(n);
		});
		await browser.pause(400);
		const code = await browser.execute((sel) => Array.from(document.querySelectorAll(`${sel} .cm-line`)).map((l) => l.textContent ?? "").find((t) => t.startsWith("Perception")) ?? "", `${LEAF} .markdown-source-view`);
		console.log("WINKEL CODE IN BEELD:", JSON.stringify(regel), JSON.stringify(code));
		expect(code).toContain("dice: 1d20 + 4");
		await plaatjes("winkel-2-live-preview", { focusWeg: false });
	});

	it("geschiedenis rechts na een paar klikken", async function () {
		await open("preview");
		await lootVerschillend(".markdown-reading-view");
		// Het paneel openen maakt het paneel actief; daarna de notitie weer actief, anders vindt LEAF geen worpen.
		await browser.executeObsidian(async ({ app }) => {
			const note = app.workspace.getMostRecentLeaf();
			await app.plugins.plugins.rollwright.openHistory();
			if (note) app.workspace.setActiveLeaf(note, { focus: true });
		});
		await browser.waitUntil(async () => browser.execute(() => document.querySelector('.workspace-leaf-content[data-type="rollwright-history"]') !== null),
			{ timeout: 5000, timeoutMsg: "het geschiedenispaneel opende niet" });
		// Elke worp één keer aanklikken, zodat alle worpen in de geschiedenis staan (graag-punt Daan). Een klik gooit
		// opnieuw; is de buit of de tolwachter daarna dubbel, dan geschiedenis leeg en de hele ronde opnieuw, zodat
		// er geen afgekeurde worpen in het paneel blijven staan.
		let w = [];
		for (let ronde = 0; ronde < 40; ronde++) {
			await browser.executeObsidian(async ({ app }) => app.plugins.plugins.rollwright.clearHistory());
			// Daan (Thijs 8 nov): niet alles op dezelfde minuut, dat oogt nep. Een avondsessie van 20:41 tot 21:02.
			const minuten = [0, 3, 7, 12, 16, 21];
			for (const [k, i] of [TOLWACHTER, LOOT, 1, 3, 2, 0].entries()) {
				await browser.execute((m) => {
					const w = window;
					if (!w.__rwEchtNu) w.__rwEchtNu = Date.now;
					const basis = new Date(); basis.setHours(20, 41, 0, 0);
					const verschil = basis.getTime() + m * 60000 - w.__rwEchtNu();
					Date.now = () => w.__rwEchtNu() + verschil;
				}, minuten[k]);
				await browser.execute((sel, i) => {
					const r = Array.from(document.querySelectorAll(`${sel} .rollwright-roll`)).filter((e) => !e.parentElement?.closest(".rollwright-roll"))[i];
					r?.querySelector(".rollwright-value")?.setAttribute("data-e2e-oud", "1");
					r?.click();
				}, `${LEAF} .markdown-reading-view`, i);
				await browser.pause(150);
			}
			// Pas lezen als elke aangeklikte worp een nieuwe uitkomst heeft (het merkteken verdwijnt met de oude).
			await browser.waitUntil(async () => browser.execute((sel) => document.querySelector(`${sel} [data-e2e-oud]`) === null, `${LEAF} .markdown-reading-view`),
				{ timeout: 10000, timeoutMsg: "een aangeklikte worp kreeg geen nieuwe uitkomst" });
			w = await wacht(".markdown-reading-view");
			const lootGoed = new Set(w[LOOT].tekst.split(",").map((t) => t.trim())).size === 3;
			if (lootGoed && zinnen(w[TOLWACHTER].tekst) === 2) break;
		}
		console.log("WINKEL GESCHIEDENIS NOTITIE:", JSON.stringify(w.map((x) => x.tekst)));
		let items = 0;
		await browser.waitUntil(async () => {
			items = await browser.execute(() => document.querySelectorAll(".rollwright-history-item").length);
			return items === 6;
		}, { timeout: 5000 }).catch(() => {});
		console.log("WINKEL GESCHIEDENIS ITEMS:", items);
		expect(items).toBe(6);
		expect(new Set(w[LOOT].tekst.split(",").map((t) => t.trim())).size).toBe(3);
		expect(zinnen(w[TOLWACHTER].tekst)).toBe(2);
		// De nieuwste staat bovenaan (alleen gelogd); de buit in de geschiedenis moet gelijk zijn aan de notitie.
		const bovenste = await browser.execute(() => document.querySelector(".rollwright-history-item")?.textContent ?? "");
		console.log("WINKEL GESCHIEDENIS BOVENSTE:", JSON.stringify(bovenste));
		const geschiedenisBuit = await browser.execute(() => Array.from(document.querySelectorAll(".rollwright-history-item")).map((e) => e.textContent ?? "").find((t) => t.includes("loot")) ?? "");
		console.log("WINKEL GESCHIEDENIS BUIT:", JSON.stringify(geschiedenisBuit));
		expect(geschiedenisBuit).toContain(w[LOOT].tekst);
		await plaatjes("winkel-3-geschiedenis");
	});
});
