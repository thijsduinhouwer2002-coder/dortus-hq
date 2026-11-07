import { EditorState, type TransactionSpec } from "@codemirror/state";
import { beforeEach, describe, expect, it, vi } from "vitest";
import RollwrightPlugin from "../src/main";
import { defuseRolls } from "../src/rollers/defuse";
import { findInlineDice, readDiceCode } from "../src/rollers/inline";
import { modifiedText } from "../src/rollers/modify";
import { rollSpec, type RollContext, type RollOutcome } from "../src/rollers/run";
import { lookupFormula, parseTable } from "../src/rollers/table";
import { CHANGED_NOTICE, EMBED_NOTICE, editorModifier, NOT_MARKDOWN_NOTICE, ReplaceCodeModal, UNPLACED_NOTICE } from "../src/ui/dice-mod";
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
function draw(plugin: RollwrightPlugin, note: string, line: number, options: { known?: boolean; inEmbed?: boolean; sourcePath?: string; dom?: string[] } = {}) {
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
	// The code elements as Obsidian would draw them; dom gives them by hand, for spans the scan does not count.
	const texts = options.dom ?? findInlineDice(text).map((f) => text.slice(f.from + 1, f.to - 1));
	const codes = texts.map((textContent) => ({ textContent, parentElement: { tagName: "P" }, replaceWith() {} }));
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
		spans[0]?.listeners.keydown?.({ key: "Enter", preventDefault() {} });
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

describe("repairs after the review of dice-mod", () => {
	it("4: a dice-mod code gets no place when the drawn codes and the scanned codes differ", async () => {
		const note = "``dice-mod: 1d1`` and `dice-mod: 1d1`";
		const files = { "A.md": note };
		const { plugin, app, confirm } = await load(files);
		const spans = draw(plugin, note, 0, { dom: ["dice-mod: 1d1", "dice-mod: 1d1"] });
		await wait();
		spans[0]?.listeners.click?.(click);
		await wait();
		expect(confirm).not.toHaveBeenCalled();
		expect(app.process).not.toHaveBeenCalled();
		expect(files["A.md"]).toBe(note);
		expect(notices).toContain(UNPLACED_NOTICE);
	});

	it("4: dice: keeps its numbering when the counts differ", async () => {
		const note = "<code>dice: 1d1</code> `dice: 2`";
		const { plugin } = await load({ "A.md": note });
		const spans = draw(plugin, note, 0, { dom: ["dice: 1d1", "dice: 2"] });
		await wait();
		expect(spans.map((span) => span.text)).toEqual(["1", "2"]);
		expect(plugin.hasResult("A.md|0:0|1d1")).toBe(true);
	});

	it("5b: writes only into a markdown note", async () => {
		const files = { "A.canvas": "`dice-mod: 1d1`" };
		const { plugin, app } = await load(files);
		expect(await plugin.replaceInNote("A.canvas", 0, 0, "1d1", "1")).toBe(false);
		expect(app.process).not.toHaveBeenCalled();
		expect(files["A.canvas"]).toBe("`dice-mod: 1d1`");
		expect(notices).toContain(NOT_MARKDOWN_NOTICE);
	});
});

describe("dice-mod: in Live Preview, through the editor", () => {
	/** The widget element: in the editor unless detached. */
	const widget = { isConnected: true };
	function fakeView(doc: string, at: number, holds: unknown[] = [widget]) {
		const view = {
			state: EditorState.create({ doc }),
			contentDOM: { contains: (node: unknown) => holds.includes(node) },
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
		editorModifier(plugin, view as never, widget as never, "1d1", 0, 1)(outcome);
		await wait();
		expect(view.state.doc.toString()).toBe("a `dice-mod: 1d1` b 1d1 -> [1] -> 1");
	});

	it("does nothing when the text there is no longer the code", async () => {
		const { plugin } = await load({});
		const view = fakeView("a `dice-mod: 1d2`", 2);
		editorModifier(plugin, view as never, widget as never, "1d1", 0, 0)(await rolled("1d1"));
		await wait();
		expect(view.state.doc.toString()).toBe("a `dice-mod: 1d2`");
		expect(notices).toContain(CHANGED_NOTICE);
	});

	it("does nothing when the widget left the editor (posAtDOM would give 0)", async () => {
		const { plugin } = await load({});
		const outcome = await rolled("1d1");
		const gone = { isConnected: false };
		const detached = fakeView("`dice-mod: 1d1` rest", 0, [gone]);
		editorModifier(plugin, detached as never, gone as never, "1d1", 0, 0)(outcome);
		const elsewhere = { isConnected: true };
		const other = fakeView("`dice-mod: 1d1` rest", 0, []);
		editorModifier(plugin, other as never, elsewhere as never, "1d1", 0, 0)(outcome);
		await wait();
		expect(detached.state.doc.toString()).toBe("`dice-mod: 1d1` rest");
		expect(other.state.doc.toString()).toBe("`dice-mod: 1d1` rest");
		expect(notices.filter((n) => n === CHANGED_NOTICE)).toHaveLength(2);
	});

	it("the old fault: posAtDOM gives another place, Replace still writes the code of the widget", async () => {
		const { plugin } = await load({});
		// posAtDOM is one off the start of the code, as seen in the real Obsidian; it is not used.
		const view = fakeView("x\nWorp: `dice-mod: 1d1` en verder", 9);
		editorModifier(plugin, view as never, widget as never, "1d1", 1, 0)(await rolled("1d1"));
		await wait();
		expect(view.state.doc.toString()).toBe("x\nWorp: 1d1 -> [1] -> 1 en verder");
		expect(notices).not.toContain(CHANGED_NOTICE);
	});

	it("a changed line gives the notice and writes nothing", async () => {
		const { plugin } = await load({});
		const view = fakeView("x\nWorp: `dice-mod: 1d1`", 0);
		const outcome = await rolled("1d1");
		// The code is no longer on line 0, and line 5 does not exist.
		editorModifier(plugin, view as never, widget as never, "1d1", 0, 0)(outcome);
		editorModifier(plugin, view as never, widget as never, "1d1", 5, 0)(outcome);
		await wait();
		expect(view.state.doc.toString()).toBe("x\nWorp: `dice-mod: 1d1`");
		expect(notices.filter((n) => n === CHANGED_NOTICE)).toHaveLength(2);
	});

	it("with two codes on one line the index picks the right one, in one undoable change", async () => {
		const { plugin } = await load({});
		const view = fakeView("`dice-mod: 1d1` en `dice-mod: 1d1|text(B)`", 0);
		const dispatch = vi.spyOn(view, "dispatch");
		editorModifier(plugin, view as never, widget as never, "1d1|text(B)", 0, 1)(await rolled("1d1"));
		await wait();
		expect(view.state.doc.toString()).toBe("`dice-mod: 1d1` en 1d1 -> [1] -> 1");
		expect(dispatch).toHaveBeenCalledTimes(1);
		expect(dispatch.mock.calls[0]?.[0]).toMatchObject({ userEvent: "input" });
		// Index 1 with the formula of index 0 is not the same code: nothing is written.
		editorModifier(plugin, view as never, widget as never, "1d1", 0, 1)(await rolled("1d1"));
		await wait();
		expect(view.state.doc.toString()).toBe("`dice-mod: 1d1` en 1d1 -> [1] -> 1");
		expect(notices).toContain(CHANGED_NOTICE);
	});

	it("Enter on a dice-mod roll keeps the key press from going on to the window", async () => {
		const files = { "A.md": "`dice-mod: 1d1`" };
		const { plugin } = await load(files);
		const spans = draw(plugin, files["A.md"], 0);
		await wait();
		const preventDefault = vi.fn();
		spans[0]?.listeners.keydown?.({ key: "Enter", preventDefault });
		spans[0]?.listeners.keydown?.({ key: "a", preventDefault });
		await wait();
		expect(preventDefault).toHaveBeenCalledTimes(1);
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
