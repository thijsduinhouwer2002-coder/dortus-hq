import { browser } from "@wdio/globals";
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";

// Ontwerptest van Daan (9 nov): beweging per wereld (Kerker en Codex), beeld voor beeld bevroren met de Web Animations API.
// richtingen.css is een prototype bovenop de echte plugin; de worpen zelf zijn echt.
const SHOTS = "screenshots";
const NOTE = "Night at the Tideflats.md";
const HIER = path.dirname(fileURLToPath(import.meta.url));
const save = (n) => browser.saveScreenshot(`${SHOTS}/${n}.png`);
const stap = async (naam, fn) => { try { await fn(); } catch (e) { console.log("STAP MISLUKT:", naam, String(e).slice(0, 300)); } };
const zetVast = (v) => browser.execute((v) => { if (!window.__rwRandom) window.__rwRandom = Math.random; Math.random = () => v; }, v);
const losKans = () => browser.execute(() => { if (window.__rwRandom) { Math.random = window.__rwRandom; window.__rwRandom = undefined; } });
const klik = (i) => browser.execute((i) => { const a = [...document.querySelectorAll(".workspace-leaf-content[data-type=\"markdown\"] .rollwright-roll")].filter((x) => x.offsetParent !== null); a[i]?.click(); return a.length; }, i);
const iconen = () => browser.execute(() => { const a = [...document.querySelectorAll(".workspace-leaf-content[data-type=\"markdown\"] .rollwright-roll")].filter((x) => x.offsetParent !== null);
	a[1]?.classList.add("rwx-ico", "rwx-ico-wolf"); a[3]?.classList.add("rwx-ico", "rwx-ico-trap"); return a.map((x) => x.className + " | " + x.innerHTML.slice(0, 200)); });
const muisWeg = async () => { try { await browser.$(".view-header").moveTo(); } catch (e) {} await browser.execute(() => { document.querySelectorAll(".tooltip").forEach((t) => t.remove()); document.activeElement?.blur(); }); };
const wereld = (w, thema) => browser.executeObsidian(({ app }, w, thema) => {
	for (const c of Array.from(document.body.classList)) if (c.startsWith("rwx-") || c.startsWith("rollwright-skin-")) document.body.classList.remove(c);
	document.body.classList.add(`rwx-${w}`, "rollwright-skin-rwx"); app.changeTheme(thema);
}, w, thema);
const meta = {};

const klikEnVries = (i) => browser.execute((i) => {
	const a = [...document.querySelectorAll(".workspace-leaf-content[data-type=\"markdown\"] .rollwright-roll")].filter((x) => x.offsetParent !== null);
	const el = a[i]; if (!el) return null; el.click();
	const anims = document.getAnimations(); anims.forEach((x) => { x.pause(); x.currentTime = 0; });
	const r = el.getBoundingClientRect(); return { n: anims.length, namen: anims.map((x) => x.animationName || x.constructor.name), r: [r.x, r.y, r.width, r.height], cls: el.className };
}, i);
const zetTijd = (t) => browser.execute((t) => { document.getAnimations().forEach((x) => { x.pause(); x.currentTime = t; }); return document.getAnimations().length; }, t);
const TIJDEN = [0, 120, 240, 360, 480, 620, 800, 1000, 1300, 1700, 2200];

describe("Rollwright skins: beweging per wereld", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		const css = fs.readFileSync(path.join(HIER, "richtingen", "richtingen.css"), "utf8");
		meta.css = await browser.executeObsidian(async ({ app }, css) => {
			app.vault.setConfig("spellcheck", false); app.customCss.setTheme("");
			const st = document.createElement("style"); st.id = "rwx-richtingen"; st.textContent = css; document.head.appendChild(st);
			return css.length;
		}, css);
		meta.venster = await browser.execute(() => { try { const w = window.require("@electron/remote").getCurrentWindow(); w.setSize(1400, 788); return "remote"; } catch (e) { try { window.resizeTo(1400, 788); return "resizeTo"; } catch (e2) { return String(e2); } } });
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
		meta.views = await browser.execute(() => [...document.querySelectorAll(".workspace-leaf-content")].map((l) => l.dataset.type));
		await browser.pause(800);
	});

	for (const [w, thema] of [["kerker", "obsidian"], ["codex", "moonstone"]]) {
		it(`beweging ${w}`, async function () {
			await stap(w, async () => {
				await wereld(w, thema); await browser.executeObsidian(async ({ app }) => app.plugins.plugins.rollwright.clearHistory()); await browser.pause(600);
				await iconen();
				await browser.execute(() => { const sc = document.querySelector(".workspace-leaf-content[data-type=\"markdown\"] .markdown-preview-view"); if (sc) sc.scrollTop = 230; });
				await browser.pause(500); await muisWeg();
				for (const [i, k, naam] of [[1, 0.99999, "nat20"], [3, 0, "nat1"], [2, 0.8, "gewoon"]]) {
					await zetVast(k); const info = await klikEnVries(i); await losKans(); await iconen(); await muisWeg();
					meta[`${w}-${naam}`] = info; console.log("BEWEGING", w, naam, JSON.stringify(info).slice(0, 400));
					await browser.pause(700); // laat het doortellen (JS) uitlopen; de CSS staat stil
					for (const t of TIJDEN) { await zetTijd(t); await browser.pause(60); await save(`beweging-${w}-${naam}-${String(t).padStart(4, "0")}`); }
					await browser.execute(() => document.getAnimations().forEach((x) => x.finish()));
				}
				await browser.pause(400); await save(`beweging-${w}-eind`);
			});
		});
	}

	after(async function () { fs.writeFileSync(`${SHOTS}/meta.json`, JSON.stringify(meta, null, 1)); });
});
