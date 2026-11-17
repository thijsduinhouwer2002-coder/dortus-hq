# Succesverhalen spellen (Fenna)

bezig: niets (verhaal 24 af 17 nov ±06:00 UTC; volgende run: vraag van de hoofdchat als die er is; anders: Idler Fest 2025 van binnen (wie deed mee met korting, wie niet), of Little Writer meten na 6 jan)

Nieuwste bovenaan.

---

## 24. Uitbrengen vlak na Next Fest: de tussenpoos zelf maakt weinig uit (92 bureaubladspellen, kans 0,53), maar de week erna is in onze hoek steeds voller, de snelle lanceringen scoren lager, en Steam's Persoonlijke Kalender wil een vaste datum 60 dagen vooraf. Die hebben wij nog niet gepland

**Vraag (eigen keus, past bij het plan):** het plan is uitbrengen op di 2 tot do 4 maart 2027, één dag na het einde van Next Fest (22 feb tot 1 mrt), met een bevriezing op 15 feb (`platformen/steam/planning-fest-2027.md`, voorstel Vera, Aanvulling 4 in `platformen/verkenner/steam-desktop-2026-11.md`). De onderbouwing daar is een GOK: "wie op het fest de demo speelde krijgt dan meteen de melding". Klopt dat bij bureaubladspellen? En wat moet er op de winkelpagina staan om zo'n datum te laten werken?

**Bronnen (17 nov 2026 met curl):**
- Valve, Next Fest-hub (`partner.steamgames.com/doc/marketing/upcoming_events/nextfest`, GEZIEN): een spel mag maar één keer meedoen ("titles may only participate in ONE Next Fest"), mag pas na het fest uitkomen, en "there are no requirements regarding when your game releases (so long as it is after Next Fest)". Valve geeft geen advies over hoeveel later. Data feb 2027: Next Fest 22 feb tot 1 mrt, Spring Sale 18 tot 25 mrt (`doc/marketing/upcoming_events`, GEZIEN).
- Valve, Persoonlijke Kalender (`partner.steamgames.com/doc/marketing/visibility/personalcalendar`, GEZIEN) en het Steamworks-bericht "Steam's Personal Calendar Full Release" van 23 okt 2026 (nieuws-API appid 593110, GEZIEN). Plus "A Refreshed Steam Store Home Page" van 4 jun 2026 (Popular Upcoming alleen nog voor de grootste).
- Chris Zukowski, "Should you launch your game immediately after you appear in Steam Next Fest?" (howtomarketagame.com, 8 jul 2024) en "How the Steam Personal Calendar affects your launch" (25 jun 2026). DERDEN, met GameDiscoverCo-data die ik niet kan nakijken.
- Eigen meting: alle 604 betaalde bureaubladapps uit Vera's kaart die tussen 1 jan 2024 en 15 okt 2026 uitkwamen. Per spel de aankondigingen (nieuws-API), gezocht op "Next Fest" in de 3 weken voor tot 3 dagen na een editie; de reviews in de eerste 28 dagen uit de weekgrafiek van Steam (`appreviewhistogram`, alle talen; bij 2 oude spellen per maand, naar rato). 92 spellen deden aantoonbaar Next Fest. Data `platformen/succes/data/nextfest-tussenpoos-bureaublad-2026-11-17.csv`, scripts `nextfest-tussenpoos-haal.py` en `-analyse.py`.
- Drukte: uitgavedata van alle 913 bureaubladapps uit 2024 tot 15 nov 2026 in Vera's kaart, plus de 23 aangekondigde met maart 2027 (appdetails, GEZIEN).

**Wat ik zag: de tussenpoos tussen het fest en de uitgave (92 spellen met Next Fest):**
| Dagen na het einde van het fest | Spellen | Reviews in 28 dagen, mediaan | 50+ | % positief, mediaan | onder 80% positief |
|---|---|---|---|---|---|
| 0 tot 7 | 13 | 37 | 46% | 79 | 6 van 12 |
| 8 tot 30 | 19 | 56 | 53% | 89 | |
| 31 tot 90 | 34 | 59 | 50% | 85,5 | |
| meer dan 90 | 26 | 68,5 | 62% | 92 | |
| (geen Next Fest-post) | 512 | 4 | 12% | 90 | |
- Uit de week na het fest kwamen Desktop Raid (6 dagen, 429 reviews in 28 dagen), Desk Paws (1 dag, 240), Pat the Cat (3 dagen, 162) en Bao Bao (2 dagen, 129). De grote winnaars kwamen later: Desktop Defender 15 dagen (1.205), Monster Farm 21 (570), Rusty's Retirement 74 (±4.900, maandgrafiek), Spirit City 56 (±2.900), Birdwatching Notebook 85 (1.167), Tiny Pasture 119 (2.618), Deskrawl 98 (3.211).
- Spellen tot 30 dagen na het fest tegen spellen daarna: de kans dat een willekeurig "later" spel meer reviews haalt dan een willekeurig "snel" spel is **0,53**. Dat is bijna een muntworp. De tussenpoos verklaart de uitkomst nauwelijks; meedoen aan Next Fest wel (mediaan 37 tot 68 tegen 4, maar daar zit ook in dat serieuze makers meedoen).
- Wat wel opvalt: de snelle lanceringen scoren lager. 6 van de 12 met 10+ reviews zitten onder 80% positief, tegen 14 van de 67 later. Kans 0,65 dat een later spel hoger scoort. Desktop Raid kondigde zijn datum 3 dagen vooraf aan (6 mrt voor 9 mrt 2026) en had daarna een "Black Screen Issue: Apology, Fix, and Compensation" (15 mrt) en compensatie in twee delen (75%). Desktop Heroes 70%, Card Corner 74%, Cozy Mining 75%. GOK over de reden: geen tijd om wat festspelers zeiden in het volle spel te verwerken.
- Een waarschuwing over verlanglijsten: Cozy Mining haalde 5.000 verlanglijsten in Next Fest juni 2026 en meldde "our cumulative wishlists have crossed 10,000" op de lanceerdag, 4 dagen na het fest (eigen posts 22 en 26 jun 2026). In 28 dagen kwamen er 37 reviews, nu 41. Verse festverlanglijsten zijn geen kopers.

