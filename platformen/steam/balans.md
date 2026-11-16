# Het Hol: startgetallen voor de balans (Sanne)

Stand 9 nov 2026, ±19:10 UTC. Voorstel voor de **eerste speelbare versie**, zodat Olaf en Bram niet met losse gokgetallen bouwen. Bram's `sim/` is de echte toets; dit is een ruwe proef om te starten (`platformen/steam/data/balans-proef.py`, vast zaad, speler koopt steeds het goedkoopste). Alle getallen GOK tot Bram's sim en een speelronde ze bevestigen.


## Stand 16 nov ±19:55 UTC: ritme in het gewone spel (Sanne, na Iris keuring 7)
**Vraag:** Iris mat in de duurtest van 20 min (run 43931188663) dat er **62% van de tijd geen held in beeld** is, gaten mediaan 30 s, nooit twee helden tegelijk, en 13% van de tijd geen held terwijl Gloop plat ligt. Zij gaf drie knoppen: (a) helden sneller na elkaar, (b) Gloop korter plat, (c) soms twee helden kort na elkaar. Ik kies met Brams sim, speeltestbuild (graven gratis, upgrades 45/126/353, drempels 3/5/7/12/17), 40 zaden, held ±15 s in beeld. Script: `platformen/steam/data/sim-ritme/ritme.py`.

**Uitkomst (GEZIEN, mediaan over 40 zaden, eerste 20 min):**

| Variant | held in beeld | gat zonder held | geen held + Gloop plat | helden in paar | ergste gat koop/hol min 1-20 | min 1-60 | hol 6 | hol 12 |
|---|---|---|---|---|---|---|---|---|
| nu (35-45 begin, 40-60 later, plat 60) | 33% | 33 s | 20% | 4% | 10,7 | 14,1 | 21 min | 98 min |
| (b) alleen plat 30 | 33% | 32 s | 12% | 4% | 8,4 | 17,5 | 18 | 94 |
| (a) 25-35 altijd | 51% | 15 s | 23% | 2% | 8,1 | 14,0 | 14 | 61 |
| (a) 25-35 + plat 30 | 51% | 15 s | 15% | 2% | 7,4 | 13,5 | 12 | 59 |
| **(a+b+c) 28-38, 15% kans paar (6-10 s), plat 30** | **49%** | **18 s** | **17%** | **16%** | **7,6** | **13,5** | **13** | **58** |
| (a) 25-35 alleen tot min 20, daarna 40-60, plat 30 | 51% | 15 s | 15% | 2% | 7,4 | 22,5 | 12 | 84 |

De sim geeft voor nu 33% in beeld; de echte build mat 38%. De sim zit dus iets aan de lage kant, de verschillen tussen varianten tellen.

**Besluit (Sanne, het ritme is mijn keus):**
1. **Tijd tussen helden 28 tot 38 s** (was 35 tot 45 in het begin en 40 tot 60 daarna), ook na de vaste stappen van BEGIN. De eerste stappen (5-7 s en 18-22 s) en het lied van de bard (8-20 s) blijven.
2. **15% kans dat de volgende held al na 6 tot 10 s komt** (niet tijdens BEGIN, niet als het lied loopt). Dan lopen er twee kort na elkaar: de een ziet de ander in de put vallen, of ze staan samen voor Gloop. Ongeveer elke 3 min een paar. Gemiddeld komt er zo een held per ±30 s.
3. **Gloop 30 s plat** (was 60). Bouncy Gloop houdt zijn factor 2/3, dus 20 s.
4. **Weg-tempo mee: `HELD_ELKE_S` 47,5 naar 30** in `voortgang.gd`, zodat weg nog steeds precies een kwart van spelen is (mijn regel van 14:05). Een nacht levert dus ±1,6 keer zoveel als nu; dat is geen extra, het is hetzelfde kwart van een sneller spel.
5. **Drempels en prijzen blijven** (3/5/7/12/17/25/31/39/53/69/88, 45/126/353). Hogere drempels voor hol 8 tot 12 geprobeerd: dan wordt het ergste gat in uur 1 slechter (15,3 tegen 13,5 min), dus niet.

**Waarom:** (a) is de enige knop die het lege deel echt kleiner maakt (33 naar 49%); (b) alleen helpt niet voor beeld, wel voor de stilte met een platte Gloop, want meer helden betekent ook vaker plat; (c) kost bijna niets en geeft het moment dat Iris mist (twee helden die elkaar iets aandoen). Meer helden is ook meer goud: de kopen vallen op 2, 8, 22, 35, 63 en 90 min in plaats van 3, 12, 37, 57, 106 en 151 (mediaan), en het gat tussen minuut 5 en 20 waar ik om 18:55 geen oplossing voor had wordt ook kleiner (ergste 10,7 naar 7,6 min). Eén knop, twee problemen.

