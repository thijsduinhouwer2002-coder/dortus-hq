import { MarkdownRenderChild, type MarkdownPostProcessorContext } from "obsidian";
import type RollwrightPlugin from "../main";
import { findInlineDice, readDiceCode } from "../rollers/inline";
import { readingModifier } from "./dice-mod";
import { mountRoll } from "./widget";

/** The note lines of each dice code in a section, so reading view and Live Preview share results. */
function codePositions(el: HTMLElement, ctx: MarkdownPostProcessorContext): { line: number; index: number }[] {
	const info = ctx.getSectionInfo(el);
	if (!info) return [];
	const positions: { line: number; index: number }[] = [];
	const lines = info.text.split("\n");
	for (let line = info.lineStart; line <= info.lineEnd; line++) {
		findInlineDice(lines[line] ?? "").forEach((_, index) => positions.push({ line, index }));
	}
	return positions;
}

/** Tells apart codes whose line is unknown, such as in table cells: they get called one element at a time. */
let unplaced = 0;

export function processReadingView(plugin: RollwrightPlugin, el: HTMLElement, ctx: MarkdownPostProcessorContext): void {
	// Second lock next to defuseRolls: never mount inside a rendered result.
	if (el.closest(".rollwright-value")) return;
	const codes = Array.from(el.querySelectorAll("code")).filter((code) => code.parentElement?.tagName !== "PRE");
	const positions = codePositions(el, ctx);
	let nth = 0;
	for (const code of codes) {
		const dice = readDiceCode(code.textContent ?? "");
		if (dice === null) continue;
		const { formula } = dice;
		const position = positions[nth];
		// Without a known line the key changes on every redraw, so keeping would only pile up keys.
		const keep = dice.keep && position !== undefined;
		const place = position ? `${position.line}:${position.index}` : `el:${++unplaced}`;
		nth++;
		const span = activeDocument.createElement("span");
		code.replaceWith(span);
		const child = new MarkdownRenderChild(span);
		ctx.addChild(child);
		// dice-mod: shows a roll like dice:, and a click asks to write it into this note only.
		const modify = dice.modify ? readingModifier(plugin, span, ctx.sourcePath, position, formula) : undefined;
		mountRoll(plugin, span, formula, `${ctx.sourcePath}|${place}|${formula}`, ctx.sourcePath, child, keep, modify);
	}
}
