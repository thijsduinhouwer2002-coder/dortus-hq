# Versie 3 met de nieuwe weg (Bram, 16 nov ±22:35 UTC, vraag Sanne 22:00)

**Vraag:** drempels boven hol 12 (en Gloop, laagsterren, bewoners) x 1,7, nu met de nieuwe weg-regel (snelheid 0,12, faam uit een keer weg hooguit 2 hol-niveaus). Landt hol 50 niet tussen 100 en 130 open uur, dan de factor zelf zetten.

**Uitkomst (GEZIEN, 30 zaden, 170 open uur, nieuw ritme en graafbonus, `uitkomst.txt`):**

| Opzet | hol 12 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|
| weg 0,25 zonder plafond, x 1,7 (zoals 21:17) | 1,1 u | 9,1 | 34,1 | 69,7 | 120,0 |
| weg 0,12 + plafond, x 1,7 | 1,1 u | 10,5 | 40,3 | 83,8 | **144,0** (buiten 100 tot 130) |
| weg 0,12 + plafond, x 1,5 | 1,1 u | 9,3 | 36,0 | 73,8 | 127,4 |
| **weg 0,12 + plafond, x 1,4 (KEUS)** | 1,1 u | 8,6 | 33,6 | 69,1 | **119,5** |
| weg 0,12 + plafond, x 1,35 | 1,1 u | 8,3 | 32,2 | 66,0 | 114,4 |

**Keus x 1,4:** hol 50 op 119,5 open uur, bijna precies het verloop van 21:17 (120,0) en ruim binnen 100 tot 130 aan beide kanten. x 1,5 haalt het ook (127,4) maar zit tegen de rand.

**Wat de nieuwe weg verder doet (`verslag-x1.4.txt` tegen `verslag-x1.7-oudeweg.txt`):**
- Goud van één nacht weg na werkdag 1 (6 open uur): 1635 in plaats van 3407; na werkdag 10: 3567 in plaats van 7387. Dus ongeveer gehalveerd, zoals bedoeld.
- Het plafond van 2 niveaus raakt in deze v3-runs nooit (afgekapte weg-faam mediaan 0): na 6 uur spelen per werkdag liggen de drempels al zo ver uit elkaar dat een nacht op 0,12 geen 2 niveaus haalt. Het plafond doet zijn werk vroeg: 30 min spelen en een nacht weg geeft zonder plafond hol 8 naar 12 (hooguit +5), met plafond 8 naar 10 (hooguit +2). Na 60 min spelen: 11 naar 13, met en zonder plafond. Toets onderaan `verslag-x1.4.txt`.
- Langste gat zonder iets nieuws (open uren, mediaan), x 1,4 nieuwe weg tegen x 1,7 oude weg: 10 tot 20 u 1,5 / 1,3; 20 tot 40 u 3,6 / 4,5; 40 tot 70 u 3,5 / 4,1; 70 tot 100 u 5,6 / 5,5; 100 tot 130 u 5,8 / 6,0. Niet slechter.
- Per week (5 werkdagen van 6 open uur): week 1 44 niveaus en 100 aankopen, week 2 17 en 60, week 3 11 en 55, week 4 10 en 5, hol 50 op werkdag 20.

**Bestanden:**
- `producten/steam-hol/sim/voortgang-v3-weg-bram.json`: de nieuwe v3-spec (drempels x 1,4, `"ritme": "nieuw"`, `"graafbonus"`, weg 0,12 met `"faam_niveaus": 2`). Draai hem direct met `sim.lagen_run`. Ik schreef hem als nieuw bestand en niet over `voortgang-v3-eind-bram.json`, omdat elf scripts (ook Sannes `eerste20-gat.py`, `sim-ritme/ritme.py`, `sim-graafbonus/graafbonus.py`) die oude json lezen en anders iets anders zouden geven dan hun uitkomstbestand. De oude json kreeg alleen een verwijzing in `_uitleg`.
- `sim.py` kent nu zelf de sleutels `ritme`, `graafbonus` en weg `faam_niveaus` (zonder die sleutels verandert er niets; nagekeken: `v3ritme.py`, `graafbonus.py`, `eerste20-gat.py` en dit script geven precies hun oude uitkomst).
- `v3weg.py`: het script. Draai: `python3 -I platformen/steam/data/sim-v3-weg/v3weg.py producten/steam-hol/sim 30 170 1.7 1.5 1.45 1.4 1.35` (±45 s). Met `KEUS=1.4` erbij komt het volle verslag en de plafondtoets; met `KEUS=1.7 VERGELIJK=1` het verslag met de oude weg.