**Wat het kost (eerlijk):**
- Hol 12 (Gloop's Empire) komt rond **58 min** in plaats van 98. In een demo van ±2 uur komt er daarna niets nieuws meer op het bordje. Voor de speeltest van za 21 nov maakt dat niet uit (Thijs speelt het begin en een nacht); voor de demo van 18 dec rekenen we het opnieuw met de v3-economie, daar komen kamertjes en laag 2 bij.
- De winkel van de speeltestbuild is op na ±90 min in plaats van ±150.
- CPU: helden die lopen zijn de dure stukken (Olaf 13 nov: de metingen boven 1 zijn de stukken met helden). GOK: gemiddeld van ±0,55 naar ±0,7 CPU-s per 10 s, nog onder de grens van 1. Olaf meet het met de duurtest.
- "Gloop is flat. Back soon." komt vaker voor (Iris: nu al 5 keer in 20 min). Vraag aan Daan: na de tweede keer een andere regel of geen regel.

**Toets:** Olaf draait na de bouw dezelfde duurtest (20 min, 1920x1080, gewoon spel) en `ritme_meting.py`. Geslaagd als held in beeld **minstens 45%**, langste stuk zonder held en zonder regel **onder 40 s**, gemiddelde CPU **onder 0,8**. Haalt het de CPU niet, dan 32 tot 42 s in plaats van 28 tot 38 (sim: ±44% in beeld).

## Stand 16 nov 18:55 UTC: het gat tussen minuut 5 en 20 in de speeltestbuild (Sanne, na Bram 18:50)
**Vraag:** Bram zegt dat het gat in minuut 5 tot 20 (ergste 10,7 min zonder koop of nieuw hol-niveau) niet met drempels op te lossen is. Lukt het met prijzen, of met drempels voor hol 5 tot 7? Gerekend met Brams sim, zelfde opzet als `sim/samenval.py` deel 3 (graven gratis, 40 zaden). Scripts en aanpak: `platformen/steam/data/sim-prijzen/` (`prijsladder.py`, `zoek.py`, `drempels.py`, `lang.py`).

**Uitkomst (GEZIEN):**
1. **Prijzen helpen bijna niet.** Het gat komt van het inkomen (±6 tot 7 goud per minuut in het begin), niet van de ladder. 45/90/180, 45/75/200, 45 x 1,8 en de rest: ergste gat blijft 10,7 min. Beste van 105 ladders (35/50/x of 40/x/x): 9,3 min, maar dan is de winkel na ±90 min op in plaats van ±150. Niet doen.
2. **Hol 5 en 6 eerder (3/5/7/9/14) maakt minuut 1 tot 20 beter** (ergste 8,2, mediaan 5,5, bijna nooit samen met een koop), **maar schuift het gat naar later**: over minuut 1 tot 40 wordt het ergste gat 15,7 tot 20,5 min (nu 13,4), over 1 tot 60 18,2 tot 20,5 (nu 14,1).

| Reeks hol 2 tot 7 | min 1 tot 20 ergste / mediaan | min 1 tot 40 | min 1 tot 60 |
|---|---|---|---|
| **nu 3/5/7/12/17/25** | 10,7 / 6,1 | 13,4 / 9,1 | 14,1 / 11,2 |
| 3/5/7/9/14/25 | 8,2 / 5,5 | 20,5 / 13,1 | 20,5 / 13,3 |
| 3/5/7/9/14/21 | 8,2 / 5,5 | 15,7 / 10,8 | 18,2 / 12,0 |

**Besluit: 3/5/7/12/17 blijft (Olafs keus), prijzen blijven 45/126/353 voor de speeltest.** Waarom: de build heeft in het eerste uur gewoon te weinig dingen om te krijgen; met getallen schuif je het gat alleen heen en weer, en het eerste uur als geheel is nu het best. Wat het echt oplost is de v3-economie (kamertjes en dingen met een prijs van ±1 uur goud, daar is het ergste gat 8,4 min), en dat komt na de speeltest.

**Wat dit gat niet meet:** de vrije momenten die geen koop zijn (eerste wrok rond 63 tot 75 s, het lied van de bard, een nieuwe bladzijde in het heldenboek, hoeden op de toren). Of minuut 5 tot 20 saai voelt, zegt dus niet deze tabel maar (a) Olafs `e2e/ritme_meting.py` op de Windows-duurtest (langste stuk zonder held en zonder kroniekregel) en (b) Thijs zelf bij vraag 1 van de speeltest ("wanneer verveelde je je"). Zegt hij "rond minuut 10", dan is dit de oorzaak en is de eerste fix na de speeltest een ding van ±60 goud dat je rond minuut 8 tot 12 kunt kopen (het eerste kamertje uit v3), geen nieuwe drempels.

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
