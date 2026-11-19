# Keuring Rollwright beeldvergelijking (architectuur.md), 19-11-2026, automatische keurder
Wat ik keurde: commit 75de19b4 (c2c894c..75de19b), alleen `producten/obsidian-rollwright/architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht in `ontwerp.md` gaat over de plugin zelf (versie 0.3.5) en zegt niets over de beeldvergelijking. Ik toets daarom of de wijziging klopt met haar eigen commitbericht.

| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is één alinea in `architectuur.md`. Die zegt nu dat de bestandenlijst links en de tooltip bij Roll op l1 niet meer meetellen als verschil. | Feit | Hoog | Het diff zelf. |
| 2 | Het commitbericht zegt "tellen niet mee", maar het script `organisatie/controle/beelden.sh` zit niet in deze wijziging. Of het script dit echt doet, kan ik niet zien. | Vermoeden | Midden | Het diff van `beelden.sh` in dezelfde of een eerdere commit, of een groene beeldvergelijking op main zonder vals alarm op l1. |
| 3 | Het commitbericht noemt een bericht aan Olaf, maar `berichten/olaf.md` staat niet in de gewijzigde bestanden. | Vermoeden | Midden | Een regel in `berichten/olaf.md` bij deze commit, of een andere commit die het bericht bevat. |
| 4 | De uitgesloten onderdelen zijn bewust smal gehouden: "alleen die tijden, het logboek zelf telt wel". Dat is een goede keuze, want het paneel blijft bewaakt. | Feit | Hoog | Het diff. |
| 5 | De wijziging raakt `src/`, `styles.css` en `manifest.json` niet. De voorwaarde van Daans akkoord voor 0.3.5 blijft dus staan. | Feit | Hoog | De lijst gewijzigde bestanden. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt in dezelfde commit als de gedragswijziging die ze beschrijft. | Feit | Hoog | architectuur.md bijgewerkt |
| 2 | Er is geen test gewijzigd of aangepast om te slagen. | Feit | Hoog | Tests niet aangepast om te slagen |
| 3 | De nieuwe bewering heeft een bron: run 44486124815, gemarkeerd als GEZIEN. Ik kan die run niet openen, dus het label blijft op woord van de bouwer staan. | Vermoeden | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 5 | De alinea is een lange regel, maar die ene regel is niet de oorzaak van een te groot bestand. Het totaal aantal regels van het bestand kan ik niet zien (de tekst is afgekapt). | Vermoeden | Laag | Een telling met `wc -l` op het bestand |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zin repareren: "de melding op m10 die nog binnenschuift de kloktijden in het logboek" mist een komma of het woord "en" voor "de kloktijden". Nu leest het alsof de melding de kloktijden binnenschuift.
- Bij de volgende run controleren dat `beelden.sh` de bestandenlijst en de tooltip op l1 echt negeert, en dat er geen vals alarm meer in `berichten/olaf.md` komt (punt 2 en 3 in deel A).
- "de drie kloktijden" is veranderd in "de kloktijden". Dat is waarschijnlijk bewust, maar controleer of het aantal klopt met het script.

---
Automatische keurder, model `claude-sonnet-5-5`, 20510 tokens in, 2481 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
