# Keuring Bison & Flex architectuur (beeldbericht weer aan), 19-11-2026 08:45 NL, automatische keurder
Wat ik keurde: commit f1d52cc6 (reeks 8a440ce..f1d52cc), bestand `producten/jetbrains-bison-flex/architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|-----------|-------------------|------------------------------|--------------------------------------|
| 1 | De wijziging raakt alleen de beschrijving van de week-test en beeldvergelijking. Code, plugin.xml en de winkelbelofte (bestandssoorten, gratis en Pro) blijven ongewijzigd. De belofte uit het ontwerp wordt dus niet geraakt. | Feit | Hoog | De lijst met gewijzigde bestanden bevat alleen `architectuur.md`. |
| 2 | De tekst zegt dat de job `beeldbericht` nu aan staat en dat `if: false` eruit is. De workflow-wijziging zelf zit niet in deze reeks. Of `.github/workflows/jetbrains-bison-flex-e2e.yml` echt `if: false` kwijt is, kan ik niet zien. | Vermoeden | Midden | Als de workflow op f1d52cc geen `if: false` meer bij `beeldbericht` heeft, klopt de tekst. Dat is dan in een eerdere commit gebeurd. |
| 3 | De bewering "twee runs van dezelfde code gaven 0 grote verschillen" (runs 44478690203 en 44478693136) is gelabeld als GEZIEN. Ik kan die runs vanuit de tekst niet nalopen. De aanpak (twee push-runs, daarna aanzetten) volgt wel de eerdere afspraak in de oude tekst. | Vermoeden | Midden | Het `BEELDVERSCHIL.md` van beide runs op de tak `schermen` met 0 grote verschillen. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|-----------|-------------------|-----------|-------|
| 1 | `architectuur.md` is bijgewerkt met de nieuwe stand van de beeldvergelijking. Het afwijkende "staat uit" is vervangen door wat er nu gebeurt. | Feit | Hoog | architectuur.md bijgewerkt |
| 2 | Er zijn geen tests aangepast of weggehaald. | Feit | Hoog | Tests niet aangepast om te slagen |
| 3 | De nieuwe cijfers (runnummers) staan als GEZIEN gemarkeerd. Er staan geen persoonsgegevens of sleutels in de wijziging. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK, geen persoonsgegevens |
| 4 | De kop van het document zegt nog "Stand 8 nov 2026: versie 0.2", terwijl de changelog bij 2026.1.2 is. Het document zelf is erg lang. Of het onder de grens van ±400 regels blijft, kan ik niet zien. | Vermoeden | Laag | architectuur.md bijgewerkt, bestandsgrootte |
| 5 | Geen AI-beeld of -geluid voor Steam en geen spelerstekst van Hats. Niet van toepassing. | Feit | Hoog | Regels voor Hats en Steam |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Controleer dat de workflow echt aan staat. `if: false` bij `beeldbericht` moet weg zijn op main, anders klopt de architectuurtekst niet (A2).
2. Zet de runnummers bij de beweringen over 0 grote verschillen naast het `BEELDVERSCHIL.md` op de tak `schermen` (A3).
3. Werk de kop "Stand 8 nov 2026: versie 0.2" bij naar de huidige stand (B4).
4. Splits `architectuur.md` als het bestand ruim boven 400 regels uitkomt. De week-test-alinea is al één heel lange regel en leest slecht (B4).

---
Automatische keurder, model `claude-sonnet-5-5`, 20893 tokens in, 2332 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
