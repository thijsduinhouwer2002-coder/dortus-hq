# Stand: Gloop's Hat Tower op Reddit

## Do 19 nov 2026 middag, filmpje opnieuw en kleine spelpunten (bouwer), nog niet gekeurd
Na de keuring van 2b (spel akkoord ja, filmpje nee).

### Filmpje `beelden/inzendfilmpje-1080x1920.mp4` (GEZIEN, zelf bekeken)
- **33,8 s**, 1080x1920, 30 beelden per seconde, H.264 met AAC-geluid.
- **Begint met actie:** beeld 0 is al de ronde; de held valt vanaf de eerste seconde, op 0 s klinkt een korte startklank (nieuw, ook in het spel), de eerste "PERFECT!" met slokklank valt op ±1,8 s. Titel in beeld de eerste 2,4 s: "Gloop's Hat Tower / a daily game on Reddit". Geen startscherm meer.
- **Echt scherp:** het spel loopt in het filmpje op een eigen klok (`src/client/filmklok.ts`, alleen met `?film=1`); `dev/film.py` zet de klok per beeld 1/30 s verder (in 4 stapjes, zodat de speler precies kan mikken) en maakt een PNG op 360x640 bij 3x, dus echt 1080x1920. Op ware grootte nagekeken (uitsnede 600x700): randen van Gloop, hoeden en letters scherp, geen jpeg-blokjes.
- **Geen proefnamen:** de lokale subreddit heet nu r/GloopsHatTower (`SUB=` om te kiezen); de ranglijst komt niet in beeld, en de regel boven het voorbeeld van de reactie noemt geen gebruikersnaam meer ("Posts as a comment from your account, under this post:"; dat lost ook "today's post" op een oude post op). Of r/GloopsHatTower op Reddit vrij is, is ONBEKEND; de echte naam komt met de opname op Reddit.
- **Ingekort:** 5 s uit het midden van de ronde eruit (van 12 tot 17 s), dus één harde knip waarbij de teller van ±15 naar ±31 springt. De vijf teksten staan er nog in, plus de titel.
- Inhoud: ronde met 56 hoeden, reeks tot 10, gouden held, een misser met "bye!", de camera van de top naar Gloop, je hoeden die groot naar de gezamenlijke toren vliegen met "+56 hats", "r/GloopsHatTower passed 150 hats today!" links in beeld, en het uitslagvel. Speler is de speler in de pagina; de 129 hoeden van vandaag komen van lokale proefspelers die niet in beeld komen.
- Nog niet: opname op Reddit zelf (post in de feed, tik, groot spel, reactie). Kan pas na de login van Thijs.

### Spel
- Mijlpaal staat links in de lege lichtbaan, niet meer over je eigen toren, en vervaagt na 1,9 s, zodat het uitslagvel vrij blijft.
- Je hoeden vliegen nu groot (op ware grootte, krimpend naar de maat van de verre toren), trager (0,9 s, 10 stuks), van onderin je toren naar een plek op de gezamenlijke toren die in beeld is, met "+N hats" bij de toren.
- Pauzeren of wegzetten tijdens de dagbeurt telt niet als te laat: het spel meet hoe lang het op de achtergrond stond en stuurt dat mee; de server trekt dat af (tot 10 minuten). Toets erbij.
- Nieuwe startklank bij het begin van een ronde.

Nieuwe beelden (uit het filmpje, 720 breed): `beelden/4-perfect-reeks.png`, `beelden/5-mijlpaal-gezamenlijke-toren.png`, `beelden/6-uitslag-delen.png`. De oudere `1-start.png` tot `3-uitslag.png` zijn lokale proefbeelden van 2a met de oude proefnaam.

Toetsen: `npm test` groen (types, lint, 22 toetsen, bouw).

## Do 19 nov 2026 middag, fase 2b af (bouwer), nog niet gekeurd
Na de herkeuring (akkoord ja, UX 8, Polish 7, Reddity 7, Daily 7).

