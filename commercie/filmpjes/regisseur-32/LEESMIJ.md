# Regisseur 32: zoekvideo Click Cuts "split a model for 3D printing in Blender" (#332)

Liggend 1920x1080, doel 1:30 tot 2:00, stem Max (ElevenLabs, via de hoofdchat). Stand za 28 nov 2026 ±03:00 NL.

## Wat er is
- `cuts_lang.py`: echte opname. Blender 5.3.0 met de gewone interface (bovenbalk, werkruimtetabs, outliner, properties, tijdlijn) onder Xvfb 1920x1080, Click Cuts 1.1.0 van main, Horse Statue 01 (Poly Haven, CC0). Klok van precies 1/30 s per beeld, echte X-muis en kliks (XTest). Volgorde: draaien om het paard dat boven het bed (Bambu Lab A1, 256 mm) uitsteekt, N, printer kiezen, paard klikken, Split to fit, Draw cut over de hals met Flip side heen en terug, Cut piece, More settings, Make fit test, Exploded view, Export parts (STL), draaien. Mist een klik, dan staat dat in `film.json` onder `vangnet`.
  `xvfb-run -a --server-args="-screen 0 1920x1080x24 -noreset" blender --gpu-backend opengl -p 0 0 1920 1080 start.blend --python cuts_lang.py -- <map> click_cuts.zip <modelmap>` met `LIBGL_ALWAYS_SOFTWARE=1` en `CJ_PYLIB` (mss, python-xlib, numpy). Duurt ±25 min voor ±75 s film.
- `film-r1.json` en `opname-r1.log.gz` horen bij opname r1 (28 nov, 2075 beelden = 69,2 s, 1 vangnet: Exploded view). De ruwe opname zelf (62 MB) kon niet in een release (releases maken mag deze sessie niet, HTTP 403) en is te groot voor de repo: draai `cuts_lang.py` opnieuw, de uitkomst is gelijk (zelfde scène, zelfde klok). r1 zelf bekeken (GEZIEN): echte Draw cut met "comes off", fit test met 0.15 tot 0.30, 15 STL-bestanden geschreven.
- `voorlees.md`: 24 zinnen voor Max, met bron per zin. Wacht op de hoofdchat (`cuts-lang-elevenlabs.mp3`).
- `thumb.py`: thumbnail uit een echt beeld van de opname, kop in Poppins ExtraBold (OFL).

## Stem eerst, beeld volgt (run 28 nov ±02:30)
De voorleestekst duurt langer dan de oude opname (69 s tegen ±1:55 met stem, GOK). Knippen of vertragen zou haperen of de stem van het beeld losmaken. Daarom loopt het nu andersom, in één doorlopende opname:
1. `tijden_lang.py <stemmap>`: zinnen uit `voorlees.md`, per zin een wav (met `STEM_MP3=.../cuts-lang-elevenlabs.mp3` geknipt met `stem/splits.py`; zonder: Kokoro als proef, nooit voor keuring), vaste pauzes (0,45 s, 0,9 s voor een nieuw hoofdstuk). Uit `stem-lang.wav` en `tijden.json`.
2. `cuts_lang.py` met `CC_TIJDEN=<stemmap>/tijden.json`: elke klik wacht op zijn zin (N bij "Press N", Split to fit bij "Now click Split to fit", Flip side bij "Click Flip side", 0.20 bij "click the one that goes in by hand", Exploded view bij zin 21, Export bij zin 22). Lange wachttijd vult de hand met rustig doordraaien (middelste knop, hand terug, verder draaien). Te laat dan 0,4 s staat in `film.json` onder `laat`.
3. `monteer_lang.py <opnamemap> <stemmap> <uit.mp4>`: stem op t=0, echte muispijl uit muis.txt, grote ondertitels (Poppins ExtraBold) op de gemeten zinnen, geel hoofdstuklabel 2,8 s, zacht tikje bij elke echte klik, geen muziek of ondergrond. Schrijft ook `.srt` en `-hoofdstukken.txt`. `--controle <mp4> <stemmap>` laat whisper het begin van elke zin naluisteren (moet binnen 0,3 s). `--beeld` maakt één beeld.
Blender eenmalig zonder het welkomstvenster: `blender -b --factory-startup --python-expr "import bpy; bpy.ops.wm.save_userpref()"`.

