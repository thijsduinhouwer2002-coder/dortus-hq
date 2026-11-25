# Keuring Robot-hoofdbeeld in KAART.md (blender-gewrichten), 25-11-2026, automatische keurder
Wat ik keurde: commit a52980a59 (alleen `producten/blender-gewrichten/KAART.md`, één regel)
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging zet in KAART.md dat het hoofdbeeld (robot uit elkaar met labels) op Gumroad en Superhive staat. Het beeld zelf zit niet in de wijziging. | Feit | Hoog | Het beeld zelf bekijken met Read, of beide winkelpagina's ophalen met curl. |
| 2 | De regel zegt "sinds 25 nov 08:45", maar deze keuring is van 08:42. De tijd ligt dus in de toekomst, of is geschat of vooraf opgeschreven. | Feit | Hoog | De publicatietijd op Gumroad en Superhive. |
| 3 | Of de robot echt live staat op beide winkels kan ik uit de tekst niet halen. | Vermoeden | Laag | De live productpagina's met curl. |
| 4 | De commit zegt dat de oude Shorts privé zijn gezet. Dat staat nergens in de wijziging. | Vermoeden | Laag | De kanaalinstellingen of een lijst van de video's. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen blinde-testuitslag GESLAAGD voor het robotbeeld. De regel in KAART.md over de blinde test gaat nog over de oude tekenpop (Cleave won, 2,0). Het beeld is al live gezet. | Feit | Hoog | Hoofdbeeld van een klant: eerst blinde test (`organisatie/blindtest/`), zonder GESLAAGD geen akkoord. |
| 2 | In de wijziging is geen keuring van het beeld door Daan te zien. | Feit | Hoog | Uiterlijk keurt Daan. |
| 3 | KAART.md is nu intern tegenstrijdig: de regel "Blinde test" noemt nog de cover met de tekenpop en het advies "gedetailleerd personage". | Feit | Midden | Cijfers en claims met bron. |
| 4 | Er zijn geen tests aangepast, het bestand is klein, er staan geen persoonsgegevens of sleutels in en er zijn geen nieuwe cijfers. | Feit | Hoog | Testregels, bestandsgrootte, persoonsgegevens, GEZIEN/DERDEN/GOK. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Ik kan het beeld niet zien, dus ik kan niets zeggen over hoe het oogt. Het advies van beide testers (tekst op elk beeld, een gedetailleerd personage) lijkt wel opgevolgd: een robot met labels. Dat is een vermoeden. | Het beeld naast Cleave leggen en blind laten testen. | Klein |

## Deel C: is het goed genoeg?
| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeleken |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | Geen cijfer | Beeld niet gezien en geen uitslag. De vorige cover verloor van Cleave. |
| Zou ik het zelf kopen of bekijken op basis van dit? | Geen cijfer | Niet te beoordelen uit tekst. |
| Zou Thijs er trots op zijn? | Geen cijfer | Niet te beoordelen uit tekst. |

Zonder uitslag GESLAAGD is het akkoord altijd nee.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Voer de blinde test uit op het robot-hoofdbeeld en zet de uitslag in `organisatie/blindtest/uitslag/`. Het beeld staat al live, dus bij een uitslag onder GESLAAGD moet het terug naar het oude beeld of een nieuw beeld.
2. Laat Daan het beeld keuren, en leg het naast het beste concurrentvoorbeeld (Cleave) met een cijfer per vraag.
3. Haal de tijdsaanduiding "08:45" weg of vervang die door de echte publicatietijd. Nu loopt die voor op de keuring.

**Kan**
1. Werk de regel "Blinde test" in KAART.md bij met de uitslag voor het robotbeeld, zodat hij niet meer over de tekenpop gaat.
2. Leg vast waar je kunt zien dat de oude Shorts privé staan, bijvoorbeeld in een bericht of de KAART.

---
Automatische keurder, model `claude-sonnet-5-5`, 18770 tokens in, 2704 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
