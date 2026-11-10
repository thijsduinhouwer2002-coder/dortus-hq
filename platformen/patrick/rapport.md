# Rapport Patrick, perfectionist (nacht 9 op 10 nov 2026)

Stand: run 2 (10 nov, ±01:45 NL). Runs van 03:13 en 05:13 controleren en schaven; na 05:13 is dit de versie voor Thijs om 08:00.
Bewijs: `bevindingen.md`. Bronnen van buiten (33 lessen, met links): `bronnen/internet.md` en `bronnen/toegang-ruw.md`. Volledige teksten om over te nemen: `voorstellen/01` tot `12`.

## Voor Thijs: vijf keer ja of nee (±3 minuten), daarna 5 minuten werk
1. Koerszin "eerst de eerste eerlijke euro, daarna spreiden" (hieronder): ja / nee.
2. Ploeg op de eerste euro (punt 1): Bram terug naar Click Joints, Klopt stil tot de KvK-datum, 6 Claudes elk uur: ja / nee. Plus één datum: wanneer verwacht je de KvK?
3. Hoofdchat beslist, Hans controleert één keer per dag, ploeg verandert alleen om 09:00 en 21:00 (punt 4): ja / nee.
4. Kansen kiezen op verwachte euro's per week werk in plaats van de 8-meetlat (punt 4): ja / nee.
5. dortus-hq privé maken (zie "Ook belangrijk"): ja / nee.
Werk: één Polar-sleutel die alleen kan lezen (punt 2, 5 minuten). De rest (punt 3 en 5) voert de hoofdchat zelf door.

## In één alinea
In drie dagen maakte de ploeg ±1.650 commits. Opbrengst: één product te koop (Rollwright, skins $6, 26 downloads), twee in keuring, €0 binnen, ±€1000 uitgegeven. Bouwen gaat goed. Wat niet goed gaat: het werk zit het meest bij producten waar de euro het verst weg is (TikTok: pas na de KvK; Steam: januari), en het minst bij wat binnen een week of twee te koop kan staan (Click Joints Pro, Garmin). Daarnaast leest elke run eerst ±100 KB, sturen drie lagen door elkaar, en ziet niemand in de ploeg of er iets verkocht is. De vijf punten hieronder lossen dat op.

## Vóór alles: één koerszin (keuze Thijs, 1 minuut)
Nu staan er vier koersen door elkaar (CLAUDE.md "gebruikers en later geld", projectbeschrijving "eerst bereik", `doelen.md` "geld gaat voor bereik", besluit 22:56 "echt geld nu"). Elke afweging leunt hierop. Advies: **"Eerst de eerste eerlijke euro, daarna spreiden. Bereik telt omdat het tot geld leidt: elk product is vanaf dag 1 te koop."** Uitwerking: `voorstellen/10-koers-in-een-zin.md`.

## Top 5

### 1. Zet de ploeg op de eerste euro (keuze Thijs, 1 minuut)
- **Wat er mis is.** Per product de vroegste euro (`voorstellen/12-eerste-euro.md`): Click Joints Pro binnen ±1 week als we alleen het scharnier verkopen via Polar (kassa staat al; scharnier staat op een tak, nog 1 tot 2 dagen werk plus Daan), Garmin-ademapp eind november, Bison & Flex half december (30 dagen proef na goedkeuring), Het Hol half januari, Klopt pas 4 tot 8 weken na een KvK die er nog niet is. Toch draaien Tess en Jet elk uur op Klopt, en zit Bram (de bouwer van Click Joints) op Steam als vijfde man.
- **Voorstel.** Elk uur: Olaf, Sanne, Mila (Steam), Bram (Click Joints Pro tot hij te koop staat), Gijs (Garmin), Daan (zijn akkoord is nodig om in te dienen). Klopt stil tot de KvK-datum vaststaat; Jet op afroep voor de lancering van Bison & Flex. Per product één kanaal om gevonden te worden: de ploeg schrijft de tekst, Thijs post hooguit één keer per week (5 minuten), want posten blijft bij hem. Geen nieuw platform tot er een euro binnen is. Elk product krijgt op het bord een "euro-datum"; schuift die twee keer, dan kleiner of stoppen.
- **Eerlijk over geld.** Minder Claudes bespaart zelf geen euro: het abonnement is vast. Het spaart weeklimiet en overleg. De echte kostenknop is een kleiner abonnement; meet na de reset (wo 21:00) een week en beslis dan. GOK, niet gemeten.
- **Oplevert.** Twee kansen op een euro in november in plaats van nul, zonder dat Steam trager gaat (de bouwer blijft).

