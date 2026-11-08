# Obsidian: volgend product (in onderzoek, nog geen voorstel)

Opdracht: bericht Thijs 8 nov 14:37 en het blok "Het volgende product" in `organisatie/rollen/platformmanager.md`. Hans beslist; zonder zijn ja niet bouwen. Rollwright gaat elke run voor.

## Aanvulling 8 nov 15:35 UTC (Olaf): klachten en gaten, eerste blik

Reddit geeft 403 vanaf hier (GEZIEN); het forum werkt. Er is weinig klachtenvolume in het forum, dus nog geen hard bewijs uit verzoeken. Wat ik wel vond (alles GEZIEN, 8 nov):
- **Fantasy Statblocks heeft geen opmaak voor D&D 2024.** In de code (laatste stand, 21 jan 2026) staan layouts voor basic 5e, Pathfinder 2e, 13th Age, Daggerheart, Fate Core en Bunkers and Badasses; nergens "2024" of "5.5" in `src/`. Forumdraad 103462 "Fantasy Statblock 5.5 2024 Layout" (30 jul 2025): 1.849 keer bekeken, gebruiker vraagt de nieuwe Monster Manual-opmaak. Draad 96755 (andere opmaak van de vaardigheden): 224 keer bekeken. Gebruikers kunnen zelf een layout maken, dus dit is een gemak, geen muur.
- Kleine concurrenten voor 2024: Compendio SRD 2024 (121 downloads totaal), One DnD Character Sheet (258), The DM Compendium (3.016 totaal, 587 per maand; 2014 of 2024 niet nagekeken).
- **Initiative Tracker is lastig in te stellen voor nieuwe gebruikers.** Draad 115148 (jun 2026, 341 keer bekeken): spelers koppelen via frontmatter lukt een beginner niet, na zes berichten nog niet opgelost. Eén draad is geen markt, wel een aanwijzing.
- **Nieuwe concurrent die op Rollwright lijkt:** wickedcreativesystems bracht eind oktober vier kleine plugins uit (Dice Tray 100, Quick Initiative 55, Encounter Builder 42, Session Log 28 downloads; forumdraad 119937, 54 keer bekeken). Dice Tray leest ook de `dice:` notatie van Dice Roller. Quick Initiative leest HP, AC en Dex uit Fantasy Statblocks. Zij bouwen dus precies het pakket rond dobbelen, initiatief en sessielog. Voor Rollwright en voor kandidaat 1 een concurrent om te volgen.

**Stand van de kandidaten:** kandidaat 2 krijgt een scherpere vorm: monsterkaarten in de opmaak van D&D 2024 met het gratis SRD 5.2 erbij (licentie CC-BY-4.0 nog na te lezen, DERDEN te verzamelen), werkt samen met Rollwright (aanvalsworpen klikbaar). Kandidaat 1 (initiatief) heeft nu een directe nieuwe concurrent. Volgende ronde: hoeveel van de 26.171 statblocks-downloads per maand gaan naar de laatste versie (nieuwe installaties tegenover updates, uit de stats per versie), licentie SRD 5.2 lezen, en kijken of Obsidian-gebruikers D&D 2024 al massaal spelen (DERDEN).

## Stand 8 nov 15:20 UTC (Olaf, tweede ronde): groei gemeten, richting TTRPG

Nog geen voorstel voor Hans. Wel een duidelijke vernauwing. Nagekeken door een controleur: alle losse cijfers klopten; vijf punten (te sterke zinnen over kanban en kalender, tellingen op ingekorte tekst) verwerkt.

**Nieuwe bron, geen wachten meer nodig:** de repo obsidianmd/obsidian-releases slaat `community-plugin-stats.json` elke dag op als commit. Met `git clone --filter=blob:none` (werkt, de GitHub-API niet) heb ik de stand van 8 nov 2026, 9 okt 2026, 10 aug 2026 en 8 nov 2025 opgehaald. Daarmee is de groei per plugin over 30 en 90 dagen GEZIEN, voor alle 10.082 plugins. Uitkomst: `metingen/groei-2026-11-08.csv` (plugins met 1000+ downloads), script `metingen/scripts/groei.py`. Alle cijfers hieronder: GEZIEN in die bestanden, "per maand" is de groei van 9 okt tot 8 nov.

