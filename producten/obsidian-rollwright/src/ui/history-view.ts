import { ItemView, Notice, setIcon, type WorkspaceLeaf } from "obsidian";
import type RollwrightPlugin from "../main";
import type { HistoryEntry } from "../main";
import { groupHistory, noteName } from "./history-groups";
import { historyLabel } from "./history-label";
import { extremeClasses, STAMP_CLASS } from "./widget";

/** The view type id stays "rollwright-history" so layouts saved before the rename to "Roll log" keep working. */
export const HISTORY_VIEW = "rollwright-history";

export class RollHistoryView extends ItemView {
	constructor(
		leaf: WorkspaceLeaf,
		private readonly plugin: RollwrightPlugin,
	) {
		super(leaf);
		this.icon = "dices";
	}

	getViewType(): string {
		return HISTORY_VIEW;
	}

	getDisplayText(): string {
		return "Roll log";
	}

	async onOpen(): Promise<void> {
		this.refresh();
		await Promise.resolve();
	}

	/**
	 * The note a roll from the panel belongs to. Typing in the panel makes the panel the active view, so
	 * the active markdown view is often gone; then the note that was open last counts. "" without one.
	 */
	private panelSource(): string {
		const active = this.plugin.currentNotePath();
		if (active !== "") return active;
		const file = this.app?.workspace?.getActiveFile?.();
		return file?.extension === "md" ? file.path : "";
	}

	/** A roll from the panel: it goes into the log (freshResult does that) and also shows as a notice. */
	private async rollAndNotify(formula: string): Promise<void> {
		try {
			const outcome = await this.plugin.freshResult(null, formula, this.panelSource());
			new Notice(`${formula}: ${outcome.text}`);
		} catch (error) {
			new Notice(error instanceof Error ? error.message : String(error));
		}
	}

	refresh(): void {
		const root = this.contentEl;
		root.empty();
		root.addClass("rollwright-history");

		const form = root.createEl("form", { cls: "rollwright-history-form" });
		const input = form.createEl("input", { type: "text", placeholder: "1d20 + 5" });
		input.setAttribute("aria-label", "Formula");
		form.createEl("button", { text: "Roll", type: "submit" });
		form.addEventListener("submit", (event) => {
			event.preventDefault();
			if (input.value.trim() !== "") void this.rollAndNotify(input.value.trim());
		});

		const saved = this.plugin.settings.formulas;
		if (saved.length > 0) {
			const row = root.createDiv({ cls: "rollwright-history-saved" });
			for (const formula of saved) {
				const button = row.createEl("button", { text: formula.name });
				button.setAttribute("aria-label", formula.formula);
				button.addEventListener("click", () => void this.rollAndNotify(formula.formula));
			}
		}

		const history = this.plugin.settings.history;
		if (history.length === 0) {
			root.createDiv({ cls: "rollwright-history-empty", text: "Click a roll in a note to see it here." });
			return;
		}
		const clear = root.createEl("button", { cls: "rollwright-history-clear", text: "Clear log" });
		clear.addEventListener("click", () => void this.plugin.clearHistory());

		const list = root.createDiv({ cls: "rollwright-history-list" });
		// Rolls of one note on one day sit under one heading, so the log reads as the story of an evening.
		for (const group of groupHistory(history)) {
			const section = list.createDiv({ cls: "rollwright-history-group" });
			const title = section.createDiv({ cls: "rollwright-history-group-title", text: group.title });
			if (group.source !== "") title.setAttribute("title", group.source);
			for (const entry of group.entries) this.renderItem(section, entry, entry === history[0]);
		}
	}

	private renderItem(parent: HTMLElement, entry: HistoryEntry, latest: boolean): void {
		const cls = ["rollwright-history-item", ...extremeClasses(entry.extreme)];
		// The newest roll gets the big d20; a class, because the group heading means it is no first child.
		if (latest) cls.push("rollwright-history-latest");
		const item = parent.createDiv({ cls });
		item.createDiv({ cls: "rollwright-history-result", text: entry.result });
		// The stamp sits next to the result, not in it, so the result is just the number. The hidden comma
		// makes a screen reader say "25, NAT 20" and not "25NAT 20".
		if (entry.extreme !== undefined && entry.stamp !== undefined) {
			item.createSpan({ cls: "rollwright-history-sep", text: ", " });
			item.createSpan({ cls: STAMP_CLASS, text: entry.stamp });
		}
		const label = historyLabel(entry.formula);
		if (label.name !== "") item.createDiv({ cls: "rollwright-history-name", text: label.name });
		// The tidy text is only for showing; the raw formula stays in the title so nothing is lost.
		const formula = item.createDiv({ cls: "rollwright-history-formula", text: label.formula });
		formula.setAttribute("title", entry.formula);
		if (entry.details !== "") item.createDiv({ cls: "rollwright-history-details", text: entry.details });
		const meta = item.createDiv({ cls: "rollwright-history-meta" });
		meta.createSpan({ text: new Date(entry.time).toLocaleTimeString() });
		if (entry.source !== "") {
			// Just the note name; the full path is in the title.
			const link = meta.createEl("a", { cls: "rollwright-history-note", text: noteName(entry.source) });
			link.setAttribute("title", entry.source);
			link.addEventListener("click", (event) => {
				event.preventDefault();
				void this.app.workspace.openLinkText(entry.source, "");
			});
		}
		const again = meta.createEl("button", { cls: "clickable-icon" });
		again.setAttribute("aria-label", "Roll again");
		setIcon(again, "refresh-cw");
		again.addEventListener("click", () => void this.rollAndNotify(entry.formula));
	}
}
