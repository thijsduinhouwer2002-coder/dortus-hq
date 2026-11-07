import { browser, expect } from "@wdio/globals";
import * as fs from "fs";
import { klikWorp } from "./klik-hulp.mjs";

const SHOTS = "screenshots";

describe("Rollwright in de echte Obsidian", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
	});

	it("de plugin is geladen en aan", async function () {
		const enabled = await browser.executeObsidian(({ app }) => app.plugins.enabledPlugins.has("rollwright"));
		expect(enabled).toBe(true);
	});

	it("een dobbelcode rolt in de leesweergave", async function () {
		await browser.executeObsidian(async ({ app }) => {
			const file = app.vault.getAbstractFileByPath("Rollen.md");
			const leaf = app.workspace.getLeaf(false);
			await leaf.openFile(file, { state: { mode: "preview" } });
			app.workspace.setActiveLeaf(leaf, { focus: true });
		});
		const roll = browser.$(".workspace-leaf.mod-active .rollwright-roll .rollwright-value");
		await roll.waitForExist({ timeout: 20000 });
		await browser.waitUntil(async () => /\d/.test(await roll.getProperty("textContent")), {
			timeout: 20000,
			timeoutMsg: "de worp kreeg geen getal",
		});
		const texts = await browser.$$(".workspace-leaf.mod-active .rollwright-roll").map(async (el) => `${await el.getAttribute("aria-label")} = ${await el.getProperty("textContent")}`);
		console.log("WORPEN IN DE NOTITIE:", JSON.stringify(texts));
		await browser.saveScreenshot(`${SHOTS}/1-leesweergave.png`);
	});

	it("bij openen heeft geen worp de klasse rollwright-rolled", async function () {
		const rolled = await browser.execute(() => document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll.rollwright-rolled").length);
		console.log("ROLLED NA OPENEN:", rolled);
		expect(rolled).toBe(0);
	});

	it("klikken rolt opnieuw", async function () {
		const roll = browser.$(".workspace-leaf.mod-active .rollwright-roll");
		const label = async () => `${await roll.getAttribute("aria-label")}|${await roll.getProperty("textContent")}`;
		const before = await label();
		let changed = false;
		for (let i = 0; i < 5 && !changed; i++) {
			await browser.execute((el) => el.click(), await roll.getElement());
			await browser.pause(400);
			changed = (await label()) !== before;
		}
		console.log("VOOR:", before, "NA:", await label());
		console.log("KLIKKEN VERANDERDE DE UITKOMST:", changed);
		expect(changed).toBe(true);
	});

	it("na een klik heeft het vakje de klasse rollwright-rolled", async function () {
		await klikWorp(".workspace-leaf.mod-active", 0);
		await browser.waitUntil(
			async () => browser.execute(() => document.querySelector(".workspace-leaf.mod-active .rollwright-roll")?.classList.contains("rollwright-rolled") === true),
			{ timeout: 5000, timeoutMsg: "na een klik kreeg het vakje geen rollwright-rolled" },
		);
		const classes = await browser.execute(() => document.querySelector(".workspace-leaf.mod-active .rollwright-roll")?.className);
		console.log("KLASSEN NA KLIK:", classes);
	});

	it("de instellingen tonen het betaalde deel", async function () {
		const result = await browser.executeObsidian(async ({ app }) => {
			const tab = app.setting.pluginTabs.find((t) => t.id === "rollwright");
			if (!tab) return { found: false };
			tab.display();
			await new Promise((r) => setTimeout(r, 500));
			const buttons = Array.from(tab.containerEl.querySelectorAll("button")).map((b) => b.textContent);
			const inputs = Array.from(tab.containerEl.querySelectorAll("input")).map((x) => x.placeholder || x.type);
			return { found: true, text: tab.containerEl.innerText, buttons, inputs };
		});
		console.log("INSTELLINGEN ROLLWRIGHT:", JSON.stringify(result, null, 1));
		expect(result.found).toBe(true);
		expect(result.buttons.some((b) => /buy/i.test(b))).toBe(true);
		expect(result.buttons.some((b) => /activate/i.test(b))).toBe(true);
	});
});
