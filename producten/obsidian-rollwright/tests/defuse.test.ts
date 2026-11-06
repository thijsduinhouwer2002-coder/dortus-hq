import { beforeEach, describe, expect, it, vi } from "vitest";
import { roll } from "../src/engine";
import { defuseRolls } from "../src/rollers/defuse";
import { findInlineDice, formulaFromCode } from "../src/rollers/inline";
import { rollSpec, type RollContext } from "../src/rollers/run";
import { processReadingView } from "../src/ui/reading-view";
import { mountRoll } from "../src/ui/widget";
import { rendered } from "./obsidian-stub";

/** Everything markdown could turn into a code element. */
function rollableCodes(markdown: string): string[] {
	const pieces: string[] = [];
	for (const pattern of [/(`+)([^`]*)\1/g, /(<code>)(.*?)<\/code>/gi]) {
		for (let match = pattern.exec(markdown); match; match = pattern.exec(markdown)) pieces.push(match[2] as string);
	}
	return pieces.filter((piece) => formulaFromCode(piece) !== null);
}

const SELF = "Before `dice: [[Self]]` and ``dice: 1d6`` and <code>DICE:1d6</code>\n\n`dice: #npc`\n\n![[Self]]\n\n![pic](Self.md)\n\n![[map.png|200]]\n\n![x](https://a.b/c)";

function context(notes: Record<string, string>): RollContext {
	return {
		sourcePath: "Self.md",
		random: (min) => min,
		readNote: async (link) => (notes[link] === undefined ? null : { path: `${link}.md`, markdown: notes[link] as string }),
		notesWithTag: async () => Object.entries(notes).map(([name, markdown]) => ({ path: `${name}.md`, markdown })),
	};
}

function fakeTarget() {
	const self: Record<string, unknown> = {
		empty() {},
		addClass() {},
		removeClass() {},
		setAttribute() {},
		addEventListener() {},
		setText() {},
		createSpan: () => self,
	};
	return self as unknown as HTMLElement;
}

beforeEach(() => {
	rendered.length = 0;
});

describe("rolled text cannot roll again", () => {
	it("leaves no dice code in any form", () => {
		expect(rollableCodes(SELF).length).toBeGreaterThan(3);
		const safe = defuseRolls(SELF);
		expect(rollableCodes(safe)).toEqual([]);
		expect(findInlineDice(safe)).toEqual([]);
	});

	it("turns note embeds into links and keeps images", () => {
		const safe = defuseRolls(SELF);
		expect(safe).not.toContain("![[Self]]");
		expect(safe).toContain("[[Self]]");
		expect(safe).toContain("[pic](Self.md)");
		expect(safe).not.toContain("![pic]");
		expect(safe).toContain("![[map.png|200]]");
		expect(safe).toContain("![x](https://a.b/c)");
	});

	it.each(["[[Self]]", "#npc", "[[Self]]|line"])("a note rolling on itself with %s stops after one render", async (formula) => {
		const notes = { Self: `\`dice: ${formula}\`` };
		const outcome = await rollSpec(formula, context(notes));
		expect(rollableCodes(outcome.text)).toHaveLength(1);
		expect(rollableCodes(defuseRolls(outcome.text))).toEqual([]);
	});

	it("the widget only hands defused text to the renderer", async () => {
		const plugin = {
			app: {},
			rollContext: () => ({ aliases: {} }),
			hasResult: () => false,
			firstResult: () => rollSpec("[[Self]]", context({ Self: "`dice: [[Self]]`" })),
		};
		mountRoll(plugin as never, fakeTarget(), "[[Self]]", "k", "Self.md", {} as never);
		await vi.waitFor(() => expect(rendered).toHaveLength(1));
		expect(rollableCodes(rendered[0] as string)).toEqual([]);
	});

	it("the post-processor mounts nothing inside a result", () => {
		const querySelectorAll = vi.fn(() => []);
		const el = { closest: () => ({}), querySelectorAll };
		processReadingView({} as never, el as never, {} as never);
		expect(querySelectorAll).not.toHaveBeenCalled();
	});
});

describe("one budget per roll", () => {
	it("stops a chain of named formulas", () => {
		const fan = (name: string) => Array.from({ length: 400 }, () => name).join("+");
		const names = { a: fan("b"), b: fan("c"), c: fan("e"), e: fan("f"), f: "1" };
		expect(() => roll("a", { names })).toThrow(/too complex/);
	});

	it("stops a chain of notes that each pick 100", async () => {
		const notes: Record<string, string> = {};
		for (let i = 0; i < 8; i++) notes[`N${i}`] = `| x |\n|---|\n| \`dice: 100[[N${i + 1}^t]]\` |\n^t\n`;
		notes.N8 = "| x |\n|---|\n| end |\n^t\n";
		let reads = 0;
		const base = context(notes);
		const counting: RollContext = { ...base, readNote: (link, from) => (reads++, base.readNote(link, from)) };
		await expect(rollSpec("[[N0^t]]", counting)).rejects.toThrow(/more than 10000 results/);
		expect(reads).toBeLessThan(20000);
	});

	it("shares the dice budget between nested rolls", async () => {
		const notes = { A: "| x |\n|---|\n| `dice: 1000d1` |\n^t\n" };
		await expect(rollSpec("20[[A^t]]", context(notes))).rejects.toThrow(/more than 10000 dice/);
	});

	it("allows a normal large pick", async () => {
		const notes = { A: "| x |\n|---|\n| a |\n^t\n" };
		expect((await rollSpec("100[[A^t]]", context(notes))).text.split(", ")).toHaveLength(100);
	});
});
