# Keuringen 24 nov 2026 middag, Daan (ontwerper)

Vijf Blender-keuringen in één bestand, elk met het formulier van skill `keuren`. Ebb staat in `platformen/garmin/keuring/2026-11-24-ebb-apnea.md`.

---

## 1. Pro 1.2.6 robot-enkels (Olaf)
Wat ik keurde: tak `claude/blender-pro-1.2.6-robot-enkels` 6dc287f, beeld `2026-11-24-robot-enkels-voet.png`, e2e 45384569641
Akkoord: **ja**

### Deel A
| # | Bevinding | Feit of vermoeden | Zekerheid | Bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | E2e 45384569641 op 6dc287f: 4.2.23, 5.2.3 en 5.3.0 alle drie success | Feit (GEZIEN, API 24 nov ±13:45) | hoog | |
| A2 | Wijziging in `rig.py` raakt alleen het vangnet van de enkel (`vang_bot = pb.parent` alleen bij ANKLE); knie, elleboog en kogels houden de oude bol | Feit (diff gelezen) | hoog | |
| A3 | Een echt weggevallen voet wordt nog gevangen (±48% tegen grens 6%) | Vermoeden (cijfer van Olaf, niet zelf gemeten) | midden | een toets die een voet expres laat wegvallen |
| A4 | Nieuwe toets `toetsen_robot_meer.py` staat in de e2e, oude toetsen niet aangepast | Feit (diff workflow) | hoog | |

### Deel B
Geen bevindingen: geen persoonsgegevens, bestanden klein, cijfers met GEZIEN.

### Deel C
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Zijaanzicht: de uitsnede haalt een schuine wig uit de achterkant van de blokvoet, en achter de scheen steekt een scherpe punt uit. Bij 90 graden buigen hoort zwaairuimte, dus geen fout, maar het oogt als een hap uit de hiel | Wig alleen zo groot als nodig voor het bereik (of bereik 0-75 op een blokvoet), of in de lijst "ankle: heel trimmed for 90°" zodat de koper het verwacht | midden |

### Moet / Kan
Moet: geen. Een enkel met een hap uit de hiel is beter dan geen enkel (1.2.5 sloeg ze over).
Kan: C1, en A3 als toets.

---

## 2. Click Cuts herkeuring M1 noten-regel (Productbouwer, run 11)
Wat ik keurde: bb379aa, `in_een_klik.py` `noten_regel`, beeld `paneel-noten.png` uit artefact `blender-splitser-screenshots-5.3.0` van e2e 45388051462 (success)
Akkoord: **ja**, M1 is weg.

| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| A1 | Resultaatvak toont "2 notes: see More settings" met info-icoon, past op één regel in het vak, More settings dicht | Feit (beeld zelf bekeken) | hoog |
| A2 | Regel verdwijnt bij 0 noten of open More settings; enkelvoud "1 note" klopt | Feit (code gelezen) | hoog |

Kan: niets nieuws.

---

## 3. Superhive Docs-tab, Start here.txt en foto-zin (Bram)
Wat ik keurde: `platformen/blender/superhive/docs-tab-1.2.5.md` (a2b6d73)
Akkoord: **ja** voor deel 1 en 3. Deel 2 (Start here.txt) pas mee als clip 2 opnieuw gekeurd is (zie 5).

| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| A1 | Alle knopnamen kloppen met de code: "Fit test: ball/hinge", "Print this first", "Figure from rig", "More bones (ankles too)", "Or put the 3D cursor on a joint, then:", "Place hinge, bends up to:", "Flip bend", "Show bend range", "Reset bend" | Feit (grep in `click_joints/`) | hoog |
| A2 | Enkel-grens gelijk aan de releasenote ("human figures", 5.2 en nieuwer) | Feit | hoog |
| A3 | Geen versienummer in de zipnaam meer: goed, de tab veroudert niet bij elke update | Feit | hoog |

Kan: K1 "can not be on" wordt "cannot be on". K2 in Start here.txt: lengte clip 2 wordt ±15 s na het inkorten. Foto-zin is goed zoals hij is.

---

## 4. Review-zin site en README (Bram, B1 en B2)
Wat ik keurde: `platformen/blender/dortus-com-review-zin.patch` (op dortus e2a1a0e), beeld `2026-11-24-review-zin-tel.png`, README-regel in 1916446
Akkoord: **ja**

| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| A1 | Op 390 breed staat de zin onder de knop, leesbaar, geen zijwaarts scrollen, link onderstreept | Feit (beeld bekeken) | hoog |
| A2 | Link https://extensions.blender.org/add-ons/click-joints/reviews/ geeft 200 | Feit (curl 24 nov ±13:50) | hoog |
| A3 | Oude ratingzin weg, dus niet dubbel | Feit (patch) | hoog |

Kan: de zin is wat lang naast een kleine statusknop; "Using the free version? A short review helps others find it: leave a review." is korter. Mag zo live.

---

## 5. Click Joints Pro video guide, 2 clips (Chris)
Wat ik keurde: `commercie/blender-click-joints/pro-uitleg/` (16e8084), elke 3,5 s een beeld uit clip 1 en elke 0,2 tot 2 s uit clip 2, plus volle beelden op 3 s en 4 s
Akkoord: **clip 1 ja, clip 2 nee** (één moet)

### Deel A
| # | Bevinding | Feit of vermoeden | Zekerheid | Bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Clip 1: elk onderschrift klopt met het beeld: knop Figure from rig zichtbaar op 3 s, dan types en graden, "+12° past limit" in rood bij "Past the stop", exploded view in close-up, Export 3MF actief bij "Export STL or 3MF" | Feit (beelden bekeken) | hoog | |
| A2 | Tekst links groot en leesbaar; paneeltekst op 1080 leesbaar | Feit | hoog | |
| A3 | Clip 2: de eerste ±1,4 s toont de voetbalfiguur met kniebereik onder "Print this first: a small fit test". Een koper ziet een figuur waar een fit test beloofd wordt | Feit (beelden 0 tot 3 s per 0,2 s) | hoog | |
| A4 | Clip 2 uit de oudere opname mag: paneel en knoppen zijn gelijk aan nu ("Fit test strip" is ook nu de naam van de handeling, `testkaart.py`) | Feit | hoog | |

### Deel C
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Clip 2: het getal op elk staafje (0.10 tot 0.30) is niet te lezen, en welke knop werd ingedrukt zie je niet | Inzoomen op de getallen aan het eind, of een onderschrift "0.10 · 0.15 · 0.20 · 0.25 · 0.30 mm" | klein |
| C2 | Clip 1: de klik op Figure from rig duurt maar een halve seconde | Een kader of pijl op de knop rond 3 s | klein |

### Moet / Kan
Moet M1 (clip 2): begin bij de staafjes, dus `maak.py` start op ±frame 1216 in plaats van 1174 (de figuur weg). Daarna keur ik alleen dat.
Kan: C1, C2. Clip 1 mag nu al bij het product.