### Wat er veranderd is (GEZIEN, zelf gedraaid en bekeken)
1. **Eindmoment terug.** De camera zoomt nooit verder uit dan 0,5. Past de toren dan niet, dan begint de camera bij de top en zakt hij in 1,5 s naar Gloop (gezien bij 58 en 67 hoeden). Bij een lage toren zoomt hij gewoon uit zoals eerst.
2. **Elke post speelt de toren van zijn eigen dag** (keuring A10). Bij het maken van een post (menu, installatie, dagtaak) zet de server `post:<id>` = dag in Redis. Een oude post speelt die toren, met zijn eigen ranglijst en één beurt per speler. Op het startscherm staat dan "This is tower #3 from 2026-11-21. Today's tower #9 is in the newest post." Dagen op rij tellen alleen met de toren van vandaag (of gisteren, rond middernacht). Posts zonder bekende dag spelen vandaag.
3. **Je hoeden vliegen naar de gezamenlijke toren.** Na de camera vliegen tot 14 hoeden van jouw toren naar de toren van de subreddit; de teller op het bordje telt mee op. Passeer je een rond getal (25, 50, 100, 150, 200, 250, ... 1.000, 1.500, ...), dan verschijnt "r/... passed 150 hats today!" met goud en een klank. Alleen bij een dagbeurt die echt meetelt, niet bij oefenen. Tijdens het spelen groeit de gezamenlijke toren niet meer live mee (dat zou dubbel tellen). De gezamenlijke toren staat nu helemaal binnen beeld (midden op x 392) met zijn voet op de vloer, en is op het startscherm doffer.
4. **Insturen alleen op tijd.** De starttijd staat in de startsleutel. Insturen kan vanaf 27 s na de start (eerder kan de ronde niet klaar zijn) tot 60 s na het eind van de ronde. Te laat telt als afgebroken (0 hoeden). Toets erbij.
5. **Inzendfilmpje** `beelden/inzendfilmpje-1080x1920.mp4`: 1080x1920, 43,9 s, H.264 met AAC-geluid. Startscherm, een hele ronde (67 hoeden, reeks tot 17, gouden held, een misser met "bye!"), de camera van de top naar Gloop, de hoeden naar de gezamenlijke toren met "r/GloopTowerTest passed 150 hats today!", het uitslagvel en de ranglijst. Engelse tekst in beeld: "One tap. 30 seconds.", "Perfect gulps stack more hats", "Same tower for everyone today", "Every subreddit builds one tower", "Share your run. New tower tomorrow." Gemaakt met `app/dev/film.py`: beelden op ware grootte uit het screencast van Chrome (55 per seconde), geluid uit dezelfde klanken van het spel, achteraf gerenderd in een OfflineAudioContext en op tijd gezet. Speler is de Playwright-speler in de pagina (mikt rond de bek, 4% te laat); de ranglijst komt van lokale proefspelers. Subreddit-naam in beeld is de lokale proefnaam GloopTowerTest.
6. Klein: het gulp-vakje in de reactie is nu oranje (zoals in het spel), een klank als een hoed op de toren landt, de beste toren werd de eerste keer niet bewaard (opgelost, toets erbij), geen geluidsknop in het filmpje.

Nieuwe beelden: `beelden/4-perfect-reeks.png`, `beelden/5-mijlpaal-gezamenlijke-toren.png`, `beelden/6-uitslag-delen.png` (stilstaande beelden uit het filmpje, 720x1280, met de Engelse tekst erop).

Toetsen: `npm test` groen (types, lint, 21 toetsen, bouw).

### Nog open
- Alles wat Reddit zelf doet is nog niet getest (Redis nx, reactie en lid worden namens de speler, dagtaak, de dag per post). Vraagt de login van Thijs.
- Het filmpje heeft alleen de spelklanken, geen muziek. Of het zo goed genoeg is voor de jury, beslist de hoofdchat; muziek erbij kan met een eigen of vrij stuk (niets kopen zonder ja).
- Niemand heeft het als mens gespeeld.

## Do 19 nov 2026 middag, fase 2a (bouwer)
Na de keuring (`KEURING.md`: akkoord nee, UX 6, Polish 6, Reddity 5, Daily 7) en de reactie van Thijs op de animatie.

