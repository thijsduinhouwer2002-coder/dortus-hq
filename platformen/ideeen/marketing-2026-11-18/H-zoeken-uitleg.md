# H: zoeken en uitleg (dortus.com, lange YouTube-uitleg, SEO voor "how to")

Agent H, 18 nov 2026 ±21:00 tot 22:30 NL, opdracht `BRIEF.md` (tweede ronde). Alle webpagina's met curl gelezen op 18 nov. Labels: **GEZIEN** (zelf gemeten of in officiële uitleg gelezen), **DERDEN** (iemand anders zegt het, met link), **GOK** (niet nagekeken). Niets geplaatst, niets ingediend, niets aangezet.

## 0. Wat al bekend is (niet overgedaan)
- Hoofdles 3: een uitlegvideo die een zoekvraag beantwoordt wint van reclame (Notebook Navigator masterclasses 118.000 en 110.000 tegen korte 8.200 en 16.000; TrueDepth "how to install and use" 31.000 en 36.000) (`platformen/succes/lessen.md`).
- Hoofdles 4: video's van anderen brengen meer dan je eigen kanaal (Auto-Rig Pro, Nomad Sculpt, HueForge, AutoCam 251.537).
- Kandidaat-lessen: installeren en uitleg zijn waar de punten verloren gaan (CatPin-reviews: video te snel, geen uitleg per knop); de uitlegvideo in het product zelf (Notebook Navigator).
- Verhaal 34 (Chrome): "eigen site gevonden in Google" was de hoofdbron bij 2 van 27 makers (Robomonkey 3.000 gebruikers bij 5.000 bezoekers per maand, VocaScript 710); de eerste 1.000 duren 6 tot 9 maanden.
- `ontwerp/website/voorstel-ombouw-2026-11-13.md` deel 6: SEO-basis per pagina (title, canonical, JSON-LD, tekst als HTML), "breathing app Garmin" is niet te winnen.
- B en C stellen al één YouTube-uitleg voor Bison & Flex voor (studenten, "Flex & Bison Tutorial: Part 1" 120.448). E heeft de keten tot "klaar voor goedkeuring" en Metricool.

Hieronder gaat het verder: hoeveel vraag er per product echt is, wat een eigen uitleg oplevert bij kanalen zo klein als het onze, Google tegenover YouTube in 2026, en één werkwijze die per uitleg een pagina én een video maakt.

---

## 1. Wat werkt aantoonbaar

### 1a. De vraag bestaat, maar zit op YouTube en in "installeren"-vragen (GEZIEN 18 nov)
Gemeten met curl: YouTube-zoekpagina (`youtube.com/results`, weergaven en leeftijd zoals YouTube ze toont), de automatische aanvullingen van Google en YouTube (`suggestqueries.google.com`, wat mensen echt typen), en de Stack Exchange-API.

| Product | Zoekvraag | Wat er staat (weergaven, leeftijd, kanaal) | Per jaar (mijn som) |
|---|---|---|---|
| Bison & Flex | "flex bison tutorial" | Part 1 120.448 (8 jaar, sanwade, 698 abonnees); Part 2 68.865 (8 jaar); installatie 33.780 (4 jaar) | ±15.000; ±8.600; ±8.400 |
| Bison & Flex | "flex bison windows" | "Install Flex and Bison on Windows & Run Lex and Yacc Files" 24.252 (1 jaar, Borhan); nieuw van 4 weken: 207 | ±24.000 |
| Bison & Flex | "lex yacc tutorial" | Engelsma Part 01 450.685 (13 jaar); "Run lex and yacc programs in windows 10" 105.372 (5 jaar) | ±35.000; ±21.000 |
| Bison & Flex | "bison clion" | geen enkele video over Bison of Flex in CLion; Google geeft geen aanvulling op "bison clion" | gat, maar weinig zoekers |
| Bison & Flex | Stack Overflow | tags bison 2.644, flex-lexer 2.126, yacc 1.933, lex 1.834 vragen; "How to compile LEX/YACC files on Windows?" 190.632 views; "CMake with flex/bison in CLion" 3.408; 350 vragen over shift/reduce bij bison | |
| Click Joints | "how to make ball joints in blender" | "Ball Joints in Blender (EASY)" 28.783 (4 jaar); Skillful Toys 20 min 4.863 (1 maand); Cleave Quick Tip 757 (3 weken, maker zelf, 139 abonnees); nieuw klein kanaal 48 (3 weken) | ±7.200; ±58.000 als het zo doorgaat (GOK) |
| Click Joints | "blender 3d print addon" | **CatPin-uitleg van de maker zelf, 25 min: 23.121 in 2 maanden** (kanaal 1,22K abonnees); CatPin promo 1:56: 20.846 (3 maanden); CutMode (gratis add-on, 318 abonnees) 1:19: 11.209 (4 maanden) | CatPin ±140.000 als het zo doorgaat (GOK) |
| Click Joints | "print in place joint blender" | de hoek wordt gewonnen door Fusion-uitleg (Slant 3D 511.595 en 983.212, What Make Art 321.005); Blender-variant 1.547 (4 maanden) | |
| Hats | Google-aanvulling op "games that sit" | **eerste aanvulling: "games that sit at the bottom of your screen"** | |
| Hats | "games to play while working" | alleen lijstjes van anderen: The Indie Brew 16.814 (9 maanden), Conkbot 16.204 (10 maanden), CozyAriGames 10.347, JGigs 318.648 en 540.553; "Cozy Idle Desktop Companion Taskbar Games" 947 (1 maand) | |
| Garmin | "garmin breathing app" | Garmin zelf (ECG 170.148, Stress 106.738); kleine apps 4 en 23 views | niet te winnen |

