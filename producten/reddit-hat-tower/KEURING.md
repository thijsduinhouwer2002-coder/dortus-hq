# Keuring Gloop's Hat Tower op Reddit fase 1, do 19 nov 2026, keurder (agent van de hoofdchat)
Wat ik keurde: commit a542cc35, `producten/reddit-hat-tower/` (ontwerp.md, stand.md, app/, beelden/). Lokaal gespeeld in een kopie in /tmp (npm ci, `npm test`, `PROEF=1 npm run local`), met Playwright op 390x780 (3x, aanraken), 1280x760, 1280x560, 1024x600, de post in de feed op 390x512 en 740x512, en liggend 844x390. Regels zelf gelezen met curl op 19 nov: redditgameofday2026.devpost.com (overzicht en /rules) en developers.reddit.com/docs/devvit_rules en /docs/capabilities/server/userActions.
Akkoord: nee (twee moet-punten, allebei klein: samen GOK een halve dag werk)

## Kort oordeel
Het ziet er eigen en warm uit, de eerste 10 seconden zijn goed: een groen slijmpje met een hoedentoren in een grot, een dikke knop, "Tower #1: Classic" en een teller van de subreddit. Het eindmoment (camera trekt terug tot je hele toren, dan het uitslagvel) is het sterkste beeld. Maar de kern van een dagspel met ranglijst klopt nog niet: **blind elke ±0,27 s tikken levert evenveel hoeden op als goed mikken**, en **wie halverwege de dagbeurt herlaadt, mag hem opnieuw spelen**. Beide maken de ranglijst zinloos, en "fair, well-calibrated" staat letterlijk in wat Reddit zoekt.

## Wat ik zag (skill kijken; beelden in /tmp, na afloop opgeruimd, de beelden van de bouwer in `beelden/` laten hetzelfde zien)
- **Post in de feed (390x512 en 740x512):** titel, dag, "110 hats stacked in r/... today", knop, Gloop met toren. Leest in één oogopslag. Op de telefoon breekt "Play today's tower" over twee regels en valt de klep van de pet rechts buiten beeld.
- **Startscherm:** duidelijk (regel van de dag, gouden helden "#4 and #20", één zin uitleg onderaan). Op de telefoon is het midden van het scherm leeg tussen de knoppen en Gloop.
- **Spelen:** de bovenste ±60% van een telefoonscherm is de hele ronde lege grot; alles gebeurt onderin. "GULP!", "x2", "+3 hats", de vliegende helm en de vonken werken. Het slokbeeld (held in de mond) heeft zichtbare trapjes en een harde zwarte pixelrand; naast de zachte render van Gloop valt dat op als ander, goedkoper werk (`beelden/2-gouden-gulp.png` laat het ook zien). Hoeden zijn op 3x iets zacht. Een gouden held telt 3 maar geeft 1 hoed op de toren: teller en toren lopen uit elkaar (8 tegen 6 zichtbaar).
- **Uitslag:** sterk. Groot getal, plek, reeks, vakjes, "Comment my result", gezamenlijke toren, ranglijst, Practice en Back. Geen uitleg wat groen, oranje en zwart betekenen. Op het blije gezicht aan het eind leest de dikke oogboog klein als een vreemd teken.
- **Desktop:** strook in het midden, zijkanten vlak donker; netjes. Bij 560 hoog raakt de teller van de subreddit net de toren.
- **Liggend (844x390):** kapot: de uitleg staat over de knop "Play tower #1", "Warm up first" valt half weg, Gloop is niet te zien.
- Geen fouten of waarschuwingen in de console (GEZIEN, 2 x 3 rondes plus de feed).

