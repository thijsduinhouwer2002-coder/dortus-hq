# Het Hol: startgetallen voor de balans (Sanne)

Stand 9 nov 2026, ±19:10 UTC. Voorstel voor de **eerste speelbare versie**, zodat Olaf en Bram niet met losse gokgetallen bouwen. Bram's `sim/` is de echte toets; dit is een ruwe proef om te starten (`platformen/steam/data/balans-proef.py`, vast zaad, speler koopt steeds het goedkoopste). Alle getallen GOK tot Bram's sim en een speelronde ze bevestigen.

## Stand 10 nov 03:05 UTC: heldensoorten, elke soort een eigen zwakte (Sanne, antwoord op Bram 02:30)
**Probleem met de eerste getallen (Bram, GOK):** drie van de vier soorten zijn zwakker tegen Gloop en sterker tegen de put, de ridder is overal gewoon. Dan is het antwoord op elke soort "meer Gloop", en voegen de soorten geen keuze toe (gat 1 uit `toppers.md`). Gemeten met Brams sim (`data/soorten-keuze.py`, 8 zaden, 10 uur, GEZIEN): de put vangt bij elke soort minder dan bij een gewone held, ook bij de ridder (25% put tegen 39% slijm).

**Besluit:** de ridder wordt de held van de put: **ridder slijm 0,7, put 1,4** (zwaar harnas: hij past niet in Gloops mond, maar zakt wel door elke vloer), **bard 1,1 en 1,1** (zwak overal, iets minder dan 1,15 zodat hij nog weleens ontsnapt en zingt). Dief (slijm 1,15, put 0,5), magiër (1,25, 0,3), taai, snelheid en de wegingen (55, 15, 15, 10, 5) blijven zoals Bram ze zette.

**Uitkomst (GEZIEN, zelfde sim):**
| Soort | Bram: slijm / put / vlucht | Besluit: slijm / put / vlucht |
|---|---|---|
| gewoon | 41 / 23 / 36% | 42 / 23 / 35% |
| ridder | 39 / 25 / 36% | **32 / 36 / 32%** |
| dief | 48 / 14 / 39% | 49 / 12 / 39% |
| magiër | 52 / 9 / 39% | 53 / 10 / 37% |
| bard | 51 / 22 / 26% | 48 / 24 / 28% |
| alles | vluchten 36,2% | vluchten 35,1% (doel ±1 op 3 gehaald) |

**Waarom zo:** nu loont het om de put te upgraden als er veel ridders komen, en Gloop als het dieven en magiërs zijn. Dat is een keuze die je in een bezoek kunt maken en die je terugziet in de kroniek. Het Heldenboek kan per soort "Weak to: Spike Pit" laten zien zodra je hem een keer zo ving (versie 1). Met meer vallen in versie 1 (rolsteen, lijmplaat) krijgen dief en magiër elk hun eigen zwakte; dan stel ik dit opnieuw bij.

**Voor Bram:** `heldensoort.gd` DATA en `sim.py` SOORT_DATA naar deze getallen, en de uitleg van de ridder wordt "Heavy armor. Too big for Gloop. Pits love him." (eerlijk: zegt wat de getallen doen). Reken `python3 sim.py soorten` na. **Rekenscript gerepareerd:** `data/ritme-bezoeker.py` zet nu `UPG_BASIS` en `GRAAF_DREMPEL` in plaats van tekst te vervangen (moet-punt controleur 01:50); de tabel hieronder blijft kloppen (GEZIEN, opnieuw gedraaid: 16/21/49, 25/26/28 en 40/41/42 min, alles na 7,0 tot 7,8 u). Alleen "upgrade 45 zonder toeslag" wordt 5,6 tot 6,8 u (stond er al zo).

