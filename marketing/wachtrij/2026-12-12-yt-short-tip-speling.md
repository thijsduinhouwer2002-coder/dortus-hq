# Tip-reeks 13: Your ball joint gap, measured, not guessed 🔥

- status: wacht (workflow regisseur-18 neemt op; de Regisseur kijkt het releasebestand na en zet dan pas open)
- kanaal: yt-short
- soort: video
- soort_reeks: tip uit de gratis Click Joints (script week 51 nr. 6, hook 6A, `commercie/filmpjes/scripts/week-51-click-joints.md`, ja Daan; gratis tip nr. 2 in `scripts/volgorde-stem.md`). Eindigt op de gratis eindkaart, geen Pro-reclame.
- product: click-joints (gratis)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-18/tip-speling-geluid.mp4 (nog niet nagekeken)
- stem_tekst: `commercie/filmpjes/regisseur-18/tip-speling-stem.txt` (voor de ElevenLabs-stem Max van de hoofdchat; tot die er is Kokoro)
- geluid_check, lengte, synchroon, beelden: nog niet (volgende run). Lengte GOK ±50 s (138 woorden; tip-dubbel 117 woorden gaf 43,4 s, GEZIEN).
- metingen (lokale proef met de echte muis, Blender 5.3.0, gratis zip van main, 24 nov, GEZIEN): cilinder 80 mm hoog, r 14 mm; Place joint met de echte klik: Good fit, wand 4,015 mm, speling ingesteld 0,2 mm, gemeten 0,1996 mm; paneel toont "Good fit", "Wall: 4.01 mm", "Clearance: 0.20 mm (measured)" (GEZIEN, schermbeeld van de proef).
- tijd: voorstel 2026-12-12T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur run 17 (24 nov 2026); opname in workflow regisseur-18 (Blender 5.3.0, xvfb, echte muis, gedeelde hulpcode van Olaf)
- vorige:

## Titel
Your ball joint gap, measured, not guessed 🔥 | Blender tip

## Tekst
```
You set 0.2 mm. Is the gap after the cut really 0.2 mm?
1. Select your part and put the 3D cursor where the joint goes.
2. Click Joints panel: Ball, Clearance 0.2, Place joint.
3. Step 3 of the panel shows Clearance (measured) and the wall in mm. Here: 0.20 mm and 4.01 mm.

Not sure which gap your printer likes? Print a fit test first.
Measured in Blender, not print tested by us yet.
Click Joints is free on Blender Extensions. More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Hook (eerste 1,5 s):** "Is your gap really what you set?", kop "Really 0.2 mm?", beeld: kogel uit de kom met Exploded view (echte Blender, einde van de opname). Geen productnaam. Het antwoord in de video is eerlijk "yes, 0.20": het gaat om controleren (script, Let op).
- **Gemeten na de snede, gemiddelde rond de kogel:** code gratis deel `producten/blender-gewrichten/click_joints/gewricht.py` r. 303 tot 310 (`passing.meet_speling` tussen deel A en B, gemiddelde als `cj_speling_gemeten_mm`), alleen bij een kogel (GEZIEN). Eerder gemeten in de echte Blender: 0,1996 mm gemiddeld over 1.521 punten (`platformen/blender/logboek.md` r. 49, GEZIEN).
- **Wall in het paneel:** `paneel.py` r. 99 tot 102 ("Wall: N mm", "Clearance: N mm (measured)") (GEZIEN). Zin 2 is de voorzichtige versie uit het script ("check that the real gap matches"), want het paneel toont echt 0.20.
- **In de gratis versie:** de paneelregel staat in de gratis code (niet in `betaald/`), sinds de eerste versies (`platformen/blender/logboek.md` r. 163). Click Joints is live op Blender Extensions (`organisatie/bord.md`, GEZIEN).
- **Fit test:** "Print a fit test first" verwijst naar een testgewricht in het algemeen; de Fit test strip zelf is Pro 1.2.0 (`platformen/blender/pro-1.2.0.md`) en wordt in deze gratis tip niet beloofd.
- **Wat het voor een print betekent:** niet geclaimd; alleen "Measured in Blender, not print tested by us yet."
- **Model:** eigen cilinder, in het script gemaakt. Geen modellicentie nodig.
- **Stem:** tijdelijk Kokoro-82M, af_heart, Apache 2.0, commercieel gebruik toegestaan (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). ElevenLabs-opname (Max) gevraagd aan de hoofdchat: `tip-speling-elevenlabs.mp3` in `commercie/filmpjes/regisseur-18/`.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen over speling meten (wachtrij en YouTube-RSS nagekeken 24 nov, GEZIEN; Sanne liep het ook na voor week 51). Verwant aan fit-hook (Fit test strip), maar ander probleem en de gratis versie.

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
