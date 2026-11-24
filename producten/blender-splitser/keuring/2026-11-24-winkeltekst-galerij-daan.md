# Keuring Click Cuts winkeltekst-kop en galerij-onderschriften, 24 nov 2026 ±23:05 NL, Daan

Wat ik keurde (issue #12): `producten/blender-splitser/galerij.md` (Productbouwer): titel, haak, eerste alinea, FAQ-zin over Free cut en de 7 onderschriften. Naast 1.0.0 op main (`split_joints/`, `CHANGELOG.md`). Code gelezen, niet zelf in Blender gedraaid.

Akkoord: **ja, mits M1 letterlijk zo wordt overgenomen**. Dan is geen nakeuring nodig. Wijkt de nieuwe tekst af van wat hieronder staat: één nakeuring.

## Bewijs
- Blinde test kop B: GESLAAGD, plek 1,0 bij Gemini en ChatGPT tegen Cleave, Split 3D Print en SnapSplit (GEZIEN, `organisatie/blindtest/uitslag/click-cuts-tekst-2026-11-24-2226.md`; volledige tekst nagekeken in `sets/click-cuts-tekst.json`, gelijk aan `galerij.md`).
- E2e Click Cuts op main 45492154406 (45920d8): success (GEZIEN via de API).

## Deel A: klopt elke belofte met 1.0.0?
| # | Belofte | Code | Oordeel |
|---|---|---|---|
| A1 | "plans every cut for you, so each part fits your bed" | `in_een_klik.py` doet Plan cuts; `plan.py` "where to cut so every piece fits on the bed". Lukt het niet: "No plan: ... pick a bigger printer". | klopt |
| A2 | "an engraved part number on every cut face" (alinea), "pins and pin holes on every cut face" (onderschrift 3), "Every cut face gets pin holes and an engraved part number" (onderschrift 4) | `verbind_3d.py`: is een vlak te klein, dan geen nummer ("no room for the number on a part of this face"); is een stuk te dun, dan geen pen ("Glue this joint"). "Every" klopt dus niet altijd. | **moet M1** |
| A3 | groen/oranje/rood met reden; groen = past, waterdicht, genoeg wand | `controle.py` regel 1 tot 5, rood bij minder dan 0,8 mm wand; reden per stuk in het paneel. | klopt |
| A4 | "remembers it for that printer and material" | `passingproef.py`: speling bewaard per printer en materiaal in de voorkeuren. | klopt |
| A5 | proefblok "your own pin at four clearances" | `passing.py`: vier gaten, speling gegraveerd, vier pennen. | klopt |
| A6 | FAQ: "Free cut adds one at any angle through one part" | `vrije_snede.py`, CHANGELOG "an extra cut at any angle through one part". | klopt |
| A7 | Onderschrift 7: drie stappen in de tab (printer, Split to fit, Export STL/3MF in mm) | `paneel.py`: bovenaan printer, Split to fit, Export parts; tab "Click Cuts". | klopt |
| A8 | Niets over plat leggen, alleen pennen, niets over zelf printen of klikken. | | klopt |
| A9 | Onderschrift 2 "The gold box is its bed": de add-on tekent zelf geen bed in het venster. Het gouden kader zit alleen in onze render (`merk/bron/splits_scene.py`). | | kan K1 |

## Deel B: regels
Engels in de winkel, Nederlands eromheen, geen AI, getallen in onderschrift 3 als voorbeeld gemarkeerd, geen persoonsgegevens. In orde.

## Deel C: goed genoeg?
| Vraag | Cijfer | Waarom, en waarmee vergeleken |
|---|---|---|
| Op het niveau van de beste in de winkel? | 8 | Naast [Cleave](https://superhivemarket.com/products/cleave): haak even kort, en wij noemen drie dingen die Cleave niet zo zegt (nummer op het snijvlak, controlekleur met reden, proefblok). Blind plek 1 bij beide rechters. |
| Zou ik het kopen op basis hiervan? | 8 | Ja: "Pick your printer. Click once. Every part fits." zegt in één regel wat ik wil. |
| Zou Thijs er trots op zijn? | 8 | Na M1 eerlijk tot op het randgeval. |

## Moet
- **M1** "Every" weg waar de code het niet altijd haalt. Letterlijk zo:
  - Alinea: `... so each part fits your bed, with pins, pin holes and an engraved part number on the cut faces.`
  - Onderschrift 3: `**One click, every part fits.** Split to fit plans every cut, so each part fits your bed, with pins and pin holes on the cut faces.`
  - Onderschrift 4: `**Numbered for assembly.** Cut faces get pin holes and an engraved part number, like 3-5 where part 3 meets part 5.`
  De boodschap blijft gelijk, dus geen nieuwe blinde test nodig.

## Kan
- K1 Onderschrift 2: schrijf `In this picture the gold box marks its bed.` of laat het kader weg uit de zin, zodat niemand een bedkader in Blender verwacht. Beter nog later: het bed echt als kader tonen in de add-on (dicht ook een gat: de koper ziet meteen wat "too big" is).
- K2 Spelling: galerij is Amerikaans ("millimeters"), CHANGELOG Brits ("millimetres", "Colour"). Kies op één winkelpagina één spelling.
