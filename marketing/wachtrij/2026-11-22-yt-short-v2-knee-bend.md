# YouTube Short recept v2, nr 2: How far can this knee bend? Check it before you print 👀 | Blender

- status: open
- kanaal: youtube-short
- soort: tip
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/youtube-shorts-3/short-2-knee-bend-geluid.mp4
- geluid_check: GOED (gemiddeld -16,5 dB, piek -1,3 dB), 22 nov 2026 ±01:15 NL, op het releasebestand: workflow run 44964764424 (`geluid_check.txt` in de release) en lokaal opnieuw na downloaden
- lengte: 0:43,7, staand 1080x1920
- tijd: (leeg: de hoofdchat plant in YouTube Studio in)
- doel: dortus.com/yt (over te typen; niet klikbaar in een Short). Als gerelateerde video: de nieuwste lange Pro-video.
- gemaakt_door: Shorts-agent recept v2 (opdracht hoofdchat 22 nov ±00:05 NL)
- vorige:

## Titel
How far can this knee bend? Check it before you print 👀 | Blender

## Tekst
```
How far can the knee of your 3D printed figure bend? Check it in Blender before you print:
1. Give the knee a Limit Rotation in your rig (here 120°).
2. Select the figure and press Figure from rig.
3. The list shows the left knee 0 to 120° from your rig; the right knee without a limit takes the same range (mirrored).
4. Bend the knee with the Bend slider: it stops at 120°. Past the stop, the parts turn red.

Measured in Blender, not print tested by us yet. Print a test joint first, every printer is different.

Real screen recording in Blender 5.3 with our add-on Click Joints Pro 1.1. Figure: MakeHuman base mesh (CC0 1.0, github.com/makehumancommunity/makehuman), colours and rig added by us.
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- Recept: `platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-21-malikose-tip-format.md` (recept v2 onderaan). Eerste beeld is het eindresultaat (figuur in pose, of uit elkaar bij nr 4), daarna stap voor stap.
- Beeld: één echte opname in Blender 5.3.0 met Click Joints Pro 1.1.0 (code van commit f727466, dezelfde als de Gumroad-zip), `commercie/filmpjes/youtube-shorts-3/opname.py`, workflow `.github/workflows/youtube-shorts-3.yml`, release youtube-shorts-3 (`opname-pro.mkv`, `film-pro.json`, `opname-pro.log`). Release youtube-shorts-2 bestond al (reeks 2 van Chris), daarom heet deze release youtube-shorts-3.
- Muis: de echte muis van het X-scherm (xdotool) beweegt en klikt; de knoppen vindt het script op het scherm met tesseract. Alle klikken raakten (geen "KORT vangnet" in `opname-pro.log`): figuur kiezen, Figure from rig, paneel openen, Exploded view, 3MF, Export 3MF. De Bend-schuif zet het script op de waarde terwijl de muis over de schuif loopt (zoals slepen). Een X-schermafbeelding toont de muis niet: `kort.py` tekent een pijltje op de plek die de opname per beeld opschreef, met een geel kringetje bij een klik.
- Staand gesneden zoals Malikose: boven de echte 3D-weergave met menubalk, onder het echte paneel van Click Joints (`kort.py`). Bogen, getallen, rood, "+4° past limit", lijst en export komen van de add-on zelf; het script kleurt niets aan de uitkomst.
- Model: MakeHuman base mesh, https://github.com/makehumancommunity/makehuman (bestand makehuman/data/3dobjs/base.obj; licentie van de assets: CC0 1.0, LICENSE.md in die repo, GEZIEN met curl 22 nov ±00:40 NL). Licentie CC0 1.0, naamsvermelding niet verplicht; wij noemen de bron toch in de beschrijving. Rig met Mixamo-botnamen uit `producten/blender-gewrichten/e2e/proef_mens.py` (linkerknie 120° en linkerelleboog 140° in Limit Rotation, rechts niets). Kleuren (oranje pak, turquoise handen en voeten) zet ons script als invoer, vóór de knop. Geen AI-model, geen bekend figuur of merk.
- Ondertitels in beeld (groot, twee regels van 2 tot 4 woorden, tijden uit `metingen.json` in de release): How far can / this knee bend? (0.0–2.5 s) | A rig with / Limit Rotation 120° (2.5–5.3 s) | Press / Figure from rig (5.3–8.1 s) | Left knee: / 0 to 120° from rig (8.1–14.77 s) | Right knee: / mirrored from the left (14.77–17.77 s) | Bend it / in the panel (17.77–24.9 s) | It stops at 120°, / past that: red (24.9–34.7 s) | Same check / for every joint (34.7–37.7 s) | Check the pose / before you print (37.7–43.7 s). Onderaan steeds "Measured in Blender, not print tested by us yet.", de laatste 5 s ook "dortus.com/yt".
- Wat Pro 1.1 kan: `platformen/blender-2/gumroad-1.1.md` (hinges at elbows and knees, ball joints at shoulders, hips and neck; end stop from Limit Rotation; mirrored; list with ranges; red past the stop; exploded view; export STL or 3MF).
- Getallen uit de opname (GEZIEN, `film-pro.json` en `opname-pro.log` in release youtube-shorts-3): 9 gewrichten ("9 joints · 2 rig · 2 mirror · 5 preset"), linkerknie 0 tot 120° from rig, rechterknie 120° mirror, export 10 bestanden .3mf (één per deel).
- Geluid: met code gemaakt (`commercie/filmpjes/geluid/geluid.py`: rustige toon, tikje bij elke nieuwe ondertitel, klikgeluid bij elke muisklik), geen stem, geen AI-stem, geen muziek van een ander. geluid_check door de workflow op het releasebestand (`geluid_check.txt` in de release).
- dortus.com/yt: Pro-pagina "Click Joints Pro for Blender: rig to printable figure" (GEZIEN met curl 22 nov ±00:35 NL). Geen Gumroad-adres, geen prijs of korting, nergens "holds a pose".
- Zelf bekeken (skill kijken): 10 beelden met Read (0,05 s, 3,5, 6, 9, 13, 18, 23, 28, 33, 38 s). Eerste beeld: figuur in pose met bogen, kop "How far can / this knee bend?". Lijst met "Left knee · Hinge · 0–120° · from rig" en "Right knee ... mirror" leesbaar in het paneel, Bend-schuif met de muis erop, rood voorbij de stop, terug naar 81. Lengte met ffprobe op het releasebestand: 43.7 s (40 tot 60: goed; de workflow faalt bij een andere lengte).

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de hoofdchat: regel onderaan `commercie/geplaatst.md`)
