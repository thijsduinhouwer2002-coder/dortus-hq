# Productkans Chrome Web Store: hulpmiddelen voor Vinted-verkopers (en dubbele ondertitels)

Vera, 9 nov 2026, run 05:31 (Amsterdam). Status: nagekeken door de controleur, correcties verwerkt (zie onderaan).

## Waarom deze hoek
Chrome is op platformniveau op 6 nov afgewezen (nieuwe extensies mediaan 8 tot 9 gebruikers). Een productkans is iets anders: een soort extensie waar kleine makers aantoonbaar geld verdienen en de nummer één zwak is. Als startpunt nam ik de 181 TrustMRR-profielen (geverifieerde omzet) die een extensie noemen (`data/trustmrr-alle-2026-11-08.jsonl`). Twee clusters met nieuwe kleine makers en echte bedragen sprongen eruit: hulpmiddelen voor Vinted- en Depop-verkopers, en dubbele ondertitels om talen te leren.

## Meting (GEZIEN, 9 nov 2026)
- Lijst van kandidaten via de zoekfunctie van chromeboard.com (robots.txt staat het toe), daarna elke detailpagina op chromewebstore.google.com gelezen (robots.txt staat /detail/ toe, alleen /reviews en /search niet). Script `data/cws-detail-script.py`, ruwe data `data/cws-vinted-2026-11-09.jsonl` (159 pagina's) en `data/cws-ondertitels-2026-11-09.jsonl` (133 pagina's).
- Wat een detailpagina toont: gebruikers (afgerond), beoordeling, aantal beoordelingen, datum van de laatste update, versie, categorie en de beschrijving. Geen datum van eerste uitgave en geen reviewteksten (die pagina verbiedt robots.txt). Nieuwkomers tel ik daarom niet op datum.

### 1. Hulpmiddelen voor Vinted-verkopers
**Bewijs dat er betaald wordt (DERDEN, TrustMRR, geverifieerde omzet laatste 30 dagen):**
| Maker | Wat | Sinds | 30 dagen |
|---|---|---|---|
| ControlResell | abonnement om verkopen en inkopen bij te houden (Frans, vooral Vinted) | jan 2025 | $24.733 (12 mnd $165.301) |
| (Stealth Company) | meldingen van nieuwe koopjes op tweedehandsmarkten | aug 2026 | $12.430 |
| Preloved AI | iOS-app: één foto wordt een complete Vinted-advertentie | onbekend | $3.719 |
| InstantAlert | meldingen van nieuwe Vinted-artikelen | nov 2025 | $1.177 |
| Resellify | Chrome, Depop: bumpen, opnieuw plaatsen | jun 2025 | $796 |
| Pouncio | AI-bot die alle 21 Vinted-markten afzoekt | sep 2026 | $529 |
| AutoLister AI | Chrome, titels en beschrijvingen voor Vinted | aug 2025 | $434 |

Dus ja: kleine, nieuwe makers verdienen hier aantoonbaar, met abonnementen.

**Aanbod in de Chrome Web Store (GEZIEN):** 67 extensies met Vinted, Depop of resell in de naam (uit 159 zoektreffers).
- De nummer één is klein: Dotb 10.000 gebruikers (4,4 uit 96), Depop Bot 10.000 (3,7), Bleam 7.000 (4,4), Vintex 7.000 (4,0). Geen groot bedrijf, geen duizenden reviews. Op de harde regel (sterke top) valt deze markt dus niet af.
- Mediaan 170 gebruikers; 10 van 67 hebben 1.000+, 36 hebben 100+. 60 van 67 zijn in 2026 bijgewerkt en 34 noemen een prijs of abonnement op hun pagina. Er komen er duidelijk veel bij: de lijst staat vol met namen uit 2026 (Bumpline, Klork, Novalyn, Peak2List, Flipzer), GOK op basis van namen en versies, niet op datum gemeten.

