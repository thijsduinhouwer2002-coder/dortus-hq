import { Component, MarkdownRenderer, setIcon, setTooltip } from "obsidian";
import { formatNumber } from "../engine";
import type RollwrightPlugin from "../main";
import { parseSpec } from "../rollers/spec";
import type { RollOutcome } from "../rollers/run";

function errorMessage(error: unknown): string {
	return error instanceof Error ? error.message : String(error);
}

function tooltipFor(outcome: RollOutcome): string {
	return outcome.details === "" ? outcome.formula : `${outcome.formula}\n${outcome.details}`;
}

function showError(target: HTMLElement, formula: string, error: unknown): void {
	target.empty();
	target.addClass("rollwright-error");
	const message = errorMessage(error);
	target.createSpan({ text: `dice: ${formula}` });
	setTooltip(target, message);
	target.setAttribute("data-rollwright-error", message);
}

async function showOutcome(plugin: RollwrightPlugin, target: HTMLElement, outcome: RollOutcome, sourcePath: string, component: Component): Promise<void> {
	target.empty();
	target.removeClass("rollwright-error");
	const { flags } = outcome;
	if (!flags.nodice) {
		setIcon(target.createSpan({ cls: "rollwright-icon" }), "dices");
	}
	if (flags.text !== undefined) target.createSpan({ cls: "rollwright-label", text: `${flags.text}: ` });
	else if (flags.form) target.createSpan({ cls: "rollwright-label", text: `${outcome.formula} -> ` });

	const value = target.createSpan({ cls: "rollwright-value" });
	if (outcome.kind === "dice") {
		value.setText(`${outcome.estimated ? "~" : ""}${outcome.total === undefined ? outcome.text : formatNumber(outcome.total)}`);
	} else {
		await MarkdownRenderer.render(plugin.app, outcome.text, value, sourcePath, component);
	}
	setTooltip(target, tooltipFor(outcome));
}

/**
 * Fills an element with a roll and makes it clickable. Used by both the reading
 * view and Live Preview. A broken formula shows a marked message, it never throws.
 * The component owns anything rendered from markdown.
 */
export function mountRoll(plugin: RollwrightPlugin, target: HTMLElement, formula: string, key: string, sourcePath: string, component: Component): void {
	target.addClass("rollwright-roll");
	target.setAttribute("role", "button");

	let hideFirst = false;
	try {
		hideFirst = parseSpec(formula, plugin.rollContext(sourcePath).aliases).flags.none;
	} catch {
		hideFirst = false;
	}

	const rerollNow = async (): Promise<void> => {
		try {
			await showOutcome(plugin, target, await plugin.freshResult(key, formula, sourcePath), sourcePath, component);
		} catch (error) {
			showError(target, formula, error);
		}
	};

	target.setAttribute("tabindex", "0");
	target.addEventListener("keydown", (event) => {
		if (event.key === "Enter") void rerollNow();
	});
	target.addEventListener("click", (event) => {
		// A link inside a rendered result keeps working as a link.
		if ((event.target as Node).instanceOf(Element) && (event.target as Element).closest("a")) return;
		event.preventDefault();
		event.stopPropagation();
		void rerollNow();
	});
	// Keep the editor from moving the cursor into the code on a click.
	target.addEventListener("mousedown", (event) => event.preventDefault());

	if (hideFirst && !plugin.hasResult(key)) {
		setIcon(target.createSpan({ cls: "rollwright-icon" }), "dices");
		setTooltip(target, formula);
		return;
	}
	plugin.firstResult(key, formula, sourcePath).then(
		(outcome) => showOutcome(plugin, target, outcome, sourcePath, component),
		(error: unknown) => showError(target, formula, error),
	).catch((error: unknown) => showError(target, formula, error));
}