## Stand 10 nov 01:50 UTC: ritme van de eerste upgrade (Sanne, antwoord op Bram 01:40)
**Besluit:** (1) **upgrade stap 1 kost 45** (stappen 45, 126, 353; `45 x 2,8^n`), (2) **graven kost 5 + 1,2 x gangen, plus 3 per gang boven de 12** (heb je 13 gangen, dan kost de volgende 24 in plaats van 21; bij 20 gangen 53 in plaats van 29; de laatste, bij 39 gangen, 133 in plaats van 52; afgerond op hele munten), (3) **het muntje boven Gloop of de put blijft staan zolang je die upgrade kunt betalen, ook als graven goedkoper is.** Graven blijft een klik op aarde (geen regel op het kaartje). De demo houdt zijn 66 goud aan het begin: dan kan hij Big Gloop rond 20 s kopen en houdt hij 21 over voor de rest van de minuut.

**Waarom:** Brams sim koopt na elke held meteen het goedkoopste. Een echte speler kijkt eens per zoveel minuten (T1) en ziet dan het muntje. Ik rekende dat na met Brams sim en mijn eigen bezoekersmodel (`data/ritme-bezoeker.py`: zelfde regels, alleen het kopen anders: eerste 10 min ongeveer elke minuut kijken, daarna elke 5, 15 of 30 min, steeds bij de eerste held na dat moment; kan een upgrade, dan eerst die). Uitkomsten GEZIEN in die sim met 20 zaden; hoe spelers echt kijken is een GOK. Eerste upgrade (min/mediaan/max):
| Speler | upgrade 60, graven zonder toeslag | upgrade 45 + toeslag graven |
|---|---|---|
| koopt steeds het goedkoopste (Brams sim) | 136 / 154 / 170 min | 50 / 61 / 72 min (`data/ritme-varianten.py`) |
| kijkt elke 5 min, muntje eerst | 28 / 48 / 87 min | 16 / 21 / 49 min |
| kijkt elke 15 min, muntje eerst | 25 / 26 / 43 min | 25 / 26 / 28 min |
| kijkt elke 30 min, muntje eerst | 40 / 41 / 42 min | 40 / 41 / 42 min |

Het muntje doet het meeste werk: wie maar af en toe kijkt, heeft het goud al bij elkaar en koopt de upgrade bij het eerste bezoek. De 45 helpt wie vaak kijkt en dus steeds graaft. De toeslag op graven heeft een andere reden: bij Brams speler staat het hol nu na 1 uur op 20 tot 24 gangen en is alles na 5,9 tot 6,6 uur gekocht; met het besluit 18 tot 19 gangen na 1 uur (bezoekers 11 tot 18) en alles na 7,0 tot 7,8 uur (doel was ±7). Het hol groeit dan over dagen, niet in een middag (T2: elke week groter). Upgrade 45 zonder toeslag zou alles al na 5,6 tot 6,8 uur laten zijn.

**Wat het verandert en wat niet:**
- Vluchten blijft 33 tot 39% (was 31 tot 38%; alleen gemeten bij Brams speler, `ritme-varianten.py`).
- Aankopen in uur 1: bezoekers 8 tot 14 (was met 60 en het muntje 6 tot 17). Wie vaak kijkt koopt iets minder, want graven wordt duurder; wie elke 30 min kijkt iets meer.
- **Het langste gat zonder aankoop in uur 1 wordt groter:** bij Brams speler 6,7 tot 16,5 min (was 5,5 tot 13,4). Dat accepteer ik: in dat gat spaar je naar iets dat je ziet (Big Gloop), en het muntje laat zien wanneer het kan. Bram: reken je doel "langste wacht" na met de nieuwe getallen; komt het boven 20 min, dan zakt de toeslag naar 2.
- Graven kost in het spel nog geen goud (Olaf 01:50: komt voor het Fest); dit is het getal waarmee dat gebouwd wordt. Bram: `BASIS` in `upgrades.gd` naar 45 en beide in `sim.py`.

## Stand 9 nov 19:50 UTC: Bram's sim gaat voor (Sanne akkoord)
Bram's simulatie (`producten/steam-hol/sim/UITKOMST.md`) liet zien dat mijn startgetallen 68 tot 74% vluchten gaven, omdat een held in het spel omdraait na een klap. Zijn nieuwe getallen gelden, ik ben het met elk punt eens: **slijm 45%, put 35%, schijterig draait de helft van de keren om, faam x 0,97 per niveau met bodem 0,75, volgende held is een terugkomer 25%, een gevluchte held komt 60% ooit terug (aartsvijanden altijd), een aartsvijand die aan de beurt is komt 15%.** Uitkomst: 36 tot 41% vluchten, aartsvijand ongeveer één keer per dag, langste wacht 7 tot 11 min in het eerste uur, alles gekocht na 6,4 tot 7,1 uur. Kosten en goud hieronder blijven.

