export interface InlineDice {
	/** Position of the opening backtick in the line. */
	from: number;
	/** Position right after the closing backtick. */
	to: number;
	formula: string;
}

/** Finds `dice: x` in one line of text. Longer backtick runs are skipped. */
export function findInlineDice(line: string): InlineDice[] {
	const found: InlineDice[] = [];
	const pattern = /(`+)([^`]*)\1/g;
	for (let match = pattern.exec(line); match; match = pattern.exec(line)) {
		const formula = formulaFromCode(match[2] as string);
		if ((match[1] as string).length === 1 && formula !== null) {
			found.push({ from: match.index, to: match.index + match[0].length, formula });
		}
	}
	return found;
}

/** The formula in the text of a code element, or null if it is not a dice code. */
export function formulaFromCode(text: string): string | null {
	const match = /^dice:\s*(.*\S)\s*$/i.exec(text.trim());
	return match ? (match[1] as string) : null;
}
