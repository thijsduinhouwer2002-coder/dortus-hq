import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// Ontwerp-v2 klus 6 in de echte Obsidian: het lege logboek toont de knop "Try it: create an example note".
// Die maakt de notitie "Rollwright example" en opent hem; alle zes worpen (vier dobbelworpen en twee
// tabellen onderaan dezelfde notitie) tonen een uitkomst zonder fout, in lezen en in Live Preview. Een
// tweede keer (knop of commando) opent dezelfde notitie en overschrijft niets.
const SHOTS = "screenshots";
const LEAF = ".workspace-leaf.mod-active";
const PANEEL = '.workspace-leaf-content[data-type="rollwright-history"]';
const PAD = "Rollwright example.md";
const GASTEN = ["A dwarf counting her coins twice", "Two elves arguing over a map", "A bard with one string left", "A sleeping knight in muddy armour"];
const GERUCHTEN = ['"The bridge at Harrow fell last night."', '"Someone is buying every lantern in town."', '"The old mine is singing again."'];

async function readRolls(view) {
	return browser.execute((sel) => Array.from(document.querySelectorAll(`${sel} .rollwright-roll`)).map((r) => ({
		value: (r.querySelector(".rollwright-value")?.textContent ?? "").trim(),
		error: r.getAttribute("data-rollwright-error") ?? "",
		cls: r.className,
	})), `${LEAF} ${view}`);
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

function check(rolls, view) {
	console.log(`VOORBEELD ${view}:`, JSON.stringify(rolls.map((r) => r.value)));
	expect(rolls.length).toBe(6);
	for (const r of rolls) expect(r.error).toBe("");
	// Initiative 1d20+3, Hit 1d20+5, Damage 2d6+3, Wisdom save 1d20.
	const grenzen = [[4, 23], [6, 25], [5, 15], [1, 20]];
	grenzen.forEach(([lo, hi], i) => {
		const getal = Number(/(\d+)\s*$/.exec(rolls[i].value)?.[1]);
		expect(getal >= lo && getal <= hi).toBe(true);
	});
	expect(GASTEN).toContain(rolls[4].value);
	expect(GERUCHTEN).toContain(rolls[5].value);
}

/**
 * Hoeveel breder het label "Wisdom save: " is dan zijn tekst zonder de spatie aan het eind. Rond 0 als de
 * spatie wegvalt (lezen); een spatiebreedte als hij blijft staan naast de gap (de dubbele ruimte, Daan ronde 6).
 */
async function spatieNaLabel(view) {
	return browser.execute((sel) => {
		const label = Array.from(document.querySelectorAll(`${sel} .rollwright-label`)).find((l) => (l.textContent ?? "").startsWith("Wisdom save"));
		const node = label?.firstChild;
		if (!label || !node) return -1;
		const range = document.createRange();
		range.setStart(node, 0);
		range.setEnd(node, (node.textContent ?? "").trimEnd().length);
		return label.getBoundingClientRect().width - range.getBoundingClientRect().width;
	}, `${LEAF} ${view}`);
}

async function actieveNotitie() {
	return browser.executeObsidian(({ app }) => app.workspace.getActiveFile()?.path ?? "");
}

describe("Rollwright: de voorbeeldnotitie (ontwerp-v2 klus 6)", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.executeObsidian(async ({ app }) => {
			const plugin = app.plugins.plugins.rollwright;
			await plugin.clearHistory();
			await plugin.openHistory();
		});
	});

	it("maakt niets vanzelf aan bij het laden", async function () {
		const er = await browser.executeObsidian(({ app }, pad) => app.vault.getAbstractFileByPath(pad) !== null, PAD);
		expect(er).toBe(false);
	});

	it("toont de knop in het lege logboek en maakt en opent de notitie bij een klik", async function () {
		const knop = await $(`${PANEEL} .rollwright-history-empty button.rollwright-history-try`);
		await knop.waitForExist({ timeout: 5000, timeoutMsg: "geen knop in het lege logboek" });
		expect(await knop.getText()).toBe("Try it: create an example note");
		await knop.click();
		await browser.waitUntil(async () => (await actieveNotitie()) === PAD, { timeout: 8000, timeoutMsg: "de voorbeeldnotitie is niet geopend" });
		const tekst = await browser.executeObsidian(async ({ app }, pad) => app.vault.read(app.vault.getAbstractFileByPath(pad)), PAD);
		expect(tekst.startsWith("> [!tip] Every roll in this note is live")).toBe(true);
	});

	it("rolt alle zes worpen zonder fout in lezen", async function () {
		await browser.executeObsidian(async ({ app }) => {
			const leaf = app.workspace.getLeaf(false);
			await leaf.setViewState({ ...leaf.getViewState(), state: { ...leaf.getViewState().state, mode: "preview" } });
		});
		check(await waitForRolls(".markdown-reading-view", 6), "lezen");
		const spatie = await spatieNaLabel(".markdown-reading-view");
		console.log("SPATIE NA LABEL lezen:", spatie);
		expect(spatie >= 0 && spatie < 1.5).toBe(true);
		const tip = await browser.execute((sel) => document.querySelector(`${sel} .markdown-reading-view .callout[data-callout="tip"]`) !== null, LEAF);
		expect(tip).toBe(true);
		await browser.saveScreenshot(`${SHOTS}/voorbeeld-lezen.png`);
	});

	it("rolt alle zes worpen zonder fout in Live Preview", async function () {
		await browser.executeObsidian(async ({ app }) => {
			const leaf = app.workspace.getLeaf(false);
			await leaf.setViewState({ ...leaf.getViewState(), state: { ...leaf.getViewState().state, mode: "source", source: false } });
		});
		check(await waitForRolls(".markdown-source-view.is-live-preview", 6), "Live Preview");
		const spatie = await spatieNaLabel(".markdown-source-view.is-live-preview");
		console.log("SPATIE NA LABEL Live Preview:", spatie);
		expect(spatie >= 0 && spatie < 1.5).toBe(true);
		await browser.saveScreenshot(`${SHOTS}/voorbeeld-live.png`);
	});

	it("overschrijft een bestaande voorbeeldnotitie niet, ook niet via het commando", async function () {
		const eigen = await browser.executeObsidian(async ({ app }, pad) => {
			const file = app.vault.getAbstractFileByPath(pad);
			await app.vault.append(file, "\nMy own line.\n");
			return app.vault.read(file);
		}, PAD);
		// Eerst een andere notitie actief, zodat het wachten hieronder echt bewijst dat het commando opent.
		await browser.executeObsidian(async ({ app }) => {
			const leaf = app.workspace.getLeaf(false);
			await leaf.openFile(app.vault.getAbstractFileByPath("Tabellen.md"));
			app.workspace.setActiveLeaf(leaf, { focus: true });
		});
		await browser.waitUntil(async () => (await actieveNotitie()) === "Tabellen.md", { timeout: 8000, timeoutMsg: "Tabellen.md niet actief" });
		await browser.executeObsidian(({ app }) => app.commands.executeCommandById("rollwright:create-example-note"));
		await browser.waitUntil(async () => (await actieveNotitie()) === PAD, { timeout: 8000, timeoutMsg: "het commando opende de voorbeeldnotitie niet" });
		const na = await browser.executeObsidian(async ({ app }) => ({
			tekst: await app.vault.read(app.vault.getAbstractFileByPath("Rollwright example.md")),
			aantal: app.vault.getMarkdownFiles().filter((f) => f.basename.startsWith("Rollwright example")).length,
		}));
		console.log("VOORBEELD TWEEDE KEER:", JSON.stringify({ aantal: na.aantal, gelijk: na.tekst === eigen }));
		expect(na.aantal).toBe(1);
		expect(na.tekst).toBe(eigen);
	});

	it("blijft rollen na hernoemen: de tabellen verwijzen met [[#^id]] naar de notitie zelf", async function () {
		const NIEUW = "Mijn herberg.md";
		await browser.executeObsidian(async ({ app }, [pad, nieuw]) => {
			await app.fileManager.renameFile(app.vault.getAbstractFileByPath(pad), nieuw);
			// Eerst een andere notitie, dan de hernoemde: zo tekent de leesweergave alles opnieuw.
			const leaf = app.workspace.getLeaf(false);
			await leaf.openFile(app.vault.getAbstractFileByPath("Tabellen.md"));
			await leaf.openFile(app.vault.getAbstractFileByPath(nieuw), { state: { mode: "preview" } });
			app.workspace.setActiveLeaf(leaf, { focus: true });
		}, [PAD, NIEUW]);
		await browser.waitUntil(async () => (await actieveNotitie()) === NIEUW, { timeout: 8000, timeoutMsg: "hernoemde notitie niet actief" });
		try {
			const rolls = await waitForRolls(".markdown-reading-view", 6);
			console.log("NA HERNOEMEN:", JSON.stringify(rolls.map((r) => ({ v: r.value, e: r.error }))));
			check(rolls, "na hernoemen");
		} finally {
			await browser.executeObsidian(async ({ app }, [pad, nieuw]) => {
				const file = app.vault.getAbstractFileByPath(nieuw);
				if (file) await app.fileManager.renameFile(file, pad);
			}, [PAD, NIEUW]);
		}
	});

	after(async function () {
		await browser.executeObsidian(async ({ app }, pad) => {
			const file = app.vault.getAbstractFileByPath(pad);
			if (file) await app.vault.delete(file);
		}, PAD);
	});
});
