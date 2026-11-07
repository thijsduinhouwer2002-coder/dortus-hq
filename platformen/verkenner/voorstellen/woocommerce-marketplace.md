# Voorstel: WooCommerce Marketplace (betaalde extensies op woocommerce.com)

Vera, verkenner, 7 nov 2026 run 16:33 (lokale tijd). Advies: **nee. Cijfer 2.**

## Wat is het
De officiële winkel van WooCommerce. Derde makers verkopen er betaalde extensies (jaarabonnement per site), Woo doet de verkoop en betaalt uit. De winkel zit in elke WooCommerce-installatie onder WooCommerce > Extensions. Dit is iets anders dan de gratis plugins op wordpress.org (al eerder nee, zie `onderzocht.md`).

## Zo gemeten (GEZIEN)
- Alle 1.562 productpagina's uit de openbare sitemap (`product-sitemap.xml` en `product-sitemap2.xml`) gelezen met een gewoon paginaverzoek. robots.txt staat `/products/` toe. Script: `data/woo-haal-script.py`, analyse: `data/woo-analyse-script.py`, ruwe data: `data/woo-2026-11-07.jsonl`.
- Per pagina staan in de pagina zelf: publicatiedatum, prijs, aantal reviews, maker, en het veld "installations". Op de pagina heet dat "Active installs", naar beneden afgerond (100, 200 ... 1K+, 2K+). Onder de 100 staat er 0 en wordt niets getoond. Dat is afgeleid uit de data: er bestaan geen waarden tussen 1 en 99, 0 komt alleen voor bij producten met hoogstens 8 reviews, en alle 44 Woo-producten hebben installs. De controleur zag op 6 pagina's dat het getal klopt met wat de pagina toont (3K+, 1K+, 100+, en bij 0 geen blok). De publicatiedatum is de echte aanmaakdatum (gelijk aan dateCreated).
- 186 pagina's zijn gratis vermeldingen (prijs 0) zonder deze velden: betaalproviders, koppelingen met SaaS-diensten van derden zoals Afterpay en AdRoll. 65 daarvan zijn van 2025 of later. Ze tonen geen installs en tellen niet mee. Over: 1.376 betaalde producten, waarvan 1.216 plugins van andere makers dan Woo (de tabel telt er 1.154, zonder de 62 van sep t/m nov 2026, die nog te jong zijn).

## Bereik (GEZIEN)
Plugins van andere makers dan Woo, naar publicatiedatum:

| Groep | Aantal | Mediaan actieve installs | 100+ | 1+ review |
|---|---|---|---|---|
| mei t/m aug 2026 (3 tot 6 maanden oud) | 85 | onder 100 | 1% | 9% |
| jan t/m apr 2026 | 119 | onder 100 | 1% | 17% |
| 2025 | 255 | onder 100 | 3% | 31% |
| 2024 | 126 | onder 100 | 21% | 59% |
| voor 2024 | 569 | 200 | 77% | 84% |

- Van alle 459 plugins die sinds jan 2025 tot eind aug 2026 verschenen, haalden er **9** de 100 actieve installs. Bij makers die pas sinds 2025 in de winkel staan: 6 van 249 plugins (102 makers).
- Nieuwe thema's sinds 2025: 51, geen enkele 100+.
- Let op: de sitemap toont alleen wat nu nog in de winkel staat. Wat al weg is, telt niet mee, dus het echte beeld is eerder slechter.

