# Bevindingen (werkbestand, met bewijs)

## A. Cijfers werkwijze (git log, 6 nov 22:00 tot 9 nov 23:20, GEZIEN)
- 1640 commits zonder merges in 3 dagen. 7 nov 390, 8 nov 774, 9 nov 561 (alle commits incl. merges).
- Per naam: Vera 248, Daan 210, Olaf 178, Noor 162, "Rollwright" 158, Jet 138, Bram 126, Click 68, Bison 52, Chris 48, Tess 25, Sanne 25, Kees 22.
- 325 commits (20%) raken alleen logboek, taken, berichten, lijsten of besluiten. Olaf 88 van 178, Jet 61 van 138, Bram 47 van 126.
- Opbrengst na 3 dagen: 1 product live (Rollwright, 19 downloads, 0 verkopen), 2 in keuring (Click Joints, Bison & Flex, 0 installs), 0 euro. Zoekers Vera plus Noor: 410 commits, ±60 platformen op één dag, uitkomst één nieuwe 7 (Garmin). Daarna door Thijs uitgezet (besluit 9 nov 18:30).
- Rollwright: drie versies op één dag via Thijs bij 19 downloads (besluit Hans 20:44 zegt dit zelf).

## B. Repo is te zwaar (GEZIEN)
- `.git` is 2,7 GB. `platformen/verkenner` 141 MB in 473 bestanden, `platformen/pionier` 34 MB. Grootste: moodle-pluglist 16 MB json, m365-apps 12 MB, fortnite 7 MB, en vele demo-GIF's van 7 tot 9 MB, deels dubbel (ontwerp/rollwright/v4/demo-v4-b.gif is gelijk aan producten/obsidian-rollwright/images/demo.gif, 8.854.557 bytes).
- Gevolg gezien in deze run: `git fetch` liep na 2 minuten vast (time-out), de kloon was ondiep (76 commits) zodat git log over 3 dagen eerst niets liet zien. Elke run van elke Claude betaalt hiervoor in tijd.

## C. Geplande taken: opdrachten verouderd en tegenstrijdig (GEZIEN via list_triggers 9 nov 22:30 UTC)
- 8 Claudes elk uur, dag en nacht: Olaf, Bram, Daan, Mila, Sanne, Gijs, Tess, Jet. Plus Hans 2x per dag. Dat is ±192 runs per dag.
- `organisatie/geplande-taken.md` is van 7 nov: mist Gijs, Mila, Kees, Lotte, Patrick; noemt Sanne en Tess "nog aan te maken"; schema Tess klopt niet (staat elke 3 uur, is elk uur). Regels.md zegt zelfs nog "Dortus-taken heten Stijn, Hans, Vera, Olaf, Jet".
- Olaf's opdracht zegt nog: "je neemt de rol van Sanne over... Eerst alleen de ideefase: drie richtingen... Thijs kiest". Achterhaald door besluit 19:00 (Sanne is game-ontwerper) en 19:20 (meteen bouwen).
- Hans' opdracht zegt: "Nieuwe platformen zijn nu de hoofdzaak: Vera en Noor leveren elke dag voorstellen". Zoekers staan sinds 18:30 uit. Hans krijgt dus een verkeerde prioriteit mee, elke run.
- Tess' opdracht: "Je eerste taak is bewijzen dat verkopers betalen; bouw pas na een ja van Hans" en "elke 3 uur": beide achterhaald.
- Herinnering "Na reset: Chris en Daan terug" (11 nov) bevat een bevroren stand ("alleen Olaf, Daan, Tess en Bram draaien"), die al twee keer is veranderd.
- Elke opdracht herhaalt ±1.500 tekens dezelfde vaste tekst (toestemming, add_repo, curl-zin, koppelingen, afsluiten), en elke opdracht noemt een eigen leeslijst. De leeslijst staat dus op drie plekken (CLAUDE.md, rol, opdracht) en loopt uiteen.

## D. Leeswerk per run (GEZIEN, bytes)
- Verplicht volgens CLAUDE.md en opdrachten: CLAUDE.md 0,9 KB, doelen 5,2 KB, regels 13,2 KB, besluiten 56 KB, rol 4 tot 8 KB, eigen berichten (Olaf 42 KB, Daan 32 KB, Bram 19 KB), plus de eigen map (steam 479 KB, jetbrains 938 KB). Ruim 80 tot 130 KB voor de eerste echte stap, ±20.000 tot 35.000 tokens, per run, 192 runs per dag.
- lijst-thijs.md is 82 KB, vooral doorgestreepte punten met hele alinea's.

## E. Besluiten draaien snel om (GEZIEN in besluiten.md, 9 nov)
- Op één dag zes besluiten over wie wanneer draait: nachtpauze, 18:30 alleen vier bouwers, 19:00 teams, 20:44 Garmin donderdag, 21:15 Garmin meteen, 21:20 Mila erbij. Garmin: hoofdchat adviseerde nee, Thijs ja ("verbruik nu niet belangrijk") terwijl dezelfde dag om 18:30 verbruik de reden was om te snoeien.
- 23:05: eis "oktobergroep 25%+" vervalt, $100 nu. Hans had 20:44 nog een 7 gegeven met die eis als voorwaarde.
