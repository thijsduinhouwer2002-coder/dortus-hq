export interface InlineDice {
	/** Position of the opening backtick in the line. */
	from: number;
	/** Position right after the closing backtick. */
	to: number;
	formula: string;
	/** True for `dice+:`: the result is kept on disk across restarts. */
	keep: boolean;
}

/** Finds `dice: x` in one line of text. Longer backtick runs are skipped. */
export function findInlineDice(line: string): InlineDice[] {
	const found: InlineDice[] = [];
	const pattern = /(`+)([^`]*)\1/g;
	for (let match = pattern.exec(line); match; match = pattern.exec(line)) {
		const code = readDiceCode(match[2] as string);
		if ((match[1] as string).length === 1 && code !== null) {
			found.push({ from: match.index, to: match.index + match[0].length, formula: code.formula, keep: code.keep });
		}
	}
	return found;
}

export interface DiceCode {
	formula: string;
	/** "dice+:" keeps the result across restarts. "dice:" and "dice-:" never do. */
	keep: boolean;
}

/**
 * Reads "dice:", "dice+:" and "dice-:". "dice-mod:" is refused on purpose (null):
 * it would change the note, and that is not built yet.
 */
export function readDiceCode(text: string): DiceCode | null {
	const match = /^dice([+-]?):\s*(.*\S)\s*$/i.exec(text.trim());
	return match ? { formula: match[2] as string, keep: match[1] === "+" } : null;
}

/** The formula in the text of a code element, or null if it is not a dice code. */
export function formulaFromCode(text: string): string | null {
	return readDiceCode(text)?.formula ?? null;
}
