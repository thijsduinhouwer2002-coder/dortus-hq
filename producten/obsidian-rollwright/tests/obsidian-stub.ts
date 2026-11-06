/** A small stand-in for the obsidian module, for testing the plugin's glue without the app. */
export class TFile {
	constructor(public path: string) {}
}

export class Plugin {
	stored: unknown = null;
	registered = { views: [] as string[], commands: [] as { id: string; name: string }[], processors: 0, extensions: 0, tabs: 0 };
	constructor(public app: unknown) {}
	async loadData(): Promise<unknown> {
		return this.stored;
	}
	async saveData(data: unknown): Promise<void> {
		this.stored = JSON.parse(JSON.stringify(data));
	}
	registerView(type: string): void {
		this.registered.views.push(type);
	}
	registerMarkdownPostProcessor(): void {
		this.registered.processors++;
	}
	registerEditorExtension(): void {
		this.registered.extensions++;
	}
	addSettingTab(): void {
		this.registered.tabs++;
	}
	addCommand(command: { id: string; name: string }): void {
		this.registered.commands.push(command);
	}
	registerEvent(): void {}
}

export const notices: string[] = [];
export class Notice {
	constructor(message: string) {
		notices.push(message);
	}
}

export function getAllTags(cache: { tags?: string[] }): string[] | null {
	return cache.tags ?? null;
}

export class ItemView {}
export class MarkdownView {}
export class Modal {}
export class PluginSettingTab {}
export class Setting {}
export class Component {}
export class MarkdownRenderChild {}
export const rendered: string[] = [];
export const MarkdownRenderer = {
	render: async (_app: unknown, markdown: string): Promise<void> => {
		rendered.push(markdown);
	},
};
export const editorInfoField = {};
export const editorLivePreviewField = {};
export function setIcon(): void {}
export function setTooltip(): void {}
