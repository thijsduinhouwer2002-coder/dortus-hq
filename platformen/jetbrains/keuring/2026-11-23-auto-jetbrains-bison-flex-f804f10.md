# Keuring Bison & Flex beschrijving in plugin.xml (linkrij en studentenzin), 23-11-2026, automatische keurder
Wat ik keurde: commit db02b4f90, bestand `producten/jetbrains-bison-flex/src/main/resources/META-INF/plugin.xml` (reeks 7ea796e..f804f10)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|-----------|-------------------|------------------------------|--------------------------------------|
| 1 | De beschrijving houdt de kernbelofte gelijk: wat, voor wie en de lijst Gratis en Pro zijn niet geraakt. Alleen een linkrij en één zin zijn erbij gekomen, en het contactregeltje is korter. | Feit | Hoog | De diff toont alleen die drie wijzigingen. |
| 2 | "The free features cover your course" is een nieuwe belofte die niet in het ontwerp staat. Een practicum met grammatica én scanner heeft juist de Pro-functie (springen over beide bestanden) nodig. | Vermoeden | Midden | Een voorbeeldopdracht van een compilercursus (bijvoorbeeld calc.y met calc.l) door de gratis functies halen. |
| 3 | De link "Report a problem" wijst naar de issues van de loketrepo. Of issues daar aan staan is nog niet gezien (staat al als open kan in het ontwerp). | Vermoeden | Midden | De link één keer openen en zien dat "New issue" werkt. |
| 4 | De link "Manual" wijst naar dortus.com/bison-flex/. Of die pagina een handleiding bevat is uit de tekst niet te halen. | Vermoeden | Laag | De pagina ophalen met `curl` en kijken of er uitleg staat. |
| 5 | Het mailadres is niet meer gekoppeld aan "a bug", want bugs lopen nu via de GitHub-link. Dat past bij de nieuwe meldknop. | Feit | Hoog | Geen controle nodig. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|-----------|-------------------|-----------|-------|
| 1 | Er is geen testbestand aangepast en het bestand blijft klein. De wijziging raakt geen code, dus `architectuur.md` hoeft niet bij. | Feit | Hoog | Tests en bestandsgrootte, architectuur.md |
| 2 | In plugin.xml staat een e-mailadres (bestond al) en de nieuwe link bevat een accountnaam die op een persoonsnaam lijkt. Beide zijn bewust openbaar, maar het is wel zichtbaar in de winkel. | Feit | Midden | Geen persoonsgegevens |
| 3 | Het akkoord van Daan geldt voor 2026.1.2 op 2e46f5e2. Dit is nieuwe winkeltekst daarna, en het ontwerp zegt dat Daan nieuwe tekst eerst nakijkt. De commit meldt dat de keuring naar Daan gaat. | Feit | Hoog | Ontwerp: nieuw zichtbaar werk eerst naar Daan |
| 4 | De versie in plugin.xml is niet verhoogd. Of 2026.1.2 al is geüpload, is uit de tekst niet te zien. Is dat zo, dan komt deze beschrijving pas in de winkel met een nieuwe upload. | Vermoeden | Laag | Eén bron voor winkeltekst en changelog |

## Deel C: zou een gebruiker het leuk en fijn vinden? (alles wat je kunt zien of spelen)
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|-----------|---------------------|-----------------------------|
| 1 | De zin voor studenten spreekt een grote groep direct aan, en dat is nieuw. Hij zegt alleen niet wat er gratis is. | Maak hem concreet: "Learning compilers? Highlighting, syntax errors and navigation within a file are free." | Klein |
| 2 | De linkrij staat boven de lijst Gratis en Pro, dus de koper moet verder scrollen voor de inhoud. Dat is vermoedelijk geen probleem bij korte tekst. | Zet de linkrij onderaan bij het contactregeltje, of laat hem staan als Daan het in beeld goed vindt. | Klein |
| 3 | De tekst kan niet worden gezien zoals de koper hem ziet (de entiteit `&middot;` in de HTML is niet bekeken). | Pluginpagina of het pluginvenster van de IDE bekijken. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Maak de studentenzin concreet of haal "cover your course" weg (A2, C1), want Pro hoort bij een cursus met grammatica én scanner.
- Open de meldlink en de Manual-link één keer en zie dat ze werken (A3, A4).
- Uitbrengen pas na een nieuw `Akkoord: ja` van Daan op deze tekst (B3).
- Kijk na of deze beschrijving met een nieuwe upload mee moet (B4).
- Overweeg een organisatieaccount voor de issues-link in plaats van een account met een persoonsnaam (B2).

---
Automatische keurder, model `claude-sonnet-5-5`, 18531 tokens in, 4172 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
