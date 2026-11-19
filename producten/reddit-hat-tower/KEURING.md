# Herkeuring filmpje, do 19 nov 2026, keurder (agent van de hoofdchat)
Wat ik keurde: commit 3fddb918. Filmpje `beelden/inzendfilmpje-1080x1920.mp4` (33,8 s, 1080x1920, 30 beelden per seconde, AAC; GEZIEN met ffprobe): blad van de eerste 10 s (2 per seconde), van 10,5 tot 18,5 s (4 per seconde), de knip beeld voor beeld, het hele filmpje (1 per seconde), uitsnede op ware grootte, geluid met ffmpeg. Spel: `npm test` en een dagbeurt op 390x780 met 10 beelden van het eindmoment. Beelden in /tmp, na afloop opgeruimd.
Akkoord: ja voor het spel. Ja voor het filmpje als concept, tot de opname op Reddit (moet 4 van de keuring fase 2b blijft staan).

## Moet-punten 1 tot 3 voor het filmpje
| # | Wat ik zag | Uitslag | Zekerheid |
|---|---|---|---|
| 1 | **Begint in de actie.** Beeld 1 is al de grot met een vallende held; titel "Gloop's Hat Tower / a daily game on Reddit" van 0 tot ±2,4 s; eerste "PERFECT! +2 hats" op ±1,5 tot 2 s; startklank op 0 s (stilte daarna van 0,17 tot 1,66 s, tot de eerste slok). Een jury ziet in de eerste 10 s: titel, drie keer PERFECT met oplopende reeks, "One tap. 30 seconds.", "Perfect gulps stack more hats", een gouden held (+6) en een toren van 15 hoeden. Dat haakt. Klein: de held vliegt bij 0,5 s even over de "G" van de titel. | opgelost | hoog |
| 2 | **Geen proefnamen.** Overal "r/GloopsHatTower"; geen ranglijst, geen `practice_bot`, geen `u/film...`. Het voorbeeld zegt nu "Posts as a comment from your account, under this post". Wel nog: "129 hats today" aan het begin en "Place 1 of 6 today" komen van de lokale proefspelers; dat is geen naam die raar oogt, maar ook geen echte stand. In de opname op Reddit wordt het vanzelf echt. | opgelost | hoog |
| 3 | **Echt scherp.** Uitsnede op ware grootte (Gloop met slijmbelletjes en vonken, de tekst PERFECT): scherpe randen, geen jpeg-blokjes meer. | opgelost | hoog |

## De knip (±12,0 s)
Eén harde knip: in één beeld springt de teller van 19 naar 31 en wordt de tijdbalk korter; de rest van het beeld (toren, camera, gezamenlijke toren, "129 hats today") blijft bijna gelijk, en de tekst "Same tower for everyone today" komt pas ±0,3 s later. Omdat alleen het getal verspringt, kan het lezen als een sprong in het spel in plaats van een montage. Geen fout die een jury afschrikt, maar makkelijk netter: laat de nieuwe tekst precies op de knip verschijnen, of zet er een korte overgang op (4 tot 6 beelden overvloeien of een witte flits). Kan, geen moet.

## De drie spelpunten
| # | Wat ik toetste | Uitslag | Zekerheid |
|---|---|---|---|
| 1 | **Mijlpaal links.** "r/GloopsHatTower passed 150 hats today!" staat links in het lege deel, niet meer over je toren (GEZIEN, filmpje en eigen ronde). | in orde | hoog |
| 2 | **Overvliegen groter.** Je hoeden vliegen in een grote boog naar de gezamenlijke toren, met "+53 hats" erbij, en het bordje springt van 129 naar 182 (GEZIEN). Nu goed te zien, ook in het filmpje (+56 hats). | in orde | hoog |
| 3 | **Pauzeren telt niet als te laat.** De browser telt de tijd dat het tabblad verborgen is (`visibilitychange`) en stuurt die mee; de server trekt hem af, hoogstens 10 minuten. Toets groen (5 minuten pauze gaat goed, een uur niet). `npm test`: 22 toetsen groen. Kanttekening: de pauze komt van de browser, dus met een zelfgemaakt verzoek kun je tot ±11,5 minuten na de start insturen; dat vraagt een script en levert niets op wat het naspelen niet al tegenhoudt. | in orde | hoog |
| 4 | Geen fouten of waarschuwingen in de console. | in orde | hoog |

