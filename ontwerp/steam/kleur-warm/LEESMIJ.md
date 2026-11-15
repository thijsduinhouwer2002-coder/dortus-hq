# Warmer en lichter (punt 1 van de hoofdchat, 15 nov 13:30)

Daan, 15 nov ±13:05 UTC. Bron: `strook-120.png` van Windows-run 43712736230 (echte build), alleen de paarse tinten (tint 0,70 tot 0,99) verschoven; Gloop, goud, gras, helden en de laars blijven zoals ze zijn. Het is een kleurproef op het plaatje, geen render.

- `proef1-nu-B-C-D.png`: grijsbruin tot zandsteen. Te flets; helden verdwijnen bij C en D.
- `proef2-nu-E-F-G.png`: E terracotta, F roze-mauve, G oker-bruin. Frisse kijker (Agent, blind): nu 5/4/6, E 8/5/7, F 6/7/5, G 7/6/8 (warm / licht / figuren). F valt af (figuren zakken weg).
- `voorstel-H-nu-boven.png`: **mijn keus**, tussen E en G in en lichter: warme aarde zoals Rusty's Retirement, Gloop (mint) springt eruit omdat warm en mint tegenover elkaar staan.

## Doelkleuren voor `hol.py` (eigenaar Mila)
Zelfde omzetting op de materialen. Licht in de render maakt het anders; meet op de strook, niet op de hex.

| materiaal | nu | doel H |
|---|---|---|
| PRUIM donker | 35203c | 684033 |
| PRUIM licht | 4e3158 | 8e5949 |
| PRUIM_L (achterwand) | 5e3d68 | a26a58 |
| PRUIM_D | 2a1832 | 5a3227 |
| STEEN (kiezels) | 7a5d86 | c69383 |
| SCHACHT_WAND | 4a2d55 | 8a5342 |
| VLOER | 8a5a8e | d0947c |
| KAMERWAND | 7a4a78 | b88168 |
| RAND_P | 3a2a40 | 6e4e44 |

Let op: de gang moet een trede van de aarde blijven verschillen (ronde 6b), en het hout van ladder en stutten (6e4632, 8a4b2a) moet tegen bruine aarde nog los staan; zo nodig hout iets donkerder of roder. Het kaartje rechts (UI) is paars en gaat mee naar warm donkerbruin met de gouden rand (Olaf/Bram, `strook.gd`).