Wat de aanvullingen zeggen (GEZIEN): bij "flex bison" typen mensen "tutorial", "install", "download", "online compiler", "example", "vs code", en op YouTube ook in het Arabisch, Bengaals en Spaans. Bij "blender 3d print" typen ze "toolbox", "addon", "tutorial", "for beginners". Bij "blender ball joint" alleen "rig" en "doll". De vraag van onze kopers is dus: **installeren en de eerste keer laten werken**, niet de naam van ons product.

### 1b. Wat een eigen uitleg oplevert bij een klein kanaal (eerlijk)
- **Het kan bij kanalen zo klein als het onze.** CatPin (1,22K abonnees) haalde met zijn eigen uitleg van 25 minuten 23.121 weergaven in 2 maanden, CutMode (318 abonnees) 11.209 met een filmpje van 1:19 (GEZIEN). CatPin is ook de winnaar van de hoek: 400+ verkopen en eerste op Gumroad bij "articulated figure" (verhaal 3 en 16).
- **Maar de meeste nieuwe uitleg blijft klein:** Cleave 757 in 3 weken (139 abonnees), een nieuw Blender-kanaal 48, twee nieuwe Flex-installatievideo's 207 en 448, twee nieuwe kleine figurenkanalen 38 en 270 (verhalen-groei, GEZIEN). Reken op honderden in de eerste weken.
- **Uitleg stapelt over jaren, reclame niet.** De Flex-uitleg van 8 jaar oud trekt nog ±15.000 per jaar (som uit GEZIEN). Een tutorial is een bezit; een post is na 2 dagen weg.
- **Wat een weergave in installs waard is, heeft niemand laten zien voor lange uitleg.** Het enige getal in onze map: VibeDesk, 3.000 Shorts-weergaven gaven 5 bezoekers en 1 abonnee (EIGEN OPGAVE, Joris), en een gewone video van 1:15 gaf meer dan alle Shorts samen. Daarom meten we het zelf (deel 3, stap F) en noem ik geen opbrengst zonder GOK.

### 1c. Google of YouTube? In 2026 eerst YouTube, de pagina als tweede (GEZIEN)
- **Google houdt "how to"-klikken steeds vaker zelf.** Pew (900 Amerikanen, maart 2025): met een AI-samenvatting klikt een gebruiker in 8% van de bezoeken op een gewoon resultaat, zonder in 15%; op een link in de samenvatting zelf in 1%. Vragen die met who, what, when of why beginnen krijgen in 60% een samenvatting; zoekopdrachten van één of twee woorden in 8% ([Pew Research, 22 jul 2025](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)).
- **YouTube staat zelf in Google.** Dezelfde studie: Wikipedia, YouTube en Reddit zijn de meest getoonde bronnen in samenvattingen én gewone resultaten, YouTube vaker in de gewone resultaten. Eén video werkt dus op twee zoekmachines.
- **Onze eigen proef: ±70 gidsen op dortus.com geven bijna niets.** Het scorebord telt voor alles buiten de productpagina's ("overig") 0, 4 en 8 bezoekers op 16, 17 en 18 nov (GEZIEN, `organisatie/scorebord.md`, Amami). Die gidsen zijn van eind oktober en dus jong, maar het laat zien dat een gids op zich geen stroom geeft.
- **Google is traag.** De Chrome-makers die via Google groeiden, deden 6 tot 9 maanden over 1.000 (verhaal 34). Een eigen pagina telt dus niet mee voor de meting van wo 9 dec; een video wel (die wordt in dagen bekeken of niet).

