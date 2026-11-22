# Voorstel: Twenty (open-source CRM, App Marketplace)

Noor, pionier, 8 nov 2026. Cijfer **5**, advies **nog niet klaar** (herhaalmeting 8 dec 2026).

## In het kort
Twenty is een open-source CRM (alternatief voor Salesforce en HubSpot), te gebruiken in de cloud of op een eigen server. Sinds Twenty 2.0 (21 april 2026) kun je er apps voor bouwen in TypeScript met de `twenty-sdk`, en sinds de zomer is er een Marketplace in de app (Settings > Applications > Marketplace). De winkel is piepjong: 55 apps op npm, waarvan nog geen enkele van een buitenstaander op de officiële lijst staat. Er komt een betaalsysteem in de app zelf (credits, met een vaste maandprijs of een prijs per gebruiker), maar dat is nog niet live en er staat nergens hoe een maker zijn geld krijgt. Dat laatste is het beslissende punt. Klanten zijn bedrijven met een terugkerend probleem, dat past goed bij de koers van 8 nov.

## De vijf vragen

### 1. Groeit het platform hard en zichtbaar? Ja, redelijk sterk.
- GitHub-sterren: 60.6K nu (GEZIEN, kop van https://twenty.com/apps; repos.ecosyste.ms geeft 60.555 op 6 nov 2026, DERDEN). Een artikel van eind februari of maart 2026 noemde nog 41K (DERDEN, https://dev.to/_46ea277e677b888e0cd13/twenty-crm-the-open-source-salesforce-alternative-with-41k-github-stars-9po). Dat is ±+48% in ongeveer 8 maanden.
- npm `twenty-sdk` (het gereedschap voor app-makers) per maand: 454 (okt 2025), 10.115 (apr 2026, lancering 2.0), 47.904 (jul), 134.500 (okt 2026) (GEZIEN, api.npmjs.org). Elke maand hoger. Let op: CI en AI-agents blazen dit op, en de SDK is nieuw, dus dit meet vooral interesse van bouwers, geen gebruikers.
- Docker-image `twentycrm/twenty`: 3,32 mln pulls in totaal (GEZIEN, hub.docker.com, 8 nov). Geen reeks, dus groei hieruit pas bij de herhaalmeting.
- Tempo: zeven releases in oktober 2026 (2.44 tot 2.52) (DERDEN, twenty.com/releases via hulpagent).
- Motor: Twenty 2.0 werd #2 van de dag op Product Hunt (DERDEN, https://chatgate.ai/post/twenty-2-0). Elke cloud-workspace heeft een MCP-server, dus het CRM lift mee met de AI-agents.
- Zwak punt: weinig geld achter het bedrijf. $5M seed (nov 2024, Runa Capital), in totaal ±$6M, ±21 mensen (DERDEN, https://tech.eu/2024/11/19/twenty-secures-5m-to-challenge-crm-giants-with-open-source/ en https://www.caplight.com/company/twenty). Geen omzet of klantenaantal gevonden.

### 2. Is de app-winkel jong? Ja, zeer jong.
- Apps verschijnen op de Marketplace via npm met keyword `twenty-app`; de server haalt de catalogus elk uur op, en pas na een keuring komt een app in de lijst (GEZIEN, https://docs.twenty.com/developers/extend/apps/operations/publishing.md en .../marketplace-review.md).
- Eigen telling (script `data/twenty-apps-meet.py`, momentopname `data/twenty-apps-2026-11-08.json`): **55 pakketten, 24 publicerende accounts**. Nieuw per maand: mrt 1, apr 3, mei 2, jun 5, jul 10, aug 4, sep 10, okt 13, nov (tot de 8e) 7 (GEZIEN).
- De officiële lijst op https://twenty.com/apps toont **8 apps, allemaal van Twenty zelf** (Call Recorder, People Data Labs, Last Contact, Exa, Slack, Microsoft Teams, Fathom, Granola) (GEZIEN door hulpagent). In de app staan ook gekeurde apps van anderen, maar hoeveel kon ik zonder account niet zien.
- Wie bouwt: vooral SaaS-bedrijven die een koppeling naar hun eigen dienst maken (Retell, CallPal, Skysay, Assinafy, Autosignly, Generect, mailfino) en een paar losse makers (QuoteFlowin, Lead Scoring Agent, Timestopper, The Bell). Downloads per maand: Twenty's eigen Last Contact 7.392, beste van een buitenstaander WhatsApp 1.964, de meeste 100 tot 1.000 (GEZIEN, npm, sterk opgeblazen door CI en installaties per server).

### 3. Kan er betaald worden? Gepland, maar nog niet voor makers.
- Apps kunnen in hun configuratie een `billing`-blok zetten: een vaste maandprijs, een prijs per gebruiker (tot $100 per maand), of betalen per gebruik in credits. Het platform int dat zelf van de workspace (GEZIEN, https://docs.twenty.com/developers/extend/apps/logic/credits.md).
- Maar die pagina zegt letterlijk: "Not live yet. Credit charging for apps launches officially in October." Op 8 nov staat die waarschuwing er nog (GEZIEN).
- Nergens staat dat de maker een deel van die credits krijgt: geen percentage, geen uitbetaling, geen Stripe Connect, ook niet in de code (hulpagent zocht op payout, revenueShare, developerShare: alleen het affiliateprogramma van 20% voor het doorverwijzen van klanten) (GEZIEN door hulpagent via Sourcegraph). Het kan dus ook zijn dat credits alleen bedoeld zijn om kosten van de app (AI, transcriptie) door te rekenen.
- De keuring vraagt wel: "Clearly state whether the app is free or paid, plan prices, billing frequency" (GEZIEN, marketplace-review.md). Betaalde apps zijn dus voorzien. Een eigen licentie met een sleutel in de app-instellingen (zoals bij Filament) lijkt nu de enige route (GOK, niet bevestigd).
- Credits werken alleen "on servers with billing enabled", dus vooral Twenty Cloud; zelfhosters betalen zo niet (GEZIEN, monitoring.md).

### 4. Is er vraag te zien? Niet goed gemeten.
- De meest besproken verzoeken over integraties (Office 365-mail 39 reacties, Gmail-antwoordknop 21, LinkedIn-extensie 20) zijn gesloten (DERDEN, issues.ecosyste.ms). GitHub-issues, Reddit en Discord konden we deze run niet rechtstreeks lezen (403 via de proxy).
- Wat de makers zelf bouwen, zegt iets: meerdere apps voor dezelfde dingen (twee keer Meta Lead Ads, twee keer Apollo-verrijking, drie keer e-handtekening). Dat zijn de koppelingen die bedrijven missen als ze van HubSpot overstappen (GOK).
- Een HubSpot-import (Shuttio, 23 okt) en offertes (QuoteFlowin, 2 nov) kwamen er net bij: tekenen dat makers de gaten van een overstapper invullen.

### 5. Is de eerste plek te pakken? Ja, bijna overal, maar welke hoek is onzeker.
- Er is geen enkele app van een buitenstaander met echt bereik. In bijna elke hoek is de plek leeg.
- Niet doen: dubbelen samenvoegen (zit al in Twenty zelf: `record-merge` en `findDuplicates` in de code, GEZIEN via GitHub-zoeken), call-recording en verrijking (Twenty doet het zelf of SaaS-bedrijven met eigen dienst).
- Kansrijke hoek: **verkoopdoelen en prognose** (doelen per verkoper, gewogen pijplijn, weekoverzicht wat er verschoof). In HubSpot en Salesforce zit dat achter dure plannen of in betaalde extra's; in de 55 Twenty-apps bestaat het niet (GEZIEN). Tweede keus: **e-mailsjablonen en opvolgreeksen** voor verkopers.

## Risico
- **Het platform haalt het niet:** klein team, weinig geld, tegen HubSpot en Salesforce. Teken: sterren en SDK-downloads stoppen met groeien, releases vallen stil, of het bedrijf draait de cloud terug.
- **Makers krijgen nooit geld via de winkel:** als credits alleen kosten doorrekenen, moeten we zelf licenties verkopen en stuurt de winkel niemand naar een kassa. Teken: na december nog steeds geen uitbetaling in de docs.
- **Twenty bouwt het zelf:** Twenty maakt zelf al 8 apps en de populairste. Teken: een officiële prognose-app of doelen in de kern.
- **Bereik klein:** CRM-gebruikers installeren weinig apps; de downloads op npm zeggen weinig over echte installs.

## Eerste productidee (alleen als het een ja wordt)
"Doelen en Prognose voor Twenty": gratis basis met een doel per verkoper en een gewogen pijplijn op de Opportunities; Pro ($9 tot $19 per maand per workspace, of per gebruiker via de credits zodra die live zijn) met maand- en kwartaaldoelen, een wekelijkse momentopname (wat schoof, wat viel af) en een mail op maandag. Ziet er uit als Twenty zelf (twenty-ui), met Daan vanaf het begin.

## Cijfer en advies
**5, nog niet klaar.** Vraag 1 en 2 zijn sterk (snelle groei, winkel van een half jaar met 55 apps), vraag 5 is open. Maar vraag 3 is het zwakke punt: betalen in de winkel is aangekondigd maar niet live, en een deel voor de maker staat nergens. Met de koers van 8 nov ("wie betaalt, hoeveel, bewijs") is dat te dun.

**Wat het een 7 maakt:** Twenty zet credits live met een uitbetaling aan makers (een percentage in de docs), of er staat een betaalde app van een buitenstaander in de Marketplace. Dan meteen opnieuw aanbieden; de vroege plek is dan nog ruim te pakken.
**Wat het een nee maakt:** sterren en SDK-downloads groeien twee maanden niet, of credits blijken alleen kostendoorrekening zonder deel voor de maker.

## Herhaalmeting 8 dec 2026
- `python3 -I data/twenty-apps-meet.py data/twenty-apps-2026-12-08.json` (±2 minuten), vergelijk met `twenty-apps-2026-11-08.json`: nieuw per maand, makers, downloads.
- Lees opnieuw `https://docs.twenty.com/developers/extend/apps/logic/credits.md` (staat "Not live yet" er nog? Staat er iets over uitbetaling?) en `https://twenty.com/apps` (apps van anderen?).
- npm `twenty-sdk` per maand en de sterren op twenty.com/apps.
