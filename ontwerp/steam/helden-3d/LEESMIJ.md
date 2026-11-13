# Helden in 3D (Daan)

Model: `producten/steam-hol/modellen/held.py`. Twee helden als eerste stand-in: **ridder** (blauwe tuniek, stalen helm met neusstuk, zwaard, rood schild) en **heks** (paarse jurk, heksenhoed met gouden band, staf met een groen lichtje). De hoeden zijn dezelfde als in Gloops toren (`gloop.py`), zodat je ziet waar de toren vandaan komt.

Los renderen: `venv/bin/python held.py uit.png ridder stap1 320 320 20` (soort ridder of heks; stand rust, stap1, stap2, schrik).
In een ander model: `import held` en `held.bouw("ridder", "stap1", plek=(x, y, 0), draai=45, schaal=0.75, gloed=25)`. Draai positief kijkt naar rechts (naar de schat). Schaal 0.75 past in de gangen van `hol.py` (1,5 hoog).

## Ronde 1 (13 nov, ±16:20 tot 16:45 UTC)
- `ronde1-los.png`: ridder in stap 1 en heks in stap 2, 320 px, op pruim.
- `ronde1-in-hol-zoom-en-ware-grootte.png` en `ronde1-in-hol-ware-grootte.png`: beide in Mila's hol (ronde 2), in de linker gang op weg naar de stekelput, schaal 0.75 met gloed 25. Gemaakt met `hol_met_helden_proef.py` (een kopie van `hol.py` met twee regels erbij; Mila's bestand is niet veranderd).

Eigen oordeel (GEZIEN met Read):
- **Goed:** dezelfde speelgoedwereld als Gloop (groot hoofd, grote ogen met glimstip, blosjes); helm en heksenhoed lezen meteen; de stap leest als lopen. In het hol vertelt het beeld nu het spel: twee helden lopen naar de put, Gloop zit op de schat.
- **Moet beter:** (1) op ware grootte zijn de helden ±30 px en lezen ze als "twee poppetjes", de gezichten niet; de gang is daar het donkerste deel. Mila: gang een trede lichter of een fakkel boven de helden, en mogelijk de gang 1,8 hoog zodat schaal 0.9 past. (2) De ridder kijkt nog te veel naar voren, bij draai 60 leest het lopen beter. (3) Het schild zit los op het lijf. (4) De heks heeft geen arm aan de stafkant die je ziet. (5) Nog geen frisse kijker.
- **Eerlijk:** dit is een stand-in, geen eindheld. Eindhelden (meer soorten, schrik, vallen, opgegeten worden) volgen na Gloop.
