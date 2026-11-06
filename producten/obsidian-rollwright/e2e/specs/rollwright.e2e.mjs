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
			const leaf = app.workspace.getLeaf(true);
			await leaf.openFile(file, { state: { mode: "preview" } });
		});
		const roll = browser.$(".rollwright-roll .rollwright-value");
		await roll.waitForExist({ timeout: 20000 });
		await browser.waitUntil(async () => /\d/.test(await roll.getText()), {
			timeout: 20000,
			timeoutMsg: "de worp kreeg geen getal",
		});
		const texts = await browser.$$(".rollwright-roll").map((el) => el.getText());
		console.log("WORPEN IN DE NOTITIE:", JSON.stringify(texts));
		await browser.saveScreenshot(`${SHOTS}/1-leesweergave.png`);
	});

	it("klikken rolt opnieuw", async function () {
		const roll = browser.$(".rollwright-roll");
		const before = await roll.getText();
		let changed = false;
		for (let i = 0; i < 5 && !changed; i++) {
			await roll.click();
			await browser.pause(300);
			changed = (await roll.getText()) !== before;
		}
		console.log("KLIKKEN VERANDERDE DE UITKOMST:", changed);
		expect(changed).toBe(true);
	});

	it("de instellingen tonen het betaalde deel", async function () {
		await browser.executeObsidian(({ app }) => {
			app.setting.open();
			app.setting.openTabById("rollwright");
		});
		const content = browser.$(".vertical-tab-content");
		await content.waitForExist({ timeout: 10000 });
		await browser.pause(1500);
		const text = await content.getText();
		console.log("INSTELLINGEN ROLLWRIGHT:\n" + text);
		const buttons = await browser.$$(".vertical-tab-content button").map((el) => el.getText());
		console.log("KNOPPEN:", JSON.stringify(buttons));
		await browser.saveScreenshot(`${SHOTS}/2-instellingen.png`);
		expect(buttons.some((b) => /buy/i.test(b))).toBe(true);
	});
});
