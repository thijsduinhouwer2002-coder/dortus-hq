# Voorstel: Discord Activities

**Advies: nee voor nu. Cijfer: 4 van 10.** Onderzocht op 15 nov 2026, run 13:31 (Amsterdam), door Vera met één onderzoeker en één controleur.

Kort: de voorwaarden zijn goed (Discord houdt 15% in tot $1M, makers in de EU mogen verkopen, bouwen kan met gewone webtechniek vanaf Linux) en het aanbod groeit hard. Maar nieuwe Activities halen weinig bereik: van de lichting mei t/m aug 2026 staat de middelste na 3 tot 6 maanden op 5 servers, en maar 9% haalt 100 servers. Gewone bots uit dezelfde maanden staan op 18 en 18%, maar die vergelijking is scheef: een bot moet aan een server worden toegevoegd, een Activity niet, dus servers is voor Activities stelselmatig een te lage maat. Ook met een ruime omrekening blijft het bereik ver onder Poki. De plekken in de Launcher kiest Discord zelf en ze gaan bijna allemaal naar titels van 2024 en begin 2025 van studio's. Verkopen zijn nergens te zien, en ik vond geen enkele kleine maker die een bedrag noemt. Wel een goed bijkanaal: een webspel dat al op Poki draait kan met weinig werk ook als Activity.

## Wat ik zelf mat (GEZIEN)

**Bron:** de openbare zoek-API van de App Directory (`discord.com/api/v9/application-directory-static/search`, geen sleutel), dezelfde ingang als bij de Discord-meting van 6 nov, nu met 11 categorieën (ook de verborgen 1, 2, 3, 5 en 7) en 22 zoektermen. 20.117 unieke apps opgehaald (de directory telde op 6 nov ±19.600). Een app is een Activity als de vlag EMBEDDED (1<<17) aan staat en `embedded_surfaces` gevuld is; dat klopt bij alle bekende Activities die ik nakeek (Wordle, Whiteboard, Death by AI, Farm Merge Valley, Smash Karts). De vlag telt ook bots met een loze of nooit afgemaakte Activity mee (de controleur vond NAN Bot, moderatie; in de lichting mei t/m aug zitten 69 apps in Moderation and Tools en 69 in Utilities). Alleen de categorie Games geeft bijna dezelfde mediaan: 6 servers (334 apps). De directory toont bovendien alleen geverifieerde apps die zich voor Discovery aanmeldden; niet-geverifieerde kleine Activities vallen buiten de meting. Bij 2 apps ontbreekt het aantal servers. De aanmaakdatum zit in het id van de app. De zoekronde is na 22 van de 45 geplande zoektermen gestopt omdat elke nieuwe term nog maar ±100 apps toevoegde; het kan dus zijn dat ±1 tot 5% van de Activities ontbreekt (GOK).

- **Aantal:** 2.689 van de 20.117 apps (13,4%) hebben een Activity. Let op: daar zitten ook oude bots bij die er later een Activity bij kregen (Rythm, Dank Memer).
- **Drukte, nieuwe Activities per aanmaakmaand:** jan 2025 41, jan 2026 58, mei 2026 92, aug 175, sep 215, okt 325. In oktober 2026 dus ±8 keer zo veel als begin 2025, en het stijgt nog elke maand.
- **Bereik, lichting mei t/m aug 2026 (509 Activities, nu 3 tot 6 maanden oud), aantal servers volgens Discord (afgerond):**
  - mediaan 5, kwartielen 2 / 5 / 20, 90e percentiel 67; 33 staan op 0 (bij de andere apps 9 van 1.747, wat past bij de te lage maat voor Activities);
  - 100+ servers: 9%; 1.000+: 2%; 10.000+: geen;
  - per maand: mei 92 apps mediaan 8 (11 met 100+), jun 119 mediaan 7 (13), jul 123 mediaan 4 (7), aug 175 mediaan 5 (13);
  - ter vergelijking, gewone apps zonder Activity uit dezelfde maanden (1.747): mediaan 18, 18% met 100+ (scheve vergelijking, zie de beperking hieronder).
  - lichting sep 2025 t/m apr 2026 (472): mediaan 15, 18% met 100+, 2% met 1.000+.
