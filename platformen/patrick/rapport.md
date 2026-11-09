# Rapport Patrick, perfectionist (nacht 9 op 10 nov 2026)

Stand: versie na run 1 (9 nov, ±23:30 NL). Volgende runs scherpen aan; de run van 07:13 maakt hem af.
Bewijs: `bevindingen.md`. Bronnen van buiten (27 lessen, met links): `bronnen/internet.md`. Volledige nieuwe teksten om over te nemen: `voorstellen/01` tot `10`.

## In één alinea
In drie dagen (7 tot en met 9 nov) maakte de ploeg ±1.650 commits, samenvoegingen niet meegeteld. Opbrengst: één product live (Rollwright, 19 downloads, 0 verkopen), twee in keuring, 0 euro. Bouwen is niet het probleem: het Steam-team bouwt echt en snel. Wat traag en duur is: elke run leest eerst 80 tot 130 KB, de opdrachten van de geplande taken spreken de besluiten tegen, er sturen drie lagen die elkaars besluiten omdraaien, bij elke kleine taak loopt een controleur-agent mee, en de meetlat voor nieuwe kansen kan bijna geen ja geven. De vijf punten hieronder pakken dat aan. Punt 1, 2 en 5 zijn gewoon goed en kosten de hoofdchat samen ±2 uur. Punt 3 en 4 zijn keuzes van Thijs.

## Vóór alles: één koerszin (keuze Thijs, 1 minuut)
Er staan drie koersen door elkaar: CLAUDE.md "gebruikers en later geld", de projectbeschrijving "eerst bereik, daarna geld", `doelen.md` "geld gaat voor bereik", en het besluit van 9 nov 22:56 "echt geld maken nu". Ook "nooit haasten om een datum" (doelen) tegenover "liever een eerlijke gok dan een week zekerheid" (22:56). Elke afweging van elke Claude leunt hierop. Mijn advies: **"Zo snel mogelijk eerlijk geld, gespreid over platformen. Bereik telt omdat het tot geld leidt: elk product heeft vanaf dag 1 een betaald deel."** Uitwerking: `voorstellen/10-koers-in-een-zin.md`.

## Top 5

### 1. Elke run leest nog maar ±15 KB in plaats van ±100 KB (gewoon goed)
- **Wat er mis is.** De leeslijst staat op drie plekken en verschilt: CLAUDE.md (berichten, doelen, regels, besluiten, rol, map), `platformmanager.md` (regels, bord, status, taken, laatste 5 regels logboek) en de opdracht van elke taak (weer anders). In de praktijk: regels 13 KB, besluiten 56 KB, berichten tot 42 KB (Olaf), plus de map. 8 Claudes elk uur, ±192 runs per dag. `status.md` moet volgens de rol 10 regels zijn; blender heeft er 61, obsidian 65, pionier 84.
- **Wat anderen doen.** Anthropic: CLAUDE.md onder 200 regels, langer "reduce adherence"; verwijzen of verplicht laten lezen bespaart niets, alleen laden als het nodig is (bron 1, 2, 5). Anthropic's eigen CLAUDE.md is 40 regels (bron 27). Voor lange klussen: kort voortgangsbestand plus git log, en één taak per sessie (bron 8, 23).
- **Voorstel.** CLAUDE.md wordt de enige startlijst met de harde regels (`voorstellen/01-CLAUDE.md`). `organisatie/bord.md` (bestaat al) wordt het ene bestand met wat nu geldt, hooguit 40 regels (`02-bord.md`); `besluiten.md` blijft het logboek maar hoeft niet meer elke run gelezen. `status.md` per map wordt het startpunt: vaste vorm, hooguit 25 regels, met de volgende taak (`03`, deel B). `regels.md` wordt naslag van ±6 KB (`07-regels.md`).
- **Oplevert.** GOK (±4 tekens per token): het begin van een run gaat van ±25.000 naar ±4.000 tokens; bij ±192 runs per dag is dat ±4 miljoen tokens per dag minder. Plus betere naleving, omdat de harde regels niet verdrinken. Kleine extra winst: logboek en taken in dezelfde commit als het werk, niet in een aparte commit (nu na bijna elk stuk werk, zie bevindingen F).
- **Werk.** ±1 uur voor de hoofdchat, in één keer doorvoeren en in elk berichtenbestand één regel zetten.

