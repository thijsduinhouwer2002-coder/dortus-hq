# Voorstel: TikTok Shop App Store, Europese markten (pionier)

Noor, 8 nov 2026, run 18:38 UTC. Gekozen na het bericht van Thijs (19:16): alleen nog winkels waar je nu al kunt verkopen.

**Cijfer: 7 (bijgewerkt 8 nov 19:50 UTC, was 6). Advies: ja met kleine inzet. De controle is gedaan: kleine Nederlandse BV's staan met één app in alle negen EU-landen (zie "Controle 8 nov 19:50" onderaan). Let op: het eerste productidee is veranderd van winstanalyse naar Europese productregels, omdat winstanalyse sinds juni vol begint te lopen.**

(Oorspronkelijk, 18:55 UTC: cijfer 6, ja na één controle: mag een Nederlands bedrijf ook in Duitsland, Frankrijk, Italië en Spanje listen?)

In één zin: TikTok Shop groeit het hardst van alle webwinkelplatformen, opende in juni 2026 in Nederland, en de Europese App Store heeft maar 260 apps, met lege categorieën die in de VS al vol zitten met tools van $99 tot $149 per maand.

## Wat het is
TikTok Shop is de webwinkel in TikTok (verkopen in video's, LIVE en een winkeltab). Verkopers (bedrijven) installeren apps uit de TikTok Shop App Store (ook "App and Service Store") via Partner Center. Er zijn twee Partner Centers: partner.us.tiktokshop.com voor de VS en partner.tiktokshop.com voor de rest (DERDEN, https://partner.tiktokshop.com/docv2/page/developer-onboarding).

## De vijf vragen

1. **Groeit het platform hard?** Ja. Wereldwijde omzet (GMV) 2025 $64,3 miljard, +94% op een jaar, VS $15,1 miljard, +68% (DERDEN, Momentum Works via https://www.contentgrip.com/tiktok-shop-data-analysis/). In Europa meer dan 100.000 bedrijven en de dagelijkse omzet groeide tussen augustus 2025 en februari 2026 met drie cijfers; Nederland, België, Oostenrijk en Polen live sinds 15 juni 2026, met verkopen over de grens ("Sell Across Europe") (DERDEN, https://www.socialmediatoday.com/news/tiktok-shop-grows-to-new-eu-merchant-countries/821443/ en https://www.shopifreaks.com/tiktok-expands-tiktok-shop-to-austria-belgium-the-netherlands-and-poland-starting-june-15/). Motor: TikTok zelf. In de VS zit TikTok sinds januari 2026 in een joint venture, maar e-commerce bleef bij de wereldwijde TikTok-bedrijven (DERDEN, https://fortune.com/2026/01/27/tiktok-deal-china-us-bytedance-winner-trump/).
2. **Is de winkel jong?** In Europa ja. Zelf geteld via de open portal-API op 8 nov (GEZIEN, script `data/tiktokshop-apps-meet.py`): VS 721 apps, VK 253, Duitsland 170, Spanje 165, Italië 156, Frankrijk 155, Ierland 135, Polen 83, Nederland 82, België 79, Oostenrijk 72. Samen 260 unieke apps in de negen EU-landen. Duitsland krijgt 2 tot 11 nieuwe apps per maand, de VS 9 tot 49 (GEZIEN, juni 2025 tot okt 2026, datum uit de service-id). Bijna alle EU-apps zijn grote koppelingen (M2E, CedCommerce, Lingxing, BaseLinker, Channable, Sendcloud) en Chinese ERP's.
3. **Kan er betaald worden?** Ja, met een eigen kassa. TikTok rekent niet zelf af en houdt niets in; de maker kiest in de listing "Free plan", "Paid plan" (bijvoorbeeld "From $80/month", met proef) of "Contact for pricing" en int zelf (DERDEN via hulpagent, gelezen in de partner-docs: https://partner.tiktokshop.com/docv2/page/app-price-information). Bewijs dat verkopers betalen: in de VS hebben 162 apps een vaste maandprijs; mediaan "vanaf" per categorie: creator-samenwerking $149, analyse en rapportage $99, klantenservice $89, reviews $49, multichannel $39 (GEZIEN in de listings). Dat zijn prijzen, geen verkoopcijfers: hoeveel klanten ze hebben is niet zichtbaar. Kosten vooraf: geen registratiekosten gevonden; wel een eigen kassa (bijvoorbeeld Stripe) en btw-administratie.
4. **Is er vraag?** Redelijk bewijs, niet zelf gemeten op Reddit (curl wordt daar geblokkeerd). Terugkerend (DERDEN): echte winst per bestelling na commissie, affiliatekosten, samples en retouren (https://community.hubspot.com/t/what-s-everyone-using-to-track-tiktok-shop-profits-accurately/141227/5, https://www.producthunt.com/p/hivehq/what-challenges-are-tiktok-shop-sellers-facing-when-tracking-real-profitability); creators vinden en samples volgen; voorraad synchroniseren. Nieuw en Europees: TikTok voegde in de partner-changelog verplichte velden toe voor de "Responsible Person" (GPSR), CLP en gevaarlijke stoffen, en een btw-dienst (DERDEN, documenttitels in de partner-docs).
5. **Is de eerste plek te pakken?** In Europa ja, in de VS niet. Categorieën in Duitsland en Nederland tegen de VS (GEZIEN): analyse en rapportage NL 2 (VS 37), creator-samenwerking NL 6 (VS 82), video shopping NL 3 (VS 36), reviews NL 1 (VS 14), boekhouding NL 3 (VS 27). Geen enkele app in Duitsland over Europese regels (GPSR, btw, EPR) gevonden (GEZIEN, zoektocht in naam en omschrijving van alle 170). Een Nederlandse maker die de Europese regels en de euro goed doet, kan daar vooraan staan; Amerikaanse en Chinese tools zijn daar zwak in (GOK).

## Toegang (belangrijk)
- Volgens de partner-docs moet de registratieregio passen bij de bedrijfsregistratie; lokale partners kiezen alleen hun eigen markt; alleen bedrijven uit China en Hongkong mogen grensoverschrijdend (DERDEN, https://partner.tiktokshop.com/docv2/page/developer-onboarding). Een Nederlands bedrijf is dus lokale partner voor Nederland. Of een app daarna via "Add market" ook Duitsland, Frankrijk, Italië en Spanje mag bedienen, staat er niet duidelijk. **Dat is de ene controle die van de 6 een 7 maakt.** Van de 82 Nederlandse apps staan er 72 ook in Duitsland (GEZIEN), maar dat zijn vooral grote of Chinese bedrijven.
- Registratie vraagt KVK-gegevens, een bedrijfsdocument, ID van de eigenaar, adres, logo en een bedrijfsintroductie (DERDEN, https://partner.tiktokshop.com/docv2/page/64f19899cb677b0286e75d67). Dat is een stap voor Thijs (inloggen, ID, voorwaarden). De VS en het VK vragen waarschijnlijk een lokaal bedrijf: niet voor ons.
- Keuring in stappen: registratie ±5 werkdagen, ontwerp 3 tot 5, test 7 tot 10, listing 7 tot 10, privacy ±2 weken; reken 4 tot 8 weken tot live (DERDEN voor de stappen, GOK voor het totaal; https://partner.tiktokshop.com/docv2/page/app-review-process).

## Wat ik niet kon meten
- Installaties per app: de App Store toont ze niet en de API geeft ze niet (GEZIEN, ook niet in service/detail). Bereik van een nieuwkomer is dus onbekend. Wel de volgorde in de standaardsortering (vermoedelijk populariteit), die het script bewaart.
- Verkopen van bestaande apps.
- Hoe snel de nieuwe landen (NL, BE, AT, PL) verkopers krijgen; alleen het artikel van TikTok zelf.

## Risico en waaraan je ziet dat het stokt
- TikTok bouwt zelf: in de VS staan al eigen apps (TikTok for Shopify, Zendesk-koppeling) en TikTok voegt API's toe voor creator-outreach. Teken: TikTok maakt de categorie zelf in Seller Center.
- Politiek: verbod of opsplitsing in Europa (DSA-onderzoeken). Teken: nieuws over een stop van TikTok Shop in een EU-land.
- Stopregel 4b: twee maanden geen groei van het aantal EU-apps en geen nieuwe landen, of TikTok verbiedt eigen kassa's.

## Categorie en eerste productidee
**Categorie: analyse en winst voor Europese verkopers (nu 2 apps in NL).** Product: "echte winst per bestelling" in euro, met commissie, affiliatekosten, samples, retouren en btw, plus een controle van elke listing op de Europese verplichte velden (Responsible Person, CLP, EPR). Gratis: winst van de laatste 30 dagen. Betaald: €19 tot €39 per maand per winkel (VS-mediaan in analyse is $99, dus ruimte), met 14 dagen proef. Wie betaalt: kleine en middelgrote webwinkels die op TikTok verkopen; hoe vaak: maandelijks; bewijs dat zulke mensen betalen: 12 analyse-apps in de VS met een vaste prijs, mediaan vanaf $99 per maand (GEZIEN, prijzen, geen aantallen).

## Wat er nodig is voor ja
1. Controle bij TikTok (via Thijs of de support van Partner Center): mag een Nederlands bedrijf ook in DE, FR, IT, ES listen? Ja maakt het een 7.
2. Thijs registreert als app-ontwikkelaar in Partner Center (KVK, ID, voorwaarden): stap voor zijn lijst.

## Herhaalmeting
Rond 8 dec: `for r in US GB DE FR IT ES IE NL BE AT PL; do python3 -I data/tiktokshop-apps-meet.py $r; done` en `python3 -I data/tiktokshop-apps-analyse.py data/tiktokshop-apps-NL-<datum>.json`. Vergelijk het aantal apps en de categorieën met 8 nov.


## Controle 8 nov 19:50 UTC (Noor): mag een Nederlands bedrijf buiten Nederland listen?

**Antwoord: ja, in de praktijk wel.** Zelf nagekeken in de tellingen van 8 nov (GEZIEN, `data/tiktokshop-apps-<land>-2026-11-08.json`, per app partner_id en service_id over de landen vergeleken):
- **Stockhub B.V.** (klein Nederlands WMS, Euregioweg 235 Enschede, GEZIEN op stockhub.nl): één partner, één app, aangemaakt 14 juni 2026 (de dag voor de start van TikTok Shop in Nederland), staat nu in alle negen EU-landen: DE, FR, IT, ES, IE, NL, BE, AT, PL.
- **Stockpilot** (Jiyu Ninja B.V., KVK 83679723, Utrecht, GEZIEN op stockpilot.com): één app, aangemaakt 12 juni 2026, in BE, DE, ES, FR, NL.
- **ChannelDock** (Nederlands) en **Monta** (Nederlands) idem: één app in alle negen landen of in vijf.
- **Sellasist** en **Apilo** (Pools): één app in alle negen landen.
- De docs zeggen het zo: een ISV kan via "+ Add market (Seller type)" markten aan een bestaande app toevoegen; "the available markets depend on your company's registration region and the app's business category" (GEZIEN, https://partner.tiktokshop.com/docv2/page/developer-onboarding en de pagina Create your App, gelezen met Playwright). De regel "local partners should choose only their local market" geldt voor de eerste registratie; daarna kan er per categorie een kwalificatie per markt bij.
- Wat nog niet zeker is: of dat voor elke categorie geldt. Alle Nederlandse voorbeelden zitten in orderbeheer en multichannel. Een paar Nederlandse en Poolse apps staan alleen in hun eigen land (ReplyBay, ESS, Stockitup, Selly.pl), maar dat kan een eigen keuze zijn. Kleine rest-onzekerheid; Thijs ziet het bij de registratie meteen in het keuzemenu.

## Bijsturing productidee (8 nov 19:50 UTC)
Bij het nakijken bleek de categorie winstanalyse in de EU niet meer leeg (GEZIEN, zelfde tellingen, aanmaakdatum uit de service-id):
- Nexium Hub (26 juni 2026, alle 9 EU-landen): "reale Nettomarge" na provisie, logistiek, btw en retouren.
- NorthProfit (27 juli 2026, alleen DE): winst per bestelling, servers in Duitsland, DATEV.
- SellerGoo (27 okt 2026, alle 9 EU-landen): live winst-en-verliesrekening met btw.
- Dashboardly (sinds okt 2025, 5 landen), Conjura (sinds sept 2025, 3 landen), TrueProfit (IE), plus boekhoudkoppelingen EasyPliant, KudTax en AccountOne (DATEV).
Drie nieuwe winstapps in vijf maanden, allemaal precies ons oude idee. Geen duidelijke nummer één (installs onzichtbaar), maar een nieuwkomer valt daar niet meer op. **Dit idee valt af als eerste product.**

**Nieuwe categorie: Europese productregels voor listings (GPSR, Responsible Person, CLP, gevaarlijke stoffen, Pfand en verpakking).**
- TikTok voegde in de partner-changelog voor de EU de laatste maanden achter elkaar verplichte velden toe: "EU GPSR Communication Doc - adding Responsible person, Manufacturer and Safety label information", "EU Markets: Category Rules Update – Responsible Person Attribute Now Mandatory", "EU market: New compliance data required - CLP/Biocides", "EU market: Pfand Fees and Packaging Type Data", "For UK & EU markets: Dangerous Goods (DG) Compliance Requirements", "EU Markets: Introducing VAT Calculation Service" en "Sell Across EU - Global Product APIs (GPA) to Local Replication Architecture" (GEZIEN, https://partner.tiktokshop.com/docv2/changelog, gelezen met Playwright).
- In de 260 EU-apps staat **geen enkele** app die dit als hoofdtaak heeft (GEZIEN, gezocht op GPSR, EPR, CLP, Responsible Person, Verpackung, Konformität in naam en omschrijving). Alleen de grote koppelingen (M2E, Lengow) vullen de GPSR-velden mee als ze producten overzetten (DERDEN, https://docs-m2.m2epro.com/docs/how-to-set-up-gpsr-compliance-for-tiktok-shop-using-m2e-connect/ en https://help.lengow.com/hc/articles/25473104444060). Wie direct in TikTok Shop verkoopt (geen Shopify, geen koppeling), heeft niets.
- Bewijs dat verkopers voor zoiets betalen: op Shopify bestaan betaalde GPSR-apps (DERDEN, https://apps.shopify.com/priceproof-gpsr; prijzen en aantallen niet kunnen lezen, de pagina laadt met JavaScript). Op Shopify-forums heet GPSR "Total Nightmare" (DERDEN, https://community.shopify.com/t/eu-ni-general-product-safety-regulations-gpsd-gpsr-total-nightmare/338849/11).
- Product: "EU-proof voor TikTok Shop". Leest alle listings via de Product API, laat per product zien welke verplichte EU-velden ontbreken (Responsible Person, fabrikant, veiligheidslabel, CLP, Pfand, gevaarlijke stoffen), vult ze in bulk in vanuit één bedrijfsprofiel en kopieert ze bij "Sell Across EU" naar elk land, met de juiste taal. Gratis: scan en lijst van wat ontbreekt. Betaald: bulk invullen en bewaken bij nieuwe regels, €15 tot €29 per maand per winkel, eigen kassa (TikTok houdt 0%).
- Waarom wij nummer één kunnen worden: niemand doet het nu, de regels veranderen steeds (dus een bewaakfunctie heeft blijvende waarde), en een Nederlands bedrijf in alle negen landen tegelijk is precies wat de lokale tools (alleen DE, alleen IT) niet zijn.
- Zwak punt, eerlijk: vraag naar een losse app op TikTok zelf is niet gemeten (geen forums te lezen, installs onzichtbaar). De velden zijn verplicht, dus elke verkoper moet ze invullen; de vraag is of ze daar een app voor nemen of het één keer met de hand doen. Teken dat het niet werkt: na lancering minder dan 20 installaties in 6 weken. Dan valt winstanalyse terug als tweede kans, of stoppen.

## Cijfer na de controle: 7
1 groeit hard (sterk), 2 winkel jong in de EU (260 apps, 2 tot 11 nieuw per maand in DE), 3 betalen werkt nu met eigen kassa en 0% afdracht, 4 vraag redelijk (verplichte velden, maar losse app niet bewezen), 5 categorie Europese regels leeg. De controle is ja, dus het voorstel komt op de afgesproken 7. Kosten vooraf: geen registratiekosten gevonden; wel een eigen kassa (Stripe of Polar) en een keuring van 4 tot 8 weken.

## Wat er nodig is voor de start (na ja van Hans)
1. Thijs registreert als app-ontwikkelaar (ISV) in het Global Partner Center (partner.tiktokshop.com/account/sign-up): KVK-uittreksel, ID, voorwaarden. Doel: Nederland, daarna via "Add market" DE, FR, IT, ES, BE, AT, PL, IE. Gebruik een e-mailadres dat niet aan een TikTok Shop-verkopersaccount hangt (GEZIEN, docs).
2. Een ontwikkelwinkel (Seller Center development shop) om tegen te testen; de manager bouwt en Daan keurt.
