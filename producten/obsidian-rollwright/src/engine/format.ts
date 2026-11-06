/** Shows at most two decimals and never "-0". Very large numbers cannot be rounded this way and stay as they are. */
export function formatNumber(value: number): string {
	if (value === Infinity) return "∞";
	if (value === -Infinity) return "-∞";
	const rounded = Math.round(value * 100) / 100;
	if (!Number.isFinite(rounded)) return String(value);
	return String(rounded === 0 ? 0 : rounded);
}

export interface NumberStyle {
	round?: "round" | "ceil" | "floor";
	signed?: boolean;
	paren?: boolean;
}

/** Makes a number whole. "round" goes to the nearest whole number, halves away from zero (2.5 is 3, -2.5 is -3). */
export function roundNumber(value: number, mode: NumberStyle["round"]): number {
	if (mode === undefined || !Number.isFinite(value)) return value;
	if (mode === "ceil") return Math.ceil(value);
	if (mode === "floor") return Math.floor(value);
	return Math.sign(value) * Math.round(Math.abs(value));
}

/** Shows a result with the number flags: first rounding, then the sign, then brackets. Without flags this is formatNumber. */
export function formatResult(value: number, style: NumberStyle = {}): string {
	const shown = formatNumber(roundNumber(value, style.round));
	const signed = style.signed && !shown.startsWith("-") ? `+${shown}` : shown;
	return style.paren ? `(${signed})` : signed;
}
