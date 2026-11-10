# Balans-simulatie Het Hol: uitkomst (Bram, 9 nov 2026)

`sim.py` speelt het spel na met dezelfde regels als `godot/systemen/held.gd` (wrok kiest het doel, roekeloos tegen je vijand, Hoard-Toucher brutaler, slijm 60 s plat, eerste held valt) en de kosten en het goud van `platformen/steam/balans.md` (Sanne). De speler koopt steeds het goedkoopste. Draaien: `python3 sim.py 10 8` (10 uur open tijd, 8 zaden). Uitvoer van deze stand: `uitkomst-10u.txt`.

## Wat er met de startgetallen gebeurde (GEZIEN, 5 zaden, 10 uur)
Met slijm 30%, put 22%, faam x 0,9 per niveau en elke terugkomer 50% kans: **68 tot 74% van de helden vluchtte** en er kwam **8 tot 10 keer per uur een aartsvijand** langs. Twee oorzaken: (1) in het spel draait een held om na een klap, dus hij komt de verdediging verderop vaak niet tegen (de proef van Sanne liet iedereen langs alles lopen); (2) faam x 0,9 zonder bodem maakt na ±10 uur elke verdediging 3 keer zwakker, en wie vlucht komt altijd terug, dus de stapel terugkomers groeit.

## Besluit Bram (sim mag de startgetallen overrulen, Sanne 19:10)
| Wat | Was | Nu | Waarom |
|---|---|---|---|
| Kans slijm / put | 30% / 22% | **45% / 35%** | dan vlucht ±1 op 3 (doel features.md) |
| Schijterig draait om na een klap | altijd | **de helft van de keren** | anders loopt bijna niemand langs de tweede verdediging |
| Faam | x 0,9 per niveau | **x 0,97, bodem 0,75** | helden worden langzaam sterker, maar je verdediging wordt nooit nutteloos |
| Volgende held is een terugkomer | 50% | **25%** | meer nieuwe namen, terugkomers blijven bijzonder |
| Gevluchte held komt ooit terug | altijd | **60%** (aartsvijanden altijd) | de rest gaat met pensioen (kan een kroniekregel worden, geen straf) |
| Aartsvijand aan de beurt komt echt | altijd | **15%** | zeldzaam, dus een feest als hij komt |

## Uitkomst met de nieuwe getallen (GEZIEN, 8 zaden, 10 uur open tijd)
- Eerste held valt na 4 s (moet_vallen): goud in de eerste minuut. **Doel gehaald.**
- Vluchten **36 tot 41%**, Hoard-Toucher 3 tot 6%. **Doel ±1 op 3 gehaald.** In `held.gd` zelf (toets, 1 slijm en 1 put): 38%.
- Aankopen: 14 tot 17 in het eerste uur, 34 tot 38 na 3 uur, alles van de eerste versie gekocht na **6,4 tot 7,1 uur**.
- Langste wachttijd tot de volgende aankoop: 7 tot 11 min in het eerste uur, 9 tot 14 min tot 3 uur, 42 tot 49 min tot 10 uur (dat is na "alles gekocht": dan valt er niets meer te kopen). **Onder het plafond van 2 uur.**
- Aartsvijand: **0,2 tot 0,8 per uur**, dus bij 2 tot 3 uur open per dag ongeveer één keer per dag. **Doel gehaald.**
- 41 tot 55 wrokken afgerekend in 10 uur ("Grudge settled").

## Wat dit niet meet
- Of het **voelt** goed: dat toetst Sanne op de GIF.
- Voortgang terwijl je weg bent (`voortgang.gd`): rekent nog met eigen kansen (0,15 + 0,12 per val + 0,10 per bewoner). Volgende stap: dezelfde kansen als hier gebruiken.
- Versie 1 moet ±40 uur inhoud hebben; met deze winkel is alles na ±7 uur op. Dat is inhoud (Sanne), niet balans.
- Volgorde van de verdediging in de gang: de sim zet slijm en put om en om.

