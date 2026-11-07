import { browser } from "@wdio/globals";

/**
 * Klikt worp i (in volgorde van querySelectorAll op `${sel} .rollwright-roll`) en zet vlak daarvoor,
 * in dezelfde stap, het merkteken data-e2e-oud op de oude uitkomst (markeer: true). Wacht tot de worp
 * er echt staat. Waarom: kort na het openen haalt Obsidian de alinea's van de leesweergave even weg en
 * zet dezelfde knopen terug (diagnose run 42390461178). Een `?.click()` in dat gat deed stilletjes
 * niets. Zie ook geschiedenis.e2e.mjs, waar dit de wiebel gaf.
 * Met ctrl: true een klik met Ctrl ingedrukt (opent de bron), zoals een gebruiker Ctrl-klikt.
 */
export async function klikWorp(sel, i = 0, { markeer = false, ctrl = false } = {}) {
	await browser.waitUntil(async () => browser.execute((sel, i, markeer, ctrl) => {
		const el = document.querySelectorAll(`${sel} .rollwright-roll`)[i];
		if (!el) return false;
		if (markeer) {
			const value = el.querySelector(".rollwright-value");
			if (!value) return false;
			value.setAttribute("data-e2e-oud", "1");
		}
		if (ctrl) el.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true, ctrlKey: true }));
		else el.click();
		return true;
	}, sel, i, markeer, ctrl), { timeout: 5000, timeoutMsg: `worp ${i} in ${sel} stond er niet om op te klikken` });
}
