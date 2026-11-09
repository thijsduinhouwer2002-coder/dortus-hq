import { browser } from "@wdio/globals";
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";

// Ontwerptest van Daan (9 nov): drie richtingen voor de betaalde skins, elk groot (16:9) in een echte notitie.
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

describe("Rollwright skins: drie richtingen", function () {
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

	for (const [w, thema] of [["taverne", "obsidian"], ["kerker", "obsidian"], ["codex", "moonstone"]]) {
		it(`richting ${w}`, async function () {
			await stap(w, async () => {
				await wereld(w, thema); await browser.executeObsidian(async ({ app }) => app.plugins.plugins.rollwright.clearHistory()); await browser.pause(600);
				await browser.execute(() => { const sc = document.querySelector(".workspace-leaf-content[data-type=\"markdown\"] .markdown-preview-view"); if (sc) sc.scrollTop = 0; });
				for (const [i, k] of [[0, 0.62], [2, 0.8], [3, 0], [4, 0.55], [1, 0.99999]]) { await zetVast(k); await klik(i); await browser.pause(1300); await losKans(); }
				meta[w] = await iconen(); await muisWeg(); await browser.pause(400);
				await save(`richting-${w}`);
				await browser.execute(() => { const sc = document.querySelector(".workspace-leaf-content[data-type=\"markdown\"] .markdown-preview-view"); if (sc) sc.scrollTop = 230; });
				await browser.pause(300); await save(`richting-${w}-b`);
			});
		});
	}

	after(async function () { fs.writeFileSync(`${SHOTS}/meta.json`, JSON.stringify(meta, null, 1)); });
});
