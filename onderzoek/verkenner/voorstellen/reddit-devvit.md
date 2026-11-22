# Voorstel: Reddit Developer Platform (Devvit)

Vera, 15 nov 2026, run 19:31 (Amsterdam). Nagekeken door een controleur (10 van 10 rijen goed, analyse opnieuw gedraaid en gelijk).

## Wat het is
Spellen en apps die in posts en subreddits op Reddit draaien. Bouwen met Devvit Web: gewone HTML, CSS en TypeScript (React, Phaser of Three.js), met een Node-server en Redis bij Reddit. Geld via de Reddit Developer Funds (Reddit betaalt bij drempels in dagelijkse spelers of installaties) en via verkopen in de app voor Reddit Gold.

## Advies: nee voor nu, cijfer 4
Bouwen past heel goed en Thijs kan als particulier in Nederland meedoen. Maar het geld voor kleine makers is per 1 augustus 2026 flink verder weg gezet: het fonds betaalt bij spellen pas vanaf 5.000 dagelijkse spelers (was 500), en het programma loopt tot 31 dec 2026 zonder woord over 2027. Bereik van spellen bepaalt Reddit zelf met uitgelichte plekken; dat is vanaf hier niet te meten. Bij de gewone apps in de gids (vooral moderatortools) krijgen nieuwkomers weinig: lichting mei t/m aug 2026 mediaan 2 subreddits.

## Eigen meting (GEZIEN)
Bron: de appgids developers.reddit.com/apps (robots.txt staat /apps en /docs toe; www.reddit.com verbiedt alle bots, daar heb ik niets gelezen). Alle 91 pagina's twee keer gelezen, daarna per app de pagina: installCount (aantal subreddits waar de app op staat), createdAt (aanmaakdatum van de Devvit-app), maker en categorie. 1.670 unieke apps van de 1.813 in de gids. Data en scripts: `data/reddit-devvit-apps-2026-11-15.jsonl`, `data/reddit-devvit-*-script.py`.

Drukte: nieuwe apps in de gids per maand: jan 2026 79, apr 73, mei 195, jul 157, sep 155, okt 185. Het groeit snel (± 2,5 keer zoveel als begin 2026).

Installs per lichting (alleen apps die in de gids staan):

| Lichting | n | mediaan | 10+ | 50+ | 250+ |
|---|---|---|---|---|---|
| mei t/m aug 2026 (3 tot 6 maanden oud) | 597 | 2 | 13% | 2% | 1% |
| waarvan moderatortools | 146 | 4 | 29% | 5% | 2% |
| waarvan spellen | 222 | 2 | 4% | 0% | 0% |
| jan t/m apr 2026 | 275 | 3 | 21% | 5% | 1% |
| jul t/m dec 2025 | 185 | 5 | 34% | 14% | 4% |
| moderatortools jul t/m dec 2025 | 29 | 43 | 79% | 48% | 21% |

Beste nieuwkomers sinds mei: image-magician 1.333, auto-sticky 656, automod-neo 602, allemaal moderatortools. 759 verschillende makers sinds mei; één maker heeft er 23.

Wat de meting niet zegt (controleur):
- installCount telt subreddits, geen spelers. Spellen draaien in een paar eigen subreddits en staan standaard niet in de gids ("unlisted", volgens de launch-gids van Reddit ideaal voor spellen). Word Herd kreeg in nov 2025 een uitbetaling uit het fonds en heeft 10 installs. Het bereik van spellen is vanaf hier dus niet te meten. Meten kan alleen met spelerscijfers uit Reddit zelf (de maker ziet ze) of met toegang tot reddit.com, die robots.txt verbiedt.
- ±8% van de gids mist, allemaal kleine apps met 1 tot 3 installs. De cijfers zijn dus iets te gunstig.
- 25% van de apps heeft geen categorie, dus de groepen spellen en moderatortools zijn onvolledig.

