# B. Communities, makers en lijsten (agent B, 18 nov 2026, ±19:00 tot 20:00 UTC)

Opdracht: `BRIEF.md` in deze map. Vraag: waar zitten de gebruikers van Click Joints, Bison & Flex en Hats, wat zijn daar de regels, welke post van een kleine maker deed het goed (met getallen), en wat kan automatisch.

**Hoe ik keek.** Reddit is met curl niet te lezen (403). Het openbare archief Arctic Shift wel: regels per subreddit (`/api/subreddits/rules`), wiki's (`/api/subreddits/wikis`), en alle posts per periode (`/api/posts/search`). Punten in dat archief zijn een **ondergrens** (soms vroeg opgehaald). Ledenaantallen komen uit hetzelfde archief en zijn van **feb 2025** (DERDEN, ouder getal; Reddit toont zelf geen leden meer). Verder: Hacker News via de Algolia-API, Stack Overflow-API, YouTube-zoekpagina's met curl, de README en git-geschiedenis van awesome-lijsten (git clone), en de sites van BlenderNation, blender-addons.org, CG Channel, Hackaday en de JetBrains-docs. Na een paar honderd verzoeken gaf Arctic Shift "Timeout. Maybe slow down a bit"; daar ben ik gestopt.

## Al bekend (niet overgedaan)
- r/blender, r/3Dprinting, r/customactionfigures, r/Garmin: mediaan 1 tot 2 punten, video helpt, "laat de print zien en stel een vraag" (Joris in `platformen/succes/lessen.md`).
- Forums (BlenderArtists, Obsidian, Garmin) en Show HN voor plugins: bodem, geen motor (Vera, `platformen/verkenner/verspreiden-2026-11.md`).
- Draaiboeken per product met teksten: `commercie/blender-click-joints/verspreiding.md`, `commercie/jetbrains-bison-flex/verspreiding.md`, `commercie/lanceerposts.md` (Chris).
- Hats: 86 YouTube-kanalen, TikTok-lijstaccounts (Indie Game Joe), curatoren, pers en festivals (Sem, `platformen/steam/marketing/`).
- Lijstkanalen van 4.000 tot 300.000 abonnees maken de winnaars, niet de grootste kanalen (Fenna, hoofdles 4).

