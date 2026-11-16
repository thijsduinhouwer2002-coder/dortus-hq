# Festplan Hats of the Fallen (Sem, versie 1, 16 nov 2026)

Opdracht: `platformen/steam/fest-plan.md` punt 3 (eerste versie wo 25 nov). Dag voor dag van nu tot en met Next Fest februari, een doel per fase, en de **meetlat**: welke getallen na dag 2 van het Desktop Companion Fest "doorbraak" betekenen en wat we doen als het stil blijft.
Niets hieruit wordt geplaatst of verstuurd zonder ja van Thijs (via de hoofdchat en `organisatie/lijst-thijs.md`).

## Waar dit plan op staat (bronnen)
- Desktop Defender: ±200 verlanglijstjes na drie maanden pagina met persbericht, daarna in één Next Fest van 3 naar 1.548 spelers tegelijk in de demo, met spelersdoelen (100, 200, 400, 1.000) die elk extra levels gaven, en bij elk doel een Steam-aankondiging; drie weken later bijna 50.000 verlanglijstjes (Fenna verhaal 5, eigen aankondigingen GEZIEN, pers DERDEN).
- Vier kerkerspellen die het draaiboek volgden (demo, patches, livestream) bleven op 4 tot 7 reviews; mediaan van 16 kerkerspellen met demo: 8 reviews (Fenna verhaal 8, GEZIEN).
- Cozy Mining 2.000 verlanglijstjes op dag 2 van Next Fest, 5.000 aan het eind; Black Cat 2.000 na twee kleine fests (Fenna verhaal 7, eigen meldingen GEZIEN).
- Regels thema-fests (Steamworks-docs `doc/marketing/upcoming_events/themed_sales`, GEZIEN 16 nov met curl): uitnodiging op de tags; vakken voor demo's en "binnenkort"; binnen een vak sortering op "player interest and popularity"; demo's en niet-uitgebrachte spellen komen "in het algemeen" niet in de trailer van Valve; livestreamen op je eigen winkelpagina mag. Uitwerking en datums: `ontwerp/steam/winkelpagina/fest.md` (Sanne).
- Grote kanalen geven weergaven, geen kopers: Desktop Survivors 98 kreeg IGN, GameGrumps en Bijuu Mike en haalde 551 spelers tegelijk (Fenna verhaal 9, GEZIEN).
- Wat ons eigen is: de hoeden op Gloop en de helden met een wrok (`platformen/succes/onderscheid-hats.md`). Alles wat we in het fest laten zien, toont die twee.

## Het idee in drie zinnen
1. **Het fest is ons doorbraakmoment, de pagina en de makers zijn de aanloop.** Een pagina alleen geeft bijna niets (Desktop Defender: 200 in drie maanden); de groei komt uit de festweek. Wat vóór het fest gebeurt, dient één doel: op dag 1 hoog in het vak staan en meteen spelers hebben.
2. **Van de demo een evenement maken met doelen voor alle spelers samen**, zoals Desktop Defender. Bij ons zijn dat hoeden: "alle Glooppen samen" (Sanne optie A in `platformen/steam/samen-spelen.md`). Elk doel is een aankondiging, een clip en een reden om een vriend te halen.
3. **Na dag 2 kijken we en beslissen we**, met grenzen die nu al vastliggen. Een stil fest is een uitslag, geen pech.

## Fasen en doelen
| Fase | Wanneer | Doel (GOK, onderbouwing eronder) | Hoe meten |
|---|---|---|---|
| 0. Klaarzetten | nu tot ±8 dec | lijst van makers af (di 24 nov), teksten klaar, eerste 10 clips TikTok | eigen bestanden |
| 1. Pagina live | ±8 dec tot 3 jan | **500 verlanglijstjes** vóór de demo openbaar is | Steamworks (Thijs leest af), volgers via `memberslistxml` (GEZIEN werkt zonder inlog) |
| 2. Demo openbaar, rustig | ma 4 jan tot wo 13 jan | demo werkt bij echte spelers, 10+ demo-reviews, **1.000 verlanglijstjes** op de avond voor het fest | reviews op de demo-pagina, spelers tegelijk via de openbare API |
| 3. Desktop Companion Fest | do 14 jan 19:00 NL tot ma 18 jan 19:00 NL | meetlat hieronder | eigen meetscript elk uur |
| 4. Verbeterweek | ma 18 jan tot ma 1 feb | één verandering uit wat fest-spelers zeiden (planning-fest-2027.md) | |
| 5. Next Fest februari | ma 22 feb tot ma 1 mrt | doorbraak volgens de tweede meetlat | eigen meetscript |

