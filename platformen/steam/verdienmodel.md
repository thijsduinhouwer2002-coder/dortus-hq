# Verdienmodel voor Hats of the Fallen (Het Hol)

Sanne, 10 nov 2026 (run 23:45 UTC op 9 nov). Opdracht Thijs 10 nov 00:28 NL en hoofdchat 00:33: hoe doen de concurrenten het, en hoe verdient Het Hol wel. Thijs neigt naar gratis spel met hoogwaardige skins en DLC. Thijs beslist; Hans stemt af.

Alle cijfers zijn op 9 nov 2026 met curl opgehaald, tenzij anders vermeld. Labels: GEZIEN (zelf gemeten), DERDEN (bron met link), GOK.
- Prijzen en DLC-lijsten: `store.steampowered.com/api/appdetails?appids=<id>&cc=us` (GEZIEN).
- Reviews: het getal op de winkelpagina met `l=english` ("x% of the N user reviews"). Dat telt alleen Engelse reviews; het echte totaal is hoger (Bongo Cat heeft er volgens de hoofdchat 100K+ in alle talen).
- Klachten: 40 meest behulpzame negatieve en 40 positieve Engelse reviews per spel van de communitypagina (script `platformen/steam/data/reviews-haal.py`), geteld op trefwoorden (geld/DLC/prijs, drops/markt/bots). GEZIEN, ruwe telling: een review kan in twee bakjes vallen.

## 1. Wat de concurrenten doen

| Spel | Model | Basisprijs | Wat ze verkopen (prijs) | Hoe het erin zit | Engelse reviews (positief) | Klachten over geld (van 40 negatieve) |
|---|---|---|---|---|---|---|
| **Bongo Cat** (3419430) | gratis | $0 | willekeurige hoedjes-drops die op de Steam-markt verhandeld worden; sinds apr 2026 ook 5 DLC-packs ($5,05 tot $10,09) | Steam Inventory (drops en markt) en gewone DLC | 31.121 (96%) | 6 van 40 over geld en 9 over drops, markt of bots (deels dezelfde reviews): "FOMO inducing", "promotes completing your collection via Steam market", "money-grubbing" |
| **Desktop Mate** (3301060) | gratis | $0 | 45 personage-DLC's, bijna allemaal $14,99 (Miku, Hello Kitty, Vocaloids) | gewone DLC per personage | 5.381 (61%, laatste 30 dagen 75%) | **23 van 40** over dure DLC, vooral omdat mods (eigen personages) eruit gehaald zijn om DLC te verkopen: "$15 PER CHARACTER", "greedy cash grab" |
| **Rusty's Retirement** (2666510) | betaald | $6,99 | alleen een Supporter Pack ($3,99) | gewone DLC | 6.625 (97%) | 4 van 79 (eerdere telling, `data/reviews-2026-11-09/telling.txt`) |
| **Spirit City: Lofi Sessions** (2113850) | betaald | $11,99 | 4 plek-DLC's ($7,99), 1 cosmetisch pack ($4,99), Supporter Pack ($5,99) | gewone DLC | 9.230 (97%) | 12 van 40: "8 euro DLC's feel like the Sims DLC's", geen updates voor het basisspel maar wel cosmetische DLC |
| **Tiny Pasture** (3167550) | betaald | $5,99 | dier-DLC $2,99, twee gratis dier-DLC's, Supporter Pack $1,99 | gewone DLC | 1.209 (93%) | betaalde dier-DLC zelf maar 67% positief (103 reviews): te weinig voor het geld |
| **Ropuka's Idle Island** (3416070) | betaald | $3,99 | alleen soundtrack ($1,99) | soundtrack-app | 2.405 (95%) | 0 van 79 |
| **Deskrawl: Idle ARPG** (4623570) | betaald | $6,99 | Supporter Pack $1,99; buit is verhandelbaar op de Steam-markt | Steam Inventory (markt) en DLC | 473 (69%), **laatste 30 dagen 36% van 1.258** | **32 van 40** over drops en markt: "designed and balanced around item trade", "pay to win", "0 rare items in 250 hours" |

Bongo Cat in geld (DERDEN, Eurogamer-interview met Marcel Zurawka, samengevat op wnhub.io/news/stores-and-publishing/item-48117, nagelezen met curl): netto **$2.000 (maart), $4.050 (april), $3.800 (mei), $2.800 (juni 2025)**, nog niet winstgevend. 170 tot 180 duizend mensen per dag online, waarvan volgens de maker ongeveer de helft bots die drops verzamelen. Het was een proef met de markt en reclame voor hun spel Oku.

