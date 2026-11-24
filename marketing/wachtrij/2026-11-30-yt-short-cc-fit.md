# Click Cuts Short 1: Model too big for your printer? Split it to fit 🔥

- status: open (plaatsen pas als Click Cuts live is en de winkellink werkt)
- kanaal: yt-short
- soort: video
- soort_reeks: lancering Click Cuts, script 1 van 6 (`commercie/filmpjes/scripts/click-cuts-lancering.md`, ja Daan na M1 en M2), hook 1A. Volgorde 1, 2, 3, 6, 4, 5: deze op de lanceringsdag.
- product: click-cuts
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-19/cc-fit-geluid.mp4 (nagekeken 24 nov run 18, workflow-run 45362400164 groen)
- stem_tekst: `commercie/filmpjes/regisseur-19/cc-fit-stem.txt` (voor Max van de hoofdchat; tot die er is Kokoro)
- lokale montage uit de proef (elk 4e beeld, Kokoro, 24 nov, GEZIEN): 43,9 s, geluid_check GOED (-16,6 dB, piek -1,4 dB), synchroon GOED 11 van 11 (grootste 0,267 s), 12 beelden bekeken. Daarna kader dikker en hook dichterbij; het releasebestand van regisseur-19 is nog niet nagekeken (volgende run).
- metingen (lokale proef met de echte muis, Blender 5.3.0, Click Cuts-zip van main 24 nov, elk 4e beeld, GEZIEN): Lion Head 320,5 x 206,4 x 436 mm, 47.214 vlakken; printer via de echte keuzelijst op Bambu Lab A1 mini; Split to fit met de echte klik: 12 stukken, alle 12 groen, 68 pennen, speling 0,20 mm; paneel "12 parts, all fit the bed" en "68 pins, 0.20 mm clearance"; Export parts met de echte klik: 13 STL-bestanden (piece_01.stl enz. plus de pennen), melding "13 STL files in ..." (GEZIEN, schermbeelden van de proef).
- releasebestand (GEZIEN): 43,9 s, 1080 x 1920; geluid_check GOED (-16,6 dB, piek -1,4 dB); synchroon GOED 11 van 11 (grootste 0,287 s); metingen film-tip.json: printer via de echte lijst, Split to fit en Export parts via OCR geklikt, 12 stukken alle groen, 68 pennen, 13 bestanden. 12 beelden bekeken, eerste groot: grijze leeuw, kop steekt boven het rode bedkader uit, geen zwevende getallen. Kan beter: het allereerste beeld staat nog ver weg (de zoom komt pas in 1 s), en bij zin 4 (watertight) zie je alleen de geselecteerde leeuw.
- tijd: voorstel lanceringsdag Click Cuts (week van 30 nov, de hoofdchat kiest)
- doel: de winkellink van Click Cuts (eerste regel van de beschrijving, invullen na de uitgave)
- gemaakt_door: Regisseur run 18 (24 nov 2026); opname in workflow regisseur-19 (Blender 5.3.0, xvfb, echte muis, gedeelde hulpcode van Olaf)
- vorige:

## Titel
Model too big for your printer? Split it to fit 🔥 | Blender

## Tekst
```
<winkellink Click Cuts, invullen na de uitgave>

Model too big for your print bed? Click Cuts splits it in Blender.
1. Pick your printer, or type your own bed size.
2. Press Split to fit.
3. Every part fits your bed, with pins and pin holes in every cut.
4. Export every part and the pins as STL or 3MF, in millimeters.

Measured in Blender, not print tested by us yet. Print the fit test first.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Script en regels:** `commercie/filmpjes/scripts/click-cuts-lancering.md` nr. 1 (geen prijs, geen print-belofte, geen klik of magneten, "fewest parts" niet "fewest possible", N niet uitspreken). Daan keurde de scripts.
- **Twee zinnen erbij** (anders te kort, 104 woorden is ±35 s): "Open model? It makes a watertight copy first, in the same click." bron `producten/blender-splitser/split_joints/in_een_klik.py` r. 1 tot 3 (Split to fit doet Make watertight alleen als het nodig is). "Parts that touch never share a color, so you see every cut." bron `kleuren.py` (kleur per stuk, buren nooit gelijk, volgens het script). Graag meekeuren.
- **Flits van het eindbeeld vóór 1A (Daan C2):** niet gedaan; montage2 kent geen stille scène. Het eerste beeld is de leeuw met een rood kader van het bed van de A1 mini (180 mm), de kop steekt erboven uit. Het kader is een eigen hulpvorm in de opname, geen deel van Click Cuts.
- **Printers:** `printers.py` (9 printers en Custom size; A1 mini 180 x 180 x 180 mm, bron OrcaSlicer-profielen).
- **Uitslag, pennen, export:** `in_een_klik.py` (uitslagregels), `exporteer.py` (STL of 3MF in mm, elk stuk en de pennen), `paneel.py` (Your printer, Split to fit, Export parts).
- **Model:** Lion Head, Poly Haven, CC0 (DERDEN: https://polyhaven.com/a/lion_head), zoals release splitser-merk-1.
- **Stem:** tijdelijk Kokoro-82M, af_heart, Apache 2.0 (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). ElevenLabs-opname (Max) gevraagd: `cc-fit-elevenlabs.mp3` in `commercie/filmpjes/regisseur-19/`.
- **Nieuw onderwerp:** eerste Short over Click Cuts; geen Short over splitsen in de laatste 14 dagen (wachtrij en RSS nagekeken 24 nov, GEZIEN).

## Keuring
- keurder: Iris, 24 nov 2026 ±12:00 UTC (opdracht hoofdchat 11:50), `marketing/keuring/2026-11-24-yt-short-cc-fit-pas-nummers-iris.md`
- beeld en plezier: akkoord **nee**
- moet M1: zin 7 en tekstpunt 3 beloven pennen in elke snede, maar dezelfde leeuw geeft in de nieuwere zip "1 note (glue joints)" (zie cc-nummers, `verbinders.py` r. 99). Zin aanpassen of bewijzen dat de cc-fit-opname nul meldingen had; nieuwe opname met de huidige zip. Nakeuren alleen op M1.
- kan: eerste beeld dichterbij (kop boven het kader), leeg beeld bij 2 s eruit; ondertitel niet over de printerlijst; kanaal `yt-short` gelijk maken aan `youtube-short`.

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
