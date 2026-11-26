# Bord rechts hoort nu bij het hol (Mila, 26 nov ±17:40 NL, issue #197)

**Waarom:** Iris (3fddb22 en bb298d3): "bord leest als los venster", groen met een gouden lijst, het grootste vlak dat niet bij het hol hoort. Rusty's Retirement heeft geen los paneel.

**Wat er voor de speler veranderde** (alleen de textuur `godot/kunst/paneel_hol.png`, geen code, geen nieuwe functie):
- Het bord is nu van planken in het hout van het hol (kamerhout uit `hol.py`), met smalle voegen, in een lijst van donkere ruwe balken zoals de stutten, vier ijzeren spijkers in de hoeken en een wal aarde onderaan.
- Geen groen lei, geen honingkleurige lijst en geen koperen hoeken meer: goud zit alleen nog in het muntje en de getallen.
- Brede planken: in het midden van het bord valt één voeg, tussen de twee regels tekst.
- Bron: `modellen/plankbord.py` (Blender uit code, zelfde 9-slice 384 px met rand 128 als het krijtbord, dus `kern/tekst.gd` bleef gelijk).

**Leesbaarheid (GEZIEN, gemeten op de beelden hieronder):**
- Hoofdletter G van de tweede regel: voor en na even hoog, 9 px op 96, 8 px op 120, 11 px op 160 (pixels lichter dan crème drempel; lettermaat en plek ongewijzigd, `tekst.gd` niet aangeraakt).
- Contrast crème tekst (f3e2c0) tegen het bord op 120: was 6,6 tegen het groen, nu 7,6 tegen het hout (WCAG-formule, mediaan van de achtergrond).

**Beelden (GEZIEN, Godot 4.3 Linux onder xvfb, `--write-movie --fixed-fps 5`, `vers=1 zaad=7 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=90`; voor = main 728a317, na = deze wijziging; rechter 700 px van de strook):**
- `voor-en-na-hoogte96-ware-grootte.png`, `-hoogte120-`, `-hoogte160-` (en `-2x.png`): boven voor, onder na, op 90 s.
- `kaartje-voor-en-na-hoogte120-*.png`: het hoge bord met kaartje en knop ("Big Gloop, Bought., Undo") op 83 s.
- `na-hoogte120-90s-hele-strook.png`: de hele strook na, ware grootte.
- `bord-textuur-384.png`: de textuur zelf.

**Toetsen:** 8 toetsen op Linux, geen FOUT, geen SCRIPT ERROR.
