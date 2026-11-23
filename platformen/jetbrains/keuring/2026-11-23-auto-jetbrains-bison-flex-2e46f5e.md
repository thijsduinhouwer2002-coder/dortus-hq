# Keuring change-notes Bison & Flex 2026.1.2, 23-11-2026, automatische keurder
Wat ik keurde: commit 2e46f5e67 (CHANGELOG.md en change-notes in plugin.xml), reeks 50b5555..2e46f5e
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De change-notes kondigen nu de meldknop (Help > Report a Problem) en het sturen vanuit het foutvenster aan. Het akkoord van Daan (19 nov) zegt dat die twee uit eb02ba1 nog niet door hem zijn gekeurd en niet in de change-notes horen. | Feit (over de tekst in het ontwerp) | Hoog | Een nieuwe keuring van Daan met `Akkoord: ja` voor deze versie bovenaan `ontwerp.md`. Staat die in het afgekapte deel, dan vervalt dit punt. |
| 2 | De wijziging bevat alleen tekst. Of de meldknop en de foutmelder in de gebouwde plugin zitten, kan ik hier niet zien. | Vermoeden | Midden | Eb02ba1 in de reeks, en de CLion- en e2e-run op de uit te brengen commit. |
| 3 | "Nothing is sent until you submit it yourself" is een privacybelofte aan gebruikers. Of de knop alleen een voorgevulde GitHub-pagina opent, zie ik niet. | Vermoeden | Midden | De code van de meldknop: opent alleen een URL en stuurt niets zelf. |
| 4 | "Checked with Plugin Verifier against ... 2025.3, 2026.2 and CLion 2026.2" staat nu in de change-notes. De 5 van 5 Compatible gold voor een eerdere commit. | Vermoeden | Midden | Een verifier-run op de uit te brengen commit met dezelfde IDE-lijst. |
| 5 | De tekst past bij de belofte (gratis en Pro). De winkelbeschrijving is niet veranderd. | Feit | Hoog | Niets nodig. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Het label "CONCEPT tot keuring Daan" is bij 2026.1.2 weggehaald. Zo lijkt de versie gekeurd terwijl dat voor de nieuwe onderdelen niet zo is (zie A1). | Feit | Hoog | Eerst keuring Daan, dan pas uitbrengen |
| 2 | De korte post staat nog als CONCEPT en alleen via de hoofdchat. Goed. | Feit | Hoog | Spelerstekst alleen als CONCEPT |
| 3 | Er zijn geen tests aangepast en de bestanden zijn klein. Er staan geen persoonsgegevens of sleutels in. | Feit | Hoog | Tests, bestandsgrootte, privacy |
| 4 | `architectuur.md` is in deze wijziging niet bijgewerkt. Het zichtbare begin spreekt nog van versie 0.2 en noemt de meldknop niet. | Vermoeden (stuk was afgekapt) | Laag | Controleer of de meldknop en foutmelder in `architectuur.md` staan. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De change-notes zijn nu twee alinea's, met "Also in 2026.1.2" op de tweede. Dat leest rustig. | Niets nodig. | klein |
| 2 | Het foutvenster heet in de IDE waarschijnlijk iets als "Report to third-party plugin". De tekst "send it to us from the error dialog" zegt niet welke knop. | De knopnaam letterlijk noemen, zoals de vorige tekst deed. | klein |
| 3 | De meldknop zelf heb ik niet kunnen zien. Ik kan dus niets zeggen over de ervaring in het menu of op de GitHub-pagina. | Daan of Iris kijkt naar het menu-item en de voorgevulde pagina. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Daan keurt de meldknop en de foutmelder (eb02ba1) en zet `Akkoord: ja` voor deze versie bovenaan `ontwerp.md`. Tot dan horen ze niet in de change-notes en mag het label CONCEPT niet weg (A1, B1).
2. Verifier-run op de uit te brengen commit, zodat "Checked with Plugin Verifier ..." klopt (A4).

**Kan**
1. De privacybelofte over de meldknop naast de code leggen (A3).
2. De knopnaam in het foutvenster noemen in de change-notes (C2).
3. `architectuur.md` bijwerken met de meldknop en de foutmelder (B4).

---
Automatische keurder, model `claude-sonnet-5-5`, 19687 tokens in, 3142 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
