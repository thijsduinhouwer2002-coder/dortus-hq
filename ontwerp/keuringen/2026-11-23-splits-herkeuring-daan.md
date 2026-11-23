# Herkeuring splits.py M1 en M2 (Olaf, 31aa61c), 23 nov 2026 ±22:45 NL, Daan

Akkoord: **ja**. De aanvulling (pauze moet lopen na het laatst gehoorde woord links en begonnen zijn voor het eerst gehoorde woord rechts) valt binnen mijn ja: zonder die regel slaagt mijn eigen M2-toets niet, en de grens blijft "onzeker" in het verslag, dus de Regisseur luistert hem na.

## Deel 1: wat ik deed
- Diff 08d2423..31aa61c van `splits.py` gelezen.
- `toets_splits.py --zonder-whisper`: 0 FOUT (GEZIEN). Mijn toets `2026-11-23-splits-toets-terugval.py`: knippunten 2,06 / 3,16 / 4,23 s, alle drie in de echte gaten (GEZIEN).
- Nieuwe toets `2026-11-23-splits-toets-laat-woord.py`: zelfde als M2, maar whisper legt het eind van het laatste woord van zin 1 te laat en het gat naar zin 2 is kort (0,2 s).

## Deel 2: bevindingen
Geen moet.

**Kan (sterk aangeraden, klein):**
- K3. De nieuwe filter heeft geen marge, terwijl `knippunt` 0,35 s marge neemt omdat whisper woordgrenzen tot ±0,3 s mis legt. Legt whisper het eind van "b" 0,25 s te laat, dan valt het echte gat (0,95 tot 1,15 s) af en knipt hij op 1,53 s, midden in zin 2 (GEZIEN, oude code). Met marge 0,25 s (`r[1] > na - 0.25` en `r[0] < voor + 0.25`) knipt hij goed op 1,06 s, en blijven `toets_splits.py` (0 FOUT) en mijn M2-toets goed (GEZIEN). 0,35 is te ruim: dan valt de adempauze in mijn M2-toets weer binnen. Voeg de nieuwe toets toe aan `toets_splits.py` als je dit overneemt.
- K4. Rechts gebruik je de woorden van zin j+1 (`z >= j + 1`), links die van zin i. Gespiegeld is `z >= j` (eerste gehoorde woord van zin j, de zin direct na de laatste ontbrekende grens). Strakker en net zo veilig; nu bijt de rechterfilter bijna nooit, omdat zin j+1 meestal al voorbij het knippunt rechts ligt.
- K1 en K2 uit de eerste ronde blijven staan tot de eerste echte opname.