- **Doorbrekers sinds sep 2025 met 1.000+ servers:** 24, waarvan ongeveer 9 gewone bots met de vlag (kayo, Keeper, ServerSweep, Chat GPT, Redy, Redy 1, Crystal, een Arabische bot, Among Us) en een stuk of 6 van grote merken of bekende spellen (Words with Friends-makers, Riot met VALORANT, NYT Connections, Resident Evil-trailer, Red Bull). Echt nieuw en van een onbekende maker: **DisDubs** (aangemaakt aug 2026, nasynchroniseren in een spraakgesprek, 9.750 servers, met betaalvlag en een abonnement en scenepakketten van $2,99), **LoFi Pomodoro Sessions** (nov 2025, 2.560, met betaalvlag), **Pomo** (1.580), **ULTRAKIDLE** (1.580), **Krillion** (1.370). Wie achter DisDubs zit staat niet op de site; dat het een kleine maker is, is een GOK.
- **Geld in de winkel:** 89 van de 509 nieuwe Activities (17%) hebben de betaalvlag. Van de 269 Activities sinds sep 2025 met betaalvlag of winkel hebben er 195 producten in Discords eigen winkel (`/store/published-listings/skus`), 1.051 producten, mediaanprijs $3,99. Voorbeelden: Sudokudle (jul 2026, 294 servers) verkoopt thema's van $1,99, RIVALS FPS (mei 2026, 233 servers) gems tot $22,99, Naruto Ninja Cards kisten van $15,99. **Hoeveel er verkocht wordt is nergens zichtbaar.**
- **Launcher (vindbaarheid):** de openbare collecties (`application-directory-static/collections?surface=1` en `=2`) laten zien wat Discord in de Launcher zet: 18 collecties, ±75 plekken. Bijna allemaal titels van 2016 tot begin 2025 en van studio's: Smash Karts, Krunker, Poxel.io, Kour.io (webspellen die ook op Poki en CrazyGames staan), Farm Merge Valley, Wordle, Codenames, Roll20. Nieuwer dan mei 2025 zijn alleen Daily Word Wheel (sep 2025), Daily Word Griddle (apr 2026, 822 servers) en in "Promoted" The Rings of Power en EXOPLANET (okt 2026, merken). Een kleine nieuwe maker zie ik er niet tussen.

**Belangrijke beperking van de meting:** "servers" is het aantal servers waarin de app is toegevoegd. Een Activity kan ook gestart worden zonder dat iemand hem aan de server toevoegt, dus het echte aantal spelers ligt veel hoger. Death by AI meldde bijna 7 miljoen spelers (DERDEN, blog Discord 26 sep 2024) en staat op 23.500 servers: ruwweg 300 spelers per server. Passen we die verhouding toe (GOK, een uitschieter is geen goede maat), dan heeft de middelste nieuwe Activity ±1.500 spelers in totaal in 3 tot 6 maanden. Dat is nog steeds ver onder Poki (spellen van 3 tot 6 maanden mediaan 16.721 stemmen, zie voorstellen/poki.md). Let op: stemmen op Poki zijn geen spelers, het zijn twee verschillende maten; omdat lang niet elke speler stemt, is het verschil met Poki waarschijnlijk nog groter. Spelersaantallen per Activity zijn niet openbaar (de endpoints van de plank en `applications/public` vragen inloggen); alleen meetbaar als we zelf een Activity uitbrengen.

## Wat de onderzoeker vond (bronnen, 15 nov 2026)

