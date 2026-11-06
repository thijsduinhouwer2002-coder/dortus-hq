import { averageOf, defaultRandom, DiceError, formatNumber, LIMITS, newBudget, roll, type Budget, type RandomInt } from "../engine";
import { listItems, noteLines, parseBlocks, type Block } from "./markdown";
import { parseSpec, type Flags, type Spec } from "./spec";
import { findColumn, findLookupRow, lookupFormula, parseTable, type Table } from "./table";

export interface NoteData {
	path: string;
	markdown: string;
}

/** What rollers need from the outside world. The plugin fills this with the vault. */
export interface RollContext {
	readNote(link: string, sourcePath: string): Promise<NoteData | null>;
	notesWithTag(tag: string): Promise<NoteData[]>;
	sourcePath: string;
	random?: RandomInt;
	defaultSides?: number;
	defaultCount?: number;
	aliases?: Record<string, string>;
	/** Shared by everything in one roll. Set by rollSpec. */
	budget?: Budget;
}

export interface RollOutcome {
	kind: "dice" | "table" | "list" | "section" | "line" | "tag";
	/** What to show. For anything but dice this is markdown. */
	text: string;
	total?: number;
	/** The first shown value is a mean, not a roll. */
	estimated?: boolean;
	formula: string;
	details: string;
	flags: Flags;
	/** The note the result came from, if there is one. */
	source?: string;
}

const MAX_NESTING = 8;
const MAX_PICKS = 100;

/** Block types of the notation. Inline ones are accepted but never match the block model. */
const BLOCK_TYPES = new Set([
	"blockquote", "break", "callout", "code", "delete", "emphasis", "footnoteReference", "footnote", "heading", "html",
	"imageReference", "image", "inlineCode", "linkReference", "link", "listItem", "list", "paragraph", "root", "strong",
	"table", "text", "thematicBreak", "toml", "yaml", "definition", "footnoteDefinition",
]);

function spendPick(context: RollContext): void {
	if (context.budget && ++context.budget.picks > LIMITS.picksPerRoll) {
		throw new DiceError(`This roll picks more than ${LIMITS.picksPerRoll} results`);
	}
}

function pick<T>(items: T[], random: RandomInt): T {
	return items[random(0, items.length - 1)] as T;
}

function diceOptions(context: RollContext) {
	return {
		random: context.random ?? defaultRandom,
		defaultSides: context.defaultSides,
		defaultCount: context.defaultCount,
		names: context.aliases,
		budget: context.budget,
	};
}

/** "" or "d" = 1, "3" or "3d" = 3, anything else is a formula that gives the number of picks. */
function pickCount(prefix: string, context: RollContext): number {
	const plain = /^(\d*)d?$/.exec(prefix);
	const count = plain ? Number(plain[1] || 1) : roll(prefix, diceOptions(context)).total;
	if (!Number.isInteger(count) || count < 0) throw new DiceError(`Cannot pick ${formatNumber(count)} results`);
	if (count > MAX_PICKS) throw new DiceError(`At most ${MAX_PICKS} results can be picked at once`);
	return count;
}