### 2. Toegang met officiële sleutels (gewoon goed, Thijs ±5 minuten nu, ±40 later)
- **Wat er mis is.** Niemand in de ploeg ziet verkopen zonder Thijs, en elke Blender-update en Steam-build zou via hem lopen. Er zijn nu maar twee sleutels: JetBrains-upload en Moneybird-proef (GEZIEN in de workflows).
- **Voorstel** (`voorstellen/11-toegang.md`, wordt `organisatie/toegang.md`). Nu: Polar-token alleen lezen, de euro-meter voor iedereen, 5 min. Later: GitHub-token voor alleen `rollwright` en `click-joints` (de ploeg maakt een concept-release, de hoofdchat publiceert), Blender-token na goedkeuring (3 min), Polar-schrijftoken bij het tweede product, Steam-build-account in december (20 min, één keer inloggen met Steam Guard op Thijs' eigen computer, daarna alleen een bestand als secret). Niet: Steam-financiële sleutel (alleen met vast IP te beperken), Moneybird-hoofdsleutel (opent de hele administratie). Garmin heeft geen upload-API: elke upload blijft handwerk.
- **Regels.** Sleutels alleen als GitHub-secret per platform-environment, alleen in Actions bij push of met de hand, nooit in een bestand of bericht. Prijzen, live zetten, eerste inzending, profielen, voorwaarden, betalen en posten blijven bij Thijs of de hoofdchat, ook als een sleutel het technisch kan.
- **Bron.** Officiële docs van elk platform, met link per punt in `bronnen/toegang-ruw.md`; Polar-scopes nagekeken in hun broncode.

### 3. Elke run start met ±15 KB in plaats van ±100 KB, met één opdracht voor iedereen (gewoon goed, ±1,5 uur hoofdchat)
- **Wat er mis is.** De leeslijst staat op drie plekken en verschilt (CLAUDE.md, `platformmanager.md`, de opdracht van elke geplande taak). `besluiten.md` is 57 KB en groeit; `status.md` moet 10 regels zijn, praktijk tot 84. De geplande opdrachten spreken de besluiten tegen: Olaf krijgt elk uur nog "Thijs kiest eerst", Hans "nieuwe platformen zijn de hoofdzaak", Tess "elke 3 uur" (list_triggers, 9 nov 23:30). `geplande-taken.md` mist vijf taken.
- **Wat anderen doen.** Anthropic: CLAUDE.md onder 200 regels, langer geeft slechtere naleving; bij tegenspraak kiest Claude willekeurig; een geplande prompt moet op zichzelf staan (bronnen 1, 2, 7, 18, 27).
- **Voorstel.** CLAUDE.md wordt de enige startlijst met de harde regels (01). `organisatie/bord.md` is het ene bestand met wat nu geldt, hooguit 40 regels (02). `status.md` per map in vaste vorm met de volgende taak (03 B). Alle geplande taken krijgen dezelfde opdracht van ±12 regels (03 A). `regels.md` wordt naslag (07). Rollen verwijzen alleen nog naar CLAUDE.md (08).
- **Oplevert.** GOK: het begin van een run van ±25.000 naar ±4.000 tokens, en een besluit van Thijs werkt meteen overal door zonder 8 opdrachten aan te passen.

### 4. Eén beslisser, vaste momenten, en kiezen op euro per week werk (keuze Thijs)
- **Wat er mis is.** Hans, de hoofdchat en de compagnon-ronde sturen alle drie. Besluiten van Hans van 20:44 werden dezelfde avond omgedraaid (Garmin, Steam-geld); op 9 nov veranderde de ploeg zes keer. De meetlat eist vier dingen tegelijk voor een 8, dus kwamen er na ±170 platformen vooral zessen, en Thijs koos Steam toch.
- **Wat anderen doen.** Project Vend 2: een baas-agent van hetzelfde model "wasn't much help, and might even have been a hindrance" (bron 25). Shape Up: vaste beslismomenten, "bets are commitments" (bron 28).
- **Voorstel** (`voorstellen/05-ploeg-en-sturing.md`). De hoofdchat met Thijs beslist koers, ploeg en geld. Hans wordt één keer per dag de controleur (dagkaart van 10 regels: wie leverde niets, wat is verouderd, wat hangt). Ploeg en schema veranderen alleen om 09:00 en 21:00, behalve bij nood. Kansen kiezen we op één getal: verwachte euro's in 90 dagen (laag, middel, hoog, met bron) gedeeld door weken werk. Drempels zijn kosten, geen afwijzing. Controleur-agent alleen bij een ontwerp, iets dat naar buiten gaat, of een getal waar een besluit op rust.
- **Eerlijk over Thijs.** Om 18:30 snoeide Thijs om verbruik, om 21:15 was verbruik "nu niet belangrijk" en startte Garmin tegen het advies van de hoofdchat in. Spreiden is een goed doel, maar elke ommezwaai kost een paar runs uitleg en overdracht. Twee vaste momenten per dag geven Thijs dezelfde macht met minder ruis.

### 5. Thijs ziet in één blik de euro's, en zijn lijst past op één scherm (gewoon goed, ±1,5 uur)
- **Wat er mis is.** `lijst-thijs.md` is 82 KB met 61 doorgestreepte punten. Het dashboard toont "commits vandaag" als kopcijfer: drukte, geen uitkomst. Niemand ziet verkopen zonder in te loggen bij Polar.
- **Voorstel** (`04-lijst-thijs.md`, `09-dashboard.md`). Lijst: hooguit 5 punten in vaste vorm (wat, minuten, wanneer, waarom in één zin, stappen); afgehandeld gaat dezelfde dag naar het archief. Dashboard: bovenaan euro's binnen (uit de Polar-leessleutel van punt 2), betalende klanten en per product de euro-datum; per persoon de laatste uitkomst in plaats van het aantal commits.

## Hoe doorvoeren zonder dat de ploeg vastloopt
1. **09:00, met Thijs (5 minuten):** koerszin, punt 1 (ploeg), punt 4 (sturing en meetlat). Thijs maakt daarna de Polar-leessleutel van punt 2 (5 minuten).
2. **Eén commit** met `CLAUDE.md` (01), `organisatie/bord.md` met euro-datum per product (02 en 12), `organisatie/regels.md` (07), `organisatie/toegang.md` (11), de lees- en agentstap in de rollen (08), `organisatie/sjablonen/status.md` (03 B) en in elk berichtenbestand één regel "zet je status.md om naar het sjabloon".
3. Direct daarna de opdrachten van de geplande taken met update_trigger (03 A), het schema van punt 1, en `geplande-taken.md` (03 C).
4. `.gitignore` (06), `lijst-thijs.md` met archief (04), dashboard (09).
5. Let op bij stap 2: (a) Hans gaat in 01 en 02 het bord mee bijhouden; dat is een nieuw besluit, zet het in `besluiten.md`. (b) Maps zonder `status.md` (abel, hoofdchat, herweger, zijpad, patrick) krijgen er een uit het sjabloon of gaan naar `uit/`. (c) 01, 03, 04, 07 en 08 verwijzen naar elkaar en naar mappen die nog niet bestaan (`berichten/archief/`, `organisatie/archief/`, `organisatie/rollen/uit/`, `organisatie/sjablonen/status.md`): alleen samen doorvoeren.

Controle: een agent die de voorstellen niet schreef, legde de huidige CLAUDE.md en regels.md regel voor regel naast 01 en 07 (10 nov 00:30). Weggevallen grenzen zijn teruggezet (alle gegevens invullen, lezen en WebSearch, nooit uit logboeken weghalen, berichten aan een ander, afsluiten na fetch). Bewust losser, dus keuze voor de hoofdchat: code samenvoegen op groene tests zonder controleur (gewijzigde tests wel), en `besluiten.md` alleen lezen vóór een groot besluit.

## Ook belangrijk, niet in de top 5
- **dortus-hq is openbaar** (GEZIEN via de GitHub API, `"private": false`). Iedereen kan lezen: besluiten (Steamworks-account, partner-ID, mailadres, W-8BEN ingediend), lijst-thijs, logboeken, en elke log van Actions. Dat maakt phishing op Thijs makkelijker en laat concurrenten meelezen. Keuze Thijs: privé maken (2 minuten, Settings), dan moeten de ploeg en `regels.md` de testuitslag met `gh api` lezen in plaats van met kale curl (regels.md noemt dit al). Kan dat niet meteen: zet in elk geval geen account-, betaal-, ID- of klantgegevens meer in de repo.
- **Weeklimiet: niemand kijkt.** 55% op ma 13:40 (herinnering "Verbruik-check", nu uit), reset wo 21:00, daarna kwamen er vier Claudes bij. Raakt hij op, dan stopt alles tegelijk. Punt 1 helpt direct; noodknop: boven 85% alleen nog Olaf, Bram en Gijs elk uur.
- **Repo afslanken** (06). `.git` is 2,7 GB; een `.gitignore` voor ruwe data kost 10 minuten.
- **dortus.com draait op GitHub Pages** (GEZIEN). Volgens GitHub niet bedoeld voor een commerciële dienst; afrekenen gebeurt bij Polar, dus voor nu prima. Bij echte verkoop van Klopt naar Cloudflare Pages (11).
- **Eerst de regels van een plek lezen** voor je ergens iets plaatst (Reddit-ban bij Rollwright). Staat in 07.
- **Zes rollen staan uit.** Verplaats ze naar `organisatie/rollen/uit/`.