## Goud per val: +3 per eerder bezoek (Bram, 9 nov 20:20 UTC, vraag Sanne 19:55)
Regel nu in `sim.py`: **6 x (1 + 0,1 x faam) x (1 + gangen / 40) + 3 per eerder bezoek** (`GOUD_PER_BEZOEK`, derde getal op de opdrachtregel; `python3 sim.py 10 8 0` = zonder bonus). Nieuwe kolom: tijd tot de eerste aankoop. Uitvoer: `uitkomst-10u.txt`.
- **Eerste aankoop: 45 tot 193 s, gemiddeld 104 s** (GEZIEN, 8 zaden). De bonus verandert dit niet: de eerste aankoop komt voor er een terugkomer valt. Dus binnen het doel van Sanne (rond 100 tot 200 s), met één snelle uitschieter (45 s). Met 3 in plaats van 6 per val zou het ±2 keer zo lang duren.
- Met de bonus: aankopen 15 tot 18 in het eerste uur (was 14 tot 17), alles gekocht na 5,9 tot 6,7 uur (was 6,4 tot 7,1), langste wacht 5,5 tot 13,2 min in het eerste uur en 11 tot 18 min tot 3 uur. Vluchten 34 tot 38%, aartsvijand 0,1 tot 1,0 per uur. **Alle doelen blijven gehaald**; de winkel is alleen iets eerder op (inhoud, Sanne).
- Een aartsvijand die na drie vluchten valt brengt 6 x ... + 9 op (Sanne rekende 15 met bezoek 3: dat klopt als het bezoek telt waarop hij valt; de sim telt eerdere bezoeken, dus vluchten).

## Hoedentoren: teller `hap_slijm` (Bram, 9 nov 21:20 UTC, vraag Sanne toets 3 punt 4)
`sim.py` telt nu elke hap van een slijm (`hap_slijm`) en de tijden van de hoeden van Gloop zelf (de eerste slijm; elke slijm heeft zijn eigen toren). GEZIEN met `python3 sim.py 1 8` en `python3 sim.py 40 4` (open tijd, dus speeltijd plus wat voortgang meetelt):
- Eerste uur: Gloop eet 13 tot 27 helden (gemiddeld 22), dus Sanne's 13 tot 28 klopt. Vier hoeden op zijn hoofd na 2 tot 18 minuten.
- Daarna ±27 per uur voor Gloop (±30 voor alle slijmen samen, omdat je er een bij koopt).
- Maten van de hoedenberg voor Gloop: 5 na 0,1 tot 0,3 u, 25 na 1,0 tot 1,5 u, 100 na 3,8 tot 4,9 u, 300 na 10,7 tot 12,3 u, 1000 na 37 tot 38 u.
- Betekenis: wie de strook een werkdag (8 u) open heeft, ziet maat 100 op dag 1, maat 300 op dag 2 en maat 1000 rond dag 5. Groei over dagen, zoals Sanne wil, maar na een week is de berg af. Voorstel aan Sanne: een zesde maat bij 3000 (±2 weken werkdagen), of de hoeden van de hoedenberg in het Heldenboek tellen zodat er daarna nog iets groeit.

**9 nov 22:30 UTC, zesde maat (Sanne 21:50):** `BERG_MAAT` is nu 5, 25, 100, 300, 1000, 3000. GEZIEN met `python3 sim.py 150 5`: maat 3000 voor Gloop na 109,5 tot 114 u open tijd (maat 1000 na 37 tot 38 u). Met een werkdag van 8 u per dag is dat rond dag 14, zoals Sanne rekende. Maat 6 wordt breder, niet hoger: 33 hoeden zichtbaar in hooguit 6 rijen (maat 5: 21 in 6 rijen).

