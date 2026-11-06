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
		const text = await roll.getText();
		expect(text).toMatch(/\d/);
		await browser.saveScreenshot(`${SHOTS}/1-leesweergave.png`);
	});

	it("de instellingen tonen de koopknop en het sleutelveld", async function () {
		await browser.executeObsidian(({ app }) => {
			app.setting.open();
			app.setting.openTabById("rollwright");
		});
		await browser.pause(1500);
		await browser.saveScreenshot(`${SHOTS}/2-instellingen.png`);
		const buy = await browser.$$("button*=Buy");
		expect(buy.length).toBeGreaterThan(0);
	});
});
