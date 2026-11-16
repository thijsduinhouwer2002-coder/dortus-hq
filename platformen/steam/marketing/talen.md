# Talen en spelers in 245 bureaubladdemo's (Sem, run 6, 16 nov 2026)

Bewijs voor het talenbesluit vóór 1 dec (fest-plan punt 6, hoofdchat met Thijs). Ik beslis het niet; dit is wat de demo's in onze hoek laten zien.

**Hoe:** de 245 aangekondigde bureaubladspellen met demo uit de nulmeting (spelers tegelijk gemeten ma 16 nov 12:38 tot 12:45 UTC), talen van het hoofdspel via appdetails (GEZIEN 16 nov ±17:00 UTC). Script `data/talen-demos.py`, uitkomst `data/talen-demos-2026-11-16.csv`.

| Groep | Aantal demo's | 1+ speler | 5+ spelers | 20+ spelers | gemiddeld (zonder Character House) |
|---|---|---|---|---|---|
| Alle | 245 | 31% | 10% | 10 | 5,2 |
| Met Vereenvoudigd Chinees | 175 | 37% | 13% | 9 | 6,8 |
| Zonder Vereenvoudigd Chinees | 70 | 16% | 3% | 1 | 1,2 |
| Chinees, Japans en Koreaans samen | 114 | 40% | 16% | 6 | 8,8 |
| Alleen Engels | 53 | 19% | 2% | 1 | 1,5 |
| 1 tot 3 talen | 103 | 19% | 2% | 1 | 0,9 |
| 4 tot 9 talen | 61 | 36% | 18% | 6 | 11,1 |
| 10 of meer talen | 81 | 41% | 14% | 3 | 6,4 |

- **De drie grootste demo's hebben alle drie Chinees, Japans en Koreaans**: Character House (12.052), Keyboard Farm (396), Desktop Dreampair (271). Van de top 10 hebben er 6 die drie talen.
- **Van de 10 demo's met 20+ spelers hebben er 9 Vereenvoudigd Chinees.** Zonder Chinees haalt 3% de 5 spelers, met Chinees 13%.

**Waarom dit geen hard bewijs is (eerlijk):**
1. **Tijdstip.** De eerste meting was om 12:40 UTC, de Aziatische avond. **Tweede meting om 17:03 UTC** (01:03 in China, nacht in Azië, middag in de VS; `data/demo-spelers-2026-11-16-1703utc.csv`, GEZIEN): met Vereenvoudigd Chinees 33% 1+ en 12% 5+ spelers, zonder Chinees 19% en **1%**; 9 van de 10 met 20+ hebben Chinees. Het verschil blijft dus ook als Azië slaapt. Een meting op een Amerikaanse avond (±02:00 UTC) doe ik nog als een run daar valt.
2. **Wie maakt het spel.** Veel spellen met Chinees komen van Chinese makers met een eigen publiek thuis (Keyboard Farm, Character House). Chinees toevoegen maakt van ons geen Chinees bedrijf met een Chinees publiek.
3. **Eén moment, één dag.**

**Wat ik er wel uit haal:** een demo met alleen Engels zit in onze hoek bijna altijd op 0 tot 4 spelers (98% onder de 5). Dat is waar Hats nu staat. De demo's die spelers hebben, hebben bijna allemaal meer talen, en Chinees is de taal die het vaakst terugkomt. Dat sluit aan bij Vera (Chinees is het grootst bij 6 van de 13 grote bureaubladspellen) en bij Character House (`character-house.md`).
**Voorstel aan de hoofdchat:** Vereenvoudigd Chinees als eerste extra taal in de demo, daarna Japans; Koreaans als derde als het past. De AI-vertaling valt onder de AI-melding (besluit ligt bij de hoofdchat). Olaf telde ±285 teksten en ±1230 woorden (`platformen/steam/taken.md`); de vertaaltabel komt na de speeltestbuild.

## Wat kost een menselijke vertaling naar Vereenvoudigd Chinees? (Sem, run 9, 16 nov ±19:50 UTC)
Opdracht hoofdchat 20:10 NL: 3 aanbieders met prijs en levertijd, vóór di 17 nov 12:00. **Niets besteld, niemand benaderd.** Thijs: talen ja, Engels plus Vereenvoudigd Chinees door een mens; kosten eerst aan hem.

**Maat:** spel ±1.230 woorden (Olaf, `platformen/steam/taken.md`, alleen wat echt in beeld komt) plus winkeltekst. De winkeltekst van Hats bestaat nog niet; Steam staat voor de korte beschrijving 300 tekens toe (±50 woorden), een gewone "About this game" is 250 tot 400 woorden. Ik reken met **±400 woorden winkeltekst (GOK), samen ±1.630 woorden.**

