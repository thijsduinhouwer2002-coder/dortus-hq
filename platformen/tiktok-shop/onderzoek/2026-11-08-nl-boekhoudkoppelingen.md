# Betalen NL/BE webverkopers voor marktplaats naar boekhouding? (8 nov 2026)

Gemeten met curl en Playwright, alleen lezen. Labels: GEZIEN (url), DERDEN (link), GOK.

| Tool | Marktplaatsen | Pakketten | Prijs | Bewijs van klanten |
|---|---|---|---|---|
| Webwinkelfacturen.nl | Bol.com (plus veel webshops/kassa's); geen Amazon/TikTok op homepage | Moneybird, Exact, e-Boekhouden, Twinfield, Informer e.a. | €80 / €130 / €180 per jaar (≈ €7 tot €15 p/m), korting per extra winkel. GEZIEN webwinkelfacturen.nl/prijzen | Claim "duizenden klanten", "Jun 2021: 1000 mensjaar bespaard", rij klantquotes. GEZIEN webwinkelfacturen.nl. Enige Bol.com-koppeling in Moneybird-overzicht. GEZIEN moneybird.nl/product/koppelingen/webshops/ |
| iWebDevelopment | Bol.com, Amazon | Exact Online | Bol: €12, €19 of €26 p/m (jaar), €13/€21/€29 maandelijks; afletteren +€17,50 p/m. GEZIEN iwebdevelopment.com/exact-online/bol | Staat in Exact App Store met Bol- en Amazon-app. GEZIEN exact.com/nl/app-store/amazon-iwebdevelopment. Geen reviewaantal gezien |
| xCore | Bol.com, Amazon | Exact Online | €29 p/m, add-ons €6 tot €12 p/m, installatie eenmalig €250. GEZIEN xcore.nl/bol-com-exact-online-koppeling/ | In Exact App Store (bol-com-koppeling-xcore, amazon-koppeling-xcore). GEZIEN broncode exact.com/nl/app-store/verkoop/webshop-koppeling. Klantcases genoemd, niet geteld |
| Informer (pakket) | Bol.com via Webwinkelfacturen | Informer | €72 per jaar (tot 250 facturen) aan Webwinkelfacturen. GEZIEN informer.nl/koppelingen/webshops/bol-com | Indirect: pakket verwijst naar betaalde koppeling |
| Schakel (schakel.app) | Bol.com live; Amazon, Etsy, Zalando "aanvragen"; pagina tiktokshop-moneybird bestaat | Moneybird, Exact, SnelStart, e-Boekhouden | €0, €10 of €30 p/m. GEZIEN schakel.app/prijzen | Geen klantbewijs gezien; lijkt nieuw (GOK). Vergelijkt zich zelf met Webwinkelfacturen. GEZIEN bolmoneybird.pages.dev |
| Link My Books | Amazon (ook NL/BE), eBay, Etsy, Shopify, TikTok Shop | Xero, QuickBooks (Sage genoemd); geen Moneybird/Exact gezien | Staffel per orders, bedragen niet uit pagina te halen. GEZIEN linkmybooks.com/pricing | "5/5 op 510+ reviews" en meer. GEZIEN linkmybooks.com/pricing |
| A2X | Amazon, eBay, Etsy, TikTok Shop, Shopify, Walmart | QuickBooks, Xero, NetSuite; geen NL-pakket | Bedragen laden via script, niet gezien | Niet gemeten |

Extra waarnemingen
- Moneybird-koppelingenpagina toont geen reviews of installaties, alleen ontwikkelaarsnamen. Voor marktplaatsen staat er alleen Bol.com (Webwinkelfacturen). GEZIEN moneybird.nl/product/koppelingen/webshops/
- Exact App Store "Webshop koppeling" heeft 44 partners; marktplaats-apps: Bol (xCore, iWeb, Webwinkelfacturen), Amazon (xCore, iWeb), plus Order2Flow ("Koppel Exact Online aan bol, Amazon..."). Reviewaantallen niet zichtbaar zonder inloggen. GEZIEN exact.com/nl/app-store/verkoop/webshop-koppeling
- Trustpilot blokkeerde de bot (niet gemeten). Boloo laadde niet binnen 30 s (niet gemeten). Channable, Sellvia, Bolfa niet onderzocht wegens tijd.
- TikTok Shop naar NL-pakket: alleen Schakel heeft een pagina "tiktokshop-moneybird" (GEZIEN schakel.app, HTTP 200), maar TikTok Shop staat niet als live kanaal (GOK: aanvraagpagina). Link My Books en A2X doen TikTok Shop wel, maar alleen naar Xero/QuickBooks/NetSuite. GEZIEN linkmybooks.com/pricing, a2xaccounting.com/pricing. Geen andere NL-aanbieder gevonden via WebSearch.

## Slot
Het betaalbewijs is redelijk: minstens drie NL-bedrijven (Webwinkelfacturen, iWebDevelopment, xCore) verkopen al jaren betaalde Bol.com- en Amazon-koppelingen naar Moneybird/Exact en zijn opgenomen in de officiële app-overzichten, maar harde klantaantallen (reviews, installs) heb ik niet kunnen zien. De gangbare prijs ligt tussen €7 en €15 per maand voor Moneybird/e-Boekhouden-achtige pakketten en €12 tot €29 per maand (plus add-ons) voor Exact Online. Een werkende TikTok Shop naar Moneybird/Exact-koppeling bestaat nog niet aantoonbaar; Schakel lijkt de enige die het plant, wat het gat bevestigt maar ook een directe concurrent aankondigt.

## Nagekeken (Tess, 8 nov 23:35 UTC)
Zelf met curl: webwinkelfacturen.nl/prijzen toont €80, €130 of €180 per jaar (tot 250, tot 1000, meer dan 1000 transacties); schakel.app/koppelingen/tiktokshop-moneybird/ bestaat (HTTP 200); schakel.app/prijzen noemt onder meer €0, €10 en €30. Klopt.
