# Skiff: prijsvoorstel (Chris, 17 nov 2026, run 78)

Prijs is een besluit van de platformmanager (Gijs) na dit voorstel. Labels: GEZIEN, DERDEN, GOK.

**Besluit Gijs, 17 nov ±09:30 UTC: prijspunt $3,00** (koper ziet $2,99 en € 3,49), zoals voorgesteld; Skiff Free blijft gratis (`berichten/chris.md`, `platformen/garmin/status.md`).

## Voorstel
**Skiff: prijspunt USD $3,00 bij Garmin, eenmalig. De koper ziet dat als $2,99 in de VS, € 3,49 in Duitsland en Frankrijk, £ 2,99 in het VK (£ 2,49 is Gibraltar). Skiff Free: gratis, zonder proeftijd of code.**

Dat is wat `platformen/garmin/reeks.md` (de kern, punt 4) al zei. Dit stuk onderbouwt het met een meting en lost een misverstand op.

## Het misverstand over $2,99 (GEZIEN 17 nov ±09:00 UTC)
In `reeks.md` en `proefstand-en-codes-2026-11-16.md` staat "$2,99 bestaat niet, het wordt $3,00". Half waar. De ontwikkelaar kiest een prijspunt in dollars ($2,00, $2,25, ... $3,00), maar de koper ziet een ander bedrag. Op `https://developer.garmin.com/connect-iq/articles/monetization/Price_Points.html` (gelezen met curl):

| Prijspunt (ontwikkelaar) | VS | Duitsland, Frankrijk, Italië, Portugal, Spanje | Gibraltar / VK |
|---|---|---|---|
| $2,00 | $1,99 | € 2,49 | £ 1,69 / £ 1,99 |
| $2,50 | $2,49 | € 2,99 | £ 2,29 / £ 2,49 |
| $2,75 | $2,75 | € 3,29 | £ 2,29 / £ 2,69 |
| **$3,00** | **$2,99** | **€ 3,49** | £ 2,49 / £ 2,99 |
| $5,00 | $4,99 | € 5,99 | (niet overgenomen) |

Daarom staan in de winkel-API wel prijzen als $1,99, $2,49 en $2,99: dat is wat de koper in de VS ziet. Nederland en België staan niet apart in de tabel (GOK: zelfde als de rij voor de euro, dus € 3,49). Garmin houdt 15% in (DERDEN, `proefstand-en-codes-2026-11-16.md`).

## Wat vergelijkbare wijzerplaten vragen (GEZIEN 17 nov ±08:55 UTC)
Zoekbalk van de winkel, alleen wijzerplaten, eerste 60 per woord op "meest relevant": body battery, stress, body battery stress, data rich, big digits, health. 285 verschillende wijzerplaten, waarvan 78 betaald. Script `meet-prijs.py`, cijfers in `data/prijs-2026-11-17.csv`. Prijs = wat de koper in de VS ziet.

| Groep | Aantal betaald | Mediaan | Meest gevraagd |
|---|---|---|---|
| Alle 78 | 78 | $2,49 | $1,99 (29), $2,49 (17), $4,99 (14), $2,99 (11) |
| Gevonden op body battery, stress of health | 48 | $2,49 | $1,99 (15), $2,49 (12), $2,99 (9), $4,99 (9) |
| Met 100+ downloads | 13 | | $1,99 (9), $4,99 (3), $2,75 (1) |

Naar downloads: 0 downloads mediaan $2,99 (15 stuks), 1+ $2,37 (32), 10+ $2,49 (18), 100+ $1,99 (10), 1.000+ $4,99 (2), 10.000+ $4,99 (1).

