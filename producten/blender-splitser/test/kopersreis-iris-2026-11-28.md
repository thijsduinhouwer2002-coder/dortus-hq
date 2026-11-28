# Kopersreis Click Cuts als mailontvanger met gratis code (issue #383)

Iris, za 28 nov 2026 middag NL. Nagespeeld: wat een van de 8 makers ziet van de Gumroad-pagina tot de eerste gesplitste en geëxporteerde STL. Script: `kopersreis_iris.py` (naast dit bestand), korte log: `kopersreis-iris-2026-11-28-log.txt`.

**Uitslag in één regel:** installeren 0 fouten in 4 van 4 (zip 1.0.0 live en 1.1.0, Blender 4.2.23 en 5.3.0, GEZIEN). 3 drempels voor een nieuwe koper, alle drie als issue bij de Productbouwer: #385, #386, #387.

## Wat getest is
| | |
|---|---|
| Gumroad-pagina | https://duinhouwer8.gumroad.com/l/click-cuts met curl, 200, price_cents 1900, 1 bestand ZIP van 64.085 bytes voor Standard en Supporter (GEZIEN) |
| Zip die nu live staat | `click_cuts-1.0.0.zip` uit e2e 45810355179, sha256 `90f4da56...`, 64.085 bytes: gelijk aan de grootte die Gumroad toont (GEZIEN) |
| Zip na vanavond 20:00 | `click_cuts-1.1.0.zip` uit uitgave-run 46093220919, sha256 `bd591759...`, gelijk aan `SHA256SUMS.txt` en aan de plakkaart (GEZIEN) |
| Blender | 4.2.23 LTS en 5.3.0 (nieuwste 5.x op download.blender.org, GEZIEN), achtergrond, schone gebruikersmap per run |
| Gevolgde tekst | "Getting started" en "Your first split" van dortus.com/click-cuts/ (de gids waar Gumroad naar linkt) en het blok "Tekst voor de tab" in `winkel/docs.md`. De Content-tab zelf zie ik niet: die staat achter een aankoop |

## Per stap
| # | Stap | Uitslag | Bewijs |
|---|---|---|---|
| 1 | Gumroad-pagina openen | GOED | 200; titel, haak, prijs $19, Supporter $29. Tekst noemt "Free cut" en "Partly" bij zelf kiezen: klopt met de zip 1.0.0 die nu live staat (GEZIEN) |
| 2 | Links op de Gumroad-pagina | GOED | Enige link https://dortus.com/click-cuts/: 200 (GEZIEN) |
| 3 | Links en beelden op de gids | GOED | hero, fit-test, magnets, numbers, panel.jpg: 200; dortus.com/click-joints/ 200; Superhive-makerspagina 200; alle 12 ankers (#start, #free-cut, #faq-folder ...) bestaan (GEZIEN). Superhive-productpagina 403 en `draw-cut.jpg` 404: verwacht, product nog in keuring en hulppagina 1.1 nog niet samengevoegd |
| 4 | Versie op pagina en zip | GOED | Gids zegt `click_cuts-1.0.0.zip`, live zip heet zo en manifest zegt 1.0.0 (GEZIEN). Let op voor 20:00: na plakdeel 1b staat 1.1.0 op Gumroad; deel 1e (tak `claude/click-cuts-hulp-1.1`) moet tegelijk, anders noemt de gids nog 1.0.0 en Free cut |
| 5 | Installeren (Install from Disk, zelfde als slepen) | GOED | `package_install_files`: FINISHED, paneel geregistreerd, tab "Click Cuts", 0 fouten in 4 van 4 combinaties (GEZIEN) |
| 6 | Knoppen uit de tekst bestaan | GOED | "Your printer", "Custom size", "Split to fit", "Export parts (STL)", "More settings", "Make fit test", "Export fit test", "Printed? Click the one that fits", "Convert to mm", "Saved for this printer" staan in de code van beide zips; "Draw cut", "Flip side" en "comes off" alleen in 1.1.0, zoals de tekst van 1.1 belooft (GEZIEN) |
| 7 | Eerste split op wat er staat: standaardkubus (2 m), printer A1 | **DREMPEL #385** | "This needs at least 512 pieces (limit 200). Check the unit of the scene or pick a bigger printer"; paneel: "No plan: check the unit or pick a bigger printer". Convert to mm is niet te kiezen (poll faalt). Geen maat in de melding, geen uitweg (GEZIEN, alle 4) |
| 8 | Model van een modelsite: STL in mm (aap, ±400 mm) importeren, Split to fit | **DREMPEL #386** (klein) | "aap_mm is 3.985e+05 mm: the unit of the scene is probably wrong. Use Convert to mm first": wetenschappelijk getal (GEZIEN, alle 4) |
| 9 | Convert to mm, opnieuw Split to fit | GOED | Scene naar mm, daarna FINISHED, 4 stukken plus pinnen, geen foutregel (GEZIEN, alle 4). Precies wat de tekst onder "Wrong unit?" belooft |
| 10 | Export parts (STL) zonder eerst op te slaan, zoals de 4 stappen letterlijk staan | **DREMPEL #387** | Bestanden gaan naar tempmap/click_cuts. De hint "Saves to a temporary folder" staat alleen onder More settings stap 4, niet bij de grote knop; de snelstart zegt pas ná stap 4 "Save your .blend first" (GEZIEN, `exporteer.py` r. 20-21, `paneel.py` r. 89 en 186) |
| 11 | Export na opslaan | GOED | `click_cuts/` naast de .blend: piece_01 tot piece_04.stl en pins_5mm_x16.stl, zoals de tekst belooft (GEZIEN, alle 4) |
| 12 | Fit test maken en exporteren (PLA) | GOED | fit_test_block.stl en fit_test_pins.stl, speling 0,20 mm voor PLA; materialen PLA, PETG, ABS, TPU, RESIN, OTHER (GEZIEN, alle 4) |
| 13 | Add free cut en Cut piece (de weg zonder muis; Draw cut zelf vraagt een muis en is niet in de achtergrond getest) | GOED | Van 5 naar 7 objecten in de stukkenverzameling, geen fout (GEZIEN, alle 4) |
| 14 | ?-knop en Online Manual in 1.1.0 | GOED | Alle ankers die `hulp.py` opent (#first-split, #fit-test, #flat, #free-cut, #magnets, #panel, #faq) bestaan op de huidige gids (GEZIEN) |

## Wat ik niet kon zien
- De Content-tab na aankoop en of de outreach-code de prijs naar $0 zet: achter inloggen. De hoofdchat zag het laatste (V1, GEZIEN in `commercie/geplaatst.md`).
- Draw cut met de muis en het paneel op beeld: niet in deze run. De e2e van de Productbouwer doet Draw cut met een echte muis (groen in 4.2.23 en 5.3.0, DERDEN: run 46056960861).

## Voor de hoofdchat (vanavond 20:00)
Plakdeel 1b (zip 1.1.0 op Gumroad) en 1e (hulppagina 1.1 samenvoegen) tegelijk doen. Nu geeft `draw-cut.jpg` 404 en zegt de gids "Free cut"; een koper van 1.1.0 die op ? drukt bij Draw cut, leest dan over Free cut.
