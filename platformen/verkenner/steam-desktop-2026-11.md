# Kaart van de Steam-markt voor Hats of the Fallen (bureaublad, taakbalk, desktop companion)

Vera, 16 nov 2026, run 04:31 (Amsterdam). Opdracht hoofdchat 16 nov 04:00 in `berichten/vera.md`.
Ruwe data: `data/steam-desktop-kaart-2026-11-16.csv` (1.714 apps, één regel per app), cijfers: `data/steam-desktop-analyse-2026-11-16.json`.
Nagekeken door een controleur (akkoord na 10 correcties, verwerkt).
Scripts: `data/steam-desktop-haal-script.py` (GitHub Actions, 6 delen, run 43801557679), `data/steam-desktop-aanvul-script.py`, `data/steam-desktop-analyse-script.py`.

## Eerst het belangrijkste
1. **Er is een spel in aanbouw dat bijna hetzelfde is als Hats.** *Don't Rob My Dungeon* (appid 5376930, Highlander Interactive, "Coming soon", demo sinds 17 okt 2026, 11 talen): "A tiny dungeon lives at the bottom of your screen while you work. Heroes walk in to steal your gold: set traps, raise monsters, smash them with the Dark Hand and grow infamous. Even your Twitch chat can try to rob you." (GEZIEN, winkeltekst en appdetails 16 nov). Het stond nog nergens in de repo. Dat raakt de belofte "in elk ander taakbalkspel ben je de held" uit `platformen/steam/idee.md`. Doorgegeven aan Fenna; Olaf en de hoofdchat moeten dit lezen.
2. **De hoek loopt vol.** Nieuwe apps per maand: 25 in jan 2026, 74 in aug, 120 in okt, en 128 in de eerste helft van november; 736 staan op "binnenkort", waarvan 34 met een datum in januari 2027 en 50 met "Q1 2027" (GEZIEN). Van de betaalde apps die in mei t/m aug 2026 uitkwamen (nu 2,5 tot 6 maanden oud) haalt de helft maar **4 reviews**, 38% haalt 10+ en 6% 100+. Een jaar eerder (jan t/m jun 2025) was dat mediaan 33,5 reviews, 72% 10+ en 42% 100+ (GEZIEN). Een deel van het verschil is leeftijd, want dit is één momentopname; dat de vloed de rest verklaart is een GOK, die de herhaalmeting rond 16 dec kan toetsen.
3. **Prijs:** onder $4 doet het duidelijk slechter; vanaf $4 gaat het beter, en $10+ scoort het hoogst maar is een kleine groep (28). Advies: **$6,99** (zie Advies).
4. **Maand:** begin maart 2027 is de beste haalbare keuze; nooit augustus of september (zie Advies).

