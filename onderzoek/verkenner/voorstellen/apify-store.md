# Voorstel: Apify Store (Actors)

## Herhaling 16 nov 2026 (run 21:31), nu met eigen meting

**Advies: nee voor nu. Cijfer: 4 van 10 (blijft).** Het geld is echt en groeit (Apify betaalt makers nu $2M per maand), en bouwen past heel goed bij ons. Maar de winkel loopt vol met ±27.000 nieuwe Actors per maand, en een gewone nieuwe Actor heeft na 3 tot 6 maanden 2 gebruikers. Een grote speler worden lukt hier alleen met massa, en dat doen honderden makers met AI al. Nagekeken door de controleur, met een eigen tweede steekproef: akkoord, zijn cijfers liggen iets lager.

Op 6 nov gaven winkel en API een 403. Nu antwoordt de open winkel-API (`api.apify.com/v2/store`, `api.apify.com/v2/acts/<maker>~<naam>`) en robots.txt van apify.com staat alles toe (ai-input=yes).

**Hoe gemeten (GEZIEN, 16 nov):**
- Sitemap apify.com (actors1 t/m 20): 123.175 Actors van 10.487 makers. Winkel-API meldt ±121.700.
- Willekeurige steekproef van 3.000 Actors uit de sitemap (zaad 16), per Actor de detail-API met aanmaakdatum en gebruikers (totaal, 30 dagen). 2.995 goed opgehaald.
- Willekeurige steekproef van 400 makers, al hun Actors via `store?username=`, plus de aanmaakdatum van hun oudste Actor. Let op: bij ±40% van de makers geeft dat filter niets terug (de controleur zag 15 van 40, hun Actors los opgevraagd haalden hooguit 7 maandgebruikers samen). De makercijfers hieronder zijn dus te gunstig.
- De nieuwste 13.362 Actors in de winkellijst (dieper bladeren kan niet): aangemaakt van 3 tot 16 nov.
- Scripts en ruwe steekproef: `data/apify-detail-script.sh`, `data/apify-actors-analyse-script.py`, `data/apify-maker-script.sh`, `data/apify-makers-analyse-script.py`, `data/apify-steekproef-3000-2026-11-16.jsonl`.

**Bereik (GEZIEN)**
- Lichting mei t/m aug 2026 (n=948): mediaan 2 gebruikers ooit, mediaan 1 in de laatste 30 dagen (vaak de maker zelf of de test van Apify, GOK). 3,4% haalde ooit 100+ gebruikers, 0,6% heeft 100+ in de laatste 30 dagen. Controleur, eigen steekproef van 600 (203 uit die maanden): mediaan 2, 2,5% en 0%.
- Ouder helpt weinig: lichting jan t/m apr 2026 mediaan 7 tot 12 ooit, ±11% 100+; lichting 2025 per maand ±10 tot 60% 100+ ooit, maar per 30 dagen bijna nergens 100+.
- Per soort (lichting mrt t/m aug): sociale media (n=155, 14% 100+) en video (n=47, 13%) doen het het best; ontwikkeltools, AI, MCP-servers en zakelijk 0 tot 7%. De beste soorten zijn juist het scrapen van grote platformen, met het grootste juridische risico.
- Geconcentreerd: in de steekproef heeft de top 1% van de Actors 86% van alle maandgebruikers, de top 10% 94%.

**Drukte (GEZIEN)**
- 13.362 nieuwe openbare Actors in ±13,5 dagen: ±27.000 tot 30.000 per maand. In de steekproef: 147 uit mei, 305 uit aug, 725 uit okt. Op 6 nov meldde apifystats 26.772 in okt (DERDEN); dat klopt.
- Massamakers: in de nieuwste 13.362 hebben 1.518 makers iets gezet, de grootste 141 tot 144 Actors in twee weken (memo23, rbbscrap). 69% van de steekproef uit mei t/m aug is van makers met 50+ Actors.
- 93% van de makers in de makersteekproef begon in 2026. De winkel is dus vooral nieuwkomers.

