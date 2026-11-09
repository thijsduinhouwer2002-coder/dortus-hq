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
