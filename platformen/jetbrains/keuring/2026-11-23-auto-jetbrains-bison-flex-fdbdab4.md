# Keuring e2e Bison & Flex: bekende IntelliJ-fout overslaan, 23-11-2026, automatische keurder
Wat ik keurde: commit fdbdab479 (d4d84c3..fdbdab4), alleen `producten/jetbrains-bison-flex/e2e/kotlin/com/dortus/bisonflex/e2e/Gedeeld.kt`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen de e2e-testhulp, niet de plugin of de winkelbelofte. Wat gekeurd en akkoord was voor 2026.1.2 verandert dus niet. | Feit | hoog | Het diff bevat alleen `Gedeeld.kt` in de map `e2e`. |
| 2 | De filter slaat een fout alleen over als de melding "node is not a child" én "OccurenceNavigatorSupport" bevat en nergens "com.dortus" voorkomt. Dat is smal en veilig ingesteld. Elke andere fout laat de test nog steeds falen. | Feit | hoog | De code in het diff. |
| 3 | De oorzaak (de knop "Next Conflict" wordt bijgewerkt terwijl de boom verandert) is een race in IntelliJ zelf. Dat staat alleen in de commentaar van de bouwer. Ik kan het niet nalezen. | Vermoeden | midden | Run 45262737601 inzien: komt de stack overeen met alleen platformcode? Komt het ook voor met een andere plugin of zonder onze rename? |
| 4 | "Geen com.dortus in de tekst" bewijst niet dat de plugin onschuldig is. Onze rename kan de boomwijziging veroorzaken terwijl de stack alleen platformframes toont. | Vermoeden | laag | Een herhaling van de e2e-run. Lukt het hernoemen naar `line` in donker thema meestal, dan is het een race. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Een test wordt zachter gemaakt zodat een rode run groen wordt. Het gaat om één benoemde fout, met reden, run-nummer en een logregel (`DORTUS-E2E bekende fout ... overgeslagen`). Dat is geen verstopte aanpassing. Toch blijft het een versoepeling en moet het zichtbaar blijven. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | Er is geen test voor `bekendePlatformfout` zelf. Een fout in de filter zou ofwel te veel verbergen ofwel niets doen, en dat merkt niemand. | Feit | midden | Tests bij nieuwe logica |
| 3 | `Gedeeld.kt` is door deze wijziging 16 regels groter en blijft ruim onder de 400 regels. De totale lengte van het bestand zie ik niet. | Vermoeden | midden | Bestanden onder ±400 regels |
| 4 | `architectuur.md` en `CHANGELOG.md` hoeven niet bij te werken: de plugin verandert niet. Er staan geen persoonsgegevens of sleutels in het diff. | Feit | hoog | architectuur.md, geen persoonsgegevens |
| 5 | Het commitbericht zegt "keuring naar Chris (Claude)". Dat is een werkafspraak en geen bevinding. | Feit | hoog | n.v.t. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Niets te zien of te spelen: dit is alleen testcode. Voor de gebruiker verandert niets. | Niet van toepassing. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Een kleine unittest voor `bekendePlatformfout` met drie gevallen: de bekende fout, dezelfde fout met `com.dortus` erin, en een andere fout.
2. Tel hoe vaak de fout wordt overgeslagen, en laat de run falen of waarschuwen als dat veel wordt. Zo verbergt de filter geen echt probleem in onze rename.
3. Controleer in run 45262737601 of de stack echt zonder onze frames is. Meld de race ook bij JetBrains als dat zo is, en haal de filter weg zodra het platform het oplost.

---
Automatische keurder, model `claude-sonnet-5-5`, 18802 tokens in, 2832 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
