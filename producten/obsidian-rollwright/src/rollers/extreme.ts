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
