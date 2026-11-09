# Het Hol: startgetallen voor de balans (Sanne)

Stand 9 nov 2026, ±19:10 UTC. Voorstel voor de **eerste speelbare versie**, zodat Olaf en Bram niet met losse gokgetallen bouwen. Bram's `sim/` is de echte toets; dit is een ruwe proef om te starten (`platformen/steam/data/balans-proef.py`, vast zaad, speler koopt steeds het goedkoopste). Alle getallen GOK tot Bram's sim en een speelronde ze bevestigen.

## Stand 9 nov 19:50 UTC: Bram's sim gaat voor (Sanne akkoord)
Bram's simulatie (`producten/steam-hol/sim/UITKOMST.md`) liet zien dat mijn startgetallen 68 tot 74% vluchten gaven, omdat een held in het spel omdraait na een klap. Zijn nieuwe getallen gelden, ik ben het met elk punt eens: **slijm 45%, put 35%, schijterig draait de helft van de keren om, faam x 0,97 per niveau met bodem 0,75, volgende held is een terugkomer 25%, een gevluchte held komt 60% ooit terug (aartsvijanden altijd), een aartsvijand die aan de beurt is komt 15%.** Uitkomst: 36 tot 41% vluchten, aartsvijand ongeveer één keer per dag, langste wacht 7 tot 11 min in het eerste uur, alles gekocht na 6,4 tot 7,1 uur. Kosten en goud hieronder blijven.

Drie dingen die ik er nog bij zie:
1. **Goud per val:** de tabel zegt 6 bij de start, de film (run 42685438422) geeft +3 per val. Olaf: welke klopt in `strook.gd`? Ik kies 6, want daar rekent de sim mee; met 3 duurt de eerste aankoop twee keer zo lang.
2. **De 40 helden die "met pensioen" gaan** (40% komt nooit terug) zijn een kans voor een kroniekregel bij openen ("Pim the Once-Fled retired. Opened a bakery."), geen straf. Staat in `kroniek-regels.md` als ik er tijd voor heb.
3. **Hoard-Toucher 3 tot 6%** is weinig voor een van onze beste grappen. Goed zo voor de balans, maar in de film van een minuut moet hij één keer te zien zijn (demo mag dat sturen, zoals `moet_vallen`).

## Getallen (startvoorstel 19:10; kansen en faam vervangen door de stand hierboven)
| Wat | Waarde |
|---|---|
| Held komt binnen | elke ±50 s (past bij `strook.gd` 25 tot 70 s en `voortgang.gd` 47,5 s) |
| Kans dat een held valt per verdediging op zijn pad | slijm 30%, stekelput 22%, +7 procentpunt per upgrade |
| Helden worden sterker met faam | elke 60 helden één faamniveau: kans per verdediging × 0,9, goud per val +10% |
| Goud per gevallen held | 6 × (1 + 0,1 × faam) × (1 + gangen / 40) |
| Graven, één cel | 5 + 1,2 × aantal gangcellen (start met 6 cellen, dus de eerste kost 12; max 40 cellen) |
| Extra slijm of put | je begint met één van elk; extra kost 104, 270, 703 (40 × 2,6^aantal; max 4 van elk; de tweede pas bij 8 gangcellen, de derde bij 16, de vierde bij 24) |
| Upgrade per bewoner of val | 60, 168, 470 (× 2,8; drie per soort) |
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
