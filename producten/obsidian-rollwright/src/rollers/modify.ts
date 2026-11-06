import { formatResult } from "../engine";
import { defuseRolls } from "./defuse";
import { findInlineDice } from "./inline";
import type { RollOutcome } from "./run";

/**
 * Puts a result on one line. A dice-mod code sits in the middle of a line, so a line
 * break in the result would split a paragraph, a list item or a table row. Every run of
 * white space that holds a line break becomes one space: the note stays plain text,
 * without HTML such as <br>, and reads the same in every editor.
 */
function oneLine(text: string): string {
	return text.replace(/\s*[\r\n]\s*/g, " ").trim();
}

/**
 * The text a dice-mod code is replaced with.
 * - Dice: "<formula> -> <breakdown> -> <total>", the total with the number flags and a "~"
 *   for an estimate. Without the formula: "<breakdown> -> <total>". When there is no
 *   breakdown (the average of |avg), that part is left out, so no arrow points at nothing.
 *   Display flags (|text, |form, |nodice, |none) only change the widget and are not written.
 * - Table, list, section, line and tag: only the result text.
 * Always defused, so the written text never holds a new code that rolls.
 */
export function modifiedText(outcome: RollOutcome, showFormula: boolean): string {
	if (outcome.kind !== "dice") return oneLine(defuseRolls(outcome.text));
	const total = `${outcome.estimated ? "~" : ""}${outcome.total === undefined ? outcome.text : formatResult(outcome.total, outcome.flags)}`;
	const parts: string[] = [];
	if (showFormula) parts.push(outcome.formula.trim());
	const breakdown = outcome.average ? "" : outcome.details.trim();
	if (breakdown !== "") parts.push(breakdown);
	parts.push(total);
	return oneLine(defuseRolls(parts.join(" -> ")));
}

/** A table row starts with "|". A "|" in the replacement would then make a new cell. */
function escapePipes(line: string, text: string): string {
	return line.trimStart().startsWith("|") ? text.replace(/\\?\|/g, (pipe) => (pipe === "|" ? "\\|" : pipe)) : text;
}

/**
 * Replaces the code with this number on the line (counted as findInlineDice counts), but
 * only when it is still a dice-mod code with this formula. Null when it is not: then
 * nothing may be written.
 */
export function replaceCodeInLine(lineText: string, index: number, formula: string, replacement: string): string | null {
	const code = findInlineDice(lineText)[index];
	if (!code || !code.modify || code.formula !== formula) return null;
	return lineText.slice(0, code.from) + escapePipes(lineText, replacement) + lineText.slice(code.to);
}

/**
 * The change for the code that starts at this column of the line, as the editor needs it:
 * from and to within the line and the text to insert. Null when no dice-mod code with
 * this formula starts there any more.
 */
export function replacementAt(lineText: string, column: number, formula: string, replacement: string): { from: number; to: number; insert: string } | null {
	const code = findInlineDice(lineText).find((found) => found.from === column);
	if (!code || !code.modify || code.formula !== formula) return null;
	return { from: code.from, to: code.to, insert: escapePipes(lineText, replacement) };
}

/** The same for a whole note, with the line counted from 0. Line endings stay as they are. */
export function replaceCodeInNote(markdown: string, line: number, index: number, formula: string, replacement: string): string | null {
	const lines = markdown.split("\n");
	const text = lines[line];
	if (text === undefined) return null;
	const replaced = replaceCodeInLine(text, index, formula, replacement);
	if (replaced === null) return null;
	lines[line] = replaced;
	return lines.join("\n");
}
