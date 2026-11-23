# Tip-reeks 2: Will your model fit your printer? Check it first 📏

- status: rood
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL, voorbeeld Thijs: BlenderSecrets)
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-3/tip-maat.mp4
- geluid_check: GOED (gemiddeld -16,4 dB, piek -1,3 dB), zelf gedraaid op het releasebestand 23 nov ±18:52 NL (GEZIEN); ook in CI (`geluid_check.txt` in release regisseur-3)
- lengte: 0:46,4, staand 1080x1920 (ffprobe op het releasebestand, GEZIEN; sha256 klopt met SHA256SUMS.txt)
- tijd: voorstel 2026-11-29T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur, workflow regisseur-3 (run 45227517215)
- vorige:

## Titel
Will your model fit your printer? Check it first 📏

## Tekst
```
Is your model too big for your printer? Check it in Blender before you slice:
1. Scene properties > Units: Unit Scale 0.001, Length Millimeters.
2. Press N. Under Dimensions you see the real size (here 310 mm tall).
3. Compare with your print bed (here a box of 220 x 220 x 250 mm).
4. Hover over the view, press S, type 0.7, Enter: now 217 mm tall, and it fits.

Measured in Blender, not print tested by us yet.
Screen recording in Blender 5.3 (no add-on used). Voice: AI text to speech (Kokoro, Apache 2.0).
More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Hook (eerste 1,5 s):** "Is your model too big for your printer?" gesproken vanaf beeld 1, kop "Too big to print?", beeld: de pion in de draaddoos van het printbed, camera draait (beweging vanaf beeld 1). Geen productnaam, geen zwevende getallen (de maten komen pas in stap 2, in het N-paneel van Blender zelf).
- **Elke stap staat echt in beeld (GEZIEN in de opname):** Properties, tab Scene, paneel Units met een echte klik opengeklapt (Unit Scale 0.001000, Length Millimeters), N-paneel met Dimensions 162 x 162 x 310 mm, S 0.7 Enter met echte toetsen (geen vangnet: hoogte na 217,0 mm, `b_hoogte_na` in `film-tip.json`), Scale 0.700 en Dimensions 113 x 113 x 217 mm.
- **Bed 220 x 220 x 250 mm:** een voorbeeldmaat, in beeld een draaddoos van precies die maat (`bed()` in `tip_opname.py`). We noemen geen printermerk. 310 x 0,7 = 217 mm (rekensom, GEZIEN in het N-paneel).
- **Model:** eigen schaakpion uit `commercie/filmpjes/regisseur-3/tip_opname.py`. Geen modellicentie nodig.
- **Stem:** Kokoro-82M, af_heart, Apache 2.0 (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). Geen ElevenLabs.
- **Synchroon (lokaal, zelfde code):** synchroon2.py met faster-whisper small.en: GOED, 9 van 9 zinnen binnen 0,3 s, grootste verschil 0,183 s (GEZIEN). Transcript gelijk aan het script ("0.001", "310 millimeters", "220 by 220 by 250", "0.7", "217mm").
- **Zelf bekeken (Read, GEZIEN):** eerste beeld op 540 breed en 22 beelden. Hersteld na kijken: venstertitel (geen add-on), uitsnede Units (velden vielen half weg, nu heel), uitsnede Dimensions (de getallen vielen rechts weg tijdens de zoom, nu één vaste uitsnede).
- **Kan beter:** in de Units-scène is de tekst klein op een telefoon (uitsnede 1500 breed); in het N-paneel valt de "m" van "mm" net weg rechts.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen ging over maat en printbed (GEZIEN, wachtrij en `commercie/geplaatst.md`).
- **Releasebestand nagekeken (23 nov ±18:52 NL, GEZIEN):** run 45227517215 geslaagd; zelfde delen en metingen als de lokale opname (menu echt geraakt, randen 22 naar 0, hoogte 310 naar 217 mm); synchroon in CI GOED (9 van 9, grootste 0,183 s); eerste beeld op 540 breed en 6 beelden van het releasebestand zelf bekeken, gelijk aan de lokale bouw.

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
