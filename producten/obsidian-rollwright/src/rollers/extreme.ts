import { rangeOf, type RollOptions } from "../engine";

/** A roll that is the highest or lowest result its formula can give. */
export type Extreme = "max" | "min";

/**
 * "max" when total is the highest result the formula can give, "min" when it is the lowest,
 * otherwise undefined. Only when both ends are known for sure (see rangeOf): never for an
 * estimate, exploding dice, or a formula that always gives the same result.
 */
export function extremeOf(total: number, formula: string, options: RollOptions = {}): Extreme | undefined {
	const range = rangeOf(formula, options);
	if (range === null || range.min === range.max) return undefined;
	if (total === range.max) return "max";
	if (total === range.min) return "min";
	return undefined;
}

/** One d20 that counts: 1d20 or d20, or two d20 of which one is kept (advantage), with plain numbers added. */
const SINGLE_D20 = /^(?:1?d20|2d20k[hl]1?)(?:[+-]\d+)*$/i;

/**
 * The stamp on a crit or fumble. "NAT 20" and "NAT 1" only when exactly one d20 counts
 * (1d20 + 4, or advantage 2d20kh1): then the die really showed that number. For any other
 * formula (2d6, 4d6kh3, 1d20 + 1d4, Fudge dice) "NAT 20" would not be true, so it says MAX or MIN.
 */
export function stampText(formula: string, extreme: Extreme): string {
	if (SINGLE_D20.test(formula.replace(/\s+/g, ""))) return extreme === "max" ? "NAT 20" : "NAT 1";
	return extreme === "max" ? "MAX" : "MIN";
}
