/**
 * Offline check of a license key of the form RW1-XXXXX-XXXXX-CCCCCC.
 * The last part is a checksum over the rest. It catches typos and marks a key
 * as well formed. It is no protection against someone who reads this file.
 * Nothing leaves the device: no network, no telemetry.
 */
const KEY_SHAPE = /^RW1-[A-Z2-9]{5}-[A-Z2-9]{5}-[0-9A-F]{6}$/;

export function licenseChecksum(body: string): string {
	let hash = 0x811c9dc5;
	for (let i = 0; i < body.length; i++) {
		hash ^= body.charCodeAt(i);
		hash = Math.imul(hash, 0x01000193) >>> 0;
	}
	return (hash >>> 8).toString(16).toUpperCase().padStart(6, "0");
}

export function isValidLicenseKey(key: string): boolean {
	const clean = key.trim().toUpperCase();
	if (!KEY_SHAPE.test(clean)) return false;
	return licenseChecksum(clean.slice(0, clean.lastIndexOf("-"))) === clean.slice(clean.lastIndexOf("-") + 1);
}

/** Empty while payment is not arranged. The buy button stays hidden as long as this is empty. */
export const BUY_URL = "";

export function shouldShowBuyButton(url: string = BUY_URL): boolean {
	return url.trim() !== "";
}
