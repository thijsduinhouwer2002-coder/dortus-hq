import { browser } from "@wdio/globals";
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";

// Ontwerptest van Daan (9 nov): de skin kleurt de hele notitie (ontwerp-notitiesfeer.md).
// wereld.css is een prototype; de spec zet zelf .rollwright-world op view.containerEl, zoals Olafs code dat straks doet.
const SHOTS = "screenshots";
const NOTE = "Night at the Tideflats.md";
const HIER = path.dirname(fileURLToPath(import.meta.url));
const save = (n) => browser.saveScreenshot(`${SHOTS}/${n}.png`);
const stap = async (naam, fn) => { try { await fn(); } catch (e) { console.log("STAP MISLUKT:", naam, String(e).slice(0, 300)); } };
const zetVast = (v) => browser.execute((v) => { if (!window.__rwRandom) window.__rwRandom = Math.random; Math.random = () => v; }, v);
const losKans = () => browser.execute(() => { if (window.__rwRandom) { Math.random = window.__rwRandom; window.__rwRandom = undefined; } });
const klik = (i) => browser.execute((i) => { const a = [...document.querySelectorAll(".workspace-leaf-content[data-type=\"markdown\"] .rollwright-roll")].filter((x) => x.offsetParent !== null); a[i]?.click(); return a.length; }, i);
const muisWeg = async () => { try { await browser.$(".view-header").moveTo(); } catch (e) {} await browser.execute(() => { document.querySelectorAll(".tooltip").forEach((t) => t.remove()); document.activeElement?.blur(); }); };
const wereld = (skin, thema, modus) => browser.executeObsidian(async ({ app }, skin, thema, modus) => {
	for (const c of Array.from(document.body.classList)) if (c.startsWith("rollwright-skin-")) document.body.classList.remove(c);
	document.body.classList.add(`rollwright-skin-${skin}`); app.changeTheme(thema);
	const leaf = app.workspace.getLeavesOfType("markdown")[0];
	await leaf.setViewState({ type: "markdown", state: { ...leaf.view.getState(), mode: modus === "lp" ? "source" : "preview", source: false } });
	leaf.view.containerEl.classList.add("rollwright-world");
	const cs = getComputedStyle(leaf.view.containerEl.querySelector(".view-content"));
	const kop = leaf.view.containerEl.querySelector(".view-header"); const kc = kop ? getComputedStyle(kop) : null;
	const pad = []; for (let e = kop; e && e !== document.body; e = e.parentElement) pad.push(e.className.slice(0, 60) + " bg=" + getComputedStyle(e).backgroundColor + " img=" + getComputedStyle(e).backgroundImage.slice(0, 30));
	return { kop: kc ? [kc.backgroundColor, kc.backgroundImage.slice(0, 40), kc.color] : "geen kop in containerEl", pad, cls: leaf.view.containerEl.className, bg: cs.backgroundColor, font: getComputedStyle(leaf.view.containerEl.querySelector(".cm-content, .markdown-preview-view") || document.body).fontFamily.slice(0, 40) };
}, skin, thema, modus);
const meta = {};

describe("Rollwright: de skin kleurt de hele notitie", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		const css = fs.readFileSync(path.join(HIER, "wereld", "wereld.css"), "utf8");
		meta.css = await browser.executeObsidian(async ({ app }, css) => {
			app.vault.setConfig("spellcheck", false); app.customCss.setTheme("");
			const st = document.createElement("style"); st.id = "rw-wereld"; st.textContent = css; document.head.appendChild(st);
			return css.length;
		}, css);
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

	for (const [skin, thema, modus] of [["parchment", "obsidian", "lezen"], ["parchment", "moonstone", "lezen"], ["arcane", "obsidian", "lezen"], ["arcane", "moonstone", "lezen"], ["parchment", "obsidian", "lp"], ["arcane", "moonstone", "lp"]]) {
		it(`wereld ${skin} ${thema} ${modus}`, async function () {
			await stap(skin + thema + modus, async () => {
				meta[`${skin}-${thema}-${modus}`] = await wereld(skin, thema, modus);
				await browser.executeObsidian(async ({ app }) => app.plugins.plugins.rollwright.clearHistory()); await browser.pause(900);
				for (const [i, k] of [[0, 0.62], [2, 0.8], [3, 0], [4, 0.55], [1, 0.99999]]) { await zetVast(k); await klik(i); await browser.pause(1300); await losKans(); }
				await muisWeg(); await browser.pause(400);
				await save(`wereld-${skin}-${thema}-${modus}`);
			});
		});
	}

	it("classic blijft rustig", async function () {
		await stap("classic", async () => {
			meta.classic = await wereld("classic", "obsidian", "lezen"); await browser.pause(600); await muisWeg();
			await save("wereld-classic-obsidian-lezen");
		});
	});

	after(async function () { console.log("META", JSON.stringify(meta)); fs.writeFileSync(`${SHOTS}/meta.json`, JSON.stringify(meta, null, 1)); });
});
