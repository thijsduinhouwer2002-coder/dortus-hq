# Bordje met het hol-niveau (Mila, 16 nov 2026)

Plaats en maat van Daan (keus A: plankje op een paaltje links naast de stenen boog, in het gras; zijn platte schets staat in `bord-voorstel-3x.png`). Dit is de 3D-versie in hetzelfde hout als het pijlbordje.

## Wat er is
- Model: `producten/steam-hol/modellen/holbord.py`. Zelfde hout (`hout`, `hout_d`), paal, camera en licht als het pijlbordje in `versiering.py`. Plank 13 x 11 spelpixels met een donkere lijst van 1 spelpixel, een licht houten vlak, twee spijkertjes bovenin, paaltje eronder.
- Blad: `godot/kunst/3d/holbord.png` (sprite `holbord` in `pijplijn/sprites.json`), 11 cellen van 15 x 18 spelpixels (px 4), allemaal dezelfde schaal en hetzelfde nulpunt:
  - `leeg`: plank met paal, zonder cijfer;
  - `c0` tot `c9`: één room cijfer (`fbf2c0`, blokjes van 4 x 6, iets uit het vlak) met een donkere geschilderde schaduw rechtsonder. Een cijfer staat in zijn cel al precies op de plek waar hij op de plank hoort als het enige cijfer.

## Zo tekent het spel hem (voor Olaf)
1. Cel `leeg` met de bovenkant van de plank op de vensterrand (bovenkant strook), plank links op spelpixel 4 (net als Daans voorstel).
2. Het getal in **dezelfde** plek als cel `leeg`: één cijfer zonder verschuiving; twee cijfers: tientallen 2,5 spelpixels naar links, eenheden 2,5 naar rechts (tot niveau 50 zijn het er nooit meer dan twee).
3. Het balkje op de onderste rij van de lijst: rij 11 van de cel (vanaf de bovenkant), 1 spelpixel hoog, x van 5,5 spelpixels links tot 5,5 rechts van het midden van de cel. Leeg donkerbruin (`4e281c`), vol goud `ffe07a`, van links naar rechts.
4. Wip bij het feestje: alles samen (plank, cijfers, balkje) 2 spelpixels omhoog en terug.
Proefscript dat precies dit doet: `mila_proef.py` (hier ernaast).

## Gezien
`mila-3d-bord-1x.png` (ware grootte op strook 120, niveau 5 met 40%, 12 vol, 47 met 70%, 9 tijdens de wip) en `mila-3d-bord-4x.png`. GEZIEN met Read: 5, 12 en 47 lezen op ware grootte, het bordje hoort zichtbaar bij het pijlbordje rechts, het gouden balkje valt op in de donkere lijst. Achtergrond: `strook-120.png` van `schermen/steam-hol/main` (16 nov 15:27).

## Waarom zo
- Room cijfer met donkere schaduw in plaats van goud: goud viel weg op het oranje hout (Daan), room leest zoals de pijl.
- Cijfers als losse cellen en niet 50 hele bordjes: 11 kleine cellen (12 kB) in plaats van 50, en elk niveau tot 99 werkt.
- Blokjescijfers: op 3 schermpixels per spelpixel blijft een blokjesvorm scherp; een gewoon lettertype werd op 4 x 6 een vlek.
