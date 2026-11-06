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
export class PluginSettingTab {}

/** A tiny element: enough for a modal to put text in. */
export interface FakeEl {
	tag: string;
	text: string;
	children: FakeEl[];
	createEl(tag: string, options?: { text?: string }): FakeEl;
	empty(): void;
}
function fakeEl(tag = "div", text = ""): FakeEl {
	const el: FakeEl = {
		tag,
		text,
		children: [],
		createEl: (child, options) => {
			const made = fakeEl(child, options?.text ?? "");
			el.children.push(made);
			return made;
		},
		empty: () => {
			el.children.length = 0;
		},
	};
	return el;
}
export function allText(el: FakeEl): string[] {
	return [el.text, ...el.children.flatMap(allText)].filter((text) => text !== "");
}

export const openedModals: Modal[] = [];
export class Modal {
	contentEl = fakeEl();
	title = "";
	constructor(public app: unknown) {}
	setTitle(title: string): this {
		this.title = title;
		return this;
	}
	open(): void {
		openedModals.push(this);
		(this as { onOpen?: () => void }).onOpen?.();
	}
	close(): void {
		(this as { onClose?: () => void }).onClose?.();
	}
}

/** Buttons made through Setting.addButton, newest last, so a test can press one. */
export const buttons: { text: string; press: () => void }[] = [];
export class Setting {
	addButton(make: (button: unknown) => void): this {
		const made = { text: "", press: () => {} };
		const button = {
			setButtonText: (text: string) => ((made.text = text), button),
			setCta: () => button,
			onClick: (press: () => void) => ((made.press = press), button),
		};
		make(button);
		buttons.push(made);
		return this;
	}
}
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