## Deel A: doet het wat beloofd is?
(toets tegen `ontwerp.md` "Af voor fase 1", de tabel "Wat het Reddity en dagelijks maakt" en de opdracht)

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | `npm test` groen: tsc, biome, 12 unit-toetsen, bouw (GEZIEN, eigen run na `npm ci`). | Feit | hoog | |
| A2 | **Blind tikken is even goed als mikken.** Server-naspelen (`speelNa`) met een tik elke 63 tot 67 stappen (252 tot 268 ms), dag 1 tot 10: 16 tot 25 hoeden. De eigen proefspeler "gemiddeld" (mikt op 810, spreiding 45, 12% te laat): 18 tot 23. Op 6 van de 10 dagen haalt blind tikken evenveel of meer (dag 9: 25 tegen 21; dag 2: 22 tegen 22; dag 10: 24 tegen 22). In Playwright: spam 19, gemikt 19 en 20 (GEZIEN). Het ontwerp zegt "je vangt dan veel, maar bijna nooit een voltreffer, dus geen reeks": dat klopt, maar de ranglijst telt eerst hoeden, dus de reeks beslist alleen bij gelijkspel. | Feit | hoog | Na een aanpassing dezelfde vergelijking draaien: een gemikte speler (spreiding 45) moet op alle vijf regels duidelijk boven het beste tikritme uitkomen (voorstel: 25% of meer). |
| A3 | **"De eerste ronde van de dag telt" klopt niet.** De score gaat pas aan het eind naar de server. Dagbeurt gestart, 5 keer getikt, pagina herladen: de knop "Play tower #1" staat er weer (GEZIEN, Playwright). Zo kun je de dagtoren onbeperkt oefenen en alleen een goede ronde insturen. | Feit | hoog | Na een start-moment op de server: herladen midden in de ronde moet de dagbeurt als gebruikt tonen. |
| A4 | De server speelt het potje na uit alleen de tikken; volgorde van tikken en stappen is in browser en server gelijk (`drukNu` rekent eerst bij, dan `druk`; `speelNa` drukt vóór `stap`). Onzin-invoer (niet oplopend, buiten bereik, meer dan 2000) wordt geweigerd. De uitslag die de server terugstuurt kwam in de Playwright-ronde overeen met wat het scherm liet zien. | Feit | hoog | |
| A5 | Wat de servercontrole niet tegenhoudt: het spel is per dag vast en de code staat in de browser, dus een script kan de perfecte tikken uitrekenen. Voor een wedstrijd van een paar weken geen probleem. | Vermoeden | midden | Pas belangrijk als er echte spelers zijn. |
| A6 | Dagcode: dag 1 = 19 nov 2026 UTC, regel per dag uit vijf (elke vijf dagen allemaal, volgorde per week gehusseld), gouden helden 4 tot 23, hoedvolgorde per dag, wachttijd per held uit dagzaad. Toets "held n wacht voor iedereen even lang" groen. | Feit | hoog | |
| A7 | Redis-sleutels per subreddit en dag (`rang:`, `uitslag:`, `hoeden:`, `spelers:`) met 40 dagen bewaartijd; `reeks:`, `beste:`, `naam:` per speler zonder bewaartijd (klein). `zRange` met `reverse: true` en de plek uit `zRank`/`zCard` passen bij `@devvit/redis` (types gecontroleerd). | Feit | hoog | |
| A8 | "Al gespeeld?" is lezen en daarna schrijven, niet in één stap. Twee gelijktijdige inzendingen (dubbeltik op traag net) tellen allebei mee in de gezamenlijke toren en het aantal spelers. | Feit (code) | midden | Toets met twee gelijktijdige `score`-aanroepen. Oplossen samen met A3 (één sleutel die maar één keer gezet kan worden). |
| A9 | Dagtaak in `devvit.json` (`0 0 * * *`, endpoint `/internal/scheduler/daily-post`) en menu (standaard alleen moderators) kloppen met het schema in `@devvit/shared-types` (GEZIEN). Niet op Reddit getest; staat eerlijk in stand.md. | Feit | hoog | `npm run playtest` na de login. |
| A10 | Het spel gebruikt altijd de dag van vandaag, niet die van de post. Een post "Gloop's Hat Tower #5: Rush Hour" speelt op dag 9 toren #9. De jury opent de demopost dagen na het maken. | Feit (code) | hoog | De dag per post bewaren (postData of Redis per postId), of de titel niet aan een dag binden. |
| A11 | De uitslag als reactie: `kaartTekst` scheidt regels met één `\n`. In Reddit-markdown wordt één regelovergang meestal één regel, dus de vakjes en "16 hats" lopen in de reactie aan elkaar. | Vermoeden | midden | Eén reactie plaatsen in playtest. Oplossing: `\n\n` of twee spaties aan het eind van elke regel (alleen voor de reactie, Copy mag zo blijven). |
| A12 | Ronde precies 30 s, eerste hoed binnen 2,5 s, goede speler 15+, missen kost niets: toetsen groen en in het spel gezien (proefspeler goed: 20 tot 26). | Feit | hoog | |
| A13 | Eerlijk in stand.md: de proefspelers heten `practice_bot_*` en staan alleen lokaal op de ranglijst (`PROEF=1`). | Feit | hoog | |

