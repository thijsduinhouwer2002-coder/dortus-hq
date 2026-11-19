# Stand: Gloop's Hat Tower op Reddit

## Do 19 nov 2026, fase 1 af (bouwer), nog niet gekeurd
Wat er is: het ontwerp (`ontwerp.md`) en een speelbare webversie in `app/`, gebouwd op de officiële Devvit-template `reddit/devvit-template-bare` (51e9aab). Lokaal speelbaar op telefoon en desktop. Niet op Reddit: daarvoor is `devvit login` nodig (zie onderaan).

### Wat werkt (GEZIEN, zelf gedraaid)
- **Spel:** de regels van Hat Tower uit `Spel.mc`, met dezelfde getallen en plaatjes, in `app/src/shared/spel.ts`. Tikken op het scherm of spatie. Slok, vliegende helm, toren, "GULP!" met reeks, "bye!", gouden helden (+3), vonken, geluid, stilstand van 80 ms op het slikken.
- **Dagspel:** dagnummer (dag 1 = 19 nov, UTC), dagregel uit vijf, gouden helden per dag, hoedvolgorde per dag, één dagbeurt plus oefenen, uitslagkaart met vakjes, dagen op rij, ranglijst per subreddit, gezamenlijke toren (als getal), dagpost om 00:00 UTC (in `devvit.json`, nog niet op Reddit getest).
- **Eerlijke score:** de server speelt elke dagbeurt na uit alleen de tikken; toets "de server speelt hetzelfde potje na" is groen.
- **Toetsen:** `npm test` groen: types (tsc), lint (biome), 12 unit-toetsen (onder meer: ronde precies 30 s, eerste hoed binnen 2,5 s, goede speler 15+ hoeden, missen kost niets, dagbeurt maar één keer, dagen op rij, verzonnen tikken leveren niet meer op), bouw van client en server.
- **Gespeeld met Playwright** (`app/dev/schermen.py`) op 390x780 (telefoon, 3x) en 1280x760 (desktop): start, ronde met tikken, gouden held, gemist, uitslag, reactie plaatsen (lokaal: tekst in het log van de server), terug naar start met eigen uitslag. Geen fouten in de browser.
- **Bekeken** (skill `kijken`): alle schermbeelden en 40 beelden uit het filmpje. Gevonden en opgelost: de geluidsknop lag over de ranglijst; de post in de feed liet de knop over Gloop vallen en werd op een brede post wazig groot; "New best" stond er bij de allereerste ronde; dag 0 gaf een fout.

Beelden: `beelden/1-start-tower-1.png`, `beelden/2-gouden-gulp.png`, `beelden/3-uitslag-ranglijst.png`, filmpje van een ronde `beelden/filmpje-ronde-telefoon.mp4` (37 s, opname van de Playwright-speler, geen inzendfilmpje). De ranglijst op de beelden komt van vijf lokale proefspelers (`practice_bot_...`) die het spel echt spelen met de regels; dat zijn geen echte mensen.

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