## Geld (GEZIEN in de voorwaarden van Reddit, tenzij anders vermeld)
- Developer Funds, H2 2026 Terms (1 aug t/m 31 dec 2026, support.reddithelp.com artikel 50860336905108, bijgewerkt 13 nov 2026): eenmalig $4.000 als een app gemiddeld 5.000 "Daily Qualified Engagers" haalt over 7 dagen (ingelogde gebruikers in SFW-communities met 300+ wekelijkse gebruikers). Daarna maandelijks op aanvraag: 6.000 geeft $111, 10.000 $556, 50.000 $5.000. Installatiebonus: 50, 250 en 1.000 installaties in communities met 300+ wekelijkse gebruikers geven $500, $1.000 en $2.000. Hooguit 3 apps per maker.
- Het oude programma (1 apr 2025 t/m 31 jul 2026) betaalde al vanaf 500 spelers ($500). Toen kregen ±60 apps samen $163.000 in één maand (nov 2025, blog van Reddit). Dat is voorbij.
- Gold: maker krijgt $0,01 per gebruikte gold; speler betaalt $1,79 tot $1,99 per 100 gold, dus de maker krijgt ±50 tot 56%. Uitbetaling vanaf $10, 30 tot 45 dagen na de maand, $2,25 plus 0,25% kosten. Geen omzet per app openbaar.
- Hackathons: Reddit hield in 2025 en 2026 elke paar maanden een hackathon met $40.000 tot $49.000 prijzengeld (hoofdprijs $15.000, tien keer $1.000). Een winnaar die niet programmeerde won $15.000 met een spel dat in 27 dagen af was (DERDEN, phaser.io mei 2026). Nu loopt er geen.
- Meedoen: 18+, Nederland staat op de landenlijst, identiteitscheck via Persona, uitbetaling via Stripe Connect. Geen bedrijf of KvK genoemd (support artikel 37760672112660, bijgewerkt 15 nov 2026).

Wat er voor kleine makers nu realistisch overblijft: de installatiebonus van $500 voor een moderatortool (5% van de nieuwe moderatortools haalt 50 installs binnen 3 tot 6 maanden, en dan moeten die subreddits ook nog 300+ wekelijkse gebruikers hebben), wat gold-verkopen in een spel dat Reddit uitlicht, en hackathonprijzen.

## Bereik en vindbaarheid
Reddit kiest zelf welke spellen het uitlicht, in vier treden (banner op r/GamesOnReddit, plek in de Games Feed, bovenaan de Games Feed, één spel per week in de Home Feed). Ze kijken naar klikratio, terugkeer op dag 1 en 3 en speeltijd. Aanvragen kan met een formulier. Een spel moet een eigen subreddit hebben. Moderatortools worden gevonden in de gids, op volgorde van populariteit, dus oude toppers staan bovenaan.

## Past het bij ons
Ja, technisch goed: TypeScript en Phaser, een npm-CLI, testen in een eigen testsubreddit met `npm run dev`, keuring door Reddit meestal 1 tot 2 werkdagen. Beperkingen: geen websockets, client mag niets van buiten ophalen, alleen Gemini en ChatGPT als taalmodel en alleen na goedkeuring. Reddit wil geen "AI slop" (DERDEN, hackathon 2026). Thijs moet een Reddit-account hebben, de Earn Terms accepteren, Persona en Stripe doen. De app staat dan onder zijn Reddit-naam, en het spel vraagt een eigen subreddit die iemand moet modereren.

## Score op de lat van een 8
1. Nieuwe kleine makers verdienen nu: zwak. De lage drempel is weg, geen omzet per app openbaar.
2. Bereik voor nieuwkomers: niet te meten voor spellen (redactioneel), zwak voor gewone apps (mediaan 2).
3. Bouwen en testen: sterk.
4. Thijs kan binnen een week verkopen: redelijk (geen KvK, wel ID en Stripe), maar gold-producten worden apart gekeurd.

Eén van vier sterk: cijfer 4.

## Eerste idee als het ooit ja wordt
Een dagelijks puzzelspel in Phaser met Gloop uit Het Hol, met kleine cosmetica voor gold, plus meedoen aan de volgende hackathon van Reddit. Een hackathon is de enige snelle geldkans: als Reddit er een aankondigt met prijzengeld, is meedoen met een spel dat we toch al hebben het overwegen waard (eerst nakijken of Nederlanders mogen meedoen).

## Opnieuw wegen
Begin jan 2027: de voorwaarden voor 2027 lezen (support artikel van de Developer Funds). Komt de drempel weer rond 500 spelers, of wordt er een hackathon aangekondigd: opnieuw wegen. Herhaal dan ook de gidsmeting met de scripts in `data/`.
