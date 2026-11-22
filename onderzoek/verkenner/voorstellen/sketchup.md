# Voorstel: SketchUp Extension Warehouse

**Advies: nee voor nu.** Cijfer 4. Onderzocht 9 nov 2026 run 02:31 (Amsterdam), eigen meting van alle 1.429 zichtbare extensies via de openbare winkel-API (zonder inlog; Thijs noemt het lezen van deze API sinds 9 nov in zijn vaste toestemming). Plus een onderzoeker voor het geld. Controleur: akkoord met alle cijfers, drie aanvullingen verwerkt.

Kort: gratis extensies krijgen behoorlijk bereik (mediaan 236 downloads na 3 tot 6 maanden, 67% haalt 100+), en de winkel is rustig (±20 tot 46 nieuwe per maand). Maar betaalde extensies blijven klein: nieuwe betaalde halen mediaan 14 tot 25 downloads (waarschijnlijk vooral proeven), de beste betaalde extensie ooit heeft 11.804 downloads in 9 jaar, en geen enkele kleine maker deelt een bedrag. Geld is dus niet aangetoond.

## Wat is het
De winkel van Trimble voor Ruby-extensies voor SketchUp (desktop, Windows en Mac). SketchUp heeft meer dan 1 miljoen betalende abonnees (nov 2024, GEZIEN door onderzoeker, news.trimble.com). SketchUp for Web draait geen extensies (GEZIEN, help.sketchup.com/en/sketchup-web/web-features).

## Cijfers

### Drukte (GEZIEN, eigen meting)
- 1.429 zichtbare extensies: 983 gratis, 236 betaald in de winkel, 210 "listing" (verkocht op de eigen site van de maker).
- Nieuw per maand (op aanmaakdatum van het pakket): 2025 6 tot 19, 2026 20 tot 46 (jan 20, mrt 39, sep 46, okt 18). 2026 tot nu 301, tegen 143 in heel 2025.
- 155 makers plaatsten iets in het laatste jaar; WorkLab Extensions alleen al 25.
- Let op (controleur): met `showHidden=true` geeft de API 4.715 pakketten, dus ruim 3.200 verborgen of weggehaalde (concepten, afgewezen, ingetrokken). Ik zie alleen de overlevers; alle cijfers hieronder zijn daardoor eerder te rooskleurig. Een paar oude pakketten zijn opnieuw geplaatst (s4u-reeks 2020), dus de aanmaakdatum is niet altijd de eerste uitgave.

### Bereik (GEZIEN, eigen meting, downloads per extensie)
| Leeftijd | n | Mediaan downloads | 100+ |
|---|---|---|---|
| 0 tot 3 mnd | 89 | 13 | 21% |
| 3 tot 6 mnd | 84 | 40 | 37% |
| 3 tot 6 mnd, echt gratis | 43 | 236 | 67% |
| 3 tot 6 mnd, betaald | 38 | 14 | 5% (2 van 38) |
| 6 tot 12 mnd | 146 | 363 | 71% |

Gratis bereik is goed vergeleken met andere winkels (WooCommerce 1% 100+, Firefox mediaan ±1 per dag). Oude gratis toppers halen 1 tot 2 miljoen downloads.

