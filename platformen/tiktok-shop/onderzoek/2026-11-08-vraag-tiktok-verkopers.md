# Onderzoek TikTok Shop EU: vraag naar "EU-proof" (A) en winstanalyse (B)

8 nov 2026, ongeveer 25 minuten. Labels: GEZIEN (zelf gelezen), DERDEN (bron met link), GOK.

## 0. Het belangrijkste eerst

**TikTok heeft zelf al een gratis bulk-route voor de EU-velden (GEZIEN).** Het Seller University-artikel "Produkt verwalten" (seller-de) beschrijft:
- "Bulk-Aktionen > Produkte bearbeiten": producten kiezen, per categorie een Excel-sjabloon downloaden, invullen, terug uploaden. "Rot markierte Qualifizierungen und Merkmale sind obligatorisch." Ook Pfand-velden kunnen via Excel.
- "Verkäufer*innen können alle Informationen zum Hersteller und zur verantwortlichen Person für ihren Shop im Qualifizierungszentrum verwalten." Fabrikant en Responsible Person staan dus één keer per winkel opgeslagen.
- Bron: https://seller-de.tiktok.com/university/essay?knowledge_id=2495034554238752&default_language=de-DE (met Playwright gelezen)

Dat haalt de kern van idee A ("in bulk invullen vanuit één bedrijfsprofiel") grotendeels weg. Wat overblijft: het is omslachtig (een sjabloon per categorie, losse documenten per categorie, drie talen in België) en het werkt niet vanuit Shopify (zie punt 1).

## 1. Klachten van verkopers over de EU-velden

