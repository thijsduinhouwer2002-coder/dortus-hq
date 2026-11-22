# YouTube Short recept v2 (herstel), nr 3: Your rigged character as printable parts with joints 🧩 | Blender

- status: ingepland
- kanaal: yt-short
- soort: video
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/youtube-shorts-4/short-3-printable-parts-geluid.mp4
- geluid_check: GOED (gemiddeld -16,5 dB, piek -1,2 dB), 22 nov 2026 ±02:25 NL, op het releasebestand: workflow run 44969683236 (`geluid_check.txt` in de release) en lokaal opnieuw na downloaden
- lengte: 0:43,3, staand 1080x1920
- tijd: ma 23 nov 12:00 NL (ingepland in YouTube Studio door de hoofdchat, 22 nov ±10:40 NL)
- adres: https://www.youtube.com/shorts/pCyyQ4Qa9Gw (privé tot het moment, dan openbaar; gerelateerde video m3sNvDOJYQ0; niet voor kinderen)
- geüpload bestand: 720x1280, opnieuw gecodeerd naar ±3,5 MB omdat het uploadgereedschap maximaal 3,8 MB per bestand aanneemt; geluid_check GOED (±-16,4 dB). Inhoud verder gelijk aan het releasebestand.
- doel: dortus.com/yt (over te typen; niet klikbaar in een Short). Als gerelateerde video: de nieuwste lange Pro-video.
- gemaakt_door: Shorts-agent recept v2 (herstel na keuring, opdracht hoofdchat 22 nov ±01:25 NL)
- vorige: 2026-11-22-yt-short-v2-printable-parts.md

## Titel
Your rigged character as printable parts with joints 🧩 | Blender

