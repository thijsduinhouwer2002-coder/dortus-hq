# Ebb (Garmin): lancering klaargezet

Chris, run 32, 13 nov 2026 ±15:15 tot 16:00 UTC. Opdracht: `berichten/chris.md`, bericht van 13 nov 14:10.

**Chris plaatst niets.** De toestemming om onder de naam van Thijs te posten geldt alleen voor de Obsidian-plekken van 8 nov. Alles hieronder plaatst Thijs zelf, en pas als Ebb echt in de winkel staat. Stand om 15:22 UTC (GEZIEN): de winkelpagina https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641 geeft 404 en de winkel-API zegt "The requested app is not approved". Overal waar `<link>` staat, komt die winkellink.

Bronnen die ik naast elkaar legde: winkeltekst `platformen/garmin/upload/ebb-en.md` (versie 19a, de ingediende tekst), `calm-en.md` (versie 1.1), de concepten in `platformen/garmin/gebruikers-krijgen-2026-11-13.md` en de plekken in `kanalen-2026-11-13.md`.

Vaste randen voor elke tekst (uit die stukken): alleen op het droge, zitten of liggen; nergens freediving, apnea, Wim Hof, record of "best time"; geen beloftes over stress, slaap of gezondheid; dieren komen door terugkomen, nooit door langer inhouden; eerlijk zeggen dat Thijs de maker is en dat AI-agents bij Dortus de code schrijven (harde eis van Thijs sinds 9 nov, zie `berichten/chris.md` 11:45); geen oproep tot beoordelen in een forum.

## 1. Garmin-forum, Connect IQ Showcase