## Kan
1. De knip netter (zie boven).
2. Eindigen met een korte oproep, bijvoorbeeld "New tower every day on r/GloopsHatTower", nu eindigt het op het uitslagvel.
3. Bij de opname op Reddit (moet 4 van fase 2b): post in de feed, tik, groot spel, en de reactie onder de post; dan zijn ook de getallen echt.

---

# Keuring fase 2b, do 19 nov 2026, keurder (agent van de hoofdchat)
Wat ik keurde: commit bd77639f. Lokaal gespeeld in een kopie in /tmp (npm ci, `npm test`, `PROEF=1 npm run local`), Playwright op 390x780 (2x, aanraken) en 1280x760, een dagbeurt per maat met daarna 22 beelden van het eindmoment (elke 0,3 s). Inzendfilmpje `beelden/inzendfilmpje-1080x1920.mp4` bekeken als blad van de eerste 10 s (2 per seconde) en van het hele filmpje (1 per seconde), losse beelden op ware grootte, en het geluid gemeten met ffmpeg. Beelden in /tmp, na afloop opgeruimd.
Akkoord: ja voor het spel. Nee voor het inzendfilmpje: dat is nog een concept (vier moet-punten hieronder, vóór de inzending).

## Nieuwe punten van 2b
| # | Wat ik toetste | Uitslag | Feit of vermoeden | Zekerheid |
|---|---|---|---|---|
| 1 | `npm test`: types, lint, 21 toetsen, bouw. | groen | Feit | hoog |
| 2 | **Tijdregel.** Insturen kan alleen tussen 27 s en 90 s na `api/start` (starttijd in de sleutel, klok van de server). Toets: na 5 s "too early", na 91 s "too late" (telt dan als afgebroken, 0 hoeden, geen nieuwe beurt), na 89 s goed. In het echt kwam de uitslag 31,2 s na de start binnen en werd bewaard (GEZIEN, telefoon en desktop). Daarmee is ook N2 van de herkeuring dicht: een afgebroken beurt van gisteren kun je niet later nog insturen. | in orde | Feit | hoog |
| 3 | Wat de tijdregel kost: het spel pauzeert als het tabblad of de app op de achtergrond gaat (geen beelden, inhalen begrensd op 250 ms). Wie midden in de dagbeurt een minuut wegswipet, krijgt "sent too late" en 0. Streng maar eerlijk; zo zeldzaam dat het mag. | kan later | Feit (code) | midden |
| 4 | **Elke post speelt zijn eigen dag.** Dag bij het maken van de post in Redis (`post:<id>`), bij openen gelezen; een post zonder dag of uit de toekomst speelt vandaag. Dagen op rij tellen alleen met de toren van vandaag of gisteren. Op een oude post: "This is tower #N from <datum>. Today's tower #M is in the newest post." Toets groen; lokaal kon ik het niet spelen (vandaag is dag 1). | in orde | Feit (toets en code) | hoog |
| 5 | **Eindmoment.** Bij 47 en 62 hoeden zoomt de camera niet verder uit dan de helft en zakt hij van de top naar Gloop; de toren blijft een toren, geen streep (GEZIEN). Daarna "r/GloopTowerTest passed 150 hats today!" en het uitslagvel. Klein: de mijlpaaltekst staat over je eigen toren heen (leesbaar door de rand). Het overvliegen van je hoeden naar de gezamenlijke toren gebeurt klein rechtsboven; op de telefoon en in het filmpje zie je het nauwelijks. | in orde | Feit | hoog |
| 6 | Voorbeeld van de reactie: gulp is nu een oranje vakje, gelijk aan het spel. | in orde | Feit | hoog |
| 7 | Geen fouten of waarschuwingen in de console. | in orde | Feit | hoog |

