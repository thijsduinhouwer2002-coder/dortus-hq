import { Component, Keymap, MarkdownRenderer, Notice, setIcon, setTooltip, type PaneType } from "obsidian";
import { formatResult } from "../engine";
import type RollwrightPlugin from "../main";
import { defuseRolls } from "../rollers/defuse";
import { parseSpec } from "../rollers/spec";
import type { RollOutcome } from "../rollers/run";
import type { ModifyHandler } from "./dice-mod";

export const NO_SOURCE_NOTICE = "This result comes from more than one note, so there is no single note to open.";

function errorMessage(error: unknown): string {
	return error instanceof Error ? error.message : String(error);
}

function tooltipFor(outcome: RollOutcome): string {
	return outcome.details === "" ? outcome.formula : `${outcome.formula}\n${outcome.details}`;
}

/** Only the dice icon, as a |none code shows before its first click. */
function showBlank(target: HTMLElement, formula: string): void {
	target.empty();
	target.removeClass("rollwright-error");
	setIcon(target.createSpan({ cls: "rollwright-icon" }), "dices");
	setTooltip(target, formula);
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
		value.setText(`${outcome.estimated ? "~" : ""}${outcome.total === undefined ? outcome.text : formatResult(outcome.total, flags)}`);
	} else {
		await MarkdownRenderer.render(plugin.app, defuseRolls(outcome.text), value, sourcePath, component);
	}
	setTooltip(target, tooltipFor(outcome));
}

/**
 * Fills an element with a roll and makes it clickable. Used by both the reading
 * view and Live Preview. A broken formula shows a marked message, it never throws.
 * The component owns anything rendered from markdown. With keep (`dice+:`) the
 * result is kept across restarts, and a click keeps the new one. With modify (`dice-mod:`)
 * a click does not roll again: it hands the shown result to modify, which asks before it
 * replaces the code.
 *
 * Ctrl- or Cmd-click opens the note a table, list, section, line or tag result came from,
 * and rolls nothing; on dice it rolls as a click does. On a |none code it makes the code empty
 * again and forgets the result. Alt-click shows the average of dice, as |avg does. On dice-mod
 * only the opening of the source is added; anything else stays a plain click.
 */
export function mountRoll(plugin: RollwrightPlugin, target: HTMLElement, formula: string, key: string, sourcePath: string, component: Component, keep = false, modify?: ModifyHandler): void {
	target.addClass("rollwright-roll");
	target.setAttribute("role", "button");

	let hideFirst = false;
	try {
		hideFirst = parseSpec(formula, plugin.rollContext(sourcePath).aliases).flags.none;
	} catch {
		hideFirst = false;
	}

	let shown: RollOutcome | null = null;
	const show = async (outcome: RollOutcome): Promise<void> => {
		shown = outcome;
		await showOutcome(plugin, target, outcome, sourcePath, component);
	};
	const fail = (error: unknown): void => {
		shown = null;
		showError(target, formula, error);
	};

	const rerollNow = async (): Promise<void> => {
		try {
			if (!modify) {
				await show(await plugin.freshResult(key, formula, sourcePath, keep));
				return;
			}
			// dice-mod: write what is shown. Hidden by |none, it is rolled and shown first.
			if (shown === null) await show(await plugin.firstResult(key, formula, sourcePath));
			if (shown !== null) modify(shown);
		} catch (error) {
			fail(error);
		}
	};

	const averageNow = async (): Promise<void> => {
		try {
			await show(await plugin.averageResult(key, formula, sourcePath, keep));
		} catch (error) {
			fail(error);
		}
	};

	const modClick = async (pane: PaneType | boolean): Promise<void> => {
		if (hideFirst) {
			shown = null;
			await plugin.forgetResult(key);
			showBlank(target, formula);
			return;
		}
		if (shown === null || shown.kind === "dice") {
			await rerollNow();
			return;
		}
		if (shown.source === undefined) {
			new Notice(NO_SOURCE_NOTICE);
			return;
		}
		await plugin.app.workspace.openLinkText(shown.source, sourcePath, pane);
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
		const pane = Keymap.isModEvent(event);
		if (pane) void modClick(pane);
		else if (event.altKey && !modify) void averageNow();
		else void rerollNow();
	});
	// Keep the editor from moving the cursor into the code on a click.
	target.addEventListener("mousedown", (event) => event.preventDefault());

	if (hideFirst && !plugin.hasResult(key, keep)) {
		showBlank(target, formula);
		return;
	}
	plugin.firstResult(key, formula, sourcePath, keep).then(show, fail).catch(fail);
}