## 10 nov 00:30 UTC (Bram): upgrades met hun eigen effect
`sim.py` rekent nu ook wat stap 2 van elke upgrade doet (`godot/systemen/upgrades.gd`): Bouncy Gloop ligt 2/3 van de tijd plat (40 s), Deep Pit laat een schijterige held na zijn eerste klap van de put niet omkeren. Uitkomst (GEZIEN, 8 zaden, `uitkomst-10u.txt`): vluchten blijft 34 tot 39%, eerste aankoop gelijk (45 tot 193 s), aankopen per uur gelijk, Gloop eet iets meer (±30 per uur in plaats van ±27, hoed 300 na ±10 u). Langste wacht tot 10 u 38 tot 49 min (dat is na "alles gekocht"). Alle doelen blijven gehaald; de stappen maken het spel niet te makkelijk.

## 10 nov 01:35 UTC (Bram): ritme van de eerste upgrade (Sanne, features.md feature 5, "GOK, na te meten in Brams sim")
Nieuw: `python3 sim.py ritme` (20 zaden). Twee spelers: "spaar" koopt alleen upgrades en graaft nooit (Sannes "als je niet graaft"), "goedkoopst" koopt steeds het goedkoopste (zoals tot nu toe). GEZIEN:
- **Spaar: eerste upgrade (60) na 7,3 / 11,1 / 15,6 min open tijd** (min, mediaan, max). Sannes gok van ±10 min klopt.
- **Goedkoopst: geen enkele upgrade in de eerste 2 uur.** Graven kost 5 + 1,2 x gangen en blijft tot 40 gangen onder de 60, dus wie steeds het goedkoopste pakt graaft eerst het hele hol vol. In het eerste uur is er dan wel elke 5,5 tot 13,4 min iets te kopen.
- Spaar heeft in het eerste uur een gat van 10,6 tot 34,8 min zonder iets te kopen (de tweede stap kost 168).
- **Betekenis voor het kaartje:** de keuze is echt (graven of sparen), en dat is goed, maar een speler die het goedkoopste kiest, ziet de upgrades pas na uren. Het muntje boven Gloop (Sanne) helpt alleen als hij spaart. Voorstel aan Sanne: het muntje ook laten zien als de speler 60 heeft en het graven hem er weer onder zou brengen, of graven per gang duurder vanaf ±12 gangen. Dat is haar keuze (balans.md); de sim kan beide doorrekenen.
- **Fout gevonden en hersteld:** Deep Pit telde in de sim nooit mee (de put heet in `sim.py` "put", de regel keek naar "stekelput"). Na herstel (8 zaden, `uitkomst-10u.txt`): vluchten 33 tot 38%, aankopen per uur gelijk, alle doelen blijven gehaald. De uitspraak van 00:30 hierboven ("Deep Pit gerekend") klopte dus niet; nu wel.

## 10 nov 02:15 UTC (Bram): upgrade 45, 126, 353 en graven +3 per gang boven de 12 (Sanne 01:50, balans.md)
Sinds nu rekenen `sim.py` (`UPG_BASIS`, `graaf_prijs()`) en `godot/systemen/upgrades.gd` (`BASIS`) met Sannes nieuwe getallen; de metingen van 01:35 hierboven (60, 168, 470) zijn daarmee oud. Uitkomst (GEZIEN, 8 zaden, 10 uur, `uitkomst-10u.txt`):
- Eerste val na 4 s, vluchten 33 tot 39%, aartsvijand 0,1 tot 0,9 per uur, Hoard-Toucher 4 tot 6%. **Doelen gehaald.**
- Eerste aankoop gelijk (45 tot 193 s): dat is graven onder de 12 gangen, daar veranderde niets. Niet omdat de sim niet opnieuw draaide.
- Aankopen 12 tot 15 in het eerste uur (was 15 tot 18), alles gekocht na **7,1 tot 7,6 uur** (was 5,9 tot 6,7). Langste wacht: 6,7 tot 15,0 min in uur 1, 11 tot 16 min tot 3 uur. **Ver onder het plafond van 2 uur.**
- Ritme (`python3 sim.py ritme`, 20 zaden): **spaar** eerste upgrade na 5,1 / 9,3 / 13,3 min (was 7,3 / 11,1 / 15,6), langste gat in uur 1 16,6 tot 33,2 min; **goedkoopst** eerste upgrade na 50 / 61 / 72 min (was: nooit in 2 uur), langste gat in uur 1 6,7 tot 16,5 min. De toeslag op graven doet dus wat Sanne wilde: ook wie het goedkoopste koopt ziet binnen ±een uur zijn eerste upgrade.
- Gloop eet ±29 tot 31 helden per uur; hoedenberg 100 na 2,9 tot 4,4 u, 300 na ±10 u.