## Het inzendfilmpje, als jury in de eerste 10 seconden
43,9 s, 1080x1920, 30 beelden per seconde, AAC stereo (GEZIEN met ffprobe). De teksten kloppen met het spel en zijn goed: "One tap. 30 seconds.", "Perfect gulps stack more hats", "Same tower for everyone today", "Every subreddit builds one tower", "Share your run. New tower tomorrow." Van 10 tot 35 s groeit de toren mooi door, met "PERFECT! +4 hats, streak 8" tot streak 17, en het eind laat het uitslagvel met Post as comment en Join zien. Maar:
- **Haakt niet in de eerste seconden.** 0 tot 3 s is een stilstaand startscherm (zes keer hetzelfde beeld), en 0 tot 4,8 s is stil (silencedetect bij -40 dB). Het eerste wat beweegt komt na ±3,5 s, de eerste "PERFECT!" na ±5 s. Een jury die 10 s kijkt, ziet vooral een menu.
- **Proefnamen in beeld.** "r/GloopTowerTest" staat het hele filmpje rechtsboven en in de mijlpaal, en op het uitslagvel staan "u/film88760" en vier keer "u/practice_bot_..." op de ranglijst. Dat ogen als nep en als test.
- **Niet echt scherp.** Op ware grootte zijn de randen zacht en zijn er blokjes van jpeg te zien, ook op Gloop en de tekst (GEZIEN, uitsnede op 1080). Vermoeden: het screencast van Chrome levert beelden op 360x640 die naar 1080x1920 zijn opgeschaald (`dev/film.py`: viewport 360x640, schalen met lanczos). Mijn eigen schermbeelden op 3x zijn duidelijk scherper.
- **Niet op Reddit.** De wedstrijd vraagt "footage that shows the Project functioning on the device for which it was built". Nu is het alleen het spel, zonder post, feed of reacties eromheen. Kan pas na de login.
- Van 12 tot 30 s lijken de beelden erg op elkaar; 30 tot 35 s is genoeg.
- Geluid: gemiddeld -31 dB, piek -3,3 dB, alleen klanken met gaten van 1 tot 2 s ertussen; geen muziek. Mag, maar de stilte aan het begin valt op.

## Moet (blokkeert akkoord op het filmpje, niet op het spel)
1. **Begin met de actie.** Binnen de eerste seconde beweging: bijvoorbeeld de hoge toren met "PERFECT! streak 12" en een titel "Gloop's Hat Tower, a daily game on Reddit", daarna pas een korte start. Geen stil begin.
2. **Geen proefnamen.** Opnemen in de echte demo-subreddit met zijn echte naam en zonder `practice_bot_...` en `u/film...` op de ranglijst (lege ranglijst, of echte spelers die het weten, of de ranglijst niet in beeld).
3. **Echt scherp.** Beeld voor beeld op 3x vastleggen (zoals de schermbeelden) of het screencast op 1080 breed laten leveren; daarna nog eens op ware grootte bekijken.
4. **Opnemen op Reddit**, in de post (feed, tik, groot spel, reactie eronder), na de login en de playtest.

## Kan
1. Mijlpaaltekst niet over je eigen toren; het overvliegen naar de gezamenlijke toren groter of dichterbij, zodat de jury het ziet.
2. Filmpje inkorten tot ±30 tot 35 s.
3. "Posts as u/... under today's post" wordt op een oude post "under this post".
4. Achtergrond (punt 3 in de tabel): bij terugkomen binnen de tijd gewoon doorspelen, daarna pas te laat.

## Jurypunten (stand nu, lokaal; GOK)
Delightful UX 8 (eindmoment is terug), Polish 7 (niets op Reddit getest; met het filmpje zoals het nu is eerder lager), Reddity 7, Daily Content 8 (elke post speelt zijn eigen toren, met een verwijzing naar die van vandaag).

---

# Herkeuring Gloop's Hat Tower op Reddit fase 2a, do 19 nov 2026, keurder (agent van de hoofdchat)
Wat ik keurde: commit 8ad9273f (fase 2a), dezelfde map. Opnieuw lokaal gespeeld in een kopie in /tmp (npm ci, `npm test`, `PROEF=1 npm run local`), met Playwright op 390x780 (3x, aanraken), 1280x760, 1280x560, liggend 844x390 en de post in de feed op 390x512 en 740x512. Filmpje `beelden/filmpje-ronde-telefoon.mp4` bekeken als blad van 33 beelden (1 per seconde). Beelden in /tmp, na afloop opgeruimd; de beelden van de bouwer in `beelden/` laten hetzelfde zien.
Akkoord: ja (beide moet-punten opgelost en zelf nagerekend; nog wel de keuring van Iris op plezier en beeld, en niemand heeft het als mens gespeeld)

