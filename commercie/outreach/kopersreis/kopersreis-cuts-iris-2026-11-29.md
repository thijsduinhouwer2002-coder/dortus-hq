# Kopersreis Click Cuts als mailontvanger met gratis code (issue #424)

Iris, za 28 nov 2026 ±18:00 tot 18:50 NL. Nagespeeld: een maker die mail 1 (Braden) uit `commercie/outreach/bundel-2026-11-29-codes.md` krijgt, de codelink opent, de zip downloadt en met een eigen te groot model de snelstart volgt tot geëxporteerde delen. Script: `kopersreis_cuts_iris.py`, kort log: `kopersreis-cuts-iris-2026-11-29-log.txt` (beide naast dit bestand).

**Uitslag in één regel:** in Blender 5.3.0 van mail tot geëxporteerde delen zonder één drempel (GEZIEN). In Blender 4.2.23 loopt een gesloten model met overlappende delen dood op "No pieces came out" zonder uitweg: nieuwe drempel #426 bij de Productbouwer. De mailtekst klopt met de pagina en de add-on: geen issue voor de Verspreider.

## Wat getest is
| | |
|---|---|
| Mail | Mail 1 (Braden), zelfde belofte als mail 2 tot 6 en het sjabloon: delen die op je bed passen, pinnen of magneetgaten, gegraveerd nummer, groen/oranje/rood met reden, STL of 3MF, "print the fit test block first" |
| Codelink | https://duinhouwer8.gumroad.com/l/click-cuts/<testcode> met curl. De echte code heb ik niet (staat alleen in Gumroad); de hoofdchat zag bij elke mail $0 (V1, GEZIEN in `commercie/geplaatst.md`) |
| Download | `click_cuts-1.1.0.zip` uit uitgave-run 46093220919, sha256 `bd591759e8c9...3d7a`, 72.966 bytes. Gumroad toont nu 1 ZIP van 72.966 bytes voor Standard en Supporter: dit is de zip die een ontvanger krijgt (GEZIEN) |
| Blender | 4.2.23 LTS en 5.3.0, achtergrond, schone gebruikersmap per run |
| Eigen model | Buste als STL in mm: 420 x 250 x 299 mm, 15.912 vlakken, gesloten, met delen die door elkaar steken (ogen in het hoofd), zoals veel modellen van modelsites. Plus een tweede ontvanger die zelf in Blender modelleert: buste van 0,42 m in meters |
| Gevolgde tekst | "Getting started" en "Your first split" op dortus.com/click-cuts/ (de gids noemt nu `click_cuts-1.1.0.zip` en Draw cut, GEZIEN) |

## Per stap
| # | Stap | 4.2.23 | 5.3.0 | Bewijs |
|---|---|---|---|---|
| 1 | Codelink openen | GEZIEN | | Link opent de productpagina (200). Een foute code geeft `discount_code valid false, invalid_offer` en $19: de link zelf werkt zoals Gumroad hoort. $0 met de echte code: NIET GEZIEN door mij, wel door de hoofdchat |
| 2 | Klopt de mail met de pagina | GEZIEN | | Alle beloftes staan letterlijk op de pagina: "fits your bed, with pins, pin holes and an engraved part number on the cut faces", "green ... orange or red with the reason", "5x2, 6x2, 6x3, 8x3 or 10x3 mm", "Magnets are not included", "STL or 3MF", "fit test block". Enige link naar de gids: 200; alle links en beelden op de gids 200 (GEZIEN) |
| 3 | Installeren (Install from Disk) | GEZIEN | GEZIEN | FINISHED, tab "Click Cuts", 0 fouten |
| 4 | STL 420 mm importeren, A1, Split to fit | GEZIEN (melding) | GEZIEN (melding) | "buste_420mm is 4.2e+05 mm: the unit of the scene is probably wrong. Use Convert to mm first". Duidelijk wat te doen; getal nog steeds wetenschappelijk (bekend, #386 open) |
| 5 | Convert to mm, opnieuw Split to fit | **NIET GELUKT: #426** | GEZIEN | 4.2: "4 pieces, 2 cuts", dan "0 pieces, 0 pins, all fit" en "No pieces came out", paneel zonder reden of uitweg. 5.3: 4 stukken, 16 pinnen, 8 nummers |
| 5b | Uitweg in 4.2: Make watertight, dan Split to fit | GEZIEN | | 4 stukken. Werkt, maar de koper wordt er niet heen gewezen |
| 6 | Belofte: elk stuk groen, oranje of rood | NIET GELUKT (geen stukken) | GEZIEN | 4 van 4 groen in Check-kleuren. Twee voegen "too small for a pin ... Glue this joint" (dun ooglid van mijn model): reden staat erbij, zoals beloofd |
| 7 | Opslaan, Export parts (STL) | NIET GELUKT (geen stukken) | GEZIEN | piece_01 tot piece_04.stl en pins_5mm_x16.stl naast de .blend; grootste maat in de STL 250,0 mm, past op de A1 (256 mm) |
| 8 | Joint op Magnets (6x3), Split to fit | NIET GELUKT (geen stukken) | GEZIEN | 4 stukken groen, 28 magneetgaten, geen pinnen; voegen te klein melden "Glue this joint or pick a smaller magnet" |
| 9 | Export parts (3MF) | NIET GELUKT (geen stukken) | GEZIEN | piece_01 tot piece_04.3mf |
| 10 | Fit test block maken en exporteren | GEZIEN | GEZIEN | fit_test_block.stl en fit_test_pins.stl, speling 0,20 mm (PLA) |
| 11 | Zelf gemodelleerd in meters (0,42 m), Split to fit, exporteren zonder op te slaan | GEZIEN | GEZIEN | 4 stukken groen, 16 pinnen. Export gaat stil naar de tempmap `click_cuts` (5 bestanden): bekend, #387 open |

## Drempels
| Drempel | Waar | Issue |
|---|---|---|
| Blender 4.2: gesloten model met overlappende delen geeft "No pieces came out" zonder reden of uitweg; Make watertight lost het op | code | **#426** (nieuw, Productbouwer) |
| "4.2e+05 mm" | code | #386 (al open, opnieuw gezien in 1.1.0) |
| Export zonder opslaan gaat stil naar een tempmap | code | #387 (al open, opnieuw gezien in 1.1.0) |
| Mailtekst | mail | geen: elke belofte klopt met pagina en add-on |

## Let op voor de hoofdchat
- Eén code "Outreach Click Cuts (15)" telt verzilveringen, max 15. Vandaag gingen 16 Click Cuts-mails met die code uit (hoofdmanager in #424); na zondag hebben meer dan 15 mensen dezelfde code (GOK). Bij de 16e verzilvering ziet een ontvanger $19 terwijl de mail $0 belooft. Nu 0 van 15, dus geen risico voor zondag; kijk de teller na voor elke ronde (dat gebeurt al) en zet de grens hoger zodra hij boven 10 komt (kost niets).
- Waarom 0 van 15 verzilverd: in deze reis zit geen drempel vóór de download. Wie de link opent, ziet de beloofde pagina. Dat het nog niet gebeurde, past bij tijd (mails zijn van vandaag, GOK).

## Wat ik niet kon zien
- De $0 met de echte code en de Gumroad-kassa bij $0 (achter de echte code).
- Het paneel op beeld en Draw cut met de muis: niet in deze run (e2e van de Productbouwer doet Draw cut, DERDEN: run 46056960861).
