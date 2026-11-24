# Keuring e2e platformfout-filter Bison & Flex, 24-11-2026, automatische keurder
Wat ik keurde: commits b8a1f9d56 en 1ccdcd4ff (reeks fdef8f3..04bc44c), bestanden `e2e/.../Gedeeld.kt` en `e2e/.../PlatformfoutTest.kt`
Akkoord: ja

## Deel A: doet het wat beloofd is?
(Er is geen eis in `ontwerp.md` voor deze wijziging. Ik toets aan de bedoeling in de commitberichten en de codecommentaren: de e2e-test mag niet falen op de platformfout "argument is not a child" bij "Previous Conflict", en echte fouten van onze plugin moeten wel falen.)
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De filter wordt van `node is not a child` verbreed naar `is not a child`, nog steeds samen met `OccurenceNavigatorSupport`. Dat dekt de nieuwe tekst "argument is not a child". | Feit (uit de diff) | Hoog | n.v.t. |
| 2 | De vier nieuwe unittests dekken: bekende fout zonder plugin, de Previous-variant, bekende fout met `com.dortus` in de stack (faalt nog), en een andere fout of maar één van de twee delen (faalt nog). Dat past bij de bedoeling. | Feit | Hoog | n.v.t. |
| 3 | Of de tests slagen weet ik niet. De functie `bekendePlatformfout` zelf staat niet in de diff. Tests 2 en 3 gaan ervan uit dat ze zoekt in bericht plus details, en dat ze `com.dortus` in de stack afwijst. | Vermoeden | Midden | Een groene e2e-run in de API, of de volledige `Gedeeld.kt` waar die logica staat. |
| 4 | De verbrede filter kan in theorie ook andere "… is not a child"-fouten wegfilteren. Dat blijft beperkt: er moet `OccurenceNavigatorSupport` in de stack staan en geen enkele regel van onze plugin. | Feit | Hoog | n.v.t. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen bestaande test is aangepast. Er is een nieuw testbestand bij gekomen. Alleen de uitzonderingslijst in de e2e-helper is breder geworden, met een uitleg bij de oorzaak (platformfout, geen plugin in de stack). Dat is geen aanpassen om te slagen. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | Beide bestanden zijn ruim onder 400 regels. | Feit | Hoog | Bestanden onder ±400 regels |
| 3 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 4 | `architectuur.md` is niet bijgewerkt. Dat hoeft hier niet, want het is alleen testgereedschap. Of de e2e-filter daar al staat, kan ik niet zien (de tekst is afgekapt). | Vermoeden | Laag | architectuur.md bijgewerkt |
| 5 | Het runnummer 45305066655 staat in een codecommentaar zonder label GEZIEN, DERDEN of GOK. Het is een verwijzing in code, geen cijfer in een belofte. | Feit | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 6 | Geen spelerstekst, geen beeld of geluid, geen wijziging in de change-notes. Dat klopt, want er is niets zichtbaar voor gebruikers veranderd. | Feit | Hoog | Hats-tekst en Steam-regels (hier niet van toepassing) |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Niet van toepassing: alleen testcode, niets voor de gebruiker zichtbaar of speelbaar. | n.v.t. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Controleer in de API dat de e2e-run en de nieuwe unittests na deze commits groen zijn. Ik kon niets draaien.
- Het codecommentaar in `PlatformfoutTest.kt` zegt "drie gevallen", maar er zijn vier tests. Pas de tekst aan.
- Zet bij het runnummer in `Gedeeld.kt` een label (bijvoorbeeld GEZIEN met datum), zodat later te zien is waar het vandaan komt.
- Controleer dat `architectuur.md` of de testbeschrijving de platformfout-uitzondering noemt, als dat daar hoort.

---
Automatische keurder, model `claude-sonnet-5-5`, 19767 tokens in, 3080 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