/** Rolls every `dice: x` in a piece of text. A cell may consist of `dice: x` without backticks. */
async function resolveNested(text: string, context: RollContext, depth: number): Promise<string> {
	const whole = /^dice:\s*(.+)$/i.exec(text.trim());
	if (whole) return (await rollSpecAt(whole[1] as string, context, depth + 1)).text;
	const pattern = /`dice:\s*([^`]+)`/gi;
	let output = "";
	let last = 0;
	for (let match = pattern.exec(text); match; match = pattern.exec(text)) {
		output += text.slice(last, match.index);
		output += (await rollSpecAt(match[1] as string, context, depth + 1)).text;
		last = match.index + match[0].length;
	}
	return output + text.slice(last);
}

/** Rolls each cell on its own, so a cell of `dice: x` without backticks does not take in its neighbours. */
async function resolveCells(cells: string[], context: RollContext, depth: number): Promise<string> {
	const texts: string[] = [];
	for (const cell of cells) texts.push(await resolveNested(cell, context, depth));
	return texts.join(" | ");
}

async function pickFromTable(table: Table, args: string[], context: RollContext, depth: number): Promise<{ text: string; detail: string }> {
	const random = context.random ?? defaultRandom;
	spendPick(context);
	if (table.rows.length === 0) throw new DiceError("The table has no rows");
	const formula = lookupFormula(table);
	const column = args[0];
	let columnIndex = -1;
	if (column !== undefined) {
		columnIndex = findColumn(table, column);
		if (columnIndex === -1 && column.toLowerCase() !== "xy") {
			throw new DiceError(`The table has no column "${column}". It has: ${table.headers.join(", ")}`);
		}
	}

	if (formula !== null) {
		const rolled = roll(formula, diceOptions(context));
		const row = findLookupRow(table, rolled.total);
		const shown = formatNumber(rolled.total);
		if (!row) throw new DiceError(`The lookup table has no row for ${shown}`);
		const cells = columnIndex > 0 ? [row[columnIndex] ?? ""] : row.slice(1);
		return { text: await resolveCells(cells, context, depth), detail: `${formula} = ${shown}` };
	}

	const row = pick(table.rows, random);
	if (columnIndex >= 0) return { text: await resolveNested(row[columnIndex] ?? "", context, depth), detail: column ?? "" };
	if (column !== undefined) {
		// xy: one cell. The first column holds row names when there is more than one column.
		const from = row.length > 1 ? 1 : 0;
		return { text: await resolveNested(row[random(from, row.length - 1)] ?? "", context, depth), detail: "xy" };
	}
	return { text: await resolveCells(row, context, depth), detail: "" };
}

function matchesType(block: Block, type: string): boolean {
	const heading = /^heading-([1-6])$/.exec(type);
	if (heading) return block.type === "heading" && block.level === Number(heading[1]);
	return block.type === type;
}

function selectBlocks(blocks: Block[], types: string[]): string[] {
	for (const type of types) {
		if (!BLOCK_TYPES.has(type) && !/^heading-[1-6]$/.test(type)) throw new DiceError(`Unknown block type "${type}"`);
	}
	if (types.length === 0) {
		return blocks.filter((b) => b.type !== "thematicBreak" && b.type !== "yaml").map((b) => b.text);
	}
	const output: string[] = [];
	for (const block of blocks) {
		if (types.includes("listItem") && block.type === "list") output.push(...listItems(block.text));
		else if (types.some((type) => matchesType(block, type))) output.push(block.text);
	}
	return output;
}

function blockTypes(args: string[]): string[] {
	return args.flatMap((arg) => arg.split(",")).map((type) => type.trim()).filter((type) => type !== "");
}

function pickMany(options: string[], count: number, random: RandomInt, emptyMessage: string, context: RollContext): string[] {
	if (count === 0) return [];
	if (options.length === 0) throw new DiceError(emptyMessage);
	const picks: string[] = [];
	for (let i = 0; i < count; i++) {
		spendPick(context);
		picks.push(pick(options, random));
	}
	return picks;
}

async function rollNote(spec: Spec, context: RollContext, depth: number): Promise<Omit<RollOutcome, "flags" | "formula">> {
	if (spec.target.kind !== "note") throw new DiceError("Not a note");
	const target = spec.target;
	const random = context.random ?? defaultRandom;
	const note = await context.readNote(target.note, context.sourcePath);
	if (!note) throw new DiceError(`Note "${target.note}" was not found`);
	const count = pickCount(target.prefix, context);
	const blocks = parseBlocks(note.markdown);

	if (target.blockId !== undefined) {
		const block = blocks.find((b) => b.id === target.blockId);
		if (!block) throw new DiceError(`Block ^${target.blockId} was not found in "${target.note}"`);
		if (block.type === "table") {
			const table = parseTable(block.text);
			const results: { text: string; detail: string }[] = [];
			for (let i = 0; i < count; i++) results.push(await pickFromTable(table, spec.args, context, depth));
			const detail = results.map((r) => r.detail).filter((d) => d !== "").join("; ");
			return { kind: "table", text: results.map((r) => r.text).join(", "), details: detail, source: note.path };
		}
		if (block.type === "list") {
			const picks = pickMany(listItems(block.text), count, random, "The list is empty", context);
			const texts: string[] = [];
			for (const item of picks) texts.push(await resolveNested(item, context, depth));
			return { kind: "list", text: texts.join(", "), details: "", source: note.path };
		}
		return { kind: "section", text: block.text, details: "", source: note.path };
	}

	if (spec.args.some((arg) => arg.toLowerCase() === "line")) {
		const picks = pickMany(noteLines(note.markdown), count, random, `"${target.note}" has no lines`, context);
		return { kind: "line", text: picks.join("\n"), details: "", source: note.path };
	}

	const options = selectBlocks(blocks, blockTypes(spec.args));
	const picks = pickMany(options, count, random, `"${target.note}" has no matching blocks`, context);
	return { kind: "section", text: picks.join("\n\n"), details: "", source: note.path };
}

async function rollTag(spec: Spec, context: RollContext): Promise<Omit<RollOutcome, "flags" | "formula">> {
	if (spec.target.kind !== "tag") throw new DiceError("Not a tag");
	const target = spec.target;
	const random = context.random ?? defaultRandom;
	const notes = await context.notesWithTag(target.tag);
	if (notes.length === 0) throw new DiceError(`No notes have the tag #${target.tag}`);

	const modes = spec.args.map((arg) => arg.toLowerCase());
	if (modes.includes("link")) {
		const note = pick(notes, random);
		return { kind: "tag", text: `[[${note.path.replace(/\.md$/, "")}]]`, details: `#${target.tag}`, source: note.path };
	}
	const chosen = modes.includes("-") ? [pick(notes, random)] : notes;
	const types = blockTypes(spec.args.filter((arg) => arg !== "-" && arg !== "+"));
	const count = pickCount(target.prefix, context);
	const parts: string[] = [];
	for (const note of chosen) {
		const options = selectBlocks(parseBlocks(note.markdown), types);
		if (options.length > 0) parts.push(...pickMany(options, count, random, "", context));
	}
	if (parts.length === 0 && count > 0) throw new DiceError(`No matching blocks in notes with #${target.tag}`);
	return { kind: "tag", text: parts.join("\n\n"), details: `#${target.tag}: ${chosen.length} note(s)`, source: chosen.length === 1 ? chosen[0]?.path : undefined };
}

