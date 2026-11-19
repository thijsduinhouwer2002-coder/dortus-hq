# Keuring Rollwright meldformulieren (R5), 19-11-2026, automatische keurder
Wat ik keurde: commit 4ed153d (2a5ebb5..4ed153d), vier bestanden: `architectuur.md` en `bug.yml`, `config.yml` en `idea.yml` onder `loket/.github/ISSUE_TEMPLATE/`
Akkoord: ja

## Deel A: doet het wat beloofd is?
Getoetst tegen de opdracht in `ontwerp.md` en wat `architectuur.md` over het commando "Report a problem" zegt. `report-problem.ts` is niet meegestuurd.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `bug.yml` heeft de veld-ids `version`, `obsidian` en `os`, precies zoals `architectuur.md` zegt dat het commando ze meestuurt. | Feit (uit de diff) | Hoog | Dezelfde ids in `reportUrl` in `report-problem.ts` en in `tests/report-problem.test.ts`. |
| 2 | `version` en `obsidian` zijn verplicht, `os` is optioneel. De placeholders (0.3.5, 1.9.14, Windows (desktop)) laten zien wat er ingevuld moet staan. | Feit | Hoog | Niet nodig. |
| 3 | `architectuur.md` zegt dat de link ook een `body` meestuurt. Een GitHub-formulier heeft geen veld met id `body`, dus die tekst wordt vermoedelijk genegeerd. Of de link `template=bug.yml` meegeeft, is niet te zien. Zonder die parameter kan GitHub de sjabloonkeuze tonen en gaan de ingevulde velden verloren. | Vermoeden | Midden | De opgebouwde URL openen op GitHub (of de URL-test lezen) en kijken of de drie velden gevuld zijn. |
| 4 | De tekst bovenaan waarschuwt dat alles openbaar is en vraagt namen en mappen uit paden te halen. Dat past bij de belofte "geen telemetrie, alleen een link die de gebruiker zelf opent". | Feit | Hoog | Niet nodig. |
| 5 | `idea.yml` en `config.yml` zijn eenvoudig en hebben één verplicht veld. Of de teksten goed lezen voor de gebruiker is niet te beoordelen uit tekst. | Feit (inhoud), smaak (lezen) | Hoog | Niet nodig. |
| 6 | `config.yml` zegt dat het contactadres op `dortus.com/rollwright/` staat. Of die pagina bestaat en het adres toont, is niet te zien. | Vermoeden | Laag | De pagina ophalen met `curl` en zoeken naar het adres. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen tests aangepast, en niets in `src/` of `styles.css` veranderd. Het akkoord van Daan voor 0.3.5 blijft daardoor ongemoeid. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` is bijgewerkt met de nieuwe map, de ids en de opmerking dat `publiceer.sh` `.github` niet meeneemt. | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | De drie nieuwe bestanden zijn kort (60, 8 en 12 regels), ruim onder de 400. | Feit | Hoog | Bestanden onder ±400 regels |
| 4 | Geen sleutels of wachtwoorden. Wel staat de GitHub-accountnaam van de eigenaar in een URL in `config.yml`; die naam lijkt een echte naam met jaartal te bevatten. Het is een publieke repo-link en staat al in `architectuur.md`. Meld ik alleen. | Feit | Midden | Geen persoonsgegevens |
| 5 | `architectuur.md` zegt "geldig tegen het schema van GitHub (GEZIEN 19 nov)". Dat bewijs zit niet in de wijziging. Bij lezen zie ik geen fout in de YAML, dus ik neem het aan. | Vermoeden | Midden | Cijfers en claims met GEZIEN, DERDEN of GOK |
| 6 | Cijfers, spelerstekst van Hats en AI-beeld of -geluid komen in deze wijziging niet voor. | Feit | Hoog | Niet van toepassing |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
1. Controleer of de link van het commando `template=bug.yml` meegeeft. Bij een formulier moet de eigen tekst in een veld (bijvoorbeeld `what`) en niet in `body`. Zo niet, dan landt de voorinvulling niet. Deel A punt 3.
2. Controleer met `curl` dat `dortus.com/rollwright/` het contactadres toont voor je het in `config.yml` belooft. Deel A punt 6.
3. Voeg een kleine test toe die de ids in `bug.yml` vergelijkt met de parameters in `reportUrl`, zodat ze niet uit elkaar lopen.
4. Leg het schema-bewijs (GEZIEN 19 nov) vast, bijvoorbeeld door de validatie of de link naar de run te noemen.
5. De CHANGELOG meldt het commando "Report a problem" onder Unreleased, en het akkoord van Daan geldt alleen voor 0.3.5. Vraag voor de volgende release een nieuw akkoord in `ontwerp.md`.
6. Kijk of de accountnaam in de publieke URL zo bedoeld is. Zo niet, gebruik dan een neutrale organisatienaam.

---
Automatische keurder, model `claude-sonnet-5-5`, 21024 tokens in, 5295 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