## De moet-punten van de eerste keuring
| # | Wat ik toetste | Uitslag | Feit of vermoeden | Zekerheid |
|---|---|---|---|---|
| M1 | **Mikken loont.** Zelf nagerekend met `speelNa`, dag 1 tot 10, 40 spelers per soort. Blind tikken met een vast ritme (160 tot 480 ms, 4 fasen): middelste uitslag 13 tot 20 hoeden, hoogste 23 tot 28 (dat hoogste kies je alleen achteraf). Blind met menselijke spreiding in het ritme: middelste 13 tot 19, hoogste 18 tot 25. Gemikt (spreiding 45, 12% te laat): middelste 33 tot 45. Slordig gemikt (spreiding 70, 25% te laat): middelste 16 tot 20, dus ongeveer gelijk aan blind. Mikken levert nu ruim het dubbele op; de nieuwe toets ("25% boven het beste vaste ritme", dag 1 tot 5) is groen en is streng genoeg, want hij vergelijkt met het beste ritme achteraf. | opgelost | Feit (GEZIEN) | hoog |
| M2 | **Eén dagbeurt.** Dagbeurt gestart, 4 keer getikt, herladen: de knop "Play tower #1" is weg, er staat "Your run for tower #1 was started and not finished, so it counts as 0. Tower #2 comes tomorrow." en alleen Practice (GEZIEN op telefoon en desktop). Server: insturen kan alleen na `api/start`, de uitslag wordt eerst geclaimd met zet-als-nieuw; toetsen voor herladen, dubbele inzending en middernacht groen. | opgelost | Feit | hoog |
| M2b | De claim gebruikt `redis.set(key, value, {nx: true}) === 'OK'`. De bouwer noemt dat GOK. In `@devvit/redis` 0.15.4 zelf (`test/mocks/RedisMock.js`) geeft Set het antwoord van Redis terug: "OK" als hij zette, anders een lege tekst; Devvit's eigen `cache/PromiseCache.js` leunt er op dezelfde manier op. Dus waarschijnlijk goed. Gaat het mis, dan krijgt elke speler "you already played today" en wordt niets bewaard: in playtest als eerste testen. | waarschijnlijk goed | Vermoeden, met bron in het pakket | midden |

## Wat ik zag (skill kijken)
- **Plaatjes:** scherp, ook ingezoomd op 3x. De trapjes en de zwarte pixelrand van het slokbeeld zijn weg. Gloop, held en hoeden komen nu allemaal uit dezelfde 3D-modellen en passen bij elkaar.
- **Animatie:** echt beter. Strook van zes beelden rond een slok: "PERFECT! +3 hats, streak 2", Gloop zakt in met slijmbelletjes, knippert, de held tuimelt ondersteboven met de hoed op, het gele "!" bij de bek, bij een misser hupt de held weg met "bye!" en kijkt Gloop met een dichtgeknepen oog. In het filmpje groeit de toren de hele ronde door tot boven het scherm uit; dat is de grap van het spel en die komt nu over.
- **Gezamenlijke toren:** rechts achterin, doffer, met het bordje "r/GloopTowerTest 131 hats today". Vult de lege grot. Op de telefoon staat hij half buiten de rechterrand en zweeft net boven de grond; op het startscherm raakt hij de tekst "together." en de uitleg.
- **Eindscherm:** uitleg van de vakjes, voorbeeld van de reactie ("Posts as u/... under today's post"), "Post as comment", Copy, "Join r/...", "Since tower #1: 290 hats", vandaag en gisteren. Reactie in het log van de server heeft witregels (GEZIEN). Klein: in het voorbeeld is een gewone gulp een geel vakje, in het spel en de uitleg oranje.
- **Eindbeeld bij hoge score:** bij 50 hoeden trekt de camera zo ver terug dat de toren een dunne streep wordt en Gloop een stipje (GEZIEN op desktop). Nu de scores door de reeksen hoger worden (30 tot 50), verliest het sterkste moment zijn kracht.
- **Liggend (844x390):** opgelost, knoppen naast elkaar, alles leesbaar. **Feed:** knoptekst op één regel, pet binnen beeld.
- **Filmpje:** 32,5 s, 390x780 op 1x, een hele ronde plus het uitslagvel. Goed om te kijken, geen inzendfilmpje: voor YouTube te klein (minstens 1080x1920 nodig) en zonder geluid.
- Geen fouten of waarschuwingen in de console (GEZIEN).
- Let op bij mijn eigen meting: op de telefoonmaat haalde mijn Playwright-speler gemikt maar 17 tegen 21 blind, op desktop 50 gemikt. Dat komt door de vertraging van de aanraak-tik in Playwright op 3x (veel late gulps), niet door het spel; de berekening in M1 is het bewijs.