**Conclusie:** maak per product één echte uitleg (installeren en de eerste keer werken), zet die als video op YouTube en als geschreven pagina met code en schermen op dortus.com. De video zoekt bereik, de pagina vangt de lange zoekvragen en is de plek waar de video, de winkel en Stack Overflow naar kunnen wijzen.

---

## 2. Per product: de 3 acties met de meeste kans

### Bison & Flex (JetBrains): hier is de meeste vraag en het minste aanbod
1. **Eén uitleg "Flex and Bison tutorial: a calculator from zero, on Windows, macOS and Linux" als pagina `dortus.com/bison-flex/tutorial/` en als video van ±10 min.** Waarom: de grootste vraag is installeren en het eerste programma draaien (SO 190.632, Borhan ±24.000 per jaar), en dit publiek zijn studenten (B, C), voor wie de plugin gratis is (besluit 17 nov). In de uitleg is de plugin het gereedschap, niet het onderwerp: kleuren, fouten, springen tussen `.y` en `.l`. De code komt uit `testdata/` en wordt in CI op drie systemen gebouwd, zodat de pagina nooit liegt (deel 3, stap C). Titel met "flex bison tutorial" vooraan; "clion" in de beschrijving (geen zoekvolume op "bison clion", wel het gat).
2. **Pagina "Install Flex and Bison on Windows (WinFlexBison, MSYS2 or WSL) and open the files in a JetBrains IDE".** Waarom: de oudste en grootste vraag (SO, lex/yacc-video's 105.372, Google-aanvulling "download" en "install"). Eén pagina, drie wegen, met een korte video van alleen de schermen. GOK op plek in Google: de vraag is lang en specifiek, dus minder AI-samenvatting dan "what is bison" (Pew), maar de concurrentie is oud en sterk.
3. **Later, bij een Pro-functie: "Bison shift/reduce conflicts explained".** 350 SO-vragen (GEZIEN). Alleen maken als de plugin er iets mee doet (ontwerp.md noemt conflicten als mogelijke betaalde functie), anders is het een losse gids zoals de Atlassian-gidsen, en die leveren niets (1c).

### Click Joints Free en Pro (Blender)
1. **Eén rustige uitleg "How to make ball joints for 3D printed figures in Blender (free add-on)", 8 tot 12 min, elke knop één keer in beeld.** Waarom: CatPin deed precies dit met een kanaal van 1,22K en haalde 23.121 in 2 maanden; de CatPin-kopers missen juist een rustige uitleg per knop (verhaal 16); "how to make ball joints in blender" heeft een oude winnaar van 4 jaar (28.783) en weinig nieuws. Free vooraan, Pro als laatste hoofdstuk. Geen belofte dat het klikt tot er een echte print is (besluit 17 nov); toon de vrije ruimte in mm en het buigbereik, wat de add-on echt laat zien.
2. **Installatievideo van 1 tot 2 min "Install Click Joints Free in Blender (Get Extensions)" en dezelfde stappen op `dortus.com/click-joints/`.** Waarom: bij TrueDepth waren "how to install and use" de best bekeken video's; installeren is waar reviews verloren gaan. Het filmpje kan ook in het veld Website en op de winkelpagina.
3. **De geschreven versie van 1 als `dortus.com/click-joints/ball-joints-blender/`: drie manieren naast elkaar (met de hand met Boolean, met Click Joints Free, met Pro), met schermen uit de echte add-on.** Waarom: een eerlijke vergelijking is wat zoekers willen en wat AI-samenvattingen het minst kunnen vervangen (schermen, stappen). Dit is ook de plek waar we naar Pro mogen verwijzen; in Blender zelf mag dat niet (besluit 15 nov).

### Hats of the Fallen (Steam)
Zoeken en uitleg zijn hier bijzaak: de motor is Steam en de lijstjes van anderen (D, C, Sem).
1. **Nu al een pagina `dortus.com/hats-of-the-fallen/` (nu 404, GEZIEN).** Waarom: de Steam-pagina komt misschien pas eind januari (D, deel 0). Tot dan vindt wie de naam van TikTok of een maker opzoekt niets. Eerste regel met de zin die mensen in Google typen: "a game that sits at the bottom of your screen" (eerste aanvulling, GEZIEN). Met echte clips uit `steam-hol-clips.yml` en, zodra hij er is, de knop naar Steam. Teksten blijven concept tot Thijs ze schrijft (besluit 16 nov 21:05).
2. **Op die pagina een perskit met kant-en-klare beelden (B-roll, GIF's, logo, korte feiten) om te downloaden.** Waarom: de video's die tellen zijn lijstjes van anderen (The Indie Brew 16.814, Conkbot 16.204, CozyAriGames); hoe makkelijker het materiaal, hoe eerder ze ons opnemen (hoofdles 4). Het benaderen zelf ligt bij Sem en G.
3. **Na de demo (4 jan): een korte beginnersgids als Steam-gids en op de pagina.** Waarom: een spel van ±100 uur krijgt zoekvragen van spelers ("how to unlock ..."); dat is pas na spelers zinvol. GOK, geen bewijs gemeten; laagste prioriteit.

### Garmin (licht)
1. **Fout op `dortus.com/ebb/`: de pagina zegt "$4.99 once", de winkel $2.99 (GEZIEN, title en description van de pagina tegen het scorebord).** Eerlijkheid gaat voor; de hoofdchat of de Garmin-eigenaar zet het gelijk.
2. Verder geen SEO of uitleg: "garmin breathing app" is van Garmin zelf (GEZIEN, 1a), en Garmin is geparkeerd.
3. Gloop's Hat Tower: op de Hats-pagina één regel "play Gloop's Hat Tower on your Garmin" en omgekeerd; meer niet.

---

## 3. Wat te automatiseren is: één script, twee uitingen

```
 A  Zoekvragen (wekelijks, workflow)          Google- en YouTube-aanvulling, YouTube-zoekpagina, Stack Exchange-API
        |                                     -> platformen/<platform>/zoekvragen.md   (kosten 0, Thijs niets)
        v
 B  Uitlegscript (eigenaar, Claude-run)      producten/<p>/uitleg/<slug>.md: vraag, stappen, code, wat op beeld komt
        |
        +--> C  Code en stappen getoetst (CI)   flex/bison/cmake op ubuntu, windows, macos; Blender-stappen headless
        |
        +--> D1 Pagina (CI)                     HTML in dortus-repo/<product>/<slug>/ uit sjabloon, controle op title,
        |                                       description, canonical, geen < of > in tekst die naar YouTube gaat
        +--> D2 Video (CI)                      opname uit de echte IDE of Blender op Xvfb + ffmpeg, tekst in beeld uit
        |                                       dezelfde stappen, hoofdstukken uit de tijden van de stappen
        v
 E  Keuring (Daan, skill keuren) -> pagina live (eigen map, mag na keuring, opslaan.md)
                                 -> video naar goedkeuren.md -> ja van Thijs -> hoofdchat plant in via Metricool
        v
 F  Meten (scorebord)            Amami-verwijzers per pagina, YouTube-weergaven, Search Console-klikken per zoekvraag
```

| Stap | Hoe | Kosten | Thijs één keer | Status |
|---|---|---|---|---|
| A Zoekvragen | `suggestqueries.google.com/complete/search?client=firefox&q=...` (met `&ds=yt` voor YouTube), YouTube-zoekpagina (ytInitialData), `api.stackexchange.com/2.3` (zonder sleutel een klein dagquotum: na ±130 aanroepen nog 171 over, GEZIEN) | € 0 | niets | proef gedraaid in deze run (tabel 1a). Let op: de aanvul-adressen zijn niet officieel gedocumenteerd en kunnen veranderen (GOK); rustig, één keer per week |
| B Script | skill `update-tekst`-achtig sjabloon: vraag uit A, stappen, code uit `testdata/` of e2e | € 0 extra | niets | nieuw |
| C Toets | workflow die de code uit het script bouwt en draait; voor Click Joints de bestaande e2e met dezelfde maten | € 0 (openbare repo) | niets | nieuw; e2e bestaat |
| D1 Pagina | sjabloon in de eigen productmap van de site-repo; nooit `sitemap.xml`, `robots.txt` of andere bestaande bestanden aanraken (opslaan.md). In plaats daarvan een **eigen sitemap per map**, bv. `dortus.com/bison-flex/sitemap.xml`: mag alleen adressen onder die map bevatten, en dat is precies wat we willen (GEZIEN, [sitemaps.org](https://www.sitemaps.org/protocol.html)) | € 0 | niets | nieuw. Bijvangst: onze productpagina's (click-joints, bison-flex, ebb, rollwright) staan nu niet in de sitemap (GEZIEN); de voorpagina linkt er wel naar |
| D2 Video | `jetbrains-bison-flex-film.yml` (Xvfb, xdotool) en de Blender-workflows bestaan; tekst in beeld, geen stem, geen gezicht. CLion in CI is niet getoetst (licentie, GOK); IDEA Community met een terminal kan altijd | € 0 | niets | deels |
| D2 Hoofdstukken | tijdstempels in de beschrijving: eerste op 00:00, minstens drie, elk minstens 10 s (GEZIEN, [YouTube Help](https://support.google.com/youtube/answer/9884579)) | € 0 | niets | nieuw |
| E Plaatsen | **Metricool** zoals bij de filmpjes (telt mee in de 20 posts per maand van Free, E). Alternatief, pas bij veel video's: YouTube Data API `videos.insert` als **privé** uploaden (eigen quotum van 100 uploads per dag, en video's van niet-geverifieerde projecten worden niet meer op privé vastgezet, GEZIEN, [docs](https://developers.google.com/youtube/v3/docs/videos/insert)); na het ja van Thijs zet `videos.update` hem openbaar. Dat is de goedkeuring in YouTube zelf | € 0 | API-weg: Google Cloud-project, OAuth-toestemming op @Dortusapps, app op "In production" zetten, anders verloopt de sleutel na 7 dagen (GEZIEN, [Google OAuth](https://developers.google.com/identity/protocols/oauth2)). 15 min. Niet nodig zolang Metricool volstaat | Metricool werkt al |
| E Indexeren | **Google:** Search Console met een URL-prefix-eigendom per productmap (bv. `https://dortus.com/bison-flex/`), bevestigd met een meta-tag in onze eigen `index.html`: Google zoekt die tag op de pagina waar het adres van het eigendom naartoe gaat (GEZIEN, [Search Console Help](https://support.google.com/webmasters/answer/9008080)). Daarna de mapsitemap indienen. **Bing en anderen:** IndexNow, een `curl` na elke nieuwe pagina. In de root van de site staat al `99b51feeb51a9a81cb709b26637cf03d.txt` met precies die sleutel als inhoud, de vorm van een IndexNow-sleutel (GEZIEN; dat het er één is: GOK). Anders mag een sleutelbestand in onze eigen map, dan geldt het alleen voor adressen onder die map (GEZIEN, [IndexNow](https://www.indexnow.org/documentation)). Google doet niet mee met IndexNow (GOK) | € 0 | Search Console: inloggen, eigendom toevoegen, tag-code aan de hoofdchat geven, op bevestigen drukken (5 min per map, of één keer als hij dortus.com al heeft; staat niet in de repo) | nieuw |
| F Meten | Amami: verwijzers per pagina (Umami heeft een metriek per verwijzer; dat Amami die doorgeeft zoals de paden in `scorebord_amami.py`: GOK); YouTube-weergaven via Data API-sleutel (E); Search Console-API voor klikken en vertoningen per zoekvraag, alleen lezen (Thijs voegt een serviceaccount toe als gebruiker, 2 min; GOK dat dit zonder OAuth werkt) | € 0 | zie E | nieuw |

**Wat Thijs in totaal één keer doet:** Search Console-eigendom voor `/bison-flex/` en `/click-joints/` (10 min) en later het ja op elke video in de wachtrij. Geen geld.

**Meetregel (voorstel aan de hoofdchat, besluit nodig):** de 14 dagen (besluit 17 nov) passen bij de video: na 14 dagen weergaven en verwijzers naar de productpagina. Een pagina krijgt na 14 dagen alleen "geïndexeerd ja of nee en vertoningen" en het echte oordeel na 60 dagen, omdat Google trager is (1c).

**Volgorde:** (1) Bison & Flex-uitleg als pagina en video, (2) Click Joints-uitleg en installatievideo, (3) zoekvragen-workflow, (4) Search Console en mapsitemaps, (5) Hats-pagina met perskit zodra er 6 tot 8 echte schermen zijn (D). Stap 1 en 2 kunnen vóór 9 dec live zijn; alleen de video's tellen dan al mee.

---

## 4. Wat niet werkt of te duur is (niet proberen)
- **Veel pagina's laten schrijven door een taalmodel.** Google noemt "generative AI tools ... to generate many pages without adding value for users" letterlijk spam ("scaled content abuse", GEZIEN, [Google spam-beleid](https://developers.google.com/search/docs/essentials/spam-policies)). Eén uitleg per product met echte code en echte schermen, niet tien.
- **Losse "what is ..."-gidsen voor brede vragen.** Daar staat in 60% van de vraagzoekopdrachten een AI-samenvatting en klikt bijna niemand door (Pew); onze ±70 Atlassian-gidsen geven samen 0 tot 8 bezoekers per dag (GEZIEN).
- **FAQ- of HowTo-gegevens (JSON-LD) voor mooie zoekresultaten.** Sinds aug 2023 toont Google FAQ-resultaten alleen voor bekende overheids- en gezondheidssites, en HowTo alleen nog op desktop (GEZIEN, [Google-blog](https://developers.google.com/search/blog/2023/08/howto-faq-changes)). Geen werk in steken.
- **SEO als antwoord op de meting van 9 dec.** Te traag (1c). Video wel.
- **Algemene Garmin- en ademzoekwoorden**: van Garmin zelf (1a).
- **Een AI-stem of AI-gezicht in de uitleg**: verboden door de brief en niet nodig; tekst in beeld werkt bij Blender Secrets (292.000 abonnees, lessen.md).
- **Betaalde SEO-gereedschappen** (zoekvolume-abonnementen): niet nodig; aanvullingen, YouTube-weergaven en straks Search Console zijn gratis en tonen wat onze zoekers typen.
- **Antwoorden op Stack Overflow door een agent**: dat is plaatsen onder een naam. Kan alleen Thijs zelf, en alleen als het antwoord ook zonder plugin nuttig is (regel uit verhaal 34: "If the answer would not be useful without my product in it, it's too promotional").
- **Een tweede of eigen YouTube-kanaal per product**: wisselen tussen producten op één kanaal wordt niet gestraft (lessen.md, verhaal 23). Alles op @Dortusapps.

---

## Bronnen
- Pew Research Center, 22 jul 2025: https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/
- Google spam-beleid: https://developers.google.com/search/docs/essentials/spam-policies
- Google, FAQ en HowTo: https://developers.google.com/search/blog/2023/08/howto-faq-changes
- Search Console bevestigen: https://support.google.com/webmasters/answer/9008080
- Sitemap-plek: https://www.sitemaps.org/protocol.html
- IndexNow: https://www.indexnow.org/documentation
- YouTube `videos.insert`: https://developers.google.com/youtube/v3/docs/videos/insert ; `captions.insert` kost 400 eenheden: https://developers.google.com/youtube/v3/docs/captions/insert
- OAuth-sleutel 7 dagen in "Testing": https://developers.google.com/identity/protocols/oauth2
- YouTube-hoofdstukken: https://support.google.com/youtube/answer/9884579
- YouTube-zoekpagina's (18 nov, curl): `youtube.com/results?search_query=` met "flex bison tutorial", "lex yacc tutorial", "bison clion", "flex bison windows", "how to make ball joints in blender", "print in place joint blender", "blender 3d print addon", "games to play while working", "desktop idle game steam", "garmin breathing app"; abonnees van @Alex_Sokol_Art, @V4SS3UR, @xideaa, @sanwade op hun kanaalpagina
- Stack Exchange-API: `api.stackexchange.com/2.3/tags/<tag>/info`, `/questions?tagged=bison&sort=votes`, `/search/advanced?q=clion&tagged=bison`
- Google- en YouTube-aanvullingen: `suggestqueries.google.com/complete/search?client=firefox[&ds=yt]&q=`
- dortus.com (curl): `/sitemap.xml`, `/robots.txt`, `/click-joints/`, `/bison-flex/`, `/ebb/`, `/rollwright/`, `/hats-of-the-fallen/` (404)
