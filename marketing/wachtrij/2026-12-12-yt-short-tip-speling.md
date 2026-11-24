# Tip-reeks 13: Your ball joint gap, measured, not guessed 🔥

- status: open
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en slotzin in beeld en stem "Click Joints is free. Want more? Click Joints Pro, on Gumroad." (opdracht hoofdchat 24 nov 16:05). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-18).
- nagekeken run 25 (GEZIEN, release regisseur-18, run 45430299174): lengte 46,8 s, geluid GOED (-16,7 dB), synchroon GOED 12 van 12 (0,187 s); 5 beelden bekeken. Eerlijkheidszin en slotzin staan in beeld en stem.
- kanaal: yt-short
- soort: video
- soort_reeks: tip uit de gratis Click Joints (script week 51 nr. 6, hook 6A, `commercie/filmpjes/scripts/week-51-click-joints.md`, ja Daan; gratis tip nr. 2 in `scripts/volgorde-stem.md`). Eindigt op de gratis eindkaart, geen Pro-reclame.
- product: click-joints (gratis)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-18/tip-speling-geluid.mp4 (nagekeken 24 nov run 18)
- stem_tekst: `commercie/filmpjes/regisseur-18/tip-speling-stem.txt` (voor de ElevenLabs-stem Max van de hoofdchat; tot die er is Kokoro)
- lengte: 46,8 s, 1080 x 1920 (GEZIEN, lengtes.txt release regisseur-18)
- geluid_check: GOED, gemiddeld -16,6 dB, piek -1,4 dB (GEZIEN)
- synchroon: whisper zegt 11 van 12 (zin 10 -0,44 s), maar dat is een meetfout: whisper plakt "first." aan "The"; RMS zelf nagemeten: stem van zin 10 begint op 33,70 s (sprong 60 naar 78 dB), scène op 33,60 s, verschil 0,10 s. Dus 12 van 12 binnen 0,3 s, grootste 0,18 s (GEZIEN).
- metingen release (film-tip.json, GEZIEN): passing groen, wand 4,015 mm, speling gemeten 0,1996 mm, uit_elkaar true, alle OCR-plekken gevonden, geen vangnet.
- beelden: 13 bekeken, eerste groot: kogel uit de kom met de 30°-boog van Blender, kop "Really 0.2 mm?", geen zwevende getallen. Paneel met "Clearance: 0.20 mm (measured)" en "Wall: 4.01 mm" leesbaar in zin 6 en 7 (GEZIEN). Kan beter: in zin 4 en 7 loopt de ondertitel over een paneelregel ("3 Fit and export", "Show bend range"), wel leesbaar.
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
Every printer is different: print a small test first.
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
- **Wat het voor een print betekent:** niet geclaimd; alleen "Every printer is different: print a small test first."
- **Model:** eigen cilinder, in het script gemaakt. Geen modellicentie nodig.
- **Stem:** tijdelijk Kokoro-82M, af_heart, Apache 2.0, commercieel gebruik toegestaan (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). ElevenLabs-opname (Max) gevraagd aan de hoofdchat: `tip-speling-elevenlabs.mp3` in `commercie/filmpjes/regisseur-18/`.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen over speling meten (wachtrij en YouTube-RSS nagekeken 24 nov, GEZIEN; Sanne liep het ook na voor week 51). Verwant aan fit-hook (Fit test strip), maar ander probleem en de gratis versie.

## Keuring
- keurder: Iris, 24 nov 2026 ±16:50 UTC, `marketing/keuring/2026-11-24-yt-short-cc-fit-na-botnamen-enkels-speling-es-iris.md`
- beeld en plezier: akkoord **ja**, Moet geen
- Kan: eerste beeld dichter op bal en kom; ondertitels niet over de paneelregels; Diameter 5.0 en later 17.0 (Auto) kan verwarren.

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
