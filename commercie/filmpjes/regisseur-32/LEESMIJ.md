# Regisseur 32: zoekvideo Click Cuts "split a model for 3D printing in Blender" (#332)

Liggend 1920x1080, doel 1:30 tot 2:00, stem Max (ElevenLabs, via de hoofdchat). Stand za 28 nov 2026 ±03:00 NL.

## Wat er is
- `cuts_lang.py`: echte opname. Blender 5.3.0 met de gewone interface (bovenbalk, werkruimtetabs, outliner, properties, tijdlijn) onder Xvfb 1920x1080, Click Cuts 1.1.0 van main, Horse Statue 01 (Poly Haven, CC0). Klok van precies 1/30 s per beeld, echte X-muis en kliks (XTest). Volgorde: draaien om het paard dat boven het bed (Bambu Lab A1, 256 mm) uitsteekt, N, printer kiezen, paard klikken, Split to fit, Draw cut over de hals met Flip side heen en terug, Cut piece, More settings, Make fit test, Exploded view, Export parts (STL), draaien. Mist een klik, dan staat dat in `film.json` onder `vangnet`.
  `xvfb-run -a --server-args="-screen 0 1920x1080x24 -noreset" blender --gpu-backend opengl -p 0 0 1920 1080 start.blend --python cuts_lang.py -- <map> click_cuts.zip <modelmap>` met `LIBGL_ALWAYS_SOFTWARE=1` en `CJ_PYLIB` (mss, python-xlib, numpy). Duurt ±25 min voor ±75 s film.
- `film-r1.json` en `opname-r1.log.gz` horen bij opname r1 (28 nov, 2075 beelden = 69,2 s, 1 vangnet: Exploded view). De ruwe opname zelf (62 MB) kon niet in een release (releases maken mag deze sessie niet, HTTP 403) en is te groot voor de repo: draai `cuts_lang.py` opnieuw, de uitkomst is gelijk (zelfde scène, zelfde klok). r1 zelf bekeken (GEZIEN): echte Draw cut met "comes off", fit test met 0.15 tot 0.30, 15 STL-bestanden geschreven.
- `voorlees.md`: 24 zinnen voor Max, met bron per zin. Wacht op de hoofdchat (`cuts-lang-elevenlabs.mp3`).
- `thumb.py`: thumbnail uit een echt beeld van de opname, kop in Poppins ExtraBold (OFL).

## Nog te doen (volgende run)
1. Montage zodra de mp3 er is: beeld per hoofdstuk op de gemeten zinnen (stem.py/splits.py met STEM_MP3), grote ondertitels, muispijl uit muis.txt, zachte klik bij elke klik in film.json, geen andere geluiden. Controle: ffprobe 30 bps gelijkmatig, geluid_check GOED, synchroon.py binnen 0,3 s.
2. Blinde test van de thumbnail (set `organisatie/blindtest/sets/click-cuts-zoek-split.json`).
3. Keuring Daan, dan `marketing/wachtrij/` met datum na Click Cuts 1.1 live, melding in #317.

## Titel en beschrijving (concept)
Titel: `How to split a model for 3D printing in Blender (with pins that fit)`

Hoofdstukken volgen de voorleestekst; tijden pas na de montage.
