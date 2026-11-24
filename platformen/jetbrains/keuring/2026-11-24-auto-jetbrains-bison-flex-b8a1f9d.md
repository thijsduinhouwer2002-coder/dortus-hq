# Keuring e2e: platformfout bij Previous Conflict, 24-11-2026, automatische keurder
Wat ik keurde: commits 1ccdcd4..b8a1f9d (b8a1f9d56), bestanden `e2e/.../Gedeeld.kt` en `e2e/.../PlatformfoutTest.kt` van `jetbrains-bison-flex`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen de e2e-testmap. De plugin, `plugin.xml` en de belofte uit het ontwerp blijven ongewijzigd, dus de eerdere goedkeuring van Daan voor 2026.1.2 blijft gelden. | Feit | hoog | De lijst van gewijzigde bestanden bevat geen bestand onder `src/main`. |
| 2 | Het filter laat nu ook "argument is not a child" door, mits `OccurenceNavigatorSupport` in de melding staat. Dat past bij de beschreven fout van de knop "Previous Conflict" in run 45305066655. | Vermoeden | midden | Run 45305066655 in het log: dezelfde stack, en een nieuwe e2e-run die niet meer faalt op deze fout. |
| 3 | De nieuwe test geeft als melding "PreviousOccurenceToolbarAction" mee en zet de foutregel alleen in de stack. Hij slaagt alleen als `bekendePlatformfout` ook in de details zoekt. De functie staat niet in de wijziging. | Vermoeden | midden | Een groene run van `PlatformfoutTest`, of de body van `bekendePlatformfout` lezen. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Het filter is losser gemaakt van "node is not a child" naar "is not a child". Dat is een versoepeling van een test, maar die is onderbouwd: er staat een run-nummer, een uitleg in de commentaar en een nieuwe test. Het filter eist nog steeds `OccurenceNavigatorSupport`. | Feit | hoog | Tests niet aanpassen om te slagen |
| 2 | De bestaande test `bekendeFoutMetPluginInDeStackFaaltNog` blijft staan. Een echte fout van Bison & Flex (com.dortus) in dezelfde stack blijft dus falen. | Feit | hoog | Tests niet aanpassen om te slagen |
| 3 | Beide bestanden zijn klein: de diff telt ongeveer 15 regels, ver onder de 400. | Feit | midden | Bestanden onder ±400 regels |
| 4 | Er staan geen persoonsgegevens, sleutels of cijfers zonder label in de wijziging. `architectuur.md` is niet aangepast. Dat is hier waarschijnlijk niet nodig, omdat het alleen een testfilter is, maar ik zie niet of de e2e-opzet daar staat. | Vermoeden | laag | Kijken of `architectuur.md` het e2e-filter noemt. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Niets om te zien of te spelen: dit is alleen testinrichting, de gebruiker merkt er niets van. | Niets nodig | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Bevestig met een groene e2e-run of unittest-run dat de nieuwe test echt slaagt (zie A3). Ik kon niets draaien.
2. Als dit filter nog een keer breder moet, zet de bekende platformfouten dan als vaste lijst in `architectuur.md`, zodat zichtbaar blijft welke fouten bewust worden overgeslagen.
3. Houd bij of het platform dit gedrag in een nieuwere IDE herstelt. Dan kan het filter weer weg.

---
Automatische keurder, model `claude-sonnet-5-5`, 19158 tokens in, 2267 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
