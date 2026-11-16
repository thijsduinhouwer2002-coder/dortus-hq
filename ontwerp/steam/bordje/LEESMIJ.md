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

## Wachtkaartje: de rij bij de ingang (Mila 16 nov ±16:55 UTC)
Voor Sanne's rij (`platformen/steam/voortgang.md`, Versie 3 definitief punt 5): staan er niveaus in de rij, dan hangt er onder de plank een papieren volgnummer zoals bij de bakker ("trek een nummertje"), met een rode punaise in het paaltje: **"+7"**. Het balkje staat dan vol, zoals Sanne vroeg. Is de rij leeg, dan is het kaartje weg.
- Model: `holbord.py`, standen `kaart1` (9 breed, plus en één cijfer), `kaart2` (13 breed, twee cijfers) en `k0` tot `k9` (donkere cijfers 3 x 5). Zelfde x = 0 en z = 0 als het bordje.
- Blad: `godot/kunst/3d/holkaart.png` (sprite `holkaart`, zelfde eenheid als `holbord` via `schaal_van`), 12 cellen.
- **Zo tekent het spel hem:** kaartcel links = bordcel links + (anker_x bord - anker_x kaart) / px spelpixels; boven = bordcel boven + (nul_y bord - nul_y kaart) spelpixels (nu -6,25 en +12,33). Cijfer `k<n>` op dezelfde plek als de kaartcel; bij twee cijfers de eenheden 4 spelpixels naar rechts. Wip bij het feestje: kaartje wipt mee. Komt er een niveau uit de rij binnen, dan telt het getal één omlaag tegelijk met het gewone feestje.
- Proefscript dat precies dit doet uit de twee bladen: `mila_proef_kaart.py`. GEZIEN met Read: `mila-kaartje-1x.png` (12 met +7, 16 met +10, 6 met +1, 9 zonder rij) en `mila-kaartje-4x.png`.

**Waarom zo:**
- Wachten in de rij = een volgnummer trekken: iedereen kent het, er zit een grinnik in, en het zegt meteen "er komt nog wat" zonder uitleg. Wachtende helden bij de boog tekenen kan niet: boven het gras is geen ruimte (de strook begint bij de vensterrand) en een held is 13 spelpixels hoog.
- Plusje in donkere inkt, niet rood: een rood plus op wit papier las als EHBO-kruis ("+7 leven").
- Room papier op donkere aarde springt eruit op ware grootte, maar is kleiner dan het bord en hangt eronder, dus het bord blijft de baas.
