# Voorleestekst zoekvideo Click Cuts (#332), voor ElevenLabs "Max - Witty Commercial Actor"

Regisseur, za 28 nov 2026. Hoofdchat: lees deze 24 zinnen in deze volgorde voor, één opname, gewone pauze tussen de zinnen (±0,4 s), en zet hem als `commercie/filmpjes/regisseur-32/cuts-lang-elevenlabs.mp3`. Daarna bouw ik met STEM_MP3. Rustig en duidelijk, uitleggend, geen reclamestem: dit is een zoekvideo, geen advertentie. Geschatte lengte 1:35 tot 1:50 (GOK, ±150 woorden per minuut).

Elke zin is waar voor Click Cuts 1.1.0 (bron per zin hieronder, uit `producten/blender-splitser/winkel/docs.md`, gekeurd Daan #169 en #254, en de code op main).

## Zinnen (Engels, letterlijk zo voorlezen)

**0:00 The short answer**
1. Need to split a model for 3D printing in Blender?
2. Here's the short answer: cut it into parts that fit your printer bed, and put pins in every cut so the parts line up again.
3. I'll show you with Click Cuts, an add-on for Blender.

**Pick your printer and split**
4. Press N and open the Click Cuts tab.
5. Pick your printer. Not in the list? Type your own bed size.
6. Click your model. The panel shows its name and how many faces it has.
7. Now click Split to fit.
8. It plans the cuts, cuts the model into parts that fit your bed, adds pins and pin holes, and engraves a part number on the cut faces.
9. The result box tells you how many parts you got, and how many pins.

**Draw your own cut**
10. Want a cut somewhere else, like through the neck?
11. Click the part, click Draw cut, and drag a line across it.
12. The part that comes off lights up white. Wrong side? Click Flip side.
13. Click Cut piece, and it gets pins and numbers, just like the other cuts.

**Pins that fit your printer**
14. Pins only work if the holes fit your printer.
15. So open More settings and click Make fit test.
16. You get a small block with four holes, each with its clearance engraved in front of it, plus four pins.
17. Print the Fit test strip first: every printer is different.
18. Push a pin into every hole, and click the one that goes in by hand and doesn't wobble.
19. Click Cuts remembers that clearance for this printer and material.

**Check and export**
20. Step four lists every part. Green means it fits the bed, it's watertight, and it has enough wall around its holes.
21. Exploded view pulls the parts apart, so you can look at every cut.
22. Then click Export parts: one STL file per part, in millimeters, and each part is laid flat on a cut face if it fits.

**Where to get it**
23. Click Cuts works in Blender 4.2 and newer.
24. The link is in the description.

## Bron per zin
| Zin | Bron |
|---|---|
| 2, 8 | docs.md "Your first split" stap 3: plans the cuts, parts that fit your bed, adds pins and pin holes, engraves a part number on the cut faces |
| 4 | docs.md "Open the panel: in the 3D viewport press N and open the Click Cuts tab" |
| 5 | docs.md stap 1, Custom size met bed size in mm |
| 6 | docs.md stap 2 ("Statue: 500 faces") |
| 9 | docs.md stap 3, resultaatvak "8 parts, all fit the bed", "12 pins, 0.20 mm clearance" |
| 10 tot 13 | docs.md "Choose where it cuts: Draw cut" stap 1 tot 4 |
| 15, 16 | docs.md "Print the fit test first" stap 1 en 2 (Make fit test zit in More settings, stap 3) |
| 17 | vaste zin uit de opdracht (CLAUDE.md regel 5) |
| 18, 19 | docs.md stap 4 en "Click Cuts remembers that clearance for this printer and material" |
| 20 | docs.md "4 Check and export": green: fits the bed, watertight, enough wall around its holes |
| 21 | eigenschappen.py "Exploded view": "Show the pieces a little apart, only in the viewport" |
| 22 | docs.md stap 4 (one file per part, millimeters) en "Lay parts flat" (on by default, a cut face on the bed if it still fits) |
| 23 | blender_manifest.toml `blender_version_min = "4.2.0"` |

Bewust niet: geen "it clicks", niets over printen door ons, geen prijs, geen AI.