Drie dingen die ik er nog bij zie:
1. **Goud per val:** de tabel zegt 6 bij de start, `strook.gd` regel 180 geeft `3 + 2 x bezoeken` (film: +3 per val). Het idee van Olaf is goed: een terugkomer is meer waard, dus een held met een wrok is een beloning en geen last. Voorstel: **6 x faam-factor + 3 per eerder bezoek** (een aartsvijand na drie vluchten is dan 15 waard). De sim rekent met 6; met 3 duurt de eerste aankoop twee keer zo lang. Bram, wil je de 3 per bezoek in de sim zetten? Olaf beslist.
2. **De helden die "met pensioen" gaan** (40% van wie vlucht komt nooit terug) zijn een kans voor een kroniekregel bij openen ("Pim the Once-Fled retired. Opened a bakery."), geen straf. Staat in `kroniek-regels.md` als ik er tijd voor heb.
3. **Hoard-Toucher 3 tot 6%** is weinig voor een van onze beste grappen. Goed zo voor de balans, maar in de film van een minuut moet hij één keer te zien zijn (demo mag dat sturen, zoals `moet_vallen`).

## Getallen (startvoorstel 19:10; kansen en faam vervangen door de stand hierboven)
| Wat | Waarde |
|---|---|
| Held komt binnen | elke ±50 s (past bij `strook.gd` 25 tot 70 s en `voortgang.gd` 47,5 s) |
| Kans dat een held valt per verdediging op zijn pad | slijm 30%, stekelput 22%, +7 procentpunt per upgrade |
| Helden worden sterker met faam | elke 60 helden één faamniveau: kans per verdediging × 0,9, goud per val +10% |
| Goud per gevallen held | 6 × (1 + 0,1 × faam) × (1 + gangen / 40) |
| Graven, één cel | 5 + 1,2 × aantal gangcellen (start met 6 cellen, dus de eerste kost 12; max 40 cellen); vanaf 10 nov plus 3 per gang boven de 12 (zie boven) |
| Extra slijm of put | je begint met één van elk; extra kost 104, 270, 703 (40 × 2,6^aantal; max 4 van elk; de tweede pas bij 8 gangcellen, de derde bij 16, de vierde bij 24) |
| Upgrade per bewoner of val | 60, 168, 470 (× 2,8; drie per soort); vanaf 10 nov 45, 126, 353 (zie boven) |
| Weghalen of dichtgooien | volle prijs terug |
| **De eerste held van een nieuw spel** | valt altijd (een schijterige held die in de put struikelt), zodat je in de eerste minuut goud ziet (toets 1 in `spelgevoel.md`) |

## Wat de proef laat zien (GEZIEN, één zaad; drie andere zaden in haakjes)
- Eerste aankoop na 100 s (150 tot 200 s).
- Eerste uur: 13 aankopen, nooit langer dan 7 minuten wachten. Dat is "bij elk bezoek iets te kopen" (T1).
- Tot 3 uur: 32 aankopen, langste wachttijd 13 min; tot 6 uur: 44, langste 25 min. Geen muur: de wachttijd groeit langzaam.
- Alles van de eerste versie gekocht na ±7 uur open tijd (6,9 tot 7,9). Voor een prototype genoeg; versie 1 moet hier ±40 uur van maken (`features.md`).
- Vluchten: 36% (38 tot 43%). Doel was ongeveer 1 op 3, dus er blijven genoeg helden met een wrok over voor verhalen.

## Wat dit niet meet
De wrok (een held met wrok loopt naar zijn vijand en is daar misschien sterker of zwakker), aartsvijanden, de Hoard-Toucher, en het plafond van 12 uur terwijl je weg bent. Dat hoort in Bram's sim. Ook niet: of het **voelt** goed. Dat toets ik op de volgende GIF en, als die er is, op een echte speelronde.
