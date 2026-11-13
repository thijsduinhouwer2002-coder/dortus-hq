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

## Frisse kijker ronde 1 (alleen de plaatjes, letterlijk samengevat)
- Ware grootte: "groene slijmbal met één oog, kroontje en zilveren helm op een berg goud. Links lopen twee kleine figuurtjes naar hem toe. Ik denk een verdedig- of tower-defense-spel: helden komen het hol binnen om de schat te pakken." Niet te zien: wie wie is, zwaard, schild, staf, gezichten, of ze lopen. "De tovenaar is donkerpaars op een donkerpaarse achtergrond." Stoppen met scrollen: 4 of 5 van 10, "de helden zijn te klein om te begrijpen wat het spel is".
- Los: "ridder met ronde zilveren helm, blauw pak, rood schild, klein zwaard; heks met paarse punthoed met gouden band. Schattig, glanzend speelgoed, niet eng, niet echt generiek." 7,5 van 10. Stoort: "gezichtjes kijken verbaasd of leeg", heks valt weg, ridder staat scheef.
- Winst: voor het eerst raadt een kijker het spel zonder uitleg (helden komen de schat halen). Dat is precies wat Mila's strook miste.

## Ronde 1b (zelfde run, ±16:30 UTC)
- Heks in een warm oranje jurk (hoed blijft paars, zoals op de toren): valt niet meer weg tegen pruim.
- Kleine glimlach en wenkbrauwen in plaats van de o-mond (de o-mond blijft voor `schrik`).
- Ridder met draai 60 in de proef: loopt duidelijker naar rechts.
- `ronde1b-los.png`, `ronde1b-in-hol-zoom-en-ware-grootte.png`, `ronde1b-in-hol-ware-grootte.png`.
- Voor Mila: de hangende wortels bij x ±-8,7 lopen door het gezicht van de heks, en een wandlamp staat precies achter het hoofd van de ridder. Helden of wortels een stukje verschuiven. Het grootste punt blijft de maat: op ware grootte zijn helden ±30 px in een donkere gang.

## Volgende ronde (Daan)
1. Grotere koppen ten opzichte van het lijf (op 30 px telt alleen het hoofd en de hoed), en een lichte rand van achteren zodat ze loskomen van de gang.
2. Schild vast aan de arm; de heks een zichtbare arm aan de stafkant.
3. Standen voor de pijplijn: rust, stap1, stap2, schrik, vallen.
