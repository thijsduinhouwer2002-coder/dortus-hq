# Keuring blender-gewrichten enkels via More bones (Pro 1.2.5), 24-11-2026, automatische keurder
Wat ik keurde: commits eef079215 en f1307dc61 (7f5feb2..5fe23a8): rig.py, scharnier_vorm.py, e2e/toetsen_mens.py
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Bij een enkel met bovenliggend bot worden de assen van het scheenbot genomen en de plek van het voetbot. Dat past bij de uitleg in de code: de voet staat haaks, dus langs de voetas ligt alleen de hiel. | Feit (uit de code) | hoog | Een groene e2e-run met enkels op robot en MakeHuman. |
| 2 | De bijgewerkte afstandsregel is `min(oude regel, r + eigen + 1 mm)`. Dat is rekenkundig nooit strenger dan voorheen. | Feit | hoog | Staat in de diff. |
| 3 | Dat de stopvlakken van knie en enkel elkaar niet raken, steunt op een meting op MakeHuman 220 mm in 5.3.0. Die meting zie ik niet, alleen de beschrijving. | Vermoeden | midden | Het meetlog van de doorsnedes, of de groene e2e-stap "met enkels: knie nog 0 tot 120". |
| 4 | De regel is nu losser voor alle scharnierparen met ongelijke reik, niet alleen knie en enkel. Op andere figuren is niet getoetst of stopvlakken elkaar dan wel raken. | Vermoeden | laag | Een run op een andere rig (bijvoorbeeld elleboog naast schouder) met controle op bereik. |
| 5 | `m.col[3][:3] = ...` en `stop[1]` van het voetbot, gebruikt als index op het scheenbot, zijn niet uit de tekst te controleren. | Vermoeden | midden | De e2e-stap "enkel geplaatst en buigt minstens 45 graden". |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De test is niet versoepeld. Er zijn alleen nieuwe checks bij gekomen (enkel minstens 45 graden, knie blijft 120). | Feit | hoog | Tests niet aanpassen om te slagen |
| 2 | De nieuwe checks draaien alleen als `CJ_MEER=1` gezet is. In deze diff staat de workflow niet. Zonder die variabele toetst CI de enkels dus nooit. | Vermoeden | midden | Test moet echt draaien |
| 3 | De commit zegt "versie 1.2.5", maar manifest en changelog staan niet in de gewijzigde bestanden. | Vermoeden | midden | Versie en changelog kloppen |
| 4 | `architectuur.md` is niet aangepast, terwijl de afstandsregel en het enkelgedrag veranderden. | Vermoeden | midden | architectuur.md bijgewerkt |
| 5 | De regel met `paren = [...]` is ruim boven de 120 tekens. Bestandsgroottes zijn niet te zien. | Vermoeden | laag | Bestanden onder ±400 regels |
| 6 | Geen persoonsgegevens, sleutels of wachtwoorden gezien. | Feit | hoog | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Beeld en gevoel zijn niet te keuren uit tekst. Een enkel die 45 graden buigt is wel een duidelijke winst voor poppen op robot en MakeHuman. | Iris of Daan kijken naar de enkel op een screenshot (voet naar voren en achter). | klein |
| 2 | De 45 graden is een drempel voor de test. Of de enkel zo ook echt mooi buigt, is niet te zien. | Een beweegbeeld van de enkel in de poster of de uitleg. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
Moet: geen.

Kan:
- Zet `CJ_MEER=1` voor minstens één e2e-run in de workflow, zodat de enkeltoets echt draait (B2).
- Controleer dat manifest en changelog op 1.2.5 staan (B3).
- Werk `architectuur.md` bij met de nieuwe afstandsregel en het enkelgedrag (B4).
- Toets de losse afstandsregel ook op een tweede rig (A4).
- Splits de lange regel in `scharnier_vorm.py` (B5).

---
Automatische keurder, model `claude-sonnet-5-5`, 20055 tokens in, 3371 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
