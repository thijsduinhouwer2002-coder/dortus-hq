# Keuring van B-ai-winkels.md (17 nov 2026)

Alles zelf opnieuw gelezen met curl bij de primaire bron, tenzij anders vermeld. WebSearch alleen om bronnen te vinden.

## 1. Claude connectors directory

**Aantal items: DEELS.**
- De 2.000+ komt uit Anthropic's eigen blog over Claude Marketplace (https://claude.com/blog/claude-marketplace, 23 sep 2026: "more than 2,000 available today"). Dat klopt als citaat.
- De openbare lijst telt minder: https://claude.com/connectors toont "1137 connectors" en https://claude.com/plugins toont "532 plugins" (gezien 17 nov 2026). Samen 1.669. Mogelijk telt de blog ook dingen mee die niet op de openbare pagina staan.
- Wat telt: het is druk en het wordt drukker. In de paginadata zie ik per maand toegevoegde connectors: 135 (jun), 165 (jul), 187 (aug), 114 (sep), 85 (okt). Niet vroeg, dat klopt.

**Indienen: KLOPT, en het is makkelijker dan de onderzoeker schreef.**
- Iedereen met een betaald plan (Pro, Max, Ultra, Team, Enterprise), geen partnerprogramma (https://claude.com/docs/directory/publish.md, gezien 17 nov 2026).
- Correctie: de onderzoeker schreef "de keuring duurt ONBEKEND lang". De docs zeggen dat een connector automatisch wordt gescand en "by default" als Community connector wordt gelist, zonder actie van jou. Pas later kan Anthropic hem automatisch doorzetten naar Verified-keuring, en daar kun je niet om vragen (https://claude.com/docs/connectors/verification.md en https://claude.com/docs/connectors/building/submission.md). Binnen 7 dagen in de lijst staan is dus haalbaar. Een plugin-bundel krijgt wel altijd een mens die kijkt voor hij live gaat.
- Wat je moet regelen: een eigen https-server, OAuth 2.0, privacybeleid, documentatie-URL, support-adres, icoon, en voor een MCP App 3 tot 5 schermafbeeldingen.

**Betaald eigen abonnement achter OAuth: KLOPT (geen verbod gevonden), en het is sterker dan een GOK.**
- In de Software Directory Policy (https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy) en de Directory Terms (https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms) staat geen woord over betalen, abonnementen of upsell. Wel verboden: advertenties en gesponsorde inhoud, crypto (meestal), geld overmaken zonder mens ertussen, en het maken van beeld, video en audio met AI (behalve ontwerphulp).
- Het indienformulier vraagt zelf bij stap 4 "what users need before they can connect, such as accounts, plans, or other setup" (submission.md). Anthropic rekent er dus op dat er een account of plan achter zit.
- Let op: stap 9 heeft een verplichte verklaring over "financial transactions". De tekst daarvan staat alleen in het portaal; ONBEKEND wat er precies in staat.
- Er is geen kassa van Anthropic voor makers. Afrekenen gaat op je eigen site. Het "kopen" in Claude Marketplace is alleen voor bedrijven met vastgelegd Anthropic-tegoed, op aanvraag (blog 23 sep). Dat klopt zoals de onderzoeker schreef.

**Zijpaneel van 10 nov alleen voor partners: DEELS.**
- De blog (https://claude.com/blog/interactive-connectors-full-tool, 10 nov 2026) begint met "a small group of tools from our directory" (Asana, Canva, Carta, Dropbox, monday.com, Smartsheet, Vercel, Webflow). Maar er staat ook: "Support for these capabilities is in public preview for developers. Developers can start building with them today."
- In de docs: zijpaneel en volledig scherm (https://claude.com/docs/connectors/building/mcp-apps/display-modes.md) en app tools (app-tools.md) zijn "available to a limited set of organizations". Dat gaat over welke gebruikers het al hebben (uitrol), niet over welke makers. Een Community-connector mag het dus gebruiken; niet iedere gebruiker ziet het al.
- Echt beperkt tot Verified: entry points (app openen zonder prompt, vanaf de Artifacts-pagina) en ingesloten websites. "Connectors installed from a Community listing can't" (entry-points.md, getting-started.md). Verified kun je niet aanvragen.
- Conclusie: de onderzoeker trok het te ver. Zijpaneel en volledig scherm kan een kleine maker gewoon bouwen. Openen zonder prompt niet.

**Cijfer onderzoeker 5: eens.** Beste etalage (zoeken, Suggested Connectors in het gesprek, rangschikking op gebruik, bevestigd in https://claude.com/docs/connectors/directory.md), snel in de lijst, eigen abonnement mag waarschijnlijk. Maar niet vroeg, geen kassa in de winkel, en Claude doet veel zelf. De correcties maken het iets beter (snellere keuring, zijpaneel bruikbaar), niet genoeg voor meer dan een 5.

## 2. Cowboy General Store

**Alleen op uitnodiging: DEELS.**
- Bladeren is open: https://cloud.cowboy.inc/general-store laat zonder inloggen 129 items zien, en de docs zeggen "Discovery is public and needs no wallet or account login" (https://cowboy.inc/references/cowboy/store.md).
- Huren en verkopen lopen via "Request an invite": de knop "Sell in the Store" op https://cowboy.inc opent hetzelfde uitnodigingsformulier (data-sf-invite="sell"). Dus voor Dortus als verkoper: ja, op uitnodiging.

**Gericht op crypto: DEELS.**
- Crypto staat vooraan: Hyperliquid-handel, Polymarket, ETH-prijswachter, eigen keten (actors draaien "on chain", betalingen en splits gaan via wallets; skill.md en pricing.md).
- Maar de winkel is breder dan crypto: veel gewone items zoals Brave Search, Exa Search, Event RSVP, Poll, NASA Picture of the Day, Anchor Browser, Lobsters. Op de winkelpagina komt "hyperliquid" 17 keer voor en "crypto" 9 keer op 129 items. Breder dan "vooral crypto", maar de bouw (wallets, keten) is crypto.

**Kassa: KLOPT NIET. Belangrijkste fout in het stuk.**
- De onderzoeker gaf wet 3 "ja op papier: maandhuur, per gebruik, eenmalig, uitbetaling via Stripe". De eigen docs zeggen iets anders: "Every listing is free to hire today" en "Coming soon: paid listings. Prices will be set and shown in dollars." (https://docs.cowboy.inc/sell/pricing.md, gezien 17 nov 2026). Ook https://docs.cowboy.inc/sell/list-an-actor.md: "Today every listing is free to hire, so the first listing you make is a free one."
- Op de winkelpagina: 128 van 129 items "Free", één item met "$5.00 about every 30 days".
- Stripe-uitbetaling heb ik in de docs niet gevonden; ONBEKEND. Betalingen worden in de docs beschreven als splits tussen wallet-adressen.
- Wel interessant voor later: dit is precies een winkel die "net een kassa gaat krijgen". Als betaalde listings live gaan, wordt het opnieuw bekijken.

**Cijfer onderzoeker 3: niet eens, ik geef 2.** Geen kassa vandaag, verkopen op uitnodiging, crypto-bouw, geen bewezen kopers.

## 3. OpenAI: digitale verkoop in ChatGPT-apps

**KLOPT.**
- https://developers.openai.com/apps-sdk/app-submission-guidelines.md (gezien 17 nov 2026), kop "Commerce and monetization": "Currently, plugins may conduct commerce only for physical goods. Selling digital products or services, including subscriptions, digital content, tokens, or credits, is not allowed, whether offered directly or indirectly (for example, through freemium upsells)."
- https://developers.openai.com/plugins/build/monetization.md: "current approval is limited to plugins for physical goods purchases".
- Kleine aanvulling die de onderzoeker half noemde: "Users may sign in to an existing paid account and access features already included in their subscription." Inloggen op een bestaand betaald account mag dus, maar je mag geen plannen tonen, geen abonnement starten en geen upgrade promoten. Ook in beschrijvingen geen prijzen of proefperiodes. Voor Dortus komt dat neer op: geen kassa, want nieuwe kopers kun je daar niet werven.
- TechCrunch (29 sep 2026) bevestigt dat OpenAI op Dev Day niets aankondigde om dit te veranderen.

**Cijfer onderzoeker 1: eens.**

## 4. Datums

**Grok Build Plugin Marketplace 11 jun 2026: KLOPT.** https://x.ai/news/grok-plugin-marketplace laadde nu wel met curl (titel "Grok Build Plugin Marketplace"), datum 2026-06-11 in de pagina. De GitHub-repo kon ik niet openen (geen toegang in deze sessie), dus het aantal van 36 plugins heb ik niet nageteld.

**ChatGPT Sites 9 jul 2026: KLOPT, maar niet bij de primaire bron.** De OpenAI-pagina (https://openai.com/index/chatgpt-for-your-most-ambitious-work/) geeft 403. Flavio Copes (https://flaviocopes.com/chatgpt-sites/, 17 nov 2026) schrijft "OpenAI launched Sites in public beta on July 9, 2026, together with ChatGPT Work" en "I tried Sites on launch day, July 9, 2026". Andere berichten (mixed-news, testingcatalog, igeeksblog) noemen ook de lancering samen met ChatGPT Work. Ik reken het als bevestigd door twee onafhankelijke bronnen.

**Cijfers Grok (2) en Sites (in 1 meegenomen): eens.**

## 5. Gemist? Een AI-winkel die nu opengaat met kassa en etalage voor een kleine maker

Gezocht met WebSearch en curl. Gevonden, maar geen enkele haalt kassa plus open etalage:

### Google Connected Apps Platform (Gemini en Search)
- Bestaat: JA. Google-blog "Build and manage Connected Apps in one place", 28 okt 2026, volgens PPC Land (https://ppc.land/google-opens-preview-for-third-party-apps-inside-search-and-gemini/, 28 okt 2026). Ontwikkelaarspagina https://developers.google.com/connected-apps toont "Apply for the preview" (gezien 17 nov 2026).
- Wat het is: MCP-servers (of Android AppFunctions) inbouwen in Gemini en Google Search, via een Connected Console met keuring. Meer dan 50 apps, allemaal merken (Adobe, Calm, Experian, Peloton).
- Wet 1: deels. Drie weken oud, maar toegang "in phases" op aanvraag; binnen 7 dagen staan is niet zeker. Wet 2: onbekend, gericht op diensten (boeken, fitness, tickets). Wet 3: ONBEKEND, het bericht noemt geen kosten en geen betaalregels. Wet 4: Google doet veel zelf. Vraag 5: ja als je erin komt, Gemini en Search sturen zelf taken door naar een app.
- Cijfer: 3. Waard om aan te vragen omdat we toch MCP bouwen (dezelfde server kan ook naar de Claude directory), maar zonder bekende kassa.
- Hoort mogelijk bij een andere onderzoeksgroep; in B stond hij niet.

### Cursor Origin Marketplace
- Bestaat: JA volgens BuildMVPFast (https://www.buildmvpfast.com/blog/cursor-origin-app-marketplace-dev-tools-2026, 26 okt 2026): open voor openbare inzendingen sinds 13 okt 2026. Primaire bron niet gelezen.
- Wet 3: nee. "Listing is free, you can't charge through it", en het bereik is alleen teams die hun code op Origin hosten.
- Cijfer: 2.

### Betaalde skill- en agentwinkels
- Losse winkels met betaalde skills of agents bestaan (SkillHQ, Capafy, 402md, kleine "agent marketplaces" op dev.to en vercel.app), maar geen ervan heeft aantoonbaar echte kopers. Dat is het Gumroad-probleem. Geen nieuwe gevonden die daar anders in is.

**Conclusie gemist: NIET GEVONDEN.** Ik vond geen AI-winkel die nu opengaat met een eigen kassa, een etalage die kopers aanvoert, en open toegang voor een kleine maker. Het dichtst bij: Cowboy (etalage en straks kassa, maar nu alles gratis en op uitnodiging).

## Oordeel over de cijfers van de onderzoeker

| Tip | Onderzoeker | Keurder | Waarom |
|---|---|---|---|
| Claude connectors | 5 | 5 | Eens; keuring sneller en zijpaneel ruimer dan gedacht, maar geen kassa en niet vroeg |
| Cowboy | 3 | 2 | Kassa bestaat vandaag niet: alles gratis, betaald "coming soon" |
| Grok | 2 | 2 | Eens, datum klopt |
| ChatGPT | 1 | 1 | Eens, verbod staat er nog letterlijk |
| Stitch / skills.sh | 2 | 2 | Niet nagezocht, geen reden tot twijfel |
| Zoom, ElevenLabs, Google Cloud | 1 | 1 | Niet nagezocht, geen reden tot twijfel |

Het stuk is netjes en eerlijk over wat GOK is. Twee echte fouten: de Cowboy-kassa (beschreven alsof hij er is) en "zijpaneel alleen voor partners" (te streng gelezen). Eén te voorzichtige GOK: eigen abonnement achter OAuth mag vrijwel zeker.

## Eigen top

**Niets haalt een 7.**

1. Claude connectors directory (5). Echte etalage, in een paar dagen gelist als Community connector, en een eigen abonnement achter OAuth staat nergens verboden (het formulier vraagt er zelfs naar). Zwak: geen kassa in Claude, 1.137 connectors en 532 plugins op de openbare lijst, en Claude bouwt veel zelf. Alleen zinvol met een brede taak die Claude zelf niet doet en waar geen groot merk zit.
2. Cowboy General Store (2), maar als wachtpost. Niet nu instappen. Wel een uitnodiging aanvragen en de pagina https://docs.cowboy.inc/sell/pricing.md in de gaten houden: op de dag dat betaalde listings live gaan, is dit een winkel die "net een kassa krijgt", en dan opnieuw keuren.