DLC-verkoop als maat (GOK, want DLC-reviews zijn geen verkopen): DLC-reviews gedeeld door reviews van het basisspel. Rusty's Supporter Pack 94 / 6.625 = 1,4%. Spirit City plek-DLC's 80 tot 287 / 9.230 = 0,9 tot 3,1%. Tiny Pasture dier-DLC 103 / 1.209 = 8,5%, Supporter Pack 43 / 1.209 = 3,6%. Desktop Mate Miku 428 / 5.381 = 8%. Een DLC-koper schrijft minder vaak een review dan een spelkoper, dus het echte aandeel kopers ligt hoger; ik reken met 8 tot 18% van de spelers die iets extra koopt (GOK).

## 2. Wat we hiervan leren
1. **Gratis met drops geeft bereik, geen geld.** Bongo Cat: top 5 meest gespeeld, toch $2.000 tot $4.050 per maand. De helft bots.
2. **Verhandelbare dingen maken het spel kapot.** Deskrawl zakte naar 36% positief omdat de buit om de markt heen gebouwd is. Bij Bongo Cat dezelfde klacht, kleiner. Spelers ruiken het meteen.
3. **Dure, dunne skins en iets afpakken geeft woede.** Desktop Mate: $14,99 per personage plus mods eruit = 61% positief. Niet de prijs alleen, maar het gevoel dat iets gratis werd afgepakt.
4. **Betaald met een Supporter Pack is veilig.** Rusty's, Tiny Pasture, Spirit City, Deskrawl: allemaal een Supporter Pack bij het uitbrengen, geen klachten erover (Rusty's 98% positief op het pack zelf). Dit werkt omdat iedereen weet dat het een fooi is.
5. **Inhoud-DLC mag, als het basisspel blijft groeien.** Spirit City verkoopt goed (tot 287 reviews per DLC), maar de klacht "Sims-DLC's" komt zodra het basisspel stilstaat. Gratis updates naast betaalde DLC is de prijs van vertrouwen.

## 3. Rekensom eerste jaar: gratis tegenover betaald

Aannames (GOK, eerlijk gezegd ruw): netto ±55% van de winkelprijs na de afdracht aan Valve (30%), btw en regionale prijzen. Spelers gratis = 5 keer zoveel als kopers betaald. Gratis: 2 tot 5% koopt iets, gemiddeld $5 tot $7. Betaald: $4,99, 8 tot 18% koopt daarnaast iets, gemiddeld $3,30.

| Schatting | Betaald $4,99: kopers | Netto basisspel | Netto DLC | **Totaal betaald** | Gratis: spelers | **Totaal gratis** |
|---|---|---|---|---|---|---|
| Laag | 2.000 | $5.500 | $500 | **±$6.000** | 10.000 | **±$550** |
| Midden | 10.000 | $27.400 | $4.000 | **±$31.400** | 50.000 | **±$5.000** |
| Hoog | 40.000 | $109.800 | $23.800 | **±$133.500** | 200.000 | **±$38.500** |

Gratis wint alleen als het bereik meer dan ±25 keer zo groot wordt als betaald. Dat lukte Bongo Cat, maar met drops en bots, en zelfs dan bleef het bij een paar duizend per maand.

## 4. Advies voor Het Hol

**Betaald, $4,99, met een permanente gratis demo en eerlijke skins als losse DLC.**

Waarom niet gratis:
- De rekensom: bij elke schatting levert betaald 5 tot 10 keer meer op.
- Van betaald naar gratis kan later altijd: de Steamworks-docs hebben er een eigen stuk voor ("Switching from paid to free", partner.steamgames.com/doc/store/freetoplay, GEZIEN). Andersom noemen de docs niet (GOK: kan niet of moeilijk). Betaald beginnen houdt dus beide wegen open.
- Het bereik van gratis halen we voor een groot deel met de **gratis demo** op het Desktop Companion Fest (zie `ontwerp/steam/winkelpagina/fest.md`): wie wil proberen, kan proberen.
- Zonder drops of markt (die willen we niet, zie les 1 en 2) mist gratis precies de motor die Bongo Cat groot maakte.

