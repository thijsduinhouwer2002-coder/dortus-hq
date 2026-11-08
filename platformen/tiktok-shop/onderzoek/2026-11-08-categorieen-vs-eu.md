# TikTok Shop App Store: welke categorie is in de EU nog leeg en wordt in de VS betaald?

Onderzoeker (agent), 8 nov 2026. Bron data: `platformen/pionier/data/tiktokshop-apps-<LAND>-2026-11-08.json` (VS 721 apps, 13 EU-landen samen 260 unieke apps, GB 253). Alle cijfers uit die bestanden zijn GEZIEN.
"Vaste prijs VS" = price_type 2 met start_price > 0 (samen 162 apps, gelijk aan het voorstel). Prijzen in de data staan in centen; mediaan is van de "vanaf"-prijs per maand.

## 1. Tabel per (sub)categorie (GEZIEN)

| Categorie / sub | VS | VS vaste prijs | VS mediaan vanaf | EU uniek | DE | NL | EU nieuw 2026 | Verhouding betaald VS : EU |
|---|---|---|---|---|---|---|---|---|
| Customer Reviews | 14 | 10 | $49 | 2 | 2 | 1 | 0 | 5,0 |
| LIVE Shopping | 9 | 5 | $55 | 0 | 0 | 0 | 0 | 5 : 0 |
| Finance / Accounting | 27 | 18 | $27 | 10 | 8 | 3 | 4 | 1,8 |
| Analytics & Reporting | 37 | 12 | $79,50 | 7 | 6 | 2 | 5 | 1,7 |
| Creator Collaborations | 82 | 25 | $149 | 17 | 9 | 6 | 13 | 1,5 |
| Catalog / Product Listing | 22 | 5 | $19 | 6 | 4 | 0 | 4 | 0,8 |
| Connectors | 43 | 23 | $18 | 40 | 32 | 20 | 10 | 0,6 |
| Multi-Channel Management | 67 | 23 | $39 | 49 | 25 | 11 | 22 | 0,5 |
| Order Management (OMS/WMS) | 89 | 12 | $32 | 23 | 12 | 7 | 11 | 0,5 |
| Dropshipping | 37 | 4 | $0,99 | 9 | 7 | 2 | 4 | 0,4 |
| Customer support | 36 | 6 | $69 | 18 | 12 | 7 | 4 | 0,3 |
| ERP | 126 | 7 | $15 | 33 | 26 | 18 | 9 | 0,2 |
| Video Shopping | 36 | 4 | $29,50 | 20 | 16 | 3 | 20 | 0,2 |
| Shipping | 22 | 3 | $65 | 12 | 3 | 1 | 2 | 0,2 |
| Print On Demand | 43 | 1 | $79 | 7 | 4 | 0 | 3 | 0,1 |

Kleine categorieën (1 tot 3 betaalde VS-apps, zoals CRM, Promotions, Returns, Loyalty) weggelaten. Analytics valt af door het besluit over winstanalyse; Creator Collaborations is in de EU al 17 apps (13 nieuw in 2026, Reacher, Cruva, Euka, Blazi zitten er al), dus niet leeg. Gekozen: Reviews, LIVE Shopping, Accounting.

## 2. Kandidaat A: reviews naar TikTok Shop overzetten