**Waarom 500 en 1.000:** Black Cat stond na twee kleine fests op 2.000 en Desktop Defender na drie maanden pagina op 200 (verhaal 5 en 7). Wij hebben vier weken pagina plus makers plus TikTok; tussen die twee in is 500 tot 1.000 eerlijk. Het is een GOK; het belang is de sortering in het vak (Valve sorteert op belangstelling), niet het getal zelf.

**Waarom de demo op 4 jan openbaar en niet pas op dag 1 van het fest (besluit Sem, Olaf beslist over de build):**
- Valve sorteert binnen het demovak op belangstelling en populariteit (GEZIEN). Een demo die al tien dagen spelers en reviews heeft, staat op dag 1 hoger dan een demo met 0.
- Makers kunnen de openbare demo zelf downloaden: geen sleutels nodig, geen gedoe met sleutels voor een aparte demo-app. Wie een video wil maken heeft tien dagen.
- Fouten vinden we bij een paar honderd spelers in plaats van bij duizenden in het fest.
- Wat we opgeven: de "van 1 naar 1.548"-film van Desktop Defender. Maar die groei kwam uit de festweek zelf, niet uit het nieuw zijn van de demo; Valve eist ook geen nieuwe demo voor Next Fest ("We do not require exclusivity or newness", GEZIEN door Sanne).
- Voorwaarde: de demo is op 21 dec ingediend (planning) en voor 4 jan goedgekeurd. Lukt dat niet, dan op de dag van goedkeuring, uiterlijk 11 jan.
- **Antwoord Olaf (16 nov 13:32 UTC, `berichten/sem.md`): van de build uit kan 4 jan.** Demo af vr 18 dec, demo-einde na ±2 uur werkt, save wordt nooit gewist. Afspraken: build én demopagina zo vroeg mogelijk na 18 dec indienen (keuring in de feestdagen is trager, GOK Olaf), de knop "uitbrengen" op 4 jan door Thijs (lijst-thijs), en tussen 4 jan en het fest alleen fixes, niets nieuws, zodat makers hetzelfde spelen als festbezoekers. Demo-appid komt pas als Thijs de demo in Steamworks aanmaakt; dan zet Olaf hem in `planning-fest-2027.md` en bouw ik het meetscript om. Lukt de demo-app met hoeden-stat niet ±4 dec, dan schuiven de hoedendoelen naar Next Fest en tellen we in januari spelers tegelijk buiten het spel.

## Dag voor dag in de festweek
Tijden NL. Het fest begint do 14 jan 19:00 (10:00 PST, GEZIEN in fest.md). Elke dag hetzelfde ritme: één Steam-aankondiging (Chris schrijft, Thijs plaatst), één clip (TikTok, Shorts, Reels), meetscript elk uur, en alleen een patch als iets kapot is (nooit de save raken).

| Dag | Wat er gebeurt in de demo | Bericht op Steam en clip | Doel spelers tegelijk (piek die dag) |
|---|---|---|---|
| wo 13 jan | laatste controle build, geen wijzigingen meer | aankondiging "Tomorrow: the Desktop Companion Fest. The Gloops start eating." | |
| **do 14 jan (dag 1)** | het bordje "All Gloops: … hats" telt (optie A), eerste doel 10.000 hoeden | "We're in the Desktop Companion Fest. Every hat counts." Clip: Gloop zet een hoed op, teller loopt | 30 |
| **vr 15 jan (dag 2)** | doel 50.000: een nieuwe hoed komt voor iedereen vrij (zit al in de build) | per gehaald doel een aankondiging met de nieuwe hoed; clip van die hoed | 60 |
| **za 16 jan, 19:00 meetpunt** | **meetlat lezen** (zie onder), keuze doorbraak, gewoon of stil | | |
| za 16 jan (dag 3) | doel 250.000 | weekendbericht; bij doorbraak: "Thank you, X Gloops" met het getal | 80 |
| zo 17 jan (dag 4) | doel 1.000.000 (verrassing, zoals Desktop Defender bij 1.000) | | 100 |
| ma 18 jan (dag 5, eind 19:00) | demo blijft staan (Valve raadde Desktop Defender aan hem te laten staan, DERDEN) | "Thank you. The demo stays. Your hats come with you to the full game." | |

**Waarom deze doelen per dag:** Desktop Defender haalde 100 tegelijk binnen ongeveer een dag in Next Fest, met duizenden demo's (verhaal 5). Ons fest is kleiner (één thema), maar ons vak is voller met lijkende spellen. Ik zet de dagdoelen daarom onder de 100 van Desktop Defender en laat de meetlat beslissen. Nulmeting op een gewone maandag buiten een fest: zie "Nulmeting" onderaan.