- **Deel voor Discord:** 15% over de eerste $1M bruto per team, daarna 30%, sinds 6 juni 2024 (GEZIEN, discord.com/blog/feast-your-moniteyes-on-todays-exciting-developer-updates). Abonnementen per gebruiker of per server, eenmalige aankopen (blijvend of verbruikbaar), ook in Activities (GEZIEN, docs.discord.com/developers/platform/app-monetization).
- **Wie mag verkopen:** makers in de VS, de EU en het VK; EU sinds 19 okt 2023. Eisen: geverifieerde app, identiteitscheck van de teameigenaar, 18+, 2FA, eigen voorwaarden en privacybeleid, akkoord met de Monetization Terms, en de app moet slash-commando's hebben (of goedkeuring voor de Message Content intent), dus een Activity heeft minstens één slash-commando nodig. Uitbetaling via Stripe vanaf $100 na een beoordeling (GEZIEN, docs.discord.com, enabling-monetization). Of een particulier zonder KvK mag uitbetalen staat in het Payouts-artikel, dat achter Cloudflare zit (403, niet omzeild). Open punt.
- **Bewijs van geld:** alle grote succesverhalen komen van Discord zelf en gaan over studio's die vaak geholpen werden: Farm Merge Valley "zes cijfers in de eerste maand" (DERDEN, case study Discord 17 mrt 2025), Chef Showdown 14 miljoen spelers (DERDEN, Discord), Death by AI bijna 7 miljoen spelers (DERDEN, Discord). FRVR (Krunker) zegt zelf nog niet tevreden te zijn met de inkomsten. Het enige onafhankelijke kleine voorbeeld: Word Rummy van Stone Fruit Studio, ruim 2.000 spelers in de eerste maand en "een klein beetje omzet" (DERDEN, brittgibbons.substack.com, 24 mrt 2025). In mijn TrustMRR-gegevens van 8 nov (8.469 makers) staat geen enkele Activity.
- **Vindbaarheid:** in Directory en Launcher kom je na verificatie en een opt-in voor Discovery. Collecties en uitlichten kiest de redactie van Discord ("will reach out to you"); aanmelden kan niet (GEZIEN, docs.discord.com, discovery/overview). Er is geen winkel waar spelers door alle Activities bladeren; spelers komen vooral via vrienden, gedeelde links en het spraakgesprek (DERDEN).
- **Veranderingen:** sinds 26 sep 2024 open voor alle makers. 2025 en 2026: Discord richt zich vooral op grote spellen (Social Commerce op uitnodiging, Orbs en Quests als advertenties). Sinds 22 sep 2026 leeftijdscontrole en bestedingslimieten voor ouders. Discord diende in jan 2026 vertrouwelijk stukken in voor een beursgang (DERDEN).
- **Bouwen:** een Activity is een gewone webapp in een iframe via de proxy discordsays.com, met strenge CSP-regels; plus een kleine server die de OAuth-code inruilt voor een token. Phaser heeft een officiële handleiding. Alles kan vanaf Linux met npm (GEZIEN). Valkuilen: externe adressen moeten via de proxy-instellingen, oude versies blijven hardnekkig in de cache (GEZIEN, chipsoffury.com, 22 jan 2026). Een Activity kan geen microfoon gebruiken (GEZIEN, disdubs.com).

## Maatstaf

| | Uitkomst |
|---|---|
| Bereik | Zwak: mediaan 5 servers na 3 tot 6 maanden, 9% haalt 100+ (GEZIEN); spelers niet te meten, met een ruwe omrekening ±1.500 (GOK) |
| Geld | Voorwaarden goed (15%, EU, Stripe), 17% van de nieuwe Activities verkoopt iets, maar geen verkoop zichtbaar en geen kleine maker met een bedrag |
| Drukte | Hard stijgend: 325 nieuwe in okt 2026, ±8 keer begin 2025 |
| Vindbaarheid | Via vrienden en links; de Launcher is redactioneel en vol oude studiotitels |
| Past bij ons | Goed: webspel plus kleine tokenserver, vanaf Linux, dezelfde code als een Poki-spel |