## Deel B: houdt het zich aan onze regels en die van Reddit?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Geen link naar buiten, geen verwijzing naar Garmin of Steam in het spel of de README; `fetch` alleen naar eigen `/api/...`; letters en plaatjes in `public/`. Toets "uitslagkaart zonder garmin/steam/http" groen. | Feit | hoog | Devvit: "Apps should not link out to other apps, or promote other versions of the app on external platforms" |
| B2 | Reactie namens de speler alleen na een tik op "Comment my result", los van de rest, niet verplicht. Reddit vraagt ook "inform users before ... commenting on their behalf": de knop zegt het, maar de tekst die geplaatst wordt zie je vooraf niet. | Feit | midden | Devvit user actions |
| B3 | Eigen IP en echt een port: Gloop staat al sinds 9 nov in Hats (`producten/steam-hol`, eerste commit 11533861), Hat Tower op Garmin is goedgekeurd en live (bord: APPROVED 17 nov). Spelregels en getallen uit `Spel.mc`, plaatjes uit de kit van Mila (renders van Dortus, geen beeld van derden). Ontwerp.md zegt dat helder ("eigen IP van Dortus"). De README zegt het niet, en dat is goed zo (Devvit-regel B1); het hoort in de Devpost-tekst ("Make sure to note your game is a port"). | Feit | hoog | wedstrijd: "you must own the original app/IP" |
| B4 | `app/LICENSE` is de BSD-licentie van de template: "Copyright (c) 2025 Reddit Inc.". Voor een inzending op eigen IP verwarrend; nergens staat dat Gloop, de held en de hoeden van Dortus zijn. De letters (OFL) staan in `public/fonts/` zonder hun licentietekst, die OFL meegeven verplicht. | Feit | hoog | rechten, OFL |
| B5 | Devvit-README-eis: "who it is for" en "how to configure, deploy, and interact with the app's full feature set". De README legt spel en dagdeel goed uit, maar niet wat een moderator doet (installeren, de dagpost om 00:00 UTC, het menu "new daily post"). | Feit | midden | devvit_rules, App README requirements |
| B6 | Geen AI-melding in spel, README of teksten (GEZIEN, grep). Wel: commentaar in `src/shared/spel.ts` regel 1 noemt de tak `claude/garmin-gloop-11`. En de repo dortus-hq zegt bovenaan dat een ploeg Claudes alles bouwt. De wedstrijd: "it shouldn't be obvious the moment we open your app". | Feit | hoog | besluit 19 nov 01:30, wedstrijdpagina "AI Slop" |
| B7 | Bestanden boven ±400 regels: `teken.ts` 443, `stijl.css` 450, `game.ts` 403. | Feit | hoog | `organisatie/regels/bouwen.md` |
| B8 | Er is geen `producten/reddit-hat-tower/architectuur.md`; de opbouw staat wel kort in ontwerp.md en de README. | Feit | hoog | keurformulier, regels bouwen |
| B9 | Cijfers in ontwerp en stand hebben GEZIEN of GOK; geen persoonsgegevens (`check.py`: "Controle openbare repo: OK"). Tests niet aangepast om te slagen (toetsen lezen als echte eisen). | Feit | hoog | harde regels 2 en 5 |
| B10 | Geen taalmodel in de app, geen verzoeken naar buiten, geen betalingen: geen extra goedkeuring van Reddit nodig behalve mogelijk voor de reactie namens de speler. | Feit | midden | devvit_rules |

## Moet (blokkeert akkoord)
1. **Mikken moet duidelijk meer opleveren dan blind tikken (A2).** Bijvoorbeeld: een voltreffer geeft een extra hoed, of elke 3 voltreffers op rij een bonushoed, of de ranglijst telt hoeden plus voltreffers. Toets toevoegen: gemikte speler (spreiding 45) haalt op alle vijf dagregels minstens 25% meer dan het beste vaste tikritme (200 tot 400 ms). Daarna de dagregels opnieuw naspelen.
2. **De dagbeurt telt vanaf de start (A3, A8).** Bij "Play tower #N" een `/api/start` die één sleutel per speler per dag zet (zet-als-nog-niet-bestaat); wie opnieuw start of herlaadt zonder uitslag, krijgt die dagbeurt als gebruikt (0 of de stand bij vertrek) en speelt verder als oefening. Toets: twee keer starten, de tweede telt niet; twee gelijktijdige inzendingen tellen één keer.

