# Videobeeld lange Pro-video (issue #94 stap 3, Beeldmaker, 26 nov 2026)

Waarom: de lange YouTube-video `4-3l3MZZWPc` ("Blender rig to 3D printable figure", ook de video op Superhive) toont als videobeeld een grijs MakeHuman-figuur in het Blender-scherm (etalage-audit S6, score 4). Dit is een eigen videobeeld van 1280x720, zoals YouTube het wil.

**Wat je ziet:** links het figuur zoals je het aanlevert (half doorzichtig, met de 20 botten van de rig in blauw), een gouden pijl met "1 click", rechts de 10 delen die de echte knop Figure from rig van Pro maakte, iets uit elkaar. Titel "Rig in. Parts out.", regel "Rigged figure to printable parts in Blender", en "9 joints" (4 scharnieren, 5 kogels; GEZIEN in `beelden/videobeeld.json`, `gewrichten`). Dat past bij wat de video laat zien: hetzelfde figuur, dezelfde knop, 9 gewrichten.

**Figuur:** MakeHuman base mesh (CC0 1.0, `commercie/filmpjes/studio/modellen/makehuman-base-LICENTIE.md`), aangekleed door `commercie/filmpjes/studio/figuur_laden.py` (CJ_HALS=rond). Geen AI-beeld, geen foto van een print: alles is een render.

**Maken:**
1. Render in GitHub Actions: workflow `.github/workflows/pro-videobeeld.yml` (Blender 5.3.0, Cycles 64 samples, 2400x1350, Pro-zip van main als 1.2.8, `ontwerp/pro-galerij/bron/galerij.py` modus klik met `HB_FIGUUR=mens`). Uit: release `pro-videobeeld-1` (`render-klik.png`, `klik.json`, `klik.log`). Inputs: `shift` (HB_SHIFT) en `vul` (HB_VUL).
   - `videobeeld-*`: shift -0.19, vul 0.74 (push-run 45737405744).
   - Proef v2: shift -0.25, vul 0.80 (dispatch-run 45738175511): de rechterhand viel buiten beeld, niet gebruikt.
2. Tekst erop: `python3 bron/videobeeld.py <render-klik.png> <klik.json> beelden <fontmap met Bricolage.ttf en Inter.ttf> ../click-joints/bron/icoon.svg [naam]`. Letters: Bricolage Grotesque en Inter (OFL, google/fonts).

**Blinde test:** set `organisatie/blindtest/sets/click-joints-pro-videobeeld.json`, tegen de YouTube-videobeelden van Cleave (`q48XFwmtp-I`), Split 3D Print (`l3I08ctCQkk`) en CatPin (`KVPY63W0ovg`), alle drie gevonden met curl op YouTube en Superhive op 26 nov.

**Plaatsen:** alleen de hoofdchat (YouTube). Bij de video `4-3l3MZZWPc`: Details, Thumbnail, Upload file, `beelden/videobeeld-1280x720.jpg`.