## 10 nov 02:20 UTC (Bram): heldensoorten (versie 1), `python3 sim.py soorten`
Ridder, dief, magiër en bard uit `features.md` (versie 1) als systeem in `godot/systemen/heldensoort.gd`, zelfde getallen in `sim.py` (`SOORTEN`, standaard uit, dus de tabel hierboven verandert niet: nagekeken, uitvoer gelijk). Na de eerste 10 helden: 55% gewoon, 15% ridder, 15% dief, 10% magiër, 5% bard. Een bard die ontsnapt zingt, dan komen er 2 helden snel achter elkaar (8 tot 20 s).
Uitkomst (GEZIEN, 8 zaden, 10 uur), zonder / met soorten:
- vluchten 33 tot 39% / **35 tot 39%** (doel ±1 op 3 blijft), helden per uur 71 tot 73 / 72 tot 75, alles gekocht na 7,1 tot 7,6 / 7,0 tot 7,6 u. (Na de controleur: de soortfactor geldt net als in held.gd alleen op de basiskans, niet op upgrade en ROEKELOOS.)
- langste wacht in uur 1: 6,7 tot 15,0 / 7,0 tot 19,8 min (ver onder 2 uur), aartsvijand 0,1 tot 0,9 / 0,2 tot 0,8 per uur, liederen 0,5 tot 1,6 per uur (een bard die zingt is dus ongeveer eens per uur een gebeurtenis).
- In `toets_held.gd` (120 helden per soort, 1 slijm en 1 put): magiër valt 2 keer in de put tegen 18 voor een gewone held, dief 8, ridder komt vaker tot de put (25, hij is taai) en loopt 19 s tegen 13 s; vluchten per soort 32 tot 44%. Getallen zijn een GOK, Sanne mag ze bijstellen.
- **02:30 UTC, karaktertrekken erbij** (versie 1): slaapkop (dutje van 4 s halverwege), wraakzuchtig (dubbel roekeloos tegen zijn vijand), opschepper (langzamer, pocht), na held 10 en dan 1 op 5 (`heldensoort.kies_trek`). In `sim.py soorten` mee: vluchten 34 tot 40%, langste wacht uur 1 6,6 tot 12,4 min, aartsvijand 0,3 tot 1,4 per uur. Doelen blijven gehaald. Toets: wraakzuchtig valt 41 van 150 keer in zijn eigen vijand tegen 27 voor een gewone held. "Verdwaald" uit features.md komt later: in één rij gangen zie je "de verkeerde gang" nog niet.

## 10 nov 03:20 UTC (Bram): ridder en bard volgens Sanne (balans.md 03:05)
Ridder slijm 0,7 en put 1,4 (held van de put), bard 1,1 en 1,1; zelfde getallen in `godot/systemen/heldensoort.gd`. `python3 sim.py soorten` (8 zaden, 10 uur, GEZIEN), zonder / met soorten: vluchten 32,9 tot 39,0% / **31,5 tot 40,6%** (doel ±1 op 3 blijft), helden per uur 71 tot 73 / 72 tot 76, langste wacht uur 1 6,7 tot 15,0 / 6,6 tot 9,3 min, alles gekocht na 7,1 tot 7,6 / 7,0 tot 7,9 u, aartsvijand 0,1 tot 0,9 / 0,4 tot 1,1 per uur, liederen 0,6 tot 1,7 per uur. Per soort zie Sannes tabel in balans.md (ridder 32 / 36 / 32%: de put vangt hem nu vaker dan Gloop).

