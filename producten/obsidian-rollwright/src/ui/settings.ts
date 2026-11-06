import { PluginSettingTab, Setting, type App } from "obsidian";
import type RollwrightPlugin from "../main";
import { BUY_URL, LICENSE_MESSAGES, paymentReady } from "../pro/license";
import { availableSkins, SKINS } from "../pro/skins";

/** A whole number of at least min, or null for anything else, an empty field included. */
export function parseWholeNumber(value: string, min: number): number | null {
	const text = value.trim();
	if (!/^\d+$/.test(text)) return null;
	const number = Number(text);
	return Number.isSafeInteger(number) && number >= min ? number : null;
}

export const COMING_SOON = "Paid skins are coming soon.";

/** The line under the key field: active since a date, or what went wrong, in plain words. */
export function licenseStatus(active: boolean, checkedAt: number, error: keyof typeof LICENSE_MESSAGES | null): string {
	if (error !== null) return LICENSE_MESSAGES[error];
	if (active) return `Active, checked on ${new Date(checkedAt).toLocaleDateString()}.`;
	return "Paste the license key from your Polar purchase and press Activate.";
}

export class RollwrightSettingTab extends PluginSettingTab {
	/** The outcome of the last Activate that failed, shown until the next try. */
	private lastError: keyof typeof LICENSE_MESSAGES | null = null;

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
					const sides = parseWholeNumber(value, 1);
					if (sides === null) return;
					settings.defaultSides = sides;
					await this.plugin.saveSettings();
				}),
			);

		new Setting(containerEl)
			.setName("Default number of dice")
			.setDesc("The number of dice when a formula leaves it out, as in d6.")
			.addText((text) =>
				text.setValue(String(settings.defaultCount)).onChange(async (value) => {
					const count = parseWholeNumber(value, 0);
					if (count === null) return;
					settings.defaultCount = count;
					await this.plugin.saveSettings();
				}),
			);

		new Setting(containerEl)
			.setName("Keep the formula when a dice-mod code is replaced")
			.setDesc("On: 3d6 -> [2, 5, 4] -> 11. Off: [2, 5, 4] -> 11. Results of tables, lists and notes never show a formula.")
			.addToggle((toggle) =>
				toggle.setValue(settings.diceModFormula).onChange(async (value) => {
					settings.diceModFormula = value;
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
			.setDesc(`All rolling is free. ${paidNames} are paid skins and need a license key.${paymentReady(this.plugin.polarIds) ? "" : ` ${COMING_SOON}`}`)
			.addDropdown((dropdown) => {
				for (const skin of availableSkins(this.plugin.isLicensed)) dropdown.addOption(skin.id, skin.name);
				dropdown.setValue(settings.skin).onChange(async (value) => {
					settings.skin = value;
					await this.plugin.saveSettings();
					this.plugin.applySkin();
				});
			});

		if (!paymentReady(this.plugin.polarIds)) {
			new Setting(containerEl).setName("License key").setDesc(COMING_SOON);
			return;
		}

		let draft = settings.licenseKey;
		const status = licenseStatus(this.plugin.isLicensed, settings.licenseCheckedAt, this.lastError);
		new Setting(containerEl)
			.setName("License key")
			.setDesc(`${status} The key is checked with Polar, at most once every 30 days.`)
			.addText((text) =>
				text.setPlaceholder("Your license key").setValue(draft).onChange((value) => {
					draft = value.trim();
				}),
			)
			.addButton((button) =>
				button.setButtonText("Activate").onClick(async () => {
					button.setDisabled(true);
					const outcome = await this.plugin.activateLicense(draft);
					this.lastError = outcome === "valid" ? null : outcome;
					this.display();
				}),
			);

		new Setting(containerEl).setName("Get the paid skins").addButton((button) =>
			button.setButtonText("Buy").onClick(() => {
				activeWindow.open(BUY_URL);
			}),
		);
	}
}