Wanneer Thijs toch gratis kiest (zijn keus): dan alleen zo, anders wordt het Desktop Mate of Deskrawl:
- skins direct te koop als DLC, nooit willekeurig, nooit verhandelbaar, geen Steam Inventory-markt;
- het gratis spel is helemaal compleet (heldenboek, wand en hoedenberg 100% te halen);
- skins $1,99 tot $3,99 en echt mooi (Mila's lat), geen $14,99;
- reken op het lage tot midden-getal uit de tabel.

Prijs: **$4,99** in plaats van de $5,99 uit `teksten.md`. Waarom: het is de mediaan van de betaalde Desktop Companion-apps (GEZIEN door Kees, `status.md`), we hebben nul reviews, en een lage drempel maakt de stap van demo naar kopen klein. Na een sterke start kan de prijs bij versie 1.1 naar $5,99 (met aankondiging). Eerste week 10% korting.

## 5. De eerste drie extra's
Alleen uiterlijk of nieuwe verhalen, nooit sneller of sterker. Wie niets koopt, krijgt alles in het spel vol.

| # | Wat | Soort | Prijs | Wanneer | Waarom |
|---|---|---|---|---|---|
| 1 | **Supporter Pack**: gouden Gloop, een eigen hoed voor Gloop die niemand anders heeft, 3 wallpapers in Mila's stijl | uiterlijk | $2,99 | bij het uitbrengen | les 4: iedereen in deze hoek doet het, niemand klaagt; geeft fans een manier om te betalen |
| 2 | **Frozen Hoard**: ijsgrot-thema (tegels, licht, schat in ijs, sneeuwmutsen op de helden, Gloop als ijsslijm) | skin | $2,99 | ±6 weken na uitbrengen | de grootste skin: hetzelfde spel, een heel ander hol; past bij de winter |
| 3 | **De Piratengilde**: 8 nieuwe helden met eigen trekken, 6 hoeden voor de hoedenberg, 40 nieuwe kroniekregels | inhoud | $3,99 | ±3 maanden na uitbrengen, samen met een gratis update voor het basisspel | meer verhalen en hoeden, niet sterker; de gratis update ernaast voorkomt de Sims-klacht (les 5) |

Bundel na DLC 3: alle drie voor $7,99. Seizoenshelden (kerst, Halloween) blijven gratis updates.

## 6. Wat Olaf moet bouwen en of het vóór 14 januari kan

**Gewone DLC, geen Steam-microtransacties en geen Steam Inventory.**
- DLC kan "alleen een licentie" zijn: de plaatjes zitten al in de gewone build en het spel kijkt of de speler de DLC heeft (`BIsSubscribedApp`, in GodotSteam `isDLCInstalled`). Geen eigen server nodig (DERDEN, partner.steamgames.com/doc/store/freetoplay en /doc/store/application/dlc, gelezen met curl).
- Microtransacties eisen een eigen veilige server (InitTxn, GetUserInfo, fraudecontrole) volgens dezelfde docs. Dat is weken werk en een server om te onderhouden, voor iets wat we niet nodig hebben.
- Steam Inventory brengt de markt en bots mee (les 1 en 2). Niet doen.

Haalbaar vóór 14 januari (GOK, met Olaf af te stemmen):
- Het Supporter Pack en de check `isDLCInstalled`: ±1 dag bouw zodra de Steamworks-app en de DLC-app bestaan (Thijs maakt ze aan). De kunst is van Mila.
- Voor het fest zelf is geen DLC nodig: we doen mee als binnenkort-spel met een demo (`fest.md`). Elke DLC krijgt een eigen winkelpagina en keuring (DERDEN, freetoplay-doc), dus we doen er bij het uitbrengen maar één.
- Valve raadt af om op dag 1 inhoud-DLC uit te brengen ("customers may perceive that the full game was ready to release but you chose to take away content", DERDEN, /doc/store/application/dlc). Een Supporter Pack is geen inhoud, dus dat mag; thema en gilde komen later.

## 7. Wat dit verandert
- `ontwerp/steam/winkelpagina/teksten.md`: prijsvoorstel $4,99 met verwijzing hierheen; de zin "No microtransactions" is weg (Daan punt 3) en vervangen door wat waar blijft.
- Stap voor Thijs (pas bij het uitbrengen, niet nu): in Steamworks de prijs invullen en de DLC-app voor het Supporter Pack aanmaken. Komt op `organisatie/lijst-thijs.md` zodra de winkelpagina klaar is.
- Zou het advies veranderen: als de demo op het fest meer dan ±25 keer zoveel spelers trekt als we kopers verwachten, of als Thijs bereik belangrijker vindt dan geld voor dit eerste spel. Dan gratis, op de manier van hoofdstuk 4.
