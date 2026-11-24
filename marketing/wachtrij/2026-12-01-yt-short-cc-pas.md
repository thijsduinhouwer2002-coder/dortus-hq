# Click Cuts Short 2: Printed pins too tight or too loose? Do this first 🔥

- status: open (plaatsen pas als Click Cuts live is en de winkellink werkt)
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en printzin "Every printer is different: print the fit test first." (slot blijft Click Cuts, want de opdracht gaat over Click Joints Pro). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-20).
- nagekeken run 25 (GEZIEN, release regisseur-20, run 45430299554): lengte 40,3 s, geluid GOED (-16,5 dB), synchroon GOED 11 van 11 (0,18 s). Eerlijkheidszin en slotzin staan in beeld en stem.
- kanaal: youtube-short
- soort: video
- soort_reeks: lancering Click Cuts, script 2 van 6 (`commercie/filmpjes/scripts/click-cuts-lancering.md`, ja Daan na M1 en M2), hook 2A. Volgorde 1, 2, 3, 6, 4, 5: deze de dag na de lancering.
- product: click-cuts
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-20/cc-pas-geluid.mp4
- stem_tekst: `commercie/filmpjes/regisseur-20/cc-pas-stem.txt` (voor Max van de hoofdchat; tot die er is Kokoro)
- releasebestand (GEZIEN, workflow-run 45373870367 op de opname van run 45371800150): 41,9 s, 1080 x 1920; geluid_check GOED (-16,3 dB, piek -1,4 dB); synchroon GOED 11 van 11 (grootste 0,18 s, gemiddeld 0,129 s). 12 beelden bekeken, eerste groot: rode pennen naast de gekleurde stukken van de leeuw, kop "Pins never fit?", geen zwevende getallen. Kan beter: bij zin 6 (van boven) vallen de buitenste spelingen net buiten de uitsnede; de gegraveerde cijfers lezen in het lettertype van de add-on wat hoekig.
- metingen (film-tip.json, GEZIEN): Lion Head 320,5 x 206,4 x 436 mm, buiten beeld gesplitst op de A1 mini: 12 stukken alle groen, 68 pennen. Alle klikken met de echte muis via OCR, geen vangnet: More settings, scrollen naar stap 3, Make fit test (spelingen 0.15, 0.20, 0.25, 0.30; blok waterdicht; 4 pennen; blok 88 x 17,1 x 12 mm met pennen), klik 0.25 (JSON daarna A1MINI|PLA 0.25 naast A1MINI|PETG 0.3), Material via de keuzelijst naar PETG: speling 0.30, terug naar PLA: speling 0.25; Export fit test: fit_test_block.stl en fit_test_pins.stl.
- tijd: voorstel de dag na de lancering van Click Cuts (week van 30 nov, de hoofdchat kiest)
- doel: de winkellink van Click Cuts (eerste regel van de beschrijving, invullen na de uitgave)
- gemaakt_door: Regisseur run 19 (24 nov 2026); opname in workflow regisseur-20 (Blender 5.3.0, xvfb, echte muis, gedeelde hulpcode van Olaf)
- vorige: 2026-11-30-yt-short-cc-fit.md

## Titel
Printed pins too tight or too loose? Do this first 🔥 | Blender

## Tekst
```
<winkellink Click Cuts, invullen na de uitgave>

Printed pins too tight or too loose? Print the fit test first.
1. Open More settings, step 3, and press Make fit test.
2. You get a small block with four holes, each with its own clearance engraved next to it, plus four pins.
3. Print it, try your pin, and click the clearance that fits.
4. Click Cuts remembers it for that printer and filament.

Every printer is different: print the fit test first. That is why you print this first.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Script en regels:** `commercie/filmpjes/scripts/click-cuts-lancering.md` nr. 2 (geen prijs, geen print-belofte, geen klik of magneten). Daan keurde de scripts. Zin 2 ("Every printer and filament prints a hole a little different") is een algemene waarheid, geen meting van ons (zie de noot bij script 2).
- **Twee zinnen erbij** (anders te kort): "So open More settings, and go to step three: pins and numbers." bron `producten/blender-splitser/split_joints/paneel.py` r. 63, 114 en 119 (fit test staat in stap 3 "Pins and numbers" onder More settings). "Press Make fit test. It uses your own pin size from the panel." bron `passingproef.py` r. 153 en 186 (blok en pennen met `inst.pen_mm` en `inst.pen_lengte_mm`). "Plus four pins" bron `passing.py` AANTAL = 4 en `passingproef.py` r. 186. Graag meekeuren.
- **Vier spelingen 0.15 tot 0.30:** `passing.py` `spelingen()` (een stap van 0,05 mm onder de ingestelde 0,20, de ingestelde, twee erboven), gegraveerd voor elk gat (`maten`, nummers richting -Y).
- **Klik op de speling en onthouden:** `passingproef.py` r. 216 tot 228 (This one fits: bewaren per printer en materiaal), r. 281 (regel "Saved for this printer: N mm").
- **Komt vanzelf terug:** `eigenschappen.py` (printer en materiaal hebben `update=_onthouden`), `passingproef.py` r. 82 `pas_toe`. In de opname is PETG 0,30 mm vooraf bewaard (buiten beeld in de voorkeuren gezet, zoals na een eerdere fit test); de kijker ziet de wissel naar PETG (0,30) en terug naar PLA (0,25).
- **Model:** Lion Head, Poly Haven, CC0 (DERDEN: https://polyhaven.com/a/lion_head), buiten beeld gesplitst op de A1 mini, alleen in de hook en zin 2.
- **Stem:** tijdelijk Kokoro-82M, af_heart, Apache 2.0 (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). ElevenLabs-opname (Max) gevraagd: `cc-pas-elevenlabs.mp3` in `commercie/filmpjes/regisseur-20/`.
- **Nieuw onderwerp:** geen Short over een fit test of speling bewaren in de laatste 14 dagen (wachtrij en RSS nagekeken 24 nov, GEZIEN). tip-speling (gratis Click Joints, wand en speling van één gewricht) is een ander product en een andere les.

## Keuring
- keurder: Iris, 24 nov 2026 ±12:00 UTC (opdracht hoofdchat 11:50), `marketing/keuring/2026-11-24-yt-short-cc-fit-pas-nummers-iris.md`
- beeld en plezier: akkoord ja; eerste beeld sterk (rode pennen, "Pins never fit?"); Moet geen
- kan: gegraveerde spelingen op het blok slecht leesbaar (Cavity aan zoals regisseur-21); ondertitel niet over de paneeltekst bij stap 1 en 2.
- plaatsen pas als Click Cuts live is.

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