### Geld
- Trimble rekent af: eenmalig of abonnement, de meeste met proef (211 van 236 betaalde hebben een proef, GEZIEN). Aankopen niet terug te krijgen (GEZIEN, help.sketchup.com/extension-warehouse/paid-extensions, bijgewerkt 29 sep 2026).
- Afdracht 30% en uitbetaling na 3 tot 4 maanden volgens makers op het forum in 2022 (DERDEN, forums.sketchup.com/t/paid-plugins-should-be-labeled-so/191248). Officiële voorwaarden niet leesbaar (developer.sketchup.com laat curl niet door). Verkopen vraagt eerst developer-status en een aanvraag bij Trimble (DERDEN).
- Nieuwe betaalde extensies sinds 2025, minstens 3 maanden oud: n=75, mediaan 25 downloads, 15 halen 100+, 6 halen 300+ (GEZIEN). Mediaanprijs $10 (kwart onder $5,50, kwart boven $24,99).
- Downloads van betaalde extensies tellen waarschijnlijk proeven mee (niet bewezen). Rekenvoorbeeld (GOK): 300 downloads, 20% koopt, $15, 70% voor de maker: ±$630 in totaal, niet per maand.
- Beste betaalde ooit: Eneroth Slicer 11.804 downloads ($5) sinds 2017. Beste nieuwe: Eclipse Cabinets PRO 841 downloads ($149, jan 2026), een bedrijf.
- Kleine makers die ervan leven bestaan (Medeek: "my only income source", 2022; Eneroth verkoopt; Fredo6 vraagt sinds 2022 $12 per plugin via SketchUcation; Curic verkoopt op Gumroad met 328 beoordelingen bij Curic Studio $99), maar niemand noemt een bedrag (DERDEN). Graphtreon: geen enkele extensiemaker gevonden.
- Veel makers verkopen buiten de winkel (210 listings, Gumroad, SketchUcation) vanwege de afdracht en trage uitbetaling (DERDEN).

### Vindbaarheid
- Winkel: Featured (gekozen door SketchUp) en Top Extensions (meeste downloads); zoeken sorteert op relevantie, prijs of datum, niet op populariteit (GEZIEN door onderzoeker). Reviews bestaan, maar het veld in de API staat overal op 0 en de reviewpagina's zijn verboden in robots.txt.
- Ook in SketchUp zelf (Extension Manager). Tweede winkel: SketchUcation (verbiedt ClaudeBot, niet gelezen). YouTube (The SketchUp Essentials).

### Past het bij ons
- Ruby, één bestand (.rbz). Klein te bouwen. Maar testen vraagt SketchUp desktop (betaald abonnement, Windows of Mac); op GitHub Actions niet zonder licentie (GOK).
- Verkopen vraagt developer-status en papieren bij Trimble: stap voor Thijs.

## Nieuw en mogelijk een productkans later
- SketchUp 2027 (okt 2026) ging van Ruby 3.2 naar 3.4; Trimble waarschuwde dat sommige extensies stuk gaan, gebruikers melden kapotte plugins (DERDEN, forums.sketchup.com/t/plugins-not-working-in-sketchup-2027/351106).
- Van de 197 extensies met 20.000+ downloads noemen er 64 geen SketchUp 2025 of nieuwer in hun eigen versielijst (GEZIEN), bv. CLF Shape Bender (1 miljoen), Curic Mirror, Windows Builder. Die lijst vult de maker zelf in, dus het bewijst niet dat ze kapot zijn. Het zijn wel gratis extensies: bereik, geen geld.

## Voor- en nadelen
Voor: goed gratis bereik, rustige winkel, betalen en proef zitten in de winkel, groot betalend publiek (1 miljoen+ abonnees), net een Ruby-wissel die oude extensies breekt.
Tegen: betaalde extensies verkopen weinig (mediaan 14 tot 25 downloads, 5% van de jonge betaalde haalt 100+), 30% afdracht en trage uitbetaling (DERDEN), geen enkele maker met een bedrag, testen vraagt een betaalde desktop-app, ruim 3.200 verborgen pakketten (veel uitval).

## Eerste idee (GOK)
Gratis extensie die een kapotte populaire extensie vervangt op SketchUp 2027 (bereik), met een betaalde Pro-versie. Pas zinvol als geld wel aangetoond wordt.

## Wat er nog moet gebeuren voor een hoger cijfer
1. Eén kleine maker met een bedrag (Medeek, Eneroth, Curic vragen kan alleen via Thijs; niet doen zonder reden).
2. Herhaalmeting: dezelfde API over 4 weken (`data/sketchup-ew-script.py`). Als nieuwe betaalde extensies dan snel stijgen (bv. 6 van 75 naar 15+ met 300+), opnieuw wegen.

## Herhaalmeting
`python3 -I data/sketchup-ew-script.py uit.jsonl` (2 verzoeken, ±1 minuut). Data van vandaag: `data/sketchup-ew-2026-11-09.jsonl`.
