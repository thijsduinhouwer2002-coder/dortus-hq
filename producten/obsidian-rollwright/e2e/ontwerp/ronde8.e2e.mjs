import { browser } from "@wdio/globals";
import * as fs from "fs";

// Ontwerptest ronde 8 van Daan: de eerste minuut (leeg logboek, knop, voorbeeldnotitie), het logboek met
// kopjes per sessie (klus 5) en een token tegen de rechterrand. Alleen plaatjes en metingen in het log.
const SHOTS = "screenshots";
let n = 0;
const shot = async (naam, el) => {
	n += 1;
	const file = `${SHOTS}/r8-${String(n).padStart(2, "0")}-${naam}.png`;
	if (el) await el.saveScreenshot(file); else await browser.saveScreenshot(file);
	console.log("SCHERM:", file);
};
const stap = async (naam, fn) => {
	try { await fn(); } catch (e) { console.log("STAP MISLUKT:", naam, String(e).slice(0, 300)); }
};
const PANEEL = '.workspace-leaf-content[data-type="rollwright-history"]';
const thema = async (naam, licht) => {
	await browser.executeObsidian(({ app }, naam, licht) => { app.customCss.setTheme(naam); app.changeTheme(licht ? "moonstone" : "obsidian"); }, naam, licht);
	await browser.pause(1200);
};
const open = async (pad, mode) => {
	await browser.executeObsidian(async ({ app }, pad, mode) => {
		const leaf = app.workspace.getLeaf(false);
		await leaf.openFile(app.vault.getAbstractFileByPath(pad), { state: { mode, source: false } });
		app.workspace.setActiveLeaf(leaf, { focus: true });
	}, pad, mode);
	await browser.pause(1500);
};
const muisWeg = async () => {
	try { await browser.$(".view-header-title-container, .view-header").moveTo(); } catch (e) {}
	await browser.execute(() => { document.querySelectorAll(".tooltip").forEach((t) => t.remove()); document.activeElement?.blur(); });
};
const zetKans = async (h) => browser.execute((h) => { if (!window.__rwRandom) window.__rwRandom = Math.random; Math.random = () => (h ? 0.99999 : 0); }, h);
const losKans = async () => browser.execute(() => { if (window.__rwRandom) { Math.random = window.__rwRandom; window.__rwRandom = undefined; } });
const klik = async (woord) => browser.execute((w) => {
	const r = [...document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll")].filter((x) => x.offsetParent !== null).find((x) => x.textContent.includes(w));
	r?.click();
	return !!r;
}, woord);
const zoom = async (f) => {
	await browser.execute((f) => { try { window.require("electron").webFrame.setZoomFactor(f); } catch (e) { document.body.style.zoom = String(f); } }, f);
	await browser.pause(600);
};
const legLogboek = async () => browser.executeObsidian(async ({ app }) => {
	const p = app.plugins.plugins.rollwright;
	await p.clearHistory();
	await p.openHistory();
});
const rechtsDicht = async () => browser.executeObsidian(({ app }) => { app.workspace.leftSplit?.collapse(); app.workspace.rightSplit?.collapse(); });
const paneelMaat = async () => browser.execute((sel) => {
	const p = document.querySelector(sel);
	if (!p) return "geen paneel";
	const b = p.getBoundingClientRect();
	const kop = [...p.querySelectorAll(".rollwright-history-group-title")].map((t) => t.textContent.trim());
	const items = p.querySelectorAll(".rollwright-history-item").length;
	const knop = p.querySelector(".rollwright-history-try");
	const kb = knop?.getBoundingClientRect();
	return `breed=${Math.round(b.width)} hoog=${Math.round(b.height)} kopjes=${JSON.stringify(kop)} items=${items} knop=${knop ? `${Math.round(kb.width)}x${Math.round(kb.height)} "${knop.textContent}"` : "geen"}`;
}, PANEEL);

describe("Rollwright ronde 8: eerste minuut, logboek, rechterrand", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.setWindowSize(1280, 820).catch(() => {});
		await browser.executeObsidian(({ app }) => app.vault.setConfig("spellcheck", false)).catch(() => {});
		await browser.executeObsidian(({ app }) => { app.workspace.leftSplit?.collapse(); });
	});

	it("leeg logboek en de knop, licht en donker", async function () {
		for (const licht of [true, false]) {
			const kant = licht ? "licht" : "donker";
			await stap(`leeg ${kant}`, async () => {
				await thema("", licht);
				await legLogboek();
				await browser.pause(1200);
				await muisWeg();
				console.log(`LEEG ${kant}:`, await paneelMaat());
				await shot(`leeg-${kant}`);
				const p = await browser.$(PANEEL);
				if (await p.isExisting()) await shot(`leeg-${kant}-paneel`, p);
			});
		}
	});

	it("knop maakt de voorbeeldnotitie, zoals een nieuwe gebruiker hem ziet", async function () {
		await stap("knop", async () => {
			await thema("", true);
			await legLogboek();
			await browser.pause(800);
			const knop = await browser.$(`${PANEEL} .rollwright-history-try`);
			await knop.click();
			await browser.pause(2500);
			const info = await browser.executeObsidian(({ app }) => {
				const leaf = app.workspace.getMostRecentLeaf();
				return `bestand=${app.workspace.getActiveFile()?.path} modus=${leaf?.view?.getMode?.()} bron=${leaf?.view?.getState?.()?.source}`;
			});
			console.log("NA KNOP:", info);
			await muisWeg();
			await shot("voorbeeld-eerste-blik");
		});
		for (const licht of [true, false]) {
			const kant = licht ? "licht" : "donker";
			for (const mode of ["preview", "source"]) {
				await stap(`voorbeeld ${kant} ${mode}`, async () => {
					await thema("", licht);
					await open("Rollwright example.md", mode);
					await browser.pause(1500);
					await muisWeg();
					await shot(`voorbeeld-${kant}-${mode === "preview" ? "lezen" : "lp"}`);
				});
			}
		}
	});

	it("het logboek na een avondje spelen, met kopjes", async function () {
		await stap("rollen", async () => {
			await thema("", true);
			await legLogboek();
			await open("Rollwright example.md", "preview");
			for (const w of ["Initiative", "Hit", "Damage", "bar", "Wisdom", "stranger"]) {
				await browser.pause(300);
				if (w === "Wisdom") await zetKans(true);
				if (w === "Damage") await zetKans(false);
				await klik(w);
				await browser.pause(700);
				await losKans();
			}
			// Tabellen apart, op hun plek (index 4 en 5), want een tabeluitkomst is wat ronde 8 moet tonen.
			for (const i of [4, 5]) {
				const ok = await browser.execute((i) => { const a = [...document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll")].filter((x) => x.offsetParent !== null); a[i]?.click(); return a.length; }, i);
				console.log("TABEL KLIK", i, "van", ok);
				await browser.pause(900);
			}
			await open("The Rusty Flagon.md", "preview");
			for (const w of ["Hit"]) { await klik(w); await browser.pause(700); }
			await browser.executeObsidian(({ app }) => app.commands.executeCommandById("rollwright:open-history"));
			await browser.pause(1200);
			console.log("LOGBOEK VOL:", await paneelMaat());
			// Nagebootst tot Olaf klus 9 bouwt: uitkomsten die geen getal zijn krijgen rollwright-history-text.
			const tekst = await browser.execute((sel) => {
				let n = 0;
				document.querySelectorAll(`${sel} .rollwright-history-item`).forEach((it) => {
					const r = it.querySelector(".rollwright-history-result")?.textContent?.trim() ?? "";
					if (!/^-?\d+$/.test(r)) { it.classList.add("rollwright-history-text"); n += 1; }
				});
				return n;
			}, PANEEL);
			console.log("TEKSTKAARTEN (nagebootst):", tekst);
		});
		for (const licht of [true, false]) {
			const kant = licht ? "licht" : "donker";
			await stap(`logboek ${kant}`, async () => {
				await thema("", licht);
				await muisWeg();
				await shot(`logboek-${kant}`);
				const p = await browser.$(PANEEL);
				if (await p.isExisting()) await shot(`logboek-${kant}-paneel`, p);
			});
		}
		for (const [t, licht] of [["Minimal", false], ["AnuPpuccin", true]]) {
			await stap(`logboek ${t}`, async () => {
				await thema(t, licht);
				await muisWeg();
				const p = await browser.$(PANEEL);
				if (await p.isExisting()) await shot(`logboek-${t}-paneel`, p);
			});
		}
		await thema("", true);
	});

	it("skin-tegels in de instellingen (klus 7)", async function () {
		for (const licht of [true, false]) {
			const kant = licht ? "licht" : "donker";
			await stap(`tegels ${kant}`, async () => {
				await thema("", licht);
				const r = await browser.executeObsidian(async ({ app }) => {
					app.setting.open();
					app.setting.openTabById("rollwright");
					await new Promise((res) => setTimeout(res, 1200));
					const el = app.setting.modalEl;
					el?.querySelector(".rollwright-skin-preview")?.scrollIntoView({ block: "center" });
					return `tab=${app.setting.activeTab?.id} tegels=${el?.querySelectorAll(".rollwright-skin-preview-tile").length} slotjes=${el?.querySelectorAll(".rollwright-skin-preview-lock").length}`;
				});
				console.log(`TEGELS ${kant}:`, r);
				await browser.pause(700);
				const hoofd = await browser.getWindowHandle();
				const ander = (await browser.getWindowHandles()).find((h) => h !== hoofd);
				try {
					if (ander) await browser.switchToWindow(ander);
					await shot(`tegels-${kant}`);
					const t = await browser.$(".rollwright-skin-preview");
					if (await t.isExisting()) await shot(`tegels-${kant}-los`, t);
				} finally {
					await browser.switchToWindow(hoofd);
				}
				await browser.executeObsidian(({ app }) => { try { app.setting.close(); } catch (e) {} });
				await browser.pause(500);
			});
		}
		await thema("", true);
	});

	it.skip("smal venster (setWindowSize werkt niet in deze Obsidian)", async function () {
		await stap("smal", async () => {
			await browser.setWindowSize(700, 820);
			await browser.pause(1200);
			await open("Rollwright example.md", "preview");
			await muisWeg();
			await shot("smal-voorbeeld");
			await browser.executeObsidian(({ app }) => app.commands.executeCommandById("rollwright:open-history"));
			await browser.pause(1200);
			await muisWeg();
			await shot("smal-logboek");
			await browser.setWindowSize(1280, 820);
			await browser.pause(800);
		});
	});

	it("token tegen de rechterrand, met sticker", async function () {
		await stap("rand", async () => {
			const tekst = [
				"The bandit captain draws a rusty blade and lunges across the table at you, your turn: `dice: 1d20|text(Parry)`",
				"",
				"A long line of words that keeps going and going until the roll ends up right at the very edge of the page `dice: 1d20|text(Dodge)`",
				"",
			].join("\n");
			await browser.executeObsidian(async ({ app }, tekst) => {
				const f = app.vault.getAbstractFileByPath("Rand.md");
				if (f) await app.vault.modify(f, tekst); else await app.vault.create("Rand.md", tekst);
			}, tekst);
			await rechtsDicht();
			for (const breed of [1024]) {
				await open("Rand.md", "preview");
				await zetKans(true); await klik("Parry"); await browser.pause(900); await losKans();
				await zetKans(true); await klik("Dodge"); await browser.pause(900); await losKans();
				const m = await browser.execute(() => [...document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll")].filter((x) => x.offsetParent !== null).map((r) => {
					const b = r.getBoundingClientRect();
					const st = r.querySelector(".rollwright-stamp, [class*='stamp']");
					const sb = st?.getBoundingClientRect();
					const pagina = r.closest(".markdown-preview-sizer, .cm-content")?.getBoundingClientRect();
					return `${r.textContent.trim()} token=[${Math.round(b.left)},${Math.round(b.right)}] sticker=${sb ? `[${Math.round(sb.left)},${Math.round(sb.right)}] boven=${Math.round(sb.top)}` : "geen"} paginarand=${pagina ? Math.round(pagina.right) : "?"} venster=${window.innerWidth}`;
				}));
				console.log(`RAND ${breed}:`, JSON.stringify(m));
				await muisWeg();
				await shot(`rand-${breed}`);
				await zoom(2);
				await browser.execute(() => [...document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll")].filter((x) => x.offsetParent !== null)[1]?.scrollIntoView({ block: "center", inline: "end" }));
				await browser.pause(300);
				await shot(`rand-${breed}-zoom`);
				await zoom(1);
			}
		});
	});
});
