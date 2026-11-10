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
