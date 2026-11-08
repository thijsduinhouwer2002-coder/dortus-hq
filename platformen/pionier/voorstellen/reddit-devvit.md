# Voorstel: Reddit Developer Platform, Devvit (pionier)

Noor, pionier. Run 8 nov 2026, ±06:40 tot ±07:40 UTC. Onderzoeker (agent) voor groei, geld, vraag en risico. Zelf gemeten: de hele openbare appgids op developers.reddit.com/apps (1.759 apps, installs per app, en per app de aanmaakdatum, maker en categorie van de detailpagina; `data/devvit-apps-2026-11-08.json`, script `data/devvit-apps-meet.py`). Controleur (agent) rekende de telling na en las de voorwaarden van H1, H2 en het Developer Program via de Zendesk-API: akkoord met correcties, verwerkt. Zelf nagelezen: de voorwaarden van Reddit Developer Funds H2 2026, de kwartaalcijfers Q3 2026, het artikel over het sluiten van de Data API, de docs over betalen.

**Cijfer: 6 van 10. Advies: ja, met kleine inzet, in de categorie moderatie tegen reposts en AI-inhoud. Haast is nuttig: de oude API stopt in maart 2027.**

Wat is Devvit: apps die binnen Reddit draaien. Moderators installeren ze in hun subreddit (mod-tools), of een app draait als bericht in de feed (spellen, "interactive posts"). Code in TypeScript, Reddit host alles. De gids is openbaar en toont installs (aantal subreddits) per app.

Waarom dit geen oceaan is, al is Reddit groot: het platform onder de apps is jong (de meeste apps zijn van 2026) en Reddit duwt nu iedereen ernaartoe. Alle bots op de oude Data API moeten over, en die bots worden nu pas opnieuw gebouwd.

## 1. Groeit het platform hard en zichtbaar? Ja, vooral de winkel; Reddit zelf matig.

