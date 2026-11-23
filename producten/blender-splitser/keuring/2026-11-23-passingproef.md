# Keuring passingproef Click Cuts (Split Joints), 23 nov 2026, keurder passingproef (aparte Claude)
Wat ik keurde: commit ccf3800 in `producten/blender-splitser/` (`passing.py`, `passingproef.py`, wijzigingen in `eigenschappen.py`, `paneel.py`, `vormen.py`, `__init__.py`; tests `e2e/toetsen_passing.py`, deel 8 van `e2e/test_logica.py`, `e2e/scherm_passing.py`; `ontwerp.md` deel 10, `architectuur.md`). Beelden `passing-1.png` en `passing-2.png` zelf bekeken. Zelf gemeten in Blender 4.2.23 met de zip uit `e2e/maak_zip.sh` (eigen scripts in /tmp/keur).
Opdracht: "één knop maakt een proefblok met je eigen pen op 4 spelingen, met de speling gegraveerd, en de gekozen speling wordt onthouden per printer en materiaal" (hoofdchat 23 nov ±18:00, must have 1 in `concurrentie.md`).
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Eén knop maakt blok plus 4 pennen. Zelf gemeten (stralen op 3 hoogtes, 90 richtingen): pen 5 mm, speling 0,20 geeft gaten r 2,650 / 2,700 / 2,750 / 2,800 mm (doel precies gelijk, max 0,014 boven door de veelhoek), diepte 6,30 mm, blok 68,0 x 17,1 x 8,3 mm op z = 0, pen 12,0 mm lang. Speling klopt met het gat. | feit | hoog | gemeten |
| A2 | Gegraveerde tekst klopt met het gat: van links naar rechts 0.15, 0.20, 0.25, 0.30, elk voor het juiste gat (bovenaanzicht `passing-2.png`, en `sj_gaten` per gat met de gemeten straal). | feit | hoog | beeld en meting |
| A3 | **Na Make fit test is het proefblok het actieve object. Klik je daarna Plan cuts en Split (de gewone volgorde: stap 3 zegt "print this first", dan terug naar stap 2), dan plant en splitst de add-on het proefblok in plaats van je model.** Zelf gemeten: kubus van 300 mm in een mm-scene, printer A1 mini, Make fit test, Plan cuts: "1 pieces, 0 cuts", `bron` = "Fit test block"; Split: "1 pieces, 0 pins, all fit", Piece 01 is het proefblok. De e2e zet vóór Plan het model weer actief (`modellen.actief(ob)` in `toetsen_passing.py` deel 4), daardoor zag de test dit niet. | feit | hoog | mijn script /tmp/keur/k2.py; opnieuw toetsen zonder `modellen.actief` |
| A4 | **De bewaarde speling komt niet terug in een nieuw bestand of nieuwe scene.** Bewaard A1 + PLA = 0,25; nieuwe scene (printer A1, PLA, de standaard): speling blijft 0,20. Hij komt alleen terug als je printer of materiaal wisselt (update-callback). Wie de standaardprinter A1 heeft, of in een nieuw bestand al op zijn printer staat, krijgt de bewaarde waarde nooit vanzelf; het vak toont dan "Saved for this printer: 0.25 mm" terwijl Split 0,20 gebruikt. Dat is niet "onthouden" zoals beloofd in `ontwerp.md` deel 10 ("komt die speling vanzelf terug"). De e2e toetst alleen wisselen (MK4 dan A1 mini). | feit | hoog | mijn script /tmp/keur/k1.py stap 7 |
| A5 | Bewaren na herstart werkt: in Blender met interface (xvfb, zonder factory-startup, eigen lege config) A1 mini + PETG = 0,30 gekozen, Blender afgesloten zonder `save_userpref`; `userpref.blend` geschreven, na herstart staat `{"A1MINI|PETG": 0.3}` in de voorkeuren en kiezen van A1 mini + PETG zet 0,30. Werkt via autosave van de voorkeuren; staat autosave uit, dan gaat het verloren zonder melding. | feit | hoog | /tmp/keur/a.py en b.py |
| A6 | **Speling 1,0 (het maximum):** proef maakt 0.95 / 1.00 / 1.05 / 1.10 (gaten gemeten 3,45 tot 3,60, kloppen). Maar knop "1.10" of "1.05" kiezen zet en bewaart 1,00 (FloatProperty max 1,0 in `passing_kies` en `speling_mm`, `lees` gooit alles boven 1,0 weg). De knop zegt 1.10, het gat was 1.10, bewaard wordt 1.00 zonder melding. | feit | hoog | gemeten: `passing_kies(waarde=1.10)` geeft speling 1.0, prefs `{"A1|PLA": 1.0}` |
| A7 | Pen 20 mm, lengte 60: blok 106,4 x 32,1 x 32,3 mm, gaten kloppen (10,15 tot 10,30), past op een A1 mini. Pen 2 mm, lengte 4: blok 68 x 14,1 x 4,3, vloer 2 mm, gaten kloppen. Scene in meters: zelfde blok in mm, gaten kloppen. Twee keer klikken vervangt de oude proef (2 objecten). | feit | hoog | gemeten |
| A8 | Printerkeuze verandert de speling: handmatig 0,12 ingesteld, printer MK4 en terug naar A1 zet stil 0,25 (de bewaarde). Zo bedoeld, maar zonder melding merkt de koper niet dat zijn eigen waarde weg is. | feit | hoog | gemeten |
| A9 | Gekozen speling met Ctrl+Z ongedaan maken zet de scene terug, maar de voorkeur blijft bewaard. Klein. | vermoeden | midden | Ctrl+Z na "This one fits" en dan voorkeuren lezen |
| A10 | De proef gebruikt de hoofddiameter, niet de kleinere Auto-pennen; eerlijk als GOK genoemd in `ontwerp.md`. Een echte print is niet gedaan (ook eerlijk genoemd). | feit | hoog | een print op een A1 mini |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Tests niet aangepast om te slagen: `test_kern.py` krijgt alleen een aanroep erbij; `test_logica.py` deel 8 lokaal 0 fout (zelf gedraaid). Wel: de e2e zet het model actief vóór Plan en mist zo A3. | feit | hoog | tests |
| B2 | Bestanden onder 400 regels (`passingproef.py` 255, `passing.py` 93). | feit | hoog | bouwen |
| B3 | `architectuur.md` bijgewerkt, maar de regel over `__init__.py` noemt `passingproef` nog niet bij de geregistreerde modules. | feit | hoog | architectuur bijgewerkt |
| B4 | e2e in CI voor ccf3800 liep nog tijdens deze keuring (run 45228604028, in_progress); `ontwerp.md` noemt alleen "lokaal 97 toetsen groen (GEZIEN)". Groen in CI nog niet gezien. | feit | hoog | werk af als tests groen zijn |
| B5 | `ontwerp.md` zegt "±68 x 18 x 8 mm"; gemeten 68,0 x 17,1 x 8,3. Met ± goed genoeg. | feit | hoog | eerlijk |
| B6 | Geen persoonsgegevens, GOK en DERDEN goed gebruikt. | feit | hoog | openbaar, eerlijk |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Het blok ziet er net en leesbaar uit (`passing-1.png`, `passing-2.png`): vier gaten op een rij, cijfers groot en diep genoeg, pennen ernaast. De "1" in 0.15 heeft een voetje links bovenaan dat schuin van voren op een "3" lijkt (`passing-1.png`: "0.35"?); van boven is het wel 0.15. | Een "1" met een duidelijker vorm in de pixelletter (bijv. met een voet onderaan) | klein |
| C2 | Na het printen moet de koper zelf onthouden welke knop hoort bij welk gat; de knoppen in het paneel tonen alleen de getallen. Goed genoeg, want het getal staat op het blok. Een zin "Pick the tightest one where the pin goes in by hand" bij de knoppen helpt (staat nu alleen in de tooltip). | Korte uitleg zichtbaar in het vak | klein |
| C3 | Geen beeld van het paneel met het nieuwe vak gezien (geen xdotool hier; de bouwer meldt ook geen paneelbeeld). Of "Fit test: print this first" midden in stap 3 tussen Clearance en Min. wall goed leest, is niet bekeken. | Paneelbeeld uit CI (`paneel-x.png`) bekijken met de skill `kijken` | klein |
| C4 | Als de bewaarde speling verschilt van de huidige, staan beide getallen in beeld zonder knop om de bewaarde te gebruiken. | Knop "Use saved" of vanzelf toepassen (zie M2) | klein |
| C5 | Stilletjes overschrijven bij wisselen van printer (A8). | Melding "Clearance set to 0.25 (saved for A1 mini + PLA)" | klein |

