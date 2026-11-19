# Ontwerp repo-radar (bouwer repo-radar, 19 nov 2026)

## 1. Wat en voor wie
Een bot die elke dag nieuwe GitHub-repo's zoekt waarin iemand een app-idee of een ander geldplan uitschrijft, de README leest en er een voorselectie van maakt. Voor de beoordelaar van Dortus (één keer per week) en de hoofdchat, die daaruit kansen kiest die wij ook kunnen bouwen en verkopen. Opdracht van Thijs, 19 nov 17:18: bewust nieuwe repo's met plannen, niet alleen bewezen omzet.

**Af is:** de workflow `ideeen-radar.yml` draait (met de hand en volgens de klok), zet `repo-radar/<datum>/rapport.md` met een top 25 en `kandidaten.json` op de tak `ideeen-data`, de tests slagen, en een keurder keurde het.

## 2. Wat er al was (verkend)
- `.github/workflows/radar.yml` en `scanner.yml`: klok-job plus werkjob, invoer via `env:`, data naar een eigen tak. Dit volgt hetzelfde patroon.
- `platformen/ai-handel/scanner/opslaan.sh`: clone van de datatak, kopiëren, commit, gewone push, 5 pogingen, nooit forceren. `opslaan.sh` hier is daar een kopie van met een andere tak en map.
- `organisatie/controle/klok.py`: interval `1d-na-04:00UTC` geeft hooguit één beurt per dag en haalt een gemiste dag in.
- `organisatie/controle/opdracht.py`: lijst TOEGESTAAN; `ideeen-radar.yml` staat erop omdat hij alleen openbare data leest, niets kost en alleen op de eigen tak schrijft.
- `platformen/ideeen/radar/` (platformradar van 18 nov) telt topics per kwartaal; dit is iets anders: losse repo's met een plan.

## 3. Open vragen, zelf beantwoord
- **Wat is "nieuw of flink bijgewerkt"?** Nieuw: aangemaakt in de laatste 2 dagen. Flink bijgewerkt kan de zoek-API niet meten; benadering: jonger dan 90 dagen, gisteren of vandaag gepusht en minstens 5 sterren. Dat is een GOK op wat "flink" is; de nieuwe repo's gaan bij gelijke score voor.
- **Hoeveel zoekvragen?** 23 zoektermen keer 2 soorten = 46 zoekvragen ("mrr" geschrapt: gaf vooral RAG-evaluaties, mean reciprocal rank), 2,2 s ertussen (onder de 30 per minuut). Elk geeft hooguit 100 repo's (de beste treffers).
- **README lezen zonder de API-limiet op te maken?** Via raw.githubusercontent.com (telt niet mee voor de 1000 per uur die alle workflows van deze repo delen). Alleen als dat niets geeft één keer de API, hooguit 200 keer per run.
- **Hoeveel README's?** Hooguit 2000 per run (eerste proefrun in de workflow: 2281 repo's gevonden, 1200 README's gelezen, hele run ±4 minuten). Volgorde: eerst nieuw, dan meer geldtermen, dan sterren. Wat niet gelezen is telt apart, niet als ruis.
- **Elke dag dezelfde populaire repo's bovenaan?** Nee: `gezien.json` op de datatak onthoudt wat al in een top stond; vanaf de volgende dag gaat dat niet meer in de top (wel in `kandidaten.json`). Een tweede run op dezelfde dag geeft dezelfde top.
- **Persoonsgegevens van makers?** We bewaren de openbare repo-naam en de link. Geen eigenaargegevens, geen README-tekst, geen link naar de site (alleen ja of nee). De beschrijving van de maker bewaren we alleen voor de top 25 van die dag (die moet de beoordelaar lezen), zonder mail, telefoon, links en @-namen. Gewone namen herkennen we niet; daarom niet bij de andere ±1000 repo's (keuring B4).
- **Wat als GitHub de zoekvraag weigert of de limiet raakt?** Bij 403 of 429 wachten tot de teller vol is (hooguit 70 s) en opnieuw, 4 pogingen. Mislukt meer dan de helft van de zoekvragen, dan faalt de run en wordt er niets opgeslagen.

## 4. Aanpakken
| | Aanpak | Voor | Tegen |
|---|---|---|---|
| A | Alleen de zoekresultaten (naam, beschrijving, topics, sterren), geen README | snel, minste verzoeken | prijs, verdienmodel en plan staan bijna altijd in de README; veel ruis blijft over |
| **B** | **Zoeken, README via raw lezen, vaste regels voor plan, ruis en score** | **gratis, uitlegbaar, testbaar; elke reden staat in het rapport** | **regels missen nuance (een prijs in een tabel met API-kosten, een woord in de verkeerde zin)** |
| C | B plus een taalmodel dat elk plan samenvat en beoordeelt | betere samenvatting in het Nederlands | GitHub Models is gestopt (zie hieronder); een ander model kost geld of tegoed van Thijs |

**Gekozen: B.** Het kost niets, draait in ±5 minuten, en het echte oordeel doet toch een agent van ons met de ideeëntest. De regels hoeven alleen de ruis weg te halen en de beste 25 bovenaan te zetten.

