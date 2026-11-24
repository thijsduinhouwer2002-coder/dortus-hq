# Tip-reeks 3: Paper thin model? Give it real walls in Blender 🏺

- status: open
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en slotzin in beeld en stem "Make your prints poseable: Click Joints Pro, on Gumroad." (opdracht hoofdchat 24 nov 16:05). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-7).
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL, voorbeeld Thijs: BlenderSecrets)
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-7/tip-dikte-geluid.mp4
- stem_tekst: `commercie/filmpjes/regisseur-4/tip-dikte-stem.txt` (voor de ElevenLabs-stem van de hoofdchat)
- geluid_check: GOED (gemiddeld -16,4 dB, piek -1,4 dB), zelf gedraaid op het releasebestand 23 nov ±21:50 NL (GEZIEN); ook in CI
- lengte: 0:44,0, staand 1080x1920 (ffprobe op het releasebestand, GEZIEN)
- tijd: voorstel 2026-11-30T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur, workflow regisseur-5 (run 45253184605)
- vorige: 2026-11-30-yt-short-tip-dikte.md

## Titel
Paper thin model? Give it real walls in Blender 🏺

## Tekst
```
Is your model just one paper thin surface? A wall with zero thickness has nothing to print. Fix it in Blender with one modifier:
1. Modifier properties > Add Modifier > Generate > Solidify.
2. Click the Thickness field, type 2, Enter: a 2 mm wall all the way around.
3. Offset -1 keeps the wall on the inside, so the outside keeps its size.
4. Even Thickness keeps the wall the same on sharp corners.

Every printer is different: print a small test first.
Screen recording in Blender 5.3 (no add-on used).
More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Versie 2 (Regisseur run 6, 23 nov ±22:00 NL):** Geen stem- of AI-regel meer in de beschrijving (rood van de Roep-Keurder); bestand eindigt op -geluid.mp4. Beeld gelijk aan versie 1 (opnieuw gemonteerd uit dezelfde opname). Synchroon in CI: GOED, 11 van 11 zinnen binnen 0,3 s, grootste 0,203 s (GEZIEN, `synchroon-tip-dikte.md` in release regisseur-5). Zelf bekeken (Read, GEZIEN): tegel van 11 beelden van het releasebestand (hook, Solidify-menu, Thickness 2 mm, Offset, Even Thickness, eindkaart).
- **Hook (eerste 1,5 s):** "Is your model just one paper thin surface?" vanaf beeld 1, kop "Paper thin?", beeld: de vaas met wand die uitzoomt (beweging vanaf beeld 1). Geen productnaam, geen zwevende getallen.
- **Elke stap staat echt in beeld:** Add Modifier, Generate en Solidify met de echte muis geklikt (OCR-plekken `c_knop`, `c_sub`, `c_item` in `film-tip.json`, `c_via_menu` true, geen vangnet), Thickness echt getypt (`c_dikte_ui` 2.0 mm). Lokaal GEZIEN: breedte 82,0 x 82,0 mm voor en na (`c_maat_voor`, `c_maat_na`), dus de buitenkant blijft gelijk; hoogte 140,0 naar 141,4 mm (de bodem groeit mee). Daarom zegt de Short "the outside keeps its size" alleen over de zijkant in beeld.
- **Beweringen:** Offset en Even Thickness: Blender-handleiding (DERDEN: https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/solidify.html): "Offset: A value between (-1 to 1) to locate the solidified output inside or outside the original mesh. The inside and outside is determined by the face normals." en "Even Thickness: Maintain thickness by adjusting for sharp corners." De normalen van onze vaas wijzen naar buiten (draaiprofiel in `tip_opname.py`).
- **Model:** eigen vaas uit `commercie/filmpjes/regisseur-4/tip_opname.py` (`vaas()`). Geen modellicentie nodig.
- **Stem:** Kokoro-82M, af_heart, Apache 2.0, commercieel gebruik toegestaan (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). Tijdelijke stem tot de ElevenLabs-opname er is (voorleestekst `commercie/filmpjes/regisseur-4/tip-dikte-stem.txt`).
- **Synchroon (lokaal, zelfde code):** synchroon2.py met faster-whisper small.en: GOED, 11 van 11 zinnen binnen 0,3 s (GEZIEN).
- **Zelf bekeken (Read, GEZIEN):** eerste beeld en 10 tot 12 beelden per Short. Hersteld na kijken: camera op de vaasrand (eerst de buitenkant, nu de rand van boven zodat voor en na het verschil te zien is), kaders op Offset en Even Thickness, hook van het ei dichterbij, uitsnede stap 1 met Edit Mode, Shorts verlengd van 36 en 37 s naar 44 s.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen over wanddikte of een platte onderkant (GEZIEN, wachtrij en RSS 23 nov).
- **Releasebestand nagekeken (23 nov ±21:35 NL, GEZIEN):** run 45247413525 geslaagd; metingen in `film-tip.json` gelijk aan de lokale opname (menu echt geraakt, dikte 2,0 mm, breedte 82,0 mm voor en na, 193 punten, voet 28,8 mm, geen vangnet); synchroon in CI GOED (11 van 11); eerste beeld op 540 breed en 10 beelden van het releasebestand zelf bekeken.
- **Kan beter:** bij tip-dikte valt het kader op Offset iets te laag (raakt de regel Even Thickness); de tekst in het Properties-paneel is klein op een telefoon.

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
