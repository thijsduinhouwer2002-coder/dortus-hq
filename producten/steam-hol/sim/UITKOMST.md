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