**Geld**
- DERDEN, Apify zelf (apify.com/partners/actor-developers, gelezen 16 nov): "$2M paid out monthly", "7,500 community developers", "Many developers earn over $3k". Op 6 nov was het $1,7M, in aug $1,4M.
- DERDEN, eigen opgave kleine maker: [Boon](https://dev.to/boo_n/3-months-shipping-my-first-apify-actor-64-users-200mo-and-everything-i-got-wrong-52i7), Vinted-scraper, begonnen feb 2026: stand mei 2026 64 gebruikers ooit, 13 actief per maand, ±$200 per maand netto na 20% afdracht. Het beste nieuwe bewijs, maar onder $300, en Vinted verbiedt tools van derden (zie kansen/chrome-vinted-en-ondertitels.md).
- DERDEN, oud: [Guillaume Lancrenon](https://blog.apify.com/turning-code-into-cash-with-apify/) $2.000+ per maand (okt 2024, geen nieuwe maker).
- GEZIEN, makers die in mei t/m aug 2026 begonnen (n=60, te gunstig, zie boven): mediaan 4 maandgebruikers over al hun Actors samen, 5% haalt 200+, niemand 1.000+. Makers met 21+ Actors halen mediaan ±120 tot 185 maandgebruikers samen; makers met 1 Actor mediaan 1. Snelste nieuwkomer in de steekproef: blueskyscraper, 70 Actors sinds sep 2026, 2.631 maandgebruikers.
- GOK, opbrengst per maandgebruiker: gemiddeld ±$1 ($2M gedeeld door ±1,8M maandgebruikers per Actor in de hele winkel, schatting uit de steekproef), maar bij Boon ±$15. Een massamaker met ±150 maandgebruikers zit dan ergens tussen $150 en $2.000 per maand. Te onzeker om op te bouwen.
- Voorwaarde van 6 nov (3 makers met minder dan 12 maanden en een eigen cijfer boven $300 per maand): niet gehaald, we vonden er 0 (Boon $200).

**Vindbaarheid**
- Zoeken in de winkel en op Google, en sinds 2026 AI-agents via MCP; Actors krijgen een vlag `isWhiteListedForAgenticPayments` (agents betalen zelf per gebruik). Dat is een nieuw kanaal, maar MCP-servers als soort doen het niet beter dan de rest (7% 100+).

**Past het bij ons**
- Bouwen: zeer goed. Code, Linux, test in de cloud van Apify, betalen en uitbetalen geregeld. Een Actor in 1 tot 3 dagen.
- Grote speler worden: alleen met tientallen Actors en onderhoud (scrapers breken). Honderden makers doen dat al met AI; geen voorsprong voor ons.
- Thijs moet een Apify-account met uitbetaling hebben (staat niet klaar). Juridisch risico bij scrapen blijft.

**Waarom niet hoger:** bereik voor een nieuwe Actor is het zwakste dat we zagen naast Zendesk en Freshworks (mediaan 2, 0 tot 0,6% 100+ per maand), de vloed is verdubbeld sinds juli, en het geldbewijs van nieuwe kleine makers blijft onder $300. **Waarom niet lager:** het geld op het platform is groot en groeit, en er zijn nieuwkomers die met massa snel honderden maandgebruikers halen.

**Wanneer opnieuw (rond 16 feb 2027):** `data/apify-detail-script.sh` op een nieuwe steekproef van 3.000 uit de sitemap, dan `data/apify-actors-analyse-script.py`. Opnieuw wegen als de lichting nov 2026 t/m jan 2027 op 5%+ met 100+ maandgebruikers komt, als de vloed onder 10.000 per maand zakt, of als we 3 makers met minder dan 12 maanden en een eigen cijfer boven $300 per maand vinden.

---

## Eerste meting 6 nov 2026

**Advies: nee. Cijfer: 4 van 10.** Op platformniveau wordt hier echt geld uitbetaald, meer dan op enig platform dat we tot nu toe zagen. Maar bij nieuwe kleine makers is dat niet bewezen (hoogste cijfer dat we vonden: $47 netto), het bereik van een gewone nieuwe Actor is erg laag, en de stroom nieuwe Actors verdubbelde in oktober. Geen manager. Heropenen alleen onder de voorwaarde onderaan. Geschreven op 6 nov 2026.

Een Actor is een klein programma in de cloud van Apify, meestal een scraper of een hulpmiddel voor AI-agents. De koper betaalt per resultaat, Apify betaalt de maker uit.

## Meetgrens
- De winkel en de API (`apify.com`, `api.apify.com`) zijn vanuit deze run niet met `curl` te lezen: de proxy geeft 403, ondanks Network access Full. De API vroeg via WebFetch om toestemming en daar antwoordt niemand op, dus dat is gestopt.
- Losse Actor-pagina's en [apifystats](https://apifystats.com/stats.html) (een onafhankelijke dagelijkse telling, niet van Apify) waren wel te lezen via WebFetch.
- Cijfers van apifystats zijn dus DERDEN. Eigen tellingen op die tabellen staan als GEZIEN, met de beperking erbij.

## Cijfers

**Bereik**
- GEZIEN (eigen telling op [Email & outreach](https://apifystats.com/tasks/email-outreach.html), stand 5 okt, top 150 van 299 zichtbaar, gerangschikt op maandgebruikers): de middelste Actor (plek 150) heeft 1 gebruiker per maand. 7 van de 299 (2,3%) hebben 100+ maandgebruikers. Alle leeftijden door elkaar.
- GEZIEN (eigen telling op [AI & agent tools](https://apifystats.com/tasks/ai-agent-tools.html), stand 14 okt, top 150 van 671 zichtbaar): plek 150 heeft al maar 1 maandgebruiker, dus de mediaan is hooguit 1. 4 van de 671 (0,6%) hebben 100+, waarvan de bovenste twee oude Actors zijn.
- GEZIEN (Email & outreach, Actors van 3 tot 6 maanden oud): in de zichtbare top 150 staan er ±50, daarvan hebben er 7 ooit 100+ gebruikers gehaald (±14%, de bovengrens). Hebben de onzichtbare 149 dezelfde leeftijden, dan is het ±7% (GOK). Maar 1 van die 50 haalt 100+ per maand. Dit cohort is van vóór de grote golf (±apr tot jul). Eén categorie is geen heel platform. Ter vergelijking: Chrome 10 tot 13% en Figma 22% in `onderzocht.md`, met een andere telling.
- GEZIEN, kleine steekproef: 13 Actor-pagina's uit onze eigen zoekresultaten, onder meer [zerobreak](https://apify.com/zerobreak/trustmrr-startup-scraper) en [crawlerbros](https://apify.com/crawlerbros/monday-marketplace-scraper.md) (niet willekeurig, leeftijd meestal onbekend). Totaal aantal gebruikers: 1, 2, 2, 2, 2, 2, 2, 3, 4, 11, 39, 57, 88. Mediaan 2, geen enkele 100+.
- DERDEN: uitschieters bestaan. [Snelste starters](https://apifystats.com/lists/fastest-starts.html): 15 Actors onder de 3 maanden met 570 tot 3.040 maandgebruikers. De meeste halen data uit Aziatische winkels en sociale media (Naver, Taobao, JD, Xiaohongshu, 1688).
- Let op: "gebruiker" is iedereen die het één keer probeerde. Dat is geen betalende klant. [Godberry Studios](https://godberrystudios.com/posts/apify-pay-per-event-migration-playbook-2026/) zag 5.407 resultaten van gratis gebruikers en $0 inkomsten (DERDEN, eigen opgave).

**Geld**
- Betaling is ingebouwd. 97,1% van de Actors is betaald per gebeurtenis (DERDEN, [apifystats](https://apifystats.com/stats.html), 5 nov). Huren per maand is sinds okt 2026 weg ([Apify](https://blog.apify.com/migrating-to-pay-per-event-pricing/)).
- Afdracht: 20%, plus de kosten van het draaien bij betaald per resultaat. ([Apify help](https://help.apify.com/en/articles/8684010-how-does-actor-monetization-work)).
- DERDEN, Apify zelf, niet te controleren: ["$1.7M paid out last month. Many developers earn over $3k"](https://apify.com/partners/actor-developers). Een andere banner, op een pagina uit aug 2026, noemt $1,4M. Help-artikel okt 2025: de beste onafhankelijke makers boven $10.000 per maand, "veel anderen" boven $1.000.
- DERDEN, tweedehands: ±3.000 betaalde makers, dus gemiddeld ±$470 per maand. [AgentByline](https://agentbyline.com/articles/apify-actor-passive-income-what-really-earns-in-2026-67lcfr), door een AI geschreven en verkoopt een cursus. Niet bij Apify teruggevonden. Apify noemt zelf alleen "5.600 community developers", niet per se betaald: dan is $1,7M gemiddeld ±$300 (GOK). Een gemiddelde zegt niets over de mediaan.
- DERDEN, eigen opgave kleine maker, het beste cijfer dat we hebben: [sessionzero_ai](https://dev.to/sessionzero_ai/i-built-13-korean-data-scrapers-heres-what-i-actually-made-in-month-1-8ep), 13 Actors, de 18 dagen na het starten met betalen (13 tot en met 31 maart 2026, dus geen volle maand): 91 gebruikers, $64,80 bruto, $47 netto. Prijs laag ($0,50 per 1.000). Hij noemt 30% afdracht, dat klopt niet met $47; de rest gaat waarschijnlijk naar draaikosten (GOK).
- [Olivier Reynaud](https://blog.apify.com/building-98-actors-on-apify-store/), onafhankelijk, op de blog van Apify: 98 Actors in 6 maanden, 855 maandgebruikers, 15 tot 20 uur per week. Omzet noemt hij bewust niet, alleen "meaningful but inconsistent".
- **Geen enkele nieuwe kleine maker gevonden met een eigen maandcijfer boven de $100.** Een [Indie Hackers-post](https://www.indiehackers.com/post/i-charge-5-per-1-000-results-my-niche-apify-actor-tripled-its-revenue-in-month-two-c9e85e2046) met "tripled its revenue" was niet te lezen.
- GOK: uit sessionzero_ai volgt ±$0,50 netto per gebruiker per maand. Voor € 350 per maand zijn dan ±800 maandgebruikers nodig, of ±130 tot 160 bij de prijs die de controleur als midden zag ($2,50 tot $2,99 per 1.000). Zeer onzeker, berust op één maker.

**Drukte (de zwakke plek)**
- DERDEN, [apifystats](https://apifystats.com/stats.html), 5 nov: 88.434 Actors van 4.778 makers. Nieuw per maand: 1.887 in jan 2026, 12.583 in jul, 13.708 in sep, 26.772 in okt. 92,7% is jonger dan een jaar. Apify zelf noemt [111.912](https://apify.com/partners/actor-developers). De cijfers passen niet netjes: de maandcijfers tellen op tot ±94.000 sinds nov 2025 en de 92,7% rust op 101.658 Actors, dus die horen niet bij de 88.434. Het beeld van de groei blijft staan, de exacte stand niet.
- Veel van deze groei lijkt door AI gebouwd (GOK). Zelfde mogelijkheid als wij hebben, dus geen voorsprong.
- DERDEN: top 100 Actors heeft 63% van alle gebruikers, top 1.000 heeft 85%.
- DERDEN: veel Actors helpen niet vanzelf. [automation-lab](https://apifystats.com/leaderboard.html) 831 Actors en ±16.000 maandgebruikers (gemiddeld 19), [maker op plek 460](https://apifystats.com/publishers/) 101 Actors en 145 maandgebruikers.

**Vindbaarheid**
- Zoeken in de winkel, Google, en AI-agents via MCP (GOK, niet gemeten). Slechts 9,2% van de Actors heeft een beoordeling (DERDEN), dus een paar reviews vallen op.
- Hoe de winkel rangschikt is niet onderzocht.

**Past het bij ons**
- Bouwen: een Actor in 1 tot 3 dagen, geen 2 weken (GOK). Dit past heel goed bij een ploeg Claudes.
- Onderhoud: scrapers breken als een site verandert. De documentatie van Apify noemt ±2 uur per week; onduidelijk of dat per Actor is. Scrapers van grote sites worden geblokkeerd.
- Risico voor Thijs: scrapen kan tegen de voorwaarden van die sites ingaan en persoonsgegevens raken. Dat moet Thijs beoordelen voordat we hier iets bouwen. Hulpmiddelen zonder scrapen (bijvoorbeeld documenten omzetten) hebben dat minder.
- Thijs moet een Apify-account met uitbetaling regelen. Geen eigen kassa voor ons. Uitbetalen is maandelijks.

## Voor
- Sterkste geldbewijs tot nu toe. Geld loopt via het platform, kopers betalen al.
- Bouwen gaat snel, dus meerdere pogingen per maand zijn mogelijk.
- Meetbaar: gebruikers, en omzet in eigen Console.

## Tegen
- De gewone nieuwe Actor heeft 1 tot 2 gebruikers.
- De stroom verdubbelde in oktober. Dit kan nog verergeren, ook voor de kopers die moeten kiezen.
- "Grote speler" lijkt hier lastig: de top zit vast bij Apify zelf en bij een paar grote makers. Een plek in een klein hoekje is haalbaarder (GOK).
- Geen schoon voorbeeld van een nieuwe maker die het tussendoel haalt.
- Juridisch en onderhoudsrisico bij scrapers.

## Eerste idee
Mocht het heropend worden: een hoekje met betaalde vraag en weinig goede aanbieders, zoals data van een regio of winkel die in het Engels slecht bediend wordt, of een hulpmiddel voor AI-agents zonder scrapen. Let op: 6 van de 15 snelste starters halen juist data van grote westerse sites, dus de lijst bewijst dit idee niet.

## Wanneer opnieuw kijken
Alleen als we minstens 3 makers vinden met minder dan 12 maanden ervaring en een eigen cijfer boven $300 per maand. Zinnige aanvulling dan: een willekeurige steekproef van 100 Actors van 3 tot 6 maanden oud via de Store-API (kan zodra `api.apify.com` open is), en Thijs laten kiezen welke soort Actors juridisch mag.

## Nakijken
Eerste versie (nog niet klaar, cijfer 5) door de controleur afgekeurd op 6 nov: de eigen grens lag boven de eigen bovengrens en was niet te meten, dus ontwijkend. Herschreven naar nee, cijfer 4, met zijn correcties. Tabellen zijn door een hulpmiddel gelezen; Reynaud, Godberry en AgentByline zijn niet door hem nagelopen.
