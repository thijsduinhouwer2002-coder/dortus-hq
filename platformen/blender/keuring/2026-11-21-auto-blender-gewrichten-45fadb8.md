# Keuring Direct-zip in architectuur.md (blender-gewrichten), 21-11-2026, automatische keurder
Wat ik keurde: commits c368201..45fadb8 (45fadb84d "architectuur direct-zip"), alleen `producten/blender-gewrichten/architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is alleen tekst in `architectuur.md`. Er staat geen code, script of test in deze reeks. | Feit | Hoog | De bestandslijst van de diff. |
| 2 | De tekst beschrijft `e2e/maak_zip.sh direct`, `e2e/direct/direct.py`, `init_direct.py`, `toets_direct_zip.py`, `test_direct.py` en `scherm_direct.py`. Dat die bestanden bestaan en doen wat er staat, kan ik hier niet zien. | Vermoeden | Midden | Die bestanden in dezelfde of een eerdere commit, en een groene run met de stap "Direct-zip" in 4.2, 5.2 en 5.3. |
| 3 | De tekst zegt dat de extensions-zip niet verandert en Pro nergens noemt, en dat de direct-zip nooit naar extensions.blender.org gaat. Dat past bij de belofte in het ontwerp (gratis versie zonder verwijzing naar betaald, regel 6.1). | Feit (over de tekst), vermoeden (over de zip zelf) | Midden | Het resultaat van `toets_direct_zip.py` en de grep in de workflow. |
| 4 | Het ontwerp noemt "twee builds uit één bron". Nu zijn het er drie, en het ontwerp noemt de directe download niet. In het stuk dat ik zag staat ook geen akkoord van Thijs of Daan voor de Pro-knoppen op slot in de gratis directe versie. | Vermoeden | Laag | Het volledige ontwerp en een besluit van Thijs of Daan. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt voor de nieuwe build, de toetsen en de workflowstap. | Feit | Hoog | architectuur.md bijgewerkt |
| 2 | Er is geen test aangepast. De diff bevat geen testbestanden. | Feit | Hoog | Tests niet aangepast om te slagen |
| 3 | Er zijn geen persoonsgegevens, sleutels of wachtwoorden in de nieuwe regels. | Feit | Hoog | Geen persoonsgegevens |
| 4 | De regel "Afkijker 21 nov, voorbeeld TrailPrint3D" heeft geen label GEZIEN, DERDEN of GOK. | Feit | Hoog | Cijfers en beweringen met GEZIEN/DERDEN/GOK |
| 5 | Het bestand heeft ±70 regels en blijft dus ruim onder de 400. De regels zelf zijn wel erg lang en moeilijk te lezen. | Feit | Midden | Bestanden onder ±400 regels |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Ik kan niets zien, alleen lezen. Drie knoppen met een slot en daaronder "Upgrade to Pro" kunnen op een gratis add-on pusherig overkomen. Dat is een vermoeden. | Scherm `d1-slot` bekijken. Overweeg één regel in plaats van drie knoppen met slot, of de knoppen samenvouwen. | Klein |
| 2 | Het venster bij een slotknop is kort en duidelijk: de functie, "This is in Click Joints Pro" en één knop. | Eventueel één plaatje of één zin over wat de functie oplevert, zodat de klik beloond wordt. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Voeg een label toe aan de TrailPrint3D-bron (DERDEN of GOK).
- Controleer dat de genoemde e2e-bestanden bij deze commit bestaan en dat de run groen is.
- Zet de directe download (drie builds) in `ontwerp.md`. Laat Thijs of Daan de Pro-knoppen op slot vooraf goedkeuren, en Daan het scherm `d1-slot` beoordelen op toon en uiterlijk.
- Splits de lange regels in `architectuur.md` op, zodat het bestand leesbaar blijft.

---
Automatische keurder, model `claude-sonnet-5-5`, 19017 tokens in, 2744 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