## Kan (mag later, in volgorde van punten per moeite)
1. Reactie-opmaak (A11) met `\n\n`, en vóór het plaatsen de tekst laten zien ("This posts as u/naam: ...") (B2).
2. Einde: knop "Join r/... for tomorrow's tower" (user action `SUBSCRIBE_TO_SUBREDDIT`; Reddit noemt "a subreddit subscription prompt" letterlijk bij goede eindschermen). Vakjes kort uitleggen (groen perfect, oranje gulp, zwart miss).
3. Demo-subreddit heeft minder dan 200 leden, dus de jury ziet een lege ranglijst en "Be the first ...". Laat ook de toren van alle dagen zien (`hoedenOoit` staat al in Redis maar wordt nergens getoond) en de top van gisteren.
4. Gezamenlijke toren als beeld (bijvoorbeeld een hoed per 10 of 100 hoeden), in de lege bovenkant van het speelscherm: lost ook het lege scherm op.
5. Dag per post bewaren (A10).
6. Slokbeeld en hoeden scherper uit de renders van 400 px (`ontwerp/garmin/gloop-spel/bron-renders/`), zonder de harde pixelrand van het horloge.
7. Liggend en lage schermen: startscherm laten schuiven of kleiner maken.
8. LICENSE en README: "Gloop, the heroes and the hats © Dortus", OFL-teksten bij de letters, een stuk voor moderators (B4, B5).
9. `claude/` uit het commentaar in `spel.ts`; in de Devpost-inzending niet naar de repo dortus-hq linken (code openbaar is optioneel) (B6).
10. Devvit Journeys aanzetten (`"journeys": true`, Reddit noemt het als pluspunt) voor dagen op rij en de ranglijst.
11. `teken.ts`, `stijl.css`, `game.ts` onder 400 regels; `architectuur.md` maken (B7, B8).
12. Ronde die over middernacht UTC loopt gaat verloren (409, "this tower is from another day"); de dag van de start laten gelden.

## Tegen de vier jurypunten (stand nu, lokaal; GOK, mijn oordeel)
| Punt | Cijfer | Waarom |
|---|---|---|
| Delightful UX | 6 | Eigen, warm en meteen te snappen; één tik; de terugtrekkende camera met de hele toren is een echt moment. Min: tweederde van het telefoonscherm is leeg tijdens het spel, blind tikken voelt even goed als mikken, geen uitleg bij de vakjes. |
| Polish | 6 | Geen fouten, eerlijke score, toetsen, eigen letters en knoppen, geen standaard-UI. Min: pixelig slokbeeld naast zachte renders, liggend kapot, knoptekst breekt in de feed. Nog niet op Reddit gedraaid; zonder werkende demopost is dit punt GOK 2 of 3. |
| Reddity | 5 | Ranglijst per subreddit, gezamenlijke toren, uitslag als reactie, dagpost. Min: in een kleine test-subreddit ziet de jury vooral leegte; de gezamenlijke toren is alleen een getal; geen abonneerknop of flair. |
| Daily Content | 7 | Zelfde toren voor iedereen, vijf rouleren de regels, gouden helden vooraf genoemd, dagen op rij, dagpost vanzelf. Min: de regels zijn vooral snelheidsknoppen, en post en dag lopen uit elkaar. |

## De 3 dingen met de meeste punten voor de minste moeite
1. **Moet 1 en 2 (mikken loont, één dagbeurt):** een paar uur, tilt UX, Polish en Daily, en maakt de ranglijst echt.
2. **Eindscherm voor Reddit:** reactie-opmaak met voorbeeld, abonneerknop, uitleg van de vakjes, en `hoedenOoit` plus de top van gisteren tonen zodat een lege demo-subreddit niet leeg oogt. Halve dag, vooral Reddity.
3. **De gezamenlijke toren als beeld bovenin het speelscherm:** vult de lege grot en maakt de grap van de subreddit zichtbaar in elke ronde en op de post in de feed. Een dag, het grootste stuk Reddity en UX.

Daarnaast, geen werk van de bouwer maar het grootste risico: de login van Thijs (uiterlijk ma 23 nov) zodat het spel ruim op tijd op Reddit draait. Zonder demopost scoort het op alle vier laag.

## Eigen IP in README en ontwerp (vraag 4)
Ja, een echte port van eigen werk (B3). Ontwerp.md zegt het goed. De README zegt het bewust niet (Devvit-regel); zet in de Devpost-tekst: port van ons eigen horlogespel Gloop's Hat Tower, figuur Gloop uit ons spel Hats, en wat er nieuw is voor Reddit (dagtoren, dagregel, gouden helden, ranglijst, gezamenlijke toren).
