import { getAllTags, MarkdownView, Notice, Plugin, TFile, type WorkspaceLeaf } from "obsidian";
import { extractSavedFormulas, mergeFormulas, type SavedFormula } from "./import/dice-roller-data";
import { isValidLicenseKey } from "./pro/license";
import { resolveSkin, SKINS } from "./pro/skins";
import { rollSpec, type NoteData, type RollContext, type RollOutcome } from "./rollers/run";
import { HISTORY_VIEW, RollHistoryView } from "./ui/history-view";
import { rollwrightLivePreview } from "./ui/live-preview";
import { RollFormulaModal } from "./ui/modal";
import { processReadingView } from "./ui/reading-view";
import { RollwrightSettingTab } from "./ui/settings";

export interface HistoryEntry {
	time: number;
	formula: string;
	result: string;
	details: string;
	source: string;
}

export interface RollwrightSettings {
	defaultSides: number;
	defaultCount: number;
	formulas: SavedFormula[];
	history: HistoryEntry[];
	licenseKey: string;
	skin: string;
}

const DEFAULT_SETTINGS: RollwrightSettings = {
	defaultSides: 100,
	defaultCount: 1,
	formulas: [],
	history: [],
	licenseKey: "",
	skin: "classic",
};

const HISTORY_LIMIT = 200;
/** Results stay put until a click, so scrolling or redrawing never rerolls them. */
const RESULT_CACHE_LIMIT = 2000;

export default class RollwrightPlugin extends Plugin {
	settings: RollwrightSettings = { ...DEFAULT_SETTINGS };
	private readonly results = new Map<string, RollOutcome>();
	private readonly skinnedDocuments = new Set<Document>();

	async onload(): Promise<void> {
		await this.loadSettings();

		this.registerView(HISTORY_VIEW, (leaf: WorkspaceLeaf) => new RollHistoryView(leaf, this));
		this.registerMarkdownPostProcessor((el, ctx) => processReadingView(this, el, ctx));
		this.registerEditorExtension(rollwrightLivePreview(this));
		this.addSettingTab(new RollwrightSettingTab(this.app, this));

		this.addCommand({
			id: "open-history",
			name: "Open roll history",
			callback: () => void this.openHistory(),
		});
		this.addCommand({
			id: "roll-formula",
			name: "Roll a formula",
			callback: () => new RollFormulaModal(this.app, this).open(),
		});

		this.applySkin(activeDocument);
		this.registerEvent(this.app.workspace.on("window-open", (win) => this.applySkin(win.doc)));
	}

	onunload(): void {
		for (const doc of this.skinnedDocuments) {
			for (const skin of SKINS) doc.body.removeClass(skin.cssClass);
		}
	}

	async loadSettings(): Promise<void> {
		const stored = (await this.loadData()) as Partial<RollwrightSettings> | null;
		this.settings = { ...DEFAULT_SETTINGS, ...stored };
	}

	async saveSettings(): Promise<void> {
		await this.saveData(this.settings);
	}

	get isLicensed(): boolean {
		return isValidLicenseKey(this.settings.licenseKey);
	}

	/** Sets the skin on this document and on every window that already has one. */
	applySkin(doc: Document = activeDocument): void {
		this.skinnedDocuments.add(doc);
		const active = resolveSkin(this.settings.skin, this.isLicensed);
		for (const known of this.skinnedDocuments) {
			for (const skin of SKINS) known.body.toggleClass(skin.cssClass, skin.id === active.id);
		}
	}

	/** Builds the bridge between the pure rollers and this vault. */
	rollContext(sourcePath: string): RollContext {
		const aliases: Record<string, string> = {};
		for (const formula of this.settings.formulas) aliases[formula.name] = formula.formula;
		return {
			sourcePath,
			defaultSides: this.settings.defaultSides,
			defaultCount: this.settings.defaultCount,
			aliases,
			readNote: (link, from) => this.readNote(link, from),
			notesWithTag: (tag) => this.notesWithTag(tag),
		};
	}