## Geld
- Maker krijgt 70% van de netto-omzet, maandelijks uitbetaald (DERDEN: [Vendor Agreement art. 2.2](https://woocommerce.com/woo-vendor-agreement/)). Geen kosten om te mogen verkopen gevonden (GOK).
- Mediaanprijs nieuwe plugins $39 (2025) tot $49 (2026) per jaar (GEZIEN).
- Beste nieuwe plugins sinds 2025, als GOK-bedrag (installs × jaarprijs × 70% / 12, en installs zijn naar beneden afgerond): Anti-Fraud Shield (KoalaApps, 100+, $99) ±$580 per maand, Stachethemes Seat Planner ±$460, daarna ±$170 tot $290. Alle negen staan op "100+", geen enkele op 200 of meer. 100+ betekent 100 tot 199, dus het echte bedrag kan tot bijna het dubbele zijn; dat verandert het beeld niet. KoalaApps en W7S zijn bovendien makers met veel producten.
- Geen controleerbaar bedrag gevonden van een maker die in 2024 of later begon (onderzoeker). Ellipsis schatte in 2022 dat drie oude verkopers samen ±75% van de omzet halen (DERDEN: [Ellipsis](https://getellipsis.com/blog/whos-winning-on-the-woocommerce-marketplace/)).

## Drukte (GEZIEN)
±20 tot 50 nieuwe producten per maand (2025: 13 tot 48, 2026: 16 tot 51). Dat is weinig, door de keuring. Maar de oude groep heeft de installs.

## Vindbaarheid
- Zoeken en "Discover" in WooCommerce > Extensions in elke winkel, plus een tab "Woo" bij Plugins toevoegen (DERDEN: [broncode Marketplace.php](https://github.com/woocommerce/woocommerce/blob/trunk/plugins/woocommerce/src/Internal/Admin/Marketplace.php)). Wat bovenaan staat bepaalt Woo zelf (GOK).
- Aantal winkels: ±4,3 miljoen, 10% minder dan een jaar eerder (DERDEN: [StoreLeads](https://storeleads.app/reports/woocommerce)).

## Past het bij ons
- Toelating: partneraccount, automatische tests, zakelijke keuring, codekeuring, UX-keuring, besluit binnen 30 dagen (DERDEN: [Woo partners](https://woocommerce.com/partners/), [submitting-your-product](https://developer.woocommerce.com/docs/woo-marketplace/submitting-your-product/)). Een gratis plugin zonder verdienmodel wordt niet aangenomen; gratis vermeldingen bestaan alleen als ingang naar een betaalde dienst. Geen AI-regel gevonden, wel eis van "originele" code.
- Bouwen in 1 tot 2 weken kan (PHP, WordPress), maar de keuring voegt weken toe.

## Voor en tegen
- Voor: geld loopt via de winkel, 70% voor de maker, niet exclusief, weinig nieuwe concurrenten per maand, kopers zijn winkels die betalen.
- Tegen: in het eerste jaar halen nieuwe plugins bijna nooit 100 actieve installs (1 tot 3%), na 2 tot 3 jaar ongeveer 1 op 5 en dan net boven de 100, de installs zitten bij plugins van voor 2024, de markt krimpt, en geen nieuwe maker met een aantoonbaar bedrag.

## Eerste idee als het toch ooit zou gaan
Alleen met een nieuwe verplichting met datum (zoals bij Shopify: een EU-regel waar winkels iets voor moeten hebben). Zonder zo'n golf niet.

## Advies
**Nee, cijfer 2.** Bereik voor nieuwe makers lijkt het laagste van alle winkels met betaling die we maten. Let op, de maten verschillen: hier actieve installs met een drempel van 100, bij Fantasy Grounds Forge mediaan 15 kopers, bij Superhive 31% met 10+ verkopen. Maar 1% met 100+ na 3 tot 6 maanden is ook naast die maten erg laag. Wat dit zou veranderen: een nieuwe verplichting voor webwinkels waar nog geen goede extensie voor is, of bewijs dat Woo nieuwe extensies actief naar voren haalt.

## Niet zelf gemeten
- Hoe Woo "installations" telt (alleen sites met een gekoppeld Woo-abonnement?) staat nergens.
- Verkopen zelf zijn niet zichtbaar; installs onder 100 zijn niet zichtbaar.
- Van de 20 producten met een externe licentie, SaaS of freemium staan er 12 op 0. Telt Woo alleen sites met een gekoppeld Woo-abonnement, dan zijn installs bij die vorm te laag.

Nagekeken door een controleur (7 nov): akkoord, 8 correcties verwerkt.
