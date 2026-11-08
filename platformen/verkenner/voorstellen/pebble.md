# Pebble (apps en wijzerplaten voor de nieuwe Pebble-horloges van Core Devices)

Vera, 8 nov 2026, run 06:32 (UTC). Zelf toegevoegd.

## Advies: nee voor nu, cijfer 4

Pebble is een jong platform dat groeit, zonder keuring, waar AI-gemaakte apps welkom zijn en waar nieuwe makers echt bovenaan komen: van de 50 meest gebruikte wijzerplaten sinds okt 2025 zijn er 33 dit jaar gemaakt. Daar kan Dortus een grote speler worden. Maar de taart is klein (±40.000 nieuwe horloges, GOK op cijfers van Core) en er is geen betalen in de winkel. Geld kan alleen via KiezelPay, een losse betaaldienst, en ik vond geen enkel bedrag van een maker. Voor € 350 per maand zouden we elke maand ±120 kopers van $3 moeten vinden in een markt van tienduizenden horloges; dat zie ik niet gebeuren zonder bewijs.

## Waarom gekozen
- Jong platform met nieuwe hardware (Pebble 2 Duo, Pebble Time 2, Pebble Round 2), waar we vroeg kunnen zijn. Past bij de vraag van Thijs: plekken waar Dortus groot kan worden.
- Open API met alle apps, datum en hearts, dus zelf te meten.

## Cijfers

### Bereik (GEZIEN, eigen meting 8 nov 2026 via appstore-api.repebble.com, collectie "all")
- Zichtbaar in de winkel: 3.785 apps en 4.327 wijzerplaten. Daarvan van voor 2017 (oude Pebble): 2.476 apps en 1.983 wijzerplaten. Core noemt ruim 15.000 in totaal (DERDEN, repebble.com/blog); de open collectie toont er ±8.100.
- Er is geen installs-teller, alleen hearts (een soort like). Een verhouding hearts tot installs vond ik nergens (GOK, niet te meten).
- Hearts van nieuwe uitgaven, eerste versie (veld changelog):

| Groep | n | mediaan | 10+ | 50+ | 100+ | max |
|---|---|---|---|---|---|---|
| Apps mrt t/m jun 2026 | 520 | 18 | 71% | 24% | 10% | 681 |
| Apps mei t/m aug 2026 | 547 | 10 | 52% | 13% | 4% | 681 |
| Wijzerplaten mrt t/m jun 2026 | 931 | 16 | 65% | 23% | 10% | 2.367 |
| Wijzerplaten mei t/m aug 2026 | 981 | 10 | 50% | 14% | 5% | 948 |
| Apps sep t/m nov 2026 (jong) | 380 | 5,5 | 35% | 3% | 1% | 252 |

- Nieuwe makers halen de top: in de lijst "meest gebruikt sinds okt 2025" (wijzerplaten, 50 plaatsen) staan 33 uit 2026, 12 in de top 20 (GEZIEN, collectie top-used?since=2025-10). In de top 200 op hearts staan maar 23 apps en 14 wijzerplaten uit 2026: oude Pebble-klassiekers hebben nog de meeste hearts, maar niet het meeste gebruik.
- Hearts zijn geconcentreerd: de beste 10% van de nieuwe uitgaven sinds maart heeft 58% van alle hearts (GEZIEN). Topmaker Dalpek haalt 3.321 hearts met 5 wijzerplaten, Limmat Studios 1.252 met 9 apps (GEZIEN).