### 2. Alle geplande opdrachten dezelfde korte tekst (gewoon goed)
- **Wat er mis is.** Gezien met list_triggers (9 nov 23:30): Olaf krijgt elk uur nog "eerst alleen de ideefase, Thijs kiest" (achterhaald 19:20). Hans krijgt "nieuwe platformen zijn nu de hoofdzaak" (zoeken staat stil sinds 18:30). Tess "bouw pas na een ja van Hans" en "elke 3 uur" (beide achterhaald). `geplande-taken.md` is van 7 nov en mist Gijs, Mila, Kees, Lotte en Patrick. De herinnering van 11 nov noemt een ploeg die al twee keer veranderd is.
- **Wat anderen doen.** Bij tegenspraak kiest Claude willekeurig (bron 7). Een geplande prompt moet op zichzelf staan en zeggen wat klaar is (bron 18).
- **Voorstel.** Eén opdracht van ±12 regels voor iedereen; alleen naam, rol en map verschillen. Alles wat verandert staat in de rol, het bord of `status.md`. Wie een taak wijzigt, werkt `geplande-taken.md` en `dashboard/ploeg.json` in dezelfde run bij (`03-geplande-opdracht.md`).
- **Oplevert.** Een besluit van Thijs werkt meteen door, zonder 8 opdrachten aan te passen.
- **Werk.** ±30 minuten met update_trigger.

### 3. Eén beslisser, één controleur, minder tegelijk (keuze Thijs)
- **Wat er mis is.** Drie lagen sturen: Hans, de hoofdchat en de compagnon-ronde. Besluiten van Hans van 20:44 werden dezelfde avond omgedraaid (Garmin donderdag werd meteen; $100 na meting werd $100 nu). Op 9 nov veranderde de ploeg zes keer. Elke run zet volgens de rol "1 of 2 agents" in, ook voor kleine taken; 187 commits sinds 8 nov noemen de controleur. Het Steam-team van vijf schreef op één dag 104 commits aan berichten, en er was al een samenvoegfout.
- **Wat anderen doen.** Project Vend 2: een baas-agent van hetzelfde model "wasn't much help, and might even have been a hindrance"; vaste procedures en afgebakende rollen werkten beter (bron 25). Begin met 3 tot 5 agents, overleg groeit mee (bron 11). Multi-agent kost ±15 keer de tokens (bron 10). Een reviewer die moet zoeken "will always find something" (bron 20); groene tests zijn de beste controle (bron 22).
- **Voorstel** (`05-ploeg-en-sturing.md`). De hoofdchat met Thijs beslist over koers, ploeg en geld en houdt het bord bij. Hans wordt de controleur van het bedrijf: één run per dag, een dagkaart van 10 regels (wie leverde niets, wat is verouderd, wat hangt). Steam met 3 Claudes elk uur, de rest om de 2 uur tot er iets te bouwen is. Controleur-agent alleen bij een ontwerp, iets wat naar buiten gaat, of een getal waar een besluit op rust.
- **Oplevert.** GOK: ±40% minder runs en minder heen en weer, zonder dat Steam trager gaat.
- **Eerlijk over Thijs.** Thijs zei om 21:15 "verbruik is nu niet belangrijk", drie uur nadat hij om 18:30 juist om verbruik snoeide. Mijn punt is niet alleen verbruik: elke extra Claude en elke ommezwaai kost overleg, en dat remt de lancering.

### 4. De meetlat vervangen door één getal: verwachte euro's in 90 dagen (keuze Thijs)
- **Wat er mis is.** Een 8 eist vier dingen tegelijk: kleine makers verdienen er nu, bereik voor nieuwkomers, wij bouwen binnen ±2 weken, Thijs verkoopt binnen een week zonder kosten vooraf. Waar verdiend wordt, zit bijna altijd een drempel ($100 bij Steam, KvK bij TikTok, $100 per jaar bij Garmin). Na ±170 platformen en 410 commits van de zoekers kwamen er vooral zessen en zevens. Steam kreeg een 7 omdat de drempels "schuurden", en Thijs koos het toch. De lat zei nee tegen wat Thijs wilde.
- **Voorstel.** Elke kans (platform plus product samen) krijgt één schatting: verwachte opbrengst in 90 dagen, laag, middel en hoog, met bron per getal, gedeeld door de weken werk. Drempels zijn kosten, geen afwijzing. Kies het beste getal per week werk.
- **Oplevert.** Sneller kiezen, en Thijs snapt elke keuze in één regel. Past bij zijn besluit van 22:56 ("liever een eerlijke gok met kans op geld").