**Drukte in onze hoek (uitgaven per week, alle bureaubladapps, Vera's kaart):**
| Next Fest | Week van het fest | Week erna | 2e week erna | Gemiddelde week in de 8 weken ervoor |
|---|---|---|---|---|
| feb 2025 | 1 | 4 | 1 | 2,0 |
| jun 2025 | 6 | 7 | 2 | 3,2 |
| okt 2025 | 2 | 13 | 7 | 2,2 |
| feb 2026 | 3 | 8 | 9 | 5,6 |
| jun 2026 | 9 | 13 | 9 | 8,1 |
| okt 2026 | 19 | **59** | **51** | 23,0 |
- De week na het fest is in onze hoek steeds 1,4 tot 6 keer zo druk als een gewone week, en in okt 2026 kwamen er 59 bureaubladapps uit in de week erna. Zukowski zag hetzelfde over heel Steam in juni 2024: "June 19th and June 20th (the first two days following Steam Next Fest) ... had the most releases that month", en zijn slotsom: "there isn't an advantage to launching right after Steam Next Fest and it could actually hurt your launch. But NOT by that much."
- Voor maart 2027 staan nu al 23 bureaubladapps aangekondigd, waarvan 8 met een vaste dag (o.a. **Woollings op 2 mrt**, in Vera's kaart "lijkt op Hats" 2; Desktop Mart 1 mrt; AEX: AFK Exos Heroes 7 mrt) en 15 met alleen "March 2027". Na Next Fest komen daar de festspellen bij die nu nog geen datum hebben.

**De Persoonlijke Kalender van Steam (nieuw sinds jun 2026, volledig sinds 23 okt 2026), wat Valve letterlijk zegt:**
- Hij toont elke speler aanbevolen spellen die net uit zijn of eraan komen, op grond van wat spelers met dezelfde smaak op hun verlanglijst zetten. Op de voorpagina "two weeks ago, and two weeks in the future", op de eigen kalenderpagina acht weken.
- Een spel staat er alleen in met een **vaste dag** op de "binnenkort"-pagina. "To maximize your visibility, set your release date at least 60 days in advance to be eligible to appear on the dedicated calendar page, and at least three weeks in advance to be eligible to appear on the front page."
- Geen drempel in verlanglijsten ("There is no minimum").
- Uitstellen mag, maar: wie "more than 24 hours" uitstelt in de laatste twee weken, verdwijnt van de kalender tot de uitgave. Vervroegen kost niets. Zaterdag en zondag tellen als de maandag erna.
- Wat het oplevert (DERDEN, Zukowski): bij Focus Grove gaf de kalender 79.820 vertoningen met 33,8% doorklik (27.001 bezoeken) tegen Popular Upcoming 1,3 miljoen met 0,8% (10.538); Don't Let It Starve ging van 5.930 naar 11.630 verlanglijsten in het venster voor de uitgave. Volgens hem: zichtbaar tot 2 maanden voor en een maand na de uitgave. Focus Grove staat ook in mijn tabel (91 dagen na Next Fest feb 2026, 113 reviews in 28 dagen, 96%).
- Voor 2 mrt betekent de regel van 60 dagen: **een vaste datum zichtbaar op de pagina uiterlijk vr 1 jan 2027**, en voor de voorpagina uiterlijk 9 feb. Ik vond in onze repo nergens een plan voor de datum op de pagina (`teksten-makers.md` zegt alleen "de lanceerdatum ligt nog niet vast"); de pagina gaat ±8 dec live.

### Drie lessen
1. **De dag na Next Fest is geen voordeel op zich.** Bij 92 bureaubladspellen zie je geen verschil in reviews tussen snel en later uitbrengen (kans 0,53); de grote winnaars kwamen 2 weken tot 4 maanden na hun fest. Zukowski kwam over heel Steam op hetzelfde: het verlanglijstje wordt in maanden gebakken, niet in de week ervoor.
2. **De week na het fest is de drukste week van onze hoek, en wie te snel uitbrengt scoort lager.** In okt 2026 kwamen er 59 bureaubladapps uit in de week na het fest, 2,6 keer een gewone week; de helft van de snelle lanceringen bleef onder 80% positief, tegen een vijfde van de latere.
3. **Een vaste datum op de pagina, 60 dagen vooraf, is nu gratis zichtbaarheid.** Valve zet een spel alleen op de Persoonlijke Kalender met een vaste dag, het liefst 60 dagen vooraf, zonder drempel in verlanglijsten. Uitstellen vóór de laatste twee weken kost niets, dus vroeg een datum zetten heeft weinig nadeel.

### Voorstel voor Dortus deze week
**Hoofdchat (beslist de datum), Mila en Sem (pagina): zet een vaste dag op de winkelpagina van Hats zodra die live gaat (±8 dec), en uiterlijk vr 1 jan.** Valve's eigen regel: 60 dagen vooraf voor de kalenderpagina. Een maand als "March 2027" telt niet. Schuift het na de festuitslag van 18 jan, dan is uitstellen tot half februari zonder straf (alleen binnen 2 weken voor de dag kost het de kalender).
**Welke dag: mijn advies is niet di 2 mrt maar een dinsdag tot donderdag 2 tot 4 weken later, met een voorkeur voor ma 29 mrt tot do 1 apr** (na de Spring Sale van 18 tot 25 mrt, en de valreserve die al in het plan staat). Waarom: (a) de tussenpoos zelf kost geen reviews (les 1), (b) we ontlopen de drukste week van onze hoek, waar Woollings al op 2 mrt staat (les 2), (c) wat festspelers van 22 feb tot 1 mrt zeggen kan nog in het volle spel, en de lage scores van de snelle groep laten zien wat er anders gebeurt, (d) de festverlanglijsten krijgen hoe dan ook de melding op de lanceerdag. De bevriezing schuift dan mee naar ±15 mrt.
Tegenargument, eerlijk: Vera's maandcijfers (februari en maart scoren het best) en de "vers in het geheugen"-gedachte; en 4 weken later is 4 weken later geld (doel 6 mrt: €300 tot €400 per maand). Mijn tabel heeft maar 13 snelle spellen; het verschil in score kan toeval zijn. Blijft het 2 mrt, dan staat punt 1 (vaste dag uiterlijk 1 jan) nog steeds.

Eerlijk over de meting: "deed Next Fest" is afgeleid uit aankondigingen; makers die er niets over postten tellen als "geen post", dus de 512 bevatten ook festdeelnemers. De reviews in 28 dagen zijn een grove maat voor verkoop. De Persoonlijke Kalender bestaat pas sinds okt 2025 (proef) en jun 2026 (voorpagina); de meeste spellen in mijn tabel kwamen uit voor die tijd, dus wat de kalender doet bij een bureaubladspel van ±$5 kan ik niet meten (alleen Zukowski's voorbeelden, DERDEN). Ook niet te meten: of de kalender in de festweek zelf zichtbaar blijft.

---

## 23. Hoe eindigt een demo van een bureaubladspel? Geen enkele van 152 stopt op de klok; ze stoppen bij een stuk inhoud, spelers laten ze dagen tot honderden uren aan staan, en de save mee is wat ze onthouden. De meeste winnaars halen de demo weg bij de lancering

**Vraag (eigen keus, past bij de demo van 21 dec):** de demo van Hats stopt na 2 uur open tijd (`producten/steam-hol/ontwerp.md`, Demo-einde: grens 7200 s) en bevat hol 1 tot 12, dat na ±2,0 open uur bereikt is (`platformen/steam/voortgang.md`, punt 3 en 5). Het volle spel loopt tot hol 50 na ±128 open uur, dus de demo is ±1,6% van de weg. Hoe doen de andere bureaubladspellen het: tijd of inhoud, hoe lang spelen mensen de demo, gaat de save mee, en blijft de demo na de lancering staan?

**Bronnen (alles 17 nov 2026 met curl, GEZIEN tenzij anders):**
- Winkeltekst van de demo zelf (`store.steampowered.com/api/appdetails` van de demo-appid) voor alle 206 uitgebrachte spellen met een demo uit Vera's kaart en 47 van de 245 aangekondigde. 152 demopagina's hebben echte tekst. Ingedeeld op zoekwoorden (tijdsgrens, inhoudsgrens, save mee), elke tijdtreffer met de hand nagelezen. Data `platformen/succes/data/demo-einde-bureaublad-2026-11-17.csv`, scripts `demo-einde-haal.py` en `demo-einde-analyse.py`.
- Nieuws-API (`ISteamNews/GetNewsForApp`, aankondigingen van de maker) van de 60 grootste betaalde bureaubladspellen, gezocht op zinnen met "demo" plus weghalen, save, grens. Script `demo-einde-nieuws.py`.
- De 50 tot 60 meest behulpzame Engelse reviews (communitypagina) van de 53 uitgebrachte spellen met demo en 30+ reviews, plus 15 spellen rond hun demo (de meeste haalden hem weg): 2.731 reviews van 66 spellen, waarvan 74 het woord demo noemen. Script `speeltijd-community-haal.py` uit verhaal 22.
- Openbare spelersteller `ISteamUserStats/GetNumberOfCurrentPlayers` op een demo-appid.

**Hoe de demo eindigt (152 demopagina's met tekst):**
| Soort grens | Aantal | Voorbeelden |
|---|---|---|
| tijdsgrens (minuten of uren, dan stop) | **0** | geen enkele |
| zegt hardop "no time limit" | 6 | Lofi Cozy Room, Nanoquarium, A Living Corner, My Little Ranch |
| inhoudsgrens beschreven | 33 | Tiny Terraces "17 plantable crops (out of 56)" (92%, 1.006 reviews); Mini Cozy Room "25 out of 160 tracks" (96%, 3.697); Birdwatching Notebook "limited to the Balcony" (97%); Book of Fei "the complete first chapter"; Idle Abyss Princesses "reaching stage 20 with a character level cap of 30"; Cat Caffeine "1-2 hours of relaxed play from the early game ... past the demo's stopping point" |
| niets over de grens | ±113 | |
In de aankondigingen hetzelfde beeld: Fishing The Abyss "a level cap of 100, but aside from that, there are no restrictions" (26 feb 2025); Desktop Defender gaf in Next Fest extra levels bij elk doel van gelijktijdige spelers (verhaal 5). Ook Cat Caffeine, die "1-2 hours" noemt, stopt bij een punt in het spel, niet bij een klok.

**Hoe lang spelers een bureaubladdemo spelen (uit de reviews van het volle spel):**
- "after trying the demo for 1 week" (Desk Garden, 184 uur), "played the demo for around 6 hours and immediately bought" (Lakeside Bar), "I put like 13 hours in the demo" (Swarmslam), "Just as good as the demo which I 100% before release" (Deskrawl), "Played the demo lots. All off the above was from the demo experience alone" over het verschil tussen uur 1 en uur 50 (Desktop Defender), "I've played the demo for like 300 hours" (Stress Relief), "well over 500+ hours" (Tap Tap Loot), "Including demo, I've had up to 900 hours" (Daydream Cat). GEZIEN.
- Van de 74 reviews die de demo noemen zijn er 61 positief; het patroon is steeds "demo gespeeld, toen meteen gekocht". Een tegengeluid: Whimside "I ... kind of liked the demo more than the full game", Deskrawl "Some things look far worse in the full release compared to the demo".
- Dat de teller van een demo echt meetelt, kun je zien: de demo van Mini Cozy Room had op 17 nov 03:43 UTC **15 spelers tegelijk**, anderhalf jaar na de uitgave (`GetNumberOfCurrentPlayers` op appid 3550820). Die teller is openbaar en werkt dus ook voor een demo.

**De save mee, en wat er gebeurt als die niet meegaat (aankondigingen en reviews):**
| Spel | Save mee? | Wat er gebeurde |
|---|---|---|
| Tap Tap Loot (Irox, 76%) | nee | Na de lancering: "We know we also didn't communicate the demo save wipe enough and we should've found a way to maintain the save files. Again, sorry." plus gratis skins als goedmaker (17 apr 2026). |
| Stress Relief (83%) | nee | Behulpzame negatieve review: "After 218hrs and 54km distance in the demo, I am regretful to say that I will not be continuing on with this game ... the developers decided to not add a way for you to import your data". |
| My Little Life (89%) | nee | Haalde de demo vóór de lancering weg "as the save files from the demo won't be transferable ... I didn't want to have people sink many hours into the demo right before the main game comes out" (8 jan 2025). |
| Tiny Pasture (93%) | nee | "demo save data won't carry over" (12 feb 2025), demo offline op de lanceerdag. Geen review in de 60 behulpzaamste klaagt erover. Dus niet dodelijk. |
| Cozy Mining, Progress98 | ja | Reviews noemen het als pluspunt: "one of the coolest things is that your progress from the demo transfers ... It made playing the demo feel worthwhile". |
| Monster Farm, Maltese's Fluffy Onsen, gogh, Duelist, Desktop Raid, Bao Bao, Bit Buddy | ja | Herhaald in bijna elke aankondiging rond de lancering ("your Demo saves WILL carry over", Monster Farm 8 tot 11 nov 2025). Desktop Raid: dag na de lancering "Partial data loss when inheriting Demo save files" als eerste bekende fout. |
| Typing Farmer, Bugtopia | deels | Munten mee (Typing Farmer 10:1, tot 10.000), Bugtopia munten via een menu. |

**Blijft de demo staan na de lancering?**
- Van de 20 grootste betaalde bureaubladspellen hebben er nu **3** een demo (To Be or Not to Be, Mini Cozy Room, Cornerpond); van de 60 grootste 16 (Vera's kaart, `demo`-kolom, en appdetails van Rusty's, Desktop Defender, Tiny Pasture, Deskrawl, Ropuka, Spirit City en Bongo Cat: geen demo, GEZIEN).
- Hardop aangekondigd weghalen op of vlak voor de lanceerdag: Desktop Defender ("the demo will be delisted a few hours before the game comes out", 3 nov 2025), Tiny Pasture, gogh, Maltese, Monster Farm, Loafing Town, Duelist, NoSlack Pets, Sensei. Lootborne hield de demo na Next Fest langer aan "after seeing your support", tot de demo "no longer reflects the current state of the game" (31 jul 2026).
- Wie hem houdt doet het niet slechter: Mini Cozy Room 96%, Birdwatching Notebook 97%, Bugtopia 92%. Of houden of weghalen meer verkoop geeft, kan ik niet zien: GOK in beide richtingen.

### Drie lessen
1. **Een bureaubladdemo stopt bij een stuk inhoud, niet op de klok.** 0 van 152 demopagina's noemen een tijdsgrens, 6 zeggen juist "no time limit", 33 beschrijven een inhoudsgrens (gewassen, nummers, een gebied, een levelplafond). Hats is met "na 2 uur open tijd" in deze hoek de enige met een klok.
2. **Spelers laten een bureaubladdemo dagen aan staan, en dat verkoopt het spel.** Een week, 13 uur, 100% van de demo, honderden uren: dat staat in de reviews van de winnaars, steeds met "toen meteen gekocht". Een demo van een spel dat je laat draaien wordt geproefd in werkdagen, niet in een half uur. Onze demo is ±2 open uur, ongeveer één ochtend werken.
3. **De save mee is wat spelers onthouden; de demo zelf gaat bij de meeste winnaars offline.** Een wis kostte Tap Tap Loot een openbare verontschuldiging en Stress Relief een behulpzame negatieve review; Cozy Mining kreeg er lof voor. 17 van de 20 grootste hebben nu geen demo meer. Een vaste demo naast het volle spel (`platformen/steam/verdienmodel.md`, "permanente gratis demo") is dus de uitzondering, niet bewezen goed of slecht.

### Voorstel voor Dortus deze week
**Olaf (beslist) en Sanne (balans): laat de demo van Hats eindigen op inhoud, niet op de klok.** Concreet: de regel `That's the demo. Your hole keeps going.` komt wanneer hol 12 bereikt is (of alle 6 dingen in de winkel gekocht), niet na 7200 s open tijd. Waarom: (a) niemand in deze hoek gebruikt een klok, (b) met een klok krijgt een rustige speler, die maar af en toe klikt, het einde vóór hol 12 en ziet dus minder van het spel dan een graver, terwijl juist de rustige werker onze koper is, (c) de demo-inhoud is al op hol 12 gebouwd (`voortgang.md` punt 5), dus het is een kleine wijziging aan `kern/demo_einde.gd` (de grens wordt een hol-niveau in plaats van seconden; de testvlag `demo_einde=` kan blijven voor de toets). Hoeveel werk precies: Olaf, GOK één run.
Als Sanne ruimte ziet: hol 13 tot 16 er ook in, zodat de demo eerder een werkdag dan een ochtend duurt. Niet als het nieuwe inhoud vraagt vóór 21 dec.

Ter info voor Olaf (nieuw feit bij zijn "nu niet" over een gezamenlijk doel, 16 nov): Steam telt de spelers van een demo zelf en openbaar (`GetNumberOfCurrentPlayers` werkt op een demo-appid, GEZIEN). Een doel als "bij 100 spelers tegelijk komt hol 13 erbij", zoals Desktop Defender deed, hoeft dus niet door ons geteld te worden. Het blijft een nieuwe feature buiten de demolijst; zijn besluit.

Eerlijk: de indeling van de demoteksten is op zoekwoorden; 113 pagina's zeggen niets over de grens, en daar kan een klok in zitten die de maker niet noemt (GOK: klein, want een klok is iets wat spelers juist zouden noemen, en geen van de 74 demoreviews doet dat). Uren in reviews zijn van tevreden kopers, dus van de spelers die het langst bleven.

### Wat ik niet kon zien
- Hoe lang de gemiddelde demospeler blijft: Steam toont dat alleen aan de maker.
- 198 van de 245 aangekondigde demo's (ophalen afgebroken om tijd te sparen; het script gaat verder waar het stopte).

---

## 22. Speeltijd op de winkelpagina: maar 2 van 244 bureaubladspellen noemen een aantal uren, en "endless" hoort bij de slechter beoordeelde kerkerspellen. Spelers rekenen je af op wat er niet is (een einde dat ontbreekt, een belofte van 200 uur), niet op een eerlijk klein getal

**Vraag:** in `platformen/steam/planning-fest-2027.md` staat dat Mila en ik de woorden kiezen voor de speeltijd op de winkelpagina van Hats ("about 40 hours to reach the third layer" of vergelijkbaar, geen "100 hours"). Wat doen bureaubladspellen die het goed doen, en wat gebeurt er als het niet klopt?

**Bronnen:**
- Eigen meting: winkeltekst (short description en "About this game", `store.steampowered.com/api/appdetails`, 17 nov) van alle 244 uitgebrachte spellen met 30+ reviews uit Vera's kaart (`platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv`, zonder de programma's). Daarin gezocht naar uren, "endless", "infinite", "hundreds of" en dergelijke, elke treffer met de hand nagelezen. GEZIEN.
- Per spel de 20 meest behulpzame Engelse reviews van de communitypagina (`steamcommunity.com/app/<id>/reviews/?browsefilter=toprated`), met "hrs on record": 221 spellen met 5+ reviews, 1.042 negatieve reviews. Bij 8 spellen met een claim tot 80 reviews. (De review-API `appreviews` stuurt ons sinds 16 nov door naar de voorpagina, zie `platformen/verkenner/data/steam-desktop-haal-script.py`.) GEZIEN.
- Nieuws-API van Mini Painter (`ISteamNews/GetNewsForApp`) en prestatie-percentages (`GetGlobalAchievementPercentagesForApp`). GEZIEN.
- Data: `platformen/succes/data/speeltijd-winkel-2026-11-17.csv`; scripts `speeltijd-haal.py`, `speeltijd-community-haal.py`, `speeltijd-analyse.py` in dezelfde map.

**Wat de winkelteksten zeggen (244 spellen, GEZIEN):**
| Soort zin | Aantal | Voorbeelden |
|---|---|---|
| een aantal uren inhoud | **2** | Mini Painter "Around 70 hours of meditative gameplay" ($3,99, 197 reviews, 89%); Desktop Driller "300+ hours of content" (gratis, 31 reviews, 61%) |
| uren zonder getal | 2 | Village Tale "infinitely for tens of hours" (81%); Lowmoor "Hundreds of hours of idle play" (gratis, 82%) |
| eindeloze voortgang ("endless waves", "no end", "never-ending") | 14 | Desktop Defender 92%, Peckers 97%, maar ook Task Bar Cube 27%, QuestAway 36%, Undealt 42% |
| eerlijk begrensd | 3 | Desktop Mark: "How many hours of gameplay will I get? Don't expect hours of content." (87%); Progress98: "This is NOT a short incremental! This is NOT an infinitely long incremental!" (96%); Desktopia zegt dat hij geen "thousands of hours of content" heeft zoals Anno (70%) |
| niets over speeltijd | ±223 | Rusty's Retirement, Bongo Cat, Tiny Pasture, Mini Cozy Room, Deskrawl: geen van de grote noemt uren |
Wel veel "hundreds of items" (17 keer), maar dat gaat over spullen, niet over tijd. Wat de toppers doen: ze zeggen wat erin zit (zaden, meubels, hoeden), niet hoe lang het duurt.

**Wat spelers ermee doen:**
| Spel en zin | Wat de reviews zeggen | Bron |
|---|---|---|
| **Mini Painter** "Around 70 hours" | 89% en de middelste positieve schrijver heeft 58 uur op de klok, dus het getal klopt ongeveer. Maar twee reviews noemen 200: "200 hours of play is a lie (took me 45, but could be finished faster)" (apr 2026) en "forcing me to restart a 200 hour game at 177 hours" (aug 2025). Of er eerder 200 op de pagina stond kon ik niet zien (het webarchief gaf geen verbinding): GOK, wel twee schrijvers los van elkaar. | GEZIEN (reviews), DERDEN (de 200) |
| Mini Painter, het einde | Uitgebracht 24 jul 2025 **zonder einde**. Behulpzame negatieve reviews: "A week and a half after launch and there's still no ending ... this is a full release" en "after 177 hours, there is still no ending". Het einde kwam op 5 aug ("The Final Chapter is Here"). Nu haalt **31%** van de spelers met prestaties de prestatie `final`. | GEZIEN |
| **Incremental Infinity** "infinite progression" | 57%, 37 van de 80 gelezen reviews negatief: "holds up to its name by being an incremental game with infinite progression, but sadly zero depth" (32 behulpzaam), "After 18h, I had 100% achievements ... Very short for a pure idle game". Eindeloos beloven en na 10 uur alles hebben is de slechtste combinatie. | GEZIEN |
| **Task Bar Cube** "Endless Levels: No level cap, no end" | 27%; de klachten gaan over betalen en lege systemen, niet over lengte: "there is no end, you have to..." staat in een review over betalen om te winnen. | GEZIEN |
| **Village Tale** "tens of hours" | 81%; "You can easily finish the game ... in 10 hours or so, if you play actively" in een positieve review, en "I feel like I have completed the game in 2-3 days" in een negatieve. Ongeveer wat de pagina zegt. | GEZIEN |
| **Desktop Mark** "Don't expect hours of content" | 87%, gratis; van de 8 negatieven zegt er geen één dat het te kort is. | GEZIEN |
| **Progress98** "NOT a short ... NOT infinitely long" | 96%, 28 van 29 positief, uitgebracht 9 nov 2026. Klein en nieuw, dus een eerste teken, geen bewijs. | GEZIEN |

**Breed (221 spellen, 1.042 behulpzame negatieve reviews):**
- Maar **48 negatieve reviews (5%)** zeggen dat het te kort is of dat de inhoud op is; **94 (9%)** klagen over grind of te traag. GEZIEN, mijn zoekwoorden (lijst in `speeltijd-analyse.py`), dus eerder te laag dan te hoog; "op na een paar dagen" in andere woorden mis ik.
- **Uren op de klok zeggen weinig bij dit soort spel:** de middelste positieve schrijver heeft 30 uur op de klok, de middelste negatieve 11 (mediaan over de spellen). Een bureaubladspel telt de tijd dat het open staat. "40 hours" is dus minder dan wat een tevreden speler sowieso op zijn klok ziet, en een speler leest het niet als belofte van 40 uur aandacht.
- **"Endless" bij de gevechts- en kerkerspellen:** de 13 met een eindeloze-voortgangszin staan op een middelste 60% positief, de 52 zonder zo'n zin op 79%. Dat is samenhang, geen oorzaak: wie "endless" roept is vaak het spel met de dunne lus of de winkel erin. Maar de winnaars (Deskrawl, Desktop Heroes, Rusty's) doen het zonder.

### Drie lessen
1. **De toppers noemen geen uren, ze noemen wat erin zit.** 2 van 244 noemen een getal; Rusty's, Bongo Cat, Tiny Pasture, Mini Cozy Room en Deskrawl geen van allen. Een getal valt dus op, en het wordt nagemeten: Mini Painter kreeg "is a lie" bij een getal dat spelers als te hoog zagen.
2. **Je wordt afgerekend op wat er niet is, niet op een klein eerlijk getal.** Desktop Mark en Progress98 zeggen hardop wat het spel níet is en staan op 87% en 96%. Mini Painter kwam zonder einde uit en kreeg daarvoor zijn behulpzaamste negatieve reviews ("this is a full release"). Hetzelfde als de Fusion Lab van Monster Farm (verhaal 6).
3. **"Endless" en "infinite" helpen niet.** Ze staan vooral bij de slechter beoordeelde kerkerspellen, en Incremental Infinity werd op zijn eigen naam afgerekend ("holds up to its name ... but sadly zero depth").

### Voorstel voor Dortus deze week
**Mila en Thijs: geen aantal uren op de winkelpagina van Hats, en nergens "endless" of "infinite". Wel wat erin zit, met getallen die bij de lancering echt af zijn, plus één eerlijke zin over het soort spel.** Concept, de echte woorden schrijft Thijs (besluit 16 nov 21:05): "50 den levels. 3 layers to dig into. 40 hats to collect." en een regel in de stijl van Progress98, bijvoorbeeld "Not a 10-minute toy, not an endless grind." De getallen pas invullen als de bevriezing van ma 15 feb voorbij is: staat laag 4 dan niet in het spel, dan staat er "3 layers", en de laag in april wordt een eigen bericht ("a new layer"). Olaf: het einde van de hoofdlijn (hol 50, of wat het einde is) moet op 2 maart in het spel zitten, niet in een update erna. Wie: Mila (pagina), Thijs (woorden), Olaf (einde in de lancering). Kosten: niets, één regel in het pagina-plan.

Eerlijk: Mini Painter is één spel, en dat de 200 echt op de pagina stond is een GOK op basis van twee reviews. De vergelijking "endless" tegen geen claim zegt niets over oorzaak. Wat wel vast staat: bijna niemand noemt uren, ook de grootste niet, en de echte klachten gaan over een ontbrekend einde, grind en dunne inhoud.

### Wat ik niet kon zien
- Of winkelteksten eerder een ander getal hadden (webarchief gaf "connection reset").
- Alle reviews per spel: de communitypagina geeft per keer 10, dus ik las de 20 meest behulpzame per spel (en tot 80 bij 8 spellen).

---

## 21. De eerste korting van 20% of meer na de lancering: de korting zelf doet weinig, de etalage van Steam doet het. Vier spellen in een themafest of Daily Deal kregen 3,6 keer zoveel reviews per week; eigen kortingen en seizoensuitverkopen gaven ongeveer 1 keer, en een update erbij gaf geen extra sprong

**Vraag:** in verhaal 20 stelde ik voor om de eerste korting van 20 tot 25% voor Hats te bewaren voor de Summer Sale van 2027, samen met een gratis update. Wat deed zo'n eerste korting echt bij bureaubladspellen, en helpt een update erbij?

### Bronnen en hoe ik keek (17 nov, ±01:15 tot 01:55 UTC)
- **Welke spellen:** de 139 betaalde bureaubladapps uit Vera's kaart (via mijn tabel van verhaal 20) die uitkwamen tussen 1 jun 2024 en 31 aug 2026 en nu 30 of meer reviews hebben.
- **Wanneer de eerste korting kwam:** alle aankondigingen van elk spel (nieuws-API van Steam, volledige tekst), doorzocht op het eerste bericht op of na dag 25 na de uitgave dat de basisprijs met 20% of meer verlaagt. Berichten over bundels, DLC, "extra korting voor wie het al heeft" en een lanceerkorting van een ander spel tellen niet. Zes treffers bleken geen korting (een plafond van 65% in een spelregel, "40% volume", een korting op een zusterspel) en heb ik er met de hand uit gehaald. Over: **24 spellen, waarvan 21 met genoeg weken om te meten.**
- **Wat het deed:** reviews per week (`store.steampowered.com/appreviewhistogram/<appid>`, alle talen). Ik vergelijk de twee weken vanaf het bericht met het gemiddelde van de drie weken ervoor ("sprong"), en de drie weken daarna met diezelfde drie weken ("erna").
- **Controle:** reviews dalen na een lancering vanzelf. Daarom dezelfde berekening op hetzelfde aantal dagen na de uitgave bij de 53 spellen in de lijst die nooit iets over korting of uitverkoop schreven. De middelste controlesprong is 0,7: zonder korting zakt een spel in die fase dus ±30% in twee weken.
- **Regels van Valve:** `partner.steamgames.com/doc/marketing/discounts` en `partner.steamgames.com/doc/marketing/upcoming_events` (GEZIEN met curl, 17 nov).
- Data: `platformen/succes/data/eerste-korting-na-lancering-2026-11-17.csv`.
- **Wat ik niet kan zien:** kortingen die de maker niet aankondigde. SteamDB (prijsgeschiedenis) heb ik niet gebruikt, en archive.org is vanaf onze omgeving geblokkeerd (verhaal 20). "Eerste aangekondigde korting" is dus niet altijd de eerste korting.

### Wat ik zag (GEZIEN; alleen spellen met 2 of meer reviews per week vooraf)
Ik heb de 21 kortingen in drie soorten verdeeld, op wat het bericht zelf zegt:

| Soort korting | Spellen | Sprong (middelste) | Erna (middelste) | Controle |
|---|---|---|---|---|
| **in de etalage van Steam:** Daily Deal, themafest of showcase | 4 | **3,6x** | **2,8x** | 0,7 |
| seizoensuitverkoop van Steam (Summer, Winter) of van de uitgever | 6 | 1,0x | 1,0x | 0,9 |
| eigen korting, zonder evenement van Steam | 5 | 1,0x | 0,5x | 0,7 |

**De vier in de etalage:**
- **Fish to Dish: Idle Sushi** ($5,99): Daily Deal op 9 jan 2026 met 20%, samen met update 2.04 ("V2.04 Update Log & Daily Deal!"). Van 21 naar 81 reviews per week (3,9x), daarna 41.
- **Zen Aquarium**: 25% in de Steam Animal Fest, dag 46. Van 2,7 naar 10 per week (3,8x), en dat bleef (9,7 erna).
- **Chonkers** ($4,99): 20% in de Idler Fest van februari 2025, dag 54 ("If you have missed the chance during the winter sale, you can now get Chonkers at 20% off"). Van 5 naar 30 en 28 per week, erna nog 20. De Winter Sale ervoor zie je in zijn grafiek niet terug.
- **Bao Bao's Cozy Laundromat**: 20% in de Minimal & Chill Showcase, dag 47 (het spel van verhaal 3). 1,7x.

**Seizoensuitverkoop:** NoSlack Pets 2,0x (Winter Sale plus update), Little Aviary 1,7x (45%, maar daar stond de controle zelf ook op 1,35), Sensei! 1,1x, gogh 0,9x (Summer Sale 20%, grote update kwam twee weken later; erna 1,4x), Bugtopia 0,7x, Maltese's Fluffy Onsen 0,7x (uitgeversuitverkoop plus update; erna 3,0x, maar dat valt samen met iets wat ik niet kon thuisbrengen).

**Eigen korting:** Lakeside Bar 1,5x, Your Mother 1,4x (Moederdag, met update), Desktop Defender 1,0x (Rebirth-update voor iedereen plus 20%), Whimside 1,0x ("the biggest discount our little game has ever had"), Tiny Pasture 0,9x (gratis DLC plus 20%). Erna zakten ze terug naar de helft.

**Eén uitschieter die buiten de tabel valt:** Meow Palace: Forbidden City (dag 59, "Spring Festival Special Offer", 20%, in de Lunar New Year Sale van Steam). Van 0 tot 2 reviews per week naar 102 en 83; van de 267 reviews in zijn weekgrafiek kwamen er 185 (69%) in die twee weken. Een Chinees spel in de Chinese feestweek.

**Update erbij of niet:** met update middelste sprong 1,0x (7 spellen), zonder 1,6x (8 spellen). Dat betekent niet dat een update schaadt: de spellen met een update zijn vaker de grote, die al hoog stonden. Wel: **een update maakt een korting niet groter.** Desktop Defender en Tiny Pasture deden precies wat Valve aanraadt (korting plus inhoud) en zagen niets bovenop het gewone verval.

**De tiny spellen** (onder 2 reviews per week vooraf, 7 stuks) laten sprongen van 0,6 tot 3,0 zien, maar dat is 1 review tegen 3; daar zeg ik niets over.

### Wat Valve zegt (GEZIEN, 17 nov)
- Daily Deal, Midweek Deal en de andere voorpagina-plekken kiest Valve zelf: "If your title qualifies for an upcoming curated slot, we will contact you with details." Ze kijken vooral naar "the most-played or best-selling games". **Daar kun je je niet voor aanmelden.**
- Themafests wel: je meldt je aan, "while discount games are prioritized", en het fest staat op de voorpagina van Steam.
- Themafests voor 2027 die nu bekend zijn (tot eind mei): Desktop Companion (14 tot 18 jan), Shop Keeper, Sheep, Couch Co-Op, Rhythm, Dinos vs. Robots, Racing, Witch (22 tot 26 apr), Fighting, Real-Time Strategy, Mountaineering. **Na onze uitgave in maart staat er nog geen fest dat echt bij Hats past.** Een Idler Fest voor 2027 staat er (nog) niet.
- Seizoensuitverkopen 2027: Spring 18 tot 25 mrt, Summer 24 jun tot 8 jul, Autumn nog niet bekend.

### Drie lessen
1. **Korting alleen verkoopt een bureaubladspel niet.** Een eigen korting van 20% of een gewone seizoensuitverkoop gaf ongeveer 1 keer de reviews van de weken ervoor (tegen 0,7 bij spellen zonder korting); na afloop zakte het terug. Dat past bij verhaal 20: korting maakt geen winnaar.
2. **De plek is de motor, niet het percentage.** Alle vier spellen met een duidelijke sprong stonden met hun korting in iets van Steam zelf met een thema of de voorpagina (Daily Deal, Animal Fest, Idler Fest, showcase). Bij Chonkers en Zen Aquarium bleef het hoger. Hetzelfde patroon als verhaal 14, 15 en 19: de winkel trekt, maar alleen voor wie hij laat zien.
3. **Een update maakt de korting niet groter.** Zeven kortingen met een update deden het niet beter dan zonder. Een update is voor de spelers die je al hebt (en voor een eigen moment met een bericht), niet een versterker van de korting.

### Voorstel voor Dortus deze week (bijstelling van mijn voorstel uit verhaal 20)
**Sem en Vera: zet in het lanceerplan dat de eerste korting van 20% of meer naar het eerste themafest gaat waar Hats in past (en niet automatisch naar de Summer Sale), en kijk elke maand op `partner.steamgames.com/doc/marketing/upcoming_events` of er een Idler-, Cozy- of Desktop-fest na maart 2027 bijkomt.** Komt er vóór de Autumn Sale geen passend fest, dan pas de Summer Sale (24 jun tot 8 jul) als terugval. De gratis update met een nieuwe laag hoeft daar niet aan vast: die mag zijn eigen dag en eigen bericht krijgen, want samen gaven ze geen grotere sprong. Wie: Sem (lanceerplan) en Vera (fests volgen, zij houdt de markt bij). Kosten: één regel in het plan en één blik per maand.

Eerlijk: het zijn 15 meetbare kortingen, 4 in de etalage. Dat is genoeg om te zien dat een themafest iets anders doet dan een eigen korting, niet genoeg om "3,6 keer" als belofte te gebruiken. En de vier etalagespellen kozen hun fest zelf omdat ze erin pasten; een fest waar Hats niet in past (Witch Fest omdat er een heks in zit) is niet hetzelfde.

**Correctie op verhaal 20 (17 nov ±01:50 UTC):** daar staat "Engelse reviews" bij week 1 en week 2. De weekgrafiek van Steam (`appreviewhistogram`) geeft voor elke taalinstelling dezelfde getallen (getest bij Meow Palace: 267 met `l=english`, `l=schinese` en `language=all`). Het zijn dus reviews in alle talen. De vergelijkingen in verhaal 20 blijven staan, want alle spellen zijn op dezelfde manier geteld.

---

## 20. De lanceerkorting: bijna iedereen geeft er een, de meesten 10 tot 20%. De spellen met 40% deden het het slechtst, en een grotere korting zie je niet terug in meer reviews in week 1. Valves eigen raad (10 tot 15%) klopt met wat de winnaars deden

**Vraag:** Vera's plan voor Hats is $6,99 met 15% korting in de eerste week (`platformen/verkenner/steam-desktop-2026-11.md`, Aanvulling 4). Klopt dat met wat bureaubladspellen echt doen, en levert een grotere korting meer op in de eerste week?

### Bronnen en hoe ik keek (17 nov, ±00:30 tot 00:45 UTC)
- **Regels van Valve:** `partner.steamgames.com/doc/marketing/discounts` en `partner.steamgames.com/doc/marketing/wishlist` (GEZIEN met curl, 17 nov).
- **Wat makers nu doen:** van alle 104 betaalde bureaubladapps uit Vera's kaart die op of na 1 nov 2026 uitkwamen, de prijs en korting van dit moment (`store.steampowered.com/api/appdetails?cc=us`, GEZIEN 17 nov 00:35 UTC). Een lanceerkorting loopt 7 tot 14 dagen, dus alleen de 41 die op of na 10 nov uitkwamen tellen eerlijk mee.
- **Wat makers eerder deden:** de 300 betaalde bureaubladapps uit de kaart, uitgekomen tussen 1 jun 2024 en 31 okt 2026 met 10+ reviews. Van elk de aankondigingen van 14 dagen vóór tot 4 dagen na de uitgave (nieuws-API), doorzocht op een percentage naast "off", "discount" of "launch". Vier treffers waren geen lanceerkorting (een bundel of een spelregel) en heb ik eruit gehaald. Daarnaast de Engelse reviews in week 1 en week 2 (`appreviewhistogram`, eerste week = de eerste week met reviews, alleen als die binnen 4 dagen van de uitgave valt; 291 spellen).
- Data: `platformen/succes/data/lanceerkorting-bureaublad-2026-11-17.csv`.
- **Niet gelukt:** de winkelpagina zoals die in de lanceerweek was (archive.org via web.archive.org is vanaf onze omgeving geblokkeerd; de CDX-zoekdienst ook). Daardoor weet ik van oudere spellen alleen de korting als de maker hem zelf noemde. "Niet genoemd" is dus niet "geen korting".

### Wat Valve zegt (GEZIEN, 17 nov)
- Lanceerkorting: 7 tot 14 dagen, minimaal 10%, maximaal 40%. "We generally suggest launch discounts around 10% to 15%, should you chose to set one."
- Na de uitgave mag er 30 dagen geen andere korting. Valt het eind daarvan midden in een seizoensuitverkoop, dan mag je er halverwege nog in. Voor Hats (uit di 2 tot do 4 mrt) eindigt die wachttijd op 1 tot 3 apr, na de Spring Sale (18 tot 25 mrt). Vera's conclusie (niet meedoen met de Spring Sale) blijft staan.
- "Rushing into a 50% or 75% discount weeks after your launch, or releasing with a very high launch discount, sends a bad message to customers who bought at full price".
- **Een korting van 20% of meer stuurt een mail naar iedereen met het spel op zijn verlanglijst** ("Any type of discount at or above 20%"). Bij de uitgave gaat er sowieso een mail. Of een lanceerkorting van 20% een tweede mail geeft, staat er niet (niet gevonden, GOK dat het niet zo is, omdat de uitgavemail al gaat).

### Wat makers nu doen: 36 van de 41 geven een lanceerkorting (GEZIEN, 17 nov)
| Korting | Aantal (uit 10 tot 15 nov 2026) |
|---|---|
| geen | 5 |
| 10 tot 11% | 13 |
| 15% | 9 |
| 20% | 9 |
| 25 tot 27% | 2 |
| 35 tot 40% | 3 |

88% geeft er een; de middelste waarde van wie er een geeft is 15%. Van de zes met een basisprijs van $6,99 of $7,99: geen, 10%, 10%, 20%, 20% en 40%.

### Wat het eerder opleverde (GEZIEN, 291 spellen met een weekgrafiek vanaf de uitgave)
Van de 249 spellen met een bericht rond de uitgave noemden er 69 een lanceerkorting in dat bericht. Van wie het noemde, schreven er 19 "twee weken" of "14 dagen" en 5 "één week" (in het stukje tekst dat ik bewaarde).

| Genoemde korting | Spellen | Reviews week 1 (middelste) | Middelste helft | Week 2 tegen week 1 | Basisprijs (middelste) |
|---|---|---|---|---|---|
| 10% | 17 | **50** | 22 tot 212 | 0,39 | $5,99 |
| 15% | 13 | 39 | 12 tot 124 | 0,25 | $4,99 |
| 17 tot 20% | 21 | **54** | 13 tot 105 | 0,33 | $4,99 |
| 25 tot 34% | 10 | 20 | 16 tot 202 | 0,28 | $4,69 |
| **40%** | 8 | **14** | 4 tot 28 | **0,10** | $7,49 |
| korting niet genoemd, wel een bericht | 180 | 19,5 | 10 tot 62 | 0,20 | $4,99 |
| geen bericht rond de uitgave | 42 | 7 | 4 tot 11 | 0,12 | $2,99 |

- **Bij 40% deed geen enkel spel het goed.** Van de acht haalde alleen Idlequarium (105) meer dan 31 reviews in week 1; Aviarium ($7,99, 40%, "just $4.79") kreeg er 9, Amphibarium, Checkers Kingdom en Reptilarium 4 of 5. Week 2 viel daar ook het hardst terug.
- **De grote lanceringen zaten bijna allemaal op 10 tot 20%:** Tiny Pasture 10% (1.352 in week 1), Hero Town 20% (1.071), Birdwatching Notebook 10% (723), Desktop Defender 15% (652), Maltese's Fluffy Onsen 10% (487), gogh 15% (403), Duelist 20% (392).
- **Twee uitzonderingen op 30%, allebei met een groot spel of een uitgever erachter:** Deskrawl ($6,99, 30%, 1.559 in week 1) en Tap Tap Loot ($6,99, 30%, 358, uitgever van Bongo Cat). Tap Tap Loot legde uit waarom: "a bit of a higher base price to allow us to discount the title further in the future" (verhaal 19). Deskrawl gaf op 13 nov, 46 dagen na de uitgave, weer 30%, samen met een grote update ("The base game will also be on sale starting tomorrow!", aankondiging 12 nov), en dus niet lager dan bij de lancering.
- **Desktop Heroes** (hetzelfde idee als Deskrawl, verhaal 2) noemde geen korting in zijn uitgavebericht en kwam op 62 in week 1.

**Wat ik er niet uit kan halen:** dat een kleinere korting beter werkt. Wie 40% geeft, is vaak een kleine maker zonder publiek die hoopt dat korting het oplost; wie 10% geeft, is vaak een uitgever met een volle verlanglijst (Tiny Pasture, Maltese, Birdwatching komen alle drie uit China met een uitgever). De korting is hier eerder een teken van hoe sterk een spel al stond dan de oorzaak. Wat wel vaststaat: **een grote korting gaf geen enkel spel in deze hoek een grote eerste week**, en de makers die het goed deden kozen wat Valve aanraadt.

Ook opvallend: spellen die de korting in hun bericht noemden, deden het beter (middelste 39 tegen 19,5). Ook dat is vooral een teken van een maker die zijn lancering goed voorbereidt (een bericht met prijs, korting, bundels en de demovoortgang die meegaat), niet het effect van het woord "korting".

### Drie lessen
1. **15% is gewoon, niet zuinig.** 88% van de nieuwe bureaubladspellen geeft een lanceerkorting, de middelste is 15%, en Valve raadt 10 tot 15% aan. Met 15% vallen we niet op en niet uit de toon.
2. **Een hoge lanceerkorting is een slecht teken, geen motor.** Alle acht spellen met 40% bleven klein (middelste 14 reviews in week 1) en zakten in week 2 het hardst. Valve zegt zelf dat het kopers tegen de vroege kopers opzet. De twee goede 30%-spellen hadden een groot publiek of een uitgever met een groot spel achter zich.
3. **De eerste korting van 20% of meer is een eigen moment, want dan krijgt de hele verlanglijst een mail.** Deskrawl koppelde zijn eerste korting na de lancering aan een grote update, precies wat Valve aanraadt ("tying the discount to a content update"). Met 15% bij de lancering bewaren wij die mail voor later.

### Voorstel voor Dortus deze week
**Vera en Sem: houd $6,99 met 15% (7 dagen, dan eindigt hij vóór de Spring Sale) en zet in het lanceerplan meteen de tweede stap: de eerste korting van 20 tot 25%, op zijn vroegst in de Summer Sale (24 jun tot 8 jul 2027), samen met de eerste gratis update met een nieuwe laag (Olafs volgorde in `platformen/steam/planning-fest-2027.md`).** Waarom: dat is de eerste mail naar de hele verlanglijst na de uitgave, en Deskrawl liet zien dat korting plus update op één dag kan. Niet naar 20% of meer bij de lancering om een extra mail te krijgen: Valve schrijft nergens dat dat een tweede mail geeft, en de uitgavemail gaat toch. Kosten: één regel in het lanceerplan (Sem), geen werk voor de bouwers. In het uitgavebericht: prijs, korting en einddatum in één zin, zoals de goede lanceringen deden (Desktop Defender: "The game will cost $4.99 USD, have a 15% launch discount"). Die zin is spelerstekst, dus CONCEPT voor Thijs.

Eerlijk: dit is een vergelijking, geen proef. Wat 15% tegen 20% bij één spel echt scheelt, laat niemand openbaar zien. Wat de cijfers wel zeggen: wie het goed deed, gaf 10 tot 20%, en niemand werd groot door een grote korting.

---

## 19. De Typing Fest van februari 2026: een themafest van vier dagen, net als het Desktop Companion Fest. Maar 2 van de 105 typespellen voor het bureaublad zeiden er iets over, allebei van de uitgever van Bongo Cat. Wat ze deden: een cadeau op dag 1, en een open speeltest alleen tijdens de festdagen

**Vraag:** wat doet een themafest van vier dagen met bureaubladspellen, en wat deden de makers die het goed gebruikten? Het Desktop Companion Fest loopt van do 14 jan 10:00 PST tot ma 18 jan 10:00 PST. Dat is vier dagen, net als de "Spotlight Fests" van 2026, en niet de gewone week (Valve's lijst via GamingOnLinux: Typing Fest 5 tot 9 feb, Horse Fest 19 tot 23 feb en Hidden Object Fest 9 tot 13 apr zijn allemaal "(Spotlight Fest)"). In de lijst voor 2027 staat dat woord niet bij het Desktop Companion Fest (GEZIEN). Of Valve het net zo klein opzet, weet ik dus niet (GOK). Van die korte fests is de **Typing Fest** de enige met bureaubladspellen erin: Bongo Cat en zijn navolgers hebben het label Typing.

### Bronnen en hoe ik keek (16 nov, ±23:30 tot 23:45 UTC)
- Lijst fests 2026 en 2027: https://www.gamingonlinux.com/2026/01/valve-reveal-all-the-steam-events-scheduled-for-2026 en https://gamingonlinux.com/2026/07/valve-announced-the-themed-sale-events-for-the-first-half-of-2027 (GEZIEN met curl).
- Steamworks-docs over themafests: `partner.steamgames.com/doc/marketing/upcoming_events/themed_sales` (GEZIEN met curl, 17 nov). De pagina van het Desktop Companion Fest gaf deze run een foutmelding; wat erop staat, staat in verhaal 18.
- Wat er in de Typing Fest in de aanbieding was: Simulation Daily, 6 feb 2026, https://simulationdaily.com/news/steam-typing-fest-2026/, en een maker op het IF-forum, https://intfiction.org/t/steam-typing-festival-05-02-09-02-2026/78930 (DERDEN).
- Uit Vera's kaart (`platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv`) 290 bureaubladapps: alle 105 met het label Typing, plus alle andere die vóór 28 jan 2026 uitkwamen met 20+ reviews. Van elk alle aankondigingen (nieuws-API) doorzocht op "Typing Fest", en de reviews per week (`store.steampowered.com/appreviewhistogram/<appid>`, lege weken als 0). Festweek = de week van de app die begint tussen 2 en 6 feb; ervoor = het gemiddelde van de drie weken daarvoor.
- Data: `platformen/succes/data/typing-fest-2026-bureaublad-2026-11-16.csv`.
- Niet gelukt: de festpagina zelf terugzien. Er is geen archiefversie (archive.org heeft niets), en `store.steampowered.com/category/typing/` is nu de gewone labelpagina. Verlanglijsten van anderen zijn niet openbaar, dus wat het fest aan verlanglijsten gaf, weet ik niet.

### Wat Valve zegt over themafests (GEZIEN, 17 nov)
- "A discount is not required to participate ... though each event page will most prominently feature discounted games."
- Elk fest heeft vakken: Discounted, VR, Free to Play, Demos en Upcoming. Daarbinnen sorteert Valve "based on heuristics like player interest and popularity, while other sections may be more random".
- "Steam themed sale events currently do not include playtests." Een speeltest komt dus niet in het fest; de demo en de pagina "binnenkort" wel.
- "Even when events are shorter than one week in duration, the official discount will typically still be set to the standard one week duration." Voor ons pas van belang na de uitgave.

### Wie zei er iets over de Typing Fest? (GEZIEN, aankondigingen)
Van de 105 typespellen voor het bureaublad noemden er **2** de Typing Fest, en van de andere 185 bureaubladapps **geen enkele**. Die twee zijn van dezelfde uitgever:
- **Bongo Cat** (Irox Games, gratis, 31.301 reviews), 5 feb: "WE ARE PART OF THE STEAM TYPING FEST". Een gratis mecha voor iedereen die het spel bijwerkt en het cadeautje aanklikt, een nieuwe mecha-verzameling in de winkel, en een skin en hoed voor wie 1 miljoen klikken haalt.
- **Tap Tap Loot** (ontwikkelaar Turtle Knight Games, uitgever Irox Games), toen nog "binnenkort", 5 feb: "Tap Tap Loot is part of the Steam Typing Fest. To celebrate this we will open up the playtest for everyone for a few days (until Typing Fest ends)". In dezelfde update: wie Bongo Cat en Tap Tap Loot tegelijk draait, krijgt extra kracht van een paar Bongo Cat-voorwerpen ("This is a bit of an experiment").

### Wat de festweek deed met de reviews (GEZIEN, histogram)
| | 3 weken ervoor (gem.) | festweek | week erna |
|---|---|---|---|
| Bongo Cat | 947 | **1.046** (+10%) | 1.037 |
| MISHA (typing, gratis) | 5,7 | 7 | 9 |
| Farlands: Tiny Harvest (typing, gratis) | 25,7 | 22 | 13 |
| 41 andere bureaubladspellen met 3+ reviews per week, mediaan | | **0,78 keer** ervoor | 0,69 keer |

Van de 41 andere spellen zaten er 13 in de festweek op of boven hun eigen niveau. Let op: veel van die 41 waren in nov of dec 2025 uitgekomen en zakten toch al (your wife 0,73, Cast n Chill 0,58). Een eerlijke vergelijking is dit dus niet. Bongo Cat, een spel dat al een jaar stabiel liep, ging in de festweek 10% omhoog en bleef de week erna op dat niveau; zijn eigen dag 1-cadeau zat in die week. Meer dan "een klein plusje" kan ik er niet uit halen.

**Wat het fest deed voor onbekende nieuwkomers (GEZIEN):** drie betaalde typespellen voor het bureaublad kwamen 2 tot 3 dagen vóór het fest uit, zonder bericht over het fest: Your Succubus ($6,99, 3 feb) kreeg 2 reviews in de festweek, Text To Speech ($6,99, 3 feb) 1, Idle Crops ($0,99, 2 feb) 1 en de week erna 3. Deskworm (gratis, uit 15 jan, met demobeloning) zakte gewoon door: 22, 9, 7, en in de festweek 4. Een plek in het fest zonder eigen actie gaf deze spellen dus niets wat je terugziet.

### Tap Tap Loot: van festspeeltest naar lancering (GEZIEN, aankondigingen en histogram)
1. **5 feb 2026, dag 1 Typing Fest:** de speeltest gaat alleen tijdens de festdagen open voor iedereen, met een samenwerking met Bongo Cat.
2. **22 feb, Next Fest:** pas nu de demo. "Your progress will carry over from the playtest". De voortgang van de demo gaat níet mee naar het volle spel; in de plaats daarvan krijgen demospelers een eigen skin (de Target Dummy).
3. **7 apr:** datum bekend (13 apr). Over de prijs: "we decided to go with a bit of a higher base price to allow us to discount the title further in the future. That's why we are launching with a 30% discount!" Basisprijs $6,99, met regionale prijzen.
4. **13 apr, uitgave:** demobeloning, en een bundel met The Farmer Was Replaced (een programmeerspel). Drie dagen later "The Typer Was Replaced": in dat spel kun je nu met `tap()` je Bongo Cat en je Tap Tap Loot-held laten tikken.
5. **Uitkomst:** week 1 **358 reviews**, net boven het bovenste kwart van 70 lanceringen van bureaubladspellen (p75 345, mediaan 133, `lanceer-verval-bureaublad-2026-11-16.csv`). Week 2 maar 100 (0,28 keer week 1; mediaan van de 70: 0,32). Nu 872 reviews.
- Ter vergelijking, **Typing Farmer** (MilkwayStudio, ook met Irox als uitgever): demo al sinds januari, geen bericht over de Typing Fest, uitgave 20 apr met lanceerbundels met Tap Tap Loot, Tiny Pasture en drie anderen. Week 1: 113 reviews, onder de mediaan. Nu 456.
- Wat ik niet kan scheiden: Tap Tap Loot had de grote speler Bongo Cat achter zich (zelfde uitgever, eigen samenwerking in het spel). Wat de Typing Fest zelf deed, is niet te zien.

### Drie lessen
1. **Bijna niemand doet iets met een themafest, dus wie iets doet, valt op.** 2 van de 105 typespellen voor het bureaublad zetten een bericht neer, en allebei hadden ze een reden om te spelen op dag 1 (een gratis mecha, een open speeltest). Dat past bij Sems meting op dag 1 van het Auto-Battler RPG Fest (alleen wie zelf spelers meebracht, steeg) en bij verhaal 3 (cadeaus in de demo). Het Desktop Companion Fest wordt de eerste keer, dus de kans dat de andere spellen stil blijven is groot (GOK op basis van deze 2 op 105).
2. **Iets wat alleen tijdens de festdagen kan.** Tap Tap Loot zette zijn speeltest alleen in de vier festdagen open voor iedereen. Daarmee is het fest een moment met een einde, en geen pagina die er toevallig ook staat. Let wel: Valve neemt speeltests niet op in het fest, dus bij Tap Tap Loot kwam het verkeer via de pagina "binnenkort". Bij ons is de demo er al (ma 4 jan); het cadeau moet dus in de demo zitten.
3. **In een fest van vier dagen gaat het bovenste vak naar spellen die al uit zijn en korting geven.** Ook dat zegt Valve zelf. Een demo of "binnenkort" krijgt een eigen vak, en daarbinnen telt belangstelling. Ons eigen festverkeer moet dus van onszelf komen (mail, makers, bericht om 19:00 NL); het fest geeft vooral een plek.

### Voorstel voor Dortus deze week
**Sem en Olaf: maak van de Fest Hat (al gepland in `marketing/makers.md` voor 8 jan) een hoed die je alleen kunt halen van do 14 jan 19:00 tot ma 18 jan 19:00 NL. Zet hem in de aankondiging van dag 1 met één zin over hoe je hem pakt: bijwerken en spelen, net zo kort als de mecha van Bongo Cat.** Waarom: de enige twee makers die de Typing Fest gebruikten, gaven op dag 1 iets dat alleen toen te halen was. Een hoed met een einddatum maakt van ons fest een moment, en de hoed gaat via de save mee naar het volle spel (Tap Tap Loot kon dat niet en gaf een skin in de plaats). Kosten: één hoed uit de pijplijn (±½ run Mila, planning Olaf) en een datumcheck in de code (klein, Olaf). Valt het buiten de demolijst van 18 dec, dan beslist Olaf; dan is de terugvaloptie het cadeau dat er al is, maar dan zonder einddatum.

Eerlijk: dit zijn twee berichten van één uitgever met honderdduizenden spelers achter zich (Bongo Cat: 500.000 spelers na 4 weken, eigen opgave, verhaal 3). Of een hoed met een einddatum bij een onbekend spel spelers trekt, laat dit niet zien. Wel laat het zien dat het de gewoonte is van de grootste speler in onze hoek.

---

## 18. Tiny Pasture als lanceerpartner: tien nieuwkomers kregen een bundel en een aankondiging op hun lanceerdag of kort erna, maar waar ik het kan meten zie je geen sprong boven het gewone verval (plus: de eisen van het Desktop Companion Fest, eindelijk gelezen)

**Vraag:** Sem vroeg (16 nov ±21:41) of er een manier is om te zien wat een ruil op de lanceerdag een nieuwkomer oplevert, zoals Bugtopia die op dag 1 een crossover plus bundel met Tiny Pasture kreeg. Ons bundelplan (`marketing/bundels.md`) zet Tiny Pasture als eerste kandidaat voor een ruil rond de lancering van Hats. Eerst heb ik de festpagina van Valve gelezen, die in verhaal 17 een foutmelding gaf.

### Bronnen en hoe ik keek (16 nov, ±22:50 tot 23:40 UTC)
- Steamworks-docs, gelezen met curl op 16 nov: `partner.steamgames.com/doc/marketing/upcoming_events/themed_sales/desktop_companion_2027` en de ouderpagina `.../themed_sales` (GEZIEN).
- Alle 59 aankondigingen van Tiny Pasture (appid 3167550) en van de tien partners, via `api.steampowered.com/ISteamNews/GetNewsForApp/v2/` (GEZIEN).
- Reviews per week van de partners en van een vergelijkingsgroep: alle 253 betaalde bureaubladspellen uit Vera's kaart die tussen juni 2024 en augustus 2026 uitkwamen met 10+ reviews; daarvan 70 met een weekgrafiek vanaf de uitgave, 12+ weken en 50+ reviews in week 1 (`store.steampowered.com/appreviewhistogram/<appid>`, GEZIEN). Week 1 = de eerste 7 dagen na de uitgave.
- In die 253 spellen ook gezocht naar aankondigingen met "bundle", "crossover" of "collab" in de eerste 10 dagen na de uitgave: 37 spellen hebben er een.
- Data: `platformen/succes/data/tiny-pasture-lanceerpartners-2026-11-16.csv` (de tien partners) en `platformen/succes/data/lanceer-verval-bureaublad-2026-11-16.csv` (de 70 spellen, verval per week).
- Niet gelukt: reviews per dag (de route `appreviews` stuurt vanaf onze omgeving door naar de voorpagina, ook met een andere browsernaam). Daardoor kan ik binnen week 1 niets scheiden.

### Eerst: wat Valve eist voor het Desktop Companion Fest (GEZIEN, 16 nov)
- **Uitnodigen gaat vanzelf, op de tags en de winkelpagina.** "If your game does not that [sic] the Desktop Companion tag, then it is likely not eligible for this Fest." Op de ouderpagina: geschiktheid komt uit de tags "as well as the gameplay that is evident from how you describe and represent your game on your store page". Wie geen uitnodiging kreeg, kijkt op de opt-in-pagina en kan bezwaar maken.
- **Wat telt als bureaubladspel:** zit "unobtrusively" op een deel van het scherm (meestal onder of opzij), speelt door als je niets doet, meestal casual of idle. **Niet:** spellen die je alleen kleiner kunt maken, schermbeveiligers, software, pomodoro-timers, en spellen voor een heel tweede scherm of volledig scherm.
- **Demo's mogen, in een eigen vak**, en de demo wordt ingedeeld op de pagina van het volle spel ("keep tags for the base game up to date"). Maar: "Demos are generally not eligible to appear in the official event trailer", en "discounted released games will be featured most prominently".
- **Datums:** trailer van Valve 8 jan, fest 14 jan 10:00 PST tot 18 jan 10:00 PST. Livestreams staan niet op de festpagina, wel op je eigen winkelpagina.
- Wat dit voor Hats betekent: de tag Desktop Companion bovenaan (staat al in de planning van 30 nov) en de winkeltekst en schermen moeten de strook onderaan laten zien, anders kan Valve ons niet uitnodigen. In de festtrailer van Valve komen wij als demo waarschijnlijk niet.

### Tiny Pasture doet een vast lanceerprogramma (GEZIEN, aankondigingen)
Tiny Pasture (7.140 reviews, uitgever Gamersky Games) zette in 13 maanden **tien aankondigingen voor een bundel met een nieuwkomer**, zes daarvan op de dag van de uitgave of de dag erna:

| Nieuwkomer | Uit | Post Tiny Pasture | Dag | Wat | Zelfde uitgever |
|---|---|---|---|---|---|
| Maltese's Fluffy Onsen | 13 mei 2025 | 22 mei 2025 | 9 | bundel 10% | nee |
| Bugtopia | 21 mei 2025 | 22 mei 2025 | 1 | crossover plus bundel 10% | nee (GCORES) |
| Idle Waters | 12 jun 2025 | 12 jun 2025 | 0 | bundel 10% | nee |
| Village Tale | 27 jul 2025 | 28 jul 2025 | 1 | bundel 10% | nee |
| Lakeside Bar | 30 jul 2025 | 31 jul 2025 | 1 | bundel | nee |
| Sensei! I Like You So Much! | 1.0 op 5 aug 2025 | 5 aug 2025 | 0 | bundel | nee |
| Fischer's Fishing Journey | 7 aug 2025 | 8 aug 2025 | 1 | bundel 10% | **ja** (Gamersky) |
| Your Big, Cute Monster Farm | 10 nov 2025 | 11 nov 2025 | 1 | gastpersonage plus bundel | **ja** (Gamersky) |
| Tingus Goose | 1 dec 2025 | 10 feb 2026 | 71 | bundel | nee |
| Birdwatching Notebook | 26 mei 2026 | 10 jun 2026 | 15 | bundel 10% | nee |

- **Het is bijna altijd een bundel, geen ruil.** Alleen Bugtopia (andere uitgever) en Monster Farm (eigen uitgever) kregen er een personage bij. Wat Tiny Pasture als ruil doet met spellen van anderen, doet het vooral met grote, al uitgebrachte spellen (Sultan's Game, Backpack Battles bij hun 1.0, Ropuka, Sanfu bij zijn verjaardag; verhaal 16).
- **De tekst is één sjabloon voor beide kanten.** Idle Waters en Tiny Pasture zetten op 12 jun 2025 dezelfde zinnen ("If you would like to fish while petting animals, then don't miss this bundle", "Exclusive Bundle Deal", "instant 10% discount"). Ook bij de anderen steeds: één regel waarom het past, "10%", "double the fun", over elk spel twee zinnen. De nieuwkomer post zelf meestal dezelfde dag.
- 8 van de 10 zijn van een andere uitgever. Hoe het contact ontstond staat in geen enkele post (niet gevonden).

### Leverde de post van Tiny Pasture iets op? (GEZIEN, verval per week)
Bij zes partners viel de post in week 1, samen met de uitgave zelf: daar is het niet te scheiden (Sem had gelijk). Bij drie viel hij later, en daar kan ik de week van de post leggen naast hoe een lancering gewoon daalt:

| Partner | Post in | Reviews | Verhouding | Gewoon in deze hoek (70 spellen) |
|---|---|---|---|---|
| Maltese's Fluffy Onsen | week 2 (dag 9) | 487 dan 176 | 0,36 | week 2 tegen week 1: mediaan 0,31 (helft tussen 0,20 en 0,43) |
| Birdwatching Notebook | week 3 (dag 15) | 241 dan 108 | 0,45 | week 3 tegen week 2: mediaan 0,52 (helft tussen 0,37 en 0,61) |
| Tingus Goose | week 11 (dag 71) | 15, 17, 12 dan 23, 24 | ±1,6x | stijging van ±8 reviews per week; rond Chinees Nieuwjaar en de nieuwjaarsupdate van Tiny Pasture |

**Bij Maltese en Birdwatching zie je niets boven het gewone verval.** Bij Tingus Goose een klein beetje, maar in dezelfde week als een feestdag in China en een update van Tiny Pasture, dus niet toe te schrijven. En de zes die de post in week 1 kregen, houden het daarna niet beter vol dan de rest: reviews in week 5 tot 12 tegen week 1 tot 4 is bij hen 0,19 tot 0,51 (mediaan ±0,23), bij de rest mediaan 0,30. Hun eerste vier weken (172 tot 570 reviews) liggen rond en boven de mediaan van de groep (216), maar Tiny Pasture kiest zijn partners, dus dat zegt niets over de bundel.

Voor Sem, de manier die wel werkt: **een post na week 1 leggen naast het verval van 70 vergelijkbare lanceringen.** Voor een post in week 1 is er geen eerlijke maat zonder de verlanglijstcijfers van de maker.

### Drie lessen
1. **Tiny Pasture is een vaste lanceerpartner, geen gunst.** Tien nieuwkomers in 13 maanden, steeds hetzelfde sjabloon: bundel 10%, één zin waarom het past, posts aan beide kanten op dezelfde dag. Vragen is dus normaal; een crossover met personage is de uitzondering (1 keer bij een andere uitgever).
2. **Een bundelpost van een groot bureaubladspel geeft geen zichtbare golf.** Waar het te meten is (2 keer schoon), valt de week van de post binnen het gewone verval. Dat past bij verhaal 15 (Bottom-Of-Your-Screen) en 16 (crossovers): het spel zelf bepaalt de lancering, partners geven een plek op een pagina, geen kopers.
3. **Voor het fest tellen de tags en de winkelpagina, niet de demo.** Valve nodigt uit op de tag Desktop Companion en op wat de pagina laat zien, zet uitgebrachte spellen met korting het meest in beeld en neemt demo's meestal niet op in zijn trailer.

### Voorstel voor Dortus deze week
**Sem past in `marketing/bundels.md` de regel voor Tiny Pasture aan: vraag om hun gewone lanceerbundel (10%, beide kanten posten op de lanceerdag) en lever de tekst kant-en-klaar in hun sjabloon mee (twee zinnen per spel, één zin waarom ze passen); de gasthoed is een extra vraag, geen voorwaarde. Reken er in het lanceerplan op nul extra kopers: het is gratis en het geeft een plek op een pagina met 7.140 reviews, meer niet. Mila of Olaf: de winkeltekst en de eerste schermafbeelding van Hats moeten de strook onderaan het bureaublad laten zien, want Valve nodigt voor het fest uit op tags plus wat de pagina toont.** Kost niets; voorkomt dat we op een ruil rekenen voor groei.

### Eerlijk: wat ik niet weet
- Wat de bundels in week 1 deden: zonder reviews per dag en zonder verlanglijstcijfers is dat niet te zien.
- Of Tiny Pasture nee zegt tegen een spel zonder uitgever; alle tien hadden een studio of uitgever, hoe ze contact kregen staat nergens.
- Of bundels verkopen: Steam toont geen bundelverkopen. Reviews zijn een trage maat; extra verlanglijsten of volgers zie ik niet.
- Of de Desktop Companion-tag door Valve of door spelers moet komen: de pagina zegt alleen dat het spel hem moet hebben.

---

## 17. Wanneer zet je de demo live, en wanneer druk je op de mailknop? De ene e-mail die Steam stuurt bij een demo moet binnen 14 dagen na de demo, en ons plan (demo ma 4 jan) valt op de laatste dag van de Winter Sale; in 449 demo's van bureaubladspellen zie ik geen beste dag

**Vraag:** in het festplan van Sem gaat de demo van Hats op **ma 4 jan** openbaar, tien dagen vóór het Desktop Companion Fest (14 tot 18 jan), met dezelfde voorbereiding als dag 1 van het fest. Niemand in de repo had uitgezocht wat Steam op de dag van de demo doet met de verlanglijsten, en of de dag van de demo ertoe doet. Dat is nu uit te zoeken en het kost niets om het plan nog te verschuiven.

### Bronnen en hoe ik keek (16 nov, ±21:30 tot 22:15 UTC)
- Steamworks-docs, gelezen met curl op 16 nov: `partner.steamgames.com/doc/store/application/demos` (kopje "Triggering release notifications"), `doc/marketing/wishlist` (kopje "Wishlist Notifications"), `doc/marketing/upcoming_events/nextfest` (vragen over de demo) en `doc/marketing/upcoming_events/2026_winter_sale` (datum).
- Chris Zukowski, "What Steam's big demo update means for your marketing strategy", 31 jul 2024: https://howtomarketagame.com/2024/07/31/what-steams-big-demo-update-means-for-your-marketing-strategy/ (DERDEN).
- Eigen meting: alle 451 bureaubladspellen met een demo uit Vera's kaart (`platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv`). Per spel de demo-appid via `store.steampowered.com/api/appdetails`, en van die demo de datum waarop hij speelbaar werd (449 gelukt). Die datum gelegd naast de eerstvolgende Next Fest (feb, jun en okt van 2024 tot 2026). Uitkomst bij uitgebrachte spellen: reviews (uit de kaart); bij aangekondigde spellen: volgers (Vera's en Sems metingen van 16 nov, 127 van de 241). Data: `platformen/succes/data/demo-timing-bureaublad-2026-11-16.csv`, scripts `demo-timing-haal.py` en `demo-timing-analyse.py` in dezelfde map.

### Wat Valve zegt (GEZIEN, Steamworks-docs, 16 nov)
1. **Eén mail, alleen in de eerste 14 dagen.** Bij de demo: "This action is available on your demo app landing page for two weeks following the initial launch of your demo. You can only take this action once." Wie de knop niet indrukt, stuurt niets; wie de demo eerder uitbrengt, verliest de knop na twee weken.
2. **Wij kiezen het uur.** "The timing of this notification is under your control up to two weeks following the release of your demo." De mail hoeft dus niet op de dag van de demo.
3. **Hooguit één mail per twee weken per spel, en in drukke weken langer.** "Customers who have been notified about an appID within the last 2 weeks (...) will be on e-mail cooldown", en: "This period may be extended in periods of high notification traffic (such as Steam seasonal sales)." Plus: "if an email is held up for over a week for whatever reason, we will stop trying to send that email."
4. **De Winter Sale loopt van 17 december 2026 tot 4 januari 2027, 10:00 Pacific** (19:00 in Nederland). Onze demodag ma 4 jan valt dus nog in de uitverkoop, precies de drukke tijd waar Valve voor waarschuwt.
5. **De dag van de demo maakt Valve niet uit.** Next Fest-docs: "Our only requirement is that it is before the start of the event", "We do not require exclusivity or newness for your demo." Demo eerder, op de dag zelf of vlak ervoor noemt Valve "all valid strategies". Een fest stuurt zelf geen mail naar verlanglijsten (niet genoemd in de docs).
6. **Een demo kan vooraf een eigen "binnenkort"-pagina krijgen** en staat dan in de lijst met aankomende demo's (demos-docs, "Releasing for 'upcoming' visibility").

### Wat een maker erover zegt (DERDEN, Zukowski, jul 2024)
- Zijn advies sinds de mailknop er is: "Time the festival / streamer / wishlist email to occur on the same day and hour", zodat zoveel mogelijk mensen tegelijk de demo spelen en hij in New & Trending komt.
- Zijn voorbeeld CleanFall: 173 volgers en ±1.800 verlanglijsten vóór de demo, demo uit op 26 jul 2024, de dag erna in New & Trending, daarna van 1.800 naar 6.000 verlanglijsten. Een YouTuber (Olexa, 166K) speelde de demo meteen; hij zegt zelf dat niet te zien is wat het deed, de YouTuber of de mail.
- Hij raadt af de demo uit te brengen zolang je weinig verlanglijsten hebt, omdat je de mail maar één keer krijgt, en noemt de Steam-playtest als manier om vreemden eerst te laten spelen: "Playtests and Betas are NOT counted as a 'Demo Release'".
- Kanttekening: dit is 2024. Hoe druk New & Trending voor demo's nu is, weet ik niet.

### Wat de data zegt: geen beste dag (GEZIEN, 449 demo's)
Uitgebrachte spellen (demo na 31 jul 2024, minstens 2 maanden uit), reviews nu, naar dagen tussen demo en de eerstvolgende Next Fest:

| Demo vóór het fest | n | Mediaan reviews | Aandeel 100+ reviews |
|---|---|---|---|
| 0 tot 3 dagen (op of vlak voor dag 1) | 4 | 38,5 | 1 van 4 (Cornerpond, 2.602) |
| 4 tot 21 dagen | 28 | 14,5 | 11% |
| 22 tot 90 dagen | 42 | 19,5 | 24% |
| 91+ dagen | 6 | 104,5 | 3 van 6 |
| geen Next Fest tussen demo en uitgave | 28 | 6 | 18% |

Aangekondigde spellen (nu "binnenkort"), volgers op 16 nov:

| Demo vóór het fest | n | Mediaan volgers | Aandeel 100+ volgers |
|---|---|---|---|
| 0 tot 3 dagen | 24 | 15 | 17% |
| 4 tot 21 dagen | 36 | 46 | 33% |
| 22 tot 90 dagen | 39 | 22 | 13% |
| nog geen fest gehad (demo na 19 okt) | 22 | 5 | 0% |

**Het patroon draait om.** Bij de uitgebrachte spellen doet "4 tot 21 dagen vóór het fest" (dat is ons plan) het slechtst, bij de aangekondigde het best. Het verschil bij de uitgebrachte is ook niet hard (Mann-Whitney p = 0,37; 3 van 28 tegen 13 van 48 met 100+ reviews, Fisher p = 0,14). Conclusie: **in deze hoek bepaalt de dag van de demo de uitkomst niet zichtbaar.** Wat wel overal terugkomt: wie geen fest had tussen demo en uitgave, bleef laag (mediaan 6 reviews, 5 volgers), wat past bij verhaal 3 en 7.

De winnaars uit eerdere verhalen deden ook beide: Desktop Defender, Bongo Cat en Cornerpond zetten de demo live op dag 1 van een fest; Bao Bao 19 dagen vóór het Idler Fest en Character House een maand vóór Next Fest, buiten elk fest (verhaal 3 en 5, `marketing/character-house.md`).

Eerlijk over de meting: ik weet niet of elk spel echt meedeed aan het fest dat ik toeken (Valve geeft geen openbare deelnemerslijst van oude fests); spellen die hun demo bij de uitgave weghaalden ontbreken (bij de winnaars gebeurt dat vaak, verhaal 8); en of en wanneer iemand op de mailknop drukte, is van buiten niet te zien.

### Drie lessen
1. **De mail is het enige moment dat Steam zelf iedereen met Hats op de verlanglijst roept, en het venster is 14 dagen na de eerste demodag.** Wie de demo eerder dan 31 dec uitbrengt, kan de mail niet meer op 14 jan sturen.
2. **Mail niet in een seizoensuitverkoop.** Valve zegt zelf dat mails dan later gaan en na een week vervallen. Ma 4 jan vóór 19:00 Nederlandse tijd is nog Winter Sale.
3. **De dag van de demo is geen hefboom, het fest wel.** In 449 demo's is er geen beste afstand tot het fest; het verschil zit tussen wél en géén fest. Dus: de demo vroeg genoeg om fouten te vangen, en de klap (mail, makers, aankondiging) op één uur samen met het fest.

### Wat dit betekent voor Hats
Het plan van Sem (demo ma 4 jan, fest do 14 jan) past binnen het venster, met één aanpassing en één grens:
- **Demo live op ma 4 jan ná 19:00 Nederlandse tijd (einde Winter Sale) of di 5 jan, zonder mail.** Rustige dagen met echte spelers om fouten te vangen, zoals Sem wil (10+ demo-reviews).
- **Mailknop op do 14 jan om 19:00 Nederlandse tijd**, het uur dat het fest begint, samen met de aankondiging en de makers die de demo spelen. Dat is dag 9 of 10 van de 14, dus binnen het venster (laatste dag ±18 jan).
- **Grens: de demo niet vóór 31 dec openbaar**, anders sluit het venster vóór het fest. Schuift de demo naar voren (bijvoorbeeld 22 dec, direct na de keuring), dan valt de mail in de Winter Sale of vóór het fest. Liever een Steam-playtest voor vroege spelers en makers: die telt niet als demo (Zukowski, DERDEN).
- Next Fest in februari heeft geen eigen mail meer; daar trekt alleen het fest zelf. De lanceermail in maart staat los (die gaat bij uitbrengen, meer dan twee weken na januari).
- Wat ik niet weet: of een demo die 10 dagen oud is in het fest lager staat dan een nieuwe. Valve sorteert in een themafest op "player interest and popularity" (verhaal 9, Sem); nieuw zijn wordt niet genoemd.

### Voorstel voor Dortus deze week
**Sem past in `marketing/festplan.md` fase 2 en 3 aan: demo openbaar ma 4 jan na 19:00 NL (of di 5 jan) zonder mail, de mailknop op do 14 jan 19:00 NL, en de regel "demo niet vóór 31 dec openbaar". Olaf zet dezelfde grens in `planning-fest-2027.md` bij 21 dec (indienen is vroeg genoeg, openbaar maken pas 4 jan). Thijs drukt de knop zelf (hij beheert Steamworks): Sem zet hem met datum en uur op `organisatie/lijst-thijs.md` zodra de demo een appid heeft.** Kost niets, voorkomt dat we de enige mail in de Winter Sale of vóór het fest verspelen.

### Eerlijk: wat ik niet weet
- Hoeveel van de mensen met een spel op hun verlanglijst de demomail openen of de demo starten: Valve geeft geen cijfer, ik vond geen maker met een getal voor deze hoek.
- Of New & Trending voor demo's in 2026 nog werkt zoals bij CleanFall in 2024.
- Of het Desktop Companion Fest eigen eisen aan de demo stelt: de pagina van Valve voor dit fest gaf op 16 nov een foutmelding ("Sorry, an error occurred"). Volgende run opnieuw proberen.

---

## 16. Crossovers tussen bureaubladspellen: een gastpersonage uit een ander spel, 23 keer gemeten. Alleen met een veel groter spel en samen met een grote update zie je soms een sprong; twee kleine spellen samen geven niets, en "speel 5 minuten onze demo voor een beloning" moest Bongo Cat stoppen

**Vraag:** in verhaal 15 zag ik dat bureaubladspellen elkaar niet alleen bundelen maar ook personages lenen (Not Monday Cafe x Lakeside Bar). Levert zo'n crossover iets op, voor wie, en hoe komen makers eraan? Hats heeft hoeden van gevallen helden: een gasthoed uit een ander spel past precies in ons spel, dus dit is een vorm die wij later goedkoop kunnen doen.

### Bronnen en hoe ik keek (16 nov, ±21:20 tot 22:10 UTC)
- Alle aankondigingen (tot 300 per spel) van de 194 spellen met 50+ reviews uit Vera's kaart (`platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv`), via `api.steampowered.com/ISteamNews/GetNewsForApp/v2/`, met curl. Gezocht op "crossover" en "collab": 79 treffers, waarvan ±30 echte crossovers met een personage of voorwerp uit een ander spel.
- Reviews per week (of per maand bij grote spellen) via `store.steampowered.com/appreviewhistogram/<appid>`. Maat: gemiddelde reviews per week in de 4 weken vóór de crossover tegen de week ervan en de week erna. Bij Rusty's, Spirit City en Backpack Battles geeft Steam alleen maanden: maand ervoor tegen de maand van de crossover.
- Uitgevers en datums via `store.steampowered.com/api/appdetails`. Steam-regel: `partner.steamgames.com/doc/marketing/advertising` (gelezen 16 nov).
- Alle 23 metingen in `platformen/succes/data/crossovers-bureaublad-2026-11-16.csv`, met per regel of beide spellen van dezelfde uitgever zijn en wat er in dezelfde week nog gebeurde. Alles GEZIEN tenzij anders vermeld.

### Wat ik zag: drie soorten crossover

**1. Een klein bureaubladspel krijgt een personage van een groot spel (9 keer, verschillende uitgevers).**

| Bureaubladspel | Gast | Datum | Reviews per week ervoor, erna | Verhouding | Wat er nog meer gebeurde |
|---|---|---|---|---|---|
| Fish to Dish | Dave the Diver | 18 jun 2026 | 11,8 naar 42,5 | 3,6x | zelfde dag grote update 3.0 met nieuw gebied |
| Tiny Pasture | Sultan's Game | 7 mei 2025 | 86 naar 217 | 2,5x | niets gevonden in de aankondigingen; korting niet na te gaan |
| Rusty's Retirement | Balatro | 7 aug 2025 | 179 naar 280 per maand | 1,6x | 10% korting over en weer voor wie het andere spel heeft |
| Virtual Cottage 2 | Against the Storm | 22 aug 2026 | 20 naar 27,5 | 1,4x | twee weken eerder al een piek (41) |
| Rusty's Retirement | Vampire Survivors | 1 apr 2025 | 296 naar 295 per maand | 1,0x | maker Poncle vroeg het zelf |
| Tiny Pasture | Bugtopia | 22 mei 2025 | 138 naar 112 | 0,8x | dag na de lancering van Bugtopia |
| Spirit City | Lofi Girl | 25 mei 2026 | 194 naar 165 per maand | 0,85x | |
| Spirit City | Among Us | 26 jun 2025 | 558 naar 337 per maand | 0,6x | mei was hoger door iets anders |
| Tiny Pasture | Backpack Battles | 13 jun 2025 | 143 naar 80 | 0,56x | |

Drie van de negen gaven een duidelijke sprong (1,5x of meer). Bij alle drie was de crossover meer dan een plaatje: Fish to Dish bracht hem als grote update 3.0 met een nieuw gebied en 8 prestaties, Rusty's maakte een nieuwe kaart met een eigen spelregel uit Balatro (kaarten spelen bij het oogsten). Maar Rusty's deed precies hetzelfde met Vampire Survivors (nieuwe kaart, knoflook tegen vleermuizen) en daar zie je niets. Eerlijk: met deze aantallen en zonder kortingsgegevens kan ik niet zeggen wat het verschil maakte. Wat wel vaststaat: **een crossover met een groot spel is geen zekere golf; zes van de negen gaven geen zichtbare stijging.**

**2. Twee bureaubladspellen van gelijke grootte ruilen een personage (4 metingen).**
- Lakeside Bar x Not Monday Cafe (7 nov 2025, elk ±5 reviews per week): 1,05x en 0,95x. Ze ruilden een medewerker (Bobby en Angie) en zetten er een bundel met 20% korting bij. Niets te zien, aan geen van beide kanten.
- Tiny Pasture x Ropuka's Idle Island (26 en 27 jun 2025): 1,7x en 1,3x, maar op dezelfde dag begon de Steam-zomeruitverkoop, en Ropuka had die week ook een nieuwe bundel en drie nieuwe talen. Niet aan de crossover toe te schrijven.
- Sill Cats x DEBUG NEPHEMEE (5 nov 2026, DEBUG NEPHEMEE is nog niet uit): 0,9x voor Sill Cats.
- BuGarden x Mushroom Nook (aangekondigd 3 en 5 nov 2026, nog in de maak): nog niets te meten.

**3. Een groot spel geeft kleine spellen een plek (Bongo Cat, 31.301 reviews).** Bongo Cat deed van juni 2025 tot juni 2026 een reeks "indie collabs": wie 5 minuten de demo van een klein spel speelde (Let Them Trade, Cloudscrapers, Turnbound, The Berlin Apartment, STUNTBOOST, Mothkeep, MOLDRISE) kreeg een hoed of vel in Bongo Cat. Bij Bongo Cat zelf zie je niets (0,9x tot 0,97x, het spel is te groot). Bij de kleine spellen kan ik het niet meten: het waren demo's, en Steam bewaart geen oude spelersaantallen van demo's die ik kan lezen. Turnbound schreef in mei 2026 wel "depending on how you found Turnbound, we had an incredible Bongo Cat skin": een deel van hun spelers kwam er dus binnen (hoeveel zeggen ze niet).
En dan het belangrijkste: **op 27 jun 2026 zette Bongo Cat dit stop.** Hun eigen woorden: "We had to disable the incentivized rewards (f.e. collab with Nightwater or the wishlist ones) ... because it was against Steam Guidelines to incentivize this". Welke regel Valve precies noemde, zeggen ze niet. De openbare regel die er het dichtst bij komt (`partner.steamgames.com/doc/marketing/advertising`): "Developers should not use advertising as a way to provide value to players, such as giving players a reward for watching or engaging with advertising in their game." Op dezelfde pagina staat ook dat crossovers mogen en zelfs worden aangemoedigd: "These types of promotions are encouraged and many customers find value in them." Dus: een gastpersonage of gasthoed mag; een beloning voor het spelen van een demo of voor een verlanglijstje niet (mijn lezing, GOK op welke regel het precies was).

### Wat het patroon verbergt: veel "crossovers" zijn één uitgever
- **IndieArk** geeft Fish to Dish, Loafing Town, Backpack Battles, Peglin en MiSide uit. Fish to Dish kondigde bij zijn lanceerdatum (21 mei 2025) "enchanting collaborations" aan met MiSide, Backpack Battles en Peglin: allemaal eigen catalogus. Loafing Town x Backpack Battles (dec 2025, 0,21x): ook IndieArk.
- **Outersloth** (het fonds van de makers van Among Us) geeft Berserk B.I.T.S uit; Berserk x Among Us (mrt 2026, 3,5 naar 5 reviews per week) is dus in de familie.
- **Gamersky Games** geeft Tiny Pasture en Your Big, Cute Monster Farm uit; Tiny Pasture zette Monster Farm erin op de dag na diens lancering (3,6x voor Tiny Pasture, maar die week was ook Steam Animal Fest).
- Bongo Cat x OKU en Lakeside Bar x Seaside Wash zijn een eigen nieuw spel van dezelfde maker.
Een uitgever met een groot spel kan zijn kleine spellen dus een gastplek geven. Wij hebben geen uitgever; voor ons tellen alleen de paren tussen echt verschillende makers, en die zijn zeldzamer.

### Hoe makers aan een crossover kwamen (wat de bron zegt)
- **Rusty's x Vampire Survivors:** "the kind folks over at Poncle were playing my silly little game, and had the idea of 'What if Poe retired?'. They reached out". De grote maker speelde het kleine spel en vroeg het zelf. Daarna: "This collaboration has opened the doors to more opportunities", en vier maanden later kwam Balatro.
- **BuGarden x Mushroom Nook:** "Thanks to a wonderful coincidence (and a lovely introduction from players in our community!)". Spelers brachten de makers samen.
- **Bongo Cat:** steeds "a good friend of ours" of "our friends", en één keer een spel dat ze zelf uitgeven (Tap Tap Loot, Nightwater).
- **Tiny Pasture** deed er zes in een half jaar (Sultan's Game, Bugtopia, Backpack Battles, Ropuka, Sanfu, Monster Farm), twee daarvan op de dag na de lancering van het andere spel. Een groot bureaubladspel dat graag crossovers doet, is zelf een plek waar een nieuw spel kan aankloppen.

### Drie lessen
1. **Een crossover is een update, geen marketingtruc.** De drie sprongen kwamen bij een crossover die als grote update met nieuw spel kwam (Fish to Dish 3.0, Rusty's nieuwe kaart met eigen regel). Een plaatje ruilen tussen twee kleine spellen (Lakeside x Not Monday) gaf aan beide kanten niets. En ook de grote crossovers geven vaker niets dan wel (6 van 9).
2. **Grootte telt, en de grote kiest.** Alleen paren met een veel groter spel lieten soms iets zien. Rusty kreeg Vampire Survivors omdat Poncle zijn spel speelde; je wordt gevraagd als je spel goed genoeg is om op te vallen. Dat past bij verhaal 8, 12 en 15: het spel zelf bepaalt het, de hulpmiddelen vermenigvuldigen.
3. **Geen beloning voor een demo of verlanglijstje.** Het bekendste voorbeeld van een groot bureaubladspel dat kleine spellen hielp (Bongo Cat) moest dat na een jaar stoppen omdat het tegen de regels van Steam was. Een gastpersonage mag wel, en Valve moedigt het aan.

### Voorstel voor Dortus deze week
**Sem zet in `platformen/steam/marketing/bundels.md` (of een eigen kopje "Crossovers") drie regels: (1) nooit een beloning voor het spelen van onze demo, een verlanglijstje of een volg-actie, ook niet via een ander spel (Bongo Cat moest het in juni 2026 terugdraaien); als een groter spel ons zoiets aanbiedt, zeggen we nee en vragen we om een gastpersonage of een vermelding in hun update. (2) Een crossover pas na de lancering, als update met iets nieuws om te spelen, en alleen met een spel dat veel groter is dan wij; twee kleine spellen samen leveren niets op (Lakeside x Not Monday). (3) De natuurlijke vorm voor Hats is een gasthoed: een held uit een ander spel valt in ons hol en laat zijn hoed achter; en wij geven een hoed terug. Lijst van kandidaten die al crossovers doen met spellen van een andere maker: Tiny Pasture (zes in een half jaar), Rusty's Retirement, Spirit City, Bongo Cat (heeft hoeden).** Voor Olaf, geen haast: kan een hoed er later bij als databestand (beeld plus naam), zonder nieuwe code? Dan kost een gasthoed alleen beeld, en dat moet altijd van een mens of van de partner zijn (geen AI-beeld op Steam).

### Eerlijk: wat ik niet weet
- Kortingen: ik kan de prijsgeschiedenis niet lezen, dus een korting in dezelfde week kan elke sprong of daling verklaren (alleen de kortingen in aankondigingen staan in de CSV).
- Wat de kleine spellen in de Bongo-reeks er echt aan overhielden; hun demospelers zijn achteraf niet te zien.
- Of de sprong bij Tiny Pasture x Sultan's Game uit China kwam (beide Chinese makers); ik telde alle talen samen.
- Welke regel Valve precies tegen Bongo Cat gebruikte.
- Reviews zijn een trage maat; een crossover kan volgers of verlanglijstjes opleveren die pas later kopen. Die cijfers heeft alleen de maker.

---

## 15. Bottom-Of-Your-Screen van binnen: Rusty maakte de bundel op de lanceerdag van een ander spel, en daarna kwam bijna iedereen erin rond zijn eigen lancering (17 spellen, 37 archiefversies)

Onderzocht 16 nov 2026, run 16. Vervolg op verhaal 14, waar ik niet wist wie de groepsbundel begon, wanneer elk spel erin kwam en of het iemand iets opleverde. Sem schreef in `platformen/steam/marketing/bundels.md` "GOK eigenaar" bij Mister Morris Games; dat kan ik nu met een bron invullen.

### Bronnen
- **37 archiefversies van de bundelpagina** in het Internet Archive, van 31 jan 2025 tot 18 okt 2026 (lijst: `web.archive.org/cdx/search/cdx?url=store.steampowered.com/bundle/48558*`), per versie de spellen erin geteld (GEZIEN, 16 nov ±19:35 UTC). Een spel kwam erin tussen de laatste versie zonder en de eerste versie met; de vensters zijn 1 tot 10 weken breed.
- Aankondiging van Rusty's Retirement van 31 jan 2025, "Steam trading cards and more!", via de nieuws-API: `api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=2666510` (GEZIEN). Ook alle aankondigingen van de 17 andere spellen doorzocht op "bottom of your screen" en de bundellink.
- Reviews per week van alle 18 spellen uit de grafiek van de winkel: `store.steampowered.com/appreviewhistogram/<appid>?l=english&review_score_preference=0` (GEZIEN; de totalen kloppen precies met de winkel, dus alle talen). Deze route werkt wel, waar `appreviews` doorstuurt naar de voorpagina.
- Welke bundels nu op de winkelpagina van elk spel staan (GEZIEN, 16 nov, `store.steampowered.com/app/<appid>/`).
- Alles per spel in `platformen/succes/data/bottom-of-your-screen-instap-2026-11-16.csv`.

### Wie begon hem, en hoe (GEZIEN)
Rusty's maker zette op **31 jan 2025** onderaan een gewone update over ruilkaarten: "we have our first "bottom-of-your-screen" game to release after Rusty! My Little Life ... We've bundled together so you can get an additional -20% off My Little Life if you already own Rusty's Retirement!" met de link naar de bundel. Die dag kwam My Little Life (9FingerGames) uit. De bundel begon dus als **twee spellen op de lanceerdag van het kleinste**, en de aankondiging ging naar iedereen die Rusty volgt. Daarna is hij nooit meer genoemd in een aankondiging van Rusty, en ook niet in die van de 16 anderen (0 treffers).

Het mechaniek is "Complete the set": wie Rusty al heeft, betaalt voor de rest 20% minder. Voor de bundel staan nu 17 spellen, $97,83 voor $78,23 (GEZIEN).

### Wanneer kwam elk spel erin (GEZIEN, archief)
| Spel | Uit | Erin, gerekend vanaf de uitgave | Reviews nu |
|---|---|---|---|
| My Little Life | 31 jan 2025 | dag 0 (bundel gemaakt) | 1.089 |
| Tiny Pasture | 17 feb 2025 | dag -10 tot 2; **weer eruit** tussen 29 mei en 30 jun 2025 | 7.366 |
| Desktop Cat Cafe | 6 mrt 2025 | dag -15 tot 17 | 90 |
| Cornerpond | 21 apr 2025 | dag -14 tot 7 | 2.674 |
| Maltese's Fluffy Onsen | 13 mei 2025 | dag -15 tot 11 | 2.938 |
| Nanomon | 24 jun 2025 | dag -26 tot 6 | 117 |
| My Little Spider | 7 nov 2025 | dag -3 tot 36 | 419 |
| Emberlands | 20 jan 2026 | dag -20 tot 18 | 29 |
| Not Monday Cafe | 22 jun 2025 | dag 8 tot 31 | 573 |
| Ropuka's Idle Island | 29 jan 2025 | dag 21 tot 53 | 4.204 |
| Spacenap | 10 okt 2025 | dag 25 tot 64 | 43 |
| Milly's Meadow | 3 jul 2025 | dag 28 tot 66 | 52 |
| Sin Slayers: Meat & Greed | 25 sep 2025 | dag 40 tot 79 | 61 |
| Fish to Dish | 16 jun 2025 | dag 45 tot 83 | 2.738 |
| Idle Waters | 12 jun 2025 | dag 49 tot 87 | 364 |
| Card Corner | 9 mrt 2026 | dag 104 tot 173 | 81 |
| Desktop Defender | 4 nov 2025 | dag 229 tot 298 | 1.830 |

- **Geen enkel spel stond erin vóór zijn uitgave.** Dat past bij wat Sem in de Steamworks-docs las: een bundel kan pas als alle spellen uit zijn.
- **8 van de 17 kwamen erin in hun lanceerweken** (het venster begint vóór of op de uitgavedag en eindigt hooguit 5 weken erna), 7 in de eerste drie maanden, en alleen de twee spellen van Conradical Games (Desktop Defender en Card Corner) veel later, samen in de zomer van 2026. Instappen is dus vooral een **lanceerding**, en een spel met 29 reviews (Emberlands) of 43 (Spacenap) mocht ook mee. Er is geen drempel te zien.
- Tiny Pasture (uitgever Gamersky) ging er na ±3 maanden weer uit en heeft nu drie eigen Gamersky-bundels op zijn pagina. Waarom, staat nergens (GOK: hun eigen bundels gingen voor, want een pagina toont er hooguit drie).

### Leverde instappen iets op?
Bij wie later instapte, kan ik voor en na vergelijken: reviews in de 4 weken vóór het venster tegen de 4 weken erna (GEZIEN, weekgrafiek).

| Spel | 4 weken voor | 4 weken na |
|---|---|---|
| Ropuka's Idle Island | 703 | 227 |
| Not Monday Cafe | 127 | 48 |
| Fish to Dish | 166 | 109 |
| Idle Waters | 41 | 18 |
| Spacenap | 24 | 3 |
| Sin Slayers | 8 | 3 |
| Milly's Meadow | 4 | 3 |
| Card Corner | 2 | 5 |
| Desktop Defender | 22 | 29 |

**Bij geen enkel spel zie je een sprong.** De meeste zakken gewoon verder na hun lancering; de twee kleine stijgingen (Card Corner +3, Desktop Defender +7) vallen binnen wat een week schommelt. Eerlijk: dit is een grove meting. De vensters zijn weken breed, de daling na een lancering is groot, en een klein effect (een paar kopers per week) zie ik hier niet. Wat ik wel kan zeggen: instappen in Bottom-Of-Your-Screen gaf **niemand een golf**.

En bij wie in de lanceerweken instapte, liep het van 19 tot 2.618 reviews in de eerste 4 weken na de uitgave (Emberlands 19, Desktop Cat Cafe 34, Nanomon 80, My Little Life 558, Cornerpond 798, Maltese 821, Tiny Pasture 2.618; alle 17 in de CSV). De bundel bepaalt de lancering niet; het spel zelf wel.

### Waar de bundel staat (GEZIEN, 16 nov)
De bundel staat op de winkelpagina van **11 van de 17 leden**: Rusty, Ropuka, My Little Life, Not Monday Cafe, My Little Spider, Idle Waters, Nanomon, Desktop Cat Cafe, Sin Slayers, Milly's Meadow en Spacenap. **Niet** op Cornerpond, Maltese's Fluffy Onsen, Fish to Dish, Desktop Defender, Card Corner en Emberlands: juist de grotere leden na Rusty en Ropuka tonen liever hun eigen paren (Cornerpond en Card Corner delen bundel 69746, Desktop Defender en Card Corner bundel 46375 van één maker). De zichtbaarheid zit dus bij Rusty (14.460 reviews) en Ropuka (4.204); de rest geeft vooral kleintjes door aan elkaar.

### Wat makers wél deden rond hun lancering (GEZIEN, aankondigingen)
- **Nanomon** zette de dag na zijn lancering "Bundles! Bundles! Bundles!": paren met Bugaboo Pocket, Ropuka, Maltese's Fluffy Onsen, Spirit City en Rain World, elk met één zin waarom ze bij elkaar passen ("Maybe there are some Nanomon who would help out by eating the grass?").
- **Not Monday Cafe** deed een bundel en daarna een crossover met Lakeside Bar (31 jul en 7 nov 2025); **Maltese's Fluffy Onsen** maakte vier paren in een jaar (met Tiny Pasture, Volcano Princess, Cat God Ranch, Tap Tap Loot), elk met een eigen aankondiging.
- **Emberlands** gaf op 16 jun 2026 een "Shoutout" aan een ander bureaubladspel (Tiny Capsule Collector), zonder bundel. Rusty deed iets vergelijkbaars in 2024 voor Outcore, een gratis bureaubladspel waarvan de maker hem hielp met een fout.
- Patroon: de bundel zelf doet stil zijn werk op een pagina; **de aankondiging** is het moment dat het andere publiek het hoort.

### Drie lessen
1. **Bottom-Of-Your-Screen is een lanceerclub, geen groeimotor.** Rusty maakte hem voor de lanceerdag van een ander spel, 15 van de 17 stapten in binnen drie maanden na hun uitgave, en bij wie later instapte zie je geen sprong. Instappen is goed voor een plek op de pagina van Rusty, niet voor een golf.
2. **Kleine spellen zijn welkom.** Emberlands (29 reviews), Spacenap (43) en Milly's Meadow (52) staan erin. De drempel is "uit en een bureaubladspel", niet een aantal reviews. Wachten tot we festcijfers hebben om indruk te maken is dus niet nodig; het ging steeds om het moment van uitkomen.
3. **Het effect zit in de aankondiging, niet in de bundel.** De enige keer dat Rusty zijn volgers erover vertelde, was op de lanceerdag van My Little Life (558 reviews in de eerste 4 weken, plek 6 van de 17 leden; Tiny Pasture had er 2.618 zonder zo'n post, dus de post maakte geen wonder). Paren die werken zoals bij Hero Town (verhaal 14) en Nanomon gaan samen met een aankondiging naar beide publieken.

### Voorstel voor Dortus deze week
**Sem past in `platformen/steam/marketing/bundels.md` twee dingen aan: (1) eigenaar Bottom-Of-Your-Screen is Mister Morris Games (GEZIEN, hun eigen aankondiging van 31 jan 2025), en de vraag gaat het best ±2 weken vóór de lanceerdatum weg, zodat Hats er op dag 1 in staat zoals Cornerpond en Maltese; festcijfers zijn welkom maar geen voorwaarde (Emberlands mocht met 29 reviews). (2) De echte hefboom is een aankondiging: vraag Mister Morris niet alleen om de bundel, maar of Rusty een regel over Hats in zijn eerstvolgende update wil zetten, zoals hij voor My Little Life deed; en zet in onze eigen lanceerweek één post "Bundles!" zoals Nanomon, met per paar één zin waarom het past.** Thijs verstuurt de vraag (al op het plan van Sem). Kanttekening: of Rusty dat nog doet weet ik niet; hij deed het één keer in 21 maanden.

### Eerlijk: wat ik niet weet
- Of instappen een klein effect gaf (een paar kopers per week); mijn meting ziet alleen golven.
- Waarom Tiny Pasture eruit ging, en of Mister Morris ooit iemand weigerde.
- Of Valve het verkeer via een bundel op andermans pagina ergens laat zien; dat staat alleen in de cijfers van de makers zelf.
- Welk deel van de 558 reviews van My Little Life door de post van Rusty kwam.

---

## 14. Wie maakte Mini Cozy Room groot in Korea en China? Geen YouTuber: uitverkopen, updates en bundels met andere bureaubladspellen (plus de groepsbundel "Bottom-Of-Your-Screen" van Rusty en 16 anderen)

Onderzocht 16 nov 2026, run 15. Vervolg op verhaal 12, waar ik niet wist wie de Koreaanse en Chinese spelers bracht. Ik zocht een streamer of YouTuber en vond die niet. Wat ik wel vond: de pieken per taal vallen precies op uitverkopen, updates en een bundel met een ander bureaubladspel op de lanceerdag daarvan. Dat zette me op het spoor van bundels tussen makers, iets wat nog nergens in onze repo staat.

### Bronnen
- Reviews per taal met datum: 3.149 reviews (Koreaans 1.093, Vereenvoudigd Chinees 953, Engels 834, Traditioneel Chinees 269) van de communitypagina, nieuwste eerst, per taal helemaal doorgebladerd: `steamcommunity.com/app/3511030/homecontent/?browsefilter=mostrecent&filterLanguage=<taal>` (GEZIEN, 16 nov ±19:30 UTC). Het zijn er iets meer dan op de winkelpagina, omdat de communitypagina ook reviews van sleutels buiten Steam toont. Per maand in `platformen/succes/data/mini-cozy-room-azie-2026-11-16.csv`.
- Spelers tegelijk, hoogste per maand: https://steamcharts.com/app/3511030/chart-data.json en van Crusaders Quest: Hero Town https://steamcharts.com/app/4126220/chart-data.json (GEZIEN).
- Aankondigingen via de nieuws-API van Mini Cozy Room (59), Hero Town en Spirit City (GEZIEN). Citaat Hero Town uit de lanceerpost van 31 mrt 2026.
- YouTube-zoekresultaten op meeste weergaven, in het Koreaans, Chinees, Japans en Engels (GEZIEN, `youtube.com/results?search_query=...&sp=CAM%253D`).
- Bundelpagina's: https://store.steampowered.com/bundle/48558/ (Bottom-Of-Your-Screen), /bundle/53728/ (Spirit City + Mini Cozy Room), /bundle/71607/ (Cute Pixels on your Screen), en welke bundels op de winkelpagina's van Rusty, Ropuka, Desktop Defender en Spirit City staan (GEZIEN).
- Regels van Valve voor bundels: https://partner.steamgames.com/doc/store/application/bundles en /bundles/collaborative (GEZIEN, gelezen 16 nov 2026).
- Prijzen in dollar, yuan en won van 20 spellen via appdetails (GEZIEN).
- Eén Koreaans bericht op X van een gewone speler, 24 feb 2026 (GEZIEN via zoekresultaat): https://x.com/lucky__roba/status/2026280427225530808
- Niet gelezen: Bilibili (de zoek-API gaf een foutpagina), arca.live en andere Koreaanse fora (blokkade van Cloudflare), Xiaohongshu, Chzzk en SOOP (Koreaanse streamsites). Een Chinese of Koreaanse streamer kan ik dus niet uitsluiten; op YouTube was er geen grote.

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Grootste YouTube-video ooit over het spel | 113.066 weergaven, maar dat is een Koreaans overzicht van **17** cozy spellen die eraan kwamen (디지털포커스게임, ±1 jaar oud); de tweede is ook een lijst (41.465, 32 spellen) | GEZIEN |
| Grootste video over alleen dit spel | Engelse trailer van de makers 13.260; daarna ±8.000 (The Curliest Fry, FullThrough). In het Chinees hooguit 1.586 | GEZIEN |
| Hoogste spelers tegelijk per maand | okt 2025 2.805, feb 2026 3.176, mrt 3.895, **apr 2026 9.093**, mei 4.804, daarna 3.100 tot 4.800 | GEZIEN |
| Reviews oktober 2025 (update 1.04 met nieuwe kamer, op 15 okt; DLC van muzikant nawhij op 22 okt) | Koreaans 80, Chinees 58, Engels 82 (maand ervoor 40, 18, 17) | GEZIEN |
| Reviews week van 24 nov 2025 (valt samen met de herfstuitverkoop van Steam; de data van die uitverkoop heb ik niet nagekeken, GOK) | Koreaans 34, Chinees **76**, Engels 56 (week ervoor 5, 6, 4) | GEZIEN |
| Reviews 16 feb tot 8 mrt 2026 (samen werken op 13 feb, 40% korting op 24 feb: ₩2.940 in plaats van ₩4.900) | Koreaans **89**, Chinees 37, Engels 27: alleen Korea sprong | GEZIEN |
| Reviews 30 mrt tot 19 apr 2026 (verjaardag "Biggest Sale Ever" op 31 mrt, **en** de lancering van Hero Town met een bundel met Mini Cozy Room) | Koreaans 121, Chinees **149**, Engels 82; april is voor Chinees de grootste maand ooit (169) | GEZIEN |
| Hero Town (CQ LABS; Crusaders Quest is een Koreaanse mobiele reeks, dat CQ LABS Koreaans is, is een GOK) | uit 30 mrt 2026, $6,99, 2.717 reviews, 75%; hoogste spelers apr 6.265 | GEZIEN |
| Prijs Mini Cozy Room in China en Korea | ¥19,99 en ₩4.900, terwijl vijf andere spellen van $4,99 ¥22 en ₩5.600 vragen. Ropuka ($3,99) vraagt ¥15 en ₩3.250, ook onder wat de anderen van $3,99 vragen (¥18, ₩4.500) | GEZIEN; dat ¥22 en ₩5.600 de standaard van Valve is, is een GOK uit de meest gebruikte prijs |

### Wat er gebeurde, in volgorde
1. **Vóór de lancering (mrt 2025): op lijstjes, niet in eigen video's.** De twee grootste Koreaanse video's zijn overzichten van aankomende cozy spellen. Het spel liftte mee op een lijst die mensen opzochten, net als de PC Gamer-lijst in verhaal 7.
2. **Juni 2025: twee bundels.** Eén met de eigen DLC (All-in-One, 20% extra korting, aangekondigd 3 jun) en één met **Spirit City: Lofi Sessions**, de grootste lo-fi werkplek op Steam (16.166 reviews, 97%), voor 10% korting. Die tweede is nergens aangekondigd. Belangrijk detail: op de pagina van Spirit City staat hij **niet** (daar staan drie andere bundels), alleen op de pagina van Mini Cozy Room. Valve toont hooguit drie bundels per spel, "the top selling bundles based on revenue", tenzij de maker er zelf een vastzet (Steamworks-docs, GEZIEN). Een bundel met een groot spel helpt dus alleen als dat grote spel hem ook laat zien.
3. **Okt en nov 2025: update en uitverkoop.** Een nieuwe kamer en een DLC met een bekende lo-fi muzikant gaven in alle drie de talen een verdubbeling; de herfstuitverkoop daarna vooral in het Chinees.
4. **13 feb 2026: samen werken, 5 talen en banners naar hun andere spellen.** In het menu kwamen knoppen naar Task Bar Hero en Panoptyca (aankondiging 1.05.00, GEZIEN). Op 24 feb was het 40% afgeprijsd in Korea en een gewone speler schreef op X "컴퓨터 작업 많이 하는 트친들에게 추천" (aanrader voor wie veel achter de computer werkt) met de prijs erbij. Alleen het Koreaans sprong: 89 reviews in drie weken tegen 37 Chinees en 27 Engels. Mijn lezing (GOK): samen werken met vrienden sloeg in Korea het eerst aan, waar het spel vandaan komt.
5. **31 mrt 2026: alles op één dag.** Mini Cozy Room wordt een jaar en zet zijn "biggest sale ever" aan. Dezelfde dag lanceert Hero Town, een ander bureaubladspel met kleine pixelfiguren, uit een Koreaanse reeks, en zet in zijn lanceerpost: "Promotion 2: 10% Bundle Discount (Cute Pixels on your Screen) A bundle discount is available together with Mini Cozy Room : Lo-Fi." Die post gaat naar iedereen die Hero Town volgde. April: 9.093 spelers tegelijk, de grootste maand in reviews. Welk deel van de uitverkoop kwam en welk deel van de bundel, kan ik niet scheiden.
6. **Daarna:** Hero Town maakte nog twee bundels, met **Deskrawl** en met Duelist: Idle Expedition (bundelpagina's op de winkelpagina van Hero Town, GEZIEN). Bureaubladspellen bundelen dus kruislings met elkaar, ook met concurrenten.

### De groepsbundel "Bottom-Of-Your-Screen" (GEZIEN)
Op de winkelpagina van Rusty's Retirement (14.460 reviews) staat een bundel van **17 bureaubladspellen**, 20% korting: "Looking for more games to play at the bottom of your screen? We've assembled this small collection of games you can play while doing other things!" Mister Morris Games (Rusty) staat als eerste maker; wie hem begon zegt de pagina niet. Erin: Rusty's Retirement, Ropuka's Idle Island, Desktop Defender, Maltese's Fluffy Onsen, Fish to Dish, Cornerpond, My Little Life, Not Monday Cafe, My Little Spider, Idle Waters, Nanomon, Desktop Cat Cafe, Card Corner, Milly's Meadow, Sin Slayers: Meat & Greed, Spacenap en Emberlands. Mini Cozy Room zit er niet in.
- Reviews van de leden: 14.460, 4.204, 2.938, 2.738, 2.674, 1.830, 1.089, 573, 419, 364, 117, 90, 81, 61, 52, 43, 29. **Mediaan 419.** Ter vergelijking: de helft van de betaalde bureaubladspellen van mei tot aug 2026 heeft 4 reviews (Vera, `platformen/verkenner/steam-desktop-2026-11.md`).
- Eerlijk: dat zegt niet dat de bundel ze groot maakte. Grote spellen worden eerder gevraagd, en vijf leden staan nog onder de 100. Ik weet niet wanneer elk spel erbij kwam, dus vóór en na kan ik niet meten.
- Wat wel vaststaat: de bundel staat op de pagina's van Rusty en Ropuka (GEZIEN), twee van de drukst bezochte bureaubladpagina's, en wie hem opent ziet alle 17 spellen met hun capsule. Op de pagina van Desktop Defender staat hij niet (die toont drie eigen bundels).

### Wat Valve zegt over bundels tussen makers (GEZIEN, Steamworks-docs)
- Een "Collaborative Bundle" mag spellen van verschillende makers bevatten. Iedere deelnemer keurt elke wijziging goed; de opbrengst telt gewoon als verkoop van elk spel apart, zonder afspraken over verdelen.
- Valve geeft zelf de vraag mee: "Does your game appearing on the other game's Steam product page make sense?"
- Een bundel staat op de winkelpagina van elk spel erin, maar hooguit drie per pagina, op omzet of vastgezet door de maker.
- Een bundelkorting stuurt geen bericht naar wie het spel op zijn verlanglijst heeft. Het is dus zichtbaarheid op andermans pagina, geen mailtje.
- Of een bundel kan met een spel dat nog "binnenkort" is, staat er niet duidelijk; de docs zeggen alleen dat de voorvertoning onvolledig is zolang niet alles uit is. Hero Town zette zijn bundel live op de lanceerdag.

### Drie lessen
1. **Bij dit spel kwamen Korea en China niet van YouTube.** Geen video over alleen dit spel haalde 15.000 weergaven, en toch 3.830 reviews, waarvan 57% Koreaans of Chinees (beide schriften, verhaal 12). De pieken vallen op updates, uitverkopen en een bundel. Dat is anders dan Rusty (verhaal 4, grote Koreaanse video) en TBH (verhaal 11); er zijn dus twee wegen naar Azië, en de tweede (in de winkel zelf) is voor ons zonder Thijs voor te bereiden.
2. **Bureaubladspellen zetten elkaar op hun winkelpagina.** Spirit City met Mini Cozy Room, Hero Town met Mini Cozy Room, Deskrawl en Duelist, en 17 spellen samen in Bottom-Of-Your-Screen. Het kost niets, de opbrengst telt per spel, en een speler die één taakbalkspel koopt, wil er vaak meer (dat zegt de tekst van de groepsbundel letterlijk). Maar: het helpt alleen als het grotere spel de bundel ook laat zien.
3. **Prijs per land telt mee.** Mini Cozy Room en Ropuka, twee spellen waar Korea en China de grootste talen zijn, vragen daar 10 tot 30% minder dan wat de anderen van dezelfde dollarprijs vragen. Of dat de oorzaak is, weet ik niet (GOK); het is wel wat beide doen.

### Wat dit betekent voor Hats
- Wij lanceren in maart in een hoek met tientallen kleine spellen. Een bundel met twee of drie grotere bureaubladspellen zet Hats op een pagina waar al kopers van ons soort spel komen, en een plek in Bottom-Of-Your-Screen zet Hats op de pagina van Rusty.
- Onze haak (hoeden, helden die vallen) past naast een rustig spel als Rusty of Ropuka: "iets anders voor onderaan je scherm". Naast Deskrawl of Desktop Defender zijn we een concurrent, al bundelde Hero Town ook met Deskrawl.
- De prijs in yuan en won is een keuze voor het moment dat we de prijs zetten, niet nu.

### Voorstel voor Dortus deze week
**Sem zet in `platformen/steam/marketing/` een bundelplan klaar voor de lancering in maart: (1) een korte Engelse vraag aan de makers van Bottom-Of-Your-Screen of Hats erbij mag zodra het uit is, (2) een lijst van 3 spellen voor een eigen bundel op de lanceerdag, met per spel of zij de bundel op hun pagina zouden laten zien (spellen die nu minder dan drie bundels hebben eerst), en (3) de tekst voor onze lanceerpost met een "Promotion 2"-regel zoals Hero Town.** Thijs verstuurt de vragen (staat op zijn lijst als de pagina live is); er hoeft niets gebouwd. Waarom: de grootste maand van Mini Cozy Room viel op de dag dat een ander spel een bundel met hen in zijn lanceerpost zette, en de groepsbundel staat op de pagina van het grootste spel in onze hoek. Kanttekening: geen belofte dat het werkt; ik kon het effect van de bundel niet los meten van de uitverkoop.

Kleine punt voor wie de prijs zet (Olaf en de hoofdchat, bij de winkelpagina): kijk naar de prijs in yuan en won naast de dollarprijs; de spellen met veel Aziatische spelers zitten daar onder wat de anderen vragen. Cijfers in de CSV.

### Eerlijk: wat ik niet weet
- Of er een Chinese of Koreaanse streamer achter een piek zat; Bilibili, Koreaanse fora en streamsites kon ik niet lezen.
- Hoeveel van april door de bundel met Hero Town kwam en hoeveel door de eigen uitverkoop.
- Wanneer elk spel in Bottom-Of-Your-Screen kwam, en of iemand er meer door verkocht.
- Of Valve een bundel toestaat met een spel dat nog niet uit is.
- Wat de prijsstandaard van Valve in yuan en won is; ik leidde hem af uit wat de meeste spellen vragen.

---

## 13. Little Writer Desktop Companion (JSLegendDev, solo): eerst de Steampagina, dan één video; 1.295 volgers zonder fest, terwijl zijn vorige spel met een even grote video op 12 bleef

Onderzocht 16 nov 2026, run 14. Een concurrent in ons venster (uit 6 jan 2027, acht dagen vóór ons fest) en het mooiste natuurlijke experiment dat ik tot nu toe vond: dezelfde maker, hetzelfde YouTube-kanaal, twee spellen. Bij het eerste spel maakte hij een grote video zonder Steampagina, bij het tweede zette hij de pagina eerst live. Hij schreef zelf op wat er misging.

### Bronnen
- Zijn eigen stuk "My Biggest Gripe With YouTube", 30 mei 2026: https://jslegenddev.substack.com/p/my-biggest-gripe-with-youtube (GEZIEN, helemaal gelezen via de Substack-API).
- Zijn spellenblog: https://jslegenddevgames.substack.com, drie posts (15 en 17 mei, 21 jun 2026) met de 10 reacties onder de aankondiging (GEZIEN).
- YouTube-kanaal @JSLegendDev: abonnees en alle Shorts van het spel van de kanaalpagina's, weergaven per video uit de openbare feed https://www.youtube.com/feeds/videos.xml?channel_id=UCcDQenwAOcjJFyrJvjlrVVw (GEZIEN, 16 nov ±16:30 UTC). De videopagina's zelf gaven een blokkade van Google, dus lengte en reacties van de trailer heb ik niet.
- Steam: appdetails van het spel (4672770), de demo (5236990) en zijn vorige spel Donovan's Demise (4393750); volgers via `steamcommunity.com/games/<appid>/memberslistxml/?xml=1`; nieuws-API; spelers tegelijk; reviewtelling van de demo op de winkelpagina (GEZIEN, 16 nov).
- Volgers een dag eerder en de plek in de Top Wishlisted: https://www.indiespade.com/game/4672770 (DERDEN).
- Ter vergelijking: Vera's volgers van 222 aangekondigde bureaubladapps (`platformen/verkenner/data/steam-volgers-2026-11-16.jsonl`) en Sems meting van 245 demo's (`platformen/steam/marketing/data/demo-spelers-2026-11-16.csv`).
- Alle cijfers in `platformen/succes/data/little-writer-2026-11-16.csv`.
- Niet gelezen: Reddit (gaf een blokpagina), X en Discord. Ik weet dus niet of hij de trailer ook buiten YouTube deelde.

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Maker | JSLegendDev, solo; maakte 3 jaar lang JavaScript-lesvideo's | GEZIEN (eigen stuk) |
| Kanaal | ±17.000 abonnees | GEZIEN |
| Het spel | "Your little companion is an ambitious writer with very little discipline. Type, and they'll write too." Elke toetsaanslag van jou laat het figuurtje schrijven; boeken af, geld, sneller typen, betere kwaliteit, grotere projecten, nieuwe plekken en kleding | GEZIEN (winkeltekst) |
| Steampagina live | uiterlijk 21 jun 2026 ("the Steam page is up!") | GEZIEN |
| Aankondigingstrailer, 13 jul 2026 | **378.314 weergaven, 17.504 duimpjes**: 22 keer zijn aantal abonnees | GEZIEN |
| Demo, 22 sep 2026 | demotrailer 91.393 weergaven; **97 reviews, 100% positief** (33 in de laatste 30 dagen); nu 81 spelers tegelijk, om 12:40 UTC 68: plek 6 van 245 demo's van aangekondigde bureaubladapps | GEZIEN |
| Shorts over het spel | 14 stuks, meestal 1.000 tot 2.500 weergaven; uitschieters: "App Focus Feature" 21.220, de trailer als Short 19.141, "Why Does My Game Look Like That?" 9.262 | GEZIEN |
| Releasedatum-video, 26 okt | 1.462 weergaven | GEZIEN |
| **Volgers op Steam** | **1.295** (15 nov 1.248 volgens indiespade). Van de 222 aangekondigde bureaubladapps die Vera mat heeft alleen 3 er meer (Character House 9.732, Amarillo's Desktop Pets 5.822, Meowniverse 1.435). Mediaan van de 88 die op Hats lijken: 10 | GEZIEN, DERDEN |
| Top Wishlisted op Steam | plek 1.848 | DERDEN |
| Verlanglijsten | ±9.000 tot 26.000 (1.295 volgers keer 7 tot 20, de verhouding van GameDiscoverCo uit Vera's kaart) | GOK |
| Aankondigingen op Steam | 1 (de releasedatum, 26 okt); geen routekaart, geen devlog op Steam | GEZIEN |
| Talen | alleen Engels; Windows en Mac beloofd | GEZIEN |
| Prijs | nog niet bekend | GEZIEN |
| **Zijn vorige spel, Donovan's Demise** | video "Making a Small RPG" "barely below 100k views", toen zonder Steampagina; de volgende video erover "below 10k"; de pagina staat nu op "Coming soon" met **12 volgers**; het spel ligt stil ("currently on hold", 22 jun) | BRON (eigen stuk), GEZIEN |

### Wat hij deed, in volgorde
1. **2023 tot 2025: lesvideo's van 4 tot 10 uur**, die steeds minder gingen doen. Toen verhalende video's van 10 tot 15+ minuten, eerst als artikel geschreven: "How do Devs Make Levels Without Game Engines?" (30k+) en "You Can Now Make PS2 Games in JavaScript" (100k+). Zijn verklaring: het onderwerp moet "remarkable" zijn, het moet een verhaal zijn, en langer dan 10 minuten (BRON).
2. **Eind 2025: "Making a Small RPG"**, het verhaal van hoe hij zijn eerste eigen spel ontwierp, bijna 100k weergaven. "I had made a big mistake by not setting up a Steam page to direct viewers to before publishing the video." De tweede video over hetzelfde spel: onder de 10k. "I had wasted my biggest marketing ammunition" (BRON). Dat spel heeft nu 12 volgers.
3. **15 tot 17 mei 2026: eerst testen, dan pas Steam.** Een ander idee (HARVEST MOVE) zette hij als prototype in de browser op itch.io: "I think this would be a smarter choice rather than going immediately for Steam" (GEZIEN). Daar hoorde ik daarna niets meer van.
4. **30 mei: zijn conclusie.** YouTube geeft bereik maar geen publiek: "I was building a sand castle". Nieuw plan: zelden een sterke video maken en de kijkers altijd naar iets sturen wat van jou is (zijn maillijst op Substack) (BRON).
5. **Juni: Shorts over het maken, kort na of rond de Steampagina.** "I'm Making an Idle Productivity Game", "Why Does My Game Look Like That?" (21 jun, 9.262), hoe het figuurtje geld verdient, nieuwe werkplekken, kleding. Op 21 jun op zijn spellenblog: "Still in somewhat early development but the Steam page is up!" met de link (GEZIEN).
6. **13 jul: één aankondigingstrailer op zijn eigen kanaal**, met als eerste regel "Wishlist here :" en de Steamlink. 378k weergaven (GEZIEN). Twee weken later dezelfde trailer als Short (19k).
7. **Jul tot okt: elke paar weken een Short over één nieuwe functie** (kleding, met Professor Layton als voorbeeld, "App Focus", donkere modus, instellingen voor beeld, typemachinegeluid). Dit is zijn routekaart, maar dan op YouTube in plaats van op Steam. Op de blog vragen lezers om te mogen testen; een schrijfster krijgt een sleutel en toegang tot de Discord (12 sep, GEZIEN).
8. **22 sep: demo**, met de zin "Your save data carries over to the full game!" en in de videotekst "Please also leave a review!" (vragen om een review, zonder beloning: dat mag). 97 reviews, alle 97 positief.
9. **26 okt: releasedatum 6 jan 2027** als eerste en enige Steam-aankondiging. Geen Next Fest-post en geen fest-evenement gevonden.

### Waarom ik denk dat het werkte (en wat ik niet weet)
- **De haak past in één zin en bij een groep die zich herkent:** "Type, and they'll write too." Wat jij doet (typen voor je werk) is wat het spel aandrijft. Hij richt zich op schrijvers (#author, #novels, #writers, #booktube); de reacties komen ook van schrijvers ("As an author I'm OBSESSED with this!"). Hij zet de privacy bovenaan de winkeltekst: "What you type is not recorded and does not leave your device", precies de vraag die iemand heeft bij een spel dat je toetsen telt.
- **De volgorde:** het verschil tussen 12 en 1.295 volgers komt overeen met zijn eigen uitleg (pagina eerst). Maar het zijn ook andere spellen (actie-RPG tegen een schrijfmaatje), dus de volgorde is niet de enige verklaring. Dit is één maker met twee spellen, geen meting.
- **Hoe 17.000 abonnees 378.000 weergaven werden** weet ik niet zeker. Zijn eigen theorie is dat YouTube een opvallend onderwerp aan mensen buiten je kanaal laat zien; de lage weergaven van de Shorts (meestal 1.000 tot 2.500) laten zien dat het geen vast publiek is dat alles kijkt. Of de trailer ook via Reddit of X liep, heb ik niet kunnen nagaan.
- **Wat er na 378k gebeurde:** zijn release-video haalde 1.462. Precies wat hij voorspelde: een vervolg doet het slecht. Zijn volgers op Steam blijven wel staan; dat is het verschil met de eerste keer.

### Drie lessen
1. **Een groot moment zonder plek om te landen is weg.** Bijna 100k weergaven zonder Steampagina leverde een spel met 12 volgers; 378k met de pagina erbij leverde er 1.295, de vierde plek van 222 aangekondigde bureaubladapps. De maker zegt het zelf: "I had wasted my biggest marketing ammunition."
2. **Eén sterke video slaat honderd kleine.** 14 Shorts samen ±81.000 weergaven, de ene trailer 378.000. Wat hem bracht was één opvallend ding op het juiste moment, niet elke dag posten. De dagelijkse Shorts hielden de functies zichtbaar, maar brachten weinig.
3. **Haak = wat de speler zelf al doet.** Bij Little Writer is dat typen; bij Bongo Cat ook (114.956 reviews volgens indiespade, DERDEN). Bij Hats is de vraag: wat doet de speler terwijl het hol loopt? Dat is werken, en het hol gaat door. Little Writer koppelt dat werk letterlijk aan de voortgang; wij niet.

### Wat dit betekent voor Hats
- **Little Writer is geen concurrent om het idee** (een schrijfmaatje, geen kerker) maar wel om de aandacht in dezelfde week: uit op 6 jan, wij in het fest van 14 jan. Met ±10.000 tot 25.000 verlanglijsten (GOK) staat het dan waarschijnlijk hoog bij "nieuw en populair" in de tag Desktop Companion (GOK). Dat is ook kans: wie in die week bureaubladmaatjes zoekt, komt bij de tag.
- **Antwoord op Sems vraag:** nee, geen routekaart op Steam vóór de uitgave (1 aankondiging totaal). Wel een routekaart in de vorm van Shorts per functie op YouTube. Het is geen geval dat zijn regel uit `routekaart.md` omgooit.
- **Ons risico is precies zijn eerste fout:** het fest-plan zet vanaf di 17 nov elke dag een TikTok-clip, terwijl de Steampagina pas rond 8 dec live gaat. Als een van die clips aanslaat, is er niets om op te klikken.
- **Niet overnemen:** de hashtags en de schrijvers-niche zelf; Hats heeft geen beroepsgroep zoals schrijvers. Zijn aanpak om met een eigen kanaal van 17.000 te beginnen hebben wij niet.

### Voorstel voor Dortus deze week
**Chris en Sem houden vóór ±8 dec de sterkste clip (het eerste filmpje waar we het meest in geloven, de "haak" uit `onderscheid-hats.md`) achter, en posten tot dan alleen kleine maak-clips met een uitnodiging om het TikTok-account te volgen. De sterke clip en de trailer gaan pas uit op de dag dat de Steampagina live staat, met de Steamlink in de eerste regel of het profiel.** Waarom: JSLegendDev verloor bijna 100k weergaven omdat er geen pagina was (zijn vorige spel staat op 12 volgers) en kreeg er met de pagina 1.295 volgers uit een video van 378k. Het kost niets en vraagt alleen een andere volgorde. Wie: Chris (TikTok), Sem (festplan en trailerdatum); Thijs hoeft er niets extra voor te doen.

Tweede punt voor Olaf (geen actie deze week, wel voor de winkeltekst van 30 nov): zet net als Little Writer in één zin wat het spel doet terwijl jij werkt, en wat het níet doet met je computer (Hats leest geen toetsen; als het iets van je bureaublad gebruikt, één regel over privacy bovenaan). Spellen in de taakbalk roepen die vraag op.

### Eerlijk: wat ik niet weet
- Het echte aantal verlanglijsten; de schatting is een GOK met factor 3 marge.
- Of de trailer buiten YouTube werd gedeeld (Reddit, X, Discord niet gelezen), en hoe lang hij is.
- Wanneer de Steampagina precies live ging; 21 jun is de eerste datum waarop hij het zegt.
- Hoeveel van het verschil tussen 12 en 1.295 door de volgorde komt en hoeveel door het idee.
- Hoe het na 6 jan gaat. Volgende stap: op 7, 13 en 20 jan volgers, reviews en spelers tegelijk meten (zelfde API's), naast ons fest.

---

## 12. Mini Cozy Room: Lo-Fi (Tesseract Studio met Nugem Studio, Korea): 3.830 reviews en 96%, waarvan maar 8% in de eerste maand; een spel dat na de lancering zes keer groter werd

Onderzocht 16 nov 2026, run 13. Zelfde bedrijf als TBH (verhaal 11), maar het tegenovergestelde verhaal: betaald ($4,99), geen markt, overweldigend positief, en het groeit nog steeds. Het is een "productiviteitsspel" (lo-fi muziek, kamer inrichten, timer en takenlijst) en geen gevecht; daarom vooral nuttig voor de vraag hoe een bureaubladspel lang open blijft en na de lancering groeit.

### Bronnen
- Alle 59 eigen aankondigingen van 7 mrt 2025 tot 14 okt 2026, via de nieuws-API: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=3511030&count=300&maxlength=0&feeds=steam_community_announcements (GEZIEN). Gelezen: de drie acties rond de lancering, beide routekaarten (5 apr en 26 jun 2025), de tussenstand na een jaar (31 mrt 2026), samen-werken (15 jan en 13 feb 2026), DLC's, Mac-speeltest (3 sep 2026).
- Steam appdetails van het spel, de demo (3550820) en de 10 DLC's, met curl, 16 nov 2026 (GEZIEN). Winkelpagina: tags en of er een AI-melding staat (GEZIEN: geen).
- Reviews per week sinds de lancering: https://store.steampowered.com/appreviewhistogram/3511030 (GEZIEN; 3.691 positief, 139 negatief). Reviews per taal uit de taalpagina's die Vera al ophaalde (`platformen/verkenner/data/steam-talen-2026-11-16.jsonl`).
- Spelers per maand: https://steamcharts.com/app/3511030, nu: GetNumberOfCurrentPlayers (GEZIEN, 16 nov ±16:30 UTC). Demo: https://steamcharts.com/app/3550820 (GEZIEN).
- 14 prestaties met percentage via de Steam-API (GEZIEN).
- Meest behulpzame reviews in het Engels, Koreaans en Vereenvoudigd Chinees, 10 per taal, met speeltijd: https://steamcommunity.com/app/3511030/reviews/?browsefilter=toprated (GEZIEN).
- Samenvatting van reviews door VaporLens (DERDEN, bijgewerkt 4 jun 2026): https://vaporlens.app/app/3511030/mini_cozy_room_lo_fi. Laagste prijs ooit $2,49 (DERDEN, https://www.dekudeals.com/items/mini-cozy-room-lofi).
- Alle cijfers in `platformen/succes/data/mini-cozy-room-2026-11-16.csv`.
- Niet gevonden: een interview of devlog met verlanglijstjes of verkoopcijfers (gezocht in het Engels en Koreaans). Gamalytic gaf 403, de review-API stuurde door (302). Wat ik hieronder over verkopen zeg is dus GOK.

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Prijs | $4,99; laagste ooit $2,49 (-50%) | GEZIEN, DERDEN |
| DLC | 10 betaalde: 5 muziek- en geluidspakketten van $2,99 (jun 2025), samenwerking met lo-fi muzikanten nawhij en Lo-Five, kapsels en Halloween, $3,99. Samen ±110 reviews (Ambient Pack 32, nawhij 20, de rest 3 tot 10) | GEZIEN |
| Reviews | **3.830, 96% positief** | GEZIEN |
| Waarvan in de eerste maand | 306 (8%); eerste jaar 2.263; tweede jaar tot nu (7,5 maand) 1.567 | GEZIEN (histogram) |
| Per taal | Koreaans 1.023 (98%), Vereenvoudigd Chinees 890 (94%), Engels 766 (96%), Traditioneel Chinees 259 (98%), Russisch 238 (97%); Japans en de rest onder de ±200 | GEZIEN |
| Talen | 11 bij de lancering, 16 sinds 13 feb 2026 (Pools, Turks, Oekraïens, Vietnamees, Thai erbij) | GEZIEN |
| Spelers tegelijk, gemiddeld per maand | apr 2025 **414**, aug 2025 548, okt 2025 1.165, jan 2026 1.118, mrt 2026 2.031, **apr 2026 4.603** (piek 9.093), daarna jun tot okt 2026 steeds 2.427 tot 2.841; nu 3.152 | GEZIEN (steamcharts, Steam-API) |
| Demo | live 19 mrt 2025, 11 dagen vóór de lancering; nooit meer dan 162 tegelijk, nu 27 | GEZIEN |
| Speeltijd | SteamSpy: mediaan 47 uur, gemiddeld 63 uur (eigenaarsveld kapot, korrel zout). Behulpzame reviews: 100 tot 5.140 uur, één speler "挂到1030级" (niveau 1030) na 2.959 uur | DERDEN, GEZIEN |
| Gemaakt door | Tesseract Studio en Nugem Studio als ontwikkelaar en uitgever; Nugem is het bedrijf van TBH (Seoul, sinds 2023) | GEZIEN |
| Verkocht | ±75.000 tot 190.000 exemplaren (3.830 reviews keer 20 tot 50) | GOK |

### Hoe ver spelers komen (prestaties, GEZIEN)
Niveau 2: 94%. Eerste huisdier: 85%. 10 nummers gespeeld: 83%. Tweede kamer: 73%. **10 uur muziek: 58%.** Derde kamer: 56%. **Niveau 100: 40,5%.** **100 uur muziek: 28%.** 100 decoraties: 18%. Timer 10 keer afgemaakt: 13%. 100 taken afgevinkt: 6,9%.
Vergelijk met de meetlat in `diepte-toppers.md`: bij Desktop Defender haalt 57% de 10 uur en **17%** de 100 uur. Hier haalt 28% 100 uur, en dat telt alleen de tijd dat er muziek speelt (wie alleen omgevingsgeluid of eigen muziek opzet telt niet mee, zegt een Chinese review). Dit is het langste open-houden dat ik bij een bureaubladspel heb gezien. Opvallend: de nuttige knoppen worden weinig gebruikt (timer 13%, taken 6,9%); mensen houden het open voor de muziek en de kamer, niet voor de werktools.

### Wat ze deden, in volgorde
1. **7 mrt 2025, drie weken vóór de lancering: actie voor volgers.** Laat een steunbericht en je mailadres achter onder de aankondiging; wie het spel op de verlanglijst zet en volgt "will increase your chances". 50 sleutels (GEZIEN).
2. **19 mrt: demo, 11 dagen voor de lancering**, met weer een actie: speel de demo, deel je indruk "on Steam or SNS", stuur hem in via een Google-formulier, 50 sleutels (GEZIEN). Geen Next Fest. De demo trok nooit meer dan 162 spelers tegelijk.
3. **30 mrt: lancering met een cadeaubonnen-actie** (1 keer $50, 2 keer $25, 9 keer $10, 30 sleutels) voor wie zijn indruk deelt (GEZIEN). Eerste maand 306 reviews en gemiddeld 414 spelers tegelijk: een nette maar kleine start.
4. **5 apr, 6 dagen na de lancering: een routekaart met vinkjes.** "Upcoming Update List" met 5 punten (kleding, mini-modus, meubels, eigen muziekbestanden, YouTube en Spotify), die ze in dezelfde post afvinken zodra iets klaar is ("✅ (Update Complete)"); ze zetten er zelfs een eerlijke correctie bij toen YouTube en Spotify maar een snelkoppeling werd (GEZIEN). Op 26 jun: "The update plans we announced last time have all been completed!" en een tweede lijst van 8 punten.
5. **Elke 1 tot 3 weken een update**, ook in het eerste jaar 30 hotfixes en kleine versies. Wat ze toevoegden kwam uit reviews: eigen muziek, mini-modus in de taakbalk, alleen in het systeemvak (tray), takenlijst en timer los op het bureaublad (29 aug 2025).
6. **3 jun 2025: vijf DLC's** met muziek, achtergronden en kleding, plus een bundel met 20% extra korting (GEZIEN). Later samenwerkingen met lo-fi muzikanten die zelf een publiek hebben op Spotify en YouTube (okt 2025, feb 2026).
7. **Feb 2026: samen werken (multiplayer) en 5 talen erbij.** Aangekondigd op 15 jan "Many of you have shared sincere feedback saying that it would be even better if you could play together with friends"; met een Focus-modus voor wie het stil wil en een cadeaudoos per vriend per 30 minuten (GEZIEN). In de tussenstand van 31 mrt: "not originally part of the second roadmap, this feature was prioritized due to strong community demand". Spelers per maand: jan 1.118, feb 1.233, mrt 2.031.
8. **31 mrt 2026: "Biggest Sale Ever" op de verjaardag**, met de tussenstand van de routekaart en een lange lijst van wat nog komt (GEZIEN). April: gemiddeld 4.603 tegelijk, piek 9.093, 396 reviews in drie weken. Daarna bleef het op ±2.500, zes keer de eerste maand.
9. **Sep en okt 2026: Mac-speeltest voor iedereen** (ook zonder het spel te kopen; "If you know any Mac users ... please share the news") en een grote update met kleuren en nieuwe kamers. Geen enkele update wiste voortgang; de Mac-test heeft wel een eigen save (GEZIEN).

**Waar de reviews vandaan kwamen (GEZIEN, histogram per week):** lanceerweek en week erna 227; week van 12 tot 26 okt 2025 213 (update 1.04 en de nawhij-DLC); week van 23 nov tot 7 dec 2025 **334**, de grootste piek (valt samen met de herfstuitverkoop van Steam eind november; de korting zelf heb ik niet gezien, dus GOK dat het die was); na samen-werken 15 feb tot 22 mrt 2026 249; verjaardagsuitverkoop 396. Elke piek is een update of een uitverkoop, vaak allebei; nooit een fest.

### Wat de spelers zeggen (meest behulpzame reviews, GEZIEN)
- **Gezelschap en schuldgevoel werken.** "my productivity has skyrocketed all because of the guilt I get from seeing my lil dude working on his tablet and me not working" (Engels, 180 uur). "the worko buddy gives some sense of relief and companionship as someone who suffers from an anxiety disorder" (1.295 uur). Koreaans, 898 uur: wie voor muziek naar YouTube gaat, raakt afgeleid; dit start op met de pc en zet je meteen in de werkstand.
- **De grootste wens in Koreaans en Chinees is dezelfde: meer figuurtjes die vanzelf bewegen.** De nummer 1 in beide talen vraagt om 2 of 3 figuren in je eigen kamer zonder multiplayer; drie andere Chinese reviews willen dat het figuurtje "自己动" (zelf beweegt), want nu "看起来没有灵魂" (lijkt het zielloos).
- **Klachten:** geheugen (tot 9 GB genoemd, "smells like a memory leak"), opstarten bij het aanzetten van de pc terwijl dat uit staat, kick is meteen een blokkade in multiplayer, "you are basically buying a Demo 2" (DLC, 8 uur), en de meest behulpzame negatieve in het Chinees (130 mensen): je krijgt alleen ervaring als het geluid aanstaat. VaporLens telt als grootste klachten fouten en onstabiliteit (97), slechte bediening (79), te weinig meubels (61).
- **Eén ernstige beschuldiging:** een Engelse review (43 behulpzaam) zegt dat de standaardmuziek als bundel van Envato komt, een site die ook AI-muziek verkoopt, en vermoedt AI-muziek. Er staat geen AI-melding op de winkelpagina. Dit is één bewering van één speler; ik heb het niet kunnen controleren.
- **Einde van het spel:** na het leegkopen van de winkel is het geld "只是个数字" (maar een getal), schrijft de speler met 2.959 uur; hij vraagt om dingen met een tijdslimiet om geld aan uit te geven. De speler met 1.179 uur heeft alles en alle prestaties.

### Drie lessen
1. **Een bureaubladspel kan na de lancering groeien in plaats van zakken, als het blijft veranderen en luistert.** 92% van de reviews kwam na de eerste maand; de spelers tegelijk gingen van 414 naar ±2.500. Dat staat haaks op Desktop Defender (verhaal 5) en de spellen uit verhaal 8, waar bijna alles in de eerste weken gebeurde. Wat ze deden: binnen een week een routekaart met vinkjes, die echt afvinken, elke 1 tot 3 weken een update, en de grootste wens van spelers (samen werken) vóór hun eigen plan zetten.
2. **Wat open blijft, wint de lange speeltijd.** 28% haalt 100 uur muziek, tegen 17% die 100 uur haalt bij Desktop Defender. Mensen houden het open omdat het iets doet terwijl ze werken (muziek, gezelschap), niet om het spel; de werktools zelf gebruikt maar 7 tot 13%. Voor Hats: het spel moet lekker blijven doorlopen als je er niet naar kijkt, met geluid en beweging die niet storen; dan stapelen de uren zich vanzelf.
3. **Pieken komen van uitverkopen met een update ernaast, en van Azië.** Geen fest, geen grote YouTuber gevonden; wel de herfstuitverkoop, de verjaardagsuitverkoop en een update vlak ervoor. Koreaans en Chinees samen 57% van de reviews, Engels 21%. Dezelfde les als Rusty (grootste video Koreaans, verhaal 4) en Ropuka (verhaal 10).

### Wat dit betekent voor Hats (en wat niet)
- **Niet overnemen:** de acties "verlanglijst en volg voor meer kans" en "deel je indruk op Steam voor een sleutel of cadeaubon". Valve verbiedt beloningen voor reviews; Nugem deed het bij beide spellen (zie ook verhaal 11). Wij doen het niet.
- **Niet zomaar vergelijkbaar:** Mini Cozy Room is geen spel met doel maar een werkplek; de 100 uur zijn deels muziek die aanstaat. Een spel met level ups zal die lijn niet halen, maar het laat zien dat de bovengrens bij bureaubladspellen hoger ligt dan 17%.
- **Wel overnemen:** de routekaart met vinkjes als vaste post op de winkelpagina; nooit voortgang wissen (staat al in het fest-plan); figuren die vanzelf bewegen en iets doen als je niet kijkt (dat is de grootste wens bij dit spel en Gloop doet het al); een uitverkoop pas met een update ernaast.

### Voorstel voor Dortus deze week
**Sem zet nu een Engelse aankondiging klaar voor de dag dat de winkelpagina van Hats live gaat (±8 dec): "What's coming to Hats of the Fallen", een lijst van 5 punten met lege vakjes, alleen dingen die Olaf vóór de lancering in maart zeker kan leveren (bijvoorbeeld de talen, hol-niveaus, samen-spelen).** Elke keer dat iets in de demo komt, vinkt hij het af in dezelfde post en meldt het in een korte nieuwe post. Waarom: Mini Cozy Room deed precies dit 6 dagen na de lancering en vinkte alles af binnen drie maanden; daarna groeide het spel zes keer, met 92% van de reviews na de eerste maand. Het kost een tekst en geen bouwwerk. Wie: Sem schrijft, Olaf zegt welke 5 punten zeker zijn, Thijs plaatst (staat op zijn lijst als de pagina live is). Regel erbij: geen punt dat we niet kunnen halen; een niet gehaald vinkje is erger dan geen lijst.

Tweede punt voor Sanne (`voortgang.md`, geen actie deze week): reken het lange eind niet alleen in "uren spelen" maar ook in "uren open". Bij Mini Cozy Room is het geld na het leegkopen van de winkel waardeloos; de speler met 2.959 uur vraagt om iets om het aan uit te geven. Een laag voor de lange termijn die geld blijft opnemen (bijvoorbeeld steeds duurdere hoeden of versieringen voor het hol, zonder einde) houdt de spelers die nooit afsluiten bezig.

### Eerlijk: wat ik niet weet
- Hoeveel verlanglijstjes en volgers ze vóór de lancering hadden; nergens gevonden.
- Wat de piek van eind november 2025 echt veroorzaakte. Het past bij de herfstuitverkoop, maar ik heb de korting niet gezien en de spelers per maand stegen toen nauwelijks (1.165 naar 1.237).
- Wie de spelers in Korea en China bracht (een streamer, een winkelplek, Nugem zelf?). Bilibili en Koreaanse sites heb ik niet gelezen.
- Of de muziek met AI gemaakt is; alleen één review zegt dat.
- Hoeveel het opbracht; de verkoopschatting hierboven is een GOK met een factor 2,5 marge.

---

## 11. TBH: Task Bar Hero (Nugem Studio, Korea): 546.000 spelers tegelijk in de taakbalk, en wat de Steam-markt ervoor terugnam

Onderzocht 16 nov 2026, run 12. Het grootste taakbalkspel ooit, en tegelijk het duidelijkste voorbeeld van wat er gebeurt als buit geld waard is. Nog niet eerder bij ons uitgezocht; Deskrawl en andere spellen liften er al op mee ("The next Task Bar Hero!? New game with Steam Market", zie `platformen/succes/data/youtube-kanalen-winnaars-2026-11-16.csv`).

### Bronnen
- Alle 116 eigen aankondigingen van okt 2025 tot 12 nov 2026, via de openbare nieuws-API: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=3678970&count=200&maxlength=0&feeds=steam_community_announcements (GEZIEN). Gelezen: lanceerdatum (30 jan), uitstel (11 mrt, 16 apr), speeltest (16 tot 27 apr), prijzen (8 mei), lancering (27 mei), markt en itemreset (30 mei tot 1 jun), excuses en compensatie (30 jun), routekaart (10 jul), datalek (12 nov).
- Steam appdetails 3678970 en de winkelpagina's van het spel en de 8 DLC's, met curl, 16 nov 2026 (GEZIEN). Reviews per taal uit de winkelpagina per taal: `platformen/succes/data/tbh-reviews-per-taal-2026-11-16.csv`.
- Spelers tegelijk per maand: https://steamcharts.com/app/3678970 en de Steam-API GetNumberOfCurrentPlayers (GEZIEN 16 nov).
- 80 prestaties met percentage (Steam-API) en beschrijving (communitypagina): `platformen/succes/data/tbh-prestaties-2026-11-16.csv` (GEZIEN).
- De meest behulpzame reviews in het Engels, Braziliaans Portugees en Vereenvoudigd Chinees, 10 per taal, met speeltijd van de schrijver: https://steamcommunity.com/app/3678970/reviews/?browsefilter=toprated (GEZIEN).
- Website van de maker: https://www.nugemstudio.com/en/about (GEZIEN): opgericht mrt 2023 in Seoul, eerder een mobiel idle-RPG met live-service, op Steam Mini Cozy Room: Lo-Fi (mrt 2025) en PANOPTYCA (nov 2025). Zoekt nu personeel. Dus geen solomaker: een klein bedrijf met ervaring in idle-spellen.
- Pers (DERDEN): Inven Global 1 jun 2026 (https://labs.invenglobal.com/articles/22394) en 8 jun 2026 (https://labs.invenglobal.com/articles/22636); allthings.how (https://allthings.how/task-bar-hero-tops-526000-concurrent-steam-players-amid-mixed-reviews/); Notebookcheck 17 jun 2026; MeinMMO 6 jun 2026; In Game News jun 2026 (https://www.ingamenews.com/2026/06/tbh-task-bar-hero-is-dominating-steam.html); persbericht Nugem (https://www.nugemstudio.com/en/news/tbh-peak-concurrent).
- Niet gelukt: de review-API van Steam stuurde deze run door naar de voorpagina (302), dus geen weekoverzicht van de reviews. De demo (appid 3804790) is verwijderd; steamcharts gaf voor de demo een serverfout. Bilibili kon ik niet lezen.

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Prijs | gratis; Priest-klasse gratis DLC; betaald: Hunter en Slayer $4,99, Supporter Pack (3 huisdieren met buitbonus) $3,99, extra opslag $2,99, later Material Stash en Trade Ship Pack $4,99, soundtrack | GEZIEN (winkel; aankondiging 8 mei) |
| Demo | live in okt 2025 (Next Fest okt 2025), 20 updates tot 24 mrt 2026, opgeheven 21 apr 2026, alle voortgang gewist | GEZIEN (aankondigingen) |
| Uitstel | lancering aangekondigd voor 1 apr, toen 15 apr, toen "april", toen 27 mei 2026 | GEZIEN (aankondigingen) |
| Open speeltest | 22 tot ±28 apr 2026, voor iedereen, ook met de betaalde klassen; daarna ook gewist | GEZIEN |
| Spelers tegelijk | 10.594 op de lanceerdag, 143.000 op 1 jun, 415.374 op 8 jun, **546.130 piek** (eigen persbericht; steamcharts: 545.349 in juni) | DERDEN (allthings.how, Inven) en GEZIEN (steamcharts) |
| Gemiddeld tegelijk per maand | juni 434.627, juli 288.455, aug 107.511, sep 76.465, okt 59.947, laatste 30 dagen 59.614; nu 66.133 | GEZIEN (steamcharts, Steam-API 16 nov) |
| Reviews | **48.731, 53% positief**; laatste 30 dagen 1.197, 56% | GEZIEN (winkelpagina) |
| Per taal | Vereenvoudigd Chinees 10.338 (25%), Braziliaans 9.097 (81%), Engels 8.862 (62%), Turks 4.438 (65%), Russisch 3.400 (47%), Japans 2.703 (41%), Koreaans 1.746 (26%) | GEZIEN |
| Reviews per piekspeler | 48.731 / 546.130 = 0,09 | rekensom |
| DLC | Supporter Pack 408 reviews (41%), Hunter 128 (45%), Trade Ship 118 (25%), Slayer 86 (25%) | GEZIEN |
| Speeltijd | SteamSpy: mediaan 202 uur sinds de lancering, laatste 2 weken mediaan 81 uur (±5,8 uur per dag). Het eigenaarsveld van SteamSpy is kapot (0 tot 20.000), dus met korrel zout | DERDEN |
| Inhoud | 3 aktes, 4 moeilijkheden (Normal, Nightmare, Hell, Torment), 500+ voorwerpen, 10 zeldzaamheden van Common tot Cosmic, Cube voor samensmelten en versieren; sinds sep 2026 Plaguelands, sinds okt relikwieën | GEZIEN (winkeltekst, aankondigingen) |

### Wat ze deden, in volgorde
1. **Okt 2025: demo met echte buit.** Al in de demo kon je kisten krijgen ("Reward Item Distribution Function Restored", 14 okt 2025). Daarna 20 demo-updates in 5 maanden, vooral balans per klasse (GEZIEN).
2. **30 jan 2026: datum en verdienmodel bekend.** Gratis spel, betaalde klassen en huisdieren, 13 talen, en het "Trading Ship system (marketplace)" bij de lancering (GEZIEN).
3. **Mrt en apr: twee keer uitstel met excuses**, dan een open speeltest via de knop op de winkelpagina, met een loting onder wie een enquête invulde via Discord (10 sleutels). De demo werd opgeheven en alle voortgang gewist (GEZIEN).
4. **27 mei: lancering** (nu 16 talen in de winkel; in januari waren er 13 beloofd), 20% korting op de betaalde DLC voor twee weken, en een actie: deel je indruk "on Steam, SNS, Community" en win een Steam-tegoedbon tot ±$66 (GEZIEN). Let op: Valve verbiedt beloningen voor Steam-reviews; de actie noemt Steam erbij. Dat is mijn lezing, niet nagelezen in de regels deze run.
5. **Dag 3 tot 6: de markt breekt het spel.** 30 mei: de itemserver van Steam kan het niet aan, goud en voorwerpen verdwijnen. 31 mei: "Steam has confirmed that, because we failed to properly meet their server usage guidelines, the game was sending excessive server requests" (eigen aankondiging, GEZIEN). Spelers moesten binnen een dag hun spullen van de markt halen; 1 juni werden hele soorten uitrusting gewist en alleen Legendary en hoger bleef verhandelbaar, pas vanaf Cube-niveau 10 (GEZIEN).
6. **Juni en juli: bots, verbanningen en verborgen aanpassingen.** Inven (DERDEN): goudboeren met cheats overspoelden het spel; wie twee keer werd betrapt, verloor de markt voorgoed, en onschuldige spelers kregen een ban. Meerdere aankondigingen over sancties tegen valsspelers (GEZIEN). Spelers in drie talen schrijven dat de kans op kisten stil werd verlaagd. Excuses en compensatie op 30 juni; "practical limitations given our current development resources" (GEZIEN).
7. **Juni: nieuwe voorwaarden en verplichte gegevensverzameling** (aankondiging 12 jun, GEZIEN). Twee van de tien meest behulpzame Engelse reviews gaan alleen daarover.
8. **Daarna: echte inhoud en een routekaart.** 10 jul routekaart, sep Plaguelands, okt relikwieën en Halloween. Het gemiddelde zakte toch van 434.627 naar ±60.000 (GEZIEN).
9. **12 nov 2026: datalek.** Via de beheertool van hun externe serverdienst haalde iemand van 17 okt tot 8 nov Steam-ID's, IP-adressen en computergegevens van alle spelers op (eigen aankondiging, GEZIEN).

### Wat de spelers zeggen (meest behulpzame reviews, GEZIEN)
- **Engels: 10 van 10 negatief**, en geen enkele over het spel zelf als saai. Onterechte bans die als "Game Ban" voorgoed op je Steam-profiel staan (3 keer, onder wie iemand met een account van 18 jaar), verplichte gegevensverzameling (4 keer), stil verlaagde buit ("they punish their most engaged players and paying customers by silently nerfing the drop rates"). Eén schrijver met 895 uur rekent het eindspel na: één Cosmic-voorwerp kost gemiddeld ±65,7 miljoen Immortal-voorwerpen; "the numbers in the late game have inflated to an absolutely ridiculous degree".
- **Vereenvoudigd Chinees: 8 van 10 negatief**, met 35 tot 1.917 uur. Vooral: kisten vallen veel minder sinds de markt-ingreep, het Supporter Pack werkt niet meer ("如果你玩的免费本体请继续，不要买DLC" = speel je het gratis spel, ga door, koop geen DLC), en de schuld werd op Steam geschoven. Eén review noemt het "Steam's Most Successful Digital Begging Simulator".
- **Braziliaans: 8 van 10 positief**, maar vaak als grap of over geld ("Virginia falou que TBH era renda extra, mas o mercado fechou": iemand zei dat TBH extra inkomen was, maar de markt ging dicht). De serieuze negatieve: "o jogo entrega pouco" na 882 uur, en "tudo foi feito para prolongar o seu tempo de jogo, não para te recompensar".
- **Wat wel geprezen wordt:** Inven noemt karakterontwerp, afwerking en balans, en dat je niets hoeft te kopen om verder te komen. Spelers delen bouwplannen en tips: een "echt spel" met keuzes, anders dan de Banana-spellen.

### Hoe ver spelers komen (prestaties, GEZIEN, met een grote kanttekening)
Held niveau 10: 100%. Normal uitgespeeld: 78%. Nightmare: 71%. Hell: 60%. Held niveau 50: 59%. Niveau 80: 39%. Vier helden op 50: 18%. Hell 3-10 alleen: 11%. Eerste Plaguelands-zone (sinds sep): 8%. Alle 2/2/2 versieringen op alle uitrusting: 0,5%.
Kanttekening: zes prestaties op precies 100% en 59% op niveau 50 is veel hoger dan bij elk spel in `diepte-toppers.md` (daar haalt 17% de 100 uur). Ik denk dat de noemer bij dit gratis spel vooral accounts bevat die blijven draaien, ook boeraccounts (GOK). Deze getallen zijn dus niet bruikbaar als meetlat voor Hats, wel als teken dat de lijst gevuld is met accounts die nooit stoppen.

### Drie lessen
1. **Buit die geld waard is koopt spelers tegelijk, maar geen fans.** 546.130 tegelijk en toch 53% positief, 25% in het Chinees, en 0,09 reviews per piekspeler. Het spel zelf werd geprezen; wat de reviews sloopte kwam allemaal uit de markt: serverlast, gewiste spullen, cheats, bans, verlaagde buit, verplichte gegevens. Inven trekt de lijn naar de Banana-spellen: piek ±910.000, nu ±20.000 (DERDEN).
2. **Met een markt wordt elke balansverandering een geldkwestie.** Wie de kans op kisten verlaagt, pakt kopers van het Supporter Pack iets af; dat is precies waar de Chinese en Engelse reviews het hardst zijn. De DLC die meer buit belooft heeft 41% (Supporter Pack) en 25% (Trade Ship); de eerlijke gratis klasse heeft 92% in de laatste 30 dagen.
3. **Exponentieel samensmelten maakt van "honderd uur" een muur.** De spelers die het langst blijven (500 tot 900 uur) klagen niet over te weinig te doen maar over dat niets meer iets oplevert. Dezelfde les als Monster Farm (verhaal 6), nu met een rekensom van een speler erbij.

### Wat dit betekent voor Hats (en wat niet)
- Hats heeft geen markt en geen drops, dat staat al in `platformen/steam/verdienmodel.md` (Sanne). Dit verhaal is het bewijs bij dat besluit; er hoeft niets te veranderen.
- **Maar het is ook een kans.** Er zijn honderdduizenden spelers die een taakbalk-RPG met level ups willen en boos zijn op server, bans, gegevens en gewiste voortgang. Hats kan alles wat zij missen in één regel beloven, als het waar is: geen account, geen markt, alles op je eigen pc. Geen van de spellen in `onderscheid-hats.md` zegt dat op de winkelpagina (Don't Rob My Dungeon heeft juist Twitch-koppeling).
- Niet overnemen: gratis met betaalde klassen (wij zijn betaald, $4,99), een open speeltest die daarna gewist wordt (wij wissen nooit voortgang, fest-plan), beloningen voor posts "on Steam".
- Niet zomaar vergelijkbaar: Nugem is een bedrijf met eerdere idle-spellen en personeel; de grootte kwam van de markt, niet van de taakbalk alleen.

### Voorstel voor Dortus deze week
**Mila en Daan zetten in de lange winkeltekst van Hats (en in de laatste seconden van de trailer) één belofte: "No account. No market. No servers. Your save stays on your PC.", nadat Olaf bevestigt dat elke zin klopt voor de build.** Waarom: de grootste taakbalk-RPG verloor zijn reviews op precies die vier punten (bans, gewiste en verdwenen spullen, servers, verplichte gegevens), terwijl het spel zelf geprezen werd. Het kost een regel tekst en geen bouwwerk. Let op: Steam-prestaties en de opgetelde Steam-stats (Olaf, `berichten/olaf.md`) zijn geen eigen server, maar zeg dan niet "works fully offline" als we nog niets offline getest hebben. Wie: Olaf (klopt het), Mila en Daan (tekst en trailer), Sem (noemt het in mails aan makers die over TBH filmden).

Tweede punt voor Sanne (geen actie deze week, past bij haar versie 3): zet in `platformen/steam/voortgang.md` een plafond op elke stap van samensmelten of sparen (bijvoorbeeld hooguit 10 keer de vorige stap) en reken het eindspel na zoals de TBH-speler deed: hoeveel van het vorige ding kost het laatste ding?

### Eerlijk: wat ik niet weet
- Hoeveel echte mensen er bij de 546.130 zaten. Pers en spelers zeggen bots en boeraccounts, maar niemand geeft een cijfer.
- Hoeveel verlanglijsten en demospelers TBH vóór de lancering had. MeinMMO zegt alleen "eine solide Spielerzahl" vóór de release; de demo-pagina is weg.
- Hoeveel de DLC opbracht. Met de verhouding van Rusty's (36.000 kopers op 94 DLC-reviews) zou 408 reviews op ±150.000 Supporter Packs wijzen, maar boze kopers schrijven vaker; dus ergens tussen 40.000 en 150.000 (GOK, wijd).
- Of de stille verlaging van de buit echt gebeurde. De makers schrijven over vertraging en serverlast; spelers zeggen dat het meer is. Ik heb alleen de reviews en de aankondigingen, geen meting.
- Of de beloningsactie bij de lancering tegen de regels van Valve was; niet nagelezen.

---

## 10. Wat een vertaling echt oplevert: drie spellen die talen toevoegden na de lancering, gemeten in reviews per taal vóór en na (plus Click and Slash: 20 talen, 1 review)

Onderzocht 16 nov 2026, run 11. Waarom nu: de hoofdchat beslist vóór 1 dec welke talen in de demo komen (`platformen/steam/fest-plan.md`, punt 6). Vera mat al welk deel van de reviews per taal binnenkomt bij de toppers (Chinees mediaan 26%, Aanvulling 6 en 7 in `platformen/verkenner/steam-desktop-2026-11.md`). Wat nog niemand had: **komen die kopers dóór de vertaling, of waren ze er toch al?** Dat zie je alleen bij een spel dat een taal later toevoegde: dan kun je vóór en na vergelijken.

### Bronnen en werkwijze
- Aankondigingen van 168 bureaubladspellen met 100+ reviews (uit Vera's kaart) via de nieuws-API van Steam, doorzocht op "Chinese", "translation", "localization", "new languages" (GEZIEN 16 nov). Zo vond ik de datum waarop een taal erbij kwam.
- Reviews per taal per maand: de communitypagina van Steam (`steamcommunity.com/app/<appid>/homecontent/?browsefilter=mostrecent&filterLanguage=<taal>&appHubSubSection=10`, met de cursor van elke pagina), alle reviews in die taal vanaf de lancering, met datum (GEZIEN 16 nov). De review-API van de winkel stuurt ons door, deze pagina niet.
- Alle reviews samen per week: `store.steampowered.com/appreviewhistogram/<appid>` (GEZIEN 16 nov).
- Ruwe tellingen per maand en taal: `platformen/succes/data/talen-voor-na-2026-11-16.csv`.
- Aankondigingen: [Ropuka JP/ZH/KO, 20 jun 2025](https://store.steampowered.com/news/app/3416070/view/1802893906762643), [Ropuka vijf Europese talen, 30 okt 2025](https://store.steampowered.com/news/app/3416070/view/1815034432856341), [Burgie's acht talen, 11 jun 2025](https://store.steampowered.com/news/app/3314340/view/1802261838710720), [Lowmoor vijf talen, 14 sep 2026](https://store.steampowered.com/news/app/4977360/view/1843481262701297), [Click and Slash release](https://store.steampowered.com/app/4598890/).

### Spel 1: Ropuka's Idle Island ($3,99, lancering 29 jan 2025, 4.204 reviews in alle talen)
Op 20 jun 2025 kwamen Japans, Vereenvoudigd Chinees en Koreaans erbij, op 30 okt 2025 Pools, Frans, Duits, Spaans en Braziliaans. Vertaald door een vertaalbureau (Kurono Studios) met namen van vertalers erbij, dus door mensen. Deel van alle reviews per taal (GEZIEN, mijn rekensom op de tellingen):

| Taal | Vóór de vertaling | Na de vertaling | |
|---|---|---|---|
| Vereenvoudigd Chinees | 3,0% (59) | **8,5%** (187) | bijna 3 keer |
| Koreaans | 0,8% (15) | 1,6% (35) | 2 keer |
| Japans | 0,6% (12) | 1,1% (24) | bijna 2 keer |
| Traditioneel Chinees, **níet vertaald** (controle) | 0,9% (24) | 0,6% (10) | omlaag |
| Duits | 2,8% (72) | 2,4% (38) | niets |
| Frans | 0,7% (19) | 0,7% (12) | niets |
| Pools | 0,7% (18) | 1,6% (25) | 2 keer |
| Spaans | 0,8% (20) | 1,6% (26) | 2 keer |
| Braziliaans | 1,9% (50) | 2,9% (47) | anderhalf keer |

"Vóór" is vanaf de lancering tot de week van de vertaling, "na" tot 16 nov 2026. Twee controles dat het de vertaling is en niet de tijd: Traditioneel Chinees (niet vertaald) zakte in dezelfde periode, en het Duits zakte van 3,7% in feb tot mei naar 1,5% in jun tot okt 2025 terwijl het Chinees in diezelfde maanden steeg.

Rekensom (mijn rekensom, GOK in de laatste stap): na 20 jun 2025 kwamen er 2.202 reviews; met het oude aandeel van 3% waren dat ±66 Chinese geweest, het werden er 187. Dus **±120 reviews extra door het Chinees, ±3% van alle reviews van het spel.** Met reviews x 30 tot 60 (grove schatting uit de rol) zijn dat ±3.600 tot 7.200 kopers, maar in China ligt de prijs lager (GOK hoeveel). De vijf Europese talen samen: 148 reviews na, tegen ±111 met het oude aandeel, dus **±37 extra**, waarvan Duits en Frans niets.

### Spel 2: Burgie's Cozy Kitchen ($6,99, solo, lancering 10 feb 2025, 1.704 reviews)
De maker (Nau) voegde op 11 jun 2025 acht talen toe, zelf vertaald waar hij kon: "I did my best to translate everything well, but some languages are completely beyond what I can handle." Hij koos "the languages I've seen most in the community". Wat er gebeurde (GEZIEN):
- **Het eerste jaar met Chinees: 7 Chinese reviews in 12 maanden** (±3% van 245). De vertaling alleen deed bijna niets.
- **Vanaf de week van 15 juni 2026 golfde het spel:** van 4 tot 10 reviews per week naar 139 en 141, en 1.349 reviews van juni tot nu, 5,5 keer zoveel als de 245 in het hele jaar ervoor. **Van die golf was 38% Chinees (512 reviews).** In de piekweken bijna de helft (66 van 139, 61 van 141). Wat de golf startte weet ik niet: in de aankondigingen staat niets bijzonders vóór 15 juni (de 1.0 kwam pas op 13 juli, de zomeruitverkoop van Steam begon eind juni). Ook de niet-Chinese reviews gingen 5 tot 10 keer omhoog, dus het was geen puur Chinese golf.
- **De andere zeven nieuwe talen samen: 28 reviews in 17 maanden** (Russisch 10, Duits 5, Koreaans 5, Pools 4, Japans 2, Turks 2). Ook tijdens de golf bijna niets.
Mijn lezing: de vertaling bracht zelf geen kopers, maar toen er een golf kwam, kon ruim een derde ervan in het Chinees landen. Zonder Chinees was die derde er waarschijnlijk grotendeels niet geweest (GOK; Cornerpond haalt zonder vertaling 8% Chinees volgens Vera, Burgie's had vóór de vertaling 0).

### Spel 3: Lowmoor Idle RPG (gratis, lancering 7 aug 2026, 126 reviews)
Vijf talen op 14 sep 2026, vertaald door vier spelers uit de community. Daarna 1 tot 4 reviews per nieuwe taal (Chinees 4, Japans 3, Pools 3, Duits 1, Braziliaans 1). Klein spel, dus weinig te zien; wel een teken dat een vertaling zonder publiek niets doet. Na een week moest de maker het Japans al herzien ("repaired sentences assembled from translated parts").

### Tegenvoorbeeld: Click and Slash (zebra3dev, Frankrijk, uitgever Sukuratchi)
"A cute desktop monster that accompanies you every day." Bureaubladspel met gevechten, prestige en een "co-working system", $7,99, Early Access sinds 27 okt 2026, **20 talen** (van Arabisch tot Noors), demo, mee in Next Fest okt 2026 met een eigen livestream ("french or english only"). Na drie weken: **1 review** en **1 speler tegelijk** op 16 nov (GEZIEN, appdetails en GetNumberOfCurrentPlayers). De maker werkte er 6 maanden aan. Twintig talen konden geen publiek maken dat er niet was. Zelfde beeld op Vera's kaart: van de betaalde bureaubladspellen uit 2024 tot sep 2026 hebben spellen met 1 taal mediaan 3 reviews, met 10 tot 14 talen mediaan 20 (GEZIEN, mijn rekensom op `platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv`); maar daar zitten grotere ploegen en uitgevers achter, dus dat zegt niet dat talen het verschil maken.

### Drie lessen
1. **Een vertaling is een vermenigvuldiger, geen motor.** Bij Burgie's deed het Chinees een jaar lang bijna niets en droeg het daarna 38% van de golf. Bij Click and Slash deden 20 talen niets omdat er geen golf kwam. Eerst het moment (fest, video, lijstje), de vertaling zorgt dat je er meer van houdt.
2. **Alleen Chinees levert echt iets op; de rest is klein of nul.** Chinees bijna 3 keer (Ropuka) en 38% van een golf (Burgie's). Koreaans, Japans, Pools en Spaans verdubbelen, maar van ±1% naar ±1,6%. Duits en Frans gaven niets: wie Duits of Frans spreekt, speelde en schreef al in het Engels of in de eigen taal. Zeven talen bij Burgie's samen 28 reviews in 17 maanden.
3. **Laat de spelers de volgende taal kiezen.** Ropuka vroeg "Let us know what other languages you want", Burgie's koos wat hij in de community zag. Dat is gratis te meten: de taal van reviews en discussies op de demo.

### Wat dit betekent voor Hats (en wat niet)
- Het bevestigt Vera's advies voor het Chinees met een oorzaak erbij, en het zwakt de rest af: Duits heeft geen bewijs, Koreaans en Japans zijn klein. Olaf telde ±1700 woorden; vier talen kosten ±€650 tot €920, het Chinees alleen €153 tot €204 (Allcorrect, DERDEN, zie de vertaalvraag hieronder).
- Niet zomaar overnemen: drie spellen is weinig, en alle drie zijn rustige gezellige spellen of een gratis RPG, geen gevecht onderaan het scherm. Bij Burgie's ken ik de oorzaak van de golf niet; misschien was het een Chinese video die ook zonder vertaling was gekomen.

### Voorstel voor Dortus deze week
**Demo voor het fest in twee talen: Engels en Vereenvoudigd Chinees (door een mens), plus de korte winkeltekst en de tekst op de capsule in het Chinees. Geen Duits, Japans of Koreaans vóór het fest.** Na het fest een derde taal alleen als die taal minstens 5% van de reviews en discussies van de demo haalt (grens is GOK). Bespaart ±€500 tot €700 tegen vier talen en ±3 vertaalrondes in de drukke weken vóór 21 dec. Wie: de hoofdchat (besluit vóór 1 dec, punt 6 van het fest-plan), Olaf (vertaaltabel, één taal extra), Thijs alleen voor de betaling van de vertaler.

### Eerlijk: wat ik niet weet
- Of de reviews per taal ook de kopers per taal zijn. Chinese kopers schrijven misschien vaker of minder vaak een review; Vera zag dat ze strenger scoren.
- Wat de golf van Burgie's in juni 2026 startte. Bilibili (waar Chinese spelers video's kijken) gaf ons geen zoekresultaten via curl.
- De prijs in China en dus wat 120 extra Chinese reviews in geld waren.
- Of de vertaling van de winkelpagina zelf al verschil maakt, los van het spel. Sill Cats meldde in juni 2026 dat de pagina in sommige talen Engels bleef terwijl het spel 30 talen had; dat heb ik niet gemeten.

---

## 9. Wie maakte de winnaars groot: 124 video's over 9 bureaubladspellen, de kanalen erachter, en hoeveel spelers het opleverde (vraag van de hoofdchat: het Desktop Companion Fest en de YouTubers)

Onderzocht 16 nov 2026, run 10. Vraag van de hoofdchat (16 nov 12:25): (1) welke spellen stonden de vorige keer in het Desktop Companion Fest en wie brak door, (2) welke YouTubers en streamers maakten de winnaars groot, met namen voor Sem.

**Eerst (1): er is geen vorige keer.** De lijst met fests in de Steamworks-docs (`partner.steamgames.com/doc/marketing/upcoming_events`, GEZIEN 16 nov met curl) noemt alleen "Steam Desktop Companion Fest 2027", 14 tot 18 jan, "Games that sit on your desktop and keep you company while you do other things." Geen eerdere editie. De dichtste proeven heb ik al: Idler Fest 2025 (verhaal 3) en Next Fest juni 2026 met 11 bureaubladspellen (verhaal 7). Deze run gaat dus over vraag (2), met spelerscijfers erbij, zodat Sem een meetlat heeft.

### Bronnen en werkwijze
- YouTube-zoekpagina per spel, gesorteerd op weergaven, met curl gelezen op 16 nov (lijst uit `ytInitialData`), plus vier zoekopdrachten over het genre. Videopagina's zelf geeft YouTube ons niet (code 418), dus ik zie geen beschrijving en geen exacte datum, alleen "5mo ago". Kanaalpagina's wel: abonnees uit de kop van de kanaalpagina (GEZIEN 16 nov; afgerond zoals YouTube ze toont).
- Spellen: TBH: Task Bar Hero (gratis), Rusty's Retirement, Tiny Pasture, Ropuka's Idle Island, Deskrawl, Desktop Defender, Desktop Survivors 98, Desktop Raid, Cornerpond. Na het weghalen van treffers over iets anders (paarden, Windows Defender, tekenfilm "Rusty's World") bleven 124 video's over: `platformen/succes/data/youtube-kanalen-winnaars-2026-11-16.csv` (spel, kanaal, abonnees, weergaven, titel, link).
- Spelers tegelijk per maand: steamcharts.com/app/<appid> (GEZIEN 16 nov). Deskrawl staat daar niet in.
- Eigen aankondigingen via de nieuws-API van Steam (Desktop Defender 48, TBH 116, Desktop Survivors 98 10, Deskrawl 38, Desktop Raid 41 berichten) doorzocht op namen van makers, YouTube, streamer, influencer en curator. Niet geprobeerd: Twitch-cijfers; sullygnome en twitchtracker geven 403.

### Spelers tegelijk in de lanceermaand, naast de grootste video (GEZIEN 16 nov)
| Spel | Prijs | Piek lanceermaand | Grootste video's (weergaven, kanaal, abonnees) |
|---|---|---|---|
| TBH: Task Bar Hero | gratis | **545.349** (jun 2026) | 350.336 Hadomancer (100K), 137.668 Task Bar Hero Dicas (13,4K, Braziliaans), gidsen van Sir Eat Alot, MyGamerAcademia, GameStar (1,59M, Duits) |
| Rusty's Retirement | $6,99 | **20.876** (mei 2024) | 907.979 우주하마 (2,2M, Koreaans), 67.196 eigen trailer, 66.642 Buckeye Bunny, 66.434 Olexa (298K), 51.757 MaxPalaro (2,82M, Braziliaans) |
| Tiny Pasture | $4,07 | **19.674** (feb 2025) | 14.392 PC Gamer Cozy Corner, 9.394 CaveLiquid, 6.036 CozyAriGames (lijstje) |
| Ropuka's Idle Island | $3,99 | **3.850** (feb 2025) | 43.224 Best Indie Games (195K, lijstje), 26.846 Wholesome Games (trailer), 16.602 The Indie Brew (4K, lijstje) |
| Desktop Raid | $8,99 | **3.001** (mrt 2026) | 23.940 Plano Plays Games (566K), 19.835 Tietie TH. (43,9K, Thais) |
| Desktop Defender | $4,99 | **2.673** (nov 2025; demo in Next Fest 1.548) | 40.008 Vinesauce "Steam Next Fest: October 2025" (666K), 16.064 Conkbot (lijstje), 12.898 eigen trailer |
| Desktop Survivors 98 | $4,99 | **551** (mei 2025) | 651.363 IGN (trailer), 270.087 GameGrumps (5,45M), 138.594 GameTrailers, 110.002 Mattastic ASMR, 82.126 Gohjoe (201K), 50.234 Vinesauce (demo), 38.967 Bijuu Mike (3,78M) |
| Deskrawl | $6,99 | niet op steamcharts | 37.451 しんじさん (Japans, over de demo), 30.423 knekroTV (158K), 21.318 Kripparrian (901K, stream) |
| Cornerpond | $2,99 | | niets boven 5.100 |

Twee dingen springen eruit:
- **Desktop Survivors 98 had de grootste kanalen en de kleinste piek.** IGN, GameGrumps, Bijuu Mike en Vinesauce samen ruim een miljoen weergaven, en dan 551 spelers tegelijk bij de lancering en nu 1.352 reviews. Desktop Defender had bijna geen grote video's (de grootste 40.008, en of die echt over Desktop Defender gaat kan ik niet zien, zie onder) en kwam op 2.673 spelers en 1.788 reviews. Let op: Desktop Survivors 98 is een actief spel met rondes, geen idlespel dat de hele dag aan staat, dus spelers tegelijk is daar per koper lager. Maar het reviewverschil is klein voor zo'n verschil in weergaven. Grote kanalen geven weergaven, geen kopers.
- **Bij de echte doorbraken kwamen de grote video's ná het succes.** TBH is het duidelijkst: de grootste video heet "The game you don't even play is breaking Steam" en een tweede "Task Bar Hero Died in 30 Days | But Who Really Profited?"; GameStar maakte "#2 on Steam: TBH has more and more players every day". Die gingen over het succes, ze maakten het niet. De vele gidsen (Braziliaans, Turks, Engels, 60.000 tot 140.000 weergaven elk) komen pas als er al honderdduizenden spelers zijn. TBH is gratis en draait om spullen die je op de Steam-markt kunt verkopen; dat recept is niet het onze.

### Welke kanalen het meest opleveren per abonnee (GEZIEN, weergaven gedeeld door abonnees)
Een video die meer dan een vijfde van het aantal abonnees haalt, bereikte mensen buiten het eigen publiek; dat is een kanaal waar dit soort spel aanslaat:
- Hadomancer: 350.336 op 100K (3,5x), idle- en TBH-video's
- JGigs: 812.813 op 87,8K (9x), "I Played 20 Idle Games For 2 Hours Each To Find The Most Addictive One" (lijstje)
- Task Bar Hero Dicas: 137.668 op 13,4K (10x), Braziliaans gidsenkanaal
- The Indie Brew: 16.602 op 4K (4x), "The BEST Idle Games to play While You Work"
- Gohjoe: 82.126 op 201K (0,4x), uzuhama 907.979 op 2,2M (0,4x), Mattastic ASMR 110.002 op 293K (0,4x), Diomio 98.806 op 180K (0,5x, Vietnamees, "everyone is playing AFK games now")
- Olexa: 66.434 op 298K (0,2x), Best Indie Games 43.224 op 195K (0,2x), knekroTV 30.423 op 158K (0,2x)
Kanalen die terugkomen bij twee of meer winnaars: Vinesauce (Desktop Survivors 98, Desktop Defender), Buckeye Bunny, Wholesome Games, Best Indie Games, The Indie Brew en Maybe Sarisa (Rusty en of Ropuka), PC Gamer (Ropuka en Tiny Pasture), CozyAriGames (Tiny Pasture, Cornerpond, lijstjes).

### Wat de makers zelf zeggen
Weer bijna niets. In 253 aankondigingen van vijf spellen geen enkele naam van een YouTuber of streamer. Desktop Defender schrijft over de eigen demo: "it started with just 1 player for a few hours, and it's now grown into this craziness" (15 okt 2025, GEZIEN), met doelen voor gelijktijdige spelers via Discord (verhaal 5). Desktop Raid had een demo "Made for Next Fest!" (26 feb 2026, GEZIEN). De groei kwam bij deze twee dus uit het fest zelf, en de video's die er zijn (Vinesauce, Plano Plays Games) zijn rond het fest gemaakt.

### Drie lessen
1. **Grote kanalen zijn niet het doel; kanalen waar het genre aanslaat wel.** Desktop Survivors 98 kreeg IGN, GameGrumps en Bijuu Mike en haalde 551 spelers tegelijk; de idle-winnaars kregen hun grootste niet-eigen video's van lijstjesmakers en genrekanalen met 4.000 tot 300.000 abonnees (Best Indie Games, The Indie Brew, JGigs, Olexa, Hadomancer, Buckeye Bunny). Die hebben kijkers die precies "iets voor naast het werk" zoeken.
2. **Fest-overzichten zijn de deur bij grote streamers.** Vinesauce maakt video's als "Steam Next Fest: October 2025" en speelde de demo van Desktop Survivors 98; Buckeye Bunny maakt "31 FREE Chill & Cozy Games, Next Fest February 2025" (verhaal 4). Die makers spelen de demo's die op dat moment in een fest staan. Ons Desktop Companion Fest is precies zo'n lijst; GOK dat kanalen als CozyAriGames en The Indie Brew er een "games that sit on your screen"-video van maken, want dat is hun vaste vorm.
3. **De grootste enkele video is vaak niet Engels.** Rusty: Koreaans 907.979, Braziliaans 51.757 en 46.681, Taiwanees 44.791. Deskrawl: Japans, Koreaans, Taiwanees. TBH: Braziliaans, Turks, Duits, Vietnamees. Talen in de demo bepalen welke kanalen we kunnen vragen; Portugees (Brazilië), Koreaans, Japans en Chinees (Taiwan) komen het vaakst voor in deze lijst.

### Meetlat voor Sem (spelers tegelijk, GEZIEN uit steamcharts en eigen meldingen, grenzen zijn GOK)
- Lanceermaand van winnaars in onze hoek: 2.673 (Desktop Defender) tot 20.876 (Rusty). Kleiner dan ±500 (Desktop Survivors 98) gaf nog steeds 1.352 reviews, maar dat is een ander soort spel.
- Demo in een fest: Desktop Defender begon met 1 speler, haalde 100 tegelijk binnen ongeveer een dag en 1.548 op dag 6 van Next Fest (verhaal 5). Dat was Next Fest, met duizenden demo's; ons fest is kleiner en ons vak voller.
- Voorstel voor de meetlat (GOK): na dag 2 van het Desktop Companion Fest boven 100 tegelijk in de demo = doorbraak, 20 tot 100 = gewoon, onder 20 = stil, dan de verbeterweek naar de haak (zoals in verhaal 8 voorgesteld).

### Eerlijk: wat ik niet weet
- Of de video's betaald, met een sleutel van de maker, of vanzelf kwamen. De beschrijvingen kon ik niet lezen.
- Of de Vinesauce-video over Next Fest oktober 2025 Desktop Defender laat zien: YouTube gaf hem bij de zoekterm "Desktop Defender steam", maar de videopagina was dicht. GOK dat hij erin zit.
- Exacte datums: "5mo ago" en "1y ago" zeggen niet of een video vóór of na de lancering kwam, behalve waar de titel het zegt (demo, Next Fest, "breaking Steam").
- Twitch, TikTok en Bilibili tel ik niet. Abonneecijfers zijn afgerond en van één dag.
- Contactgegevens heb ik niet verzameld; dat is Sems werk (punt 2 in `platformen/steam/fest-plan.md`).

### Voorstel voor Dortus deze week
**Sem begint zijn lijst van 40 met deze kanalen, in drie bakken** (alle cijfers in de CSV):
- **Bak A, genre en lijstjes (eerst, rond 8 jan een demosleutel):** Olexa, Wanderbots (522K, incremental), Orbital Potato, Hadomancer, JGigs, Best Indie Games (ClemmyGames), The Indie Brew, CozyAriGames, Maybe Sarisa, Buckeye Bunny, Conkbot, Kosh Idle, Indie Signal, Gohjoe, Idle cub (203K), Dex (316K), Krayn (95K), Starker MMOs, Gaming Meets Experience, knekroTV.
- **Bak B, grote kanalen met fest-overzichten (februari, voor Next Fest):** Vinesauce, Plano Plays Games, Mattastic ASMR, Kripparrian, GameGrumps, Bijuu Mike. Lage kans op antwoord, en dit verhaal zegt dat ze weergaven geven, geen kopers.
- **Bak C, andere talen (alleen als die taal in de demo zit):** 우주하마 en 강한오빠 (Koreaans), MaxPalaro, Felps LIVE, EuSouOGiba en Task Bar Hero Dicas (Portugees), 狐狸牧場 foxranch en 小月歡樂星 (Taiwan), しんじさん, くろろじちゃんねる en ひろてくのゲーム研究室 (Japans), Tietie TH. en FineByMeh (Thai), Diomio (Vietnamees), GameStar (Duits), IlloRubiu en Alex Baena (Spaans).
- **Trailer-plekken (via de hoofdchat, het insturen is iets plaatsen):** Wholesome Games, PC Gamer Cozy Corner, GameTrailers.
Versturen gaat via de lijst van Thijs. Melding staat in `berichten/sem.md`.

---

## 8. Wat níet werkt: vier kerkerspellen voor de schermhoek die het hele draaiboek volgden en onder de 10 reviews bleven (Minimon als hoofdverhaal, naast Deskrawl uit hetzelfde fest)

Onderzocht 16 nov 2026, run 9. Vraag van de hoofdchat (16 nov 00:05): een taakbalkspel dat het minder goed deed, zodat we ook zien wat níet werkt. Ik koos niet één flop maar vier die het meest op Hats lijken (helden of monsters die vechten en buit halen in een hoekje van je scherm) en die op papier deden wat wij van plan zijn: winkelpagina, demo, Next Fest, updates, Discord. Alle vier staan nu op 4 tot 7 reviews. Daarnaast het basispercentage uit Vera's kaart: hoe vaak lukt het eigenlijk?

### Bronnen
- Eigen aankondigingen op Steam via de openbare nieuws-API `api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=<id>` (GEZIEN 16 nov): Minimon 4547080 (13 berichten), Idle Squire 3982800 (13), Idlewood Outpost 3897350 (6), Dungeoneers Idle 5135740 (29).
- Prijs, datum, demo, talen: `store.steampowered.com/api/appdetails`; reviews op de winkelpagina ("7 user reviews" bij Minimon); spelers nu: `ISteamUserStats/GetNumberOfCurrentPlayers` (GEZIEN 16 nov ±10:30 UTC, maandagochtend).
- Devlog van Idlewood Outpost op itch.io: https://tidepoolgames.itch.io/idlewood-outpost/devlog (GEZIEN, berichten van 6 juli tot 29 juli 2025).
- YouTube-zoekpagina per spelnaam en het kanaal https://www.youtube.com/@ReignOfGaming (GEZIEN met curl 16 nov).
- Basispercentage: `platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv` (Vera, 16 nov). Mijn tabel: `platformen/succes/data/kerker-flops-2026-11-16.csv`.
- Niet gelukt: volgers per spel (steamcommunity gaf steeds 429, te veel verzoeken) en de reviewteksten (de review-API stuurt door naar de voorpagina). Reddit gaf via curl geen antwoord.

### Eerst het basispercentage (GEZIEN, rekensom op Vera's kaart)
Betaalde spellen uit de bureaubladhoek, uit tussen 1 jan 2025 en 30 sep 2026, die enigszins op Hats lijken: 377 stuks. Mediaan **10 reviews**; 70 van de 377 (19%) haalden 100 of meer.
- Alleen de gevechts- en kerkerspellen met een demo die nog op de pagina staat: 16 stuks, mediaan **8 reviews**, maar **3 van de 16** boven de 100 (Desktop Survivors 98 1.352, Book of Fei 358, Nanomon 115).
- Een demo hebben maakt weinig verschil in de mediaan (15 tegen 10). Let op: spellen die het goed deden haalden hun demo vaak weg bij de lancering (Desktop Defender, Lootborne, Deskrawl), dus deze vergelijking is scheef.
- Talen: 1 taal mediaan 4 reviews, 6 tot 15 talen mediaan 19. Dat is samenhang, geen bewijs dat talen de oorzaak zijn: wie veel vertaalt heeft vaak ook een uitgever en geld.
- Ik testte ook of "desktop", "taskbar", "screen" of "corner" in de naam helpt (vindbaar, verhaal 4). **Nee:** met zo'n woord mediaan 7, zonder 11,5 (103 en 274 spellen). Die gok uit verhaal 4 houdt dus geen stand.

Kort: het draaiboek volgen is de norm, niet het verschil. Vier op de vijf halen geen 100 reviews.

### De vier, naast twee die het wel haalden (GEZIEN 16 nov)
| Spel | Prijs | Uit | Reviews | Talen | Next Fest | Spelers nu | YouTube met de naam |
|---|---|---|---|---|---|---|---|
| Minimon: Tiny Idle Tactics (uitgever Bufflehead) | $7,99 | 31 aug 2026 | 7 | 5 | juni 2026 | 0 | eigen video 15.678, de rest 26 views |
| Idle Squire (solo, "family life") | $4,99 | 6 mei 2026 | 6 | 1 | feb 2026 | 0 | niets gevonden |
| Idlewood Outpost (twee makers, Stockholm) | $4,99 | 17 nov 2025 | 4 | 1 | okt 2025 | 0 | 196 views samen |
| Dungeoneers Idle | $8,49 | 11 nov 2026 | 7 | 6 | niet genoemd | 9 | 23 views |
| Desktop Defender (verhaal 5) | $4,99 | 4 nov 2025 | 1.788 | 19 | okt 2025 | 32 | 14 video's, 38.083 views |
| Deskrawl (verhaal 2) | $6,99 | 28 sep 2026 | 3.631 | 13 | juni 2026 | | 19 video's, 31.618 views |

Idlewood Outpost en Desktop Defender zaten in **hetzelfde** Next Fest (okt 2025), en Minimon en Deskrawl ook (juni 2026). Zelfde kans, heel andere uitkomst.

### Hoofdverhaal: Minimon, wat ze deden, in volgorde (aankondigingen, GEZIEN)
1. **Een studio met een eigen YouTube-kanaal.** Reign of Gaming heeft 49.600 abonnees en 1.074 video's; de kanaaltekst zegt dat het nu "its debut as a developer / publisher" maakt. Maar de oude video's zijn 10 jaar oud en de nieuwe halen 34 tot 433 views. De Minimon-video van 5 maanden geleden staat op 15.678 views, de video op de lanceerdag op 282 (GEZIEN). Een slapend kanaal is geen publiek.
2. **Demo vóór Next Fest, met speltest-updates.** 22 en 29 mei grote demo-updates (tutorial, balans), met de waarschuwing dat er "occasional wipes" komen: je voortgang in de demo kan weg.
3. **Next Fest juni 2026, hard gewerkt:** een "Mega-Patch" de dag ervoor, een livestream van de ontwikkelaar, een patch op dag 1 en een patch voor het laatste weekend. Dat is precies wat Deskrawl in hetzelfde fest deed (verhaal 2). Verschil: in die laatste patch staat **"this wipe is absolutely necessary"**: midden in het fest ging de voortgang van alle demospelers weg. De makers schrijven zelf "progress mid-festival is frustrating".
4. **Pas na het fest vertaald:** op 1 aug "Minimon now speaks four languages" (Frans, Portugees, Chinees). Tijdens het fest was de demo dus alleen Engels (afleiding uit dat bericht).
5. **Augustus: Twitch-functies** (kijkers typen !join en worden een vijand, chat kiest de naam van een gevangen monster) en een toernooimodus voor streamers. Bètabuild naar "beta testers and content creators".
6. **31 aug uitgebracht**, $7,99 met 10% korting, 90 monsters, 15 paden. Een week later prestaties en Japans erbij.
7. Daarna geen aankondigingen meer (laatste bericht 7 sep). Nu 7 reviews in de winkel, 0 spelers op een maandagochtend.

**Deskrawl in hetzelfde fest deed drie dingen die Minimon niet deed** (verhaal 2): een ranglijst en een baas-evenement waar "about 4000 players" aan meededen, de top 100 kreeg de bèta, en "invite your friends". Zij gaven spelers een reden om te blijven en anderen te halen. Minimon gaf spelers patches en wiste hun voortgang.

### De andere drie, kort
- **Idlewood Outpost:** in mei 2025 begonnen als "a little tech experiment with Electron", itch-demo in de browser op 6 juli ("We've slapped a fake desktop on"), Steampagina pas op 29 juli, Steam-demo 16 aug, Next Fest okt, uitgebracht 17 nov. **Van pagina tot lancering 16 weken**, één taal, en de demo bleef staan ("I won't be taking it down"). Na een jaar 4 reviews.
- **Idle Squire:** één maker die werkt "between family life", sinds sep 2025 wekelijkse berichtjes, toen twee maanden stil ("Still here!"), nieuwe demo en trailer 1 feb, Next Fest feb 2026 met een bericht van 205 tekens, uitgebracht 6 mei. Eén taal. Haak die echt anders is ("every key you press is an attack"), maar geen enkele video op YouTube met de naam.
- **Dungeoneers Idle:** demo 14 sep, daarna **25 updates in 7 weken** (0.8.1 tot 0.16.1), Discord, 1.0 op 11 nov. Nu 7 reviews en 9 spelers; vijf dagen is te vroeg om te oordelen, maar al die updates gaven geen zichtbaar publiek (eigen trailer 23 views).

### Wat ze allemaal missen (mijn lezing, met bewijs per punt)
- **Geen doorbraakmoment in het fest.** Desktop Defender ging in zijn fest van 1 naar 1.548 gelijktijdige spelers en kwam in "most played demos" (verhaal 5). Van geen van de vier staat een piek, mijlpaal of verlanglijstgetal in hun eigen berichten; makers die zoiets halen melden het altijd (Cozy Mining, Lootborne, Black Cat in verhaal 7). GOK: ze kwamen er nooit in.
- **Niemand anders maakte video's.** Bij de twee winnaars zijn de meeste video's van anderen (gidsen, livestreams, recensies); bij de vier alleen eigen trailers of niets.
- **Op het plaatje lijkt het spel op elk ander fantasyspel.** Ik legde de zes capsules naast elkaar (header 460 px): Minimon, Idle Squire, Idlewood en Dungeoneers zijn verzorgd getekend, maar geen ervan laat zien dat het in een hoekje van je scherm leeft. Desktop Defender zegt het in de naam, Deskrawl in "Desk". Maar de naamtest hierboven zegt dat dat alleen niet genoeg is.

### Drie lessen
1. **Demo plus Next Fest plus updates is de norm, geen voorsprong.** Van de 16 kerkerspellen met demo haalden er 3 de 100 reviews. Minimon deed in juni wat Deskrawl deed (dagelijkse patches, livestream) en kwam uit op 7 reviews tegen 3.631. Het verschil zat niet in hoe hard ze werkten.
2. **Wis nooit de voortgang van demospelers tijdens een fest, en geef ze een reden om anderen te halen.** Minimon kondigde in mei wissen aan en wiste midden in het fest; Deskrawl gaf een ranglijst, een gezamenlijke baas en bèta voor de top 100, Desktop Defender gaf extra levels bij elk spelersdoel. Wie in een fest geen reden geeft om te blijven en te delen, krijgt geen piek, en zonder piek geen lijstjes.
3. **Meet tijdens het fest of je doorbreekt, en beslis dan.** De vier gingen na een stil fest gewoon door naar de lancering met hetzelfde spel en dezelfde capsule. Idlewood bracht vier weken na een fest zonder gemelde piek uit. Een stil fest is een uitslag, geen pech.

### Wat dit betekent voor Hats (en wat niet)
- Hats lijkt op deze vier (helden, buit, hoekje van het scherm, fantasy). De mediaan voor ons soort spel met demo is **8 reviews**. Dat is de uitkomst als we "gewoon goed" werken. Ons tijdpad in `planning-fest-2027.md` (pagina ±8 dec, fests jan en feb, uitbrengen begin maart: ±12 weken pagina) lijkt op dat van Idlewood (16 weken). Maar Desktop Defender had ook maar ±15 weken pagina, dus de korte tijd is niet de oorzaak; wat telt is wat er in het fest gebeurt.
- Wat ons anders maakt (hoeden op Gloop, helden met wrok, zie `onderscheid-hats.md`) moet in het fest zichtbaar worden. Bij de vier zag ik geen eigen stuk op de capsule.
- Onze save-regel (save gaat mee naar het volle spel, punt 6 van de demolijst) is precies goed; dit verhaal zegt: ook geen wis tijdens of tussen de fests.
- Wat niet geldt: van de vier ken ik geen verlanglijstjes en geen volgers, dus ik weet niet of ze klein binnenkwamen of veel verlanglijstjes slecht omzetten. Het Desktop Companion Fest is een eigen vak voor ons soort spel; misschien valt een klein spel daar meer op dan in Next Fest (GOK).

### Voorstel voor Dortus deze week
**Olaf zet in `platformen/steam/planning-fest-2027.md` een meetpunt op vr 15 jan (dag 2 van het Desktop Companion Fest) en een uitslag op ma 18 jan, met een vaste regel vooraf:** groeien de verlanglijsten in de festweek met minder dan 1.000 (GOK als grens; Cozy Mining ging in Next Fest van 2.000 naar 5.000, Black Cat stond na twee kleine fests op 2.000), dan gaat de verbeterweek naar de haak (capsule, eerste 30 seconden, tekst) en niet naar poetsen, en legt de hoofdchat de lanceerdatum van maart opnieuw neer. Plus twee regels voor de demo: **nooit de save wissen tijdens of tussen de fests**, en **één reden om anderen te halen** (bijvoorbeeld een gezamenlijke teller in de discussies: "samen 10.000 helden opgegeten, dan komt hoed X in de demo"; gezamenlijk doel zoals Desktop Defender, zonder eigen server). Melding staat in `berichten/olaf.md`.

### Eerlijk: wat ik niet weet
- Hoeveel verlanglijstjes en volgers de vier hadden; de volgerpagina van Steam gaf steeds "te veel verzoeken". Een volgende run kan dat alsnog proberen.
- Wat spelers zeggen: met 4 tot 7 reviews is er weinig, en de review-API werkte niet.
- Of de Minimon-video van 15.678 views betaald gepromoot is (GOK: het kanaal haalt verder 34 tot 433, dus dat zou kunnen).
- Of Dungeoneers Idle nog groeit: vijf dagen na de lancering is te vroeg.
- Spelers nu is één meting op een maandagochtend; bij spellen die op de achtergrond draaien zegt dat iets, maar weinig.

---

## 7. Elf bureaubladspellen uit een vol festival: wat Next Fest juni 2026 deed voor de spellen die PC Gamer koos (proef voor ons eerste Desktop Companion Fest)

Onderzocht 16 nov 2026, run 8. Vraag van de hoofdchat: hoe gebruikten makers het Desktop Companion Fest? Dat kan niet: het fest van 14 tot 18 jan 2027 is het **eerste** (de lijst met fests in de Steamworks-docs kent geen eerdere, GEZIEN 16 nov; de pagina van het fest zelf gaf bij curl "Sorry, an error occurred"). De beste proef is daarom een fest waar al honderden bureaubladspellen naast elkaar stonden: Steam Next Fest juni 2026 (15 tot 22 juni, GEZIEN uit de aankondigingen van Lootborne en Cozy Mining). PC Gamer schreef op 17 juni 2026 dat er "nearly 500 idlers" in zaten, startte er 45 tegelijk op, sloot alles wat haar niet "more than a few seconds" boeide en hield er 11 over. Ik heb die 11 gevolgd tot vandaag. Dat is precies onze situatie in januari: een vak vol lijkende spellen, en een kijker die in seconden kiest.

### Bronnen
- PC Gamer, 17 juni 2026 (schrijver: Andrea; achternaam stond niet in de tekst die ik las): https://www.pcgamer.com/games/i-ran-45-idle-game-demos-from-steam-next-fest-all-at-once-for-a-desktop-companion-battle-royale/ (GEZIEN met curl)
- Eigen aankondigingen van de makers op Steam, via de openbare nieuws-API `api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=<id>` (GEZIEN 16 nov): Black Cat Book Club 3972410, Cozy Mining 4283650, Lootborne 4335620, Duelist: Idle Expedition 4282780.
- Prijs, datum, demo: `store.steampowered.com/api/appdetails`; volgers: `steamcommunity.com/games/<appid>/memberslistxml/?xml=1` (GEZIEN 16 nov ±09:35 UTC). Reviews en talen uit Vera's kaart van 16 nov (`platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv`; de review-API van Steam stuurt nu door naar de voorpagina).
- Alles bij elkaar: `platformen/succes/data/nextfest-juni-2026-pcgamer-11.csv`.
- Niet gebruikt: een blog van gamineai.com over het Desktop Companion Fest; leest als automatisch geschreven en noemt geen bronnen.

### Cijfers: de 11 die de pers koos, vijf maanden later (GEZIEN 16 nov, tenzij anders)
| Spel | Prijs | Uit | Reviews | % | Volgers | Verlanglijsten (eigen melding) |
|---|---|---|---|---|---|---|
| Duelist: Idle Expedition (uitgever Infini Fun) | $8,99 | 8 okt | 744 | 76 | 3.822 | onbekend; 20.000 verkocht in 6 dagen |
| Lootborne | $1,99 | 21 sep | 478 | 57 | 1.843 | 10.000 na Next Fest, 20.000 bij lancering |
| Idyll Isle | $3,99 | 14 jul | 91 | 89 | 213 | |
| Black Cat Book Club (solo) | $4,99 | 25 sep | 76 | 100 | 1.158 | 2.000 dec 2025, 10.000 aug 2026 |
| PawMart Tiny Market | $5,99 | 15 sep | 42 | 90 | 441 | |
| Cozy Mining | $6,99 | 26 jun | 41 | 75 | 409 | 2.000 → 5.000 in het fest, 10.000 bij lancering |
| Grandpa's Bee Haven | $6,99 | 10 sep | 19 | 84 | 205 | |
| Idle Bookstore | $5,99 | 14 sep | 19 | 78 | 279 | |
| Succulent Break | $1,99 | 10 aug | minder dan 10 | | 11 | |
| Tiny Farmie | $4,99 | 16 sep | 4 | | 74 | |
| DeskFarm: Idle Garden | | nog niet uit | | | 18 | |

Mediaan: 42 reviews. Ter vergelijking (verhaal 5): Desktop Defender haalde na één Next Fest 652 reviews in de eerste week.

### Wat ze deden, in volgorde (de vier met eigen cijfers)
**Cozy Mining (kleine Japanse studio):** demo in Next Fest, op dag 2 al 2.000 verlanglijsten ("we honestly didn't expect this milestone so fast"), aan het eind van het fest 5.000, **drie dagen na het fest uitgebracht** met 10.000 (aankondigingen 17, 22 en 26 juni). Daarna bijna elke dag een update. Vijf maanden later: 41 reviews. Vier talen.

**Lootborne:** winkelpagina in mei, Discord en demo twee dagen vóór het fest (13 juni), tijdens het fest een "Demo Bonus Event" met een baas (Bifidus) en patches. Na het fest 10.000 verlanglijsten. Ze zouden de demo weghalen maar hielden hem aan "after seeing your support". Demo eraf in augustus, met twee badges in het volle spel voor wie de demo speelde en voor wie de baas versloeg. Bij lancering 20.000 verlanglijsten, prijs $1,99. Nu 478 reviews, maar 57%.

**Black Cat Book Club (één maker met "two cats helping me"; in Europa, GOK: de lanceringstijd staat eerst in CEST):** winkelpagina al in 2025, deed mee aan twee kleine festivals van anderen (Midwinter Spirits Festival en "Taskbar Treasure Week", "a festival focused on incremental idle games with cozy vibes") en stond op 9 dec 2025 op **2.000** verlanglijsten. Speeltest mei, demo op 12 juni vlak voor Next Fest. Daarna, met de feedback uit het fest, de kern omgebouwd: "like a proper desktop companion game, now the cat automatically studies the glyphs, but you can still help by clicking" (24 juli). In augustus **10.000** verlanglijsten, lancering 25 sep met 10% korting. Nu 76 reviews, 100% positief.

**Duelist: Idle Expedition (Chinese studio met uitgever):** speeltest maart, demo 8 mei, nieuwe demo met grote functie ("Deploy Three Teams at Once") speciaal voor Next Fest, lancering 8 okt in 31 talen met een aftelreeks van aankondigingen (7, 5, 3 dagen). 10.000 verkocht na 3 dagen, 20.000 na 6. Hun eigen bericht na 3 dagen geeft de klacht toe: "progression blockers and tedious operations".

### Drie lessen
1. **Het fest geeft verlanglijsten, maar die zeggen weinig over wat er daarna gebeurt.** Cozy Mining en Black Cat haalden allebei ±10.000 verlanglijsten en staan nu op 41 en 76 reviews; Lootborne op 20.000 en 478. Grof per verlanglijst: Cozy Mining 0,004 reviews, Black Cat ±0,006, Lootborne 0,024 (GEZIEN in hun eigen meldingen en de reviews; de verlanglijsten bij de lancering van Black Cat ken ik niet, dus "±"). Wat Lootborne anders heeft: $1,99 en een spel met vechten en buit; Duelist ook vechten, met uitgever en 31 talen. GOK: goedkope prijs en vechtspel zetten verlanglijsten beter om dan "cozy", maar vier spellen is te weinig om dat hard te zeggen.
2. **Uitgekozen worden door de pers is geen succes.** Vier van de elf (Tiny Farmie, Succulent Break, DeskFarm, Idle Bookstore) staan op minder dan 20 reviews of zijn nog niet uit. DeskFarm had in juni een demo, haalde PC Gamer en heeft vijf maanden later 18 volgers. Wat in het fest in een paar seconden boeit, is de toegang; wat daarna komt (vertalen, uitbrengen, diepte) beslist.
3. **De winnaars gebruikten de tijd na het fest om het spel te veranderen, niet alleen om te poetsen.** Black Cat maakte van een klikspel een spel dat zichzelf speelt en kreeg 100%. Lootborne hield de demo aan zolang hij klopte en beloonde demospelers met badges. Cozy Mining bracht drie dagen na het fest uit en had geen tijd voor zo'n ronde (75%). Bao Bao (verhaal 3) deed hetzelfde en kreeg "niets te doen" (82%).

### Wat dit betekent voor Hats (en wat niet)
- Ons plan is Black Cat in het klein: eerst een klein fest (Desktop Companion, januari), dan Next Fest (februari), dan uitbrengen (maart). Black Cat liet zien dat de kleine fests een begin geven (2.000), en Next Fest plus een betere demo de groei.
- Tussen ons fest (18 jan) en de inzending voor Next Fest (1 feb) zitten precies **twee weken**. Dat is onze enige verbeterronde met echte spelers vóór het grote fest. Die moet gepland zijn, anders gaat hij op aan kleine fouten.
- Wat niet geldt: Next Fest is veel groter dan een themafest (8.000+ demo's in oktober, PC Gamer), en wij staan in januari in een vak met honderden Desktop Companion-spellen; hoe een eerste fest uitpakt, weet nog niemand.

### Voorstel voor Dortus deze week
**Olaf:** zet in `platformen/steam/planning-fest-2027.md` de weken 18 jan tot 1 feb vast als "verbeterweek demo": één verandering op basis van wat fest-spelers zeggen (zoals Black Cat), geen nieuwe inhoud. Bouw daarvoor nu in de demo één knop of regel naar de Steam-discussies ("Tell us what bored you"), zodat we in vijf dagen genoeg reacties hebben. En geef demospelers iets mee naar het volle spel (een hoed voor Gloop, zoals de badges bij Lootborne en de hoeden bij Bongo Cat in verhaal 3). Melding staat in `berichten/olaf.md`.

### Eerlijk: wat ik niet weet
- De verlanglijsten van de andere zeven: ze meldden geen getallen. Ik weet dus niet of het fest hun weinig gaf of dat ze daarna weinig omzetten.
- Wie "Taskbar Treasure Week" organiseerde en hoeveel het Black Cat gaf: de aankondiging noemt geen link en zoeken gaf niets.
- Waarom Cozy Mining zo weinig reviews per verlanglijst heeft. Japanse en Chinese kopers schrijven mogelijk minder reviews (GOK); de verdeling van kopers per land is niet openbaar.
- Verkopen uit reviews schatten (de bekende vuistregel 30 tot 60 kopers per review) heb ik niet gedaan: bij zulke kleine aantallen is de spreiding te groot.

---

## 6. Your Big, Cute Monster Farm (KaiPlay Studio, China, eerste spel): waarom maar 77%, en wat hun tweede spel ons laat zien

Onderzocht 16 nov 2026, run 7. Tip van Vera: monsters verzamelen voor een hogere prijs ($7,99), maar maar 77% positief. Vraag: waarom, en wat leert het over verzamelen en de grindmuur? Onderweg vond ik het tweede spel van dezelfde studio (Legend of Defenders, 2 nov 2026, een idle torenverdediging die op de achtergrond doorvecht). Dat maakt het een vergelijking: twee spellen, twee tegengestelde fouten, hetzelfde gevolg.

### Bronnen
- Steam appdetails, winkelpagina, weekoverzicht reviews (`store.steampowered.com/appreviewhistogram/3659410`) en volgers (`memberslistxml`), gelezen 16 nov 2026. GEZIEN.
- Alle 37 aankondigingen via `ISteamNews/GetNewsForApp` (appid 3659410), van "nu op Steam" (26 jun 2025) tot 25 aug 2026. GEZIEN.
- Engelse reviews op steamcommunity.com (negatief en positief, acht sorteringen: meest behulpzaam, nieuwste, trends per week tot jaar, grappig): 32 verschillende negatieve en 34 positieve. Door alle 32 negatieve heb ik zelf heen gelezen. De JSON-reviews van Steam gaven een doorverwijzing, dus meer kon ik niet ophalen.
- Legend of Defenders (appid 4740930) en Tiny Pasture (3167550): appdetails, weekoverzicht, volgers, aankondigingen, top negatieve reviews. GEZIEN.
- Onze eigen balanssim: `producten/steam-hol/sim/sim.py`, door mij gedraaid met `python3 sim.py 40 3`. GEZIEN.
- Niet gelukt: SteamDB, verlanglijstcijfers, prijsgeschiedenis. Verkoop is dus GOK.

### Cijfers (GEZIEN 16 nov 2026, tenzij anders)
- Maker KaiPlay Studio, uitgever Gamersky Games (Chinees; ook uitgever of mede-uitgever van Tiny Pasture, Deskrawl en Desktop Raid). Uit 10 nov 2025, $7,99, 10 talen, Supporter Pack $2,99 op de lanceerdag. 71 prestaties.
- **1.232 reviews, 77% positief** ("Mostly Positive"); laatste 30 dagen 70% van 86. 3.469 volgers.
- Verkoop: 1.232 x 30 tot 60 = **37.000 tot 74.000 stuks** (GOK met de vuistregel). Dus ondanks 77% een echte verkoper, voor $7,99.
- Het cijfer stond er **vanaf week twee**, niet later gezakt: week 1 245 positief en 40 negatief (86%), **week 2 73 tegen 34 (68%)**, week 3 111 tegen 26. Opgeteld 81% na drie weken, 80% na drie maanden, 78% nu (weekoverzicht). Drie balansupdates (grond goedkoper 30 nov 2025, meer kans op vaardigheden 21 apr 2026, meer en goedkopere grond 25 aug 2026) hebben het niet meer opgetild.

### Wat ze deden, in volgorde
| Wanneer | Wat | Bron |
|---|---|---|
| 26 jun 2025 | Winkelpagina live | aankondiging, GEZIEN |
| 8 jul tot aug 2025 | Twee rondes Steam Playtest; ronde 2 met een herbouwde basis, saves van ronde 1 vervielen | aankondigingen, GEZIEN |
| 19 sep 2025 | Demo, met de save van de playtest | aankondiging, GEZIEN |
| 13 okt 2025 | Next Fest (hetzelfde fest als Desktop Defender in verhaal 5). In het festbericht: de **Fusion Lab** als "core feature currently in development" | aankondiging, GEZIEN |
| 8 tot 10 nov | Aftellen: drie berichten "nog 3, 2, 1 dag" | aankondigingen, GEZIEN |
| 10 nov 2025 | Uit, demosave gaat mee. Zelfde dag: samenwerking met Tiny Pasture (rode panda in het spel, bundel met korting). Melding dat de Duitse, Franse, Russische, Portugese en Spaanse tekst nog fouten heeft | aankondigingen, GEZIEN |
| 12 tot 30 nov | 14 updates en berichten in drie weken; 30 nov: "this is our team's first time developing a game" en grond goedkoper | aankondigingen, GEZIEN |
| dec 2025 tot aug 2026 | Kerst-, reuzengewas- en feestupdate, "biggest sale ever" (21 apr), daarna twee monsters en vier gewassen (14 aug) plus reclame voor hun nieuwe spel | aankondigingen, GEZIEN |
| 2 nov 2026 | Tweede spel Legend of Defenders uit, $14 (nu $9,80 met 30% korting), 5 talen | appdetails, GEZIEN |

### Waarom 77%: wat de negatieve reviews zeggen
Van de 32 negatieve gaan er **ongeveer 20 over de economie**: prijzen die veel harder stijgen dan wat je verdient (mijn eigen telling, met de hand nagelezen; reviews kunnen in meer groepen vallen). **Ongeveer 10** zeggen dat er na een paar uur niets nieuws meer komt, **5** klagen over toeval bij uitbroeden en samensmelten, 3 over slechte uitleg. Bugs en zwaar voor de pc: bijna niet. Wat ze letterlijk schrijven:
- De sprongen: "The land parcels go from 5,000 gold, to 50,000 gold, to 1,000,000 gold", terwijl een gewas van 10 naar hooguit 56 goud gaat (meest behulpzame negatieve review, 16,5 uur). Een ander: van 1 miljoen naar 10 miljoen voor de volgende uitbreiding.
- Het moment: "after around 10-12 hours it's starting to feel extremly grindy"; "I enjoyed this game while unlocking the first 10 different crops"; "I stopped feeling any sense of progress after maybe a day".
- Geen idle en geen actief spel: "If you leave it alone ... you gain nothing. But, if you keep playing it ... you'll spend your all gold and crystals in like 2 clicks" (191 uur).
- Waarom onderaan het scherm? "it's so slow that you may as well have it hidden for hours ... It feels like a decision made because bottom of the screen games were trending lately".
- Beloofd en niet geleverd: "I WANT THE FUSION LAB! ... an early access without saying it". Dat ding stond in het Next Fest-bericht.
- Toeval: "Fusion and hatching can feel like gambling"; "Hatching many eggs in a row and only getting..."
- Rusty's Retirement wordt drie keer genoemd als het spel dat het wel goed deed ("at least it was balanced").

Opvallend: de helft van de negatieve schrijvers heeft **50 uur of meer** gespeeld (16 van 32, mediaan 57,5 uur). Ook van de positieve reviews noemen er 13 van 34 de grind of de prijzen ("this game has more money crisis than real life itself"). De mensen vonden het spel dus leuk genoeg om het weken aan te laten, en werden daarna boos. Speeltijd zegt bij een idlespel weinig over plezier.

### Het tweede spel: de omgekeerde fout
Legend of Defenders (zelfde studio en uitgever, uit 2 nov 2026): **713 reviews in twee weken, 80%**, 2.878 volgers (GEZIEN). Week 1 374 tegen 95, week 2 186 tegen 58. Het verkoopt dus sneller dan Monster Farm (eerste week 469 reviews tegen 285), voor een hogere prijs, met 5 talen in plaats van 10. Maar de klachten:
- "I had the game running for 8 hours in the background ... my heroes were between lvl 2000 - 7000, i got billions of gold in an hour" (meest behulpzame negatieve review).
- "Access to legitimately new systems dries up about a few hours in"; "After the first 10–12 hours..."; "after you've unlocked all 18 SSR units and upgraded your castle to max ... nothing left to do".

Monster Farm was te duur, Legend of Defenders te makkelijk, en in **beide** haakten spelers af rond **10 tot 12 uur**, met hetzelfde woord: er komt niets nieuws meer. Het getal van de prijscurve is dus niet de kern; de kern is of er tussen uur 3 en uur 40 steeds iets nieuws te halen valt.

### Wat goed ging (want 37.000 tot 74.000 kopers is niet niks)
- **Het eerste uur.** Positieve reviews op de lanceerdag: "this is definitely the best idler I have played so far"; "It can be as hands on/off as you want". Week 1 was 86%.
- **Een uitgever met een reeks.** Gamersky zette Tiny Pasture (7.140 reviews, 21.716 volgers) ernaast met een bundel en een gast-dier op de lanceerdag, en gebruikt nu Monster Farm om Legend of Defenders te verkopen ("add Legend of Defenders to your Wishlist" in twee aankondigingen). Het tweede spel kwam sneller op gang dan het eerste.
- **Playtest, demo, fest, uitbrengen binnen een maand na het fest**, met de save mee. Zelfde ritme als Desktop Defender en Bao Bao.

### Drie lessen
1. **Het reviewcijfer van een idlespel ligt vast in de eerste drie weken, en wordt bepaald door uur 10, niet door uur 1.** Week 1 86%, week 2 68%, toen de eerste spelers de muur raakten; drie balansupdates daarna tilden het niet meer op (81% na drie weken, 78% nu). Wie de muur pas na de lancering repareert, is te laat.
2. **Spelers haken af als er niets nieuws komt, of het nu te duur of te makkelijk is.** Dezelfde studio maakte twee keer de fout andersom (sprongen van 10 en 20 keer, en daarna miljarden goud per uur) en kreeg twee keer dezelfde klacht rond 10 tot 12 uur. Wat Rusty's anders deed volgens deze reviewers: "balanced"; volgens verhaal 1 had Rusty's zelf de klacht "na 3 dagen op".
3. **Beloof in je festberichten alleen wat er bij de lancering in zit.** De Fusion Lab stond in het Next Fest-bericht als kernfunctie en ontbrak bij de lancering; dat werd "early access zonder het te zeggen" in een review. En toeval bij het verzamelen (eieren, samensmelten) gaf 5 van de 32 klachten: wie wil verzamelen, wil dat het lukt.

### Wat doen wij anders? (met een meting)
- Toeval: Hats heeft al "geen buit met kleine kans en geen eindgrind" en een Heldenboek dat 100% te halen is (`platformen/steam/features.md`, Bewust niet). Dat klopt met wat deze spelers vragen.
- **De muur: Hats heeft nu het probleem van Legend of Defenders, niet dat van Monster Farm.** Ik draaide onze eigen sim 40 uur (`python3 sim.py 40 3`, GEZIEN): **alles wat te koop is, is gekocht na 7,4 tot 7,5 uur open tijd**; 46 aankopen in de eerste 10 uur, daarna niets meer. De langste wacht tussen twee aankopen tot uur 10 is 38 tot 45 minuten. De hoedenberg-stempels (1000 hoeden na ±28 uur) en de aartsvijanden lopen door, maar er is na uur 7,5 niets meer om op te sparen. `balans.md` zegt dat zelf ook: "versie 1 moet hier ±40 uur van maken". Dat is precies de plek waar beide KaiPlay-spellen hun spelers verloren.
- De demo stopt na ±2 uur, dus op het fest merkt niemand dit. Maar het volle spel komt (voorstel) begin maart uit, en volgens les 1 beslissen de eerste drie weken daarna het cijfer.

### Voorstel voor Dortus deze week
**Een 40-uurstoets in de sim, met drie vaste getallen die groen moeten zijn vóór de lancering van het volle spel, zodat de inhoud van versie 1 erop gepland wordt.** (1) Laatste nieuwe aankoop of ontgrendeling: nu 7,4 uur, doel **minstens 35 uur** open tijd. (2) Langste wacht tussen twee nieuwe dingen tussen uur 3 en uur 40: doel **hooguit 45 minuten** open tijd (nu tot uur 10 al 38 tot 45, daarna oneindig). (3) Grootste prijssprong tussen twee stappen van hetzelfde ding: doel **hooguit 3 keer** (Monster Farm 10 en 20 keer; onze extra slijm of put is nu 2,6 keer, dat zit goed). Bram zet de drie getallen als regel onder elke run van `sim.py` (een uur werk, GOK); Olaf en Sanne plannen de stukken van versie 1 (4 soorten helden, 5 vallen, kamers, faam) zó dat ze over 40 uur verdeeld vrijkomen in plaats van in de eerste 7. Daarnaast voor Chris: in fest- en winkelteksten alleen noemen wat in de build zit die op dat moment uitkomt. Waarom deze week: het raakt de demo voor 18 dec niet, maar wel welke stukken van versie 1 er komen en wanneer; dat plan moet er zijn voordat er na het fest gebouwd wordt. Wie: Bram (toets), Olaf en Sanne (inhoud), Chris (teksten).

### Eerlijk: wat ik niet weet
- Hoeveel verlanglijstjes Monster Farm vóór de lancering had en wat Next Fest gaf. Er staat niets over in de aankondigingen, en SteamDB was niet bereikbaar.
- De Chinese reviews heb ik niet gelezen. Het spel heeft Chinese steun en een Chinese uitgever; de 77% geldt voor alle talen samen, mijn klachtentelling alleen voor Engels.
- Mijn telling van de klachten is met de hand en grof; één review kan in meer groepen vallen.
- Onze sim is een sim: hij koopt steeds het goedkoopste en kent de stukken van versie 1 nog niet. De 7,4 uur geldt voor wat er nu in `balans.md` staat.
- Of Legend of Defenders in een strook onderaan het scherm draait of in een klein venster, weet ik niet zeker. De winkeltekst noemt een venster dat je met één toets verbergt en vechten op de achtergrond; de studio noemt het zelf "a brand-new desktop companion experience". Voor Vera: een nieuwe, snelle verkoper in onze hoek (713 reviews in twee weken), nog niet in haar kaart.

---

## 5. Desktop Defender (Conradical Games, Zwitserland): van 200 naar bijna 50.000 verlanglijstjes in drie weken, door één Next Fest

Onderzocht 16 nov 2026, run 6. Tip van Vera: het dichtst bij ons spelgevoel dat al verkoopt (idle auto-battler in de hoek van het scherm, $4,99). Vraag: hoe kwamen ze aan hun publiek? Ik heb er een tweede vraag bij gezocht, omdat de maker daarna nog drie zulke spellen uitbracht: werkt het trucje twee keer?

### Bronnen
- Alle 48 aankondigingen van Desktop Defender via de nieuws-API van Steam (`ISteamNews/GetNewsForApp`, appid 3772810), gelezen 16 nov 2026. Allemaal geschreven door "Conrad, Lead Developer".
- Steam appdetails en winkelpagina's (16 nov 2026) van alle 13 spellen van Conradical Games; reviews per week via `store.steampowered.com/appreviewhistogram/<appid>`; volgers via `steamcommunity.com/games/<appid>/memberslistxml`. Alles GEZIEN.
- Interview door Chris Zukowski (How To Market A Game, 4 nov 2025): https://howtomarketagame.com/2025/11/04/the-optimistic-case-that-indie-games-are-in-a-golden-age-right-now/
- Persberichten van de uitgever Poysky Productions op Games Press: aankondiging 23 jul 2025 (https://www.gamespress.com/Desktop-Defender---Rustys-Retirement-meets-Tower-Defense) en na Next Fest (https://www.gamespress.com/The-Game-That-Went-From-3-to-1548-Concurrent-Players-in-One-Week---Des).
- Nieuws: GamesRadar 21 okt 2025 (https://www.gamesradar.com/platforms/pc-gaming/1-week-ago-we-had-3-players-steam-notifies-surprised-dev-their-demo-was-one-of-the-most-played-during-steam-next-fest), Mein-MMO 21 okt 2025 (https://mein-mmo.de/en/desktop-defender-steam-next-fest-erfolg,1532985), Automaton 22 okt 2025 (https://automaton-media.com/articles/newsjp/desktop-defender-20251022-362475/).
- Negatieve en positieve reviews (top, Engels) via steamcommunity.com, gelezen 16 nov 2026.
- Niet gelukt: SteamDB en Gamalytic (blokkade of betaalde sleutel), de JSON-reviews van Steam (gaf een inlogpagina). Verkoopcijfers zijn dus GOK.

### De maker
Conradical Games is een kleine studio in Zwitserland (Games Press, Mein-MMO). Sinds 2020 tien spellen op Steam, bijna allemaal zonder succes: Lootbox Lyfe 32 reviews, Girabox 25, The Outbound Ghost ($19,99, het grote spel) 226 reviews met 67%, Wanted Shadows 52, Soul Stalker 77, Little Laps 14 (GEZIEN). Desktop Defender is het eerste dat het haalde. Een ervaren maker dus, met jaren aan pogingen ervoor, geen beginner met geluk.

### Wat ze deden, in volgorde
| Wanneer | Wat | Bron |
|---|---|---|
| ±jul 2025 | Gebouwd in **ongeveer 2 weken**, "probably being 1 month total" tot de lancering. Onderdeel van een plan: "6 games in 12 months. 1 is a bigger one, the others are smaller ones a la Desktop Defender. Do the big ones for prestige/deals/etc. and the small ones to fill in the gaps revenue wise" | Zukowski, DERDEN |
| 23 jul 2025 | Winkelpagina en trailer bekend, met persbericht van uitgever Poysky ("Rusty's Retirement meets Tower Defense") | Games Press, DERDEN |
| 13 aug 2025 | Gesloten bèta, aanmelden via een formulier | aankondiging, GEZIEN |
| tot 13 okt 2025 | **Ongeveer 200 verlanglijstjes.** Bijna drie maanden pagina plus persbericht gaven dus vrijwel niets | Conrad zelf: "Went from 200 wishlists, to almost 50,000" (3 nov), GEZIEN |
| 13 okt 2025 | Demo live op de eerste dag van Next Fest, 10 levels. "It started with just 1 player for a few hours" | aankondiging 15 okt, GEZIEN |
| 14 en 15 okt | Discord geopend. Daar beloofde hij: boven 100 gelijktijdige spelers 10 levels erbij. Na 2 uur gehaald, demo naar 20 levels; doel 200, naar 25; doel 400, naar 30; doel 1.000 een verrassing. **Bij elke stap een aankondiging op Steam** | aankondigingen 14 en 15 okt, GEZIEN |
| 18 okt | Piek **1.548 gelijktijdige spelers** in de demo; top 5 tot top 10 meest gespeelde demo's van het fest; 280.000 uur gespeeld; demo 99% positief bij ±200 reviews | Mein-MMO, Automaton, persbericht, DERDEN |
| 20 okt | Mail van Valve: één van de populairste demo's, komt in het overzicht "most played demos", en het advies de demo te laten staan | GamesRadar, DERDEN |
| 4 nov 2025 | Uitgebracht, **drie weken na het fest**, $4,99 met 15% lanceerkorting en eigen lagere prijzen per land, 19 talen. Demo een paar uur ervoor weggehaald. Oproep: "Try to reach 50 reviews in the first 24h" | aankondigingen 3 en 4 nov, GEZIEN |
| 4 tot 18 nov | **14 dagen achter elkaar een patch**, elk met een eigen aankondiging en de zin "if you're enjoying the game, I would REALLY appreciate it if you reviewed it" | 15 aankondigingen, GEZIEN |
| 11 nov | Na een week: "Overwhelmingly Positive", 2.694 gelijktijdige spelers, top 5 meest gespeelde nieuwe spellen, 27 updates | aankondiging, GEZIEN |
| dec 2025 tot nu | Grote gratis updates elke 1 tot 3 maanden (Rebirth, Skins, Critical, Forge), steeds eerst op een bètatak. 9 mrt 2026: Daily Deal van Steam (30% korting) | aankondigingen, GEZIEN |
| 2026 | Drie opvolgers in dezelfde soort, elk met een andere uitgever, alle drie $4,99, met bundelkorting en een gratis skin over en weer | appdetails, aankondigingen, GEZIEN |

### Cijfers (GEZIEN 16 nov 2026, tenzij anders)
- **Desktop Defender:** 1.830 reviews in de weekoverzichten (winkel toont 1.788), 92% positief, 3.573 volgers. Eerste week **652 reviews**, eerste vier weken 1.205 (66% van alles). Daarna 10 tot 30 per week; de Daily Deal-week in maart gaf weer 79. Nu 0 tot 8 per week, 34 spelers op een maandagochtend.
- Verkopen: 1.830 x 30 tot 60 = **55.000 tot 110.000 stuks** (GOK met de vuistregel uit de rol). Na korting, regioprijzen, Steam-deel en uitgever blijft er per stuk veel minder dan $4,99 over; omzet voor de studio GOK in de orde van een ton.
- Speeltijd zegt weinig: SteamSpy meldt een mediaan van 279 uur, maar het spel draait op de achtergrond en heeft prestaties voor 50 en 100 uur spelen. Een reviewer: "You'll finish the game long before both of them."

### Werkt het een tweede keer? De opvolgers
| Spel | Uit | Uitgever | Reviews | Positief | Eerste week | Volgers |
|---|---|---|---|---|---|---|
| Desktop Defender | 4 nov 2025 | Poysky, Level Up Gaming | 1.788 | 92% | 652 | 3.573 |
| Card Corner (idle poker) | 9 mrt 2026 | Assemble Entertainment | 77 | 74% | 41 | 258 |
| Desktop Detective | 19 aug 2026 | Playsaurus | 183 | 85% (laatste 30 dagen 53%) | 69 | 1.277 |
| Screen Stocks (online handel) | 27 okt 2026 | Oro Interactive | 239 | 92% | 180 | 505 |

Alles GEZIEN. Zelfde maker, zelfde vorm, zelfde prijs, een eigen publiek van duizenden kopers die hij in aankondigingen bereikt, telkens een uitgever erbij, en toch maar **4 tot 13 procent** van de reviews van de eerste. Wat de reviews zeggen:
- Card Corner: "Way too repetitive and grindy"; "Gambling or poker doesn't really work (for me) if you have no active interaction"; "They updated the game for a week and then gave up".
- Desktop Detective: "requires near constant babysitting and menuing"; "far from an idler"; "Nothing really happens on the screen so you don't feel like you are progressing"; en twee keer: het lijkt te veel op Desktop Defender ("both games feel almost identical").
- Ook bij Desktop Defender zelf gaan de slechte reviews over hetzelfde: "not NEARLY idle enough", te veel klikken met Shift, onduidelijke uitleg, "a little too cpu intensive".

### Drie lessen
1. **Het publiek kwam niet van de pagina, de uitgever of de pers, maar van de demo in Next Fest.** Drie maanden pagina met persbericht: ±200 verlanglijstjes. Eén week Next Fest met demo: van 3 naar 1.548 spelers, en drie weken later bijna 50.000 verlanglijstjes. Een bureaubladspel heeft daar een eigen voordeel (GOK, mijn uitleg): het draait op de achtergrond, dus spelers laten het uren aan staan, en dat telt mee als "meest gespeeld". Iemand die 100 uur in een demo zit (Automaton zag zulke reviews) is één gelijktijdige speler, de hele dag.
2. **Van de demo een evenement maken, met elke stap een bericht.** De doelen (100, 200, 400, 1.000 spelers) gaven spelers een reden om vrienden te halen en gaven Steam vier aankondigingen in twee dagen. Na de lancering hetzelfde: 14 dagen elke dag een patch met bericht en een vraag om een review; week één 652 reviews. Dit is dezelfde les als Deskrawl in verhaal 2 (demo bijna dagelijks bijgewerkt tijdens Next Fest), nu bij een tweede spel.
3. **Een klein spel kan het halen, maar herhalen is geen recept.** Desktop Defender kostte ±2 weken bouwen en was het goedkoopste van tien spellen. Drie opvolgers in dezelfde vorm, met uitgevers en een eigen publiek, haalden 77 tot 239 reviews, en de klachten waren "niet idle genoeg" en "lijkt op de vorige". Wat het verschil maakte zie ik niet hard; de reviews wijzen op twee dingen die wij al op onze lijst hebben: echt doorgaan zonder jou, en op het scherm zien dat je vooruitgaat.

### Wat doen wij anders?
- Wij bouwen Hats of the Fallen al weken met een ploeg en 3D, naar één fest toe. Conrad bouwde in 2 weken en liet het fest beslissen. Wij zetten ook alles op een fest (Desktop Companion Fest 14 tot 18 jan, Next Fest februari), dus dat deel klopt; maar ons plan heeft geen idee voor wat er tijdens die week gebeurt.
- Onze demo stopt na ±2 uur speeltijd (vaste lijst punt 6, het spel blijft draaien). Bij Desktop Defender was de grens een aantal levels die tijdens het fest groter werd, en spelers bleven honderden uren. Hoe langer een bureaubladdemo aan staat, hoe meer hij meetelt.
- Wij hebben geen plek waar spelers samenkomen (geen Discord). Conrad opende zijn Discord op dag twee van het fest; daar kwamen de doelen, een wiki en mods vandaan.
- CPU: één van de klachten bij Desktop Defender. Onze grens (onder 1 CPU-seconde per 10 seconden) is een echte troef; zet het op de winkelpagina.

### Voorstel voor Dortus deze week
**Een fest-plan voor de demo, met een inhoudsgrens in plaats van een tijdgrens en twee vooraf gebouwde uitbreidingen die tijdens het Desktop Companion Fest vrijkomen bij doelen voor gelijktijdige spelers.** Concreet: (1) Olaf toetst of punt 6 van de demolijst kan worden: de demo stopt bij een vaste plek in het hol (bijvoorbeeld 10 gangen of een held van niveau X) in plaats van na 2 uur, en het spel blijft daarna gewoon draaien en goud tellen. (2) Olaf bouwt vóór 18 dec twee kleine extra stukken (bijvoorbeeld 5 gangen meer en één nieuwe hoed), al in de demo maar op slot; de vrijgave is een nieuwe build die Thijs in Steamworks met één klik live zet (zelf inloggen kan niemand anders). Zo blijft "niets nieuws na 18 dec" overeind. (3) De hoofdchat zet op de lijst van Thijs: een Discord-server vóór 14 jan (aanmaken kan alleen hij), en Chris schrijft vier korte Steam-aankondigingen klaar ("100 spelers: 5 gangen erbij"). Kosten: een dag of twee voor Olaf; risico: de doelen worden niet gehaald, dan zetten we ze lager (bij Conrad was het eerste doel 100). Wie: Olaf (demo), Chris (teksten), hoofdchat (lijst Thijs). Waarom nu: de demo-inhoud ligt op 18 dec vast, dus later kan het niet meer.

### Eerlijk: wat ik niet weet
- Hoe de demo in de eerste dagen werd gevonden. Conrad schrijft alleen "1 player for a few hours", daarna de groei. Of dat kwam door de lijsten van Next Fest, een streamer (Vinesauce deed een Next Fest-stream met 40.008 weergaven, GEZIEN, maar ik weet niet of het spel erin zat en wanneer) of door de tag Idler, weet ik niet.
- Wat Poysky en Level Up Gaming precies deden. Er staan twee persberichten van Poysky; meer heb ik niet gevonden.
- Verkoop en omzet: alleen de grove vuistregel. SteamDB en Gamalytic waren niet bereikbaar.
- Of mijn uitleg bij les 1 klopt (achtergrondspel telt zwaarder in "meest gespeeld") is een GOK; Valve zegt niet hoe die lijst wordt berekend.

---

## 4. Hoe taakbalkspellen op YouTube kwamen: acht spellen naast elkaar, plus een concurrent die op 6 jan uitkomt

Onderzocht 16 nov 2026, run 5. Vraag uit run 4: hoe kreeg een taakbalkspel YouTubers en streamers? Geen enkele maker schrijft daar zelf over (zie onder), dus ik heb het omgekeerd gedaan: per spel de best bekeken video's op YouTube opgezocht en ingedeeld naar soort. Zo zie je wie die video's maakte en wat daarvoor nodig was.

### Bronnen en werkwijze
- YouTube-zoekpagina, gesorteerd op weergaven, met curl gelezen op 16 nov 2026 (`youtube.com/results?search_query=<naam>&sp=CAM%253D`, de lijst uit `ytInitialData`). Per spel de bovenste 14 tot 16 video's. Weergaven zijn GEZIEN op die dag. Datums staan alleen als "2y ago" in de zoeklijst; de videopagina's zelf blokkeert YouTube voor ons ("Sign in to confirm you're not a bot"), dus exacte datums en abonneecijfers ontbreken.
- Spellen: Rusty's Retirement, Bongo Cat, Ropuka's Idle Island, Bao Bao's Cozy Laundromat, Tiny Pasture, Deskrawl, Desktop Heroes, Soggy Beans, Chonkers. Plus drie zoekopdrachten over het genre ("Steam Idler Fest 2025", "desktop companion games steam", "games that sit on your taskbar").
- Alle aankondigingen van Rusty (34), Bao Bao (17), Ropuka (29) en Bongo Cat (65) via de nieuws-API van Steam doorzocht op youtube, streamer, twitch, creator, curator, keymailer en influencer.
- Steam appdetails (16 nov 2026): Ropuka 4.113 aanbevelingen, $3,99, 10 talen, 2 mensen (Moczan en Little Chmura, Polen); Tiny Pasture 7.140, $4,07, uitgever Gamersky Games; Little Writer Desktop Companion, uitbrengdatum 6 jan 2027.
- Interview met Moczan (Ropuka) op Game Dev Journey: https://sites.google.com/view/game-dev-guide/home/developer-diaries/unity-diaries/ropukas-idle-island. Zegt niets over marketing, wel: het begon als zijproject en "after playing with the prototype and seeing people's reaction to it, we decided to turn it into a full game."

### Wat de makers zelf zeggen over YouTubers en streamers
Bijna niets. In 145 aankondigingen van vier spellen staat geen woord over sleutels sturen, Keymailer of influencers. Wat er wel staat, gaat allemaal over **streamers het makkelijk maken in het spel zelf**:
- Rusty: Twitch-koppeling vanaf de lancering (apr 2024, kijkers planten met !plant), een instelling "mainly used by streamers" (jun 2024), een tweede inlogmanier in de Twitch-gids (dec 2024). GEZIEN.
- Bao Bao: "Access to Twitch chat functionalities for streamers" (19 dec 2024, in de demo vóór het Idler Fest). GEZIEN.
Hoe de video's van anderen tot stand kwamen (sleutels gemaild, via Curator Connect van Steam, of vanzelf opgepikt) weet ik dus niet. GOK: het meeste vanzelf, via fests en lijstjes, zie hieronder.

### Wat er op YouTube staat, per soort
| Soort | Voorbeelden (weergaven, GEZIEN 16 nov) | Wie maakte het mogelijk |
|---|---|---|
| **1. Trailer op een groot kanaal** | Wholesome Games: Ropuka 26.843, Rusty aankondiging 20.242, Bao Bao 7.280. GameTrailers: Balatro x Rusty 44.633, Soggy Beans via Frosty Games Fest 1.728 | De maker levert de trailer aan (GOK: via een inzendformulier of een showcase; de pagina wholesomegames.com/submit bestaat niet meer) |
| **2. Trailer op eigen kanaal** | Rusty release-trailer 67.190, Deskrawl launch-trailer 15.848, Tiny Pasture launch 9.392 | De maker zelf |
| **3. Lijstjes en cozy-nieuws** | "MOST ADDICTIVE Incremental/Idle Games" 43.199 (Ropuka), "The BEST Idle Games to play While You Work" 16.577, PC Gamer Cozy Corner over bureaubladspellen 14.373 (Ropuka, Bao Bao en Tiny Pasture samen), Buckeye Bunny: review Rusty 66.632 en "31 FREE Chill & Cozy Games, Next Fest February 2025" 17.410 (met Bao Bao) | Niemand hoeft iets te doen behalve gevonden worden: in een fest, op een lijst, met een duidelijke titel |
| **4. Kanalen in andere talen** | Rusty: Koreaans (우주하마) **907.965**, Braziliaans 51.757 en 46.681, Taiwanees 44.788. Deskrawl: Japans 37.451, Koreaans 16.996, Taiwanees 13.132 en 13.902, Spaans (IlloRubiu, stream). Ropuka: Thai 5.695, Turks 1.578 | Vertaald spel (GOK dat het verband oorzaak is; Rusty had 11 talen en 46% kopers in Azië, zie verhaal 1) |
| **5. Genrekanaal en grote streamer** | Deskrawl: "The next Task Bar Hero!?" (Starker MMOs) 8.752, twee video's van Gaming Meets Experience ±6.000, Kripparrian (stream) 21.318, knekroTV 30.421 | Een bestaand publiek dat al een soortgelijk spel speelt (Task Bar Hero) en een haak die zij snappen (handelsmarkt van Steam) |

Wat opvalt:
- **De grootste video over Rusty is niet Engels.** Eén Koreaanse video heeft meer weergaven (908.000) dan alle Engelse video's over het spel in de lijst samen (rond 320.000; twee nog grotere treffers gaan over een kindertekenfilm "Rusty's World" en tellen niet mee).
- **Lijstjes doen het meeste werk bij de kleine succesjes.** Bij Ropuka en Bao Bao zijn de best bekeken video's geen eigen video's maar verzamelvideo's ("speel dit terwijl je werkt") en een Next Fest-overzicht. Een themafest of Next Fest is precies waar die makers hun lijst vandaan halen; er staan ook Idler Fest-overzichten (4.534 en 2.710 weergaven).
- **Het eigen kanaal van de maker telt alleen bij een trailer.** Behalve trailers maakte geen van de acht makers een video die in de bovenste 14 kwam.

### Wat níet werkte
- **Soggy Beans** (23 reviews): beste video is de trailer via Frosty Games Fest op GameTrailers, 1.728 weergaven. Daarna niets boven de 500. **Chonkers**: beste video 2.947, de rest onder 1.000.
- **Een naam die je niet kunt vinden.** Bij "Desktop Heroes" (104 reviews) staan in de bovenste 14 dertien video's over iets anders (Windows 10, Company of Heroes, Nexon); de beste echte video heeft 3.488 weergaven. Bij "Tiny Pasture" gaan de bovenste vier over paarden en kwartels, terwijl het spel 7.140 aanbevelingen heeft. Wie zoekt, vindt het spel niet. "Hats of the Fallen" heeft op YouTube en Steam nu geen botsing (zoektest 16 nov: Steam 0 treffers, YouTube alleen haakwerk en One Piece). Goed zo houden.
- **Bongo Cat** laat zien dat een bekend meme alles overstemt: de zoeklijst is gevuld met muziekcovers van het Bongo Cat-kanaal (63 miljoen), niet met het spel. Dat is geen route voor ons.

### Een concurrent in ons venster: Little Writer Desktop Companion
- Solo-maker JSLegendDev, een YouTuber met programmeerlessen (zijn gewone video's: 6.000 tot 114.000 weergaven, GEZIEN). Spel: een schrijvertje dat met jouw toetsaanslagen meeschrijft, "a productivity game".
- Aankondigingstrailer op zijn eigen kanaal, ongeveer 4 maanden geleden: **378.303 weergaven** (GEZIEN). Zijn bericht met de uitbrengdatum, 2 weken geleden: 1.461 (GEZIEN). Hij had dus één uitschieter, en die viel op het moment dat de pagina nieuw was.
- **Uitbrengdatum 6 jan 2027** (appdetails en aankondiging van 26 okt 2026, GEZIEN): 8 dagen vóór het Desktop Companion Fest. Hij gaat dus waarschijnlijk met korting of als nieuw spel in hetzelfde fest staan als wij (GOK).

### Drie lessen
1. **Een taakbalkspel komt op YouTube via andermans lijstjes, niet via eigen filmpjes.** De makers zelf maakten alleen trailers; de grote aantallen kwamen van verzamelvideo's, cozy-nieuws en fest-overzichten. Die makers putten uit fests en uit wat ze op Steam vinden. Meedoen aan het fest met een demo, een heldere titel en een capsule die in een lijstje opvalt, is dus het werk.
2. **Video's volgen de talen.** Rusty's grootste video is Koreaans, Deskrawl werd in Japan, Korea en Taiwan gestreamd. Dat past bij verhaal 1 (46% kopers in Azië); het onderbouwt het voorstel van de vertaaltabel die al bij Olaf ligt.
3. **Maak het streamers makkelijk in het spel, want daar zeggen makers wél iets over.** Rusty en Bao Bao bouwden Twitch-chatfuncties; geen van beiden schreef over e-mails aan YouTubers. Het eenvoudigste voor ons: een modus die er op een stream goed uitziet (groter beeld of een venster dat OBS kan vangen). Een Twitch-koppeling is te veel voor de demo van 18 dec.

### Eerlijk: wat ik niet weet
- Of de makers sleutels hebben gestuurd. De zoeklijst laat alleen zien wat er staat, niet hoe het kwam.
- Exacte datums: "2y ago" zegt niet of een video vóór of na de lancering kwam.
- YouTube is maar één kanaal. Bij Rusty kwam veel van TikTok, Reels en Twitch (verhaal 1); die tel ik hier niet.
- Zoekresultaten van YouTube zijn per land en per keer iets anders; dit is één meting.

### Voorstel voor Dortus deze week
**Joris (groei) maakt vóór 1 dec een lijst van ±30 YouTube-kanalen die lijstjes maken van idle-, taakbalk- en cozy-spellen en fest-overzichten** (beginnen bij de namen hierboven: Buckeye Bunny, The Indie Brew, Best Indie Games, Maybe Sarisa, CozyAriGames, Indie Signal, Ken Cikas, Indie Games Hub, Gaming Meets Experience, Starker MMOs; daarnaast Koreaanse, Japanse en Braziliaanse kanalen). Per kanaal: taal, soort video, openbaar zakelijk adres of formulier als dat op hun pagina staat. Het versturen (een korte mail met de demo, rond 8 jan als Valve de fest-trailer brengt) is iets plaatsen op internet en gaat dus via de lijst van Thijs. Waarom: bij elk geslaagd taakbalkspel kwamen de meeste weergaven van zulke kanalen, en we hebben zelf nul volgers.

Tweede punt voor de hoofdchat en Olaf (na de speeltest): zet Little Writer Desktop Companion (uit 6 jan 2027) in de vergelijking van de winkelpagina en het fest, en zet "ziet er goed uit op een stream" als wens op de lijst voor na het fest; niet in de demo, want de demolijst is vast.

---

## 3. Hoe makers het themafestival voor idle-spellen gebruikten: Idler Fest 2025, met Bao Bao's Cozy Laundromat als hoofdverhaal

Onderzocht 16 nov 2026, run 4. Vraag van de hoofdchat: hoe gebruikten makers het Desktop Companion Fest? **Eerlijk vooraf: dat fest bestaat nog niet.** Januari 2027 is de eerste keer; in de lijst van Valve met alle fests van 2026 staat het niet (GamingOnLinux, lijst van Valve, jan 2026). De beste voorganger is het **Steam Idler Fest van 3 tot 10 februari 2025**, het enige eerdere fest voor idle- en bureaubladspellen. Daar keek ik naar: wie deed mee, wat deden ze, en wat leverde het op.

Hoofdverhaal: **Bao Bao's Cozy Laundromat** (Destroyer Doggo, één maker met een pixelartiest), omdat die precies ons pad liep: demo, themafest als "binnenkort", Next Fest in februari, uitbrengen in maart. Naast hem drie andere makers op hetzelfde fest, die het elk anders gebruikten.

### Bronnen
- Lijst van alle 337 spellen met de tag Desktop Companion (tag-id 1320952), via de zoek-API van Steam, 16 nov 2026. Van de bovenste 120 alle aankondigingen doorzocht op "Idler Fest" via de openbare nieuws-API (`api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=<id>&count=100&maxlength=0&feeds=steam_community_announcements`). Zes spellen noemden het fest: Bongo Cat, Rusty's Retirement, Ropuka's Idle Island, Chonkers, Bao Bao's Cozy Laundromat, Soggy Beans.
- Alle 17 aankondigingen van Bao Bao (appid 3194550), dec 2024 tot okt 2026: https://store.steampowered.com/news/app/3194550
- Reviews per week uit het reviewhistogram van Steam (`store.steampowered.com/appreviewhistogram/<appid>`, alle talen; het totaal klopt met de winkelpagina), en de 10 meest behulpzame negatieve reviews van Bao Bao: https://steamcommunity.com/app/3194550/negativereviews/
- Appdetails (prijs, datum, talen, demo) en winkelpagina's (tags, reviewsamenvatting), 16 nov 2026.
- Bongo Cat: aankondigingen (appid 3419430) en het interview van Eurogamer met Marcel Zurawka (Irox Games), samengevat door PC Gamer, 26 jun 2025: https://www.pcgamer.com/gaming-industry/game-development/top-10-steam-game-bongo-cat-is-actually-losing-us-money-says-dev-which-is-fine-because-its-been-great-for-business-before-we-knocked-on-50-doors-now-they-are-coming-to-us
- Lijst van fests 2026: https://www.gamingonlinux.com/2026/01/valve-reveal-all-the-steam-events-scheduled-for-2026
- Niet gelukt: een eigen nabeschouwing van een maker met verlanglijstjes per dag tijdens het Idler Fest. Reddit is vanuit onze omgeving niet te lezen. Wat hieronder over verlanglijstjes staat, komt uit de eigen aankondigingen van de makers.

### Cijfers
| | Bao Bao's Cozy Laundromat | Bongo Cat | Soggy Beans | Ropuka's Idle Island | Chonkers |
|---|---|---|---|---|---|
| Rol in het Idler Fest | binnenkort, demo al 3 weken uit | binnenkort, demo uitgebracht op dag 1 van het fest | binnenkort, demo uitgebracht op dag 1 | net uit (29 jan 2025) | uit sinds dec 2024, 20% korting |
| Prijs | $3,99 | gratis (cosmetica, winkel met extra's) | $10,99 | $3,99 | $4,99 |
| Uitgebracht | 6 mrt 2025, 3 dagen na Next Fest | 5 mrt 2025, 2 dagen na Next Fest | 21 sep 2026, 19 maanden na de demo | 29 jan 2025 | 11 dec 2024 |
| Verlanglijstjes bij uitbrengen | **25.000** (DERDEN, eigen aankondiging 6 mrt 2025) | onbekend | onbekend | onbekend | onbekend |
| Daarna | 5.000 spelers na 3 weken; **15.000 verkocht na 9 maanden** (DERDEN, eigen aankondigingen 29 mrt en 27 nov 2025) | 150.000 spelers na 6 dagen, 500.000 na 4 weken (DERDEN, eigen aankondigingen); later ±$3.000 per maand omzet (DERDEN, Eurogamer via PC Gamer) | **23 reviews** na 8 weken (GEZIEN) | | |
| Reviews nu | 414, 82% positief (GEZIEN) | 31.301 Engelse, 96% (GEZIEN) | 23, 100% (GEZIEN) | 2.410 Engelse, 95% (GEZIEN) | 526, 87% (GEZIEN) |

Wat het fest deed met spellen die al uit waren (reviews per week, GEZIEN in het histogram):
- **Chonkers**: 4 tot 6 per week in januari, **30 en 28** in de twee weken van het fest (week vanaf 5 en 12 feb). Zes keer zoveel, met 20% korting als enige actie.
- **Ropuka's Idle Island**: 218 in de lanceerweek, **304** in de week van het fest, dus het fest gaf meer dan de lancering zelf.
- **Rusty's Retirement**: 394 in januari, 650 in februari 2025 (had ook een Daily Deal van Steam in dezelfde dagen, dus niet alleen het fest).
- Bao Bao: 15.000 verkocht op 349 reviews tot 27 nov 2025 = **±43 verkopen per review** (rekensom, DERDEN en GEZIEN). Dat past binnen de vuistregel x30 tot x60 uit onze rol.
- Bruto omzet Bao Bao in 9 maanden: 15.000 keer ±$3,50 (met kortingen) is ±$50.000; na het deel van Steam ±$35.000 (GOK, geen bron voor de echte omzet).

### Wat Bao Bao deed, in volgorde
1. **19 dec 2024:** "development is finally complete". Pas toen het spel af was, kondigde hij de demo aan, met de reden: eerst nog testen tot er geen grote fouten meer in zitten. In de demo zat een koppeling met Twitch-chat voor streamers.
2. **15 jan 2025:** demo uit. YouTubers maakten er filmpjes over (hij noemt QC Done en GameTout bij naam).
3. **30 jan:** lanceerdatum bekend (6 maart), vóór het fest, zodat bezoekers van het fest een datum zagen.
4. **3 tot 10 feb: Idler Fest** als "binnenkort" met demo. Bericht op dag 2: "It's been 17 days since I launched the demo, and the response has been absolutely incredible."
5. **8 feb, midden in het fest:** de Gouden Panda aangekondigd, een zeldzame versiering **alleen in de demo**, voor wie 100.000 goud verdient, en alleen te halen van 3 tot 6 maart (de dagen vlak voor de lancering). Een reden om de demo te blijven spelen tot de koopdag.
6. **19 feb:** aankondiging Next Fest (24 feb tot 3 mrt 2025), met dezelfde demo.
7. **6 mrt:** uitgebracht voor $3,99, "less than the price of a coffee", met 25.000 verlanglijstjes. 20 talen.
8. **Maart:** St. Patrick's-evenement en een focustimer die een speler vroeg. Daarna kortingen in themafests ("Minimal & Chill", april), een tweede Bao Bao-spel (aug 2025), en een pauze "due to burnout" tot de kerstupdate van nov 2025.

### Wat de spelers van Bao Bao zeiden (meest behulpzame negatieve reviews)
Bijna allemaal hetzelfde: mooi, maar er is niets te doen. "There is absolutely nothing here mechanically." "It feels more like a proof of concept than a fully fleshed out game." "I excitedly bought at full price when it launched ... because I loved the art style so much." Verder: uitleg bij voorwerpen ontbreekt, voortgang heel traag, panda's lopen vast. Een speler had het spel in zijn top 5 van meest verwachte spellen. **De beelden en het fest haalden de verlanglijstjes; de diepte bepaalde de reviews (82%, tegen 96% bij Bongo Cat en 87% bij Chonkers).**

### Wat de anderen deden op hetzelfde fest
- **Bongo Cat** bracht de demo uit op de avond dat het fest begon, en zette de volgende dag al een update met wensen uit reviews en Discord (kat verschuiven, naar een ander scherm, knop in de taakbalk verbergen). Wie de demo 30 minuten speelde, kreeg in het volle spel twee exclusieve hoeden. Next Fest 3 weken later, uitbrengen 2 dagen na Next Fest. Let op: Bongo Cat was al een bekende meme sinds 2018 en is gratis; het succes komt grotendeels daarvandaan, niet van het fest. De maker zegt zelf dat het spel ±$3.000 per maand oplevert en "actually losing us money", maar dat het als reclame voor hun volgende spel werkt: "before, we knocked on 50 doors; now, they are coming to us."
- **Ropuka's Idle Island** kwam 5 dagen vóór het fest uit, en zette midden in het fest een **Idler Fest-stickerverzameling** in het spel als bedankje ("We're midway through Idler Fest and we are thrilled to see how many new people discovered our little frog").
- **Soggy Beans** (aquarium op het bureaublad) bracht een vroege demo uit voor het fest, alleen in het Engels, en deed daarna mee met Next Fest juni 2025, een Back to School-viering, Animal Fest, Ocean Fest en Anime Fest. De demo-saves werden twee keer gewist. Het spel kwam pas 19 maanden na de demo uit, voor $10,99, en heeft na 8 weken 23 reviews. De demo zelf heeft 21 reviews, 10 daarvan in de eerste week.

### Drie lessen
1. **Een themafest werkt het best als de lancering er vlak achter zit.** Bao Bao en Bongo Cat brachten uit binnen 5 weken na het fest en 2 tot 3 dagen na Next Fest; Soggy Beans liet 19 maanden tussen demo en lancering en kwam op 23 reviews. Oorzaak en gevolg zijn niet zeker (prijs en spel verschillen), maar de volgorde demo, themafest, Next Fest, meteen uitbrengen hoort bij de twee die het haalden. Ons plan (fest 14 jan, Next Fest 22 feb, uitbrengen maart) is precies het pad van Bao Bao.
2. **Geef demospelers een reden om tot de koopdag te blijven, en iets wat ze meenemen.** Bao Bao: een Gouden Panda alleen in de demo, alleen te halen in de dagen vóór de lancering. Bongo Cat: twee exclusieve hoeden voor wie 30 minuten de demo speelde. Ropuka: stickers met het fest als thema. Alle drie kosten weinig en geven een reden om terug te komen en erover te praten.
3. **Beelden en een fest halen verlanglijstjes, maar alleen diepte houdt reviews hoog.** Bao Bao haalde met een lief uiterlijk 25.000 verlanglijstjes en 15.000 verkopen, maar de klacht in vrijwel elke negatieve review is "niets te doen", en de maker brandde op. Dit is dezelfde les als "not idle enough" bij Desktop Heroes (verhaal 2), van de andere kant: daar te veel aandacht nodig, hier te weinig om naar te streven.

### Eerlijk: wat niet zomaar voor ons geldt
- Het Desktop Companion Fest is nieuw. Het Idler Fest had een bredere groep (alle idle-spellen, ook boerderijen en klikspellen); ons fest is smaller, dus minder bezoekers maar wel precies onze kopers (GOK).
- De 25.000 verlanglijstjes zijn een eigen opgave van de maker, niet nagekeken. Hoeveel daarvan door het Idler Fest kwamen, weet ik niet; hij had ook YouTubers, Next Fest en een demo van 7 weken.
- Bongo Cat is een bekende figuur en gratis. Niet als maatstaf gebruiken.
- Ropuka en Chonkers laten zien dat het fest ook spellen helpt die al uit zijn. Voor ons is dat pas in een volgende editie (2028) van belang.

### Voorstel voor Dortus deze week
**De hoofdchat besluit vóór 18 dec: in de demo komt één fest-hoed voor Gloop, die je krijgt als je de demo speelt tijdens het Desktop Companion Fest (14 tot 18 jan) of Next Fest, en die via de save meegaat naar het volle spel.** Waarom: drie van de vier makers die het Idler Fest goed gebruikten, gaven demospelers iets exclusiefs (Gouden Panda, twee hoeden, fest-stickers), en ons spel gaat over hoeden: een "Fest Hat" is het meest logische cadeau dat er is. Onze save gaat al mee naar het volle spel (Bongo Cat kon dat niet door de regels van Steam-voorwerpen; wij gebruiken een gewone save, dus dat probleem hebben wij niet, GOK tot Olaf het bevestigt). Wie: de hoofdchat beslist (de demolijst is vast, dit is een kleine toevoeging), Olaf bouwt het (één hoed, een datumcheck of een vlag "demo gespeeld"), Daan maakt de hoed in de 3D-stijl, Chris zet hem in het bericht van 8 januari ("play the demo during the fest and keep the Fest Hat forever").

Voor Hans en Chris (geen actie nu): houd de lanceerdatum in maart zo dicht mogelijk na Next Fest (Bao Bao en Bongo Cat: 2 tot 3 dagen erna), en zet de datum al vóór het Desktop Companion Fest op de pagina, zoals Bao Bao deed op 30 januari.

---

## 2. Desktop Heroes (Telazer, 3 mensen) naast Deskrawl (First Day Games, 2 mensen): hetzelfde idee, heel andere uitkomst

Onderzocht 16 nov 2026, run 3. Het verhaal van een taakbalkspel dat het minder goed deed, met een tweelingspel dat het wel haalde ernaast, zodat het verschil zichtbaar wordt. Beide zijn een "idle ARPG" (helden vechten en vinden buit) in een strook boven de taakbalk, beide voor ±$4 tot $7, beide met een uitgever, beide met een demo in Next Fest en een lancering ±4 maanden na de aankondiging.

### Bronnen
- Eigen aankondigingen op Steam, alle berichten gelezen via de openbare nieuws-API: Desktop Heroes (33 berichten, aug 2025 tot mrt 2026) https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=3734200&count=60&maxlength=0&feeds=steam_community_announcements en Deskrawl (38 berichten, mei tot nov 2026) https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=4623570&count=60&maxlength=0&feeds=steam_community_announcements
- Steam appdetails 3734200 en 4623570 (prijs, talen, aantal beoordelingen, uitgever) en de winkelpagina's (reviewsamenvatting), met curl opgehaald 16 nov 2026.
- Steam-reviews, de 10 "meest behulpzame" negatieve en positieve van Desktop Heroes en de 10 negatieve van deze week van Deskrawl: https://steamcommunity.com/app/3734200/negativereviews/ en https://steamcommunity.com/app/4623570/negativereviews/
- Interview met Telazer op de site van Phaser (8 mei 2026): https://phaser.io/news/2026/04/desktop-heroes-phaser-electron-steam
- Persbericht aankondiging Desktop Heroes op Game Developer (4 jul 2025): https://www.gamedeveloper.com/press-release/telazer-games-announces-new-game-desktop-heroes
- Geen bron gevonden met verlanglijstjes of verkoopcijfers van een van beide. Alles over verkoop hieronder is daarom een schatting uit reviews (GOK).

### Cijfers naast elkaar
| Wat | Desktop Heroes | Deskrawl | Label |
|---|---|---|---|
| Maker | Telazer, 3 mensen, eerste Steam-spel (wel 1 miljoen spelers met webspellen) | First Day Games, 2 mensen, tweede spel, "duizenden uren Diablo" | DERDEN (Phaser-interview) en DERDEN (eigen aankondiging 18 mei 2026) |
| Uitgever | Blackburne Games Studio | Gamersky Games (Chinees), plus een QQ-groep naast Discord | GEZIEN (appdetails, aankondiging) |
| Aangekondigd | 4 jul 2025 | ±11 mei 2026 ("vorige week" op 18 mei) | DERDEN |
| Demo | 7 aug 2025 in het Debut Festival, daarna Next Fest okt 2025 (vanaf 13 okt) | 15 jun 2026, in Next Fest juni | DERDEN (aankondigingen) |
| Lancering | 27 okt 2025, één week na Next Fest | 28 sep 2026, ruim 3 maanden na Next Fest, na een gesloten en daarna open bèta (19 tot 28 aug) | DERDEN |
| Prijs | $5,99 (een review van 30 okt 2025 noemt "6 whole dollars"; Phaser schreef in mei 2026 $3,99, mogelijk een korting) | $6,99, lancering met 30% korting, nu weer 30% korting | GEZIEN (appdetails 16 nov 2026) |
| Talen | 14, met Chinees, Japans, Koreaans | 13, met Chinees, Japans, Koreaans, Thai | GEZIEN |
| Beoordelingen | **104 na ruim 12 maanden**, 70% positief | **3.630 na 7 weken**, "Mixed"; laatste 30 dagen 777 reviews, 36% positief | GEZIEN (winkelpagina 16 nov 2026) |
| Engelstalige reviews | (bijna) allemaal | 484 van 3.630 = 13%; de rest vooral andere talen | GEZIEN, het percentage is mijn rekensom |
| Verkocht (grof) | 104 x 30 tot 60 = ±3.000 tot 6.000 | 3.630 x 30 tot 60 = ±110.000 tot 220.000 | GOK (vuistregel uit de rol; Chinese spelers schrijven mogelijk vaker een review, dan is Deskrawl lager) |
| Laatste bericht maker | 24 mrt 2026 (daarna 8 maanden stil) | 12 nov 2026, elke paar dagen een patch | GEZIEN |

Ter vergelijking: Rusty's Retirement heeft 13.987 beoordelingen (verhaal 1).

### Wat Desktop Heroes deed, in volgorde
1. **Aankondiging met persbericht** (4 jul 2025), daarna een demo in het **Debut Festival** van Steam (7 tot 11 aug), een festival voor eerste spellen.
2. **Tussen de twee festivals de hele code omgegooid**, 2 sep 2025: "All old saves and progress will be deleted upon updating." Wie de demo in augustus speelde, begon in september opnieuw.
3. **Next Fest okt 2025 met een stream, en één week later lanceren** (aangekondigd op 23 okt, uit op 27 okt).
4. **De eerste weken bijna elke dag een update**, en meteen de kern van de klachten: het spel is niet idle genoeg. De makers antwoordden op 31 okt met een eigen bericht: "Desktop Heroes is not designed to be a game that you can set up and leave running for hours without interacting with it." Ze kozen bewust een mengvorm ("Unlike other 'bottom-of-the-screen' games, we aimed to create a hybrid experience").
5. **Pas 7 weken na de lancering bijgestuurd** (16 dec 2025, "We heard you ... we made the game more idle-friendly"), daarna een roadmap die schoof, een groot verhaal-update in mrt 2026 (v3.0.0), en sindsdien stilte.

### Wat de spelers zeiden (Desktop Heroes, de meest behulpzame negatieve reviews)
- "As an idle game, there is no idle progression. As an ARPG, there is no action." (31 okt 2025)
- "It's neither idle (needs you to intervene in high difficulty) nor manual (you can't afford the time to babysit the whole game). Make. Up. Your. Mind." (28 okt 2025)
- "If you die you stop progressing all together, so the idleing just stops." (8 nov 2025)
- "it's incredibly distracting ... I really can't have it running while studying, programming, or working ... TLDR; Not idle enough." (14 dec 2025)
- "No idle progress and no offline progress." (apr 2026)
- Ook "barebones", "recycled sprites" en "just another pile of slop added to the idler genre" van iemand die "close to 150" idle games speelde: kenners vergelijken met veel gratis idle games.
- Positief, ook terugkerend: het idee ("it's fun to glance down and see your little hero fighting") en snelle patches. Opvallend: één van de top-positieve reviews was eerst negatief en draaide om door de patches.

### Wat Deskrawl anders deed, in volgorde
1. **Een duidelijke belofte aan een bekende groep:** "a game that we could always play no matter if we are working, or watching TV shows", van twee Diablo-spelers voor Diablo-spelers. Aankondiging, en vijf weken later al een demo in Next Fest.
2. **De demo als levend spel behandeld:** in de eerste week van de demo zes patches, waarvan drie met nieuwe inhoud (nieuwe kaart, max level omhoog, nieuwe legendarische spullen "for you all to explore and test during Next Fest"), allemaal op verzoek van spelers (venster schalen, cloud save).
3. **Spelers een reden gegeven om te blijven en vrienden te halen:** een ranglijst in de demo, een baas-evenement waar "about 4000 players" de baas versloegen, de top 100 kreeg toegang tot de bèta, en 1.000 bètasleutels werden verloot onder de rest. "Don't forget to invite your friends if they haven't tried the demo yet!"
4. **Gesloten bèta, daarna open bèta, pas daarna lanceren** (3 maanden na Next Fest), met 30% korting en twee nieuwe klassen.
5. **Een Chinese uitgever en een QQ-groep vanaf de eerste dag.** 87% van de reviews is niet Engels (rekensom). Het spel lijkt vooral in Azië verkocht (GOK, het precieze land per review heb ik niet).

**Maar Deskrawl gaat nu mis op iets anders:** 36% positief in de laatste 30 dagen. De klachten van deze week gaan over handel met echt geld en buit: spullen te koop op de Steam-markt, "so leaderboards mean nothing", prijzen die keldern, te weinig buit ("74 hours not a SINGLE rune drop"), en spelers zonder online modus missen "the 300% loot buff". Een goed begin beschermt niet tegen een verdienmodel dat spelers oneerlijk vinden.

### Drie lessen
1. **"Onderaan je scherm" is een belofte: het moet ook zonder jou doorgaan.** De grootste klacht over Desktop Heroes was niet de prijs of de beelden, maar dat het niet idle genoeg was: doodgaan stopt de voortgang, geen voortgang als je weg bent, en het trekt te veel aandacht tijdens werk. De makers gaven dat zelf toe ("not designed to ... leave running for hours"). Spelers in dit genre kopen rust, geen tweede taak.
2. **Een demo die leeft en een reden geeft om terug te komen, wint.** Deskrawl patchte de demo tijdens Next Fest bijna dagelijks, deels met nieuwe inhoud, maakte er met een ranglijst en een baas-evenement een wedstrijd van (±4.000 spelers versloegen de baas, DERDEN) en beloonde de fanatiekste spelers met de bèta. Desktop Heroes wiste tussen twee festivals alle saves en lanceerde een week na Next Fest. Of die volgorde de oorzaak is, is niet bewezen (GOK), maar het verschil in uitkomst is ±35 keer in reviews.
3. **Talen alleen zijn niet genoeg; een partij die de markt kent wel.** Beide spellen hadden Chinees, Japans en Koreaans. Het verschil: Deskrawl had een Chinese uitgever en een QQ-groep vanaf de aankondiging. Dit verfijnt de les van Rusty's (46% Azië): de vertaling opent de deur, maar iemand moet er ook mensen naartoe brengen (GOK in hoeverre, er zijn geen landcijfers).

Extra, kleiner: Deskrawl laat zien dat handel en online buit-bonussen in een rustig spel snel als oneerlijk voelen. Wij hebben geen handel en willen dat zo houden.

### Eerlijk: wat niet zomaar voor ons geldt
- Beide zijn ARPG's met buit en gevechten; Hats of the Fallen is een spel waar je zelf het hol bent. Onze kern (helden komen naar jou, jij graaft en zet bewoners neer) is van zichzelf al meer idle. Ons ontwerp heeft "nooit straffen als je weg bent" al als eis (T3 en demo-eis 4 in `planning-fest-2027.md`). Les 1 bevestigt die keuze, het is geen nieuw werk.
- Deskrawl is pas 7 weken uit; hoe het afloopt weet niemand. Desktop Heroes verkocht misschien toch genoeg voor een team van drie met lage kosten (GOK).
- Een ranglijst of evenement in een demo vraagt servers of een account bij Steam (leaderboards). Dat is techniek die wij nog niet hebben, en de demolijst ligt vast tot 18 dec.

### Voorstel voor Dortus deze week
**Olaf zet in de speeltest van 4 dec voor Thijs twee vaste vragen en in de simulatie één vaste meting: (1) "Kon je 15 minuten werken terwijl het draaide, zonder dat het je aandacht trok?", (2) "Gebeurde er iets goeds terwijl je niet keek?", en (3) in de simulatie: een uur zonder één klik geeft minstens de helft van het goud van een uur met klikken, en niets staat stil.** Waarom: de grootste klacht over het taakbalkspel dat mislukte was "not idle enough", en die kwam pas na de lancering boven. Wij hebben de regel al op papier; dit maakt hem toetsbaar vóór de demo. De helft is een eerste getal (GOK), Olaf en Bram mogen het na de simulatie bijstellen. Wie: Olaf (vragen en meting), de hoofdchat neemt de vragen op in het speeltestformulier.

Voor na 18 dec (geen actie nu, voor Hans en de hoofdchat): tijdens het Desktop Companion Fest en Next Fest de demo bijhouden zoals Deskrawl (elke dag fouten oplossen en dat melden in een aankondiging), nooit saves wissen tussen festivals, en het volle spel niet een week na Next Fest uitbrengen maar pas als de klachten uit de demo verwerkt zijn.

---

## Vraag van de hoofdchat (16 nov): valt vertalen met AI onder de AI-melding van Steam, en wat kost een mens?

Onderzocht 15 nov 2026 (klok van de run), run 2. Geen verhaal maar een vraag; antwoord kort bovenaan, onderbouwing eronder.

### Kort antwoord
1. **Ja. Vertalen met AI valt er letterlijk onder.** Valve noemt vertalen (localization) bij naam als inhoud die gemeld moet worden. Ook als een mens de AI-vertaling daarna nakijkt, is de tekst "met hulp van AI-tools gemaakt", dus melden (dat laatste is mijn lezing van de definitie, geen apart citaat van Valve).
2. **Maar voor ons verandert het weinig.** Wij melden toch al AI: de spel- en winkeltekst schrijven Claudes. Het voorstel van Abel voor de melding (`platformen/abel/accounts/steam.md`) noemt al "text and code ... made with the help of AI tools". AI-vertalen voegt één woord toe aan een melding die er al staat; het maakt van een spel zonder melding geen spel met melding.
3. **Een mens kost ongeveer €45 tot €70 per taal voor 500 woorden**, dus ±€190 tot €270 voor Vereenvoudigd Chinees, Japans, Koreaans en Duits samen, plus mogelijk een minimumbedrag per opdracht en extra voor elke latere tekstwijziging.

### De regel van Valve (bron en citaat)
- Bron: Steamworks-documentatie, pagina Content Survey, deel 3 "Generative Artificial Intelligence Content", met curl gelezen op 15 nov 2026: https://partner.steamgames.com/doc/gettingstarted/contentsurvey
- Citaat (één zin): "This includes content such as artwork, sound, narrative, localization, etc." De zin ervoor zegt waar het om gaat: "the use of AI in creating content that ships with your game, and is consumed by players." GEZIEN.
- Sinds wanneer: deze tekst staat er sinds ongeveer 17 jan 2026. GamingOnLinux meldde op die dag (via GameDiscoverCo) dat Valve het formulier zo had aangepast, met precies dit citaat: https://www.gamingonlinux.com/2026/01/valve-tweak-steam-ai-disclosure-form-for-developers-to-clarify-its-for-content-consumed-by-players DERDEN.
- Wat er níet onder valt: hulpmiddelen die alleen het werk versnellen ("Efficiency gains through the use of these tools is not the focus of this section"). Volgens FinalBoss valt ook winkeltekst, capsule en trailer eronder (DERDEN, niet in de tekst van Valve zelf gezien).
- **De demo heeft een eigen Content Survey.** Steamworks, pagina Demos: "Make sure your Content Survey accurately reflects the demo content." GEZIEN: https://partner.steamgames.com/doc/store/application/demos . Komen er talen in de demo, dan moet de melding van de demo dat ook zeggen.

### Hoe gewoon is een AI-melding nu?
- FinalBoss (nov 2026, eigen analyse van ±63.600 Steam-uitgaven sinds jan 2024): **49,9% van de spellen die in okt 2026 uitkwamen heeft een AI-melding**, tegen 26,4% in okt 2025. Bij spellen met een melding noemt 30% "tekst en vertalingen", 63% beelden, 26% winkelpagina. https://finalboss.io/steam-ai-disclosures-hit-49-9-what-buyers-should-check DERDEN (de methode is niet openbaar, dus voorzichtig).
- Wat dit betekent: de melding is geen uitzondering meer, de helft van de nieuwe spellen heeft er een. Of hij de verkoop drukt is daarmee niet gezegd; het getal "tot 53% minder" uit de YouTube-video is nog steeds NIET NAGEKEKEN.
- Eigen meting in de repo (verkenner, itch.io, kleine aantallen): tools met AI-melding haalden minder vaak 3+ beoordelingen (0,8% tegen 3,7%). Andere winkel, maar het wijst dezelfde kant op: een melding kost waarschijnlijk iets. GOK hoeveel.

### Wat kost een menselijke vertaler?
| Bron | Prijs per woord | 500 woorden | Label |
|---|---|---|---|
| Allcorrect (groot spelvertaalbureau), openbare prijslijst: https://allcorrectgames.com/localization-pricing/ | Duits en Japans €0,10 tot €0,14; Koreaans en Trad. Chinees €0,09 tot €0,14; Vereenvoudigd Chinees €0,09 tot €0,12 | €45 tot €70 per taal | DERDEN (gelezen 15 nov 2026) |
| Gastartikel van een vertaalbureau op Game Developer (oud, datum niet te lezen): https://www.gamedeveloper.com/programming/how-much-does-game-localization-cost- | €0,09 tot €0,12 voor de grote talen, Chinees inbegrepen | €45 tot €60 | DERDEN |

- Optelsom voor de vier talen uit het Rusty-voorstel (zh-Hans, ja, ko, de) bij 500 woorden: Chinees €45 tot €60, Japans €50 tot €70, Koreaans €45 tot €70, Duits €50 tot €70, **samen €190 tot €270**. Mijn rekensom met DERDEN-prijzen.
- Kleine opdrachten: "The majority of translators and localization agencies charge a minimum fee" (Game Developer). Allcorrect heeft er ook een, maar zegt die maar zelden te rekenen. Bij 500 woorden kan dat minimum de prijs bepalen (GOK, hoe hoog staat er niet).
- Herhalingen zijn bij Allcorrect gratis. Testen in het spel (LQA, kijken of de tekst past en klopt in beeld) is een aparte post die hier niet in zit.
- Elke latere tekstwijziging is een nieuwe opdracht. Bij een spel dat nog verandert is dat de verborgen kostenpost.

**Bijgewerkt 16 nov met de telling van Olaf (±1700 woorden, niet 500):** met dezelfde prijzen van Allcorrect (DERDEN) kost het Chinees €153 tot €204, Japans €170 tot €238, Koreaans €153 tot €238, Duits €170 tot €238, **samen ±€650 tot €920** voor vier talen (mijn rekensom). Alleen Chinees en Japans nakijken of vertalen: ±€320 tot €440. Het minimumbedrag per opdracht speelt bij 1700 woorden waarschijnlijk geen rol meer (GOK). Het voorstel hieronder blijft staan: de demo met AI-vertaling; een mens pas als Azië verlanglijstjes geeft, en dan is het bedrag ruim drie keer zo hoog als eerst gedacht.

### Eerlijk: wat ik niet weet
- Of Chinese, Japanse of Koreaanse spelers een slechte AI-vertaling afstraffen in reviews. Dat hoor je vaak, maar ik heb er nu geen bron voor. GOK.
- Of 500 woorden klopt: dat getal kwam van de hoofdchat, niet uit het spel geteld. **Nagekomen (16 nov, Olaf telde): het is ±1700 woorden (±390 teksten).** Zie de bijgewerkte prijzen hierboven.
- Het voorstel van Abel noemt "pixel art"; Het Hol is inmiddels 3D uit Blender-code. Of beelden die Claude met code maakt "met hulp van AI" zijn, beslist niet ik: dat is de tekst die de hoofdchat met Thijs invult. Eerlijk lijkt me: noemen.

### Voorstel voor Dortus
**De hoofdchat besluit: demo van 18 dec met AI-vertaling (Claude) in Vereenvoudigd Chinees, Japans, Koreaans en Duits, en de AI-melding van spel én demo noemt "text and translations".** Waarom: de melding staat er toch al, dus het kost geen extra label en geen geld, en de grootste voorganger haalde 46% van zijn kopers uit Azië (zie Rusty hieronder). Tweede stap, vóór de lancering van het volle spel en alleen als de demo in Azië verlanglijstjes geeft (te zien in Steamworks per land): een mens kijkt de Chinese en Japanse tekst na, ±€320 tot €440 voor die twee bij 1700 woorden (eerst geschat op €100 tot €130 bij 500 woorden; geld, dus via de lijst van Thijs). Wie: Olaf zet de tabel klaar (al uitgezet), de hoofdchat beslist de talen en past de meldingstekst bij Abel aan. Niet doen: menselijke vertaling nu, terwijl de tekst tot 18 dec nog verandert.

---

## 1. Rusty's Retirement (Jordan Morris, solo, Mister Morris Games)

Onderzocht 15 nov 2026, run 1. De vader van het genre "spel onderaan je scherm", dus de directe voorganger van Hats of the Fallen.

### Bronnen
- GameDiscoverCo, "How Rusty's Retirement idle-farmed its way to 300k+ Steam sales!" (interview met de maker, eind aug 2024, met zijn echte Steam-cijfers): https://newsletter.gamediscover.co/p/how-rustys-retirement-idle-farmed
- Eigen aankondigingen van de maker op Steam (alle berichten van dec 2023 tot okt 2025 gelezen via de openbare nieuws-API): https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=2666510&count=60&maxlength=0&feeds=steam_community_announcements
- Steam appdetails 2666510 (prijs, talen, DLC, aanbevelingen), met curl opgehaald 15 nov 2026.
- Tweets van de maker (gezien als zoekresultaat, niet zelf geopend; datum berekend uit het tweetnummer): 100.000 verlanglijstjes op 25 mrt 2024, https://x.com/MrMorrisGames/status/1772305610580619385
- TikTok van de maker, 4 dec 2023 (datum uit het videonummer): https://www.tiktok.com/@mister.morris.games/video/7308754929005464865
- GamesRadar over de Next Fest-demo (6 feb 2024): https://www.gamesradar.com/my-early-steam-next-fest-highlight-is-like-an-idle-stardew-valley-but-i-promise-its-not-as-distracting-as-it-sounds
- GamesRadar over 100k en 200k verkocht (2 en 15 mei 2024), 80.lv (3 mei 2024, korting bij lancering).

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Prijs | $6,99 (GameDiscoverCo schrijft $7); bij lancering 10% korting | GEZIEN (appdetails) en DERDEN (80.lv) |
| Bouwtijd | 6 maanden, begonnen als prototype van 2 weken | DERDEN (maker op Steam, okt 2024; GameDiscoverCo) |
| Steampagina live | rond eind nov of begin dec 2023 ("a little under 4 months ago" op 25 mrt 2024; TikTok met "wishlist" op 4 dec 2023) | DERDEN, datum is een afleiding |
| Demo | 2 feb 2024, drie dagen voor Next Fest februari; na Next Fest nog een week online | DERDEN (aankondigingen Steam) |
| Verlanglijstjes | 100.000 op 25 mrt 2024; ±140.000 op de lanceerdag | DERDEN (tweet; GameDiscoverCo) |
| Lancering | vr 26 apr 2024, bewust op de vrijdag vóór het Farming Fest van Steam (29 apr) | DERDEN (maker in GameDiscoverCo) |
| Verkocht | 100.000 in 5 dagen, 200.000 in ruim 2 weken, bijna 330.000 eind aug 2024 | DERDEN (maker op Steam en X; GameDiscoverCo) |
| Opbrengst per stuk | ±$5 per verkocht exemplaar vóór de 30% van Steam (door terugbetalingen, kortingen en regionale prijzen); dus ±$3,50 naar de maker, ±50% van de winkelprijs | DERDEN (GameDiscoverCo), de $3,50 is mijn rekensom |
| Na 4 maanden | ±$1.800 per dag zonder actie, ±300 stuks per dag | DERDEN (maker in GameDiscoverCo) |
| Supporter Pack | $3,99 gouden pakje voor Rusty; 36.000 verkocht = **11% van de kopers**, $111.000 | DERDEN (GameDiscoverCo) |
| Landen | 26% China, 10% Japan, 6% Korea, 4% Taiwan (samen 46% Azië); 11 talen bij lancering | DERDEN (GameDiscoverCo); 11 talen GEZIEN (appdetails) |
| Aanbevelingen nu | 13.987 | GEZIEN (appdetails 15 nov 2026) |
| Vorig spel van de maker | Haiku, the Robot (apr 2022, $19,99), 2.600 aanbevelingen | GEZIEN (appdetails) |

### Wat hij deed, in volgorde
1. **Prototype van 2 weken** na zijn vorige spel. Hij twijfelde over weer een Metroidvania, maar koos dit idee omdat het "verkoopbaar" was (GameDiscoverCo).
2. **Eén haak die je in één beeld snapt:** een boerderij die onderaan je scherm leeft terwijl jij werkt. Twee handelingen: zaaien en dingen neerzetten die het werk overnemen. Voor de rustige speler en voor de min-maxer.
3. **Steampagina rond eind nov 2023, korte filmpjes vanaf het begin.** Zijn eigen woorden: "veel succes met posten op Twitter en Instagram Reels, die ik daarna ook op TikTok zette. Het idee bleef bij mensen hangen." Streamers pikten het op (Pirate Software wordt genoemd).
4. **Demo vlak voor Next Fest (2 feb 2024)**, met een feedbackformulier in het spel, een versiering-wedstrijd tijdens het fest (deel je boerderij op Twitter of Steam, winnaars krijgen een prijs) en een eigen livestream. Daarna schoof hij de lancering op van Q1 naar Q2 om de feedback te verwerken.
5. **100.000 verlanglijstjes in minder dan 4 maanden pagina.** Lanceerdatum gekozen op een Steam-themafestival (Farming Fest): hij lanceerde de vrijdag ervoor, kreeg een weekend vaart en daarna een tweede piek door het festival ("dubbele piek").
6. **Lancering met 11 talen, 10% korting en meteen een Supporter Pack.** Twitch-kijkers konden met een commando op de boerderij verschijnen en helpen (!plant).
7. **De eerste weken alleen bugs repareren**, bijna elke dag een build (zwart scherm, grote monitoren, Mac). Daarna een rustpauze en gratis updates (winter, samenwerkingen met Vampire Survivors en Balatro in 2025). Kortingen van 20 en 25% in de grote uitverkopen zetten de verlanglijstmails aan en gaven telkens een nieuwe piek.

### Drie lessen
1. **Een themafestival van Steam is de motor van de lancering, niet alleen Next Fest.** Hij koos zijn lanceerdatum rond het Farming Fest en zegt zelf dat dat de kans op succes vergrootte; de verkoop had twee pieken. Kortingen die verlanglijstmails aanzetten gaven daarna steeds nieuwe pieken.
2. **Bijna de helft van de kopers zat in Azië, en dat lukte door 11 talen bij de lancering.** GameDiscoverCo: "zo krijg je internationaal succes". Een strookspel heeft weinig tekst, dus vertalen is relatief goedkoop.
3. **Een Supporter Pack is echt geld: 11% van de kopers nam het.** Dat is veel meer dan wat wij uit reviews afleidden: in `platformen/steam/verdienmodel.md` staat voor ditzelfde pack 94 DLC-reviews op 6.625 = 1,4%. De echte koopkans is dus ongeveer 8 keer hoger dan de reviewverhouding (rekensom met DERDEN-cijfers). De aanname van Sanne (8 tot 18% koopt iets extra) klopt daarmee.

Extra, kleiner: verkeer van buiten Steam kwam vooral uit korte filmpjes en streamers, en hij maakte het streamers makkelijk (Twitch-commando's). Lastig voor meten: streams stonden meestal onder "Just Chatting" omdat het spel niet het hele scherm vulde.

### Eerlijk: wat niet zomaar voor ons geldt
- Hij was de eerste. In 2023 was "onderaan je scherm" nieuw; "We're spawning a genre" schreef hij zelf in mei 2024. Nu zijn er honderden Desktop Companion-apps (405 geteld door Olaf op 9 nov). Een nieuwe haak alleen is voor ons niet genoeg.
- Hij had al een spel met publiek (Haiku, the Robot, 2.600 aanbevelingen) en een eigen account op X. Wij beginnen bij nul volgers.
- Hoeveel verlanglijstjes de demo en Next Fest precies gaven, zegt geen bron. Het verloop staat in een grafiek bij GameDiscoverCo die ik niet kan lezen (alleen plaatje).
- Reviews x 30 tot 60 zou 420.000 tot 840.000 geven (GOK); de echte 330.000 na 4 maanden past daarbij.

### Voorstel voor Dortus deze week
**Olaf zet nu alle tekst van Hats of the Fallen in één vertaaltabel (geen tekst meer vast in de code) en de hoofdchat beslist of Vereenvoudigd Chinees, Japans, Koreaans en Duits in de demo van 18 dec komen.** Waarom: bij de grootste voorganger kwam 46% van de kopers uit Azië dankzij 11 talen (DERDEN). Nu één tabel maken kost weinig; achteraf alle tekst uit de code halen kost veel. Let op: de demolijst in `planning-fest-2027.md` is vast, dus talen erbij is een besluit van de hoofdchat, geen eigen keuze van Olaf. Vertalen met AI kan onder de AI-melding van Steam vallen (GOK, nog na te lezen in de regels van Steam); dat moet eerst uitgezocht.

Tweede punt voor Hans en Chris (geen actie deze week): kies de lanceerdatum van het volle spel rond een themafestival van Steam waar we in passen (Steam had in feb 2025 een "Idler Fest", zie de aankondiging van 4 feb 2025 in de nieuws-API van Rusty's), niet alleen rond Next Fest.