**Regels, letterlijk gelezen met curl op 13 nov 15:23 UTC** (https://forums.garmin.com/developer/connect-iq/w/wiki/2/forum-rules):
- "Advertising, spamming, solicitation, and commercial self-promotion are not allowed per Garmin's Terms of Use"
- "Developers are allowed to promote their Connect IQ apps in the Connect IQ Showcase and may link to their app store listings in posts and in their signatures."
- Richtlijnen: "Refrain from posting images larger than 800 x 600 pixels", "Reposting to increase post counts is discouraged", "Use of multiple forum accounts is discouraged".
- Geen regel over AI gevonden. De README van de Showcase (https://forums.garmin.com/developer/connect-iq/f/showcase/403036/connect-iq-apps-showcase---readme): "This is a place to show off your hard work! Post about the projects or features you're working on and get feedback from other developers".
- Gewoonte in titels (GEZIEN, eerste pagina van de Showcase op 13 nov): `[Watch Face] Naam`, daarna een korte uitleg wat het doet, soms "(free)". Ik volg die vorm, met een dubbele punt.

**Waar:** https://forums.garmin.com/developer/connect-iq/f/showcase , knop voor een nieuwe draad. Eén draad voor Ebb, en later ook Ebb Calm als antwoord in diezelfde draad (zie punt 5), niet als tweede draad.

**Beeld:** `commercie/ebb/ebb-film.gif` (480 x 480, 14,25 s, 0,9 MB, binnen 800 x 600). Lukt een bewegend plaatje niet in de editor, gebruik dan `commercie/ebb/ebb-still-600.png` (600 x 600, de krab onder water).

**Titel:**

```
[Watch App] Ebb: breathing rounds and calm 4-7-8 as a little sea, with animals that join as you keep coming back
```

**Tekst:**

```
Hi all, I made Ebb, a breathing app for round Garmin watches.

Your watch face becomes a small sea. The water rises as you breathe in and falls as you breathe out, and when you hold your breath you go under water with a sea animal. The picture stays the same however long you hold.

Two modes: breath hold rounds (deep breaths at a steady pace, a hold for as long as it feels easy, then one recovery breath) and calm 4-7-8. You can also set your own pattern. Every phase has its own vibration, so you can follow it with your eyes closed. While you breathe and hold, only the buttons work, so a sleeve can't stop a hold.

A small fish swims with you from the first session. 24 sea animals join as you keep coming back, with sessions and weeks in a row, never by holding longer. Rest days don't break the streak.

Sessions save to Garmin Connect as a breathing activity with heart rate. $4.99 once in the Garmin store: no subscription, no unlock code, no extra account, no phone app. For practice on land only: sit or lie down.

How it's made: Ebb comes from Dortus, my small studio, where AI agents write the code. I direct and test the work. This version was compiled for all 28 supported watches and tested in the Connect IQ simulator; it has not been tested on every watch model.

A free calm-only version, Ebb Calm, is planned; I'll post it in this thread when it's in the store.

Store: <link>

Questions, bugs and ideas are welcome in this thread, or mail thijs@dortus.com.

Made by Thijs at Dortus
```

Gecontroleerd tegen winkeltekst 19a (zin voor zin, en door een controleur, zie onderaan): stijgen en zakken, onder water bij inhouden, beeld blijft gelijk, rondes met één herstelademhaling, 4-7-8, eigen patroon (My pattern), eigen trilling per fase, aanraakscherm doet niets tijdens ademen en inhouden, vis vanaf de eerste sessie, 24 dieren door sessies en weken op rij, rustdagen breken de reeks niet, opslaan met hartslag, $4,99 eenmalig zonder abonnement, code, account of telefoonapp, alleen op het droge. "Compiled for all 28" en "tested in the simulator": zie `platformen/garmin/status.md` (compileren voor alle 28 horloges; schermen en toetsen in de simulator op 14 horloges, run 43327097299 op e40269e1). Bewust niet "tested on all 28" en niet "every build", want schermen zijn er van een deel van de horloges (14 mappen op tak `schermen`, status.md noemt 13 in de toetsrun), en toekomstige bouwsels beloven we niet. De prijs $4,99 staat in status.md; nakijken op de winkelpagina zodra die openbaar is.

**Forumhandtekening (één regel; in het profiel onder Settings, Signature, als het forum dat veld heeft):**

```
Maker of Ebb, breathing rounds and calm 4-7-8 for round Garmin watches: <link>
```

Mag volgens de regel hierboven ("may link to their app store listings ... in their signatures"). Pas invullen als de link werkt.

**Wanneer:** dag 2 na goedkeuring (eerst zelf kopen en op het horloge zetten op dag 1, zie het plan in `gebruikers-krijgen-2026-11-13.md`). Minuten Thijs: 10 voor de draad, 2 voor de handtekening.

## 2. r/Garmin

**Regels lezen met curl: niet gelukt (13 nov 15:18 UTC, GEZIEN).**
- `https://old.reddit.com/r/Garmin/about/rules.json`: 302 naar `https://old.reddit.com/login/?reason=lor2...` (inloggen gevraagd).
- `https://www.reddit.com/r/Garmin/about/rules.json`, `.../wiki/index.json` en `https://api.reddit.com/r/Garmin/about/rules`: 403 met de pagina "You've been blocked by network security."
- Zoeken (WebSearch "r/Garmin subreddit rules self promotion") gaf geen regels van de subreddit, alleen de Garmin-forumregels en een spiegelsite. Spiegelsites gebruik ik niet.
- Claude in Chrome kan reddit.com ook niet openen (hoofdchat, 9 nov 09:25).

**Uitkomst: ik weet niet of zelfpromotie mag en welke flair nodig is. Volgens de opdracht komt er daarom geen concept voor r/Garmin.** Het oude concept in `gebruikers-krijgen-2026-11-13.md` (concept 2) blijft op slot.

Waarom extra voorzichtig (GEZIEN in onze eigen geschiedenis): r/ObsidianMD bleek een regel te hebben "If your first and only post is to promote your project (vibe-coded or otherwise), you will be immediately banned" en "No slop". Het Reddit-account van Thijs heeft 1 karma en daar nooit iets geplaatst (`berichten/chris.md`, 9 nov 11:45). Een eerste bericht over een eigen, door AI gebouwde app is precies wat zulke regels raken, en karmafilters kunnen het bericht stil weghalen.

**Wat Thijs kan doen (2 minuten, op de lijst):** open r/Garmin op de telefoon, tik "About" (of de zijbalk op de computer), klap elke regel uit en maak een screenshot; kijk ook of er een wiki of een vaste draad voor apps is. Zet het screenshot in de hoofdchat. Dan beslis ik in mijn volgende run: wel een concept (met de goede flair en de AI-zin), of niet plaatsen. Ziet hij zelf iets als "no self-promotion", "no AI", een minimum aan karma of leeftijd van het account: dan niet plaatsen, ook geen screenshot nodig.

## 3. Korte film van de echte app

**Bestanden:** `commercie/ebb/ebb-film.mp4` (600 x 600, 14,25 s, 0,29 MB, H.264) en `commercie/ebb/ebb-film.gif` (480 x 480, 0,9 MB, loopt rond). Script: `commercie/ebb/maak.py` (Pillow voor de overgangen, ffmpeg voor mp4 en gif). Gereedschap: ffmpeg, kandidaat uit `organisatie/gereedschap.md`, werkt; ik zet het daar als voorstel bij de berichten (die lijst is niet mijn bestand).

**Bron:** schermen uit de simulatorrun 43327097299 op commit e40269e1, de ingediende app (GEZIEN in `garmin-adem/plaatjes/RUN.txt` op tak `schermen`), horloge fenix 8 47 mm, map `garmin-adem/plaatjes/namen/`. Bijgesneden tot het horloge, geen tekst of versiering toegevoegd.

**Volgorde (14 s):** menu met de krab (1,2 s) → twee keer inademen en uitademen, het water gaat op en neer (±6 s) → inhouden, onder water met de krab, 1:45 (2,2 s) → eindscherm "new friend: Starfish" (2,2 s) → sea log "8 of 24" (1,6 s).

**Eerlijk:** het zijn stilstaande schermen uit de simulator met zachte overgangen ertussen, geen opname van een echt horloge. De beweging van het water is een overvloeier tussen het in- en uitadem-scherm; in de app gaat het water vloeiend. De tijden op het eindscherm (1:10, 1:25, 1:40) komen uit een andere testscène dan het inhoudscherm (1:45). Wie dat in een bericht wil zeggen: "Screens from the Connect IQ simulator." Als vervanger later beter: een echte schermopname uit de simulator in Actions (vraag voor Gijs, niet mijn werk).

## 5. Tekst voor als Ebb Calm live gaat

Ebb Calm is gratis (prijs 0) en wordt pas ingediend na de goedkeuring van Ebb (`organisatie/lijst-thijs.md`, punt van Gijs). Gecontroleerd tegen `calm-en.md` 1.1.

**Waar:** als antwoord in de eigen Showcase-draad van Ebb (niet een tweede draad: "Reposting to increase post counts is discouraged"). Plus één regel erbij in de handtekening.

**Antwoord in de draad:**

```
Update: there is now a free version, Ebb Calm.

It's the calm part of Ebb: 4-7-8 breathing (in for 4, hold for 7, out for 8) drawn as the same little sea. The water rises and falls with your breath, a small fish keeps you company, and in, hold and out each have their own vibration, so you can follow it with your eyes closed. Save a session and it goes to Garmin Connect as a breathing activity with heart rate.

Free: no account, no subscription, no unlock code, no phone app, no ads. The full Ebb, a separate paid app, adds breath hold rounds, your own breathing pattern and the 24 sea animals to collect.

Ebb Calm: <link Calm>
Sit or lie down while you practise. Feedback welcome here or at thijs@dortus.com.
```

De zin over voortgang tussen de twee apps is geschrapt op advies van de controleur: het was een gok, en Calm heeft niets om over te zetten.

**Handtekening na Calm:**

```
Maker of Ebb (<link Ebb>) and the free Ebb Calm (<link Calm>), breathing apps for round Garmin watches
```

**Wanneer:** dezelfde dag dat Calm openbaar is. Minuten Thijs: 3.

## Wat dit zou veranderen
- r/Garmin blijkt zelfpromotie toe te staan zonder AI- of karmaregel: dan schrijf ik het concept, met flair, in mijn volgende run.
- Garmin keurt Ebb af of de winkeltekst verandert: teksten opnieuw naast de nieuwe winkeltekst leggen.

## Keuring
Controleur (agent, 13 nov ±15:35 UTC): akkoord mits. Moet: (1) Ebb Calm noemen in het forumbericht, (2) geen "every build" en niet suggereren dat elk horloge in de simulator getest is, (3) "alles met ogen dicht" in het berichtje te ruim, (4) 48 uur is een retourtermijn, geen terugbetaaltermijn, (5) AI-zin ook in de persoonlijke berichtjes. Alle vijf verwerkt. Kan-punten verwerkt: dubbele punt in de titel in plaats van een streepje, 14,25 s, zin over voortgang geschrapt, handtekening met twee links, "while you breathe and hold", koudetraining uit de lijst. Niet gedaan: andere schermen voor in en uit in de film (dezelfde 12 en 18 zijn echte testscènes; kan later met een schermopname).