### Wat er veranderd is (GEZIEN, zelf gedraaid en bekeken)
1. **Mikken loont (moet 1).** Gewone vangst 1 hoed; voltreffer 2, met een reeks voltreffers 3 en daarna 4 per vangst; gouden held 2 extra. Te vroeg happen breekt de reeks (kost geen hoed) en de bek blijft 350 ms dicht (horloge 250). Vroeg vangen geeft geen tempo meer: de pauze na een vangst duurt zolang de held nog tot de onderkant van de bek had moeten vallen. Toets: mikken met spreiding 45 (en 10% te laat) haalt op alle vijf dagregels minstens 25% meer dan het beste vaste tikritme van 200 tot 400 ms (5 fasen per ritme). Nagerekend op dag 1 tot 15: verschil 30 tot 106% (kleinste op Classic en Golden Hour).
2. **Eén dagbeurt (moet 2).** `api/start` zet per speler per dag één sleutel, alleen als die nog niet bestaat. Herladen of een tweede tabblad: de beurt staat als gebruikt (0 hoeden, "started and not finished") en wat je speelt is oefenen. Insturen kan alleen na een start, en de uitslag wordt eerst geclaimd (zet-als-nieuw) en dan pas geteld, dus twee gelijktijdige inzendingen tellen één keer. Een ronde die vlak voor middernacht UTC begon, telt nog voor die dag. Toetsen voor alle drie groen.
3. **Animatie.** Nieuwe plaatjes uit de echte 3D-modellen van Hats (`kunst/render.sh` met bpy, `kunst/knip.py`), 2,6 keer zo groot als op het scherm nodig: geen pixels en geen zwarte rand meer. De held valt in een boog langs de lichtbaan, tuimelt, rekt een beetje uit en draagt de hoed die straks op de toren komt. Bij een slok gaat hij ondersteboven de mond in (alleen boven en in de mond zichtbaar), Gloop zakt in en veert na, slijmdruppels, vonken bij een voltreffer, goud bij een gouden held, een korte schermschok, 80 ms stilstand. De hoeden vliegen een voor een naar de toren, landen met squash en de toren zwiept na. Gloop ademt, knippert, rekt zich uit als een held nadert, hapt open in de vangzone, knijpt zijn oog dicht bij een misser of te vroeg happen en schudt zijn hoofd. Gemist: de held valt door, landt met squash en stof, en hupt weg. Gemeten 58 tot 60 beelden per seconde in headless Chrome op 3x zonder grafische kaart (grot en gezamenlijke toren worden één keer getekend en hergebruikt).
4. **Gezamenlijke toren als beeld.** Achterin rechts staat de toren van de subreddit van vandaag (een hoed per hoed, wankel, verder weg en doffer), met een bordje "r/... / 1,204 hats today". Je eigen hoeden komen er live bij. Hij vult de lege grot.
5. **Eindscherm.** Reactie met witregels; de tekst staat eerst in beeld met "Posts as u/... under today's post", daarna "Post as comment". Knop "Join r/... for tomorrow's tower" (Devvit `subscribeToCurrentSubreddit`, alleen na een tik). Uitleg van de vakjes. "Since tower #1: N hats" en "Yesterday's tallest towers". Liggend scherm (844x390) heeft nu een compacte opmaak met de knoppen naast elkaar; de knop in de feed breekt niet meer over twee regels en de pet valt niet meer buiten beeld.
6. **Kan-punten.** `app/LICENSE`: code BSD (deels van de template van Reddit), Gloop, de helden, de hoeden en alle plaatjes (c) 2026 Dortus, letters onder OFL met de volledige teksten in `public/fonts/`. README: puntentelling, eerlijke start en een stuk voor moderators. Geen taknaam meer in het commentaar. `architectuur.md` erbij. Bestanden onder 400 regels (scene opgesplitst in basis, held en scene; css in stijl en uitslag).

