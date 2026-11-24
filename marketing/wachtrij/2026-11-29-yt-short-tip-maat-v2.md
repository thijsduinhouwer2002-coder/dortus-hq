# Tip-reeks 2: Will your model fit your printer? Check it first 📏

- status: open
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en slotzin in beeld en stem "Make your prints poseable: Click Joints Pro, on Gumroad." (opdracht hoofdchat 24 nov 16:05). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-7).
- nagekeken run 25 (GEZIEN, release regisseur-7, run 45430412786): lengte 46,5 s, geluid GOED (-18,1 dB), synchroon whisper 7 van 9 (zin 8 en 9 niet herkend), met RMS nagemeten 9 van 9: stem zin 8 op 35,9 s bij scène 35,77, zin 9 op 40,7 bij 40,57; beelden 36,5 en 41,5 s bekeken. Eerlijkheidszin en slotzin staan in beeld en stem.
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL, voorbeeld Thijs: BlenderSecrets)
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-7/tip-maat-geluid.mp4
- geluid_check: GOED (gemiddeld -18,1 dB, piek -1,1 dB), zelf gedraaid op het releasebestand 23 nov ±22:08 NL (GEZIEN); ook in CI
- lengte: 0:46,5, staand 1080x1920 (ffprobe op het releasebestand, GEZIEN)
- tijd: voorstel 2026-11-29T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur, workflow regisseur-7 (run 45263884196)
- vorige: 2026-11-29-yt-short-tip-maat.md

## Titel
Will your model fit your printer? Check it first 📏

## Tekst
```
Is your model too big for your printer? Check it in Blender before you slice:
1. Scene properties > Units: Unit Scale 0.001, Length Millimeters.
2. Press N. Under Dimensions you see the real size (here 310 mm tall).
3. Compare with your print bed (here a box of 220 x 220 x 250 mm).
4. Hover over the view, press S, type 0.7, Enter: now 217 mm tall, and it fits.

Every printer is different: print a small test first.
Screen recording in Blender 5.3 (no add-on used).
More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Versie 2 (Regisseur run 6, 23 nov ±22:00 NL):** Stem nu ElevenLabs Max (opname hoofdchat, `stem/splits.py`); geen stem- of AI-regel meer in de beschrijving; bestand eindigt op -geluid.mp4; uitsneden verbeterd: bij STEP 1 waren de labels van Units afgesneden, bij STEP 2 en IT FITS viel het getal ("310 mm", "217 mm") rechts half weg. Nu staan Unit Scale 0.001, Length Millimeters en de hele Dimensions-kolom in beeld. Synchroon in CI: GOED, 9 van 9 zinnen binnen 0,3 s, grootste 0,18 s (GEZIEN, `synchroon-tip-maat.md` in release regisseur-7). Zelf bekeken (Read, GEZIEN): eerste beeld en 6 beelden (Units, schalen, 217 mm) van het releasebestand van regisseur-7, plus de tegel van 12 beelden van regisseur-5.
- **Hook (eerste 1,5 s):** "Is your model too big for your printer?" gesproken vanaf beeld 1, kop "Too big to print?", beeld: de pion in de draaddoos van het printbed, camera draait (beweging vanaf beeld 1). Geen productnaam, geen zwevende getallen (de maten komen pas in stap 2, in het N-paneel van Blender zelf).
- **Elke stap staat echt in beeld (GEZIEN in de opname):** Properties, tab Scene, paneel Units met een echte klik opengeklapt (Unit Scale 0.001000, Length Millimeters), N-paneel met Dimensions 162 x 162 x 310 mm, S 0.7 Enter met echte toetsen (geen vangnet: hoogte na 217,0 mm, `b_hoogte_na` in `film-tip.json`), Scale 0.700 en Dimensions 113 x 113 x 217 mm.
- **Bed 220 x 220 x 250 mm:** een voorbeeldmaat, in beeld een draaddoos van precies die maat (`bed()` in `tip_opname.py`). We noemen geen printermerk. 310 x 0,7 = 217 mm (rekensom, GEZIEN in het N-paneel).
- **Model:** eigen schaakpion uit `commercie/filmpjes/regisseur-3/tip_opname.py`. Geen modellicentie nodig.
- **Stem:** ElevenLabs, stem "Max - Witty Commercial Actor" (Voice Library), model Eleven v4, opname van de hoofdchat in het account van Thijs (`commercie/filmpjes/regisseur-3/stem/tip-maat-elevenlabs.mp3`, besluit Thijs 23 nov). **Licentie, let op:** het gratis plan is volgens ElevenLabs "Personal use, attribution"; een commerciele licentie zonder naamsvermelding begint bij Starter (DERDEN: https://elevenlabs.io/pricing, gelezen 23 nov ±22:00 NL). Thijs wil geen stemregel in de beschrijving, dus voor plaatsen is Starter of een ja van Thijs op dit risico nodig (gemeld aan de hoofdchat). Valt dat weg: de Kokoro-versie kan met dezelfde workflow (zonder mp3).
- **Synchroon (lokaal, zelfde code):** synchroon2.py met faster-whisper small.en: GOED, 9 van 9 zinnen binnen 0,3 s, grootste verschil 0,183 s (GEZIEN). Transcript gelijk aan het script ("0.001", "310 millimeters", "220 by 220 by 250", "0.7", "217mm").
- **Zelf bekeken (Read, GEZIEN):** eerste beeld op 540 breed en 22 beelden. Hersteld na kijken: venstertitel (geen add-on), uitsnede Units (velden vielen half weg, nu heel), uitsnede Dimensions (de getallen vielen rechts weg tijdens de zoom, nu één vaste uitsnede).
- **Kan beter:** in de Units-scène is de tekst klein op een telefoon (uitsnede 1500 breed); in het N-paneel valt de "m" van "mm" net weg rechts.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen ging over maat en printbed (GEZIEN, wachtrij en `commercie/geplaatst.md`).
- **Releasebestand nagekeken (23 nov ±18:52 NL, GEZIEN):** run 45227517215 geslaagd; zelfde delen en metingen als de lokale opname (menu echt geraakt, randen 22 naar 0, hoogte 310 naar 217 mm); synchroon in CI GOED (9 van 9, grootste 0,183 s); eerste beeld op 540 breed en 6 beelden van het releasebestand zelf bekeken, gelijk aan de lokale bouw.

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