async function rollSpecAt(raw: string, context: RollContext, depth: number, firstRoll = false): Promise<RollOutcome> {
	if (depth > MAX_NESTING) throw new DiceError("Rollers are nested too deeply, or a table points at itself");
	const spec = parseSpec(raw, context.aliases);
	const formula = raw.trim();

	if (spec.target.kind === "dice") {
		const dice = spec.target.formula;
		if (firstRoll && spec.flags.avg) {
			const average = averageOf(dice, diceOptions(context));
			return { kind: "dice", text: formatNumber(average.value), total: average.value, estimated: !average.exact, formula: dice, details: average.exact ? "Average" : "Estimated average", flags: spec.flags };
		}
		const result = roll(dice, diceOptions(context));
		return { kind: "dice", text: formatNumber(result.total), total: result.total, formula: dice, details: result.breakdown, flags: spec.flags };
	}
	const outcome = spec.target.kind === "note" ? await rollNote(spec, context, depth) : await rollTag(spec, context);
	return { ...outcome, formula, flags: spec.flags };
}

/**
 * Rolls anything that can follow "dice:". Rejects with DiceError when it is broken.
 * With firstRoll set, |avg gives the mean instead of a roll; a click then rolls for real.
 */
export function rollSpec(raw: string, context: RollContext, options: { firstRoll?: boolean } = {}): Promise<RollOutcome> {
	return rollSpecAt(raw, { ...context, budget: newBudget() }, 0, options.firstRoll ?? false);
}

export { parseSpec };