Gevonden, specifiek over TikTok Shop EU:
- **1 echte klacht (GEZIEN).** Shopify Community, "Official TikTok Shop + Shopify integration is extremely limited for real EU catalog management", 19 maart 2026, 2 berichten, 159 keer bekeken, 0 likes. Citaat: "there is no obvious bulk workflow for TikTok-required compliance fields", "merchants end up trapped between Shopify support and TikTok support". Het antwoord (31 mei) zegt dat verkopers terugvallen op de CSV/bulk-sjablonen in Seller Center, "painful, but currently the fallback". Toon: geïrriteerd, zakelijk, niet woedend. https://community.shopify.com/t/official-tiktok-shop-shopify-integration-is-extremely-limited-for-real-eu-catalog-management/592651
- Shopify Community zoeken op "tiktok GPSR", "tiktok responsible person", "tiktok EU compliance", "tiktok safety information": telkens alleen dezelfde draad (GEZIEN, search.json). Oudere draden over verplichte TikTok-velden (2023, VS: "Where to fill out TikTok required fields for Age Warning, Ingredients, and Manufacturer?", "products disapproved due to attributes required").
- Reddit: old.reddit JSON gaf geen antwoord; WebSearch met site:reddit.com gaf nul Reddit-treffers over TikTok GPSR (GEZIEN, zoekresultaten). Telt als: niet gevonden, niet als: bestaat niet.
- Duitse fora (Händlerbund, onlinehaendler-news): geen draad van verkopers over TikTok en GPSR gevonden. Wel juridische uitleg (WBS Legal, blckalpaca) (DERDEN, https://www.wbs.legal/it-und-internet-recht/tiktok-shop-in-deutschland-welche-rechtlichen-pflichten-haendler-jetzt-beachten-muessen-84629/).
- Consumentenkant: vzbv vond dat TikTok Shop gegevens van verkopers en fabrikanten "nicht immer" toont (DERDEN, https://www.vzbv.de/meldungen/online-shopping-tiktok-shop-stellt-nicht-immer-alle-informationen-zur-verfuegung). Druk op TikTok om te handhaven, dus op verkopers.
- Wat er wél veel is: hulpartikelen van koppelsoftware (M2E, Lengow, Channable, ChannelEngine, Tradebyte, SPL, 4Seller) over GPSR-velden voor TikTok (DERDEN, bijv. https://docs.m2ecloud.com/docs/tiktok-shop-gpsr-compliance-guide/, https://help.lengow.com/hc/en-us/articles/27440477496988). Bestaande tools lossen het dus al op als onderdeel van hun koppeling.
- Ter vergelijking (algemeen, niet TikTok): GPSR heet op Shopify "Total Nightmare" (2024) (DERDEN, https://community.shopify.com/t/eu-ni-general-product-safety-regulations-gpsd-gpsr-total-nightmare/338849/11).

Samengevat: hoe vaak: zeer weinig (1 draad); hoe recent: maart tot mei 2026; hoe boos: matig.

## 2. Doet TikTok het zelf al?

- Ja, zie punt 0: gratis bulk-bewerking via Excel en een "Qualifizierungszentrum" voor fabrikant en Responsible Person per winkel (GEZIEN).
- De regels worden wel steeds strenger, wat het onderhoud zwaarder maakt (GEZIEN, partner-changelog https://partner.tiktokshop.com/docv2/changelog, met Playwright):
  - 25 sep 2024: "EU market: Adding compliance required fields to Products API".
  - 11 dec 2024: "EU GPSR Communication Doc: Responsible person, Manufacturer and Safety label information".
  - 8 sep 2025: CLP/Biociden: 4 nieuwe velden (biocide, chemicaliën, gevarensymbolen, H-zinnen). https://partner.tiktokshop.com/docv2/page/vfskyjvl
  - 11 feb 2026: Responsible Person verplicht vanaf 28 feb 2026 in meer categorieën; bestaande listings bijwerken vóór 28 maart 2026, anders "may be deactivated". https://partner.tiktokshop.com/docv2/page/r1wchdjn
  - 3 sep 2026: Dangerous Goods voor UK en EU, verplicht vanaf 22 sep 2026 (batterijtype, aerosol- en vloeistofvolume, SDS/UN38.3 enz.). https://partner.tiktokshop.com/docv2/page/h6c7xadr
- Geen apart "Compliance center" met automatische controle van alle listings gevonden. Of het Qualifizierungszentrum ontbrekende velden per listing toont: niet gezien (GOK: waarschijnlijk alleen per product bij afkeuring).

## 3. Verkopers per EU-land (DERDEN)

| Land | Cijfer | Bron |
|---|---|---|
| EU totaal (FR, DE, IE, IT, ES) | meer dan 100.000 bedrijven, dagomzet met drie cijfers gegroeid aug 2025 tot feb 2026 | TikTok, via https://www.dataiads.io/en/blog/tiktok-shop-one-year-europe-review-2026 |
| DE | 14.000 verkopers (sep 2025), bestellingen gemiddeld +43% per maand | https://www.textilwirtschaft.de/fashion-management/so-viele-haendler-verkaufen-bereits-im-online-shop-von-tiktok-82555 |
| FR | ongeveer 33.000 actieve verkopers eind 2025 | dataiads (citaat TikTok France) |
| IT | meer dan 21.000 actieve verkopers (april 2026) | https://www.italiaoggi.it/marketing-e-media/marketing/tiktok-shop-compie-un-anno-in-italia-oggi-ospita-piu-di-21-mila-venditori-attivi-kk7fl30i |
| ES | meer dan 21.000 lokale verkopers, 18,7% van de Spaanse webverkopers | dataiads (NielsenIQ via TikTok) |
| IE | geen cijfer gevonden | |
| NL, BE, AT, PL | live sinds 15 juni 2026, registratie vanaf 1 juni; geen verkopersaantallen gepubliceerd | https://newsroom.tiktok.com/tiktok-introduceert-tiktok-shop-in-nederland?lang=nl-NL |
| Omzet FR+DE+ES+IT | ongeveer €499 mln in 90 dagen tot 9 juli 2026 (DE €175 mln, FR €133 mln, ES €105 mln, IT €87 mln) | Lengow/Kalodata, https://blog.lengow.com/tiktok-shop-europe-q2-2026-e500m-across-four-markets/ |

GOK: samen nu ruwweg 100.000 tot 130.000 EU-verkopers, waarvan een groot deel Chinese grensoverschrijdende verkopers met eigen ERP.

## 4. Apps in de EU-winkel: B tegenover A (GEZIEN, data 8 nov 2026)

Bestanden voor 13 EU-landen (AT BE CZ DE ES FR GR HU IE IT NL PL PT): 260 unieke apps. **De EU-data bevat geen prijsveld** (price_info ontbreekt bij alle 260), dus prijzen komen van de websites van de makers.

**Idee B, winst/analytics: 22 treffers, waarvan 11 echt over winst per bestelling/product:**
- Nexium Hub (jun 2026, 13 landen): €49 en €99 per maand op site (GEZIEN, nexiumhub.com)
- SellerGoo (okt 2026, 10 landen): €29, €39, €59 per maand (GEZIEN, sellergoo.com)
- NorthProfit (jul 2026, 1 land): bedragen €29, €49, €249, €499 op site (GEZIEN; GOK dat €29/€49 maandprijzen zijn)
- Kixmon Nettogewinn (dec 2025, 5 landen): $16 tot $249 per maand (GEZIEN, kixmon.com)
- ZonWizard (jan 2026, 13 landen): €70 op site (GEZIEN)
- Dashboardly Gewinn/Bestand (okt 2025, 4) en Dashboardly (jun 2026, 5), Conjura (sep 2025, 3), MerchantSpring (feb 2026, 2), Margn (jan 2026, FR), TrueProfit (aug 2024, 1, gratis volgens omschrijving): prijs niet gelezen
- Daarnaast ERP's met winstmodule (Lingxing, Irobotbox, Tallyvo, Stockitup).
- 8 van de 11 winst-apps zijn in 2026 bijgekomen. B is dus een gevulde, groeiende categorie met prijzen van €29 tot €99.

**Idee A, compliance: 1 treffer, en die is vals** (Furgonetka.pl, verzendlabels). Zoekwoorden GPSR, compliance, safety, responsible, EPR, Verpackung, CLP, Konformität, hazard: verder nul in de EU. In GB ook nul; in de VS 8, waarvan alleen "Apex Compliance App" listings scant (op claims, niet EU-velden).

**Ter vergelijking, Shopify (GEZIEN, apps.shopify.com/search?q=gpsr):** 103 apps voor "gpsr". De meeste "Free plan available"; meeste reviews 78 (EAS), 75 (Complimus), 29 (GCM, "bulk editing"). Enige vaste prijs op de eerste pagina: Meetanshi $9,99 per maand. Verkopers nemen GPSR-tools wel, maar willen er weinig voor betalen.

## Slot

Het bewijs dat TikTok-verkopers voor idee A een app nemen en betalen is zwak. De lege categorie is echt (nul apps in de EU), maar de pijn is weinig zichtbaar (één Shopify-draad, geen Reddit- of forumgolf) en TikTok biedt zelf gratis bulk-bewerking via Excel plus een centrale plek voor fabrikant en Responsible Person, terwijl koppelsoftware (M2E, Lengow, Channable) de velden al meeneemt. Wat overblijft is een smallere belofte: "zie welke listings nu of straks worden gedeactiveerd en los het op zonder 20 sjablonen", gedreven door telkens nieuwe regels (RP maart 2026, Dangerous Goods september 2026); op Shopify ligt de prijs voor zoiets rond gratis tot $10. Idee B heeft sterker bewijs van betalen (11 apps, prijzen €29 tot €99 per maand, 8 nieuw in 2026), maar is daardoor ook drukker; B is sterker als vraag, A is alleen sterker als gat, en dat gat is deels door TikTok zelf gedicht.