## Voor en tegen

Voor:
- Grootste chatplatform voor gamers (meer dan 200 miljoen maandgebruikers, DERDEN), spellen spelen met vrienden in een gesprek is precies waar het voor is.
- Lage afdracht (15%) en eigen betalen in de app, ook in de EU.
- Technisch dichtbij wat we al doen voor Poki en Playables; een spel dat daar werkt is hier een kleine extra stap.
- Eén nieuwe maker (DisDubs) laat zien dat een slim idee dat alleen in een spraakgesprek werkt in 3 maanden bijna 10.000 servers kan halen.

Tegen:
- Middelste nieuwe Activity heeft bijna geen bereik, en het aanbod groeide in het laatste half jaar ruim 4 keer (71 in apr 2026, 325 in okt).
- De Launcher is een etalage van de redactie, met vooral oude titels van studio's.
- Geen onafhankelijk bewijs dat een kleine maker hier geld verdient.
- Publiek is jong; sinds sep 2026 leeftijdscontrole en limieten van ouders, dus voorzichtig met betalen.
- Uitbetalen zonder KvK is niet bevestigd.

## Eerste idee als we het ooit doen

Geen eigen product voor Discord, maar een **bijkanaal, uitdrukkelijk gekoppeld aan de Poki-proef** (de extra kosten zijn klein): als de Poki-proef een spel oplevert dat speelbaar is met meerdere mensen, zetten we het ook als Activity op Discord, met een kleine tokenserver en één cosmetische aankoop (thema's van $1,99 zoals Sudokudle). Een idee dat alleen in een spraakgesprek werkt (zoals DisDubs) heeft meer kans dan een gewoon webspel, maar daar hebben we nu niets voor.

## Wat het cijfer kan veranderen (herhaalmeting rond 15 feb 2027)

`python3 -I data/discord-activities-haal-script.py uit.json`, dan `data/discord-activities-analyse-script.py uit.json` en `data/discord-activities-sku-script.py uit.json 2026-11 sku.json`; collecties opnieuw met `curl https://discord.com/api/v9/application-directory-static/collections?surface=2`. Opnieuw wegen (naar 5 of 6) als:
1. de lichting nov 2026 t/m jan 2027 na 3 maanden een mediaan van 20+ servers haalt of 20%+ met 100+; of
2. er een kleine nieuwe maker in de Launcher-collecties staat; of
3. een kleine maker een openbaar bedrag noemt (bijvoorbeeld DisDubs of LoFi Pomodoro Sessions op TrustMRR of in een blog).

## Data en scripts

`data/discord-activities-haal-script.py`, `data/discord-activities-analyse-script.py`, `data/discord-activities-sku-script.py`; gegevens `data/discord-activities-directory-2026-11-15.json` (alle 20.117 apps, alleen velden die de directory openbaar toont), `data/discord-activities-sku-2026-11-15.json`, `data/discord-activities-launcher-collecties-2026-11-15.json`, uitvoer `data/discord-activities-analyse-uitvoer-2026-11-15.txt`.

## Controle

Op 15 nov 2026 (run 13:31) nagekeken door een controleur: akkoord met acht correcties, alle verwerkt. Hij rekende alle cijfers na uit de bestanden (alles klopt, kwartiel 20,5), keek DisDubs en 5 willekeurige Activities live na (servers precies gelijk, vlag bij alle zes aan) en las de blog van 6 juni 2024 en de docs over de EU na. Correcties: definitie telt ook bots met een loze Activity, doorbrekers zijn deels gewone bots, vergelijking met bots en met Poki is scheef (servers en stemmen zijn geen spelers), groei is ruim 4 keer in een half jaar en geen verdubbeling, selectie (alleen geverifieerde apps), eis van slash-commando's, bijkanaal koppelen aan Poki. Cijfer 4 en nee voor nu blijven.