- Reddit Q3 2026: 130,3 miljoen dagelijkse bezoekers (DAUq), +12% op jaarbasis; omzet $895 miljoen, +53% (GEZIEN, https://www.sec.gov/Archives/edgar/data/1713445/000171344526000114/earningspressreleaseq326.htm). Maar t.o.v. Q2 stond DAUq stil en in de VS -2% op jaarbasis (DERDEN volgens de onderzoeker, zelfde bron, aandeelhoudersbrief). Ingelogde gebruikers en app-gebruikers groeiden wel per kwartaal (GEZIEN, zelfde bron).
- **Nieuwe apps per maand in de gids** (GEZIEN, eigen telling op aanmaakdatum, alleen apps die nu nog openbaar staan): 2024 3 tot 16 per maand; mei tot okt 2025 samen 133 (±22 per maand); nov 2025 tot apr 2026 53, 61, 76, 80, 63, 77; mei tot okt 2026 213, 141, 176, 118, 154, 198. **Dat is ±8 keer zoveel per maand als een jaar geleden.**
- Motor: Reddit stopt met de openbare Data API. RSS stopt op 13 nov 2026, bots die zich niet aanmeldden verliezen toegang op 12 jan, de API gaat dicht in maart 2027; 14.000+ bots en apps meldden zich aan en moeten naar Devvit (DERDEN, https://ppc.land/reddit-to-halt-public-data-api-access-in-march-2027-as-14-000-apps-register/, 4 okt 2026). Reddit betaalt $1.000 per overgezette bot (potje $1 miljoen, aanmelden tot 30 nov 2026) (DERDEN volgens de onderzoeker, https://support.reddithelp.com/hc/en-us/articles/47822311698452).
- Spellen: een games-tab in de app wordt getest (1% van de gebruikers in maart, 5% in juni 2026) (DERDEN, https://karmium.com/guides/reddit-games-tab/), hackathons met $40.000 prijzengeld (DERDEN, https://phaser.io/news/2026/06/reddit-and-phaser-launch-a-40-000-game-dev-hackathon).

## 2. Is de winkel jong? Ja.

- 1.759 apps in de gids (GEZIEN). 1.032 daarvan zijn gemaakt sinds mei 2026, dus 59% is jonger dan een half jaar (GEZIEN).
- Per soort (Reddit's eigen categorie, GEZIEN): 616 spellen (samen 3.229 installs, want spellen draaien vooral in hun eigen subreddit), 263 mod-tools (samen 62.946 installs), 679 zonder categorie.
- Alle installs samen 122.675; mediaan 3; 107 apps boven 100, 23 boven 1.000 (GEZIEN).

## 3. Kan er betaald worden? Ja, op twee manieren, maar het fonds is onzeker na 2026.

- **Reddit Developer Funds H2 2026**, 1 aug tot 31 dec 2026, max 3 apps per maker (GEZIEN, https://support.reddithelp.com/hc/en-us/articles/50860336905108-Reddit-Developer-Funds-H2-2026-Terms, laatst bijgewerkt 4 nov 2026):
  - Installs: $500 bij 50 "qualified installs" (subreddits met 300+ wekelijkse bezoekers, veilig voor werk), +$1.000 bij 250, +$2.000 bij 1.000. Samen $3.500 per app, eenmalig per trede, 7 dagen vasthouden.
  - Gebruik: $4.000 eenmalig bij gemiddeld 5.000 dagelijkse gebruikers, daarna maandelijks oplopend ($556 bij 10.000, $5.000 bij 50.000, $25.000 bij 1 miljoen).
  - Voor de maandelijkse uitbetaling moet je je apart aanmelden (GEZIEN, zelfde bron).
  - Bij gebruik strenger dan in H1 (1 apr 2025 tot 31 jul 2026: toen al $500 bij 500 dagelijkse gebruikers, tot $167.000 per app); bij installs niet duidelijk strenger (toen telde een subreddit met 1.000+ leden, nu met 300+ wekelijkse bezoekers) (GEZIEN door de controleur, https://support.reddithelp.com/api/v2/help_center/en-us/articles/27958169342996.json). Na 31 dec 2026 is niets aangekondigd.
  - Reddit betaalde in nov 2025 $163.000+ uit aan ±70 apps (DERDEN, https://developers.reddit.com/docs/blog/2025/12/18/november-payouts).
- **Betalen in de app** met Reddit Gold: de maker krijgt $0,01 per gold, gebruikers betalen $1,79 tot $1,99 per 100 gold, uitbetaling vanaf $10 (GEZIEN door de controleur, https://support.reddithelp.com/hc/en-us/articles/30641905617428-Developer-Program). Gebruikers betalen $1,79 tot $1,99 per 100 gold (DERDEN volgens de onderzoeker), dus de maker houdt ±50 tot 56% (gerekend). Elk product wordt gekeurd (GEZIEN, https://developers.reddit.com/docs/earn-money/payments/payments_overview). Nederland staat op de landenlijst; wel 18+, ID-controle via Persona en Stripe Connect (DERDEN volgens de onderzoeker). Dat is een stap voor Thijs.
- Eerlijk: moderators betalen zelden voor tools. Bij mod-tools is het fonds de geldroute, bij spellen de verkoop van gold-items. Voor Dortus komt bereik eerst, en dat past.

## 4. Is er al vraag te zien? Ja, heel concreet, met een datum.

- 14.000+ bots moeten over, in TypeScript, terwijl de meeste in Python zijn geschreven (PRAW). De maker van Repost Sleuth (een van de bekendste bots tegen reposts) vond geen route vanwege het rekenwerk; de mods van r/science verwachten dat hun bots breken (DERDEN, ppc.land, zelf nagelezen).
- Moderators vinden Reddit's eigen AI-regelhulp (Rules Hub) te zwak: "Automod is load bearing", hij handhaaft 2 van de 8 regels (DERDEN, https://radar.zurb.com/article/reddit-mods-automod-is-load-bearing-and-rules-hub-enforces-2-of-8-rules).
- De apps die echt groeien zijn mod-tools: van de 1.032 nieuwe apps sinds mei kwamen er 8 boven 100 installs, en 7 daarvan zijn mod-tools (GEZIEN). Bovenaan: Image Magician (reposts) 1.319, Automod Neo 532, Automated Sticky Comments 412, YouTube Info and Enforcer 279.
- Niet gelukt: r/Devvit, r/ModSupport en r/modhelp lezen (403 op reddit.com, ook via about.json). Ledenaantallen ontbreken dus.

## 5. Is de eerste plek in een categorie nog te pakken? In repost- en AI-moderatie: ja, nog net.

- Bij algemene mod-tools zit een sterke maker: fsv (onder meer Bot Bouncer 12.294, Comment Mop 6.912, Evasion Guard 4.792, Hive Protector 3.332, Modmail Automator 2.197, Automod Neo 532) (GEZIEN). Daar niet tegen in gaan.
- **Repost- en duplicaatdetectie** (regex `repost|duplicate` op naam en omschrijving): 19 apps, samen 2.760 installs; nummer één Image Magician 1.319, pas sinds 24 mei 2026, van één maker (CosmicKeys) (GEZIEN). Repost Sleuth, de oude leider, heeft geen route naar Devvit. Op Reddit zijn reposts een van de grootste ergernissen, dus het plafond ligt veel hoger dan 1.319 (GOK).
- **AI-inhoud herkennen**: ±11 tot 15 apps (afhankelijk van de zoekterm), samen ±1.000 tot 1.400 installs. Stop AI 954 ("scans posts and comments for AI text, finds reposts") en Image Moderator 343 ("Detect AI images"), de rest klein (GEZIEN, nageteld door de controleur). Zwak bezet, en een groeiende klacht.
- Let op: Stop AI doet repost en AI-tekst al samen, dus "beide in één tool" is niet nieuw. Stop AI is de directe concurrent, met 954 installs na een jaar (sinds okt 2025). Image Magician groeide in 5 maanden harder (1.319).
- Waarom wij toch beter kunnen: geen van beide combineert beeld (perceptuele hash), titel, link en AI-tekst met een duidelijke uitleg aan de plaatser en een link naar het origineel; wij voegen een import toe van de wiki-instellingen van Repost Sleuth en Magic Eye (de bots die nu stoppen), een rustig overzicht in het modmenu, en we testen in de echte omgeving. De concurrenten lijken projecten van één persoon (GOK op basis van de makersnamen). De eerste plek is dus te pakken maar niet leeg; dat drukt het cijfer naar de onderkant van een 6.

## Risico: haalt het platform het?

- Reddit is groot, winstgevend (nettowinst $283 miljoen in Q3, GEZIEN) en zet zijn API-beleid op Devvit. Dat Devvit verdwijnt is onwaarschijnlijk (GOK).
- Echte risico's: (a) Reddit verandert eenzijdig de regels, zoals bij de API-prijzen in 2023 (DERDEN, https://en.wikipedia.org/wiki/Reddit_API_controversy); (b) het fonds stopt na 31 dec 2026 of wordt nog strenger; (c) Reddit bouwt reposts of AI-detectie zelf in; (d) nieuwe apps krijgen weinig bereik: mediaan 2 installs voor apps sinds mei (GEZIEN). Alleen een tool die een echt gat vult, groeit.
- Teken dat het stokt: minder dan 100 nieuwe apps per maand twee maanden op rij, geen nieuw fonds voor 2027, of Reddit kondigt eigen repostdetectie aan. Herhaalmeting rond 8 dec: `python3 data/devvit-apps-meet.py`.

## Eerste productidee

**Repost- en AI-wachter voor moderators** (werknaam). Bij elk nieuw bericht: vergelijkt plaatje (perceptuele hash), titel en link met eerdere berichten in dezelfde subreddit, en geeft een score of het op AI lijkt. Moderator kiest per drempel: melden, verwijderen met een nette uitleg en link naar het origineel, of alleen een notitie in de modlijst. Import van bestaande Repost Sleuth- en Magic Eye-instellingen uit de wiki. Gratis, met het fonds als eerste geld. Realistisch eerste doel: 50 subreddits met 300+ wekelijkse bezoekers ($500); 250 en 1.000 (samen $3.500) is het maximum, want van de 1.032 nieuwe apps sinds mei haalden er maar 8 de 100 installs; later eventueel een betaalde laag voor grote subreddits als Reddit dat toestaat.
Eerst nakijken: kan Devvit beelden ophalen en hashen binnen de rekenlimiet, en hoeveel opslag (Redis) krijgt een app per subreddit. Image Magician bewijst dat beeldvergelijking binnen Devvit kan (GOK op basis van de omschrijving).

## Wat ik niet kon meten
- Wanneer apps uit de gids verdwenen (de telling per maand bevat alleen apps die er nu nog staan).
- Spelers per spel en ledenaantallen van subreddits (reddit.com geeft 403 aan curl).
- Hoeveel van de 14.000 aangemelde bots mod-tools zijn die moderators zelf niet kunnen overzetten.

## Wat Thijs moet doen als het ja wordt
Een Reddit-account voor Dortus, het Developer Program en de verificatie (18+, Persona, Stripe Connect) om geld uit het fonds te ontvangen. Bouwen en testen kan zonder geld; een eigen test-subreddit is nodig.
