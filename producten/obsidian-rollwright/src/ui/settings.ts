import { Notice, PluginSettingTab, Setting, type App } from "obsidian";
import type RollwrightPlugin from "../main";
import { BUY_URL, isValidLicenseKey, shouldShowBuyButton } from "../pro/license";
import { availableSkins, SKINS } from "../pro/skins";

export class RollwrightSettingTab extends PluginSettingTab {
	constructor(
		app: App,
		private readonly plugin: RollwrightPlugin,
	) {
		super(app, plugin);
	}

	display(): void {
		const { containerEl } = this;
		containerEl.empty();
		const settings = this.plugin.settings;

		new Setting(containerEl)
			.setName("Default die")
			.setDesc("The number of sides when a formula leaves it out, as in 3d.")
			.addText((text) =>
				text.setValue(String(settings.defaultSides)).onChange(async (value) => {
					const sides = Number(value);
					if (!Number.isInteger(sides) || sides < 1) return;
					settings.defaultSides = sides;
					await this.plugin.saveSettings();
				}),
			);

		new Setting(containerEl)
			.setName("Default number of dice")
			.setDesc("The number of dice when a formula leaves it out, as in d6.")
			.addText((text) =>
				text.setValue(String(settings.defaultCount)).onChange(async (value) => {
					const count = Number(value);
					if (!Number.isInteger(count) || count < 0) return;
					settings.defaultCount = count;
					await this.plugin.saveSettings();
				}),
			);

		new Setting(containerEl).setName("Saved formulas").setHeading();

		settings.formulas.forEach((formula, index) => {
			new Setting(containerEl)
				.addText((text) =>
					text.setPlaceholder("Name").setValue(formula.name).onChange(async (value) => {
						formula.name = value.trim();
						await this.plugin.saveSettings();
					}),
				)
				.addText((text) =>
					text.setPlaceholder("Formula").setValue(formula.formula).onChange(async (value) => {
						formula.formula = value.trim();
						await this.plugin.saveSettings();
					}),
				)
				.addExtraButton((button) =>
					button.setIcon("trash").setTooltip("Remove").onClick(async () => {
						settings.formulas.splice(index, 1);
						await this.plugin.saveSettings();
						this.display();
					}),
				);
		});

		new Setting(containerEl)
			.setName("Add a formula")
			.setDesc("Use its name in any roll, such as dice: attack.")
			.addButton((button) =>
				button.setButtonText("Add").onClick(async () => {
					settings.formulas.push({ name: `formula${settings.formulas.length + 1}`, formula: "1d20" });
					await this.plugin.saveSettings();
					this.display();
				}),
			);

		new Setting(containerEl)
			.setName("Import saved formulas")
			.setDesc("Copies named formulas from the data file of the Dice Roller plugin, if you have it. That file is only read, and existing names stay as they are.")
			.addButton((button) =>
				button.setButtonText("Import").onClick(async () => {
					await this.plugin.importSavedFormulas();
					this.display();
				}),
			);

		new Setting(containerEl).setName("Skins").setHeading();

		const paidNames = SKINS.filter((skin) => skin.paid).map((skin) => skin.name).join(" and ");
		new Setting(containerEl)
			.setName("Skin")
			.setDesc(`All rolling is free. ${paidNames} are paid skins and need a license key.`)
			.addDropdown((dropdown) => {
				for (const skin of availableSkins(this.plugin.isLicensed)) dropdown.addOption(skin.id, skin.name);
				dropdown.setValue(settings.skin).onChange(async (value) => {
					settings.skin = value;
					await this.plugin.saveSettings();
					this.plugin.applySkin();
				});
			});

		new Setting(containerEl)
			.setName("License key")
			.setDesc("Checked on this device only. Nothing is sent anywhere.")
			.addText((text) =>
				text.setValue(settings.licenseKey).onChange(async (value) => {
					settings.licenseKey = value.trim();
					await this.plugin.saveSettings();
					this.plugin.applySkin();
				}),
			)
			.addButton((button) =>
				button.setButtonText("Check").onClick(() => {
					new Notice(isValidLicenseKey(settings.licenseKey) ? "The license key is valid." : "This license key is not valid.");
					this.display();
				}),
			);

		if (shouldShowBuyButton()) {
			new Setting(containerEl).setName("Get the paid skins").addButton((button) =>
				button.setButtonText("Buy").onClick(() => {
					activeWindow.open(BUY_URL);
				}),
			);
		}
	}
}