## Nieuwe bevindingen
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel of bron |
|---|---|---|---|---|
| N1 | Nog open (A10): een post speelt de toren van vandaag, niet die uit de titel. Staat eerlijk in stand.md. | Feit | hoog | |
| N2 | `score` aanvaardt ook gisteren als er een start van gisteren is. Wie gisteren startte en afbrak, kan vandaag met een zelfgemaakt verzoek alsnog insturen. Kan alleen met een script. Goedkope rem: insturen alleen binnen bijvoorbeeld 60 s na de start (de starttijd staat al in de sleutel). | Feit (code) | midden | |
| N3 | Bestanden onder 400 regels (hoogste `stijl.css` 351), `architectuur.md` is er, LICENSE zegt nu "Copyright (c) 2026 Dortus" met Gloop, helden, hoeden en plaatjes van Dortus, OFL-teksten bij de letters, README met een stuk voor moderators. Geen `claude`, geen link naar buiten, geen Garmin of Steam in spel of README (grep). | Feit | hoog | B4 tot B8 van de eerste keuring |
| N4 | De plaatjes komen uit `producten/steam-hol/modellen` (eigen modellen van Hats, `kunst/render.sh`): eigen IP, en de port blijft echt. | Feit | hoog | wedstrijd: eigen IP |
| N5 | Niet getest, kan pas na de login: Redis met nx (M2b), `submitComment` en `subscribeToCurrentSubreddit` namens de speler, de dagtaak, uitgelogd spelen. | Feit | hoog | |

## Moet (blokkeert akkoord)
Geen.

## Kan (volgorde: punten per moeite)
1. Eindbeeld bij hoge torens: niet verder uitzoomen dan een vaste grens; laat de camera van de top van de toren naar Gloop zakken, of laat de toren boven het vel uit lopen met het getal ernaast.
2. Dag per post bewaren (N1).
3. Insturen alleen kort na de start (N2).
4. Gezamenlijke toren op de telefoon helemaal in beeld en op de grond; op het startscherm niet achter de tekst.
5. Gulp-vakje in het voorbeeld van de reactie dezelfde kleur als in het spel (of de uitleg aanpassen).
6. Inzendfilmpje: 1080x1920, onder 1 minuut, met geluid, eindigend op de toren en het uitslagvel.

## Tegen de vier jurypunten (stand nu, lokaal; GOK, mijn oordeel)
| Punt | Eerst | Nu | Waarom |
|---|---|---|---|
| Delightful UX | 6 | 8 | Scherpe, samenhangende plaatjes, echte animatie (Gloop reageert, held tuimelt en hupt weg), mikken voelt nu de moeite waard met "PERFECT! streak". Min: het eindbeeld wordt bij hoge scores een streep; nog niet door een mens gespeeld. |
| Polish | 6 | 7 | Geen fouten, liggend en feed in orde, LICENSE, OFL, README voor moderators, eerlijke start en score met toetsen. Min: niets is op Reddit getest (Redis nx, reactie, lid worden, dagtaak); zonder werkende demopost blijft dit GOK 2 of 3. |
| Reddity | 5 | 7 | Gezamenlijke toren in elke ronde met het bordje van de subreddit, reactie met voorbeeld, Join-knop, gisteren en alle dagen. Min: de gezamenlijke toren is een zuil aan de rand, nog geen moment waarop jij er zichtbaar iets aan toevoegt; in een kleine demo-subreddit blijft het stil. |
| Daily Content | 7 | 7 | Zelfde toren voor iedereen, vijf dagregels, gouden helden vooraf, dagen op rij, gisteren te zien. Min: post en dag lopen nog uit elkaar (N1); de regels zijn vooral tempoknoppen. |

## Top 3 voor de volgende ronde
1. **Op Reddit krijgen en de vier onbekende delen testen** (Redis nx, reactie, lid worden, dagtaak) in een demopost. Vraagt de login van Thijs (uiterlijk ma 23 nov). Dit levert de meeste punten: Polish hangt er helemaal aan.
2. **Het eindmoment terug** (kan 1) **plus dag per post** (kan 2). Klein werk; het eindbeeld is ook het beeld voor het filmpje en de Devpost-pagina.
3. **Je eigen hoeden zichtbaar naar de gezamenlijke toren** aan het eind (een seconde: jouw toren vliegt over naar de zuil van de subreddit, met "r/... passed 1,000 hats today" bij een mijlpaal), daarna het inzendfilmpje op 1080x1920 met dat moment erin. Maakt Reddity zichtbaar in de eerste 10 seconden van de jury.

---

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