## Moet (blokkeert akkoord)
- **M1 (A3):** na Make fit test mag Plan cuts en Split niet op het proefblok werken. Bijvoorbeeld: na het maken het vorige actieve model weer actief maken, en/of Plan en Split weigeren objecten met `sj_passing`. Toets in de e2e zonder `modellen.actief(ob)` vóór Plan.
- **M2 (A4):** de bewaarde speling moet ook terugkomen zonder te wisselen: bij een nieuw bestand of nieuwe scene (bijv. toepassen bij het laden of bij Make fit test, Plan en Split, of minstens een knop "Use saved"), zodat paneel en Split niet een andere speling gebruiken dan "Saved for this printer". Toets: bewaard A1 + PLA = 0,25, nieuwe scene op A1 + PLA, dan Split meet 0,25.
- **M3 (A6):** de vier spelingen mogen niet boven het maximum van 1,0 uitkomen (of het maximum omhoog), zodat de gekozen knop exact bewaard wordt. Toets in `test_logica.py`.

## Kan (mag later)
- C1 vorm van de "1", C2 korte uitleg bij de knoppen, C5 melding bij overschrijven, A9 undo, B3 `__init__`-regel in `architectuur.md`.
- B4: CI-run 45228604028 groen zien voor de herkeuring; C3 paneelbeeld bekijken.
- Melding als autosave van de voorkeuren uit staat (A5).
