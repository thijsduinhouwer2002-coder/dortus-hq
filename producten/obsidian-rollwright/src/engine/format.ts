/** Shows at most two decimals and never "-0". */
export function formatNumber(value: number): string {
	const rounded = Math.round(value * 100) / 100;
	return String(rounded === 0 ? 0 : rounded);
}