- EU (GEZIEN): Judge.me (12 landen, sinds sep 2025) en Junip (DE, ES, FR, IE, IT). GB: dezelfde twee.
- VS top 3 op volgorde (GEZIEN): Judge.me (#16, vanaf $15), Yotpo (#32, $89), AfterShip Feed for Review Sync (#82, $9). Verder REVIEWS.io $99, Loox $39,99, Okendo $109.
- Wat ze doen: alle 14 zijn koppelingen van een bestaand reviewplatform (Shopify) naar TikTok. De klant betaalt voor het reviewplatform, niet voor de koppeling.
- Shopify-reviews (GEZIEN, apps.shopify.com): Judge.me 49.796, Loox 10.061, Yotpo 4.626, Okendo 1.449, Junip 1.177, REVIEWS.io 778. Sterk betaalbewijs voor reviewsoftware, niet voor een losse TikTok-app.
- Waarom de EU leeg is (DERDEN): Yotpo-sync "only to merchants in the US" (https://support.yotpo.com/docs/en/tiktok-shop-yotpo-reviews-integration); AfterShip "limited to TikTok Shops in the United States" (https://support.aftership.com/en/feed/article/tiktok-shop-review-syndication-1mw1zid). Judge.me werkt wel in DE, FR, IT, ES, IE, UK, alleen in het betaalde Awesome-plan ($15) (https://judge.me/help/en/articles/10305619). De reviewimport is dus een functie die TikTok per land vrijgeeft; of elke partner hem mag gebruiken is niet gemeten.
- TikTok zelf: geïmporteerde reviews staan in Seller Center onder Products > Product ratings > Imported reviews (DERDEN, zelfde Judge.me-pagina). Geen eigen gratis import door TikTok gevonden.
- Oordeel: valt af voor Dortus. Wij hebben geen reviews om over te zetten; de grote spelers volgen vanzelf zodra TikTok de functie per land opent.

## 3. Kandidaat B: hulpmiddelen voor LIVE-verkoop (orders, inpakken, veilingen)

- EU en GB (GEZIEN): 0 apps in deze categorie.
- VS top 3 op volgorde (GEZIEN): CommentSold (#68, $149,99/mnd), livepilot (#272, prijs op aanvraag), Stickler (#280, $55 tot $375). Nieuw in 2026: PackSnap ($299,99 tot $2.499,99, inpakfoto's per order), Notbot ($30, label per gewonnen veiling), Live Show Tools (voorraad en inpakken), Copyt.
- Volgorde: geen enkele LIVE-app in de VS-top 60; dit is een kleine nis (GEZIEN, rang #68 en lager).
- Shopify-bewijs (GEZIEN): SoldLive 81 reviews, $35 tot $300/mnd; LiveMeUp 100 reviews, $89 tot $399/mnd; Videeo by CommentSold 23 reviews, $79,99 tot $599/mnd.
- Vraag in Europa: UK meer dan 6.000 LIVE-sessies per dag, +55% per jaar, LIVE-veilingen voor goedgekeurde verkopers (DERDEN, https://newsroom.tiktok.com/tiktokshoplivefashionandcollectables?lang=en-GB, https://www.retailgazette.co.uk/blog/2026/07/tiktok-shop-hits-300000-uk-small-business-sellers-as-live-sales-surge/). Countdown Bidding beschreven voor de VS (DERDEN, https://ppc.land/tiktok-shops-countdown-bidding-turns-live-sessions-into-real-time-auctions/). LIVE-veilingen in DE, FR, IT, ES of NL: niet gevonden.
- TikTok zelf: LIVE Manager voor het uitzenden bestaat (GOK, niet nagelezen in Seller University); de VS-apps zitten juist in het werk erna (inpakken, labels, gewonnen biedingen). Of TikTok dat gratis doet: niet gemeten.
- Oordeel: echt leeg (ook GB), prijzen zijn hoog, maar het is een nis met verzamelaars en tweedehands, en of de EU die markt heeft is onbewezen.

## 4. Kandidaat C: boekhoudkoppeling per land (TikTok-uitbetalingen naar het boekhoudpakket)

- EU (GEZIEN): 10 apps, maar het zijn vooral Duitse DATEV-exporten: EasyPliant, DATEV Export (pathway), Fybu, CONA, KudTax, AccountOne; verder ZonWizard, Kixmon en Margn (winst, FR) en Triffin (IE). In NL alleen AccountOne, ZonWizard en EasyPliant.
- VS top 3 op volgorde (GEZIEN): Onramp (#67, financiering, geen prijs), Link My Books (#94, $17 tot $329, naar Xero/QuickBooks), Finaloop (#103, $245 tot $995). Verder Synder $52, Taxomate $12, Webgility $79. In 2026 kwamen er in de VS 13 bij.
- Gat: in geen enkele EU- of GB-listing staat Moneybird, Exact, e-Boekhouden, SnelStart, Pennylane of Holded (GEZIEN, tekstzoektocht in alle 15 bestanden). Xero/QuickBooks-koppelingen (Synder, Parex) staan alleen in GB.
- Taal- en regelreden: in elk land een ander pakket (DATEV in DE, Moneybird/Exact in NL, Pennylane in FR) en btw per land/OSS; een VS-app op QuickBooks past daar niet (GOK voor de verdeling van pakketten per land; DATEV-aanbod GEZIEN).
- Shopify-bewijs (GEZIEN): A2X 363 reviews ($29 tot $115), Synder 219 ($65 tot $599), Finaloop 77, Link My Books 44 ($21 tot $100). Nederlands: Moneybird-koppelingen 30 reviews ($18 tot $36) en 7 reviews ($15,95) (https://apps.shopify.com/moneybird-1, https://apps.shopify.com/moneybird).
- TikTok zelf: uitbetalingsrapporten zijn te downloaden in Seller Center (GOK, niet nagelezen); een koppeling naar een boekhoudpakket biedt TikTok niet in de data.
- Oordeel: betalen is normaal en het "waarom wij" is duidelijk (lokaal pakket), maar de markt per land is klein en de DE-markt is al bezet.

## 5. Slot

- **Sterkste kandidaat: C, boekhoudkoppeling voor de landen buiten DE** (eerst NL met Moneybird/Exact/e-Boekhouden, daarna FR met Pennylane). Hier betalen verkopers aantoonbaar elke maand voor, het gat per land is GEZIEN, en een VS-app kan het niet zomaar (ander pakket, andere btw). B is leger en duurder, maar de vraag in de EU is onbewezen. A valt af.
- **Betaalbewijs:** C redelijk (VS 18 vaste prijzen, mediaan $27; Shopify A2X/Synder honderden reviews; NL-koppelingen maar 7 en 30 reviews, dus kleine aantallen). B redelijk voor de VS en het VK, dun voor de EU. A sterk voor reviewsoftware, maar niet voor ons.
- **Let op bij C:** de mediaan van $27 ligt dicht bij onze ondergrens van €15 en de Moneybird-koppelingen op Shopify vragen $16 tot $36. Winstdelen (ZonWizard, Kixmon) zitten deels in hetzelfde vak.
- **Nog niet gemeten:** hoeveel TikTok-verkopers er per EU-land zijn (NL pas sinds 28 mei 2026, DERDEN: https://newsroom.tiktok.com/tiktok-introduceert-tiktok-shop-in-nederland?lang=nl-NL); of TikTok een open API voor uitbetalingen geeft in de EU (partnerdocs niet gelezen); wat de Seller Center-rapporten al gratis doen; of LIVE-veilingen in de EU bestaan; installaantallen van de EU-apps (niet zichtbaar); of de reviewimport-API voor elke partner open is. Seller University (seller-de, seller-uk) niet gelezen, die laadt met JavaScript en er was geen tijd meer.

## Correcties na controle (8 nov, controleur, verwerkt door Tess)
Tabelrijen Reviews, LIVE Shopping, Accounting en Creator Collaborations zijn nageteld en kloppen; geen listing noemt Moneybird, Exact, e-Boekhouden, SnelStart, Pennylane of Holded (alle 18 bestanden); Shopify-cijfers Moneybird (30 en 7 reviews) en A2X (363) kloppen. Wel fout in de tekst hierboven:
1. NL-start: TikTok Shop NL is live sinds 15 juni 2026, registratie vanaf 1 juni. 28 mei 2026 is alleen de publicatiedatum van het persbericht.
2. "Xero/QuickBooks alleen in GB" klopt niet: Link My Books (Xero of QuickBooks Sync) staat ook in ES.
3. AccountOne noemt DATEV niet ("exported for further accounting use"). Kixmon is een Duitse winstapp (DE, ES, FR, IE, IT, GB), niet Frans; alleen Margn is Frans.
4. Moneybird-koppelingen op Shopify: moneybird-1 $18, $24, $36 per maand (30 reviews); moneybird $15,95 per maand (7 reviews).
5. Betaalbewijs voor C: redelijk voor de VS, dun voor NL. De VS-apps zijn vooral boekhoudplatforms, geen losse koppelingen, en of TikTok in de EU een API voor uitbetalingen geeft is nog niet gecontroleerd.
