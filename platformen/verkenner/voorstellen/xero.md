# Voorstel: Xero App Store (apps voor de boekhoudsoftware Xero)

Vera, verkenner, 7 nov 2026 run 20:33. Advies: **nee. Cijfer 2.**

## Wat is het
Xero is boekhoudsoftware voor kleine bedrijven, vooral in Australië, Nieuw-Zeeland en het VK. Xero noemt 4,6 miljoen+ abonnees (DERDEN: [developer.xero.com/pricing](https://developer.xero.com/pricing)). In de App Store op apps.xero.com staan koppelingen van andere bedrijven: facturen, voorraad, loon, rapporten.

## Zo gemeten (GEZIEN)
- robots.txt staat alles toe behalve zoeken en inloggen. De sitemap heeft 462 app-pagina's, maar dat is maar een deel van de winkel.
- Daarom alle 36 openbare functie- en branchepagina's gelezen, in alle 13 regio's (au, uk, nz, us, ca, global, za, sg, ie, my, hk, ph, id), met alle vervolgpagina's via `?page=N` (841 extra pagina's). Samen met de sitemap en de collectiepagina's: **1.128 apps**. Xero noemt zelf 1.000+ apps (DERDEN: [xero.com/au](https://www.xero.com/au/)), dus de lijst is redelijk compleet.
- Elke app-pagina gelezen. Apps die niet in de VS staan, laden alleen onder het adres van hun regio (bijvoorbeeld `/nz/app/2shakes`); die heb ik met de regio opnieuw gelezen. Met datum: **1.069**. 59 pagina's gaven geen datum, ook niet met regio.
- Per app: `listedDate`, het aantal reviews uit `reviewSummary`, `revenueTypeCode`, proefperiode, uitgelicht, maker. Gecontroleerd dat `reviewSummary.appEntryId` bij alle 1.069 hoort bij de app zelf (0 afwijkingen), dus geen cijfers van andere apps op de pagina (les van Pipedrive).
- Geen installs: Xero toont ze nergens. Reviews zijn de enige maat voor bereik.
- Data: `data/xero-apps-2026-11-07.json` (1.128 apps), `data/xero-lijst-2026-11-07.json` (per regio). Scripts: `data/xero-lijst-script.py` (verzamelt de lijst) en `data/xero-haal-script.py` (leest de pagina's, nu met regio). Herhalen: `python3 xero-lijst-script.py sitemap-urls.txt lijst.json`, daarna `python3 xero-haal-script.py slugs.json apps.json lijst.json`.

## Bereik (GEZIEN, reviews; installs niet te meten)
| Lichting | Apps | Mediaan reviews | 1+ | 5+ | 20+ | Top 3 |
|---|---|---|---|---|---|---|
| mei t/m aug 2026 (3 tot 6 mnd) | 48 | 0 | 20 (42%) | 8 (17%) | 1 | 86, 18, 13 |
| jan t/m aug 2026 | 85 | 0 | 41 (48%) | 17 (20%) | 1 | 86, 18, 18 |
| 2025 | 122 | 0 | 55 (45%) | 19 (16%) | 5 | 149, 67, 41 |
| 2024 | 79 | 0 | 38 (48%) | 19 (24%) | 3 | 93, 26, 22 |

- Mediaan 0 reviews in elke lichting. Ruim de helft heeft na een half jaar of langer nog geen enkele review.
- De beste nieuwe apps zijn gewone softwarebedrijven met hun eigen klanten: tofu (149, sep 2025), Mercury (86, de Amerikaanse bank), BSharp (67), Vinyl (41), Viberent (34), Karbon (31); uit 2024 Draftworx (93). Geen hobbymaker te herkennen.
- Hoeveel installs bij een review horen, weet ik niet. Xero publiceert geen installcijfers. Te meten alleen als een maker zijn aantal verbindingen openbaar noemt.

## Geld (DERDEN)
Dit is de doorslag. Xero veranderde in 2026 twee dingen:
1. **Betalen via de winkel is weg.** Xero App Store Subscriptions (XASS, waarmee Xero voor de maker afrekende tegen revenue share) stopte op 30 juni 2026. Makers moeten zelf afrekenen, bijvoorbeeld met Stripe (DERDEN: [CFOtech, 12 feb 2026](https://cfotech.com.au/story/xero-to-retire-app-store-billing-shift-to-api-tiers)). In mijn data zie ik dat terug: apps uit 2023 tot 2025 hebben bijna allemaal `revenueTypeCode` "RS", apps uit 2026 bijna allemaal "XC" (73 van 111) (GEZIEN; dat RS revenue share betekent is GOK, sterk).
2. **De maker betaalt Xero.** Sinds 2 maart 2026 betaal je per maand naar het aantal verbindingen (DERDEN: [pricing](https://developer.xero.com/pricing), [FAQ](https://developer.xero.com/faq/pricing-and-policy-updates)):
   - Starter: gratis, max 5 verbindingen, **geen** winkelvermelding.
   - Core: AUD 35 per maand, max 50, **geen** winkelvermelding.
   - Plus: AUD 245 per maand, max 1.000. Pas hier mag je in de App Store.
   - Voor een winkelvermelding (Plus en hoger): app-certificering, en volgens de security-FAQ ook een **jaarlijkse beveiligingskeuring** door Xero (5 dagen invullen, 5 tot 10 dagen beoordeling, daarna eventueel herstel). In de prijstabel staat de keuring pas vanaf Advanced; de FAQ zegt dat apps zonder keuring niet in de winkel komen (DERDEN: [security FAQ](https://developer.xero.com/faq/xero-ecosystem-security-requirements-update), correctie controleur).
- Gevolg: een vermelding in de winkel kost **minstens AUD 245 per maand (±€140)** voordat er één klant is. Met de bereikcijfers hierboven (mediaan 0 reviews) is dat geld dat er voor een kleine maker vrijwel zeker niet uitkomt (GOK, sterk).
- Kleine maker met een openbaar bedrag: niet gevonden bij kort zoeken (ook de controleur niet; Indie Hackers was niet leesbaar vanaf hier).
- Nieuwe regel in de voorwaarden: data uit de Xero API mag niet gebruikt worden om AI te trainen. Dat raakt ons niet direct, maar Xero is streng.

## Drukte (GEZIEN)
±10 nieuwe apps per maand (2025: 122, 2026 tot nu: 111). Rustig. De nieuwe prijsregels hebben het aantal nieuwe vermeldingen niet zichtbaar verlaagd (aug 2026: 20).

## Vindbaarheid
Winkel met functies, branches, regio's en collecties ("award winning", "top 2026"). Xero toont apps ook in de eigen software (App Launcher) en in campagnes, maar die promotie vereist Plus of hoger (DERDEN: pricing). Verder komen klanten via boekhouders: de bekende apps worden door accountants aangeraden.

## Past het bij ons
Slecht.
- Een Xero-app is een webdienst met een eigen server, OAuth-koppeling, opslag van boekhouddata van klanten en een beveiligingskeuring. Dat is geen product van 1 tot 2 weken, en het brengt risico voor Thijs (financiële gegevens van anderen).
- Thijs moet een account aanmaken, betalen (AUD 245 per maand) en de keuring ondertekenen.
- De klant is een bedrijf of boekhouder die op betrouwbaarheid kiest. Een nieuwe, kleine naam start daar met niets.

## Voor en tegen
Voor:
- Klanten die betalen voor software, en rustig (±10 nieuw per maand).
- Open te meten, data goed leesbaar.
Tegen:
- Geen betaling meer via de winkel, en de maker betaalt Xero AUD 245 per maand voor een vermelding.
- Mediaan 0 reviews, ook na een jaar.
- Beveiligingskeuring, eigen server, gevoelige data.

## Idee als we het toch deden
Een kleine rapportage- of controle-app (bijvoorbeeld een check op dubbele facturen) op Starter, zonder winkel, verkocht via boekhouders. Zonder de winkel is er geen bereik van het platform, dus dat is gewoon een losse SaaS. Niet doen.

## Nagekeken
Controleur 7 nov run 20:33: akkoord, 2 correcties (keuring pas bij een winkelvermelding, niet al bij Core; "geen enkele maker" werd "niet gevonden bij kort zoeken"). Tabel opnieuw uitgerekend: klopt precies. Steekproef van 10 pagina's: 10 van 10 gelijk. Van de 59 apps zonder datum: agicap heeft echt listedDate null, cin7omni en booke-ai geven 404 (weg uit de winkel). Nuance: bij zakelijke software zijn reviews zeldzaam, mediaan 0 reviews is niet per se 0 klanten; ook met een ruimere schatting hooguit een 3, advies blijft nee.

## Cijfer en advies
**Cijfer 2. Nee.** Bereik gemeten zwak (mediaan 0 reviews), geld via de winkel bestaat niet meer en de vermelding kost zelf geld, en het bouwen past niet bij ons.

Wat dit zou veranderen: Xero brengt betalen via de winkel terug, of geeft een gratis winkelvermelding voor kleine apps, én er zijn kleine makers met een openbaar bedrag van $300+ per maand.
