# Sale-Short Click Joints Pro (procesvorm v7b): From rig to poseable figure in Blender 🤖

- status: CONCEPT v7b, wacht op nakeuring Daan (M2 en M3 uit #217, nieuw issue "Keur: sale-Short v7b"). Eerste beeld gelijk aan v7 (set `pro-sale-proces-v7`): blinde test kon niet draaien (ChatGPT en Gemini zonder tegoed), dus nog NIET GESLAAGD; niet plaatsen voor dat geregeld is of de hoofdchat anders beslist.
- v7b tegen v7 (Daan #217): M2 de camera zoomt niet meer uit bij de pose, hij komt over de hele opname heel langzaam 8% dichterbij. M3 één open pose, in de weergave en in de Cycles-film dezelfde: rechterarm zwaait met de elleboog 135 graden gebogen, linkerarm zwaait mee naar achter (niets voor het lijf), stap met de rechterknie 48 graden gebogen, hoofd iets naar de camera. 0 botsingen (eigen check) en 0 rode vlakken van Pro, ook tijdens de overgang (GEZIEN, `film-run45894709013.json`). Oorzaak van "twee poses" in v7 gevonden: verborgen tussenstappen van het snijden renderden mee in Cycles; nu uit de render (`eind_fix.py`). K1 eindcamera draait 60 graden over een boog, hele figuur steeds in beeld.
- eigen controle: (GEZIEN, 26 nov ±22:45 NL): 22,1 s, 1080x1920, 30/1, 663 beelden, 0 gaten, 0 dubbele tijdstempels en 0 gelijke beelden in het draaiende deel 0 tot 15,5 s (`commercie/filmpjes/regisseur-26/vloeiend.py` GOED); geluid_check GOED voor de film (-17,8 dB, piek -1,4) en de 3 stukjes van 10 s (-18,7, -16,3, -17,1 dB); 22 beelden op 1 per seconde (`commercie/filmpjes/regisseur-29/v7b-strook.jpg`) plus het eerste beeld, 14,8 s en 20,5 s groot bekeken. Plus 5 beelden van de eindcamera los gecontroleerd: hele figuur steeds in beeld.
- kanaal: yt-short
- soort: video
- product: click-joints-pro
- issue: #159
- bestand: `marketing/wachtrij/2026-11-28-yt-short-pro-sale-proces.mp4` (muziek 1, Dreamer). Muziekkeuze voor Thijs, elk de eerste 10 s van dezelfde film: `...-muziek1-10s.mp4` (Dreamer), `...-muziek2-10s.mp4` (Floating Cities), `...-muziek3-10s.mp4` (Lasting Hope). Kiest hij 2 of 3: `montage7.py` maakt de hele film met die muziek in een minuut.
- vorm: zoals het voorbeeld van Thijs (simonzhang.art): één doorlopende opname van de weergave, het model vult het beeld, de camera draait de hele tijd rustig rond (7 graden per seconde), geen knip en geen staptekst. In hetzelfde beeld verandert de robot: grijs met rig (0 s), Figure from rig met de delen in kleur (1,0 s), Exploded view (2,3 tot 3,6 s), grijs (4,2 s), knie buigt tot de stop van 120 graden (4,4 tot 5,4 s), voorbij de stop rood (6,0 s), deel voor deel kleur (7,6 tot 11,8 s), pose: zwaaien en een stap (12,5 tot 14,0 s). Eén vaste tekst bovenin tot 9 s: "Turning a rig into / a poseable figure:". Daarna 6,5 s Cycles-film met een camera die langzaam om de robot op de sokkel draait, hele figuur in beeld; saleregel pas de laatste 3 s.
- beeld: echte schermopname (Xvfb, beeld voor beeld gepakt met mss) van Blender 5.3.0 met de interface en Click Joints Pro 1.2.8, workflow `regisseur-29`: opname run 45894709013, Cycles en montage run 45896469352 (tak `regisseur-29b`), script `commercie/filmpjes/regisseur-29/proces7.py` en `verloop7.py`. De stappen zet het script in de echte Blender (geen muisklikken in beeld); Blender tekent alles zelf, niets is nagetekend. Montage met `montage7.py`, metingen `film-run45894709013.json`.
- pose: vaste open pose `g_zwaai_achter_loop` uit `commercie/filmpjes/regisseur-29/poses7.py`, gekozen na proeven in Blender met Pro vanuit de hoeken van de weergavecamera en de eindcamera (variant met de vuist naar voren afgewezen: in de weergave hing hij voor de buik). 0 botsingen, 0 rood.
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
