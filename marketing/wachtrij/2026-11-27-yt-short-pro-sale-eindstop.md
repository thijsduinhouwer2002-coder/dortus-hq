# Sale-Short Click Joints Pro: Knee bends too far? Give it an end stop from your rig 🦿 | Blender

- status: klaar om te plakken (Daan ja in #111, 25 nov 23:05)
- kanaal: yt-short
- soort: video
- product: click-joints-pro
- issue: #75
- bestand: `marketing/wachtrij/2026-11-27-yt-short-pro-sale-eindstop.mp4` (1080x1920, 30 beelden per seconde, stem Max van ElevenLabs). Contactblad: `commercie/filmpjes/regisseur-26/sale-eindstop-blad.jpg`
- controle (GEZIEN): ffprobe 30/1 zonder gaten of dubbele tijden (vloeiend.py GOED); synchroon GOED, 9 van 9 zinnen binnen 0,3 s (grootste verschil 0,17 s, `commercie/filmpjes/regisseur-26/sale-eindstop-synchroon.md`); geluid_check GOED (-17 dB gemiddeld, piek -1,4 dB, geen bed, alleen stem en zachte klikjes); ruim 40 beelden zelf bekeken
- v2 na feedback Thijs 25 nov 21:40 ("kan spectaculairder"): ingezoomd op de robot (echt scherm, 1,5x, menubalk zichtbaar), de rig en de echte klik op Figure from rig met het paneel eronder, het echte Exploded view met de gewrichten, labels "Right elbow 0–140°" en "Left knee 0–120°", en het rood dat verschijnt als je 135 typt voorbij de stop van 120
- beeld: echte schermopname van Blender 5.3.0 met Click Joints Pro 1.2.8 en de eigen robot (ffmpeg x11grab, 30 beelden per seconde, echte muis en klikken, de knie gebogen met de Bend-schuif); geen getekende stappen
- eerste beeld: `commercie/filmpjes/regisseur-26/eerste-beeld-eindstop-inzet.jpg` (robot groot, inzet uit de echte schermopname met de groene boog "Left knee 0-120°", "Knee bends too far?", "25% OFF THIS WEEK"); blinde test GESLAAGD (Gemini 1,0, ChatGPT 1,0, `organisatie/blindtest/uitslag/pro-sale-eindstop-2-2026-11-25-2023.md`). Reserve, ook GESLAAGD 1,0: `eerste-beeld-eindstop-scherm.jpg`. De eerste poging `eerste-beeld-eindstop.jpg` slaagde niet en wordt niet gebruikt.
- slot: "Click Joints Pro, 25% off this week, on Gumroad." in beeld en stem
- plaatsen: **vr 27 nov ochtend** (Daan K3: niet samen met een-knop op één ochtend). Alleen tussen vr 27 nov tot en met di 1 dec, en alleen als CYBER25 aanstaat (`bash platformen/blender/sale-controle.sh`); daarna niet meer gebruiken
- gemaakt_door: Regisseur run 29 en 30 (25 nov 2026)

## Titel
Knee bends too far? Give it an end stop from your rig 🦿 | Blender

## Tekst
```
Your rig already knows how far a knee may bend. Click Joints Pro uses that.
1. Click Figure from rig.
2. The knees get a hinge that stops at the rotation limit of your rig.
3. Bend it: it stops right at that angle. Past the stop, red shows where parts would hit.

Print the Fit test strip first: every printer is different.
Click Joints Pro, 25% off this week (until Tuesday December 1, 23:59 CET):
https://duinhouwer8.gumroad.com/l/click-joints-pro/CYBER25?utm_source=yt&utm_medium=video
```

## Voice-over (zin voor zin, Engels)
Zie `commercie/filmpjes/regisseur-26/sale-eindstop-stem.txt`. Hook: "Does your figure's knee bend way too far?"
