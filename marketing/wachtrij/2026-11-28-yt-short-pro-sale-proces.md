# Sale-Short Click Joints Pro (procesvorm v7): From rig to poseable figure in Blender 🤖

- status: CONCEPT v7, wacht op keuring Daan (issue "Keur: sale-Short v7", #159). Thijs keurde v6b af (26 nov 18:10); v7 volgt zijn opdracht van 18:14 en het bericht van de hoofdchat van 18:30: alles in één beeld. Eerste beeld: blinde test kon niet draaien (ChatGPT en Gemini zonder tegoed, run 45876865256), dus nog NIET GESLAAGD; niet plaatsen voor dat geregeld is of de hoofdchat anders beslist.
- eigen controle (GEZIEN, 26 nov ±20:30 NL): 22,1 s, 1080x1920, 30/1, 663 beelden, 0 gaten en 0 dubbele tijdstempels (`commercie/filmpjes/regisseur-26/vloeiend.py` GOED; in het draaiende deel 1 gelijk beeld op 468, in de eindfilm 2 op 195); geluid_check GOED (gemiddeld -17,8 dB, piek -1,4 dB); 24 beelden op 1 per seconde plus het eerste groot en 2 eindbeelden groot bekeken.
- kanaal: yt-short
- soort: video
- product: click-joints-pro
- issue: #159
- bestand: `marketing/wachtrij/2026-11-28-yt-short-pro-sale-proces.mp4` (muziek 1, Dreamer). Muziekkeuze voor Thijs, elk de eerste 10 s van dezelfde film: `...-muziek1-10s.mp4` (Dreamer), `...-muziek2-10s.mp4` (Floating Cities), `...-muziek3-10s.mp4` (Lasting Hope). Kiest hij 2 of 3: `montage7.py` maakt de hele film met die muziek in een minuut.
- vorm: zoals het voorbeeld van Thijs (simonzhang.art): één doorlopende opname van de weergave, het model vult het beeld, de camera draait de hele tijd rustig rond (7 graden per seconde), geen knip en geen staptekst. In hetzelfde beeld verandert de robot: grijs met rig (0 s), Figure from rig met de delen in kleur (1,0 s), Exploded view (2,3 tot 3,6 s), grijs (4,2 s), knie buigt tot de stop van 120 graden (4,4 tot 5,4 s), voorbij de stop rood (6,0 s), deel voor deel kleur (7,6 tot 11,8 s), pose (12,5 tot 14,0 s). Eén vaste tekst bovenin tot 9 s: "Turning a rig into / a poseable figure:". Daarna 6,5 s Cycles-film met een camera die langzaam om de robot op de sokkel draait, hele figuur in beeld; saleregel pas de laatste 3 s.
- beeld: echte schermopname (Xvfb, ffmpeg x11grab) van Blender 5.3.0 met de interface en Click Joints Pro 1.2.8, workflow `regisseur-29` run 45874505707 (tak `regisseur-29-proef`), script `commercie/filmpjes/regisseur-29/proces7.py` en `verloop7.py`. De stappen zet het script in de echte Blender (geen muisklikken in beeld); Blender tekent alles zelf, niets is nagetekend. Montage lokaal met `montage7.py` van main, uitslag `pro-sale-proces-v7-montage.json`, metingen `film-run45874505707.json`.
- pose: de eerste kandidaat-pose zonder botsing (6 poses afgewezen omdat een onderarm in de romp kwam, pose 7 met 0 botsingen en 0 rode vlakken van Pro; GEZIEN in `film-run45874505707.json`). Zelf bekeken op 14,5 s en in de eindfilm: geen arm door het lijf.
- geluid: geen stem, geen zoem; alleen muziek met vrije licentie, zacht opbouwend
- slot: "Click Joints Pro / 25% off this week, / on Gumroad" in beeld, laatste 3 s
- plaatsen: alleen tussen vr 27 nov en di 1 dec, alleen als CYBER25 aanstaat (`bash platformen/blender/sale-controle.sh`), na keuring en nadat Thijs hem zag (issue #159)

## Titel
From rig to poseable figure in Blender 🤖 | Click Joints Pro

## Tekst
```
Rig in, poseable figure out. Click Figure from rig in Click Joints Pro: knees and elbows get a hinge that stops at the rotation limit of your rig, shoulders, hips and neck get a ball joint. Exploded view shows how the parts fit; past the end stop, red shows where parts would hit.

Print the Fit test strip first: every printer is different.
Click Joints Pro, 25% off this week (until Tuesday December 1, 23:59 CET):
https://duinhouwer8.gumroad.com/l/click-joints-pro/CYBER25?utm_source=yt&utm_medium=video

Music: "Dreamer" Kevin MacLeod (incompetech.com), licensed under Creative Commons: By Attribution 4.0, https://creativecommons.org/licenses/by/4.0/
```
(Kiest Thijs muziek 2 of 3: zet "Floating Cities" of "Lasting Hope" in de regel Music.)