## Nieuwe feiten voor de hoofdchat (GEZIEN vandaag)
1. **BlenderNation heeft Click Joints geplaatst op 18 nov 2026**: "Click Joints: free add-on that cuts printable ball joints and shows how far they bend" (https://www.blendernation.com/2026/11/18/click-joints-free-add-on-that-cuts-printable-ball-joints-and-shows-how-far-they-bend/). In `commercie/blender-click-joints/geplaatst.md` staat nog "wacht op hun keuring".
2. **awesome-blender heeft pull request #141 samengevoegd op 17 nov**; Click Joints staat in de README onder "3D Printing & Manufacturing/CAM" (regel 132). Ook dit staat nog als "wacht".
3. Click Joints Free: **233 downloads** op extensions.blender.org (18 nov 19:45 UTC; 16 nov 21:50 UTC waren het er 172). Welk deel van de stijging van BlenderNation komt, kan Vera met haar uurmetingen zien.
4. **r/incremental_games eist sinds 2 jun 2026 een blok "AI Disclosure" in elke post van een maker** (wat, waarvoor en hoeveel AI; zonder blok wordt de post weggehaald; aankondiging 877 punten). Alleen reacties in de wekelijkse Feedback Friday-draad zijn vrij. Hats is door AI geschreven. Het besluit "geen AI-melding" (16 nov 21:05) gaat over Steam; voor deze subreddit moet Thijs kiezen: eerlijk melden of de plek overslaan. Nooit weglaten.

---

## 1. Wat werkt aantoonbaar, per plek

### Hats (bureaublad, idle, cozy)

| Plek | Grootte | Regels voor makers | Wat het deed (GEZIEN via Arctic Shift) | Wanneer |
|---|---|---|---|---|
| **r/incremental_games** | 150.070 leden | Eigen werk 1 keer per 30 dagen; er moet iets speelbaars zijn (demo, Steam-playtest of itch telt); blok "AI Disclosure" verplicht; Feedback Friday-draad wekelijks | 1 jun tot 18 aug: 2.564 makersposts, mediaan 1, p90 11, 88 (3,4%) haalden 50+. Bureaubladspellen: **Deskrawl "My Diablo like desktop idle game has a demo now!" 68 punten, 26 reacties** (16 jun, Next Fest-week); de rest 1 tot 6 (Cozy Mining 3, Pier Pals 5, HordeFall 4). Toppers: Defrag Incremental 198 ("lived on your desktop", een tweede post na kritiek uit de eerste: "You were right"), Lowmoor 190 ("I posted the first browser version here in July"), Dwarven Digging Machine 381 (gratis webdemo, vraagt feedback), Harvest Dice Profit 479 (verhaal van een streamer die het speelde) | Demodag of festweek; daarna 30 dagen later een "wat we veranderden"-post |
| **r/CozyGamers** | 242.012 | Flair Game Developer; **1 post per 30 dagen, alleen op woensdag (UTC)**; alleen bijna af of af; naam, uitgebreide beschrijving en links verplicht; geen "would you play this?"; milde gevechten mogen | 1 jun tot 1 okt: 1.308 makersposts, 976 daarvan op woensdag. Mediaan 1, p75 14, p90 65, 94 haalden 100+. Bureaublad: **Dejinochi "cozy virtual pet game that lives on your desktop" 302** (23 sep), idle-kat 91, Blubbi 71, desktop pet 66, Little Writer 60, Gloombo 38, Hocus Focus 32. Toppers zijn weggeefacties bij de release (Cat Isle 3.114 punten en 1.519 reacties, Bottled By Bears 2.197 en 1.166) | Woensdag, ±14:00 tot 16:00 UTC (GOK, Amerika wakker) |
| **r/cozygames** | 38.679 | Een spel hooguit 1 keer per 2 weken; kleine updates horen elders | 1 jun tot 1 okt: 1.760 posts, waarvan 1.174 met flair "My Game"; **mediaan 6** (vriendelijker dan de grote). "I'm making a game about sorting files on a messy desktop" 303 (5 sep), Cat Isle-weggeefactie 363 | Na r/CozyGamers, minstens 2 weken tussen posts |
| r/indiegames | 226.590 | Beeld van het spel verplicht; geen vraag in de titel van een promopost; geen feedback vragen op winkelpagina of trailer | 141 posts met "desktop" (mei tot okt): mediaan 1. Uitschieter: "A tiny aquarium that lives on your desktop. People are now trading the fish on Steam." 61 | Lage prioriteit |
| r/IndieGaming | 377.234 | Reddit-regel 10% eigen werk (wiki "spam") | 100 posts met "desktop": mediaan 1, top 119 (een vraag om ideeën); 14 posts met "taskbar": mediaan 0, top 12 | Niet de moeite |
| r/playmygame | 102.650 | Alleen gratis speelbaar of demo, directe link, zelf meepraten | niet gemeten | Demodag, als extra |
| r/pcgaming | 3.785.803 | Ontwikkelaars moeten eerst geverifieerd worden | niet gemeten | Alleen na verificatie |

Wat de goede makersposts gemeen hebben (GEZIEN, 12 toppers gelezen): een bewegend beeld (GIF of video), iets wat je meteen gratis speelt, één zin wat het spel is en waar het zit, en vaak een **tweede post die laat zien wat er na de eerste veranderde**. Weggeefacties trekken de meeste reacties, maar ons lanceerplan zegt "geen weggeefactie op Reddit of Discord rond de lancering" (`lanceerplan.md` punt 2). Dat laat ik staan; het is wel een nieuw feit voor Sem: op r/CozyGamers mag een weggeefactie op woensdag, met voorwaarden binnen de subreddit (geen "wishlist om mee te doen").

Nieuwsbrieven en lijsten voor Hats: de makers- en curatorlijsten van Sem dekken dit. Nieuw gevonden en klein: incrementaldb.com (database van idle-spellen, gratis vermelding met account; staat al bij Sem als laag). Een awesome-lijst voor idle- of bureaubladspellen bestaat niet in bruikbare vorm (zoeken op GitHub: hooguit 2 sterren).

### Click Joints (3D-printen en Blender)

| Plek | Grootte | Regels | Wat het deed | Wanneer |
|---|---|---|---|---|
| r/blender | 1.271.346 | Niet-gratis met flair "Non-free Product/Service"; niets verbergen | Bekend (Joris, Chris). Onze post 16 nov: 2 punten | Volgende alleen met een nieuwe versie die het melden waard is |
| r/3Dprinting | 2.940.796 | Minder dan 10% eigen werk, meedoen met anderen; lijst met verboden sites | Bekend: "ik heb een tool gemaakt" mediaan 2, 6 van 13 weggehaald | Alleen met een echte print |
| **r/customactionfigures** | 13.170 | Zijbalk: "Just post it anyway"; geen verbod op zelfpromotie | Bekend: joint-add-on van $12, 88 punten met een vraag en zonder link | Eerste plek zodra er een print is |
| **r/BambuLab** | 217.767 | Eigen modellen van MakerWorld mogen met flair "Self Designed Model"; betaald hooguit 1 per week; foto van het geprinte model verplicht; geen affiliate | niet gemeten | Na de eerste print, met het model op MakerWorld |
| r/functionalprint | 493.482 | Geen platte zelfpromotie; makers mogen delen als het iets toevoegt en ze meepraten | niet gemeten; figuren zijn hier geen "functioneel" onderwerp | Niet |
| r/PrintedMinis | 135.926 | Alles wat je verkoopt alleen op vrijdag | niet gemeten | Alleen als het over minifiguren gaat |
| r/BJD | 28.915 | Eén nieuwsbericht per uitgave met flair [news]; AI-filters verboden | niet gemeten | Niet (poppen, geen printers) |
| r/3Dmodeling | 1.393.798 | Geen reclame voor betaalde dingen; gratis bronnen welkom | niet gemeten | Gratis versie, met beeld |
| r/ActionFigures, r/blenderhelp | 171.041 en ? | Geen zelfpromotie | | Niet |

YouTube, wie zulke add-ons laat zien (GEZIEN, YouTube-zoekpagina's 18 nov):
- **Lijstkanalen voor nieuwe en gratis add-ons**: InspirationTuts "Free Blender Modeling Addons in 2026" 51.001 weergaven (1 maand oud), "New Blender Modeling Addons in 2026" 43.730 (2 maanden), "Free Blender Animation Addons in 2026" 105.991; BlenderHub "Best New FREE Blender Addons in 2026" 17.377; Artinvader "Best Free Blender Addons in 2026" 4.794 (staat al in `commercie/blender-click-joints/makers.md`). InspirationTuts maakt elke maand zulke lijsten per soort; in `commercie/blender-click-joints/verspreiding.md` staat het kanaal als "later" (51.500 abonnees), maar niet in `makers.md`. Nieuw is dat een lijst daar 2 tot 3 keer zijn abonneetal haalt, en dat BlenderHub erbij kan. Zakelijk adres niet gelezen (YouTube-over-pagina vraagt JavaScript).
- **Eigen video's van kleine add-on-makers voor 3D-printen**: 3DRedBox "Dovetail Key, Cut & Join Any Mesh for 3D Printing" 29.811 (4 maanden), xideaa "CutMode, FREE Blender Add-on" 11.209 (4 maanden), SierraVisualLab Split & Pin Pro 1.330, Blender Procedural SPLIT IT 1.412, Nunn Breakable "Blender Auto Joints" 619. Een eigen video kan dus 10.000+ halen als het woord in de titel staat ("Cut & Join", "FREE").
- **Figuurmakers**: Skillful Toys "How to Make a Ball Joint for Action Figures" 4.860 en "Blender from Scratch for Action Figures" 10.744 (precies onze gebruiker), ZeroDotCMD "How To Design Articulating 3D Prints" 48.734, Print That Thing "Ball Joints in Blender (EASY)" 28.783 (4 jaar oud, nog steeds bovenaan bij "blender addon ball joint").

Lijsten en nieuwssites:
- **awesome-blender** (7.684 sterren): Click Joints staat erin (zie boven). Betaalde add-ons alleen als ze "widely recognized" zijn, dus Pro niet aanmelden. Eén bron per pull request.
- **awesome-3d-printing** (2.105 sterren): eist sinds 2 nov 2026 dat een project **minstens 4 maanden** bestaat en **100 sterren of onafhankelijke aandacht** heeft (geen eigen tekst), en dat je zegt dat het van jou is. Click Joints kan op z'n vroegst rond 10 mrt 2027, en het BlenderNation-stuk telt niet (geschreven door ons).
- **BlenderNation**: gratis voor gratis add-ons; commercieel alleen met hun Patreon "Commercial Blender User" of **€ 25 per bericht** (GEZIEN, formulier). Ze maken ook verzamelstukken ("3D Print Suite: 18 Blender add-ons for 3D printing", 10 nov 2026).
- **blender-addons.org**: gratis catalogus met knop "Submit addon" (GEZIEN); BlenderNation raadde hem in 2021 aan als vaste vindplek (DERDEN).
- **CG Channel**: wekelijks "New CG software you may have missed", vooral grotere programma's (GEZIEN 15 nov); de lijst met Black Friday-acties neemt aanvragen aan ("Find out how to send in an offer"). Of een kleine add-on erin komt: GOK, waarschijnlijk niet.
- **Hackaday**: schreef over Blender-plugins (CAD Sketcher 2022, printplaatsporen 2021, GEZIEN via hun zoekpagina). Alleen zinvol met een echte print in beeld.

### Bison & Flex (Bison/Flex in CLion en IntelliJ)

| Plek | Grootte | Regels | Wat het deed | Wanneer |
|---|---|---|---|---|
| **JetBrains Marketplace zelf** | grootste bron | "New plugins" staat **op volgorde van de laatste upload** (GEZIEN, `plugins-ranking.html`); zoeken weegt downloads met log10(1 + 5 x downloads) | Zoekplek "bison" 2, "yacc" 3 (Chris, 17 nov) | Elke versie |
| **r/Compilers** | 25.339 | Geen regel over zelfpromotie in de API (wel lezen in de browser, zoals Chris vraagt) | 1 nov 2025 tot 20 okt 2026: 1.910 posts, mediaan 3; 145 posts over eigen werk, mediaan 1, **45 (31%) haalden 10+**, top 225. Gereedschap: "i made my own programming language in C + Flex" 12, "Bison-ish parser generator for Rust, and just added LSP support" 11, "Antlr is very very very slow" 20 punten en 22 reacties | Staat al op dag 2 tot 3 bij Chris |
| **r/Jetbrains** | 19.477 | Geen regels in de API | Sinds jun 2025: 79 posts over een eigen plugin, mediaan 2. Toppers hebben één vorm: **"I built a JetBrains plugin that [doet X]"**: 157 (verbergt geheimen), 83 (Poof-animatie), 43 (tabs per map); "Sticky Project View plugin is here" 138 | Staat bij Chris na dag 14 |
| r/IntelliJIDEA | 21.031 | idem | 52 posts over een eigen plugin, mediaan 1, top 14 | Niet |
| r/ProgrammingLanguages | 107.558 | Alleen taalontwerp; geen moeiteloze posts; weert AI-projecten (Chris) | 262 posts over eigen werk, mediaan 1; gereedschapstitels mediaan 1 | Niet |
| r/cpp | 308.809 | **Persoonlijke projecten alleen in de vaste draad "Show and Tell"** | niet gemeten | Alleen in die draad |
| Show HN | | | Bekend (Vera): plugins mediaan 1. Een parsergenerator haalde wel 33 punten (Yantra, 1 okt 2026), een plugin niet | Niet |
| Stack Overflow | vragen per tag: bison 2.644, flex-lexer 2.126, yacc 1.933, lex 1.834 (GEZIEN, API) | Verbiedt door AI geschreven antwoorden | | Niet (zie Chris) |

Wie de gebruikers zijn (GEZIEN, YouTube): vooral **studenten in compilerpractica**. "Flex & Bison Tutorial: Part 1" 120.448 weergaven, "Install Flex and Bison on Windows & Run Lex and Yacc Files" 24.252 (1 jaar oud), UC Riverside CS152 Compiler Design 12.118, The Compiler Bro 33.780, Tsoding "Worst Way to Write a Parser" 54.743. Zoeken op "flex bison clion" geeft geen enkele video over een plugin.

Lijsten en nieuwsbrieven:
- awesome_jetbrains_plugins: bekend, issue in plaats van pull request (Chris).
- **awesome-compilers** (9.964 sterren): laatste wijziging 26 mei 2024 (GEZIEN, git log), dus een aanvraag blijft liggen. Niet doen.
- awesome-intellij (5 sterren): te klein.
- **Staff Picks**: aanvragen via een YouTrack-ticket, ook voor plugins die via de Marketplace betaald worden; downloads wegen het zwaarst (GEZIEN, `staff-picks.html`). Staat bij Chris voor april 2027.
- Busy Plugin Developers Newsletter (JetBrains, elk kwartaal): voor pluginmakers, de "Community Spotlight" gaat over uitleg voor makers, niet over plugins voor gebruikers (GEZIEN, Q3 2026). Geen route.

### Vergelijkingssites
- AlternativeTo: vanuit de cloud niet te lezen (403, Cloudflare). Iedereen kan er een app toevoegen (DERDEN, algemeen bekend, niet gecontroleerd). Waarde voor ons onbekend: GOK laag.
- Voor Steam-spellen geen vergelijkingssite gevonden die kleine spellen aanneemt; de lijstjes zijn YouTube, curatoren en fest-pagina's (Sem).

### Garmin (kort)
Niets nieuws: r/Garmin werkt als gratis duw van een paar reviews met "probleem van een groep + gratis proberen + codes voor de eerste 5" (Joris, 178 punten tegen 0 voor dezelfde wijzerplaat met een andere kop).

---

## 2. Per product: de 3 acties met de meeste kans

### Hats
1. **r/incremental_games op de demodag (ma 4 jan) of in de festweek (14 jan)**, met een GIF van de strook op de taakbalk, één zin "idle [soort] that lives on your taskbar", de gratis demo, en het verplichte AI-blok. Waarom: dit is de plek van idle-spelers; het enige bureaublad-idle-spel met een gewone post haalde hier 68 punten in de Next Fest-week (Deskrawl, nu een winnaar). 30 dagen later een tweede post "wat we veranderden na jullie feedback" (Defrag 198, Lowmoor 190). **Eerst nodig:** Thijs kiest de tekst van het AI-blok, of zegt "sla over".
2. **r/CozyGamers op een woensdag en r/cozygames twee weken later**, rond de demo. Waarom: bureaubladmaatjes halen op r/CozyGamers 30 tot 302 punten (p90 van alle makersposts 65), en r/cozygames is de vriendelijkste plek (mediaan 6). Gebruik de cozy kant (hoed, Gloop), want Hats heeft gevechten; "mild combat" mag. Niet vóór de demo: alleen "near or completed games".
3. **Lijstmakers op de paginadag en bij de demo**, volgens de lijst van Sem (Easily Distracted Games, Indie Game Joe en de rest). Niets nieuws aan toe te voegen; dit blijft de grootste hefboom (hoofdles 4).

### Click Joints
1. **Eerste echte print, dan één post met de print in beeld**: r/customactionfigures (vraag stellen, geen link, zoals de post van 88 punten) en hetzelfde model op MakerWorld met een post in r/BambuLab onder "Self Designed Model". Waarom: printplekken belonen de print, niet de tool (TrailPrint3D 400 tot 2.500 punten, Joris), en r/BambuLab laat eigen modellen uitdrukkelijk toe. Tot die print niets beloven (besluit 17 nov).
2. **InspirationTuts en BlenderHub benaderen voor hun maandlijst van nieuwe gratis add-ons**, met een clip van 20 seconden. Waarom: hun lijsten halen 17.000 tot 106.000 weergaven en ze zoeken elke maand nieuwe gratis add-ons; Click Joints Free is gratis en staat nu bij BlenderNation (bewijs dat hij echt is). Mail via de hoofdchat na ja van Thijs. InspirationTuts staat bij Chris op "later"; ik zou het naar nu halen en toevoegen aan `commercie/blender-click-joints/makers.md`.
3. **blender-addons.org aanmelden** (gratis, vaste catalogus, één keer) en bij de volgende gratis versie die het melden waard is weer BlenderNation (gratis). Een BlenderNation-bericht over Pro kost € 25: alleen doen samen met de korting in de Cyber Sale (voorstel aan Thijs; verwachte opbrengst GOK: een paar verkopen van $9 tot $12, dus net quitte).

### Bison & Flex
1. **Elke 2 tot 3 weken een kleine versie uploaden.** Waarom: elke upload zet de plugin bovenaan de lijst "New plugins" in de Marketplace (GEZIEN in de docs), en de Marketplace is de grootste bron. Dit is gratis en loopt via de bestaande workflow.
2. **r/Compilers volgens het plan van Chris, en r/Jetbrains in de vorm "I built a JetBrains plugin that jumps from a Flex token to its Bison %token"**, met een GIF van die sprong. Waarom: 31% van de posts over eigen werk op r/Compilers haalt 10+, en op r/Jetbrains halen alleen posts in die vorm 43 tot 157. Op r/cpp alleen in de draad "Show and Tell".
3. **Studenten bereiken**: één korte video "Flex and Bison in CLion: highlighting and jump between scanner and grammar", met "flex bison" en "clion" in de titel. Waarom: de gebruikers zijn studenten die op YouTube zoeken hoe ze Flex en Bison aan de praat krijgen (24.252 weergaven voor een installatievideo van een jaar oud), en er is geen enkele video over een plugin. Samen met een studentenkorting (al gemeld door Chris). Opbrengst GOK.

### Garmin
Niets nieuws boven op Joris; licht houden.

---

## 3. Wat te automatiseren is

| Wat | Hoe | Kost | Wat Thijs één keer doet |
|---|---|---|---|
| **Postkalender per subreddit** | Een klein script in onze repo met per plek de regel (r/CozyGamers: woensdag UTC, 30 dagen; r/cozygames: 14 dagen; r/incremental_games: 30 dagen en speelbaar; r/BambuLab: foto, 1 per week) en de datum van onze laatste post uit `geplaatst.md`. Het zet "mag vanaf [datum]" met de klaargezette tekst naar de hoofdchat, die het op de lijst van Thijs zet. Klaar voor goedkeuring, nooit zelf plaatsen | € 0 | Niets; hij plaatst zelf |
| **Meting na elke post** | Arctic Shift `posts/ids` en `comments/tree` op 24 en 48 uur, naast de downloads (Blender API, Marketplace-API, Steam). Chris doet dit al met de hand; als script in Vera's `reacties-script.py`. Rustig vragen (een paar seconden tussen verzoeken), anders "Timeout" | € 0 | Niets |
| **Wie noemt ons** | Per subreddit zoeken op titel (`title=` werkt, zoeken in de tekst gaf time-outs) in r/blender, r/3Dprinting, r/customactionfigures, r/Jetbrains, r/Compilers, r/incremental_games, r/CozyGamers; Hacker News via Algolia; BlenderNation en blender-addons.org met curl. Eén keer per dag, uitkomst in een bestand | € 0 | Niets |
| **Elke versie: winkel en "New"-lijst** | Bestaande uitbreng-workflows (Blender Extensions, JetBrains `publishPlugin`). Bij JetBrains komt de plugin daarmee vanzelf bovenaan "New plugins" | € 0 | Niets extra |
| **Elke versie: changelog naar BlenderNation** | Niet automatisch in te sturen (formulier, geen API). Wel automatisch klaar: bij een gratis versie met een nieuwe functie maakt de skill `update-tekst` de tekst plus beeld van 1456x672; de hoofdchat stuurt in na ja van Thijs. Alleen bij een versie die het melden waard is (les This Week in Obsidian) | € 0 (gratis versie) | Ja op de tekst |
| **awesome-lijsten** | Eenmalig, geen vaste inzending per versie. Pull request met `gh` voorbereiden; de hoofdchat dient in onder het account van Thijs na zijn ja. awesome-3d-printing pas als de agenda op 10 mrt 2027 staat en er onafhankelijke aandacht is | € 0 | Ja op de tekst |
| **Korte filmpjes** | Metricool `createScheduledPostForReview` (andere agent) | volgens dat voorstel | |

Niet te automatiseren: Reddit plaatsen (Thijs zelf), mails aan makers (onder zijn naam), Steam-aankondigingen (geen openbare API gevonden om ze te plaatsen; GOK, niet verder gezocht).

---

## 4. Wat niet werkt of te duur is
- **r/IndieGaming en r/indiegames voor Hats**: posts met "desktop" mediaan 1, met "taskbar" mediaan 0. Alleen een rare haak breekt door (aquarium met handel in vissen, 61).
- **r/ProgrammingLanguages, r/IntelliJIDEA en Show HN voor Bison & Flex**: mediaan 1. r/cpp buiten "Show and Tell" wordt weggehaald.
- **awesome-compilers** (stil sinds mei 2024), **awesome-intellij** (5 sterren), **awesome-3d-printing vóór maart 2027**.
- **Busy Plugin Developers Newsletter** en **CG Channel's weekoverzicht**: bereiken geen kopers van kleine plugins of add-ons.
- **r/blenderhelp, r/ActionFigures, r/functionalprint**: zelfpromotie verboden of past niet.
- **Een render of film op een printplek** zonder echte print: misleidend en tegen ons besluit.
- **Weggeefacties die om een verlanglijst vragen**: op r/CozyGamers verboden, en in strijd met ons lanceerplan.
- **Stack Overflow**: verbiedt door AI geschreven antwoorden.
- **BlenderNation-bericht voor Pro buiten een actie**: € 25 voor naar verwachting minder dan dat aan verkopen (GOK).

## Bronnen (alle opgehaald 18 nov 2026)
- Arctic Shift: `https://arctic-shift.photon-reddit.com/api/subreddits/rules?subreddits=<naam>`, `.../api/subreddits/wikis?paths=/r/CozyGamers/wiki/guide`, `.../api/posts/search?subreddit=<naam>&after=...&before=...`. Aankondiging AI-regel r/incremental_games: post-id `1tublm5` (2 jun 2026).
- awesome-blender en awesome-3d-printing: `git clone` van github.com/agmmnn/awesome-blender en github.com/ad-si/awesome-3d-printing (CONTRIBUTING, README, git log).
- JetBrains: https://plugins.jetbrains.com/docs/marketplace/plugins-ranking.html en https://plugins.jetbrains.com/docs/marketplace/staff-picks.html.
- BlenderNation: https://www.blendernation.com/submit-news/ en het artikel hierboven. blender-addons.org voorpagina.
- Stack Overflow: `api.stackexchange.com/2.3/tags/bison;flex-lexer;yacc;lex;antlr/info`.
- Hacker News: `hn.algolia.com/api/v1/search?tags=show_hn&query=...`.
- YouTube: zoekpagina's met curl (weergaven zoals YouTube ze toont op 18 nov).