	private async readNote(link: string, sourcePath: string): Promise<NoteData | null> {
		const file = this.app.metadataCache.getFirstLinkpathDest(link, sourcePath);
		if (!(file instanceof TFile)) return null;
		return { path: file.path, markdown: await this.app.vault.cachedRead(file) };
	}

	private async notesWithTag(tag: string): Promise<NoteData[]> {
		const wanted = `#${tag}`.toLowerCase();
		const notes: NoteData[] = [];
		for (const file of this.app.vault.getMarkdownFiles()) {
			const cache = this.app.metadataCache.getFileCache(file);
			const tags = cache ? getAllTags(cache) : null;
			if (tags?.some((t) => t.toLowerCase() === wanted || t.toLowerCase().startsWith(`${wanted}/`))) {
				notes.push({ path: file.path, markdown: await this.app.vault.cachedRead(file) });
			}
		}
		return notes;
	}

	hasResult(key: string): boolean {
		return this.results.has(key);
	}

	/** The result for this place in a note: remembered, or rolled for the first time. */
	async firstResult(key: string, formula: string, sourcePath: string): Promise<RollOutcome> {
		const known = this.results.get(key);
		if (known) return known;
		const outcome = await rollSpec(formula, this.rollContext(sourcePath), { firstRoll: true });
		this.remember(key, outcome);
		return outcome;
	}

	/** A roll someone asked for. Only these go into the history. */
	async freshResult(key: string | null, formula: string, sourcePath: string): Promise<RollOutcome> {
		const outcome = await rollSpec(formula, this.rollContext(sourcePath));
		if (key !== null) this.remember(key, outcome);
		await this.addToHistory(outcome, formula, sourcePath);
		return outcome;
	}

	private remember(key: string, outcome: RollOutcome): void {
		if (this.results.size >= RESULT_CACHE_LIMIT) {
			const oldest = this.results.keys().next().value;
			if (oldest !== undefined) this.results.delete(oldest);
		}
		this.results.set(key, outcome);
	}

	private async addToHistory(outcome: RollOutcome, formula: string, sourcePath: string): Promise<void> {
		this.settings.history.unshift({
			time: Date.now(),
			formula,
			result: outcome.text,
			details: outcome.details,
			source: sourcePath,
		});
		this.settings.history.length = Math.min(this.settings.history.length, HISTORY_LIMIT);
		await this.saveSettings();
		this.refreshHistoryViews();
	}

	async clearHistory(): Promise<void> {
		this.settings.history = [];
		await this.saveSettings();
		this.refreshHistoryViews();
	}

	private refreshHistoryViews(): void {
		for (const leaf of this.app.workspace.getLeavesOfType(HISTORY_VIEW)) {
			if (leaf.view instanceof RollHistoryView) leaf.view.refresh();
		}
	}

	async openHistory(): Promise<void> {
		const { workspace } = this.app;
		let leaf = workspace.getLeavesOfType(HISTORY_VIEW)[0];
		if (!leaf) {
			leaf = workspace.getRightLeaf(false) ?? undefined;
			await leaf?.setViewState({ type: HISTORY_VIEW, active: true });
		}
		if (leaf) await workspace.revealLeaf(leaf);
	}

	currentNotePath(): string {
		return this.app.workspace.getActiveViewOfType(MarkdownView)?.file?.path ?? "";
	}

	/** Reads the named formulas of the other plugin. Reads only; its file stays as it is. */
	async importSavedFormulas(): Promise<void> {
		const path = `${this.app.vault.configDir}/plugins/obsidian-dice-roller/data.json`;
		const adapter = this.app.vault.adapter;
		if (!(await adapter.exists(path))) {
			new Notice("No saved formulas found to import.");
			return;
		}
		const found = extractSavedFormulas(await adapter.read(path));
		const { merged, added } = mergeFormulas(this.settings.formulas, found);
		this.settings.formulas = merged;
		await this.saveSettings();
		new Notice(`Imported ${added} of ${found.length} saved formulas.`);
	}
}