## 5. De regels (in `regels.py`)
- **Ruis op naam, beschrijving en topics** (vóór het lezen): fork, gearchiveerd, sjabloon of boilerplate, huiswerk of oefening (ook "clone"), crypto-pump, spam of illegaal (cracks, "patched build", mod-apk), awesome-lijsten. Plus **kopie-netwerken**: hetzelfde begin van de beschrijving bij 3 of meer eigenaren, hetzelfde eind bij 4 of meer, of 5 of meer eigenaren waarvan de naam met dezelfde 7 tekens begint én die ook op elkaar lijken (minstens de helft van de woorden in repo-naam en beschrijving gedeeld (gewone woorden als saas, app, free, with tellen niet) met een andere eigenaar uit de groep). In de eerste proef waren dat tientallen `apimart*`-accounts met dezelfde reclame. Alleen een gelijk begin van de naam is niet genoeg: dat gooide 5 eerlijke makers weg die Mohammed heten (keuring A4).
- **Ruis na het lezen:** geen README, lege README (minder dan 200 tekens), sjabloon, huiswerk of crypto in de tekst (losse woorden als "homework" alleen zonder echt verdienplan), kopie van andermans repo (de README verwijst naar dezelfde repo-naam bij een andere eigenaar), alleen code zonder uitleg (minder dan 40 woorden lopende tekst; tekst in tabellen telt mee), geen verdienplan (geen verdienmodel, geen prijs, geen betaallink en minder dan 2 geldwoorden).
- **Wat we eruit halen:** wat (de beschrijving van de maker), voor wie (vaste lijst groepen, in het Nederlands), verdienmodel (abonnement, paywall of in-app aankopen, eenmalige koop, gratis met pro-versie of pro-licentie, per gebruik, commissie, advertenties, affiliate, donaties), prijs (bedragen vanaf 0,99, met per maand of per jaar). Verdienmodel en prijs komen alleen uit de verkooptekst: de beschrijving, stukken onder een kopje met prijzen, Pro, kopen of licentie, en regels over de eigen verkoop (Pro, buy, licentie, betaallink). Kopjes over prijzen van anderen (vergelijking, alternatieven, "pricing models explained") en tariefregels als "2.9% + $0.30" tellen niet, dus ook bedragen in vergelijkingstabellen, API-kosten en omzet van anderen niet; ontkenningen als "no subscription" ook niet (keuring A3), platform (Blender, Obsidian, JetBrains, Garmin, Steam, Chrome, web, Gumroad; en andere zoals iOS of Shopify zonder punten), tractie (sterren, forks, betaalpagina, wachtlijst, eigen site). Een betaalpagina telt alleen als link naar een eigen kassa (buy.stripe.com, een eigen Gumroad- of Lemon Squeezy-pagina, Paddle-checkout, Polar), niet de site van Stripe zelf en niet Ko-fi of Buy Me a Coffee (dat zijn donaties). Platform en doelgroep alleen uit de kop en de eerste 3000 tekens van de README; verderop staan vaak lijsten met koppelingen.
- **Score (max 10):** verdienmodel +2 (zwak model +1), kopje prijzen +1, plan uitgeschreven (2+ kopjes zoals probleem, doelgroep, roadmap) +1, prijs +2, platform van ons +2 of web +1 (Gumroad is de kassa: 0 punten als platform, wel +1 als betaalpagina), sterren 10+ +1 of 50+ +2, betaalpagina of wachtlijst +1, eigen site +1. Bij gelijke score: eerst nieuw, dan sterren. Hooguit 1 repo per maker in de top.

## 6. Stap 2: GitHub Models (uitgezocht 19 nov 2026, 16:20 UTC)
GEZIEN met curl op docs.github.com (`/en/github-models/about-github-models`, `/en/billing/concepts/product-billing/github-models` en `/en/github-models/use-github-models/prototyping-with-ai-models` geven alle drie dezelfde pagina): *"GitHub Models has been retired. As of July 30, 2026, GitHub Models has been fully retired. The playground, model catalog, inference API, and bring your own key (BYOK) are no longer available to any customer."* GitHub verwijst naar Azure AI Foundry of Copilot; dat kost geld of een abonnement. Het oude adres `models.github.ai/inference/chat/completions` geeft alleen nog de tekst "OK" terug.

**Besluit: de voorbeoordeling met een taalmodel bouwen we niet.** Het echte oordeel doet één keer per week een agent van ons met `opdracht-beoordelaar.md`. De hoofdchat maakt die geplande taak aan.

## 7. Wat het niet doet
- Geen oordeel of iets goed is: alleen een voorselectie. Een hoge score betekent "duidelijk plan met prijs", niet "goed idee".
- Geen vertaling: de beschrijving staat er in de taal van de maker.
- Geen contact met makers, niets kopen, niets naar buiten.
- Repo's van een paar uur oud zonder README vallen eruit; die komen morgen niet terug als ze ouder dan 2 dagen zijn, tenzij ze actief zijn en 5 sterren hebben.
