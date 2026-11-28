# Panelen en knoppen afgewerkt (#333 punt c, Olaf 28 nov)

Waarom: de blinde tests van 27 en 28 nov zeiden "UI looks too plain", "UI elements ... crisper and more cohesive", "less like a hacked-together desktop window" (GEZIEN, `organisatie/blindtest/uitslag/hats-speelscherm-minuut1-200-2026-11-28-0132.md`). Op 200 px was het kaartje een klein regeltje in een groot leeg bord (letter 15 en 18 zoals op 160) en het uitlegbordje een donkere pil met een rand van 1 px.

Wat er veranderde in het spel (geen nieuwe functies):
- **Knop** (`kern/tekst_kaart.gd`): de pil staat op een donkere onderlip (±1/10 van de knophoogte), glans en lip rekenen mee met de knop; "Buy" heeft nu een muntje vóór de prijs, net als "Undo +45". Op alle hoogtes.
- **Kaartje op 200 en 240 px**: groeit mee met de strook, 1,25 keer de maat van 160 (kop 23, uitleg 19, knop 35 hoog op 200; was 18, 15, 28). Uitleg wordt kleiner als hij niet past, nooit afgeknipt. Op 160, 120 en 96 even groot als eerst; het dichte bord houdt zijn maat.
- **Uitlegbordje** ("Click the dirt to dig.", "Click Gloop to grow him."): donkere buitenrand, gouden rand die meegroeit (2 px op 200, was 1), donkere onderlip, glansstrook, letter met schaduw, meer ruimte rond de tekst. Pijl met een rand die meegroeit.
- **Tekstschaduw** op het bord vanaf 200 px 2 px diep (was 1, viel weg op schaal 5).
- `kern/tekst.gd` was 480 regels: knop en kaartje staan nu in `kern/tekst_kaart.gd` (tekst.gd 410).

Beelden (GEZIEN, Godot 4.3 Linux onder Xvfb, `--write-movie --fixed-fps 5`, `hoogte=200 vers=1 uitleg_klik=6 koper=1 koper_wacht=8 balk=0`):
- `kaartje-200-voor-na-2x.png`: boven main (ca6f928), onder nu, zaad 12 op 73 s.
- `kaartje-200-160-120-2x.png`: het kaartje op 200, 160 en 120 px.
- `uitlegbordje-voor-na-160-120-2x.png`: 200 voor, 200 na, 160 na, 120 na.
- `minuut1-200-plaat-ware-maat.png` (75 s) en `minuut1-200-kaartje-ware-maat.png` (78 s): zaad 11, op het bureaublad van `ontwerp/steam/mila/speelscherm/maak_speelscherm.py`, voor de blinde test.

Toetsen: 11 x 0 FOUT op Linux. Films op 200 (100 s), 160 en 120 (80 s): 0 SCRIPT ERROR (GEZIEN).
Blinde test: set `organisatie/blindtest/sets/hats-speelscherm-ui-af.json`, met het oude beeld van 01:32 als controle in dezelfde run.

Wat ik zie (Read op 1x en 2x): het kaartje leest op 200 als een winkelkaart met een echte knop in plaats van kleine tekst in een plank; het uitlegbordje hoort nu bij het houten bord. Nog leeg: de onderste plank van het kaartje onder de knop, en links van het hol (x 0 tot 240) alleen aarde.