## Tekst
```
From one rigged character to separate printable parts with joints, in Blender:
1. Select the rigged figure and press Figure from rig.
2. It is cut into parts with 9 joints.
3. Exploded view moves the parts apart along each joint: you see the ball and socket at the shoulder and at the hip.
4. Pick 3MF and press Export: one file per part (10 files here).

Measured in Blender, not print tested by us yet. Print a test joint first, every printer is different.

Real screen recording and viewport render in Blender 5.3 with our add-on Click Joints Pro 1.1. Figure: MakeHuman base mesh (CC0 1.0, github.com/makehumancommunity/makehuman), colours and rig added by us.
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- Herstel na de keuring `marketing/keuring/2026-11-22-yt-shorts-3.md` (alle 4 rood). Wat anders is: eigen eerste beeld per Short (een stilstaande render, 3 s met een langzame zoom, geen gradengetallen, geen label, niets achter de ondertitel), eigen pose, eigen opbouw en eigen eind; teksten bij het rood zeggen wat je ziet (rode boog en "+12° past limit"); printzin en dortus.com/yt boven de onderste 15%. Reeks 3 had 4 Shorts; nr 3 (posable-toy) vervalt omdat hij een kopie van nr 1 was (opdracht hoofdchat: 3 sterke in plaats van 4 gelijke).
- Eerste beeld: render-3.png: de figuur in Exploded view, dichtbij romp en heupen: de kogels tussen romp en benen zijn te zien (onderkant zacht vervaagd boven de ondertitel). Gemaakt aan het eind van dezelfde opname: Blender rendert de 3D-weergave door een camera (Material Preview, EEVEE; `bpy.ops.render.opengl`), met glanzende plastic materialen (Principled BSDF, ruwheid 0,3, coat) en drie zonlampen, achtergrond leeg (de effen kleur zet `kort.py` eronder). De buiging komt van de add-on (Bend in het paneel, binnen het bereik in de lijst); wij draaien geen delen zelf. Een Cycles-render liet de buiging in onze proef niet zien (de add-on zet hem in delta_rotation); daarom de render van de 3D-weergave. Armen echt omhoog kan niet eerlijk: schouders zijn kogels met ±20° en draaien alleen de bovenarm, dus de pose blijft bij knieën en ellebogen.
- Eind: render-4.png, de hele figuur in Exploded view van schuin achter, met "One 3MF file / per part" (anders dan nr 1 en 2).
- Beeld daarna: één echte opname in Blender 5.3.0 met Click Joints Pro 1.1.0 (code van commit f727466, dezelfde als de Gumroad-zip), `commercie/filmpjes/youtube-shorts-4/opname.py`, workflow `.github/workflows/youtube-shorts-4.yml`, release youtube-shorts-4 (`opname-pro.mkv`, `film-pro.json`, `opname-pro.log`, `render-1.png` tot `render-4.png`). Release youtube-shorts-3 blijft staan.
- Muis: de echte muis van het X-scherm (xdotool) beweegt en klikt; de knoppen vindt het script met tesseract. Alle klikken raakten (geen "KORT vangnet" in `opname-pro.log`); wel stond er één keer "KORT ocr niet gevonden: 'Export 3MF'": de eerste poging vond de knop niet, de tweede wel (het script probeert tot 5 keer). De Bend-schuif zet het script op de waarde terwijl de muis over de schuif loopt (zoals slepen). Een X-schermafbeelding toont de muis niet: `kort.py` tekent een pijltje op de plek die de opname per beeld opschreef, met een geel kringetje bij een klik.
- Staand gesneden zoals Malikose: boven de echte 3D-weergave, onder het echte paneel van Click Joints. Bogen, getallen, rood, "+12° past limit", lijst en export komen van de add-on zelf.
- Model: MakeHuman base mesh, https://github.com/makehumancommunity/makehuman (`makehuman/data/3dobjs/base.obj`), licentie van de assets CC0 1.0 (LICENSE.md deel C, GEZIEN met curl 22 nov). Rig met Mixamo-botnamen uit `producten/blender-gewrichten/e2e/proef_mens.py` (linkerknie 120° en linkerelleboog 140° in Limit Rotation, rechts niets); kleuren zet ons script als invoer, vóór de knop. Geen AI-model, geen bekend figuur of merk.
- Ondertitels in beeld (tijden uit `metingen.json` in de release): Your character as / printable parts (0.0–3.0 s) | Select the / rigged figure (3.0–5.8 s) | Press / Figure from rig (5.8–8.6 s) | Cut into parts / with 9 joints (8.6–11.93 s) | Exploded view: / ball and socket (11.93–23.13 s) | Same at / the hip (23.13–31.13 s) | Pick 3MF, / then Export (31.13–39.8 s) | One 3MF file / per part (39.8–43.3 s). Printzin "Measured in Blender, not print tested by us yet." steeds in beeld (boven het paneel, of onder de ondertitel bij de render); de laatste 5 s ook "dortus.com/yt".
- Wat Pro 1.1 kan: `platformen/blender-2/gumroad-1.1.md` (hinges at elbows and knees, ball joints at shoulders, hips and neck; end stop from Limit Rotation; mirrored; list with ranges; red past the stop; export STL or 3MF). Exploded view staat níet in gumroad-1.1.md: die knop komt uit de add-on zelf (in beeld, en `producten/blender-gewrichten/architectuur.md` op commit f727466).
- Getallen uit de opname (GEZIEN, `film-pro.json` en `opname-pro.log` in release youtube-shorts-4): 9 gewrichten ("9 joints · 2 rig · 2 mirror · 5 preset"), linkerknie 0 tot 120° from rig, rechterknie mirror, voorbij de stop 132° ("+12° past limit"), export 10 bestanden .3mf (één per deel).
- Geluid: met code gemaakt (`commercie/filmpjes/geluid/geluid.py`: rustige toon, tikje bij elke nieuwe ondertitel, klikgeluid bij elke muisklik), geen stem, geen muziek van een ander.
- dortus.com/yt: Pro-pagina "Click Joints Pro for Blender: rig to printable figure" (GEZIEN met curl 22 nov ±00:35 NL). Geen Gumroad-adres, geen prijs of korting, nergens "holds a pose".
- Zelf bekeken (skill kijken): eerste beeld groot (540 px) en 10 beelden gelijk verdeeld van 3,2 s tot het eind, van het releasebestand. Eerste beeld: render in Exploded view dichtbij romp en heupen, de twee kogels tussen romp en benen goed te zien, onderkant zacht vervaagd, niets achter de ondertitel. Daarna kiezen, Figure from rig, Exploded view bij de schouder en bij de heup, 3MF gekozen (knop blauw) en Export 3MF, eind op render-4: de hele figuur uit elkaar van schuin achter met "One 3MF file / per part" en dortus.com/yt. Lengte met ffprobe op het releasebestand: 43.3 s (40 tot 60: goed).

## Keuring
groen (akkoord): moet-punten van reeks 3 opgelost, eerste beeld toont losse delen met kogels; figuur zonder hoofd en grijze onderarm mogen later (kan-punten in `marketing/keuring/2026-11-22-yt-shorts-4.md`, keurder, 22 nov ±02:20 NL).

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de hoofdchat: regel onderaan `commercie/geplaatst.md`)
