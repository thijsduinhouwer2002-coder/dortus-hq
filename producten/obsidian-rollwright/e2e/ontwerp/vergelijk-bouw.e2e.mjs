import { browser } from "@wdio/globals";
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";

// Vergelijking van Daan (9 nov run 51): gratis Classic tegen de werelden, zelfde notitie, zelfde worpen, zelfde plek.
// Ontwerptest: de skin kleurt de hele notitie (ontwerp-notitiesfeer.md).
// Run 52: opnieuw opgenomen uit de echte bouw van Olaf (tak claude/obsidian-2026-11-09-stap2b), zonder prototype-CSS.
const SHOTS = "screenshots";
const NOTE = "Night at the Tideflats.md";
const HIER = path.dirname(fileURLToPath(import.meta.url));
const save = (n) => browser.saveScreenshot(`${SHOTS}/${n}.png`);
const stap = async (naam, fn) => { try { await fn(); } catch (e) { console.log("STAP MISLUKT:", naam, String(e).slice(0, 300)); } };
const zetVast = (v) => browser.execute((v) => { if (!window.__rwRandom) window.__rwRandom = Math.random; Math.random = () => v; }, v);
const losKans = () => browser.execute(() => { if (window.__rwRandom) { Math.random = window.__rwRandom; window.__rwRandom = undefined; } });
const klik = (i) => browser.execute((i) => { const a = [...document.querySelectorAll(".workspace-leaf-content[data-type=\"markdown\"] .rollwright-roll")].filter((x) => x.offsetParent !== null); a[i]?.click(); return a.length; }, i);
const muisWeg = async () => { try { await browser.$(".view-header").moveTo(); } catch (e) {} await browser.execute(() => { document.querySelectorAll(".tooltip").forEach((t) => t.remove()); document.activeElement?.blur(); }); };
// Echte bouw (Olaf stap 2b): de skin gaat via de instellingen van de plugin, de plugin zet zelf .rollwright-world.
const wereld = (skin, thema, modus) => browser.executeObsidian(async ({ app }, skin, thema, modus) => {
	app.changeTheme(thema);
	const plugin = app.plugins.plugins.rollwright;
	const betaald = skin !== "classic";
	Object.assign(plugin.settings, { skin, licenseKey: betaald ? "E2E-SLEUTEL" : "", licenseCheckedAt: betaald ? Date.now() : 0, noteWorld: "rolls" });
	plugin.applySkin();
	const leaf = app.workspace.getLeavesOfType("markdown")[0];
	await leaf.setViewState({ type: "markdown", state: { ...leaf.view.getState(), mode: modus === "lp" ? "source" : "preview", source: false } });
	await new Promise((r) => setTimeout(r, 600));
	const el = leaf.view.containerEl;
	const cs = getComputedStyle(el.querySelector(".view-content"));
	return { body: document.body.className.split(" ").filter((c) => c.startsWith("rollwright")), wereld: el.classList.contains("rollwright-world"), bg: cs.backgroundColor, beeld: cs.backgroundImage.slice(0, 30), font: getComputedStyle(el.querySelector(".markdown-preview-view p") || document.body).fontFamily.slice(0, 40) };
}, skin, thema, modus);
const meta = {};

const scroll = (wat) => browser.execute((wat) => { const v = document.querySelector('.workspace-leaf-content[data-type="markdown"] .markdown-preview-view'); if (!v) return "geen"; if (wat === "top") v.scrollTop = 0; else { const h = [...v.querySelectorAll("h1,h2,h3,.callout")].find((e) => /wolf/i.test(e.textContent)); if (h) v.scrollTop += h.getBoundingClientRect().top - v.getBoundingClientRect().top - 40; } return v.scrollTop; }, wat);

describe("Rollwright: gratis tegen de werelden, echte bouw", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		meta.css = await browser.executeObsidian(async ({ app }) => {
			app.vault.setConfig("spellcheck", false); app.vault.setConfig("propertiesInDocument", "hidden"); app.vault.setConfig("showInlineTitle", false); app.customCss.setTheme("");
			return "echte bouw, geen eigen css";
		});
		meta.venster = await browser.execute(() => { try { window.require("@electron/remote").getCurrentWindow().setSize(1400, 788); return "remote"; } catch (e) { try { window.resizeTo(1400, 788); return "resizeTo"; } catch (e2) { return String(e2); } } });
		await browser.pause(800);
		await browser.executeObsidian(async ({ app }, pad) => {
			for (let i = 0; i < 40 && !app.vault.getAbstractFileByPath(pad); i++) await new Promise((r) => setTimeout(r, 250));
			await app.plugins.plugins.rollwright.clearHistory();
			app.workspace.leftSplit?.collapse();
			const leaf = app.workspace.getLeaf(false);
			await leaf.openFile(app.vault.getAbstractFileByPath(pad), { state: { mode: "preview" } });
			app.workspace.setActiveLeaf(leaf, { focus: true });
		}, NOTE);
		await browser.pause(1500);
		await browser.executeObsidian(({ app }) => app.commands.executeCommandById("rollwright:open-history"));
		await browser.pause(1200);
		await browser.executeObsidian(({ app }) => { const l = app.workspace.getLeavesOfType("markdown")[0]; if (l) app.workspace.setActiveLeaf(l, { focus: true }); });
		await browser.pause(800);
	});

	for (const [skin, thema] of [["classic", "moonstone"], ["classic", "obsidian"], ["parchment", "moonstone"], ["arcane", "moonstone"]]) {
		it(`vergelijk ${skin} ${thema}`, async function () {
			await stap(skin + thema, async () => {
				meta[`${skin}-${thema}`] = await wereld(skin, thema, "lezen");
				await browser.executeObsidian(async ({ app }) => app.plugins.plugins.rollwright.clearHistory()); await browser.pause(900);
				await scroll("top"); await browser.pause(300);
				for (const [i, k] of [[0, 0.62], [2, 0.8], [3, 0], [4, 0.55]]) { await zetVast(k); await klik(i); await browser.pause(1300); await losKans(); }
				meta[`${skin}-${thema}-scroll`] = await scroll("wolf"); await browser.pause(500);
				await zetVast(0.99999); await klik(1); await losKans(); await browser.pause(2600);
				await muisWeg(); await browser.pause(300);
				await save(`vergelijk-${skin}-${thema}-wolf`);
				await scroll("top"); await browser.pause(500); await muisWeg();
				await save(`vergelijk-${skin}-${thema}-top`);
			});
		});
	}

	after(async function () { try { await browser.executeObsidian(({ app }) => { const p = app.plugins.plugins.rollwright; Object.assign(p.settings, { skin: "classic", licenseKey: "", licenseCheckedAt: 0 }); p.applySkin(); }); } catch (e) {} console.log("META", JSON.stringify(meta)); fs.writeFileSync(`${SHOTS}/meta.json`, JSON.stringify(meta, null, 1)); });
});