## 10 nov 03:35 UTC (Bram): Trick Lid tegen de magiër (idee Sanne, features.md 03:10)
Trick Lid (stap 3 van de put) ziet eruit als vloer, dus de magiër ziet hem niet: factor put 0,3 wordt 1,0 (`heldensoort.VERBORGEN_X`, `sim.py TRICK_MAGIER`). Gemeten met een teller per soort (8 zaden, 10 uur, GEZIEN), alleen helden die kwamen terwijl Trick Lid er lag: magiër in de put **10,6% wordt 19,3%**, magiër Gloop 61,5 wordt 58,5%, magiër vlucht 27,9 wordt 22,2%. Gewone held en ridder gelijk (binnen ruis). Alle helden: vluchten 35,1 wordt 34,8%. `sim.py soorten`: vluchten 31,5 tot 40,7%, langste wacht uur 1 6,6 tot 9,3 min, alles gekocht na 7,0 tot 7,9 u. Doelen blijven gehaald. Klein effect op het geheel, wel een echte tegenzet die je in het Heldenboek kunt teruglezen.

## 10 nov 03:50 UTC (Bram): hoe snel vult het Heldenboek (Sanne features.md 03:10, "Bram meet na")
`python3 boek_meting.py` (sim met heldensoorten, 8 zaden, 140 uur, speler koopt het goedkoopste, GEZIEN), uren open tijd min / mediaan / max:
- hoofdstuk 1 vol (5 soorten x 3 stempels): 1,0 / 1,8 / 3,0 u; de laatste stempel is meestal de magiër in de put (0,2 / 1,8 / 3,0 u).
- alle 10 hoeden (als elke held een willekeurige hoed draagt): 0,6 / 1,1 / 1,9 u.
- hoedenberg 1000: 31 / 32 / 33 u, 3000: 93 / 94 / 96 u (Sanne rekende 110 u; Gloop eet nu iets meer door upgrades en soorten). 10.000 komt pas na ±300 u.
Dus: hoofdstuk 1 en de hoeden zijn op dag 1 klaar (zoals Sanne verwachtte), de bergstempels bij een werkdag open op dag ±4 en ±12, de aartsvijanden lopen altijd door. Karakters (hoofdstuk 2) zitten niet in de sim; de trekken komen na held 10 met 1 op 5, dus ook dag 1.

## Eerste aartsvijand (Bram, 10 nov 04:20 UTC, `python3 sim.py aarts`, 60 zaden, 6 u, GEZIEN)
Sanne vraagt in `features.md` (eerste tien minuten): geen aartsvijand in het eerste uur van een nieuw spel.
| regel | met soorten | aartsvijand in uur 1 | vroegste | mediaan eerste | binnen 6 u |
|---|---|---|---|---|---|
| geen regel (nu in strook.gd) | nee | 12 van 60 (20%) | 0,18 u | 1,82 u | 54 |
| geen regel (nu in strook.gd) | ja | 19 van 60 (32%) | 0,18 u | 1,60 u | 56 |
| pas na 3600 s open tijd | ja | 0 | 1,00 u | 2,29 u | 58 |
| pas vanaf 60 nieuwe helden | ja | 1 (0,98 u) | 0,98 u | 2,25 u | 58 |
In uur 1 komen 50 tot 69 nieuwe helden (mediaan 60). Advies: tel in nieuwe helden (`helden_nr` staat al in de save), dan hoeft er geen open tijd bij. `heldensoort.aarts_mag(helden_nr)` geeft true vanaf 60. De aartsvijand komt dan gemiddeld na ±2,3 u, nog steeds op dag 1.
