# Keuring versnelling Click Cuts, 24 nov 2026, Daan
Wat ik keurde: diff van 144fb69 (Productbouwer run 9) in `split_joints/splitsen.py`, `controle.py`, `verbind_3d.py`, `in_een_klik.py`, `paneel.py`, toets in `e2e/toetsen_klik.py`, uitleg `ontwerp.md` deel 14. Sindsdien geen wijziging in `split_joints/` (GEZIEN, git log).
Voorwaarde hoofdchat: `click-cuts-snelheid.yml` groen in 4.2. Run 45349335526 op 144fb69: snelheid 4.2.23 success, 5.3.0 success; e2e splitser op 144fb69 success (GEZIEN via de Actions-API).
Akkoord: **ja, één moet op de tekst (niet op de code)**

## Deel A: doet de code wat ze belooft?
| # | Bevinding | Feit of vermoeden | Zekerheid | Bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | `vlakken_op` rekent precies wat de oude lus deed: punt in mm (co / u) maal de normaal, binnen 0,001 mm van c; een vlak telt als al zijn punten erop liggen (`minimum.reduceat` op de loops). Nagespeeld in numpy met twee vierhoeken en een driehoek: goede vlakken gekozen (GEZIEN). | feit | hoog | |
| A2 | De indices kloppen met `bm.faces`: `from_mesh` houdt de volgorde van `me.polygons`, en het oude pad gebruikte ook geen `matrix_world`, alleen de schaal 1/u. Zelfde conventie. | feit | hoog | |
| A3 | `reduceat` gaat ervan uit dat `loop_start` oploopt; in Blender 4.x en 5.x zijn de vlak-offsets altijd oplopend. Leeg mesh vangt de functie zelf af. | feit | midden | |
| A4 | Nummerstap op Manifold: `stuk` is al model ∩ celdoos (en eventueel hersteld), dus stuk ∩ (doos − nummers) geeft hetzelfde stuk als model ∩ (doos − nummers), zonder het hele model nog eens te snijden. Bij Exact (4.2) blijft de oude weg, terecht (open randen in run 45213448129). | feit | hoog | |
| A5 | `Plaatser`: `tri` komt als int64 uit `mesh_mm`, dus `tolist()` geeft gehele getallen zoals vroeger `int(i)`. | feit | hoog | |
| A6 | Paneelregel alleen zonder uitslag, kost in `draw` alleen `len(polygons)`. Toets dekt geen regel bij een licht model en wel een regel boven de grens. | feit | hoog | |

## Deel B: meting en eerlijkheid
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | De CI-run meet niet de schedel van 1M uit deel 14, maar Suzanne met 0,5M vlakken. Daar: 4.2 (Exact) 21,1 s, 5.3 (Manifold) 11,5 s, 8 van 8 stukken groen in beide (GEZIEN in de logs). | feit | hoog | eerlijk |
| B2 | Dus 4.2 is op dit model bijna twee keer zo traag als 5.3, en de versnelling in `splitsen.py` werkt in 4.2 niet. De zin voor FAQ en winkel ("1 million face scan: about 40 seconds") geldt voor 5.3, niet voor 4.2. Een 4.2-koper met 1M zit eerder rond 80 s (GOK uit B1). | feit + gok | midden | eerlijk |
| B3 | Paneel zegt vanaf 1,0M "can take a few minutes" terwijl 1M rond 40 s meet. Ruim, maar beter te ruim dan te krap. | feit | hoog | |

## Moet
- M1 (B2): de zin voor FAQ en winkeltekst noemt de Blender-versie, bijvoorbeeld: "Tested on a 1 million face scan in Blender 5.3: about 40 seconds (2-core test machine). In Blender 4.2 it takes about twice as long." Zonder versie geen snelheidsclaim in de winkel.

## Kan
- K1 (B1): de workflow ook één keer met de schedel van 1M in 4.2 laten draaien, dan is de 4.2-tijd GEZIEN in plaats van GOK.
- K2 (B3): "Split can take a minute or more" past beter bij 1M; bij 3M klopt "a few minutes".
- K3 (A3): een regel commentaar bij `reduceat` dat het op oplopende `loop_start` steunt.

Voor de vaste zip van do 27 nov: de code mag mee.
