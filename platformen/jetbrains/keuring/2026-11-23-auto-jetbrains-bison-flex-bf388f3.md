# Keuring e2e licentiecontrole Bison & Flex, 23-11-2026, automatische keurder
Wat ik keurde: commit bf388f352 (9d9237d..bf388f3), bestanden `e2e/.../Gedeeld.kt` en `e2e/.../StructuurEnZweven.kt`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen de e2e-test. De plugin zelf en de belofte uit `ontwerp.md` (gratis deel, Pro, 30 dagen proef) veranderen niet. | Feit | Hoog | Het diff bevat alleen twee testbestanden. |
| 2 | Het regex zoekt nu naar woordbegin (`\b`), dus "Design info" geeft geen vals alarm meer op "sign in". Echte titels als "License", "Trial" of "Sign in" blijven passen. | Feit | Hoog | De regex-tekst in het diff. |
| 3 | `structuurBij` roept nu `geenLicentievenster(naam)` aan als de structuurweergave na focus niet bij het bestand hoort (ook bij een lege structuur). Dat geeft een duidelijke reden in plaats van alleen "structuur klopt niet". | Feit | Hoog | Het diff. |
| 4 | De functie `geenLicentievenster` zelf staat niet in het diff. Dat die bestaat en zo heet, haal ik alleen uit de doc-regel erboven. | Vermoeden | Midden | Een groene compileer- en e2e-run na deze commit. |
| 5 | Dat deze test nu in CLion en IDEA groen is, valt niet uit de tekst te halen. De genoemde run 45107087865 is van vóór de wijziging. | Vermoeden | Midden | Een nieuwe e2e-run op bf388f3 met de verwachte uitkomst. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er wordt een testhulp aangepast. Dat maakt de controle op één punt strenger (extra check) en op een ander punt iets nauwer (woordbegin). Het lijkt een echte oorzaak te verhelpen, geen test die slaagt door verzwakken. | Vermoeden | Midden | Tests niet aangepast om te slagen |
| 2 | Beide bestanden krijgen hooguit enkele regels erbij. Of ze onder de ±400 regels blijven, kan ik uit het diff niet zien. | Vermoeden | Laag | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet aangepast. Dat is gerechtvaardigd, want alleen de e2e-hulp verandert. | Feit | Midden | architectuur.md bijgewerkt |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in het diff. | Feit | Hoog | Geen persoonsgegevens |
| 5 | Het commentaar noemt een runnummer als bewijs. Dat is een verwijzing, geen cijfer dat een label nodig heeft. | Feit | Midden | Cijfers met GEZIEN/DERDEN/GOK |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Niets te zien of te spelen: dit is alleen testcode. Er is geen gebruikerseffect, dus geen oordeel over plezier of beeld. | Niet van toepassing | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Wacht op een groene e2e-run op bf388f3 (CLion en IDEA, licht en donker) en controleer daarin dat `geenLicentievenster` bestaat en bij de lege structuur de bedoelde reden geeft.
- Overweeg een kleine eigen test voor de regex (voorbeeld: "Design info" mag niet matchen, "License Agreement" wel). Zo blijft "woordbegin" bewaakt.
- Een nauwere regex kan titels missen waar het trefwoord midden in een woord zit. Let daarop als een licentievenster ooit onopgemerkt blijft.

---
Automatische keurder, model `claude-sonnet-5-5`, 18892 tokens in, 2400 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