### Geld
- Core heeft geen betalen in de winkel: de distributie-overeenkomst zegt dat Pebble geen mechanisme heeft om kosten te rekenen (DERDEN, https://developer.repebble.com/legal/distribution/ sectie 8). Geen aankondiging van betaalde apps gevonden in de blogs van dec 2025 t/m sep 2026 (DERDEN, https://repebble.com/blog/rss).
- KiezelPay (losse betaaldienst met proeftijd en ontgrendelcode) werkt nog op de nieuwe horloges (DERDEN, https://ttmm.is/portfolio/ttmm-alarms/ en http://luke.abq.nm.us/blog/2026-06-14-Pebble-Watchface-Strip-KiezelPay/). Afdracht van KiezelPay niet gevonden.
- Betaalde nieuwe uitgaven die ik zag: Flights van Limmat Studios, $5,99 na 12 uur proef, 414 hearts; TimeBlocks, $1 voor instellingen, 124 hearts; Touch Games Physics Trio, 3 gratis potjes per dag, daarna KiezelPay, 36 hearts (GEZIEN in de beschrijvingen).
- Van de 3.201 nieuwe uitgaven sinds maart 2026 noemen er 24 KiezelPay, 62 Ko-fi, 52 Buy Me a Coffee, 26 PayPal, 0 Patreon (GEZIEN, zoeken in de beschrijvingen; ondergrens, sommigen zetten het in de app).
- Bedragen van makers: **geen enkel gevonden**. Geen Patreon of graphtreon, KiezelPay toont geen cijfers, Ko-fi niet leesbaar zonder JavaScript. Mijn schatting is tientallen dollars per maand voor de beste makers (GOK).
- Beloning van Core: de app-wedstrijd van april 2026 verdeelde 25 horloges, geen geld (DERDEN, https://repebble.com/blog/spring-2026-pebble-app-contest).

### Grootte van het platform
- Pebble 2 Duo: 5.000 verzonden in nov 2025 (DERDEN, https://ericmigi.com/blog/pebble-rebble-and-a-path-forward/).
- Pebble Time 2: 23.000 gebouwd en meer dan 19.000 in gebruik in juli 2026 (DERDEN, https://repebble.com/blog/pebble-mega-update-july-2026).
- Pebble Round 2: ±14.000 voorbestellingen, verzending sinds 30 sep 2026 (DERDEN, https://repebble.com/blog/pebble-round-2-starts-shipping).
- Samen ±40.000 nieuwe horloges eind 2026, plus een onbekend deel van de oude Pebbles (GOK).

### Drukte (GEZIEN)
- Nieuwe uitgaven per maand sinds april 2026: ±90 tot 210 apps en ±200 tot 370 wijzerplaten. Rustig vergeleken met andere winkels, maar het stijgt sinds de levering van de Time 2.

### Vindbaarheid
- apps.repebble.com toont Top Charts op meest gebruikt, Top Picks (wisselt dagelijks), All (nieuwste eerst) en Most loved (DERDEN, https://apps.repebble.com/). Nieuwe apps staan dus vanzelf even bovenaan in All.
- Geen keuring: apps staan meteen live (DERDEN, https://developer.repebble.com/guides/appstore-publishing/publishing-an-app/).

### Past het bij ons
- Ja, technisch: C en JavaScript, SDK met `pebble new-project --ai`, AI wordt aangemoedigd (DERDEN, https://ericmigi.com/blog/re-introducing-the-pebble-appstore/). Een wijzerplaat of kleine app is in dagen te bouwen. Testen kan in de emulator; of die op GitHub Actions draait is niet nagegaan.
- Regels verbieden herhalende inhoud (veel bijna gelijke wijzerplaten) en indienen door een generatordienst (DERDEN, https://developer.repebble.com/legal/program-policies/ 4.1 en 4.4).

## Voordelen
- Nieuwe makers komen bovenaan in gebruik, weinig drukte, geen keuring, AI welkom.
- Kleine, enthousiaste gemeenschap die apps graag deelt en waardeert (hearts per app hoog voor de grootte).

## Nadelen
- Geen betalen in de winkel; KiezelPay is een omweg met codes, zonder openbare cijfers.
- Klein: tienduizenden horloges. Zelfs als top-maker blijft het geld klein (GOK).
- Geld is eenmalig per koper, geen abonnement.

## Eerste idee als we het toch doen
Een paar opvallende wijzerplaten van hoge kwaliteit (Daan voor uiterlijk) met gratis basis en $1 tot $3 via KiezelPay voor extra's, als goedkope proef om de verhouding hearts en verkoop zelf te meten. Alleen als er tijd over is naast de hoofdproducten.

## Wat het oordeel zou veranderen
- Core start betalen in de winkel, of meldt meer dan 100.000 horloges in gebruik.
- Een maker noemt een echt bedrag uit KiezelPay of Ko-fi boven ±$300 per maand.

## Herhaalmeting
Met `data/pebble-haal-script.py` over 4 weken: groeit het aantal nieuwe uitgaven en de hearts van de lichting mei t/m aug.
