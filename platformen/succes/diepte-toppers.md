# Hoe diep zijn de toppers? Prestatie-percentages, voortgang en grind (voor Sanne)

Fenna, 16 nov 2026, ±12:15 tot 13:00 UTC. Opdracht hoofdchat 16 nov 13:10 (spoed, voor `platformen/steam/voortgang.md`, uiterlijk wo 18 nov 09:00). Thijs (13:01): diep spel met level ups, ±100 uur.

## In het kort (voor wie maar 1 minuut heeft)
1. **De meetlat voor ±100 uur bestaat al, en hij is streng.** Twee toppers hebben prestaties voor speeltijd. Desktop Defender: 1 uur 83%, 5 uur 66%, 10 uur 57%, 20 uur 46%, 50 uur 29%, **100 uur 17%**. Rusty's Retirement: 1 uur 84%, 24 uur 44%, 48 uur 25% (GEZIEN, Steam API). Ze lopen bijna gelijk. Dus: **de helft van de spelers is weg rond 15 uur open tijd, 1 op 4 haalt 50 uur, 1 op 6 haalt 100 uur.** Ook in het beste geval ziet maar ±1 op 6 het eind van een voortgang van 100 uur.
2. **Het eerste uur is overvol.** Elk spel heeft 2 tot 9 prestaties die 80% of meer haalt, bijna allemaal in het eerste uur (eerste bewoner, eerste upgrade, eerste baas). 9 tot 14% van de spelers die beginnen, stopt al vóór het eerste uur (Rusty 92,7 naar 83,8; Desktop Defender 96,7 naar 82,9).
3. **De hoofdinhoud van de toppers is op tussen ±20 en ±50 uur.** Daarna houden ze spelers vast met één van drie dingen: een prestige-laag (Desktop Defender: ascend, dan rebirth), een verzameling (Ropuka, Tiny Pasture, Spirit City) of nieuwe kaarten (Rusty's: 5 extra boerderijen). Rusty's kreeg reviews als "at only 22 hours into the game I had already completed it" en "completely done after 3 days".
4. **Grind ontstaat op vijf manieren, telkens dezelfde:** prijzen die harder stijgen dan je inkomen (Ropuka, Tiny Pasture: "2.4 billion coins"), levels die niets nieuws geven (Spirit City "after reaching level 15 or so, there is nothing new"), een eind dat alleen via geluk loopt (Ropuka-loterij, Deskrawl-drops), wachttijden waarvoor je terug moet komen (Rusty's chips, "12 minute cooldown"), en een reset die voelt als overdoen (Desktop Defender rebirth "the biggest time waster ever").
5. **Wat spelers prijzen aan level ups:** dat je verschil ziet ("You definitely see a difference from hour 1 and hour 50"), automatiseren en upgraden van helpers, en verzamelen met hints.

Advies voor Hats staat onderaan.

---

## Bronnen en werkwijze
- **Percentages:** `api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v2/?gameid=<appid>`, met curl, 16 nov 2026 ±12:20 UTC (GEZIEN).
- **Wat je ervoor moet doen:** naam en beschrijving van elke prestatie uit de openbare communitypagina `steamcommunity.com/stats/<appid>/achievements/?l=english` (GEZIEN). Alles samen, 419 prestaties: `platformen/succes/data/diepte-prestaties-2026-11-16.csv` (spel, appid, api-naam, naam, beschrijving, verborgen, procent).
- **Opbouw:** winkeltekst (`store.steampowered.com/api/appdetails`) en de aankondigingen van de makers (nieuws-API van Steam, tot 100 berichten per spel), GEZIEN.
- **Reviews en uren van de schrijvers:** de communitypagina's (`steamcommunity.com/app/<appid>/homecontent/`, meest nuttige Engelse reviews, ±120 positief en ±120 negatief per spel, script `platformen/steam/data/reviews-haal.py`). De API `appreviews` stuurt vanuit onze omgeving door naar de voorpagina (302, GEZIEN), daarom deze weg. Let op: de uren op de communitypagina zijn de **uren nu**, niet op het moment van schrijven, en het zijn de meest nuttige reviews, dus vooral fanatieke spelers.
- Appids: Rusty's Retirement 2666510, Ropuka's Idle Island 3416070, Tiny Pasture 3167550, Deskrawl 4623570, Desktop Defender 3772810, Spirit City: Lofi Sessions 2113850. Extra: **Desktop Detective 4225890** (opvolger van Desktop Defender, 19 aug 2026), omdat de maker daar zelf een doel van 150 tot 200 uur noemt.

### Drie dingen om eerlijk bij te zeggen
1. **Waarover gaat het percentage?** Steam zegt het niet precies op de pagina. De eerste prestatie haalt 92 tot 99% (Spirit City "complete the tutorial" 98,7%), dus het zijn vrijwel zeker de mensen die het spel minstens één keer startten, niet alle kopers (GOK, afgeleid).
2. **"Uren" zijn open tijd.** In deze spellen telt de tijd door als het venster openstaat. Dat is precies wat Sanne bedoelt met open tijd, maar het is geen aandacht.
3. **Een percentage is een momentopname.** Rusty's is 2,5 jaar uit, Desktop Detective 3 maanden. Bij jonge spellen stijgen de lage percentages nog.

---

## 1. Hoe ver komen spelers echt?

### De tijdlijn (de enige echte uurmeters)
| Open tijd | Desktop Defender | Rusty's Retirement |
|---|---|---|
| eerste prestatie | 96,7% (wave 3) | 92,7% (decoratie plaatsen) |
| 1 uur | 82,9% | 83,8% |
| 5 uur | 65,5% | |
| 10 uur | 56,7% | |
| 20 uur | 46,4% | |
| 24 uur | | 43,5% |
| 48 / 50 uur | 28,9% (50 u) | 25,0% (48 u) |
| 100 uur | **16,9%** | |
GEZIEN, Steam API 16 nov. Twee heel verschillende spellen (gevechten met prestige tegenover een rustige boerderij) en toch bijna dezelfde lijn. Daarom gebruik ik die lijn hieronder als grove meetlat om andere prestaties in uren te zetten. **Dat omzetten is een GOK**: het neemt aan dat spelers in elk spel ongeveer even snel afhaken.

| Meetlat (GOK, uit de twee lijnen) | ±85% | ±65% | ±57% | ±45% | ±27% | ±17% |
|---|---|---|---|---|---|---|
| Open tijd | <1 u | 5 u | 10 u | 20 tot 24 u | ±50 u | ±100 u |

### Per spel: wat je doet, hoeveel het haalt, en waar dat op de meetlat valt
**Rusty's Retirement** ($6,99, 71 prestaties, 13.987 reviews; GEZIEN)
| Wat | % | Uur (bron) |
|---|---|---|
| Eerste decoratie / eerste nieuw gewas | 92,7 / 87,6 | <1 u |
| Eerste bewoner (Haiku's huis) | 79,0 | ±1 tot 2 u (GOK) |
| 10 gewassen | 74,9 | ±3 u (GOK) |
| Huizen Sonnet, Echo, Forbic, Pinion (bewoners 2 tot 5) | 70,0 tot 66,7 | ±4 tot 5 u (GOK) |
| Slate, Splunk (bewoners 6 en 7) | 59,6 / 56,9 | ±10 u (GOK) |
| 25 gewassen, 250.000 onderdelen | 49,0 / 52,8 | ±15 u (GOK) |
| Eén van elke robot | 45,0 | ±20 u (GOK) |
| **24 uur gespeeld / eerste extra boerderij (Flower Swamp)** | **43,5 / 42,3** | **24 u (GEZIEN, zelfde spel)** |
| Robots helemaal opgewaardeerd, Reaper (bewoner 8) | 39,5 tot 33,5 | 24 tot 48 u |
| Eerste chip (systeem uit de winterupdate dec 2024) | 33,7 | 24 tot 48 u |
| **48 uur gespeeld** | **25,0** | **48 u (GEZIEN)** |
| Alle gewassen | 20,6 | na 48 u |
| 2e boerderij (Sandy Desert) | 14,8 | ±100 u (GOK) |
| 5e boerderij (Snowy Fields), 10 miljoen onderdelen | 8,5 / 7,7 | ruim na 100 u (GOK) |

**Desktop Defender** ($4,99, 80 prestaties, 1.788 reviews; GEZIEN)
| Wat | % | Uur |
|---|---|---|
| Wave 5, level 3 | 92,8 / 91,7 | <1 u |
| **Eerste ascend (prestige laag 1)** | **82,4** | **±1 u** (zelfde % als "1 uur") |
| Wave 10, level 10 | 77,1 / 69,7 | 2 tot 4 u (GOK) |
| 5 uur gespeeld | 65,5 | 5 u (GEZIEN) |
| 10 uur gespeeld, 5 keer ascend | 56,7 / 55,1 | 10 u (GEZIEN) |
| Level 20, wave 20 | 54,1 / 54,7 | ±10 tot 12 u (GOK) |
| Upgrade tot level 100 | 47,2 | ±18 u (GOK) |
| 20 uur gespeeld | 46,4 | 20 u (GEZIEN) |
| Level 40, 10 keer ascend | 42,2 / 39,5 | ±25 u (GOK) |
| Wave 50, level 100, level 150 | 35,3 / 33,2 / 32,2 | 30 tot 40 u (GOK) |
| 50 uur gespeeld, alle wapens | 28,9 / 28,3 | 50 u (GEZIEN) |
| **Eerste rebirth (prestige laag 2)** | **23,1** | **±60 u (GOK)** |
| Wave 100 | 19,9 | ±80 u (GOK) |
| **100 uur gespeeld** | **16,9** | **100 u (GEZIEN)** |
Een negatieve review (72,9 u): "Game can be completed at around 40ish hours with occasional check-ins." Dat klopt met de tabel: level 150 en alle wapens liggen rond 30 tot 50 uur.

**Desktop Detective** (Conradical Games, $4,99, 111 prestaties, 183 reviews, 3 maanden uit; GEZIEN)
De maker schreef vooraf (aankondiging 24 jul 2026): "we expect it to take about 150 - 200 hours to get to level 100, but the Rebirth system after that can extend playtime into the thousands of hours" (DERDEN, eigen opgave).
| Wat | % |
|---|---|
| Stat naar level 5 / zaak 5 opgelost | 93,7 / 90,2 |
| Eerste ascend | 59,8 |
| Level 10 | 45,2 |
| Level 25 / 50 | 16,5 / 10,8 |
| **Level 100 (het doel van 150 tot 200 uur)** | **8,6** |
| Eerste rebirth / 5 rebirths | 7,4 / 3,6 |
Na 3 maanden haalt 8,6% het einddoel van de hoofdlijn. 76 van de 111 prestaties zitten onder de 20%: de bovenste helft van het spel ziet bijna niemand.

**Spirit City: Lofi Sessions** ($11,99, 34 prestaties, 15.530 reviews; GEZIEN). XP komt vooral van open tijd (plus taken en timers).
| Wat | % | Uur (GOK via meetlat) |
|---|---|---|
| Tutorial / level 2 | 98,7 / 90,8 | <1 u |
| Eerste geest (Goopii) | 83,5 | ±1 u |
| Level 10 | 59,6 | ±8 u |
| Level 20 | 40,6 | ±25 u |
| Level 30 | 26,1 | ±50 u |
| Level 40 | 15,9 | ±100 u |
| Level 50 (max van de prestaties) | 10,5 | ruim na 100 u |
24 geesten om te ontdekken, van 83,5% (eerste) tot 15,2% (Deermuff).

**Tiny Pasture** ($4,07, 55 prestaties, 7.142 reviews; GEZIEN)
| Wat | % |
|---|---|
| Eerste dier volwassen | 94,9 |
| Meer weideplekken / geldbijenkorf | 77,6 / 74,6 |
| 10 dieren volwassen / fokgordijn | 70,8 / 63,1 |
| 50 dieren volwassen | 56,4 |
| Gebouwen op hoogste niveau | 52,9 tot 49,5 |
| 21 weideplekken / eerste regenboogdier | 42,3 / 42,0 |
| Alle kleuren per soort (15 soorten) | 54,5 tot 25,2 |
| Alle kleuren in regenboogkwaliteit per soort | 25,1 tot 12,3 |
| 500 dieren volwassen | 12,3 |

**Ropuka's Idle Island** ($3,99, 31 prestaties, 4.113 reviews; GEZIEN). Geen levels: alleen upgrades voor de kikker en het gras, en een stickerboek ('92 collection, 15 pagina's) dat je vult met gras en een loterij.
| Wat | % |
|---|---|
| Op Ropuka klikken / eerste upgrade | 92,8 / 90,6 |
| Eerste sticker / loterij 1 keer | 80,8 / 78,3 |
| Loterij 5 keer | 67,3 |
| Eerste pagina vol | 50,8 |
| Loterij 50 / 100 keer | 38,1 / 28,8 |
| Andere pagina's vol | 26,9 tot 23,8 (bijna gelijk) |
| Alle hoeden ("Mad Hatter") | 23,1 |
| **Alles verzameld en op max** | **15,1** |
Opvallend: zodra je pagina 2 vol hebt (26,9%), maakt de rest bijna niet meer uit (tot 23,8%). Wie verzamelt, gaat door tot bijna het eind.

**Deskrawl: Idle ARPG** ($4,89, 37 prestaties, 3.638 reviews, 1.0 sinds 28 sep 2026; GEZIEN)
| Wat | % |
|---|---|
| Eerste minibaas / eerste minion | 91,6 / 90,5 |
| Bazen in gebieden 1 tot 9 | 90,0 tot 61,8 |
| Life skills-boom vol | 62,8 |
| **Level 70 (huidige top, was 25 in jun 2026)** | **60,8** |
| Mythic Rift | 51,2 |
| Uitrusting +10 | 27,6 |
| Inferno per klasse (eindbaas van het eindspel) | 24,1 tot 10,1 |
**Deze cijfers passen niet bij de meetlat.** Level 70 bij 60,8% zou ±8 uur zijn, terwijl een review zegt "getting to lvl 98 in Diablo2 is faster than getting to lvl 31". De schrijvers van reviews hebben mediaan 226 uur (positief) en 168 uur (negatief), veel meer dan bij de rest. Twee verklaringen, allebei GOK: Deskrawl houdt een kleinere, fanatieke groep veel langer vast, of de cijfers zijn opgeblazen door spelers die uitrusting farmen voor de Steam-markt (Deskrawl heeft handel op de markt). Gebruik Deskrawl niet als meetlat voor afhaken.

### Uren van de reviewschrijvers (communitypagina, uren nu, GEZIEN)
| Spel | Mediaan positief | Mediaan negatief | Negatief onder 5 u |
|---|---|---|---|
| Ropuka's | 289 u | 45 u | 19 van 117 |
| Deskrawl | 226 u | 168 u | 13 van 118 |
| Spirit City | 216 u | 28 u | 36 van 118 |
| Rusty's | 109 u | 29 u | 24 van 118 |
| Desktop Defender | 101 u | 44 u | 14 van 90 |
| Tiny Pasture | 80 u | 13 u | 30 van 81 |
| Desktop Detective | 48 u | 20 u | 2 van 15 |
Negatieve schrijvers stoppen meestal tussen 13 en 45 uur, precies waar de hoofdinhoud van de toppers op is.

---

## 2. Hoe bouwen ze hun voortgang op?
| Spel | Lagen (van kort naar lang) | Aantal stappen | Prestige? | Wat zeggen reviews over het einde |
|---|---|---|---|---|
| **Rusty's Retirement** | gewassen vrijspelen, bewoners (huizen), robots opwaarderen tot max, chips per gewas, extra boerderijen | 9 bewonershuizen, 25+ gewassen, 7 robotsoorten, 5 extra boerderijen (plus collab-boerderijen, nieuwe save nodig) | Zacht: elke nieuwe boerderij begint opnieuw, tellers lopen "across all farms" door | "at only 22 hours into the game I had already completed it" (35,8 u); "completely done after 3 days" (99,1 u); "After 24h you have kind of seen everything" (83,9 u) |
| **Desktop Defender** | waves, speler-level (nu 215 levels), upgrades tot level 100, wapens (18+), buit, ascend (Ascendium voor blijvende upgrades), rebirth (bonussen tot 100 rebirths), smeden | 3 lagen boven elkaar; record wave 430 (maker, 8 jun 2026) | Ja, twee lagen | "the rebirth mechanic leaves a lot to be desired" (72,9 u); "do not rebirth it is the biggest time waster ever" (150,5 u, positief) |
| **Desktop Detective** | zaken, stats, gereedschap, uitrusting, 14 detectives, 9 plekken, ascend, rebirth, smeden | 100 levels, 300+ zaken | Ja, twee lagen | "re-leveling after rebirthing, just to get back where..." (92,4 u); "I was enjoying the game before I unlocked Rebirth" (281,9 u) |
| **Spirit City** | XP-level (vooral open tijd, ook taken en timers), geesten ontdekken met combinaties en hints, kleren en kamer | level 50, 24 geesten | Nee | "after reaching level 15 or so, there is nothing new you get from collecting XP" (240,5 u); "I'm leaving the game running while AFK to grind the time-based exp bar and get to level 50" (244,5 u) |
| **Tiny Pasture** | dieren kopen en laten groeien, plekken en pakhuizen, gebouwen tot max, fokken, kleuren, regenboogkwaliteit | 15 soorten met elk een kleurenreeks, 2 kwaliteitslagen | Nee | "I did not expect to be 'end game' on day 2" (161 u, positief); "The next one alone costs 2.4 billion coins" (375,1 u, positief) |
| **Ropuka's** | gereedschap en gras opwaarderen, stickerboek van 15 pagina's, loterij | ±15 pagina's, één verzameling | Nee | "the last achievement took over 100+ hours more to get compared to the other achievements" (525,4 u, positief); "Everything becomes more and more expensive and your buying power does not" (26,5 u) |
| **Deskrawl** | level (25 in jun, 70 bij 1.0), 9+ gebieden met minibaas en baas, minions vangen, legendarische uitrusting, runes, life skills, paragon-boom, Mythic Rift, Inferno per klasse, schatkaarten, wereldbaas | 4 klassen, elk een eigen Inferno | Nee (paragon na de top) | "pretty fun until you reach the endgame, where none of the rarest items seem to drop" (1.100 u); "after playing more than 400hrs of the game i only got 2 black mist gear" (461,6 u) |

Wat opvalt:
- **Geen enkele topper heeft alleen levels.** Het is altijd een stapel: iets kleins dat elke paar minuten komt (gewas, wave, upgrade), iets middelgroots dat elk uur of elke paar uur komt (bewoner, wapen, geest, gebied) en iets groots (boerderij, ascend, rebirth, Inferno).
- **Wie langer wil, voegt een laag toe in plaats van meer levels.** Desktop Defender rekte uit met rebirth en schreef zelf (8 jun 2026): "I personally feel that the level bonuses have capped out at this point, with Rebirth bonuses playing a more important role". Deskrawl verhoogde het maximum level van 25 naar 70.
- **Prestige werkt als eerste stap en wordt gehaat als lange klus.** De eerste ascend in Desktop Defender haalt 82% (binnen het eerste uur, het is uitleg); de rebirth haalt 23% en krijgt de klachten.

---

## 3. Wat spelers prijzen aan level ups, en waar het grind wordt

Telling op trefwoorden in ±120 positieve en ±120 negatieve meest nuttige reviews per spel (GEZIEN; grove telling, een review telt als het woord erin staat):
| Spel | "op/klaar" neg | "grind/tedious" neg | "prestige/reset/rebirth" neg |
|---|---|---|---|
| Deskrawl | 33 | 25 | 0 |
| Rusty's | 18 | 10 | 8 |
| Spirit City | 9 | 5 | 5 |
| Desktop Defender | 7 | 8 | **26** |
| Ropuka's | 7 | 8 | 0 |
| Tiny Pasture | 5 | 10 | 0 |

### Wat ze prijzen (zelf gelezen, citaten van hooguit één zin)
- **Verschil zien over tijd:** "You definitely see a difference from hour 1 and hour 50." (Desktop Defender, 275,6 u)
- **Automatiseren en helpers opwaarderen:** "Automating your farm, upgrading bots, and leveling up tools is so addictive it is hard to put down." (Rusty's, 780 u)
- **Een klein moment tussendoor:** "entertaining enough to spend 5 minutes redecorating your island" (Ropuka's, 341,3 u)
- **Verzamelen met hints:** "You get little hints and have to play around with different..." (Spirit City, 176 u)
- **Zelfs het enige minpunt is "op":** "The one and only negative thing about this game is that I ran out of achievements." (Rusty's, 337,3 u)

### Waar het grind wordt (vijf patronen)
1. **Prijs loopt weg van het inkomen.** Ropuka's: "Everything becomes more and more expensive and your buying power does not" (26,5 u). Tiny Pasture: 7,2 miljard goud voor een prestatie (195,1 u). Zelfde patroon als Monster Farm in verhaal 6.
2. **Levels zonder nieuws.** Spirit City: na level ±15 niets nieuws, en mensen laten het spel AFK draaien om level 50 te halen.
3. **Eind via geluk.** Ropuka's laatste stickers alleen via de loterij ("over 100+ hours more"); Deskrawl: zeldzame buit valt niet.
4. **Terugkom-wachttijden.** Rusty's chips: "a 12 minute cooldown no mater if you reroll or buy everything" (183,5 u). Desktop Defender: "would prefer you sink 10+ actions in to it every 5 minutes or so" (242,9 u). Desktop Detective: "You need to babysit this thing constantly" (92,4 u).
5. **Reset die voelt als overdoen.** Desktop Defender 26 keer prestige/reset/rebirth in negatieve reviews, de hoogste van alle spellen; Desktop Detective: "re-leveling after rebirthing, just to get back where" (92,4 u).

En de grootste klacht blijft **op**: Rusty's 22 uur, "3 days"; Desktop Defender "40ish hours"; Tiny Pasture "end game on day 2".

---

## Wat dit betekent voor Hats (advies Fenna, voor Sanne, Bram en Olaf)
1. **Ontwerp voor de lijn, niet voor het eind.** Reken met de meetlat: wat na uur 1 komt ziet ±83%, na uur 10 ±57%, na uur 40 ±30%, na uur 100 ±17% (GOK op basis van twee spellen). Stop de duurste en mooiste dingen (nieuwe bewoners, nieuwe helden, hoeden) in uur 0 tot 20, waar de meeste mensen zijn, en zorg dat er tot ±40 uur elk uur iets nieuws komt. Na 40 uur mag het goedkoper per uur zijn, maar nooit leeg.
2. **Het eerste uur: 4 tot 6 kleine feestjes.** Alle toppers hebben 2 tot 9 prestaties boven 80%. Voor de demo betekent dat: eerste val, eerste bewoner, eerste hoed, eerste level, eerste held met wrok, allemaal binnen 30 tot 60 minuten.
3. **Elk level geeft iets dat je ziet.** Niet zoals Spirit City na level 15. Dit staat al in Sannes opdracht; de cijfers bevestigen het.
4. **Lange termijn: kies een laag die nieuwe inhoud geeft, geen reset.** "Dieper graven naar nieuwe lagen met eigen helden en bewoners" lijkt op de boerderijen van Rusty's (nieuwe kaart, nieuwe gewassen) en ontloopt de klacht over rebirth. Wil Sanne toch prestige: houd het vrijwillig, laat de eerste keer vroeg komen (Desktop Defender: binnen het uur, 82%) en laat elke keer iets nieuws vrijkomen, niet alleen een vermenigvuldiger. Dit is een advies, geen meting.
5. **Vijf verboden die de cijfers geven** (passen bij T1 tot T4): geen prijs die harder stijgt dan het inkomen (Bram kan dat in zijn sim toetsen: verhouding prijs volgende ontgrendeling / goud per uur moet vlak blijven), geen eind via loterij, geen terugkom-timers, geen level zonder iets nieuws, en de laatste prestatie niet 100 uur verder dan de rest (Ropuka's).
6. **Prestaties als meetinstrument.** Geef Hats prestaties voor 1, 5, 10, 20, 50 en 100 uur open tijd, net als Desktop Defender. Dan kunnen we na de lancering precies zien waar spelers afhaken. Kost bijna niets (Steamworks-stats, Olaf).

**Voorstel deze week:** Sanne gebruikt de meetlat-tabel (uur 1, 5, 10, 20, 50, 100 met 83, 66, 57, 46, 29, 17%) als kolom naast haar tabel per uur in `voortgang.md`, zodat bij elk doel staat hoeveel spelers het zien. Bram toetst de verhouding prijs / goud per uur in de sim. Olaf zet de zes tijd-prestaties op de lijst voor Steamworks.