Wat er achter die getallen zit:
- **De groep van $1,99 met 100+** zijn vooral "Data Rich"-platen van een handvol makers op 177 tot 188 horloges (VoltGrid, StriveGrid, Neon Hex DataGrid, Obsidian Lotus, CyberPanel 85 en meer, 7 van de 13 op 150+ horloges). Hun bereik komt van de lijst horloges en de vele platen, niet van de lage prijs alleen (GOK).
- **De toppers vragen $4,99:** *Fenix 8 - Data Dash GB - PRO* (10.000+), *Fenix 9 CAMO - Rich data* en *ALCHEMIST Data - Tactix 8* (1.000+), allemaal met honderden reviews en een sterke eigen stijl (GEZIEN). Een nieuwe plaat zonder reviews op $4,99 doet het niet vanzelf: *Astra Vital Pro* (Stress en Body Battery, $4,99) staat op 10+ (GEZIEN).
- **Het dichtst bij Skiff:** *Clean Rings: Activity & Body Battery* $1,99 (100+), *Body Battery* $2,49 (10+), *Body Clock* $2,99 (10+), *Daybook* $2,99 (1+, `reeks.md`), Two Suns Pro en DayArc Pro $2,49 (1+, `reeks.md`).

## Waarom $2,99 (prijspunt $3,00) en niet $1,99 of $4,99
1. **Niet $1,99:** daar staan 29 platen die op elkaar lijken. Een lagere prijs maakt ons één van velen, en Skiff heeft juist een eigen beeld (de zee). Het verschil per koper: $2,99 min 15% is ±$2,54, $1,99 ±$1,69, dus 50% meer per koper (rekensom, belasting niet meegenomen; GOK hoeveel minder kopers het kost).
2. **Niet $4,99:** dat vragen platen met honderden reviews. Wij beginnen op 0, en een koper die twijfelt heeft eerst de gratis versie. Over 30 dagen, met reviews, kan omhoog altijd nog (een prijswijziging kost misschien een nieuwe keuring, NIET GEZIEN, zie `proefstand-en-codes-2026-11-16.md` deel 3).
3. **$2,99 is gewoon in onze hoek:** 9 van de 48 op body battery, stress en health vragen het, en de mediaan is $2,49. Wij zitten één stap boven de mediaan met vier thema's en negen velden, wat de meeste daar niet hebben (NIET GEZIEN per plaat; de tabel in `reeks.md` laat het zien voor vijf).
4. **De gratis versie doet het werk:** de betaalde haalt mediaan een tiende van zijn gratis broertje (Joris, verhaal 22, 452 paren, DERDEN `platformen/succes/verhalen-groei.md`). Het bereik komt dus uit Skiff Free, en de prijs van Skiff gaat over wie al overtuigd is. Dan past een prijs boven de bodem.

## Geen proeftijd, geen korting bij de start
- Garmin kent in zijn betaling geen proefstand (GEZIEN, `proefstand-en-codes-2026-11-16.md` deel 1). Skiff Free is de proef, en blijft gratis.
- Een actieprijs (`listPrice` en `salePrice` bestaan in de API) bij de lancering: niet doen. Er is geen bewijs dat het helpt in deze winkel, en het venster "nieuw" (14 dagen) loopt toch al (GOK).

## Wat het oplevert (GOK, eerlijk)
Meetlat uit `reeks.md`: Skiff Free op 1.000 downloads, Skiff op ±een tiende daarvan, dus ±100 kopers. 100 keer $2,54 is ±$254 in totaal, niet per maand. Mediaan voor een betaalde wijzerplaat van een kleine maker in de eerste maanden is ±$25 (Vera, DERDEN `platformen/verkenner/garmin-wijzerplaten-2026-11.md`). Eén plaat haalt de doelen niet; de reeks en een uitschieter moeten het doen.

## Meten na de lancering
Dag 7, 14 en 30: downloads van Skiff en Skiff Free naast elkaar in `cijfers.md` (nog te maken bij de lancering). Is de verhouding betaald tegen gratis op dag 30 onder 1 op 20, dan eerst naar de tekst en de beelden kijken, daarna pas naar de prijs.

## Controleur (agent, run 78)
Zelf opnieuw gemeten: 285 platen, 77 betaald, mediaan $2,49, $1,99 bij 28, 100+ bij 12: gelijk binnen de schommeling van de winkel. Prijstabel van Garmin klopt voor $2,00, $2,50, $2,75, $3,00 en $5,00; rekensom klopt. MOET verwerkt: de twee kolommen bij het VK zijn Gibraltar en het VK, een Britse koper ziet £ 2,99.