| Aanbieder | Soort | Prijs (bron) | Voor ±1.630 woorden | Levertijd | Kanttekening |
|---|---|---|---|---|---|
| **Allcorrect** | vertaalbureau alleen voor games (19.000 opdrachten vorig jaar, eigen zeggen) | €0,09 tot €0,12 per woord EN naar Vereenvoudigd Chinees; LQA (testen in het spel) €34 per uur; minimumbedrag bestaat maar zelden nodig (DERDEN, [prijspagina](https://allcorrectgames.com/localization-pricing/), 5 mrt 2026) | **€147 tot €196**, met 2 uur LQA **€215 tot €264** | voorbeeld op hun pagina: winkeltekst van 319 woorden naar 5 talen in 3 werkdagen, 10.000 woorden in 10 werkdagen; voor ons GOK 3 tot 5 werkdagen | prijs alleen op offerte; offerte aanvragen gaat via een formulier met naam en mail, dus stap voor Thijs |
| **Alconost Nitro** | vertaalbureau, zelfbediening met menselijke vertalers (moedertaal) | vanaf $0,10 per woord, geen minimum (DERDEN, [Nitro](https://alconost.com/en/nitro)); hun eigen gemiddelde voor Vereenvoudigd Chinees $0,10 mens, LQA $41 per uur ([kostenblog](https://alconost.com/en/blog/localization-cost)) | **±$163** (±€150 GOK koers), met 2 uur LQA ±$245 | 63% van de opdrachten binnen 2 uur, 96% binnen 24 uur (eigen zeggen) | plakken en betalen, vertaler ziet het spel niet; goed voor de winkeltekst, voor speltekst alleen met een korte uitleg per regel; account aanmaken en betalen is Thijs |
| **Wolfwalker localization** | freelanceteam van 3 Chinese gamevertalers (EN naar Vereenvoudigd Chinees), [site](https://siriuswolf-studio.carrd.co) | geen prijs openbaar; vertaalden o.a. **Outcore: Desktop Adventure** (een bureaubladspel) en meer dan 2 miljoen woorden; markt voor freelancers EN naar ZH **GOK $0,06 tot $0,10** per woord | **GOK $98 tot $163** | niet openbaar; GOK 1 week | enige met een bureaubladspel in de portfolio; vraagt een mail van Thijs |
| LocalizeDirect (ter vergelijking) | gamebureau | woordprijs niet openbaar, minimum €100 per opdracht (DERDEN, [prijzen](https://localizedirect.com/prices)) | onbekend, minstens €100 | onbekend | offerte pas na gratis account |

**Afgevallen, met reden:** buildbench op itch.io ($299 per taal) vertaalt met AI en laat pas bij $1.499 een mens kijken; een itch-aanbod van $8 per 1.000 woorden (2023) en een Taiwanese modder (jan 2026) werken met een AI-stap. Dat botst met "door een mens" en met de open AI-melding. Vrijwilligers die gratis vertalen voor hun portfolio (itch.io, 2025) sla ik over: geen afspraak over levertijd en wijzigingen, en we hebben vóór het fest updates nodig.

**Wat het hele bedrag zou zijn (GOK):** ±€150 tot €265 eenmalig, plus kleine bedragen per update (nieuwe kroniekregels, ±€0,10 per woord). Ter vergelijking: met Chinees had 13% van de bureaubladdemo's 5+ spelers, zonder 3% (boven).

**Mijn advies aan de hoofdchat (Thijs beslist, geld):**
1. **Allcorrect voor de speltekst plus 2 uur LQA.** Waarom: gamebureau met een openbare prijs, en LQA vangt te lange regels in de strook (de kroniek heeft weinig ruimte, Chinese tekens zijn breder). Bovenkant ±€264.
2. Tegelijk een offerte bij **Wolfwalker** vragen; zijn zij goedkoper bij dezelfde levertijd, dan zij (bureaubladspel in hun portfolio).
3. Winkeltekst mag mee in dezelfde opdracht; Nitro alleen als de winkeltekst los en snel moet.
4. **Wanneer:** de vertaaltabel komt na de speeltestbuild (vr 20 nov, Olaf). Demo af vr 18 dec, dus de vertaling moet uiterlijk ±ma 7 dec binnen zijn om nog in het spel te testen (GOK planning). Bestellen ±ma 30 nov geeft een week marge.
5. **Voorwaarde (besluit Thijs 16 nov 21:05):** pas bestellen als de Engelse tekst van Thijs op DEFINITIEF staat in `platformen/steam/teksten-thijs.md`, zowel de tekst in het spel als de winkeltekst. Wat Thijs na de bestelling nog verandert, kost een tweede ronde (GOK ±€0,10 per gewijzigd woord plus minimumtarief). Staat de tekst op ma 30 nov nog niet op DEFINITIEF, dan schuift de bestelling mee; uiterste datum om de demo van 18 dec te halen is ±do 3 dec (levering 2 tot 3 werkdagen bij ±1.630 woorden, GOK op basis van de levertijden hierboven). Haalt Thijs dat niet, dan gaat de demo eerst alleen in het Engels de keuring in en komt Chinees in een demo-update vóór 14 jan.
6. Geef de vertaler een lijst met de 17 heldennamen die onvertaald blijven en de vaste zinnen van de winkelpagina (`teksten-makers.md` regels 6b en 6c), zodat Chinees en Engels hetzelfde beloven.