Proef r3 (28 nov ±03:15, Kokoro am_michael als tijdelijke stem, NIET voor keuring, niet bewaard): 115,9 s, 3478 beelden op 30 bps, 0 afwijkende tijdstempels, geluid_check GOED (-18,2 dB, piek -1,3 dB), whisper-controle 24 van 24 zinnen binnen 0,3 s (grootste 0,09 s), 13 echte kliks, 15 STL-bestanden. Bijna gelijke beelden (mpdecimate) alleen bij het op gang komen en afremmen van de hand, hooguit 6 achter elkaar (0,2 s), niet midden in een beweging. Alles GEZIEN; strook `strook-proef-r3.jpg` (16 beelden).
Bekende punten: (a) Exploded view: de echte klik valt op het vinkje maar de eigenschap verandert niet, dus het script zet hem 1 beeld later (vangnet, zelfde beeld); nog uitzoeken. (b) Export parts valt ±2 s na "Then click Export parts" (scrollen), zin 16 de proef ±1,4 s laat in beeld.

Tweede run 28 nov ±03:20 tot 04:30 (gelijktijdig, zag pas bij het pushen dat het bovenstaande er al stond; eigen dubbele versie niet gepusht):
- (a) opgelost: Exploded view staat standaard AAN, dus de echte klik zette hem juist UIT. Met `CC_TIJDEN` begint hij nu uit (`opzet()`), en de klik bij zin 21 trekt de delen echt uit elkaar. Getoetst in een eigen proefopname met dezelfde stap (geschatte tijdlijn, 94,9 s, 2848 beelden op 1/30 s, 13 echte kliks, vangnet leeg, GEZIEN).
- Workflow `.github/workflows/regisseur-32.yml`: draait stap 1 tot 3 en de controles (ffprobe tijdstempels, geluid_check, `monteer_lang.py --controle`) vanzelf zodra `cuts-lang-elevenlabs.mp3` op main komt, en zet film, beelden en uitslagen in release `regisseur-32`. Dan hoeft de volgende run alleen na te kijken en Daan te vragen.

Derde run 28 nov ±04:20 (wacht nog steeds op de stem van Max):
- **Workflow zou zijn vastgelopen:** `cuts_lang.py` schreef de OCR-plaatjes naar een vaste map die alleen in onze eigen sessie bestaat (`/tmp/claude-0/w`), dus in GitHub Actions faalde de eerste knopzoektocht (bij "Bambu Lab A1 mini"). Nu in de opnamemap.
- (b) aangepakt: Make fit test op de stem sneller (4 tikjes per scroll, geen omweg langs de uitleg, klik op het eind van zin 15), Export parts wordt al in de pauze vóór zin 22 gezocht en geklikt 0,9 s na het begin van "Then click Export parts".
- Elke echte klik schrijft nu `kliksync` in `film.json` (welke zin, hoeveel s na het begin). De workflow zet dat in `kliksync.txt` en geeft rood bij een klik later dan 0,5 s na het eind van zijn zin of bij een vangnet.

## Nog te doen (volgende run, zodra `cuts-lang-elevenlabs.mp3` er is)
1. `STEM_MP3=.../cuts-lang-elevenlabs.mp3 python3 tijden_lang.py <stem>`, dan `cuts_lang.py` met `CC_TIJDEN` (±15 min), dan `monteer_lang.py`, dan `--controle`, geluid_check, ffprobe, beelden zelf bekijken. Komt Max boven 2:00: `PAUZE=0.35 HOOFDSTUK_PAUZE=0.7`.
2. Thumbnail is al GESLAAGD (`organisatie/blindtest/uitslag/click-cuts-zoek-split-2026-11-28-0150.md`, Gemini plek 2 en 2).
3. Keuring Daan, dan `marketing/wachtrij/` met datum na Click Cuts 1.1 live, melding in #317.

## Titel en beschrijving (concept)
Titel: `How to split a model for 3D printing in Blender (with pins that fit)`

Hoofdstukken volgen de voorleestekst; tijden pas na de montage.

Vierde run 28 nov ±08:30 (wacht nog op de stem van Max): de workflow liep in Actions nog nooit echt door (alleen overgeslagen zonder mp3). Nu met `workflow_dispatch` en `proef=1`: de hele keten met Kokoro als tijdelijke stem (am_michael, nooit voor keuring), uitkomst in release `regisseur-32-proef`. Zo vallen fouten nu al op en niet pas als de mp3 van Max er is.