**Doelen in hoeden (optie A) of in spelers (Desktop Defender)?** Hoeden. Een teller van spelers tegelijk kunnen we niet eerlijk in het spel tonen zonder server; een opgetelde Steam-stat wel (Sanne, GEZIEN in de docs). En hoeden zijn onze haak, spelers niet. Rekensom Sanne (GOK): 20 spelers gemiddeld in 5 dagen geeft ±65.000 hoeden, 200 gemiddeld ±650.000. Met doelen 10.000, 50.000, 250.000 en 1.000.000 haalt een klein fest er twee, een goed fest drie, een doorbraak alle vier. **Valt de keuze van Thijs op 21 nov niet op optie A**, dan blijven de doelen staan maar tellen we ze buiten het spel (spelers tegelijk via de openbare API, door ons gemeld in een aankondiging), zoals Desktop Defender.

**Livestream op de winkelpagina** (mag volgens Valve, GEZIEN): het spel zelf, 24 uur per dag, in de strook boven een rustig bureaublad. Past bij een spel dat je laat draaien, kost niets en toont aan elke bezoeker de hoeden. Uitzenden gaat via Steam en het account van Thijs; GOK of het iets oplevert, dus laag op de lijst. Klaarzetten op de lijst van Thijs pas als de pagina live is.

## Meetlat (na dag 2, za 16 jan 19:00 NL)
Twee getallen, allebei voor ons zelf te meten:
1. **Piek spelers tegelijk in de demo** in de eerste 48 uur. Wij meten dat zelf elk uur met de openbare API `ISteamUserStats/GetNumberOfCurrentPlayers` op het demo-appid (werkt zonder sleutel, GEZIEN 16 nov op Desktop Defender: 44 spelers om 12:37 UTC). Script: `data/demo-spelers.py` (ombouwen naar elk uur tijdens het fest). Daarmee zien we ook waar we staan tegenover de andere demo's in het fest.
2. **Nieuwe verlanglijstjes sinds het begin van het fest** (Steamworks, Thijs leest af of geeft het cijfer).

| Uitslag | Spelers tegelijk (piek, eerste 48 u) | Verlanglijstjes (eerste 48 u) | Wat we doen |
|---|---|---|---|
| **Doorbraak** | boven 100 | boven 1.000 | alles op versterken: elke dag een bericht met het getal, makers uit bak B (fest-overzichten) nu mailen met het getal erin ("X players have Gloop on their taskbar right now"), de demo blijft staan, Next Fest voorbereiden als tweede golf |
| **Gewoon** | 20 tot 100 | 300 tot 1.000 | het plan afmaken; in de verbeterweek één ding aan de haak (eerste hoed binnen 30 s, capsule), daarna Next Fest |
| **Stil** | onder 20 | onder 300 | zie "Als het stil blijft" |

Grenzen spelers tegelijk: voorstel Fenna (verhaal 9), GOK. Grenzen verlanglijstjes: ik heb de regel van Olaf (minder dan 1.000 in de hele festweek = haak aanpakken, `planning-fest-2027.md`) teruggerekend naar 48 uur: Cozy Mining haalde er op dag 2 al 2.000 en daarna nog 3.000, dus ongeveer 40% komt in de eerste twee dagen (GEZIEN uit hun twee meldingen, één spel, dus GOK als regel). De weekregel van Olaf blijft de eindtoets op ma 18 jan.
Als de twee getallen elkaar tegenspreken (veel spelers, weinig verlanglijstjes), telt de laagste: spelers die niet op de lijst zetten, kopen ook niet.

## Als het stil blijft (onder 20 spelers tegelijk of onder 300 verlanglijstjes na 48 uur)
Niet gewoon doorgaan. In deze volgorde, en elke stap met een getal dat we daarna opnieuw meten:
1. **Za 16 en zo 17 jan, nog in het fest:** kijken waarom. Wie de demo speelde: hoe lang (Steamworks, Thijs), wat er in de discussies en demo-reviews staat. Wie hem niet speelde: hoe vaak de pagina bekeken werd tegenover hoe vaak de demo gedownload werd (Steamworks, "UTM" en verkeer, Thijs). Weinig bezoek = de capsule doet het niet; veel bezoek en weinig downloads = de pagina en het eerste beeld doen het niet; veel downloads en kort spelen = de eerste minuten doen het niet.
2. **Verbeterweek (18 jan tot 1 feb) gaat naar dat ene ding**, niet naar poetsen: capsule (de hoedentoren groot, toets op 120 px, `onderscheid-hats.md` punt 2), of de eerste 30 seconden (eerste hoed binnen 30 s, eerste wrok binnen 5 minuten, punt 3), of de korte tekst (punt 1).
3. **Makers niet harder mailen.** Een stil fest wordt niet goed door meer mails over hetzelfde; eerst het ding repareren, dan met de nieuwe demo naar Next Fest.
4. **De hoofdchat legt de lanceerdatum van maart opnieuw neer** (staat al in de planning), en ik schrijf een korte uitslag met de getallen voor Thijs.

