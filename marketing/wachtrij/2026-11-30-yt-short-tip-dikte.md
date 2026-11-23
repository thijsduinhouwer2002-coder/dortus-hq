# Tip-reeks 3: Paper thin model? Give it real walls in Blender 🏺

- status: rood
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL, voorbeeld Thijs: BlenderSecrets)
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-4/tip-dikte.mp4
- stem_tekst: `commercie/filmpjes/regisseur-4/tip-dikte-stem.txt` (voor de ElevenLabs-stem van de hoofdchat)
- geluid_check: GOED op het releasebestand (gemiddeld -16,5 en -16,4 dB, piek -1,4 dB), zelf gedraaid 23 nov ±21:35 NL (GEZIEN); ook in CI
- lengte: 0:44,0, staand 1080x1920 (ffprobe op het releasebestand, GEZIEN; sha256 klopt met SHA256SUMS.txt)
- tijd: voorstel 2026-11-30T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur, workflow regisseur-4 (run 45247413525)
- vorige:

## Titel
Paper thin model? Give it real walls in Blender 🏺

## Tekst
```
Is your model just one paper thin surface? A wall with zero thickness has nothing to print. Fix it in Blender with one modifier:
1. Modifier properties > Add Modifier > Generate > Solidify.
2. Click the Thickness field, type 2, Enter: a 2 mm wall all the way around.
3. Offset -1 keeps the wall on the inside, so the outside keeps its size.
4. Even Thickness keeps the wall the same on sharp corners.

Measured in Blender, not print tested by us yet.
Screen recording in Blender 5.3 (no add-on used). Voice: AI text to speech (Kokoro, Apache 2.0).
More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```
Komt er een ElevenLabs-stem, dan wordt de stemregel: "Voice: AI text to speech (ElevenLabs, elevenlabs.io)".

## Eerste reactie
(leeg)

## Bronnen
- **Hook (eerste 1,5 s):** "Is your model just one paper thin surface?" vanaf beeld 1, kop "Paper thin?", beeld: de vaas met wand die uitzoomt (beweging vanaf beeld 1). Geen productnaam, geen zwevende getallen.
- **Elke stap staat echt in beeld:** Add Modifier, Generate en Solidify met de echte muis geklikt (OCR-plekken `c_knop`, `c_sub`, `c_item` in `film-tip.json`, `c_via_menu` true, geen vangnet), Thickness echt getypt (`c_dikte_ui` 2.0 mm). Lokaal GEZIEN: breedte 82,0 x 82,0 mm voor en na (`c_maat_voor`, `c_maat_na`), dus de buitenkant blijft gelijk; hoogte 140,0 naar 141,4 mm (de bodem groeit mee). Daarom zegt de Short "the outside keeps its size" alleen over de zijkant in beeld.
- **Beweringen:** Offset en Even Thickness: Blender-handleiding (DERDEN: https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/solidify.html): "Offset: A value between (-1 to 1) to locate the solidified output inside or outside the original mesh. The inside and outside is determined by the face normals." en "Even Thickness: Maintain thickness by adjusting for sharp corners." De normalen van onze vaas wijzen naar buiten (draaiprofiel in `tip_opname.py`).
- **Model:** eigen vaas uit `commercie/filmpjes/regisseur-4/tip_opname.py` (`vaas()`). Geen modellicentie nodig.
- **Stem:** Kokoro-82M, af_heart, Apache 2.0 (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M).
- **Synchroon (lokaal, zelfde code):** synchroon2.py met faster-whisper small.en: GOED, 11 van 11 zinnen binnen 0,3 s (GEZIEN).
- **Zelf bekeken (Read, GEZIEN):** eerste beeld en 10 tot 12 beelden per Short. Hersteld na kijken: camera op de vaasrand (eerst de buitenkant, nu de rand van boven zodat voor en na het verschil te zien is), kaders op Offset en Even Thickness, hook van het ei dichterbij, uitsnede stap 1 met Edit Mode, Shorts verlengd van 36 en 37 s naar 44 s.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen over wanddikte of een platte onderkant (GEZIEN, wachtrij en RSS 23 nov).
- **Releasebestand nagekeken (23 nov ±21:35 NL, GEZIEN):** run 45247413525 geslaagd; metingen in `film-tip.json` gelijk aan de lokale opname (menu echt geraakt, dikte 2,0 mm, breedte 82,0 mm voor en na, 193 punten, voet 28,8 mm, geen vangnet); synchroon in CI GOED (11 van 11); eerste beeld op 540 breed en 10 beelden van het releasebestand zelf bekeken.
- **Kan beter:** bij tip-dikte valt het kader op Offset iets te laag (raakt de regel Even Thickness); de tekst in het Properties-paneel is klein op een telefoon.

## Keuring
- keurder: Roep-Keurder, 23 nov 2026 ±20:50 NL
- 1 bron klopt: ja (getallen en stappen staan in beeld; bronnen in het concept)
- 2 geen AI-zin, geen AI-melding: nee, de tekst bevat "Voice: AI text to speech (Kokoro, Apache 2.0)"; geen AI in titel of beschrijving toegestaan
- 3 geen medische claim: ja
- 4 geen Hats-spelerstekst: ja
- 5 echt beeld zelf bekeken, -geluid.mp4 en geluid_check GOED: nee, bestand heet tip-*.mp4 en eindigt niet op -geluid.mp4 (geluid_check wel GOED -16,4 dB); echt Blender-beeld wel bekeken (4 beelden en tegel)
- 6 geen persoonsgegevens: ja
- 7 past bij het kanaal: ja
- 8 niet gelijk aan een post van de laatste 14 dagen: ja
- 9 geen AI-beeld, AI-stem of AI-persoon: nee voor de tekst (AI-vermelding); beeld echt, stem Kokoro mag volgens de uitzondering van 23 nov
- 10 schrijft als Dortus, niet als Thijs: ja
- techniek-check: oranje-regels: Short (alleen uit de reserve, hoofdchat beslist); geen Gumroad, geen < of >, eerste reactie leeg; media bereikbaar (GET 206)
- uitkomst: rood
- reden: De beschrijving noemt de AI-stem ("Voice: AI text to speech"), dat mag niet volgens REGELS (Thijs 23 nov 20:28), en het bestand eindigt niet op -geluid.mp4; nieuw bestand met schone tekst en een -geluid.mp4 nodig.

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
