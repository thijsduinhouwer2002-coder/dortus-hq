# Strook een stap hoger en een gedempt palet (#333, Olaf 28 nov)

Waarom: blinde test minuut 0 (e0ed18c, 120 px) gaf plek 2,5 bij Gemini met "make the active gameplay area slightly taller and clearer"; de itch-omslag kreeg "cheap mobile game", "softer, less saturated". Rusty's strook is op hun scherm van 1080 ±300 px hoog (GEZIEN, hun eerste winkelbeeld), de onze was 120.

Wat er veranderde in het spel:
- Eerste start kiest 200 px op 100% Windows (schaal 5, was 120 en schaal 3) en 240 px vanaf 125% (schaal 6, was 160). Eerst 160 geprobeerd; de blinde test hieronder koos 200. Het menu Height heeft nu 96, 120, 160, 200 en 240. Wie al een hoogte koos, houdt die.
- `palet=zacht` (kern/palet.gd): de kleuren van de hele strook gedempt. Staat nog niet standaard aan; dat kiezen Sanne en Mila na de blinde test.

Beelden: zelfde zaad (11), zelfde moment (25 s, Gloop eet Mara), Godot 4.3 Linux onder Xvfb, `--write-movie --fixed-fps 5`, `vers=1 zaad=11 uitleg_klik=6 koper=1 koper_wacht=8 balk=0`, op het bureaublad van `ontwerp/steam/mila/speelscherm/maak_speelscherm.py`, ware maat 1920 x 1080 (GEZIEN):
- `minuut0-h120-ware-maat.png`: oud, ter vergelijking
- `minuut0-h160-ware-maat.png` en `minuut0-h160z-ware-maat.png`: nieuwe standaard, vol en zacht
- `minuut0-h200-ware-maat.png` en `minuut0-h200z-ware-maat.png`: 200 px, vol en zacht

Toetsen: 11 x 0 FOUT op Linux (GEZIEN). Films op 96 (zacht, bovenrand blijft doorzichtig), 120, 160, 200 en 240 zonder SCRIPT ERROR (GEZIEN).
Blinde test: set `organisatie/blindtest/sets/hats-speelscherm-minuut0-hoger.json`, uitslag volgt in `organisatie/blindtest/uitslag/`.

## Uitslag ronde 1 (Gemini, 28 nov 01:21, GEZIEN: `organisatie/blindtest/uitslag/hats-speelscherm-minuut0-hoger-2026-11-28-0121.md`)
| beeld | plekken | gemiddeld |
|---|---|---|
| 120 vol (oud) | 2, 2 | 2,0 GESLAAGD (op 27 nov 2,5: de rechter schommelt) |
| 160 vol | 2, 3 | 2,5 |
| 160 zacht | 3, 2 | 2,5 |
| 200 vol | 2, 2 | 2,0 GESLAAGD |
| 200 zacht | 2, 2 | 2,0 GESLAAGD |

Besluit Olaf: standaard 200 op 100%, want alleen de hoogte gaf hier geen enkele plek 3 en twee keer vroeg de rechter "larger" of "cramped" bij 160. Het verschil met 120 is binnen de ruis van één rechter met 2 rondes, daarom ronde 2: `minuut1-std-200-ware-maat.png` en `minuut1-stdz-200-ware-maat.png` (75 s, eerste start zonder gekozen hoogte, log `HOL eerste start dpi=95 hoogte=200`), set `hats-speelscherm-minuut1-200`.
