# Keuring Bison & Flex plugin.xml (linkrij en studentenzin), 23-11-2026, automatische keurder
Wat ik keurde: commit db02b4f90, bestand `producten/jetbrains-bison-flex/src/main/resources/META-INF/plugin.xml`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De beschrijving krijgt een rij met twee links (Manual, Report a problem). De oude regel "More at ... / or a bug" is weg en de mailregel zegt nu alleen "Questions". De HTML is netjes dicht. | Feit | hoog | Niets nodig, staat in de diff. |
| 2 | De link "Manual" wijst naar dortus.com/bison-flex/. Of daar een handleiding staat of alleen een productpagina, zie ik niet. | Vermoeden | laag | Eén keer openen met `curl`. Staat er geen handleiding, noem de link "Website". |
| 3 | De link "Report a problem" gaat naar de issues van de loketrepo. Of issues daar aan staan is nog niet gezien (open kan uit het ontwerp). Deze link staat nu ook in de openbare winkeltekst. | Vermoeden | midden | De link één keer openen en zien dat "New issue" bestaat. |
| 4 | "Learning compilers? The free features cover your course." belooft meer dan de rest van de tekst. Een practicum gebruikt vaak grammatica én scanner samen, en springen en hernoemen over beide bestanden is juist Pro. | Vermoeden | midden | Een echte practicumopdracht met Bison en Flex. Lukt die met alleen het gratis deel, dan klopt de zin. |
| 5 | Het akkoord van Daan geldt voor uitgave 2026.1.2 op 2e46f5e2. De winkeltekst is nu anders, en die is de bron voor poster en plaatjes. De commit zegt zelf dat de keuring naar Daan gaat. | Feit | hoog | `Akkoord: ja` van Daan voor deze tekst, vóór de volgende upload. |
| 6 | Er is geen versienummer of change-note veranderd. De nieuwe tekst bereikt de winkel dus pas bij de volgende upload of een handmatige aanpassing. | Vermoeden | midden | Kijken hoe Jet de beschrijving bijwerkt (nieuwe versie of Marketplace-bewerking). |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen testbestand aangeraakt. Er is dus ook niets aangepast om te slagen. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | De wijziging is 5 regels erbij en 3 eraf in plugin.xml. De totale lengte van het bestand zie ik niet, maar dit schuift het niet richting 400. | Vermoeden | midden | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet bijgewerkt. Voor een tekstwijziging lijkt dat niet nodig, maar het afgekapte deel kon ik niet nalopen. | Vermoeden | laag | architectuur.md bijgewerkt |
| 4 | plugin.xml bevat een e-mailadres (stond er al) en nu in de issues-link een GitHub-accountnaam die op een persoonsnaam lijkt. Ik schrijf ze niet over. | Feit dat ze er staan, vermoeden of dat zo bedoeld is | midden | Geen persoonsgegevens |
| 5 | De studentenzin heeft geen bronlabel. Er staan verder geen cijfers in de wijziging. | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 6 | De wijziging bevat geen beeld, geluid of spelerstekst. Dit onderdeel geldt dus niet. | Feit | hoog | Geen AI-beeld of -geluid, Hats-concept |

## Deel C: zou een gebruiker het leuk en fijn vinden? (alles wat je kunt zien of spelen)
Ik zie alleen tekst. Dit zijn aannames over de koper, geen gezien resultaat.
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | De linkrij vroeg in de tekst helpt wie vastloopt. De sentence case in "Report a problem" past bij de JetBrains-regel voor links. | Laten staan. | klein |
| 2 | De studentenzin staat vóór de Free-lijst, dus de student leest de belofte voordat hij weet wat gratis is. | Zet de zin onder de lijst, of schrijf "The free list below covers most coursework." | klein |
| 3 | Een student ziet "gratis" en later toch een Pro-melding bij springen over beide bestanden. | Zeg erbij dat het gratis deel na de proef blijft werken. Dat staat al in het ontwerp. | klein |
| 4 | Melden kan nu alleen via GitHub of mail, de mail heet "Questions". Wie geen GitHub gebruikt, ziet niet dat mail ook voor een bug mag. | "Questions or feedback" in de mailregel. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Daan keurt de nieuwe winkeltekst voor de volgende upload. Zijn akkoord op 2e46f5e2 dekt deze tekst niet.
- Open de issues-link en de Manual-link één keer voor de upload (A2, A3).
- Maak de studentenzin eerlijker of zet hem na de Free-lijst (A4, C2).
- Controleer of de GitHub-accountnaam in de openbare link zo bedoeld is (B4).
- Zet in de mailregel weer "bug" of "feedback" erbij (C4).

---
Automatische keurder, model `claude-sonnet-5-5`, 18531 tokens in, 6609 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
