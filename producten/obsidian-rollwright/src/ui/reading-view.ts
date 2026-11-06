import { MarkdownRenderChild, type MarkdownPostProcessorContext } from "obsidian";
import type RollwrightPlugin from "../main";
import { findInlineDice, formulaFromCode } from "../rollers/inline";
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

export function processReadingView(plugin: RollwrightPlugin, el: HTMLElement, ctx: MarkdownPostProcessorContext): void {
	const codes = Array.from(el.querySelectorAll("code")).filter((code) => code.parentElement?.tagName !== "PRE");
	const positions = codePositions(el, ctx);
	let nth = 0;
	for (const code of codes) {
		const formula = formulaFromCode(code.textContent ?? "");
		if (formula === null) continue;
		const position = positions[nth];
		const place = position ? `${position.line}:${position.index}` : `el:${nth}`;
		nth++;
		const span = activeDocument.createElement("span");
		code.replaceWith(span);
		const child = new MarkdownRenderChild(span);
		ctx.addChild(child);
		mountRoll(plugin, span, formula, `${ctx.sourcePath}|${place}|${formula}`, ctx.sourcePath, child);
	}
}
