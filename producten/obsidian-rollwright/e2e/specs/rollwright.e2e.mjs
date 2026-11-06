import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

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

	it("de instellingen tonen het betaalde deel", async function () {
		await browser.executeObsidian(({ app }) => {
			app.setting.open();
			app.setting.openTabById("rollwright");
		});
		await browser.pause(1000);
		const classes = await browser.execute(() => Array.from(document.querySelectorAll(".modal-container .modal")).map((m) => m.className));
		console.log("OPEN VENSTERS:", JSON.stringify(classes));
		const content = browser.$(".mod-settings .vertical-tab-content");
		await content.waitForExist({ timeout: 10000 });
		await browser.pause(1500);
		const text = await content.getProperty("innerText");
		console.log("INSTELLINGEN ROLLWRIGHT:\n" + text);
		const buttons = await browser.$$(".mod-settings .vertical-tab-content button").map((el) => el.getProperty("textContent"));
		console.log("KNOPPEN:", JSON.stringify(buttons));
		await browser.saveScreenshot(`${SHOTS}/2-instellingen.png`);
		expect(buttons.some((b) => /buy/i.test(b))).toBe(true);
	});
});
