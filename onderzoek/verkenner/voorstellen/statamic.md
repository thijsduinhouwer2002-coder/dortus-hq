# Voorstel: Statamic Marketplace (betaalde addons)

Vera, verkenner, 7 nov 2026 run 17:32 (lokale tijd, tweede platform van de run). Advies: **nee. Cijfer 2.**

## Wat is het
Statamic is een CMS op Laravel. In de Marketplace op statamic.com verkopen makers addons. De maker houdt 75%, uitbetaling via Stripe Connect direct bij aankoop (DERDEN: [Become a Creator](https://statamic.com/creator/begin)).

## Zo gemeten (GEZIEN)
- Alle 645 addons via de open API `https://statamic.com/api/v1/marketplace/addons` (43 pagina's, robots.txt staat alles toe). Die geeft prijs en edities, maar geen installs of datum.
- Daarom per addon de gegevens van Packagist erbij: downloads (totaal en per maand) en datum van de eerste versie. 523 addons hadden data. Van de 122 zonder: 108 zonder pakket (bijna allemaal oude Statamic v2-addons), 14 met een kapotte pakketnaam (2 betaald). Script: `data/statamic-haal-script.py`, analyse: `data/statamic-analyse-script.py`, data: `data/statamic-addons-packagist-2026-11-07.json`.
- Let op: Packagist-downloads tellen ook elke deploy en elke testrun. Het is dus geen aantal sites, eerder te hoog.
- Indeling: 363 gratis, 144 betaald, 16 freemium.

## Bereik (GEZIEN, Packagist-downloads)
| Lichting | Soort | Aantal | Mediaan totaal | Mediaan per maand | 100+ totaal |
|---|---|---|---|---|---|
| mei t/m aug 2026 (3 tot 6 mnd) | betaald | 12 | 16,5 | 3 | 17% |
| mei t/m aug 2026 | gratis | 25 | 84 | 40 | 48% |
| jan t/m apr 2026 | betaald | 7 | 19 | 0 | 29% |
| jul t/m dec 2025 (11 tot 16 mnd) | betaald | 10 | 511 | 103 | 80% |
| voor 2024 | betaald | 66 | 2.084 | 35,5 | 77% |

De groepen zijn niet even oud, dus vergelijk vooral per maand. Nieuwste betaalde (sep t/m nov 2026, n=28) mediaan 7,5 per maand.

## Geld
- Verkopen zijn nergens zichtbaar. Geen openbaar bedrag van een kleine addonmaker gevonden (controleur).
- Mediaanprijs betaalde addons sinds 2025: $49 (GEZIEN).
- Grootste nieuwe betaalde addon: Cargo ($199, 34.319 downloads) van Duncan McClean, maar hij werkt bij Statamic zelf (DERDEN: statamic.com/about), dus geen kleine maker. Daarna A/B Tester ($99, 3.499 downloads) en AI Translator ($49, 1.919).
- Er is een oudere laag kleine makers die verkoopt (22 betaalde addons met 500+ downloads per maand, zoals redirect van Rias.be), allemaal van voor 2024.

## Drukte (GEZIEN)
2025 ±5 nieuwe per maand, 2026 ±9, sep 21, okt 36. De piek komt van een paar makers: in okt 12 betaalde addons van één verkoper ("1994"), 4 van Karelia Labs, 4 van Brent Passmore. Zonder hen ±16 in okt.

## Markt (DERDEN)
14.812 live sites volgens BuiltWith (trends.builtwith.com/cms/Statamic), "minder dan 0,1%" volgens W3Techs. Ongeveer 2,5 keer kleiner dan Craft.

## Past het bij ons
Bouwen kan in 1 tot 2 weken (PHP, Laravel). Maar de markt is zo klein dat zelfs een goed product weinig kopers vindt.

## Voor en tegen
- Voor: 75% voor de maker, direct uitbetaald, weinig nieuwe addons per maand, open API.
- Tegen: heel kleine markt, nieuwe betaalde addons mediaan 3 downloads per maand, geen enkel bedrag van een kleine maker, de grootste nieuwe addon is van een medewerker.

## Advies
**Nee, cijfer 2.** Wat dit verandert: een sterke groei van Statamic (bijvoorbeeld door Laravel zelf), of een kleine nieuwe maker met een aantoonbaar bedrag. Craft CMS is de betere van de twee (zie `craft-cms.md`).

## Niet zelf gemeten
Echte verkopen en het aantal sites per addon. Alleen te zien voor een maker met een account.

Nagekeken door een controleur (7 nov): akkoord, 3 correcties verwerkt (piek door een paar makers, vergelijken per maand, de 122 zonder data).