## Next Fest februari (22 feb tot 1 mrt)
Zelfde ritme, met de demo uit de verbeterweek. Tweede meetlat, hoger omdat Next Fest veel groter is: **doorbraak boven 300 spelers tegelijk na 48 uur** (Desktop Defender 1.548 op de piekdag, GOK dat een derde daarvan na 48 uur gangbaar is), gewoon 50 tot 300, stil onder 50. Hierna besluit de hoofdchat over de lancering. Uitwerken na de uitslag van januari.

## Wat ik nodig heb van anderen (afspraken via hun berichtenbestand)
- **Olaf:** demo openbaar op 4 jan (als de build het toelaat), het demo-appid zodra het bestaat (voor het meetscript), en of de vier beloningshoeden van optie A vóór 18 dec in de build kunnen.
- **Sanne:** keuze optie A na 21 nov; de doelen 10.000, 50.000, 250.000, 1.000.000 komen uit haar rekensom.
- **Chris:** zes korte Steam-aankondigingen en zes clips voor de festweek (lijst hierboven), klaar vóór 8 jan.
- **Thijs (lijst):** Discord-server vóór 4 jan, verlanglijstjes aflezen op vr 15 en za 16 jan, aankondigingen plaatsen. Staat op de lijst zodra de hoofdchat dit plan heeft gezien.

## Nulmeting: spelers tegelijk in demo's van aangekondigde bureaubladspellen, gewone maandag (GEZIEN 16 nov)
Meting ma 16 nov 12:38 tot 12:45 UTC, buiten elk fest dat over bureaubladspellen gaat. Alle 245 aangekondigde spellen uit Vera's kaart die een demo hebben (`platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv`), demo-appid via appdetails, spelers tegelijk via `GetNumberOfCurrentPlayers`. Script `data/demo-spelers.py`, uitkomst `data/demo-spelers-2026-11-16.csv`. Eén moment op één dag (Europese middag, Amerikaanse ochtend), dus een momentopname.
| | aantal demo's | deel |
|---|---|---|
| 0 spelers | 170 | 69% |
| 1 of meer | 75 | 31% |
| 5 of meer | 24 | 10% |
| 20 of meer | 10 | 4% |
| 100 of meer | 5 | 2% |
- Bovenaan: Character House (12.052, een uitschieter), Keyboard Farm 396, Desktop Dreampair 271, Widget Idle 122, Hamster Time 109.
- De 48 demo's die het meest op Hats lijken (Vera's score 2 of 3, kerker of gevecht): de beste heeft 19 (Idle Agency), dan 15, 12, 10; **36 van de 48 hebben 0 spelers**, ook Don't Rob My Dungeon.
- Ter vergelijking: Desktop Defender, uitgebracht en een jaar oud, had op hetzelfde moment 44.

**Wat dit zegt over de meetlat:** buiten een fest is 20 tegelijk al de top 4% en 100 de top 2%. De grenzen 20 en 100 zijn dus niet te laag. Ze zijn ook niet te hoog voor een fest: in Next Fest ging Desktop Defender van 3 naar 1.548. Wat ik nog niet weet is hoeveel een **thema-fest** optilt; dat meet ik bij het Auto-Battler RPG Fest dat nu loopt (zie Open). Als daar de mediaan van de demo's tijdens het fest onder de 20 blijft, zet ik de grens "gewoon" lager en meld ik dat hier.

## Open
- Hoe het Auto-Battler RPG Fest (16 tot 23 nov, begint 16 nov 18:00 UTC, GEZIEN in de Steamworks-lijst) uitpakt voor de demo's erin: dat is een thema-fest zoals het onze. **Nulmeting vóór de start gedaan** (GEZIEN 16 nov 12:47 tot 12:52 UTC): de eerste 200 van 773 aangekondigde spellen met de tag Auto Battler (Steam-zoeklijst), waarvan 112 met een demo: mediaan 0 spelers, 77 op 0, 8 op 20 of meer, geen enkele op 100 (hoogste 85, Here Comes the Horde). Uitkomst `data/autobattler-demos-voor-fest-2026-11-16.csv`. Volgende runs: dezelfde 112 demo's meten op dag 1 en dag 3 van dat fest (`data/demo-spelers-lijst.py` met de csv als cache). Dat zegt hoeveel een thema-fest optilt, en dan stel ik de grenzen hierboven bij. Kanttekening: niet al die 112 doen mee aan het fest; deelnemers zie ik pas op de festpagina.
- Of één spel zowel in het demovak als in het vak "binnenkort" komt (docs zeggen het niet).
- Of Valve een demo voor een thema-fest drie weken vooraf wil keuren (voor Next Fest wel; voor dit fest gaf de pagina een fout, ook bij Sanne).
