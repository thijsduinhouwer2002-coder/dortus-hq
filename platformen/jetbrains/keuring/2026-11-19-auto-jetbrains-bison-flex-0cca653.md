# Keuring jetbrains-bison-flex, 19-11-2026, automatische keurder
Wat ik keurde: commits 1cd470c..0cca653 (0cca653d), alleen `producten/jetbrains-bison-flex/ontwerp.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is alleen tekst in de Akkoord-regel. De belofte en de eisen zijn niet aangeraakt. | Feit | Hoog | Niets nodig: de diff toont één gewijzigde regel. |
| 2 | Het akkoord wordt smaller: het geldt tot en met 281d0a3 en uitdrukkelijk niet voor de meldknop en error handler van R5 (eb02ba1). Dat is voorzichtiger dan voorheen. | Feit | Hoog | Geen. |
| 3 | De regel zegt dat R5 niet in de change-notes staat. De CHANGELOG bevestigt dat: de R5-punten staan onder "Unreleased" en niet onder 2026.1.2. | Feit | Hoog | Geen. |
| 4 | Dat 281d0a3 de laatste gekeurde commit is en eb02ba1 de R5-commit, kan ik uit de diff niet halen. Ik heb de git-geschiedenis niet. | Vermoeden | Midden | `git log` die laat zien dat eb02ba1 de meldknop en error handler bevat en 281d0a3 ervoor ligt. |
| 5 | Het keuringsbestand `platformen/jetbrains/keuring/2026-11-18-bison-flex-2026.1.2-daan.md` en de runs (CLion 65, e2e 145) zijn niet meegestuurd. Ik kan ze niet nakijken. | Vermoeden | Midden | Dat bestand en het log van die runs. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen code- of testwijzigingen, dus er is niets aangepast om een test te laten slagen. De 400-regelsgrens speelt hier niet. | Feit | Hoog | Tests niet aanpassen om te slagen / bestandsgrootte |
| 2 | `architectuur.md` hoeft niet bij, want er is geen code gewijzigd. | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | Het commitbericht noemt ook "berichten Chris en hoofdchat, logboek", maar die bestanden zitten niet in deze wijziging. Dat kan in een andere repo of een andere map staan. | Vermoeden | Laag | Wijziging moet bij de beschrijving passen |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 5 | De Akkoord-regel is door Claude geschreven namens Daan. Het is de afspraak dat Daan zo bovenaan het ontwerp akkoord zet, dus dat mag. Of Daan het echt zo gezegd heeft, zie ik niet. | Vermoeden | Midden | Akkoord van Daan bovenaan ontwerp.md |
| 6 | De Akkoord-regel noemt "Daan 19 nov 00:40 NL", maar deze keuring is van 00:38. Het akkoord is dus twee minuten later gedateerd dan het moment van keuren. Dat kan een klokverschil zijn of een tikfout. | Vermoeden | Midden | De werkelijke commit-tijd van 0cca653 (`git show`). |
| 7 | In de CHANGELOG staat 2026.1.2 nog als "CONCEPT tot keuring Daan", terwijl het akkoord er al is. De regel is afgekapt in wat ik zie, dus ik weet niet of dat later is bijgewerkt. | Vermoeden | Laag | De CHANGELOG op main na dit commit. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
- Geen.

**Kan**
- Controleer de tijd "00:40 NL" in de Akkoord-regel. Hij ligt na het keurmoment van 00:38 en moet de echte tijd van het akkoord zijn.
- Haal "CONCEPT tot keuring Daan" bij 2026.1.2 in de CHANGELOG weg, als dat nog niet gebeurd is.
- Maak duidelijk waar de berichten aan Chris, de hoofdchat en het logboek staan, die het commitbericht noemt.
- Laat bij het volgende akkoord Daan (of de keurder) eb02ba1 apart keuren, want dat blijft nu buiten het akkoord.

---
Automatische keurder, model `claude-sonnet-5-5`, 18690 tokens in, 2672 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