**Richting 3 (verlaten reus) en richting 2 (Bases-weergaven) vallen grotendeels af: Obsidian zelf overlapt ze steeds meer.**
- Kanban groeit nog 90.466 per maand terwijl de laatste versie 890 dagen oud is. Maar Obsidian 1.14 heeft een eigen kanbanweergave in Bases (GEZIEN in https://obsidian.md/changelog/: "a kanban view for Bases"; forumdraad 117910 spreekt van "the new Kanban Base View"). Die werkt op eigenschappen van notities, de plugin op Markdown-borden, en gebruikers vragen nog om handmatig sorteren binnen een kolom. Dus: overlapt grotendeels, vervangt niet alles. Toch geen plek voor ons: tegen een gratis weergave van Obsidian zelf verdien je niets.
- Calendar groeit 82.546 per maand (2027 dagen oud). Een "Calendar view for Bases" staat op https://obsidian.md/roadmap/ onder Planned (GEZIEN), nog niet gebouwd. De Calendar-plugin is een navigator voor dagnotities in de zijbalk; of de geplande weergave hem vervangt is een GOK. Opvolgers zijn er al (Calendar Bases 9.351, Full Calendar Remastered 7.830 per maand). Voor nu niet verder.
- Highlightr groeit 13.569 per maand, maar 1.14 heeft zelf "highlight colors" (GEZIEN, changelog).
- Bases-weergaven: ruwe telling 236 plugins die "base" of "bases" noemen in naam of omschrijving (ook treffers als "knowledge base"), samen 244.507 per maand. Kanban heeft Obsidian al, een kalender is gepland, en de hoek loopt snel vol: 118 van de 222 die ik eerst telde bestonden 90 dagen geleden nog niet. Een plugin daar kan door één update van Obsidian overbodig worden. Nee, tenzij een weergave die Obsidian zeker niet bouwt.
- Style Settings (80.941 per maand) en Remotely Save (72.842) zijn ook oud, maar geen product dat geld oplevert en geen open plek (thema-makers en sync hebben veel opvolgers). Niet verder.

**Richting 1 (TTRPG) blijft over en is sterker dan gedacht.**
- Ruwe telling: 149 TTRPG-plugins samen 134.014 downloads per maand (zoekwoorden ttrpg, d&d, statblock, initiative, dice, campaign enzovoort, op naam en volledige omschrijving; er zitten een paar losse treffers tussen). Let op: de omschrijving in `groei-2026-11-08.csv` is ingekort tot 120 tekens, wie daarop telt komt lager uit.
- De grote plugins van dezelfde maker (Javalent; Statblocks, Initiative Tracker en Dice Roller zijn nu ondergebracht bij de organisatie obsidian-ttrpg-community, Calendarium staat nog onder javalent) staan stil. Commits GEZIEN via `git clone`:
  - **Fantasy Statblocks**: 371.581 totaal, **26.171 per maand** (grootste groeier van alle TTRPG-plugins), laatste commit 21 jan 2026, 0 commits in de laatste 180 dagen.
  - **Initiative Tracker**: 165.736 totaal, 2.961 per maand, laatste commit 13 apr 2026, 0 commits in 180 dagen.
  - **Dice Roller**: 289.111 totaal, 3.999 per maand, laatste versie 593 dagen oud (onze eerste keuze, Rollwright).
  - Calendarium: 202.146 totaal, 5.795 per maand, laatste commit 26 sep 2025.
- Nieuwe spelers groeien hard, dus de vraag is echt, maar het is ook druk: Atlas VTT (gevechtskaarten, 13.610 per maand, nieuw), TTRPG Tools - Maps (12.407 per maand), Relations (3.322), Combat Ledger (1.312 per maand, een nieuwe gevechtsteller die eigenschappen uit je notities leest), Sheetsmith (karakterbladen, 1.015 in de eerste weken).
- Voordeel voor ons: zelfde spelers als Rollwright, dus winkeltekst, Polar, publiceer.sh en de e2e-test herbruikbaar, en de producten kunnen elkaar versterken (een gevechtsteller die Rollwright gebruikt om initiatief te gooien).

**Kandidaten voor de derde ronde (nog geen keuze, GOK tot bewezen):**
1. **Opvolger van Initiative Tracker** (gevechtsvolgorde, levenspunten, toestanden), samen met Rollwright. Vraag: 2.961 + 1.276 (Generic Initiative Tracker, 1743 dagen oud) + 1.312 (Combat Ledger) per maand. Kleiner te bouwen dan statblocks.
2. **Statblocks** (monsterkaarten en bestiarium). Grootste vraag (26.171 per maand) maar groot om te bouwen, en per spelsysteem zijn er al nieuwe (PF2e Statblocks 1.531, Beastvault voor Daggerheart 655, The DM Compendium 587 per maand). De bestaande werkt nog; stilstaan is niet hetzelfde als kapot.
3. **Iets wat nog niemand doet** voor spelleiders, uit de klachten en verzoeken.

**Wat nog ontbreekt voor een voorstel (de regel "markt bewijzen"):** klachten en verzoeken. GitHub-issues van anderen zijn vanuit onze omgeving dicht (403 op api.github.com en op github.com, GEZIEN). Het forum werkt wel (`forum.obsidian.md/search.json`, GEZIEN). Volgende stap: in het forum en op Reddit (r/ObsidianMD, r/DMAcademy) zoeken naar klachten over Initiative Tracker en Fantasy Statblocks, en per kandidaat de drie sterkste concurrenten uitlichten met wat ze missen. Ook nagaan welk deel van de 26.171 statblocks-downloads nieuwe gebruikers zijn en welk deel updates (de stats tellen per versie).

**Let op voor Rollwright (GEZIEN):** Dice Roller krijgt nog 3.999 downloads per maand (±130 per dag), Rollwright staat na een dag op 4 (communitypagina https://community.obsidian.md/plugins/rollwright, GEZIEN 8 nov 15:15 UTC met curl). Rollwright staat nog niet in `community-plugin-stats.json`. Bereik hangt dus vooral van vindbaarheid af; dat zet ik in de status voor Chris en Hans.

## Stand 8 nov 14:45 UTC (Olaf, eerste ronde)

Nog geen keuze. Wat er nu ligt is een lijst om verder uit te zoeken, geen bewijs van vraag.

**Bron:** `community-plugin-stats.json` en `community-plugins.json` uit obsidianmd/obsidian-releases (GEZIEN 8 nov 14:35 UTC, 10.082 plugins). Momentopname van alle plugins met 10.000+ downloads: `metingen/plugin-stats-2026-11-08.csv`. Door die meting over een paar dagen te herhalen zie ik per plugin hoeveel downloads er per dag bij komen (GEZIEN), ook zonder GitHub-API (die is in onze omgeving dicht voor repo's van anderen).

**Veel gebruikt, lang niet bijgewerkt (laatste versie meer dan 2 jaar oud, GEZIEN):** Calendar 3,26 mln (5,6 jaar), Style Settings 2,83 mln, Kanban 2,82 mln, Mind Map 907k (5,9 jaar), Advanced Slides 842k (3,7 jaar), Periodic Notes 797k, Highlightr 748k (4,2 jaar), Pandoc 567k, Full Calendar 475k (3,6 jaar), Banners 361k, Charts 336k (2,8 jaar), Leaflet 320k (2,6 jaar).

**Maar vaak is er al een opvolger (GEZIEN, zelfde bron):** Mind Map heeft Mindmap NextGen (135k, nu bijgewerkt) en Markmind (625k); Advanced Slides heeft Slides Extended (52k, fork) en Advanced Canvas (988k); Banners heeft Pixel Banner (196k) en Pretty Properties (372k); Full Calendar heeft Full Calendar Remastered (57k); Leaflet heeft TTRPG Tools - Maps (`zoom-map`, 95k); Charts heeft Charts View (99k) en voor Bases al Bases Charts (30k) en Bases Chart Views (17k).

**Richtingen voor de volgende ronde (GOK, nog te bewijzen):**
1. **Iets voor dezelfde spelers als Rollwright** (TTRPG): kopers en publiek delen, winkeltekst en Polar hergebruiken. Te meten: groei van TTRPG-plugins (Leaflet, zoom-map, Initiative Tracker, Fantasy Statblocks, Dice Roller) per dag, en open verzoeken met veel duimen bij Javalent-plugins.
2. **Weergaven voor Bases** (kern-functie van Obsidian sinds 2025): een jonge hoek waar de eerste plugins snel groeien. Te meten: groei per dag van alle plugins met "Bases" in naam of tekst.
3. **Verlaten plugin zonder sterke opvolger**: per kandidaat nagaan of er echt geen goede opvolger is (Highlightr, Periodic Notes, Style Settings, Kanban) en wat gebruikers missen (issues met veel duimen, via github.com in de browser of zoeken).

**Volgende stap:** over 1 tot 3 dagen dezelfde meting, groei per plugin uitrekenen, dan per richting de 3 sterkste concurrenten, open verzoeken en klachten, en een voorstel van één pagina. Controleur loopt het na, dan naar Hans in `berichten/hans.md`.
