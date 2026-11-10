# Kunst Het Hol (Daan)

Alles hier wordt gemaakt door `ontwerp/steam/kunst-bron/maak_kunst.py` (pixel voor pixel in code, geen beeldgenerator). Pas de PNG's niet met de hand aan: zeg het Daan, of pas het script aan en draai het opnieuw.

**Maat (besluit Daan, 9 nov):** pixel art, cellen van 16 x 16 spelpixels, **schaal 3** bij een strook van 120 tot 160 px (100% Windows), schaal 2 onder 120 px, bij 150% en 200% Windows schaal 4 en 6. Altijd hele schaal, filter nearest (Project Settings, Rendering, Textures, Default Texture Filter: Nearest). Strook 120 px = 40 spelpixels = maaiveld 8 + twee rijen cellen. Meer hoogte toont meer aarde eronder.

Waarom schaal 3: op schaal 2 worden de figuren 28 schermpixels hoog en zie je geen gezichten meer; Rusty's Retirement zit ook op ±3 (GEZIEN, hun winkelplaatje 1). Karakter gaat voor een extra rij.

Framematen, volgorde en ankers staan in `kunst.json`. Kort:
- `tegels.png`: rij 0 aarde (8 varianten), rij 1 gang (16 varianten, index = n*1 + e*2 + s*4 + w*8, bit 1 = die buur is aarde).
- `gras.png` en `maaiveld.png`: 16 x 8, de bovenkant van de strook.
- Held = `held_lijf.png` (4 loopframes) + een hoed uit `held_hoeden.png` + een wapen uit `held_wapens.png`, allemaal 16 x 16 op hetzelfde anker. Zo maak je veel helden uit weinig plaatjes, en hoeden zijn later skins.
- `slijm.png`, `schat.png`, `stekelput.png`, `fakkel.png`, `ingang.png`, `versiering.png`, `gloed.png`.
- Beweging spaarzaam: fakkel en schat alleen als ze in beeld zijn, slijm wiebelt 3 fps. Past bij de regel van Olaf: alleen tekenen als er iets gebeurt.

Voorbeeld op ware grootte: `ontwerp/steam/kunst-bron/voorbeeld-strook.png`, vergelijking met Rusty's Retirement: `vergelijk-rusty.png`.

## Karakter-laag (Daan, 9 nov 19:45 UTC)
Gemaakt door `ontwerp/steam/kunst-bron/maak_karakter.py` (draait na maak_kunst.py, zelfde palet). Wensen van Sanne (19:05) en de keuring van Olafs build 408d67b. Alles staat met maten in `kunst.json`.
- `held_lijf_kleuren.png`: zelfde 4 loopframes in 5 tuniekkleuren (rij 0 rood = held_lijf.png). Kies de rij vast per held (zaad = naam): zo herken je Kees als hij terugkomt.
- `held_littekens.png`: pleister, ooglap, schram, verband (mitella). Losse laag tussen lijf en hoed. Bezoek 2 een litteken, bezoek 3 twee, aartsvijand drie. Vervangt de rode streepjes in `held.gd`.
- `held_hoeden_hap.png`: dezelfde vier hoeden met een hap eruit, voor wie door Gloop gebeten is.
- `tekens.png` (8 x 8): boos, uitroep, zweet, zzz, ster. Vervangt de losse pixels boven het hoofd in `held.gd`.
- `slijm_leven.png`: slapen (2), spugen (4, laars vliegt eruit), hap (3), plat (1), opstaan (1). **Plat is een eigen frame: schaal de slijm nooit in y**, dat maakt halve pixels (zie de film van 408d67b: Gloop wordt een vage veeg).
- `laars.png`: de laars die Gloop uitspuugt, ligt daarna even op de vloer.
- `paneel.png` (9-slice, rand 4): houten bordje met gouden spijkers voor de melding rechts in de strook, in plaats van het zwarte vlak. `naamkaartje.png` (9-slice, rand 3): goud, voor aartsvijanden. `trofee.png`: bord voor de wand van aartsvijanden, hoed erop.
Voorbeeld: `ontwerp/steam/kunst-bron/voorbeeld-karakter.png`, paneel voor en na op de echte build: `paneel-voor-na.png`.

## Aarde met lagen (Daan, 9 nov, run 58)
Gemaakt door `ontwerp/steam/kunst-bron/maak_aarde.py` (draai `maak_karakter.py`, die draait alles; `maak_kunst.py` alleen schrijft kunst.json opnieuw zonder de nieuwe bladen).
- `aarde_lagen.png`: 3 rijen (bovenste rij met graswortels, tweede rij, dieper) van 8 varianten. Vervangt rij 0 van `tegels.png`: kies de rij op diepte. Elke laag iets donkerder, met een golvende laaglijn die naadloos doorloopt en een gedithterde overgang.
- `vondsten.png`: helm, zwaard, botten, fossiel, pot. Over ongeveer 1 op 10 aardecellen, weg als je graaft.
Voorbeeld: `ontwerp/steam/kunst-bron/voorbeeld-aarde.png` (ware grootte, 3 rijen = strook van 160 px).

## Stijl van Mila (9 nov 2026)
- Aarde en holwand zijn **pruim** in plaats van bruin (palet in `ontwerp/steam/kunst-bron/maak_kunst.py` en `maak_aarde.py`). Zelfde bladen, zelfde maten. Harde bruine kleuren in code: holwand donker `#1d1426`, aarde `#3f2846`.
- **Gloop heeft één oog**, een scheve grijns en één tand, in alle frames van `slijm.png` en `slijm_leven.png`. Het oog kijkt naar rechts; naar links = het frame spiegelen.
- Komt eraan: Gloops hoedentoren (zie `ontwerp/steam/mila/stijl.md`, bouw Bram in `slijm.gd`).
- `poef.png` (4 beelden van 12 x 10, Mila 10 nov): het boze wolkje knapt als een held met een wrok in een val valt. Midden van het wolkje op (6, 3), dus teken het op de plek van het oude wolkje min 2 px in x. 10 fps, één keer. Bron `ontwerp/steam/mila/bron/poef.py`.
- `held_soort.png` (Mila 10 nov): kleding per heldensoort, laag over het lijf. 4 loopframes x 4 rijen in de volgorde van `heldensoort.gd` SOORTEN (ridder, dief, magier, bard), 16 x 16, zelfde anker en frame als `held_lijf_kleuren.png`. Tekenen direct na het lijf, vóór littekens en hoed. Ridder: harnas met tabbert in zijn eigen tuniekkleur. Dief: masker met knoop achter en een buidel op de rug. Magier: baard en een mantel tot de voeten. Bard: luit op de rug. Ridder, dief en bard houden hun tuniekkleur, dus een terugkomer blijft herkenbaar. Bron `ontwerp/steam/mila/bron/held_soort.py`, voorbeeld `ontwerp/steam/mila/held-soorten-3x.png`.
