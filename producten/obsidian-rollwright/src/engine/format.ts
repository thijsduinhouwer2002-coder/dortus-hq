/** Shows at most two decimals and never "-0". Very large numbers cannot be rounded this way and stay as they are. */
export function formatNumber(value: number): string {
	if (value === Infinity) return "∞";
	if (value === -Infinity) return "-∞";
	const rounded = Math.round(value * 100) / 100;
	if (!Number.isFinite(rounded)) return String(value);
	return String(rounded === 0 ? 0 : rounded);
}
