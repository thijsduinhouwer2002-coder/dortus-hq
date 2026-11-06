import { EditorState, type TransactionSpec } from "@codemirror/state";
import { beforeEach, describe, expect, it, vi } from "vitest";
import RollwrightPlugin from "../src/main";
import { defuseRolls } from "../src/rollers/defuse";
import { findInlineDice, readDiceCode } from "../src/rollers/inline";
import { modifiedText, replaceCodeInLine, replaceCodeInNote, replacementAt } from "../src/rollers/modify";
import { rollSpec, type RollContext, type RollOutcome } from "../src/rollers/run";
import { lookupFormula, parseTable } from "../src/rollers/table";
import { CHANGED_NOTICE, EMBED_NOTICE, editorModifier, ReplaceCodeModal, UNPLACED_NOTICE } from "../src/ui/dice-mod";
import { processReadingView } from "../src/ui/reading-view";
import { allText, buttons, type FakeEl, notices, openedModals, TFile } from "./obsidian-stub";

function context(notes: Record<string, string> = {}, rolls: number[] = []): RollContext {
	const queue = [...rolls];
	return {
		sourcePath: "A.md",
		defaultSides: 100,
		defaultCount: 1,
		aliases: {},
		random: (min, max) => queue.shift() ?? Math.max(min, Math.min(max, 1)),
		readNote: async (link) => (notes[link] === undefined ? null : { path: `${link}.md`, markdown: notes[link] as string }),
		notesWithTag: async () => [],
	};
}

const rolled = (spec: string, rolls: number[] = [], notes: Record<string, string> = {}) => rollSpec(spec, context(notes, rolls));

/** Every code that would roll when the text is rendered as markdown. */
function rollable(text: string): unknown[] {
	return text.split("\n").flatMap((line) => findInlineDice(line));
}

describe("dice-mod: is read in the note itself", () => {
	it("readDiceCode gives modify, in any case, and never keep", () => {
		expect(readDiceCode("dice-mod: 3d100 + 12")).toEqual({ formula: "3d100 + 12", keep: false, modify: true });
		expect(readDiceCode("DICE-MOD:1d6")).toEqual({ formula: "1d6", keep: false, modify: true });
		expect(readDiceCode("dice: 1d6")?.modify).toBeUndefined();
		expect(readDiceCode("dice-mod 1d6")).toBeNull();
		expect(readDiceCode("dice-mo: 1d6")).toBeNull();
	});

	it("is still refused in nested cells and as a lookup table header", async () => {
		expect(lookupFormula(parseTable("| `dice-mod: 1d20` | x |\n|---|---|"))).toBeNull();
		const notes = { M: "| What |\n|---|\n| `dice-mod: 6` and dice-mod: 7 |\n^t\n", W: "| Whole |\n|---|\n| dice-mod: 5 |\n^t\n" };
		expect((await rolled("[[M^t]]", [], notes)).text).toBe("`dice-mod: 6` and dice-mod: 7");
		expect((await rolled("[[W^t]]", [], notes)).text).toBe("dice-mod: 5");
	});
});

describe("modifiedText", () => {
	it("gives exactly the form of the design", async () => {
		const outcome = await rolled("3d100 + 12", [75, 20, 75]);
		expect(modifiedText(outcome, true)).toBe("3d100 + 12 -> [75, 20, 75] + 12 -> 182");
		expect(modifiedText(outcome, false)).toBe("[75, 20, 75] + 12 -> 182");
	});

	it("shows the total with the number flags", async () => {
		expect(modifiedText(await rolled("1d6 - 5|signed", [2]), true)).toBe("1d6 - 5 -> [2] - 5 -> -3");
		expect(modifiedText(await rolled("1d6|signed|paren", [4]), true)).toBe("1d6 -> [4] -> (+4)");
		expect(modifiedText(await rolled("1d6 / 4|ceil", [5]), false)).toBe("[5] / 4 -> 2");
	});

	it("leaves out the label of |text and the other display flags", async () => {
		expect(modifiedText(await rolled("1d6|text(Damage)|form|nodice", [3]), true)).toBe("1d6 -> [3] -> 3");
	});

	it("leaves out the breakdown of an average, with ~ for an estimate", async () => {
		const exact = await rollSpec("2d6|avg", context(), { firstRoll: true });
		expect(modifiedText(exact, true)).toBe("2d6 -> 7");
		expect(modifiedText(exact, false)).toBe("7");
		const estimate: RollOutcome = { ...exact, total: 3.5, estimated: true };
		expect(modifiedText(estimate, false)).toBe("~3.5");
	});

	it("gives only the result text for a table, on one line", async () => {
		const notes = { T: "| Item |\n|---|\n| Sword `dice: 1d6` |\n^t\n", S: "# One\n\nFirst `dice: 2d6`\nsecond\n\n![[Other]]\n" };
		const table = await rolled("[[T^t]]", [], notes);
		const text = modifiedText(table, true);
		expect(text).not.toContain("->");
		expect(text).toMatch(/^Sword 1$/);
		const section: RollOutcome = { kind: "section", text: notes.S, details: "", formula: "[[S]]", flags: table.flags };
		const written = modifiedText(section, true);
		expect(written).not.toContain("\n");
		expect(written).toContain("[[Other]]");
		expect(rollable(written)).toEqual([]);
	});

	it("never writes a code that rolls, for any prefix in a result", () => {
		for (const prefix of ["dice", "dice+", "dice-", "dice-mod", "DICE-MOD"]) {
			const outcome: RollOutcome = { kind: "list", text: `a \`${prefix}: 1d6\` b\nc`, details: "", formula: "[[L^l]]", flags: { nodice: false, form: false, avg: false, none: false } };
			expect(rollable(modifiedText(outcome, true))).toEqual([]);
		}
	});

	it("the text of a dice result holds no rollable code itself", async () => {
		const text = modifiedText(await rolled("1d6 + 2", [3]), true);
		expect(rollable(text)).toEqual([]);
		expect(rollable(`\`${text}\``)).toEqual([]);
	});
});

