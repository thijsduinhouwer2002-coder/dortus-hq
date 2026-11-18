# Keuring blender-gewrichten (bug.yml, privacyzin), 19-11-2026, automatische keurder
Wat ik keurde: commit 8fa9e1f6, bestand producten/blender-gewrichten/loket/.github/ISSUE_TEMPLATE/bug.yml
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De enige wijziging in dit bestand is één extra regel in het intro-blok: een waarschuwing dat meldingen openbaar zijn en dat je je naam of gebruikersmap uit bestandspaden moet halen. Dat past bij het doel van het formulier (meldingen van gebruikers, zonder persoonsgegevens). | Feit | Hoog | De diff toont alleen deze regel erbij. |
| 2 | De regel staat binnen het bestaande `value: \|`-blok met dezelfde inspringing als de regel erboven. Het YAML-schema zou dus geldig moeten blijven. | Vermoeden | Midden | Een controle van het formulier tegen het GitHub-schema, of de eerste echte melding in de loketrepo. De commitnaam noemt dit niet. |
| 3 | De bestandsnaam in de tekst is een voorbeeld (`C:\Users\yourname`), geen echt pad. | Feit | Hoog | De diff. |
| 4 | De opdracht en de andere genoemde commitwijzigingen (Obsidian-versie getest, test gebruikersnaam robuuster) zitten niet in de meegestuurde diff. Ik kan daar niets over zeggen. | Feit | Hoog | De volledige diff van 8fa9e1f6 en de testlog. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. De waarschuwing helpt juist te voorkomen dat gebruikers die in een publieke melding zetten. | Feit | Hoog | Geen persoonsgegevens |
| 2 | Er is geen test aangepast en er zijn geen cijfers zonder label toegevoegd. | Feit | Hoog | Tests niet aangepast om te slagen; cijfers met GEZIEN/DERDEN/GOK |
| 3 | Het bestand is klein, ruim onder de 400 regels. | Feit | Hoog | Bestanden onder ±400 regels |
| 4 | `architectuur.md` en CHANGELOG zijn niet in deze diff gewijzigd, maar `architectuur.md` beschrijft de formulieren al. Er is geen nieuw gedrag dat de architectuur verandert. | Feit | Midden | architectuur.md bijgewerkt |
| 5 | De tekst is Engels, zoals de rest van het formulier en het paneel voor kopers. Geen AI-beeld of -geluid. | Feit | Hoog | Geen AI-beeld of -geluid op Steam |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer het formulier opnieuw tegen het GitHub-schema na deze wijziging (deel A, rij 2), want in de meegestuurde tekst staat daar geen bewijs van.
- Voeg de gebruikersnaam-waarschuwing ook toe aan `idea.yml`, als daar ook tekst of foto's geplakt kunnen worden. Dat bestand zag ik niet.

---
Automatische keurder, model `claude-sonnet-5-5`, 17108 tokens in, 1323 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
