# Kamers boven de gang: één brede kamer in plaats van drie ogen (Daan, 13 nov 2026)

Hoort bij moet 3 van mijn keuring van het hol in 3D (`platformen/steam/taken.md`, antwoord aan Olaf 19:35).

## Wat er mis is in het spel nu
`spel-nu-main-c1a35ed-160px-2x.png` (Windows-run 43496125769, main c1a35ed, strook 160 px, 2x): elke gegraven cel in de bovenste rij krijgt een eigen ovale kom (`kamer_links` of `kamer_rechts` om en om, `hol_3d.gd` regel 63), elk met een fakkel rechtsboven. Die vlam leest als pupil: drie gegraven cellen naast elkaar worden drie ogen. Frisse kijker: "drie losse eieren met dezelfde fakkel, een stempel", cijfer 4.

## Voorstel
Vier stukken in plaats van twee, gekozen op de buren in de bovenste rij:

| buren gegraven | stuk |
|---|---|
| links nee, rechts nee | `kamer_los`: losse grot, warm lila licht van binnen, twee lichtgevende zwammen op de vloer (geen fakkel hoog) |
| links nee, rechts ja | `kamer_begin`: rond einde links, fakkel laag op de wand |
| links ja, rechts ja | `kamer_midden_a` en `kamer_midden_b` om en om (op kolomnummer even/oneven): a een houten stut met twee schoren, b een houweel en een tonnetje |
| links ja, rechts nee | `kamer_eind`: rond einde rechts, kistje |

Het midden is recht en egaal belicht (een lamp die naar achteren kijkt over de hele kamer, dus de voorkant van de aarde krijgt geen eigen vlek). Daardoor past het midden naadloos, hoe lang de kamer ook wordt.

Beelden:
- `tegels2-ware-grootte-3x.png`: rij 1 zoals het spel nu legt, rij 2 drie cellen (begin, midden, eind) en een losse, rij 3 vijf cellen en een losse. Op ware grootte (120 px strook) en 3x vergroot zonder vervagen. `tegels2-ware-grootte.png` is echt ware grootte, `tegels2-groot.png` de render zelf.
- `hol-oud-boven-nieuw-onder.png`: het hele hol, boven `hol.py` nu, onder dit voorstel (Gloop en helden verborgen, zoals in de pijplijn).

Frisse kijker ronde 1 (eerste versie): nu 4, voorstel 7. Zijn punten (stutten mechanisch en als doelpalen, naden in het plafond, grot te donker) zitten in ronde 2: stut met schoren om en om met houweel en ton, licht van binnen, grot warm lila.

## Hoe gemaakt
`hol_kamers_proef.py` is een kopie van Mila's `producten/steam-hol/modellen/hol.py` (13 nov 19:46) met alleen het stuk kamers, de kiezels om de kamers, de fakkels en vloer in de kamers en twee lampen anders. `hol.py` zelf is niet veranderd. Brede kamer in kolom 2 tot 4 (begin, midden, eind), losse in kolom 11. `HOL_MIDDEN=a` of `b` kiest het middenstuk.

    HOL_VERBERG='["gloop","held"]' HOL_MIDDEN=a python3.13 hol_kamers_proef.py /abs/pad/n7a.png 960 160 16 2 2
    HOL_VERBERG='["gloop","held"]' HOL_MIDDEN=b python3.13 hol_kamers_proef.py /abs/pad/n7b.png 960 160 16 2 2
    python3 maak_tegels_proef.py <oud.png> n7a.png tegels2.png n7b.png

(1 spelpixel = 4 px in de render, kolom = 64 px, bovenste rij van y 32 tot 96.)

## Wie wat doet (voorstel, ieder beslist in zijn eigen bestand)
1. **Mila** (`hol.py`): neem de kamers over zoals hier, of beter. Midden a en b moeten in één render naast elkaar kunnen staan; kan ook met een vijfde kolom of twee renders zoals ik deed.
2. **Bram** (`pijplijn/sprites.json`): stukken `kamer_los`, `kamer_begin`, `kamer_midden_a`, `kamer_midden_b`, `kamer_eind` in plaats van `kamer_links` en `kamer_rechts`.
3. **Olaf** (`hol_3d.gd`, `stuk()`): kies het stuk op `h.boven[k - 1]` en `h.boven[k + 1]` (de schacht en de schatkamer tellen als niet gegraven), midden a of b op `k % 2`.

## Nog open (kan, niet moet)
- De strook aarde boven de kamer is in het voorstel een tint donkerder dan de herhalende aardtegel uit kolom 13 (die heeft een eigen lamp). Dat is hetzelfde als moet 1 (licht stopt op celranden): de aarde moet overal hetzelfde licht krijgen. Mila.
- Het hout van stut en kistje mag een tint donkerder en minder oranje.