Beelden: `beelden/1-start.png`, `beelden/2-gouden-gulp.png`, `beelden/3-uitslag.png`, filmpje `beelden/filmpje-ronde-telefoon.mp4` (32 s, 390x780, een hele ronde plus het uitslagvel; gespeeld door de Playwright-speler in de pagina zelf, die rond de bek mikt en 12% te laat is). De ranglijsten op de beelden komen van vijf lokale proefspelers (`practice_bot_...`), geen echte mensen.

Toetsen: `npm test` groen (types, lint, 18 toetsen, bouw).

### Nog open
- Niemand heeft het als mens gespeeld; of het tempo en de nieuwe telling goed voelen, weet alleen een mens.
- Of `redis.set(..., {nx: true})` echt "OK" teruggeeft als de sleutel nieuw is, is GOK; testen in playtest (de toets gebruikt de opslag in het geheugen).
- `submitComment` en `subscribeToCurrentSubreddit` namens de speler: pas te testen na de login; Reddit kan er goedkeuring voor vragen.
- De dag hangt nog aan vandaag, niet aan de post (keuring A10): een oude post speelt de toren van vandaag.
- Geluid is nog getekend met de Web Audio API; geen echte klanken.

## Do 19 nov 2026 ochtend, fase 1 (bouwer)
Wat er is: het ontwerp (`ontwerp.md`) en een speelbare webversie in `app/`, gebouwd op de officiële Devvit-template `reddit/devvit-template-bare` (51e9aab). Lokaal speelbaar op telefoon en desktop. Niet op Reddit: daarvoor is `devvit login` nodig (zie onderaan).

### Wat werkt (GEZIEN, zelf gedraaid)
- **Spel:** de regels van Hat Tower uit `Spel.mc`, met dezelfde getallen en plaatjes, in `app/src/shared/spel.ts`. Tikken op het scherm of spatie. Slok, vliegende helm, toren, "GULP!" met reeks, "bye!", gouden helden (+3), vonken, geluid, stilstand van 80 ms op het slikken.
- **Dagspel:** dagnummer (dag 1 = 19 nov, UTC), dagregel uit vijf, gouden helden per dag, hoedvolgorde per dag, één dagbeurt plus oefenen, uitslagkaart met vakjes, dagen op rij, ranglijst per subreddit, gezamenlijke toren (als getal), dagpost om 00:00 UTC (in `devvit.json`, nog niet op Reddit getest).
- **Eerlijke score:** de server speelt elke dagbeurt na uit alleen de tikken; toets "de server speelt hetzelfde potje na" is groen.
- **Toetsen:** `npm test` groen: types (tsc), lint (biome), 12 unit-toetsen (onder meer: ronde precies 30 s, eerste hoed binnen 2,5 s, goede speler 15+ hoeden, missen kost niets, dagbeurt maar één keer, dagen op rij, verzonnen tikken leveren niet meer op), bouw van client en server.
- **Gespeeld met Playwright** (`app/dev/schermen.py`) op 390x780 (telefoon, 3x) en 1280x760 (desktop): start, ronde met tikken, gouden held, gemist, uitslag, reactie plaatsen (lokaal: tekst in het log van de server), terug naar start met eigen uitslag. Geen fouten in de browser.
- **Bekeken** (skill `kijken`): alle schermbeelden en 40 beelden uit het filmpje. Gevonden en opgelost: de geluidsknop lag over de ranglijst; de post in de feed liet de knop over Gloop vallen en werd op een brede post wazig groot; "New best" stond er bij de allereerste ronde; dag 0 gaf een fout.

Beelden van fase 1 zijn vervangen door die van fase 2a (zie boven). De ranglijst op de beelden komt van vijf lokale proefspelers (`practice_bot_...`) die het spel echt spelen met de regels; dat zijn geen echte mensen.

### Lokaal draaien
```
cd producten/reddit-hat-tower/app
npm install
npm test
PROEF=1 npm run local      # http://localhost:5173/splash.html en /game.html
```
`?u=naam` speelt als een andere speler, `?dag=12` speelt een andere dag. Node 22 werkt lokaal; Devvit vraagt Node 24.18 of nieuwer voor `devvit playtest`.

