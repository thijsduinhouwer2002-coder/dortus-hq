# Hoedenwand (Mila, 16 nov 2026)
Elke held die Gloop opat, laat een hoed achter die scheef half in de aardwand boven de gang blijft steken. Dichtheid en eigen gezicht in één: de wand is het logboek van wie Gloop at. Uitleg en doelbeeld: `ontwerp/steam/winkelpagina/vol/LEESMIJ.md`.
- `hoedenwand.py`: holte (donker), de hoed uit `producten/steam-hol/modellen/hoeden.py` (schaal 1,25, zijwaarts gekanteld), een platte aardrand met kluitjes en steentjes ervoor. Doorzichtige achtergrond. Camera en licht uit `gedeeld.py`.
- `renders/wand-<nr>.png`: alle 10 hoeden (kanteling -22, 18, -15, 25, -18, 20, -25, 15, -12, 22 graden), 400x300, 32 samples, ±6 s per stuk op de CPU (bpy 5.2.4).
- GEZIEN met Read: alle tien als blad op aardkleur, en op 50 px in de strook (doelbeeld): elke hoed blijft herkenbaar, de holte maakt dat hij IN de wand zit.
- Zwak: de onderrand van de aardschijf is iets donkerder dan de wand van het spel; als het in de pijplijn zit, de aardkleur gelijk trekken met `aardemat("pruim")` uit `hol.py`.
- `wortels.py` en `renders/wortels-1..3.png`: wortels onder het gras geprobeerd. GEZIEN in het doelbeeld: te dun en vaag op 600, en ze liepen over de kamers. Niet gebruikt; als iemand het opnieuw probeert: dikker (2x), lichter en alleen tussen kamers.
- **Klaar voor de pijplijn:** `blad/hoedenwand.png` (604x56, 39 kB, px 4 zoals deco.png) en `blad/hoedenwand.json` in de vorm van `sprites.json` ("soort": "stukken"; per stuk `maat` in spelpixels, `vak_px`, en `midden` = midden van de holte). Elk stuk 13 spelpixels breed. Gemaakt met `maak_blad.py`. GEZIEN met Read op spelmaat 2x op wandkleur: alle 10 hoeden te herkennen; de pet (rood) is het zwakst.
- Voorstel plaatsing (Olaf): op de aardwand boven de gang, `midden` op spelpixel y 14 tot 20, alleen in kolommen zonder kamer erboven (`not h.boven[k]`), hooguit één per twee kolommen, hash-plek zoals `deco_hh`. Aantal = aantal opgegeten helden (hooguit wat er past). Volgorde: de hoed van de held die werd opgegeten (`hoed_nr`).

## 16 nov ±10:00 UTC: moets van Daan (09:50) verwerkt, alleen in de wand
- `wand_beter(nr, h)` in `hoedenwand.py`; `hoeden.py` blijft gelijk, dus de helden en de hoedenhoop veranderen niet.
- **Kap (2):** punt bovenop (knakt iets naar rechts), donkerder groen (4a7a2a) en een donkere leren band (1f3a17) net boven de aardrand. Waarom: zonder punt en rand was het een groene bol, dus slijm.
- **Pet (3):** klep wit (f4f1ea), groter en naar de camera gekanteld (`PET_KLEP_LOC`, `PET_KLEP_ROT`), witte knoop bovenop weg (een stip op een rode koepel is een paddenstoel), en **kanteling -18 in plaats van 25** (bij 25 hing de klep als een tong omlaag de aarde in).
- **Hoge hoed (7) en pan (8):** holte lichter (4a2a1e in plaats van 2e1712) en een warm vlaklicht van boven achter, zodat de bovenrand oplicht.
- GEZIEN met Read: `blad/vgl-moets-daan-oud-boven-nieuw-onder.png` (renders groot), `blad/vgl-blad-oud-boven-nieuw-onder-2x.png` (blad op spelmaat 2x), en uitsneden uit het opnieuw gemaakte doelbeeld op 1920 en 600. Oude renders bewaard in `renders/oud-voor-daan-0950/`.
- Voor de pijplijn (Bram): neem `_mat_kleur`, `PET_KLEP_*` en `wand_beter` over in `producten/steam-hol/modellen/hoedenwand.py`, roep `wand_beter(nr, h)` aan na de kanteling, en zet `KANTEL[3]` op -18.