describe("defuse: a result with dice-mod: in it does not roll again (L9)", () => {
	it.each(["`dice-mod: 1d6`", "`` dice-mod: 1d6 ``", "<code>dice-mod: 1d6</code>", "it`s\n\n`dice-mod: 1d6`", "> `\n> dice-mod: 1d6`", "`dice - mod: 1d6`"])("%s", (text) => {
		const out = defuseRolls(text);
		expect(rollable(out)).toEqual([]);
		expect(readDiceCode(out.replace(/[`<>/]|code/g, "").trim())).toBeNull();
	});
});

describe("replacing the code", () => {
	const line = "Hit `dice-mod: 1d6` and `dice-mod: 1d6` and `dice: 2d6`";

	it("replaces the right one of two codes on a line", () => {
		expect(replaceCodeInLine(line, 1, "1d6", "1d6 -> [4] -> 4")).toBe("Hit `dice-mod: 1d6` and 1d6 -> [4] -> 4 and `dice: 2d6`");
		expect(replaceCodeInLine(line, 0, "1d6", "X")).toBe("Hit X and `dice-mod: 1d6` and `dice: 2d6`");
	});

	it("refuses when the code changed, is gone or is not dice-mod", () => {
		expect(replaceCodeInLine(line, 0, "1d8", "X")).toBeNull();
		expect(replaceCodeInLine(line, 2, "2d6", "X")).toBeNull();
		expect(replaceCodeInLine(line, 3, "1d6", "X")).toBeNull();
		expect(replaceCodeInLine("Hit `dice: 1d6`", 0, "1d6", "X")).toBeNull();
	});

	it("replaces in a note on the right line and keeps line endings", () => {
		const note = "a\r\n`dice-mod: 1d6`\r\nb `dice-mod: 1d6`\r\n";
		expect(replaceCodeInNote(note, 2, 0, "1d6", "X")).toBe("a\r\n`dice-mod: 1d6`\r\nb X\r\n");
		expect(replaceCodeInNote(note, 0, 0, "1d6", "X")).toBeNull();
		expect(replaceCodeInNote(note, 9, 0, "1d6", "X")).toBeNull();
	});

	it("keeps a table row whole", () => {
		expect(replaceCodeInLine("| a | `dice-mod: [[T^t]]` |", 0, "[[T^t]]", "x | y")).toBe("| a | x \\| y |");
		expect(replacementAt("| a | `dice-mod: 1d6` |", 6, "1d6", "p|q")).toEqual({ from: 6, to: 21, insert: "p\\|q" });
		expect(replacementAt("| a | `dice-mod: 1d6` |", 5, "1d6", "x")).toBeNull();
	});
});

/** A small element for the widget: it records listeners and the shown text. */
function fakeSpan(inEmbed = false) {
	const listeners: Record<string, (event: unknown) => void> = {};
	const el: Record<string, unknown> = {
		listeners,
		text: "",
		empty() {},
		addClass() {},
		removeClass() {},
		setAttribute() {},
		setText: (text: string) => (el.text = text),
		createSpan: () => el,
		addEventListener: (name: string, listener: (event: unknown) => void) => (listeners[name] = listener),
		closest: (selector: string) => (inEmbed && selector.includes("embed") ? {} : null),
	};
	return el as { listeners: Record<string, (event: unknown) => void>; text: string };
}

const click = { target: { instanceOf: () => false }, preventDefault() {}, stopPropagation() {} };
const wait = () => new Promise((resolve) => setTimeout(resolve, 20));

function fakeApp(files: Record<string, string>) {
	const tfiles = Object.keys(files).map((path) => new TFile(path));
	const process = vi.fn(async (file: TFile, change: (data: string) => string) => {
		files[file.path] = change(files[file.path] ?? "");
		return files[file.path];
	});
	return {
		process,
		workspace: { on: vi.fn(), getLeavesOfType: () => [], getActiveViewOfType: () => null, onLayoutReady: (callback: () => void) => callback(), iterateAllLeaves: () => {} },
		metadataCache: { getFirstLinkpathDest: (link: string) => tfiles.find((f) => f.path === `${link}.md`) ?? null, getFileCache: () => null },
		vault: {
			configDir: ".obsidian",
			cachedRead: async (file: TFile) => files[file.path] ?? "",
			getMarkdownFiles: () => tfiles,
			getAbstractFileByPath: (path: string) => tfiles.find((f) => f.path === path) ?? null,
			process,
		},
	};
}

async function load(files: Record<string, string>) {
	const app = fakeApp(files);
	const plugin = new (RollwrightPlugin as unknown as new (app: unknown) => RollwrightPlugin)(app);
	await plugin.onload();
	const confirm = vi.spyOn(plugin, "confirmReplace").mockResolvedValue(true);
	return { plugin, app, confirm };
}

/** Draws one paragraph of a note in reading view and gives back the span of each code. */
function draw(plugin: RollwrightPlugin, note: string, line: number, options: { known?: boolean; inEmbed?: boolean; sourcePath?: string } = {}) {
	const lines = note.split("\n");
	const spans: ReturnType<typeof fakeSpan>[] = [];
	vi.stubGlobal("activeDocument", {
		body: { toggleClass() {}, removeClass() {} },
		createElement: () => {
			const span = fakeSpan(options.inEmbed);
			spans.push(span);
			return span;
		},
	});
	const text = lines[line] ?? "";
	const codes = findInlineDice(text).map((f) => ({ textContent: text.slice(f.from + 1, f.to - 1), parentElement: { tagName: "P" }, replaceWith() {} }));
	const ctx = {
		sourcePath: options.sourcePath ?? "A.md",
		getSectionInfo: () => (options.known === false ? null : { text: note, lineStart: line, lineEnd: line }),
		addChild() {},
	};
	processReadingView(plugin, { closest: () => null, querySelectorAll: () => codes } as never, ctx as never);
	return spans;
}

beforeEach(() => {
	notices.length = 0;
	openedModals.length = 0;
	buttons.length = 0;
	vi.stubGlobal("Element", class {});
	vi.stubGlobal("activeDocument", { body: { toggleClass() {}, removeClass() {} } });
});

describe("dice-mod: in reading view, with a stand-in for the app", () => {
	it("a click asks, then replaces exactly that code in this note, with the shown result", async () => {
		const files = { "A.md": "Intro\nHit `dice-mod: 1d1 + 2` and `dice-mod: 1d1 + 2` now" };
		const { plugin, app, confirm } = await load(files);
		const spans = draw(plugin, files["A.md"], 1);
		await wait();
		expect(spans[1]?.text).toBe("3");
		spans[1]?.listeners.click?.(click);
		await wait();
		expect(confirm).toHaveBeenCalledWith("1d1 + 2 -> [1] + 2 -> 3");
		expect(app.process).toHaveBeenCalledTimes(1);
		expect(files["A.md"]).toBe("Intro\nHit `dice-mod: 1d1 + 2` and 1d1 + 2 -> [1] + 2 -> 3 now");
		expect(plugin.settings.history).toHaveLength(0);
	});

	it("Enter does the same as a click, and the setting drops the formula", async () => {
		const files = { "A.md": "`dice-mod: 1d1`" };
		const { plugin } = await load(files);
		plugin.settings.diceModFormula = false;
		const spans = draw(plugin, files["A.md"], 0);
		await wait();
		spans[0]?.listeners.keydown?.({ key: "Enter" });
		await wait();
		expect(files["A.md"]).toBe("[1] -> 1");
	});

	it("Cancel writes nothing", async () => {
		const files = { "A.md": "`dice-mod: 1d1`" };
		const { plugin, app, confirm } = await load(files);
		confirm.mockResolvedValue(false);
		const spans = draw(plugin, files["A.md"], 0);
		await wait();
		spans[0]?.listeners.click?.(click);
		await wait();
		expect(app.process).not.toHaveBeenCalled();
		expect(files["A.md"]).toBe("`dice-mod: 1d1`");
	});

	it("refuses when the code changed in the meantime", async () => {
		const files: Record<string, string> = { "A.md": "`dice-mod: 1d1`" };
		const { plugin } = await load(files);
		const spans = draw(plugin, files["A.md"] ?? "", 0);
		await wait();
		files["A.md"] = "`dice-mod: 1d2`";
		spans[0]?.listeners.click?.(click);
		await wait();
		expect(files["A.md"]).toBe("`dice-mod: 1d2`");
		expect(notices).toContain(CHANGED_NOTICE);
	});

	it("refuses when the line is unknown, as in a table cell", async () => {
		const files = { "A.md": "| `dice-mod: 1d1` |" };
		const { plugin, app, confirm } = await load(files);
		const spans = draw(plugin, files["A.md"], 0, { known: false });
		await wait();
		spans[0]?.listeners.click?.(click);
		await wait();
		expect(confirm).not.toHaveBeenCalled();
		expect(app.process).not.toHaveBeenCalled();
		expect(notices).toContain(UNPLACED_NOTICE);
	});

	it("never writes in an embedded note", async () => {
		const files = { "A.md": "![[B]]", "B.md": "`dice-mod: 1d1`" };
		const { plugin, app } = await load(files);
		const spans = draw(plugin, files["B.md"], 0, { inEmbed: true, sourcePath: "B.md" });
		await wait();
		expect(spans[0]?.text).toBe("1");
		spans[0]?.listeners.click?.(click);
		await wait();
		expect(app.process).not.toHaveBeenCalled();
		expect(files["B.md"]).toBe("`dice-mod: 1d1`");
		expect(notices).toContain(EMBED_NOTICE);
	});

	it("a table roll writes only the result into this note, never into the table note", async () => {
		const files = { "A.md": "Loot: `dice-mod: [[Loot^t]]`", "Loot.md": "| Item |\n|---|\n| Sword `dice: 1d1` |\n^t\n" };
		const { plugin, app } = await load(files);
		const spans = draw(plugin, files["A.md"], 0);
		await wait();
		spans[0]?.listeners.click?.(click);
		await wait();
		expect(app.process).toHaveBeenCalledTimes(1);
		expect((app.process.mock.calls[0]?.[0] as TFile).path).toBe("A.md");
		expect(files["A.md"]).toBe("Loot: Sword 1");
		expect(files["Loot.md"]).toBe("| Item |\n|---|\n| Sword `dice: 1d1` |\n^t\n");
	});
});

describe("dice-mod: in Live Preview, through the editor", () => {
	function fakeView(doc: string, at: number) {
		const view = {
			state: EditorState.create({ doc }),
			posAtDOM: () => at,
			dispatch: (spec: TransactionSpec) => {
				view.state = view.state.update(spec).state;
			},
		};
		return view;
	}

	it("replaces the code at the widget in one change", async () => {
		const { plugin } = await load({});
		const view = fakeView("a `dice-mod: 1d1` b `dice-mod: 1d1`", 20);
		const outcome = await rolled("1d1");
		editorModifier(plugin, view as never, {} as never, "1d1")(outcome);
		await wait();
		expect(view.state.doc.toString()).toBe("a `dice-mod: 1d1` b 1d1 -> [1] -> 1");
	});

	it("does nothing when the text there is no longer the code", async () => {
		const { plugin } = await load({});
		const view = fakeView("a `dice-mod: 1d2`", 2);
		editorModifier(plugin, view as never, {} as never, "1d1")(await rolled("1d1"));
		await wait();
		expect(view.state.doc.toString()).toBe("a `dice-mod: 1d2`");
		expect(notices).toContain(CHANGED_NOTICE);
	});
});

describe("the confirmation window", () => {
	it("shows the text and answers Replace, Cancel or close", () => {
		const answers: boolean[] = [];
		const modal = new ReplaceCodeModal({} as never, "1d6 -> [4] -> 4", (replace) => answers.push(replace));
		modal.open();
		expect(allText(modal.contentEl as unknown as FakeEl)).toContain("1d6 -> [4] -> 4");
		expect(buttons.map((b) => b.text)).toEqual(["Cancel", "Replace"]);
		buttons[1]?.press();
		new ReplaceCodeModal({} as never, "x", (replace) => answers.push(replace)).open();
		buttons[2]?.press();
		const closed = new ReplaceCodeModal({} as never, "x", (replace) => answers.push(replace));
		closed.open();
		closed.close();
		expect(answers).toEqual([true, false, false]);
	});
});
