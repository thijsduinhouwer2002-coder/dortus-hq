# Keuring e2e-licentievenster en EAP-keuze Bison & Flex, 23-11-2026, automatische keurder
Wat ik keurde: commit 4dce0bfc8 (reeks a0d246f..240c950), bestanden `e2e/.../Gedeeld.kt` en `e2e/.../IdeTest.kt` van `producten/jetbrains-bison-flex`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Dit is alleen testwerk. De belofte in `ontwerp.md` (bestandssoorten, kleuren, Pro) verandert niet, en er is geen productcode of winkeltekst gewijzigd. | Feit | hoog | De diff raakt alleen `e2e/`. |
| 2 | `geenLicentievenster` zoekt via xdotool een zichtbaar venster met een licentie-achtige titel. Dan maakt het een schermafbeelding en laat het de test falen met een duidelijke reden. Er wordt niets aangeklikt. Dat past bij het doel in de commit. | Feit | hoog | Code gelezen. Een run met zo'n venster zou het bevestigen. |
| 3 | De commit zegt ook dat de week-test geen bugfix-EAP meer kiest en de nieuwste EAP aan de Plugin Verifier geeft. Die wijziging zit niet in de meegestuurde bestanden (waarschijnlijk een workflow). Ik kan dat deel dus niet keuren. | Vermoeden | midden | Het workflowbestand in dezelfde commit, of een run waarin de EAP-keuze zichtbaar is. |
| 4 | De test noemt de bugfix-EAP 263.8311.30 als oorzaak van "No subscription" en "Bison & Flex, Activate to enable". Dat staat nergens bewezen als alleen een EAP-eigenschap. Het kan ook gedrag van onze product-descriptor zijn. Dan zou een gebruiker op die IDE hetzelfde zien, terwijl de test het wegzet als niet onze fout. | Vermoeden | laag | Dezelfde test op een vaste, stabiele 2026.3-versie. Als het venster daar niet komt, is het de EAP. |
| 5 | De licentiecontrole draait ook vóór `waitForIndicators`. Een kortstondig venster met bijvoorbeeld "trial" of "sign in" in de titel kan een goede run rood maken. De regex is ruim: "sign ?in" past ook op "design in". | Vermoeden | laag | Een paar groene runs op de vaste versie zonder vals alarm. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De test wordt strenger, niet slapper. Er wordt niets weggehaald of afgezwakt om te slagen. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | In de commentaarregel staat een run-nummer met GEZIEN. Dat is een eigen waarneming met bron. De andere twee run-nummers (45093981465, 45099923752) staan in de bestaande context. | Feit | midden | Cijfers met GEZIEN/DERDEN/GOK |
| 3 | Geen persoonsgegevens of sleutels in de diff. | Feit | hoog | Geen persoonsgegevens |
| 4 | De bestandslengte van `Gedeeld.kt` en `IdeTest.kt` kan ik uit de diff niet halen. `Gedeeld.kt` heeft minstens 170 regels. | Vermoeden | laag | Bestanden onder ±400 regels |
| 5 | `architectuur.md` is niet bijgewerkt. In het meegestuurde stuk staat niets over de e2e-hulpjes, maar het is afgekapt. Voor een testhulpje is dat hooguit een kan-punt. | Vermoeden | laag | architectuur.md bijgewerkt |
| 6 | De commit noemt hash 4dce0bfc8, terwijl het bereik eindigt op 240c950. Waarschijnlijk dezelfde reeks onder een andere vorm. | Vermoeden | laag | Duidelijk wat er gekeurd is |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Geen gebruikerszichtbare wijziging, dus niets te beoordelen als speler of koper. | Niet van toepassing. | klein |
| 2 | Wat een gebruiker op een nieuwe IDE-versie ziet bij "Activate to enable" is hier juist de vraag (zie A4). | Eén controle op een stabiele IDE, met schermafbeelding. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer op een vaste, stabiele 2026.3 of "No subscription" en "Activate to enable" echt alleen op de bugfix-EAP komen (A4). Zo niet, dan is het een echte productfout.
- Maak de regex strakker, bijvoorbeeld op hele woorden, om vals alarm te voorkomen (A5).
- Laat het workflowbestand voor de EAP-keuze en de Plugin Verifier de volgende keer meesturen (A3).
- Controleer of `architectuur.md` een korte regel over deze e2e-hulp nodig heeft (B5).

---
Automatische keurder, model `claude-sonnet-5-5`, 19670 tokens in, 3485 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
