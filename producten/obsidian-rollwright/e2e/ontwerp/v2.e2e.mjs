import { browser } from "@wdio/globals";
import * as fs from "fs";

// Ontwerptest v2 van Daan: plaatjes van het voorstel in ontwerp-v2.md. Elke stap vangt zijn eigen fout.
const SHOTS = "screenshots";
let n = 0;
const shot = async (naam, el) => {
	n += 1;
	const file = `${SHOTS}/v2-${String(n).padStart(2, "0")}-${naam}.png`;
	if (el) await el.saveScreenshot(file); else await browser.saveScreenshot(file);
	console.log("SCHERM:", file);
};
const stap = async (naam, fn) => {
	try { await fn(); } catch (e) { console.log("STAP MISLUKT:", naam, String(e).slice(0, 300)); }
};
const NOTE = "The Rusty Flagon.md";
const open = async (pad, mode) => {
	await browser.executeObsidian(async ({ app }, pad, mode) => {
		const leaf = app.workspace.getLeaf(false);
		await leaf.openFile(app.vault.getAbstractFileByPath(pad), { state: { mode, source: false } });
		app.workspace.setActiveLeaf(leaf, { focus: true });
	}, pad, mode);
	await browser.pause(1500);
};
const thema = async (naam, licht) => {
	await browser.executeObsidian(({ app }, naam, licht) => { app.customCss.setTheme(naam); app.changeTheme(licht ? "moonstone" : "obsidian"); }, naam, licht);
	await browser.pause(1500);
};
const skin = async (s) => {
	await browser.execute((k) => {
		document.body.classList.remove("rollwright-skin-classic", "rollwright-skin-parchment", "rollwright-skin-arcane");
		document.body.classList.add(k);
	}, `rollwright-skin-${s}`);
	await browser.pause(300);
};
// Zet de klasse die Olaf straks na een klik zet, en markeer de saving throw als 20 en de schade als 1-1 (nagebootst).
const markeer = async () => {
	await browser.execute(() => {
		const rolls = [...document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll")];
		for (const r of rolls) r.classList.add("rollwright-rolled");
		const save = rolls.find((r) => r.textContent.includes("Wisdom"));
		if (save) { save.classList.add("rollwright-crit"); save.querySelector(".rollwright-value").textContent = "20"; }
		const dmg = rolls.find((r) => r.textContent.includes("Damage"));
		if (dmg) { dmg.classList.add("rollwright-fumble"); dmg.querySelector(".rollwright-value").textContent = "5"; }
	});
};
const klik = async (woord) => {
	await browser.execute((w) => {
		const r = [...document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll")].find((x) => x.textContent.includes(w));
		r?.click();
	}, woord);
};
const zoom = async (f) => {
	await browser.execute((f) => { try { window.require("electron").webFrame.setZoomFactor(f); } catch (e) { document.body.style.zoom = String(f); } }, f);
	await browser.pause(600);
};
const zijpaneelDicht = async () => {
	await browser.executeObsidian(({ app }) => { app.workspace.leftSplit?.collapse(); app.workspace.rightSplit?.collapse(); });
};

describe("Rollwright v2 voorstel", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.setWindowSize(1280, 820).catch(() => {});
		await zijpaneelDicht();
	});

	it("licht en donker, lezen en Live Preview, met crit en fumble", async function () {
		for (const licht of [true, false]) {
			const kant = licht ? "licht" : "donker";
			await stap(`notitie ${kant}`, async () => {
				await thema("", licht);
				await open(NOTE, "preview");
				await markeer();
				await browser.pause(2500);
				await browser.execute(() => document.activeElement?.blur());
				await shot(`notitie-${kant}`);
				await zoom(2);
				await shot(`notitie-${kant}-zoom`);
				await zoom(1);
			});
		}
		await stap("live preview", async () => {
			await thema("", true);
			await open(NOTE, "source");
			await markeer();
			await browser.pause(2500);
			await shot("live-preview-licht");
		});
	});

	it("de worp rolt, vertraagd 8 keer", async function () {
		for (const [woord, naam] of [["Initiative", "gewoon"], ["Wisdom", "crit"], ["Damage", "fumble"]]) {
			await stap(`rollen ${naam}`, async () => {
				await thema("", true);
				await open(NOTE, "preview");
				await zoom(2.5);
				await markeer();
				await browser.execute(() => document.body.style.setProperty("--rw-slow", "8"));
				await klik(woord);
				// Na de klik tekent de widget opnieuw; zet crit of fumble weer zoals Olaf dat straks doet.
				await browser.pause(60);
				await markeer();
				for (const ms of [250, 900, 1800, 4500, 8000]) {
					await browser.pause(ms === 250 ? 250 : ms - [250, 900, 1800, 4500, 8000][[250, 900, 1800, 4500, 8000].indexOf(ms) - 1]);
					await shot(`rol-${naam}-${ms}ms`);
				}
				await browser.execute(() => document.body.style.setProperty("--rw-slow", "1"));
				await zoom(1);
			});
		}
	});

	it("het logboek", async function () {
		for (const licht of [true, false]) {
			const kant = licht ? "licht" : "donker";
			await stap(`logboek ${kant}`, async () => {
				await thema("", licht);
				await open(NOTE, "preview");
				if (licht) {
					for (const w of ["Rumour", "Initiative", "Hit", "guests", "Wisdom", "Damage", "stranger says"]) { await klik(w); await browser.pause(500); }
				}
				await browser.executeObsidian(({ app }) => app.commands.executeCommandById("rollwright:open-history"));
				await browser.pause(1500);
				await browser.execute(() => document.activeElement?.blur());
				await shot(`logboek-${kant}`);
				const paneel = await browser.$(".rollwright-history");
				if (await paneel.isExisting()) await shot(`logboek-${kant}-paneel`, paneel);
			});
		}
		await zijpaneelDicht();
	});

	it("thema's en skins", async function () {
		for (const [t, licht] of [["Minimal", false], ["AnuPpuccin", true], ["Things", true], ["Border", false]]) {
			await stap(`thema ${t}`, async () => {
				await thema(t, licht);
				await open(NOTE, "preview");
				await markeer();
				await browser.pause(1500);
				await shot(`thema-${t}-${licht ? "licht" : "donker"}`);
			});
		}
		await thema("", true);
		for (const s of ["parchment", "arcane"]) {
			for (const licht of [true, false]) {
				await stap(`skin ${s}`, async () => {
					await thema("", licht);
					await open(NOTE, "preview");
					await skin(s);
					await markeer();
					await browser.pause(1500);
					await shot(`skin-${s}-${licht ? "licht" : "donker"}`);
				});
			}
		}
		await skin("classic");
		await thema("", true);
	});

	it("skins in de instellingen", async function () {
		await stap("instellingen", async () => {
			await browser.executeObsidian(async ({ app }) => {
				app.setting.open();
				await new Promise((r) => setTimeout(r, 600));
				app.setting.openTabById("rollwright");
			});
			await browser.pause(1200);
			await browser.execute(() => {
				const tegel = document.querySelector(".rollwright-skin-preview");
				tegel?.scrollIntoView({ block: "center" });
			});
			await browser.pause(500);
			await shot("instellingen-skins");
			await browser.executeObsidian(({ app }) => app.setting.close());
		});
	});
});