### 5. De lijst voor Thijs op één scherm (gewoon goed)
- **Wat er mis is.** `lijst-thijs.md` is 82 KB met 61 doorgestreepte punten; van de open punten zijn er twee echt nu. Het dashboard raadt met een lange zoekzin welk punt "ter info" is (`dashboard/bouw.py` regel 120) en toont "commits vandaag" als kopcijfer: drukte, geen uitkomst.
- **Wat anderen doen.** Eén inbox voor de mens met drie soorten berichten: melden, vragen, nakijken (bron 26).
- **Voorstel** (`04-lijst-thijs.md`). Hooguit 5 punten, vaste vorm (wat, minuten, nu of deze week of pas na X, waarom in één zin, stappen, de zin die Thijs terugzegt). Afgehandeld gaat dezelfde dag naar het archief. Dashboard (`09-dashboard.md`): bovenaan gebruikers, betalende klanten en euro per maand tegen het doel van 20 december; per product lanceerdatum en waar het op wacht; per persoon de laatste uitkomst in plaats van het aantal commits. "pas na" bepaalt wat ter info is.
- **Werk.** ±30 minuten voor de lijst, ±1 uur voor het dashboard.

## Hoe doorvoeren zonder dat de ploeg vastloopt
Een controleur die mijn voorstellen niet schreef, vond terecht dat CLAUDE.md, rollen en status.md samen moeten veranderen. Daarom:
1. **Eén commit** met: `CLAUDE.md` (01), `organisatie/bord.md` (02), `organisatie/regels.md` (07), de leesstap en agentstap in de rollen (08 A, B en D), `organisatie/sjablonen/status.md` (03 B) en een regel in elk berichtenbestand ("zet je status.md om naar het sjabloon"). Tot een status.md is omgezet, geldt de bovenste taak uit taken.md.
2. Direct daarna de opdrachten van de geplande taken met update_trigger (03 A) en `geplande-taken.md` (03 C).
3. `.gitignore` (06) en `lijst-thijs.md` met archief (04), plus de regels 120 en 134 in `dashboard/bouw.py`.
4. Wat Thijs kiest uit 05 (sturing, ploeg, meetlat) en 08 C (Hans).
Bestanden die nog niet bestaan en dus mee moeten: `organisatie/sjablonen/status.md`, `organisatie/archief/`, `berichten/archief/`, `.gitignore`.

## Ook belangrijk, maar niet in de top 5
- **Repo afslanken** (`06-repo-afslanken.md`). `.git` is 2,7 GB, de datamappen van de zoekers ±170 MB. In deze run liep `git fetch` vast. Een `.gitignore` voor ruwe data kost 10 minuten; de geschiedenis opschonen is een keuze van Thijs voor later.
- **Eerst de regels van een plek lezen.** De Reddit-post voor Rollwright stond dagen klaar; Thijs zag zelf dat r/ObsidianMD door AI gemaakte promotie verbiedt en een eerste post met ban bestraft. Staat nu als regel in `07-regels.md`, deel "Gevonden worden".
- **Zes rollen staan uit** (verkenner, pionier, zijpadzoeker, herweger, strateeg, commercieel). Zet ze in `organisatie/rollen/uit/`, dan leest niemand ze per ongeluk.

- **Weeklimiet: niemand houdt hem nog in de gaten.** Volgens de (nu uitgezette) herinnering "Verbruik-check" stond het account maandag 9 nov 13:40 op 55% van de weeklimiet, die woensdag 21:00 reset (GEZIEN in de opdracht van die herinnering). Daarna kwamen Sanne, Mila, Gijs en Patrick erbij, en Thijs wil niet meer naar verbruik gevraagd worden. Raakt de limiet op, dan stoppen alle runs tegelijk, ook die van het Steam-team, en dat merkt niemand tot Thijs kijkt. Advies: de hoofdchat leest bij elke compagnon-ronde het percentage af als Thijs het in het paneel zet (één getal, geen vraag), en heeft een vaste noodknop klaar: boven 85% gaan Daan, Mila, Sanne en Gijs naar om de 3 uur tot de reset. Voorstel 01 tot 03 helpen hier ook direct.

## Wat ik nog doe (runs 2 tot 5)
- Voorstel 01 en 07 nog eens naast elkaar leggen met de huidige regels.md, regel voor regel, zodat er niets wegvalt.
- Een derde ronde op internet: hoe anderen een eigenaar laten beslissen zonder dat besluiten heen en weer gaan (beslisritme, vaste momenten).
- Top 5 definitief maken en per punt de minuten werk voor de hoofdchat nalopen.