### Wat nog niet goed is of ontbreekt
- Niemand heeft het als mens gespeeld. Of het leuk is op een telefoon, weet alleen een mens.
- De gezamenlijke toren is een getal, nog geen beeld. Voor Reddity is een getekende toren van de subreddit sterker (bijvoorbeeld een hoed per 100 hoeden).
- Plaatjes zijn de 454-kit van het horloge; op een telefoon iets zacht. Scherper maken uit de renders van 400 px in `ontwerp/garmin/gloop-spel/bron-renders/` (vraag aan Mila).
- Bovenin het scherm is het tijdens de eerste seconden leeg. Kan rustiger of mooier (grotplafond, druppels).
- Op een brede post in de feed staat Gloop rechts met een donkere vlakke rand links; kan mooier.
- Spammen (elke ±260 ms tikken) vangt veel, maar zonder reeks. Zo is het op het horloge gekeurd; opnieuw bekijken na het eerste echte spel.
- Niet getest: `submitComment` namens de speler, de dagtaak, de echte Redis, ingelogd en uitgelogd op Reddit. Dat kan pas na de login.

## Fase 2 (wat er moet, in volgorde)
1. **Thijs: login** (zie onder). Daarna `npm run playtest` in `app/`: Devvit maakt zelf een test-subreddit en een post (GEZIEN in de quickstart: "The dev command automatically creates a development subreddit").
2. **Op Reddit testen:** Redis-ranglijst, dagen op rij, reactie plaatsen namens de speler (`asUser: SUBMIT_COMMENT` in `devvit.json`; mogelijk vraagt Reddit daar goedkeuring voor), dagtaak om 00:00 UTC, uitgelogd spelen, de post in de feed op telefoon en desktop (hoogte "tall").
3. **Polish:** gezamenlijke toren als beeld, scherpere plaatjes, korte uitleg bij de eerste held, het lege bovenstuk, een titelbeeld voor de post.
4. **Keuring** door een ander (skill `keuren`) en Iris op plezier en beeld.
5. **Openbare test-subreddit** onder 200 leden met een post waarin het spel draait (eis van de wedstrijd), of de app `dr-admin-approve` erin.
6. **Inzending op Devpost:** tekst in het Engels met de vermelding dat het een port is van ons eigen horlogespel (de categorie vraagt dat; in het spel zelf staat het niet), link `developers.reddit.com/apps/gloop-hat-tower`, de README (staat klaar in `app/README.md`), link naar subreddit en post, en het **filmpje onder 1 minuut** (in de praktijk verplicht: de jury mag alleen op tekst, beelden en filmpje oordelen, `KEURING.md` A5). Tekst gaat onder de naam van Thijs, dus zijn ja nodig (uiterlijk ma 7 dec). Filmpje op @Dortusapps na keuring door een ander.
7. Eventueel: Feedback Award ($200, 5x): het feedbackformulier invullen.

## Wat Thijs moet doen voor `devvit login` (±15 minuten, uiterlijk ma 23 nov)
1. **Een Reddit-account voor Dortus maken** (niet zijn eigen account; harde regel 4). Gewoon via reddit.com, met een mailadres van Dortus. ±5 min.
2. **Naar developers.reddit.com gaan**, inloggen met dat account en de voorwaarden voor ontwikkelaars accepteren. ±2 min.
3. **Inloggen samen met de hoofdchat:** de hoofdchat draait `npx devvit login --copy-paste` (GEZIEN: die optie bestaat in devvit 0.15.4) en geeft Thijs een link. Thijs opent de link, logt in met het Dortus-account, keurt goed en plakt de code die Reddit toont terug in de chat. ±5 min. Het token komt in `~/.devvit/token` van die omgeving en gaat nooit de repo in.
4. Los daarvan (mag op hetzelfde moment): **Devpost-account en "Join Hackathon"** op redditgameofday2026.devpost.com, ±10 min, uiterlijk ma 23 nov (daarmee accepteert hij de regels).

Kosten: geen. Geen geld nodig voor Devvit, Devpost of de test-subreddit.