## Hoe gemeten
- **Wat erin zit:** alle apps met het Steam-label Desktop Companion (988, ook programma's en "binnenkort"), plus apps uit zoektermen (taskbar, desktop pet, desktop companion, desktop idle, idle desktop, desktop buddy, desktop dungeon, desktop farm) waarvan de winkeltekst echt over de taakbalk, onderkant of rand van het scherm, een bureaubladhuisdier of "while you work" gaat. Van 2.536 kandidaten bleven 1.714 games en programma's over: 978 uit, 736 binnenkort. DLC, soundtracks en demo's tellen niet mee.
- **Per app (GEZIEN, 16 nov):** naam, maker, uitgever, prijs in dollars (zonder korting), releasedatum, labels, talen, demo ja/nee, aantal DLC (appdetails en winkelpagina). Reviews: het totaal over alle talen uit appdetails (`recommendations`), en de Engelse score (aantal en % positief) van de winkelpagina. Steam toont sinds kort per taal; de oude teller `appreviews` stuurt nu door naar de voorpagina, ook vanaf GitHub. Voor gratis apps geeft appdetails vaak geen totaal; dan staat er het Engelse aantal (Bongo Cat heeft er dus in werkelijkheid veel meer dan 31.301). Positief is daarom het Engelse percentage.
- **Desktop Companion Fest:** het eerste fest is 14 tot 18 jan 2027 (`platformen/steam/planning-fest-2027.md`). Niemand heeft er dus al op gestaan; de kolom zegt dat. Wel waren er eerder Idler Fest en Cozy-fests (zie Fenna, `platformen/succes/verhalen-spellen.md`).
- **Soort spel** is een ruwe indeling op trefwoorden in naam, korte tekst en labels (gevecht/kerker/RPG, boerderij, vissen, huisdier, programma, focus, overig idle). Er zitten fouten in (bijvoorbeeld "Fish to Dish" valt onder gevecht door het woord battle). Gebruik het als grove richting.
- Zes appnamen in de CSV bevatten een gedachtestreepje; dat zijn de letterlijke Steam-namen van andere makers, niet onze tekst.
- **Lijkt op Hats:** 0 tot 3 punten: kerker/held/monster/slijm, verzamelen of hoeden, grappig (comedy, funny).
- Reviews naar verkopen: ±30 verkopen per review, bandbreedte 20 tot 40 (DERDEN, zie `voorstellen/steam-bureaublad.md`).

## De cijfers
**Alle 978 uitgebrachte apps** (GEZIEN):

| | aantal | 0 tot 9 reviews | 10 tot 99 | 100+ | 1.000+ | 10.000+ (aantal) | mediaan reviews |
|---|---|---|---|---|---|---|---|
| alle | 978 | 50,6% | 32,2% | 17,2% (168) | 4,2% (41) | 4 | 9 |
| betaald | 812 | 54,2% | 30,3% | 15,5% (126) | 4,1% (33) | 3 | 6 |
| gratis | 164 | 32,3% | 42,1% | 25,6% (42) | 4,9% (8) | 1 | 28 |

Twee apps hebben geen prijs (niet te koop), daarom is 812 + 164 geen 978.

- **Mediane prijs van betaalde apps: $3,99** (GEZIEN). Kees mat in september $4,99 voor de nieuwe lichting; de goedkope vloed van de laatste maanden trekt de mediaan omlaag.
- **Scheefheid:** Wallpaper Engine alleen heeft 956.438 reviews, meer dan alle andere samen. Zonder Wallpaper Engine hebben de 10 grootsten 48% van alle reviews (GEZIEN). De 10.000+-groep: Wallpaper Engine, Bongo Cat (gratis), Spirit City: Lofi Sessions, Rusty's Retirement. Dat zijn uitzonderingen van 2018 tot 2025, niet wat een nieuw spel in 2027 mag verwachten.

**Per lichting, betaald** (GEZIEN; jongere lichtingen hebben minder tijd gehad):

| uitgekomen | aantal | mediaan reviews | 10+ | 100+ | 1.000+ (aantal) |
|---|---|---|---|---|---|
| jan t/m jun 2025 | 64 | 33,5 | 72% | 42% | 16 |
| jul t/m dec 2025 | 109 | 17 | 65% | 28% | 5 |
| jan t/m apr 2026 | 93 | 15 | 59% | 17% | 1 |
| mei t/m aug 2026 | 189 | 4 | 38% | 6% | 2 |

Nieuwe apps per maand (alle, GEZIEN): 2025 meestal 10 tot 35; 2026: jan 25, apr 35, jul 73, aug 74, sep 101, okt 120, nov (tot 16 nov) 128. Het aantal is in een jaar 4 tot 5 keer zo groot geworden, het aantal dat 100 reviews haalt niet.

**Wat verkoopt het best (betaald, minstens 2 maanden uit, 568 apps, GEZIEN):**

| soort | aantal | 100+ | 1.000+ | mediaan |
|---|---|---|---|---|
| boerderij of tuin | 81 | 28% | 10% | 19 |
| gevecht, kerker of RPG | 95 | 27% | 8% | 15 |
| vissen | 35 | 26% | 6% | 11 |
| programma of hulpmiddel | 111 | 22% | 5% | 9 |
| huisdier of maatje | 182 | 17% | 4% | 12,5 |
| idle of clicker zonder thema | 38 | 5% | 0% | 5 |

Weggelaten wegens te klein: overig (19 apps, 5% 100+) en focus en productiviteit (7 apps).

| prijs | aantal | 100+ | 1.000+ | mediaan |
|---|---|---|---|---|
| onder $2 | 128 | 10% | 3% | 6,5 |
| $2 tot $3,99 | 177 | 16% | 2% | 12 |
| $4 tot $5,99 | 145 | 26% | 7% | 19 |
| $6 tot $7,99 | 60 | 28% | 12% | 17,5 |
| $8 tot $9,99 | 30 | 23% | 3% | 16,5 |
| $10 en meer | 28 | 43% | 25% | 25 |

- **Talen:** 1 taal 8% 100+, 2 tot 5 talen 19%, 6 tot 10 22%, 11+ talen 29% (GEZIEN). Samenhang, geen bewijs dat vertalen het doet: grotere makers vertalen meer en maken ook betere spellen.
- **Demo:** met demo 21% 100+ (mediaan 15), zonder 20% (mediaan 11) (GEZIEN). Op zich weinig verschil; een demo is vooral het toegangskaartje voor fests.
- **Kalendermaand** (betaald, uit t/m sep 2026, GEZIEN): 100+ in februari 36%, november 39%, maart 29%, april 26%, januari 22%; augustus 10% en september 9%. Let op: augustus en september zijn vooral lichting 2026 (vloed en jong), dus dit is maar half een maandeffect. Kleine aantallen per maand (27 tot 90).
- **Lijkt op Hats** (2 of 3 punten): 160 apps, 26% haalt 100+ tegen 15% bij de rest (GEZIEN). Kerker en monsters met grappen halen dus vaker 100+ (samenhang; trefwoordtelling met fouten).

## De spellen die het meest op Hats lijken (uit, betaald tenzij anders, GEZIEN)
| spel (appid) | prijs | uit | reviews | positief (Engels) | waarom vergelijkbaar |
|---|---|---|---|---|---|
| Deskrawl: Idle ARPG (4623570) | $6,99 | 28 sep 2026 | 3.631 | 68% | kerker en buit op de taakbalk, grootste van 2026; Fenna verhaal 2 |
| Desktop Defender (3772810) | $4,99 | 4 nov 2025 | 1.788 | 92% | idle auto-battler "in the corner of your screen" die golven vijanden tegenhoudt, net als helden in je hol |
| Desktop Survivors 98 (3339780) | $4,99 | 20 mei 2025 | 1.352 | 94% | grappig, retro-Windows, monsters |
| Your Big, Cute Monster Farm (3659410) | $7,99 | 10 nov 2025 | 1.232 | 77% | monsters verzamelen en kweken |
| Tap Tap Loot (3959890) | $6,99 | 13 apr 2026 | 872 | 76% | buit en helden |
| Desktop Raid (3122460) | $8,99 | 8 mrt 2026 | 703 | 75% | kerkerraid, belooft "no grind" |
| Book of Fei (3733510) | $2,99 | 20 feb 2026 | 358 | 92% | klein en goed gemaakt |
| TBH: Task Bar Hero (3678970) | gratis | 27 mei 2026 | 8.860 | 62% | de grootste taakbalk-RPG, maar boos publiek |

**Binnenkort, dicht bij Hats (GEZIEN, winkeltekst):** Don't Rob My Dungeon (5376930, zie boven, demo uit), There is no HERO: Desktop Quest (5091650, grappige desktop-RPG, je verdedigt je dorp, 2027), Work From Dungeon (5478110, 19 nov 2026, 99 monsters verzamelen), Loafing Dungeon (4262590, 2027), Corner Dungeon (4846310, 2027, van Kygua Tech, makers van Fish to Dish met 2.676 reviews), Task Bar Dungeons (5320500, jul 2027, demo). Dungeon Architect: Idle (5368130) staat er niet in: geen label en geen taakbalk.

## Advies
**Prijs: $6,99, met 15% korting in de eerste week ($5,94)** (GOK met onderbouwing). Onder $4 doet het in deze hoek duidelijk slechter (10 tot 16% haalt 100+), vanaf $4 beter: $4 tot $5,99 26% (7% 1.000+), $6 tot $7,99 28% (12% 1.000+), $8 tot $9,99 23%, en $10 en meer 43% (25% 1.000+, maar maar 28 apps, vooral grote namen als Spirit City en Cast n Chill) (GEZIEN). De kerkerspellen die het meest op Hats lijken vragen $6,99 tot $8,99 (Deskrawl, Tap Tap Loot, Monster Farm, Desktop Raid). Het huidige plan is $4,99 (`platformen/steam/verdienmodel.md`), gekozen als lage drempel; dat valt nog in de goede band en is verdedigbaar. Waarom toch $6,99: de band $6 tot $7,99 haalt vaker 1.000+, Hats is in 3D (zeldzaam bij de toppers), en met de korting in de eerste week zit de instap nog onder $6. Eerlijk: duurdere spellen zijn vaak ook betere spellen; de prijs alleen doet het niet. Dit is een advies aan Olaf en de hoofdchat, geen besluit.

**Maand: begin maart 2027** (GOK met onderbouwing). Februari en maart scoren in de data goed (36% en 29% 100+), augustus en september slecht. Het Desktop Companion Fest (14 tot 18 jan) en Next Fest februari bouwen verlanglijsten op; uitbrengen kort daarna laat die verlanglijsten meteen een melding krijgen. Januari zelf wordt druk: 34 apps in deze hoek hebben nu een datum in januari 2027 en 50 "Q1 2027", waarschijnlijk rond het fest. Niet in de week van een grote Steam-uitverkoop (data staan in de Steamworks-kalender; niet zelf nagekeken voor maart 2027).

**Wat dit betekent voor Hats (eerlijk):**
- Wie nu uitkomt, belandt in een vloed: de helft van de nieuwe betaalde apps haalt minder dan 5 reviews. Bij 30 verkopen per review is dat ±150 verkopen, ±$400 netto bij $4,99 (GOK). Een spel moet dus duidelijk boven de massa uitsteken: plaatjes, een eigen idee, en een demo op het fest.
- Het eigen idee staat onder druk door Don't Rob My Dungeon. Wij moeten in één zin kunnen zeggen waarom Hats anders is (helden die terugkomen met een wrok en een hoed, de kroniek, 3D). Volgende stap: iemand speelt hun demo (Olaf of Fenna, alleen de openbare demo) en schrijft op wat zij wel en niet doen.
- Spellen met 11+ talen halen vaker 100+ (29%). Dat is samenhang, geen bewijs dat vertalen het doet, maar het past bij het vertaalplan van Fenna en Olaf.

## De 3 spellen om van te leren (doorgegeven aan Fenna)
Rusty's Retirement, Deskrawl en Desktop Heroes heeft Fenna al. Nieuw:
1. **Don't Rob My Dungeon (5376930):** bijna hetzelfde idee als Hats, nog niet uit, demo sinds 17 okt. Hoe groot is hun publiek (volgers, demo-reviews, Twitch-koppeling), wat doen ze anders, wanneer komen ze uit?
2. **Desktop Defender (3772810):** $4,99, 1.788 reviews, 92% positief: golven tegenhouden aan de taakbalk, het dichtst bij ons spelgevoel dat al bewezen verkoopt. Hoe kwamen ze aan hun publiek (uitgever Poysky en Level Up Gaming), wat prijzen spelers?
3. **Your Big, Cute Monster Farm (3659410):** $7,99, 1.232 reviews, 77%: monsters verzamelen voor een hogere prijs. Waarom 77%: welke klachten, en wat leert dat over verzamelen en de muur van de grind?

## Grenzen van deze meting
- Momentopname van 16 nov 2026; de nieuwste lichtingen groeien nog.
- Apps zonder label en zonder de zoektermen kunnen ontbreken. Het label is de kern (988 van 1.714).
- "Positief" is het Engelse percentage; voor gratis apps is het totaal vaak alleen Engels.
- Soort en "lijkt op Hats" zijn trefwoordtellingen, met fouten.
