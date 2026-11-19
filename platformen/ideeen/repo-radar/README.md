# Repo-radar

Elke dag kijkt deze bot op GitHub naar nieuwe projecten waarin iemand een plan heeft om geld te verdienen: een app-idee, een SaaS met prijzen, een plugin met een betaalde versie, een wachtlijst. Hij leest de uitleg (README), haalt er het plan uit en zet de beste 25 in een rapport. Wij kijken daarna of het goed is en of wij het ook kunnen maken.

Opdracht van Thijs, 19 nov 2026 17:18. Gratis: alleen de zoekfunctie van GitHub, geen eigen sleutel, geen geld.

## Waar staat het rapport
Op de tak `ideeen-data` van deze repo, niet op main:
- `repo-radar/rapport.md`: het nieuwste rapport
- `repo-radar/<datum>/rapport.md` en `kandidaten.json`: per dag, met alle gegevens per repo en alles wat eruit ging
- `repo-radar/gezien.json`: welke repo's al eens in de top stonden

Lezen vanuit je checkout: `git fetch origin ideeen-data && git show origin/ideeen-data:repo-radar/rapport.md`.

## Hoe het werkt
1. **Zoeken.** 24 zoektermen (saas, side project, indie hacker, monetize, pricing, subscription, MRR, revenue, gumroad, stripe, lemon squeezy, paddle billing, business plan, go-to-market, app idea, startup, landing page, waitlist, pro version, freemium, premium features ...), elk twee keer: repo's van de laatste 2 dagen, en repo's jonger dan 90 dagen die gisteren of vandaag zijn bijgewerkt en minstens 5 sterren hebben.
2. **Ruis eruit op naam:** forks, sjablonen, huiswerk en klonen, crypto-pump, cracks en spam, verzamellijsten, en kopie-netwerken (dezelfde tekst bij veel accounts).
3. **README lezen** van de rest (hooguit 2000), eerst de nieuwe.
4. **Ruis eruit op tekst:** geen of lege README, alleen code zonder uitleg, sjabloon of huiswerk, geen verdienplan.
5. **Plan eruit halen:** wat, voor wie, verdienmodel, prijs, platform, tractie (sterren, forks, betaalpagina, wachtlijst, eigen site).
6. **Score** van 0 tot 10 met vaste regels (zie `ontwerp.md`) en een rapport met de top 25 (hooguit 2 per maker) en de ruis per reden.

Het rapport is een voorselectie, geen oordeel. Het echte oordeel doet één keer per week een agent met de ideeëntest (`opdracht-beoordelaar.md`).

## Wanneer draait het
Eén keer per dag (klok: eerste start na 04:00 UTC), en meteen na een push die de radar zelf verandert. Met de hand starten: een opdrachtbestand met `{"workflow": "ideeen-radar.yml", "invoer": {}}` (skill `actions`). De run duurt ongeveer 5 minuten.

## Bestanden
| Bestand | Wat |
|---|---|
| `radar.py` | zoeken, README's ophalen, alles aan elkaar knopen, bestanden schrijven |
| `regels.py` | de vaste regels: zoektermen, wat ruis is, wat we uit een README halen, de score |
| `rapport.py` | maakt het rapport in gewone woorden |
| `opslaan.sh` | zet de uitkomst op de tak `ideeen-data` (nooit geforceerd) |
| `test_radar.py` | tests zonder internet: `cd platformen/ideeen/repo-radar && python3 -m unittest -v test_radar` |
| `ontwerp.md` | keuzes, regels en wat we vonden over GitHub Models |
| `opdracht-beoordelaar.md` | opdracht voor de wekelijkse beoordelaar |
| `.github/workflows/ideeen-radar.yml` | de workflow |

## Privacy
We bewaren alleen de openbare repo-naam en de link. Geen namen, mailadressen of andere gegevens van makers; die halen we ook uit de beschrijving voor die wordt opgeslagen.

## GitHub Models
Uitgezocht op 19 nov 2026: GitHub Models is sinds 30 juli 2026 helemaal gestopt (GEZIEN in de documentatie van GitHub, zie `ontwerp.md`). Daarom geen automatische voorbeoordeling met een taalmodel.
