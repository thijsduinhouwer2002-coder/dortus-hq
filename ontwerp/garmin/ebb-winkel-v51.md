# Ebb: winkelbeelden v5.1 (Mila, run 55, 12 nov)

Opdracht hoofdchat 12 nov 07:25 (drie punten, één harde eis). Script `bron/winkel_v51.py` (basis `winkel_v5.py`), beelden `winkel51/` (poster 1000, kaarten 800, `rij-220.png`, `overzicht-500.png`).
GEZIEN met Read: `overzicht-500.png`, `rij-220.png` en kaart 2 op 500.

## Wat er veranderde
1. **HARDE EIS, poster:** kop is nu "Breathe. Make **sea friends.**" (besluit 11 nov 23:25). Het scherm op de poster is nu het ademscherm (krab inademen dag, "breathe in 12"), niet meer het inhoudscherm met "hold 1:45": een timer van het inhouden op de poster verkoopt inhouden toch, ook met de goede kop. Briefje "can't swim yet" blijft, pijl naar de linkerkant van de zwemband (468, 668).
2. **Kaart 2 "Every friend, their own world":** geen half cijfer meer in de rondjes. Het venster is gemeten op de witte pixels van de echte schermen: het cijfer eindigt op y 153 van 454, "round 2 · 18 left" begint op y 316; de uitsnede is y 159 tot 309 (vak 0,33 van de breedte, midden y 0,515). Geen tekst in beeld op alle drie.
3. **Kaart 3 dag en nacht:** het nachthorloge heeft een lichte rand (200, 200, 255) en een zachte blauwe gloed achter de kast. Op 220 px staat het nu los van de kaart.

## Nagelopen op inhouden als doel (alle zes beelden en de winkeltekst)
| Nr | Kop | Scherm | Verkoopt inhouden? |
|---|---|---|---|
| 0 | Breathe. Make sea friends. | krab inademen | nee (was: hold 1:45, nu weg) |
| 1 | Breathe in. The sea rises. | krab inademen | nee |
| 2 | Every friend, their own world. | drie uitsneden zonder tekst | nee |
| 3 | The sea keeps your time. | krab inademen dag en nacht | nee |
| 4 | Your day is a beach walk. | Today met schelpen | nee (schelp per sessie, geen tijden) |
| 5 | Fill your sea log. | sea log | nee |

Winkeltekst v12 (tak `claude/garmin-2026-11-10b`, `producten/garmin-adem/winkeltekst.md`, gelezen met curl): geen kop of zin die inhouden als doel verkoopt. Er staat "Hold only while it feels easy", "never by holding longer" en de veiligheidsregels; dat is goed. Wel let op voor Gijs: het veld Screenshots daar noemt nog de beelden v4 (`1-hold.png` enzovoort). Bij het uploaden horen de beelden v5.1 (zodra ze met echte schermen gevuld zijn), dus `1-hold.png` valt weg.

## Voor Gijs
Zelfde vervanglijst als in `ebb-winkel-v5.md`, met twee wijzigingen: poster = krab **inademen** dag (niet hold); kaart 2 uitsnede midden y 0,515 en vak 0,33 (x blijft 0,50 / 0,60 / 0,64). Meet het venster opnieuw op de simulatorschermen: de bovenrand moet onder het cijfer en de onderrand boven de rondjesregel.

## Nog open
- Opbouw varieert nog weinig (rondjes op blauw). Niet in deze ronde, want de hoofdchat vroeg drie gerichte punten.
