# Keuring e2e-terugtype structuurweergave (Bison & Flex), 23-11-2026, automatische keurder
Wat ik keurde: commit 810099bbc, bestand `producten/jetbrains-bison-flex/e2e/kotlin/com/dortus/bisonflex/e2e/StructuurEnZweven.kt` (opgegeven bereik 06c29cb..6c95120)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen testcode (een e2e-hulpbestand). Plugincode, winkeltekst en belofte in `plugin.xml` blijven gelijk, dus geen afwijking van de belofte. | Feit | Hoog | Een diff van `src/` en `plugin.xml` die leeg is. Die is niet meegestuurd. |
| 2 | Het terugtype van `getStructureViewWrapper()` gaat terug van `StructuurWrapperAlgemeen?` naar `StructuurWrapperOpAfstand?`. De commit en de opmerking zeggen dat de eerdere variant `null` gaf in 263 (run 45095465886) en dat het oude type werkte (run 45087195189). | Vermoeden | Midden | Een groene e2e-run op 263 met deze commit, plus de definitie van `StructuurWrapperOpAfstand`, die in de diff niet staat. |
| 3 | Als de wrapper `null` is, schrijft de test nu een regel naar het log en geeft hij `null` terug, zoals daarvoor. Het gedrag is dus gelijk en alleen beter te volgen. | Feit | Hoog | Niet nodig. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen assertie weggehaald of verzwakt. Alleen het type van een Driver-verwijzing is aangepast, plus een `println`. Dat is geen aanpassing om te slagen. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | De bestandslengte is niet te zien (de diff is klein, het bestand zelf niet meegestuurd). | Vermoeden | Laag | Bestanden onder ±400 regels |
| 3 | `architectuur.md` hoeft niet mee te veranderen: het gaat om een e2e-detail zonder gevolgen voor de opbouw van de plugin. | Feit | Midden | architectuur.md bijgewerkt |
| 4 | Geen persoonsgegevens, sleutels of wachtwoorden in de diff. De genoemde run-nummers zijn geen geheimen. | Feit | Hoog | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden? (alles wat je kunt zien of spelen)
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Niets zichtbaar voor een gebruiker: alleen testcode. Ik kan hier niets over de IDE zelf zeggen. | Niet van toepassing | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer dat de e2e-run op 263 groen is voor deze commit. Het bewijs in de commitregel is van eerdere runs en staat niet in de tekst die ik kreeg.
- De opgegeven commitreeks (06c29cb..6c95120) en de genoemde commit (810099bbc) komen niet zichtbaar overeen. Controleer dat er niets anders in de reeks zit dat niet is meegestuurd.
- Zet bij het `println` een duidelijke melding of een korte wachttijd als het venster nog niet gemaakt is, zodat een `null` door timing niet als echte fout wordt gelezen.

---
Automatische keurder, model `claude-sonnet-5-5`, 18888 tokens in, 1910 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
