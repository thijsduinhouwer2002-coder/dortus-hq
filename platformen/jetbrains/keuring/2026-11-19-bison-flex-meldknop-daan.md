# Voorkeuring meldknop en error handler Bison & Flex (R5), 19 nov 2026 ±04:30 NL, Daan
Wat ik keurde: plek en tekst van de Help-regel en de error handler op main ebd1f7d (`plugin.xml` regels 87 tot 99, `melden/Melden.kt`, `CHANGELOG.md` onder Unreleased). Geen scherm gezien: de Help-regel is een gewone menuregel van de IDE, dus de code zegt hier genoeg.
Akkoord voor plek en tekst: ja. Dit is nog geen akkoord voor de uitgave: dat volgt als de twee regels in de change-notes van `plugin.xml` staan en de CLion- en e2e-run op die commit groen zijn.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Plek: onderaan het Help-menu (`HelpMenu`, `anchor="last"`). Daar zoekt iemand met een probleem; het zit niemand in de weg. | feit (code) | hoog | |
| 2 | Tekst: `&amp;&amp;` wordt in een actietekst één `&`, dus in beeld "Report a Problem with Bison & Flex...". Duidelijk welke plugin, drie puntjes omdat er een browser opent. | feit (IntelliJ-regel voor ezelsbruggetjes) | hoog | Eén scherm van het Help-menu |
| 3 | De melding vraagt drie dingen in gewoon Engels (wat gebeurde, wat verwachtte je, stappen) en zet versie, IDE en OS eronder, zonder gebruikersnaam of paden. | feit (code) | hoog | |
| 4 | De loketrepo `bison-flex` bestaat (GEZIEN, git ls-remote, main be5bb5a) maar heeft alleen een README, geen issueformulier. De velden `version`, `ide` en `os` in de link doen dan niets; de body met de versies komt wel in een lege melding. Werkt dus. | feit | hoog | |
| 5 | Of issues in de loketrepo aan staan kon ik niet zien (GitHub-pagina en API gaven 403 via de proxy). Staan ze uit, dan opent de knop een fout. | GOK | laag | Thijs of de hoofdchat opent de link één keer |
| 6 | CHANGELOG zegt dat je in het foutvenster "Report to third-party plugin" kiest. Ik weet niet zeker of de IDE precies die woorden toont. | vermoeden | midden | Een scherm van het foutvenster, of de tekst laten algemener zijn |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er wordt niets vanzelf verstuurd: de gebruiker plaatst de melding zelf, en de error handler vraagt eerst toestemming in het foutvenster. | feit (code en JetBrains-werking) | hoog | eerlijk |
| 2 | De link noemt de accountnaam van Thijs (`thijsduinhouwer2002-coder`). Die staat al openbaar in de repo's en is geen persoonsgegeven uit regel 2, maar een orgnaam zou netter zijn. | feit | hoog | harde regel 2 (geen overtreding) |

## Moet
Geen voor plek en tekst.

## Kan (mag later)
1. Schrijf in CHANGELOG en change-notes de foutvenster-zin zonder knoptekst, bijvoorbeeld: "If the IDE shows an error from Bison & Flex, you can send it to us from the error dialog." Dan klopt hij hoe de IDE de knop ook noemt.
2. Laat iemand de link één keer openen om te zien dat issues aan staan (A5).
3. Zet de zin "Nothing is sent until you submit it yourself" ook in de change-notes; die neemt de angst weg.
