import { browser, expect } from "@wdio/globals";
import * as fs from "fs";
import { klikWorp } from "./klik-hulp.mjs";

// Ontwerp-v2 klus 5 en 5b in de echte Obsidian: het paneel heet "Roll log", worpen staan onder een
// kopje met de notitienaam (zonder map en zonder .md) en het uur, de link in een item toont alleen de
// naam, en een worp uit het invoerveld van het paneel komt in het logboek (niet alleen als melding).
const SHOTS = "screenshots";
const LEAF = ".workspace-leaf.mod-active";
const PANEEL = '.workspace-leaf-content[data-type="rollwright-history"]';
const NOTITIE = "Campagne/De Roestige Kroes.md";
const NAAM = "De Roestige Kroes";

async function history() {
	return browser.executeObsidian(({ app }) => (app.plugins.plugins.rollwright?.settings?.history ?? []).map((h) => ({ result: h.result, formula: h.formula, source: h.source })));
}

/** Wat het paneel toont: titel, kopjes met hun items, en de links naar de notitie. */
async function paneel() {
	return browser.execute((sel) => {
		const root = document.querySelector(sel);
		return {
			kopjes: Array.from(root?.querySelectorAll(".rollwright-history-group") ?? []).map((g) => ({
				titel: (g.querySelector(".rollwright-history-group-title")?.textContent ?? "").trim(),
				pad: g.querySelector(".rollwright-history-group-title")?.getAttribute("title") ?? "",
				items: Array.from(g.querySelectorAll(".rollwright-history-item")).map((i) => (i.querySelector(".rollwright-history-result")?.textContent ?? "").trim()),
			})),
			items: root?.querySelectorAll(".rollwright-history-item").length ?? 0,
			nieuwste: root?.querySelector(".rollwright-history-item")?.className ?? "",
			links: Array.from(root?.querySelectorAll(".rollwright-history-meta a") ?? []).map((a) => ({ tekst: (a.textContent ?? "").trim(), title: a.getAttribute("title") ?? "" })),
			wissen: (root?.querySelector(".rollwright-history-clear")?.textContent ?? "").trim(),
		};
	}, PANEEL);
}

async function wachtOpLengte(n, wat) {
	let laatst = [];
	await browser.waitUntil(async () => {
		laatst = await history();
		return laatst.length === n && (await paneel()).items === n;
	}, { timeout: 8000, timeoutMsg: `${wat}: geen ${n} regels in het logboek` }).catch((e) => {
		console.log(`LOGBOEK BIJ TIME-OUT (${wat}):`, JSON.stringify(laatst));
		throw e;
	});
	return laatst;
}

describe("Rollwright: het logboek (ontwerp-v2 klus 5 en 5b)", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.executeObsidian(async ({ app }) => {
			const plugin = app.plugins.plugins.rollwright;
			await plugin.clearHistory();
			await plugin.openHistory();
		});
		await browser.waitUntil(async () => browser.execute((sel) => document.querySelector(`${sel} .rollwright-history-empty`) !== null, PANEEL), {
			timeout: 5000, timeoutMsg: "het paneel toont geen leeg logboek",
		});
	});

	it("heet Roll log, ook in het commando, met dezelfde id's als voorheen", async function () {
		const namen = await browser.executeObsidian(({ app }) => {
			const leaf = app.workspace.getLeavesOfType("rollwright-history")[0];
			return {
				titel: leaf?.view?.getDisplayText?.() ?? "",
				tab: leaf?.tabHeaderEl?.getAttribute("aria-label") ?? leaf?.tabHeaderInnerTitleEl?.textContent ?? "",
				kop: leaf?.view?.containerEl?.querySelector(".view-header-title")?.textContent ?? "",
				commando: app.commands.commands["rollwright:open-history"]?.name ?? "",
			};
		});
		console.log("LOGBOEK NAMEN:", JSON.stringify(namen));
		expect(namen.titel).toBe("Roll log");
		expect(namen.commando).toContain("Open roll log");
	});

	it("zet een worp uit een notitie onder een kopje met de notitienaam zonder map en zonder .md", async function () {
		await browser.executeObsidian(async ({ app }, path) => {
			const file = app.vault.getAbstractFileByPath(path);
			if (!file) throw new Error(`notitie ${path} niet gevonden`);
			const leaf = app.workspace.getLeaf(false);
			await leaf.openFile(file, { state: { mode: "preview" } });
			app.workspace.setActiveLeaf(leaf, { focus: true });
		}, NOTITIE);
		await browser.waitUntil(async () => browser.execute((sel) => document.querySelector(`${sel} .rollwright-roll .rollwright-value`) !== null, `${LEAF} .markdown-reading-view`), {
			timeout: 20000, timeoutMsg: "geen worp in De Roestige Kroes",
		});
		await klikWorp(`${LEAF} .markdown-reading-view`, 0);
		const h = await wachtOpLengte(1, "klik in de notitie");
		const p = await paneel();
		console.log("LOGBOEK NA KLIK:", JSON.stringify({ geschiedenis: h, paneel: p }));
		expect(h[0].source).toBe(NOTITIE);
		expect(p.kopjes.length).toBe(1);
		expect(p.kopjes[0].titel.startsWith(`${NAAM} · `)).toBe(true);
		expect(p.kopjes[0].titel).not.toContain(".md");
		expect(p.kopjes[0].titel).not.toContain("Campagne");
		expect(p.kopjes[0].pad).toBe(NOTITIE);
		expect(p.links[0].tekst).toBe(NAAM);
		expect(p.links[0].title).toBe(NOTITIE);
		expect(p.wissen).toBe("Clear log");
		expect(p.nieuwste).toContain("rollwright-history-latest");
	});

	it("zet een worp uit het invoerveld van het paneel ook in het logboek", async function () {
		const veld = await browser.$(`${PANEEL} .rollwright-history-form input`);
		await veld.waitForDisplayed({ timeout: 5000 });
		await veld.setValue("7");
		await browser.$(`${PANEEL} .rollwright-history-form button`).click();
		const h = await wachtOpLengte(2, "worp uit het invoerveld");
		const p = await paneel();
		const melding = await browser.execute(() => Array.from(document.querySelectorAll(".notice")).map((n) => (n.textContent ?? "").trim()));
		console.log("LOGBOEK NA INVOERVELD:", JSON.stringify({ geschiedenis: h, paneel: p, meldingen: melding }));
		expect(h[0].formula).toBe("7");
		expect(h[0].result).toBe("7");
		// Het paneel was actief, dus de notitie die het laatst open was telt als bron.
		expect(h[0].source).toBe(NOTITIE);
		expect(p.kopjes[0].items[0]).toBe("7");
		expect(p.kopjes[0].titel.startsWith(`${NAAM} · `)).toBe(true);
		expect(melding.some((m) => m.includes("7: 7"))).toBe(true);
		await browser.saveScreenshot(`${SHOTS}/l1-logboek.png`);
	});
});