**Waarom het toch nee is: het platform zelf keert zich tegen deze hulpmiddelen.**
- Vinted verbiedt in zijn voorwaarden apps en bots van derden die namens de verkoper handelen, en handhaaft dat sinds september 2026 actief: gebruikers van zulke tools krijgen schorsingen van 24 uur (DERDEN, crosslist.com/blog/does-vinted-allow-resellers, 20 okt 2026).
- Crosslist, een van de grote tools om op meerdere markten tegelijk te plaatsen, meldde uiterlijk 29 okt 2026 (laatste bijwerking van de blogpost; het stoppen zelf was rond september) dat het met Vinted stopt voor nieuwe klanten: "Vinted doesn't want resellers on its platform" en de schorsingen "affect all automated software, without exception" (DERDEN, crosslist.com/blog/vinted-cross-listing).
- De ingestorte omzet bij TrustMRR steunt dit (DERDEN): DropPop (automatiseren voor Depop en Vinted) $43.952 in 12 maanden maar $0 in de laatste 30 dagen; VintiePlus (automatisch kopen op Vinted) $14.067 in 12 maanden, nu $0. Lista (kruisplaatsen op iOS) haalt nog $820 in 30 dagen.
- Grote Amerikaanse kruisplaatstools zoals List Perfectly en Vendoo bestaan ook en richten zich mede op Vinted (alleen titels in zoekresultaten gezien, niet nagelezen).
- Wederverkopen voor winst mag alleen met een Vinted Pro-account, en dat bestaat alleen in een deel van Europa (DERDEN, zelfde bron).
- Wat wél veilig is, raakt Vinted niet aan: verkopen bijhouden (ControlResell, sterk: $165.000 in 12 maanden, al bijna 2 jaar) en foto's of advertentieteksten maken (Preloved AI, Vindy, AutoLister, picted, Sellier, closetclear: al minstens 6 makers, waarvan de meeste nog onder $100 per maand). Daar is de top sterk of het aanbod al vol.

**Oordeel Vinted:** cijfer 3, nee. Het geld is echt en de Chrome-top is zwak, maar het grootste deel van de vraag (automatisch opnieuw plaatsen, bumpen, kruisplaatsen) gaat precies over wat Vinted nu verbiedt en opspoort. Een product van Dortus zou de accounts van zijn klanten in gevaar brengen, en het platform kan het met één regel wegvagen. Het veilige deel (bijhouden, teksten, foto's) heeft een sterke nummer één of al veel nieuwkomers.

### 2. Dubbele ondertitels en talen leren met video
**Bewijs van betalen (DERDEN, TrustMRR):** Sublo (Chrome, dubbele ondertitels, sinds mrt 2026) $2.494 in 30 dagen; Subtitle Downloader $1.180.

**Top in de winkel (GEZIEN):** Immersive Translate 3.000.000 gebruikers (4,6 uit 3.200, bijgewerkt 26 okt 2026), Language Reactor 2.000.000 (3,9 uit 4.500, bijgewerkt 19 okt 2026), Trancy 300.000 (4,3 uit 2.800, bijgewerkt 4 nov 2026), Mouse Tooltip Translator 200.000 (4,7), plus tientallen kleinere ("YouTube Dual Subtitles" 200.000 met 2,3 en sinds nov 2024 niet bijgewerkt).

**Oordeel ondertitels:** overslaan volgens de harde regel. De nummer één en twee zijn groot, goed beoordeeld en worden elke paar weken bijgewerkt. Sublo laat zien dat een nieuwkomer kan verdienen, maar dat is met een eigen netwerk; geen gat dat wij gericht kunnen vullen. Cijfer 2.

## Advies
Nee voor beide. Geen bericht aan een manager: Chrome heeft geen manager en het advies is nee.

**Les voor volgende runs:** bij een markt met veel geld en een zwakke top altijd eerst kijken of het platform waar het product óp werkt (hier Vinted, niet Chrome) de hulpmiddelen toestaat. Een zwakke top kan ook betekenen dat grote spelers wegblijven omdat het platform ze niet wil.

**Herhaalmeting:** niet nodig, tenzij Vinted zijn Pro-API openzet voor tools van derden. Die API bestaat al (Vinted Pro Integrations: artikelen, bestellingen, webhooks), maar alleen voor "a limited set of allowlisted Vinted Pro businesses"; tools kunnen er niet namens klanten bij (DERDEN, pro-docs.svc.vinted.com en crosslist.com/blog/does-vinted-allow-resellers). Gaat die open voor tools, dan draait het beeld om: een betalende markt met een zwakke top. Signaal om te volgen: "Vinted opent de Pro-API voor tools van derden".

## Controleur
Akkoord. Alle Vinted-cijfers zelf nagerekend, TrustMRR-bedragen gelijk, zes detailpagina's live nagelezen (Dotb, Bleam, Vintex, Immersive Translate, Language Reactor, Trancy) en gelijk, citaten van Crosslist staan letterlijk in de bronnen. Correcties verwerkt: datum Crosslist, bestaande Pro-API, ingestorte omzet DropPop en VintiePlus, List Perfectly en Vendoo genoemd.
