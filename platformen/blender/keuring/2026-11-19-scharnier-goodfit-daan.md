# Keuring "No joint yet" bij scharnier (Click Joints Pro), 19 nov 2026, Daan
Wat ik keurde: commit ca36d53 (`betaald/scharnier.py`, 3 regels) en de e2e-run op main daarna, run 44503804192 (groen, alle 24 stappen, schermen op tak `schermen` met RUN.txt = ca36d53). Plaatjes zelf bekeken.
Akkoord: ja scharnier Good fit op ca36d53

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Na "Place hinge" krijgen beide delen `cj_passing = "groen"`. `paneel.py` r.90 leest precies die sleutel en toont dan `passing.fit_tekst("groen")` = "Good fit"; zonder die sleutel "No joint yet" (r.112). De fout uit de film had dus precies deze oorzaak. | feit (code) | hoog | |
| 2 | Hetzelfde pad is al zichtbaar in `17-figuur-heel-paneel.png` van deze run: scharnierdeel `held_B` (gemaakt via figuur.py, die al groen zette) toont onder "3 Fit and export" een vinkje met "Good fit", en onder Hinge "Bends 0° to 135°". Zo ziet stap 3 er nu ook uit na het losse Place hinge. | feit (GEZIEN) | hoog | |
| 3 | Een scherm van het losse "Place hinge" met paneel bestaat niet: 11, 12, 13 en 14 zijn alleen de 3D-weergave (bijgesneden, geen paneel). Het directe bewijs komt pas met een nieuwe film of een paneelscherm. | feit (lijst van de map op tak schermen) | hoog | paneelscherm na Place hinge |
| 4 | Randgeval: heeft een deel al een kogelgewricht met Tight (oranje), dan zet een scharnier erop het deel op groen en verdwijnt de waarschuwing over de dunne wand. Zeldzaam, maar dan zegt het paneel iets wat niet klopt. | vermoeden (code overschrijft zonder te kijken) | midden | toets: eerst kogel met Tight, dan scharnier op hetzelfde deel |
| 5 | "Een scharnier bestaat alleen bij Good fit": `scharnier.py` r.137 roept `neus.maten_neus` aan en weigert bij een reden, dus groen is eerlijk voor het scharnier zelf. | feit (code) | midden | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Alle e2e-stappen groen op 5.3.0, ook "geen terugval" en de twee zips uit één bron. | feit (GEZIEN in run 44503804192) | hoog | tests groen |
| 2 | Geen test bewaakt deze regel; de fout werd in een film gevonden. | feit | hoog | gemiste kans, geen blokkade |
| 3 | Geen persoonsgegevens. | feit | hoog | |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. In `scherm_scharnier.py` na Place hinge een toets `cj_passing == "groen"` op beide delen plus een paneelscherm (zoals 15 tot 19 `-paneel.png`). Dan bewaakt de e2e dit voortaan.
2. Randgeval A4: zet groen alleen als het deel nog geen slechtere passing had (`if deel.get("cj_passing") not in ("oranje", "rood")`). Klein, maar eerlijker.
3. Bij een nieuwe opname van YouTube Pro 1 de stukken op 0:47 en 0:58 opnieuw laten zien met "Good fit".

Daan
