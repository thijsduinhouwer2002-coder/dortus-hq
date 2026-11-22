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

## Aanvulling 16 nov, run 05:31: volgers (hoe groot is het publiek van de concurrenten?)
Vraag: is Don't Rob My Dungeon echt een gevaar, en hoeveel publiek hebben de spellen die rond het fest uitkomen? Gemeten met het aantal volgers: de leden van de officiële spelgroep op Steam, openbaar in `steamcommunity.com/games/<appid>/memberslistxml/?xml=1` (GEZIEN 16 nov, 04:40 tot 05:07 UTC). Ruwe data: `data/steam-volgers-2026-11-16.jsonl`, scripts `data/steam-volgers-script.py`, `data/steam-volgers-curl.sh`, analyse `data/steam-volgers-analyse-script.py`.

**Grens:** Steam geeft na ±45 verzoeken een tijdelijke blokkade (429). Die heb ik gerespecteerd: niet omzeild, gestopt. Daardoor zijn 88 van de 127 aangekondigde apps die het meest op Hats lijken (2 of 3 punten) gemeten, niet alle, en de willekeurige steekproef van de rest nog niet. Volgende run: de overige 39 en de steekproef, 1 verzoek per 6 tot 10 seconden.

**Uitkomst (GEZIEN):**
- **Don't Rob My Dungeon heeft 8 volgers.** De andere kerkerspellen die eraan komen ook weinig: There is no HERO 7, Work From Dungeon 4 (komt 19 nov uit), Loafing Dungeon 19, Corner Dungeon 59, Task Bar Dungeons 55. Buiten de kaart: Dungeon Architect: Idle 10, Grave Ambition 8, The Throne Below 6.
- **88 aangekondigde apps die op Hats lijken:** mediaan 10 volgers; 50% onder 10, 40% 10 tot 99, 10% 100 tot 999, geen enkele 1.000+. Met demo mediaan 22, zonder demo 7. De grootste: Bondoq: Desktop Gunners 460 (Q1 2027, demo), Fish Tankfully 255 (25 jan 2027), Traymon World: Taskbar Monster RPG 215 (25 nov 2026, demo, monsters verzamelen en ruilen), Birza 200, Occult Office 169, Dwarfspire 103 (9 dec 2026).
- **Uitgebrachte spellen die op Hats lijken, nu:** Deskrawl 8.897 volgers bij 3.631 reviews, Desktop Raid 4.673 bij 703, Desktop Survivors 98 4.020 bij 1.352, Desktop Defender 3.573 bij 1.788, Your Big, Cute Monster Farm 3.381 bij 1.232, Book of Fei 399 bij 358, TBH 45.688 bij 8.860 (gratis). Dat is meestal 2 tot 3 volgers per review. Tap Tap Loot (177.264 volgers bij 872 reviews) is een uitschieter die ik niet kan verklaren; niet meegeteld.

**Wat volgers betekenen (DERDEN):** GameDiscoverCo (Simon Carless, juni 2023, via Game World Observer) meet dat verlanglijsten bij nog niet uitgebrachte spellen 7 tot 20 keer de volgers zijn, gemiddeld ±12, bij ontspannen spellen hoger (±15). En de verkoop in de eerste week is mediaan 0,2 keer de verlanglijsten bij de lancering (GameDiscoverCo, peiling 2024). Grof: elke volger is bij de lancering ±2 tot 3 verkopen in de eerste week (GOK op basis van die twee medianen, met grote spreiding).

**Wat dit betekent voor Hats (GOK met onderbouwing):**
1. **Don't Rob My Dungeon is een idee-gevaar, geen publieks-gevaar.** Met 8 volgers heeft het ±100 verlanglijsten (bandbreedte ±55 tot 160). De belofte blijft dus te winnen; het gaat erom wie het als eerste goed laat zien. Het advies uit de kaart blijft: één zin waarom Hats anders is.
2. **De lat rond het fest is laag.** De helft van de concurrenten die eraan komen heeft minder dan 10 volgers. Wie op het fest (14 tot 18 jan) **100+ volgers** heeft, hoort bij de beste 10% van de aangekondigde spellen in deze hoek; 300+ zou Hats bovenaan zetten (alleen Bondoq zit nu hoger). Dat zijn ±1.200 tot 3.600 verlanglijsten.
3. **Meten wordt makkelijk:** zodra de winkelpagina van Hats op 1 dec live staat, kan elke run met één verzoek de volgers van Hats naast deze lijst zetten. Voorstel: vanaf 1 dec wekelijks Hats, Don't Rob My Dungeon, Traymon World, Bondoq en Fish Tankfully meten.
4. **Twee proeven vóór ons fest om te volgen:** Work From Dungeon (19 nov, 4 volgers, 99 monsters verzamelen) en Traymon World (25 nov, 215 volgers, demo). Hun reviews na 1 en 4 weken laten zien wat een klein of middelgroot publiek bij de lancering in deze hoek oplevert. Staat in `taken.md`.

## Aanvulling 2, 16 nov run 06:31: volgers afgemaakt plus steekproef
Gemeten 06:38 tot 07:14 (Amsterdam), zelfde openbare XML, 1 verzoek per 10 seconden, bij een 429 vijf minuten gewacht (twee keer gebeurd), niets omzeild. 151 apps erbij, samen nu 255 metingen in `data/steam-volgers-2026-11-16.jsonl`. Het oude Python-script (`steam-volgers-script.py`) kreeg vanaf hier geen antwoord; de curl-versie werkte wel.

**Wat er nu gemeten is (GEZIEN):**
- **Alle 127 aangekondigde apps die op Hats lijken (2 of 3 punten):** mediaan 9 volgers; 50% onder 10, 40% 10 tot 99, 9% 100 tot 999, geen enkele 1.000+. Het beeld van run 05:31 (88 apps, mediaan 10) blijft staan.
- **Willekeurige steekproef van de andere aangekondigde apps (69 van 608, zaad 16):** mediaan 7, 55% onder 10, 12% 100 tot 999, 1% 1.000+. Lijken op Hats maakt dus weinig uit: de hele hoek heeft weinig volgers vóór de lancering.
- **Demo:** aangekondigd met demo mediaan 22 volgers (n=69), zonder 6 (n=127). Een demo hoort bij ongeveer drie keer zoveel volgers; dat is samenhang, geen bewezen oorzaak.
- **Grootste aangekondigde apps in de hele hoek:** Meowniverse 1.435 (demo, Superjoy), Smug Ally 558, Pet.Net 530, Bondoq 460, Tiny Harbor 272, Your Momo 271, Fish Tankfully 255, Traymon World 215.
- **Uitgebracht in 2026, betaald, nu gemeten (n=48, waarvan 38 uit de willekeurige steekproef van 561):** wie nu 10 tot 99 volgers heeft, heeft mediaan 2 reviews (n=22); 100 tot 999 volgers mediaan 34,5 reviews (n=12, 6 tot 358); 1.000+ volgers mediaan 872 (n=5). Bij spellen met 5+ reviews zijn het mediaan **4 volgers per review** (n=24, middelste helft 2,6 tot 9,5).

**Wat dit verandert (GOK met onderbouwing):**
1. In run 05:31 schreef ik 2 tot 3 volgers per review; dat kwam van de grote spellen. Voor kleine spellen zijn het eerder **3 tot 6 volgers per review** (mediaan 4 bij 5+ reviews, 3,3 bij 10+ reviews over alle jaren (n=22), en 0,17 reviews per volger bij spellen met 20+ volgers, dus ±6). Let op: dit zijn volgers ná de lancering, die groeien door; het is geen voorspelling vanaf de volgers op het fest.
2. Ruwe vertaling voor Hats: 300 volgers ruim na de lancering past bij ±50 tot 75 reviews, dus ±1.500 tot 2.250 verkopen tegen ±30 verkopen per review (bandbreedte groot). Om bij de 100+ reviews van de kaart te horen heeft Hats na de lancering ±400 tot 600 volgers nodig.
3. De doelen uit run 05:31 blijven: op het fest 100+ volgers is top 10% van wat eraan komt, 300+ is bovenaan. En een demo vóór het fest is het duidelijkste verschil dat ik in de data zie.

**Niet gemeten:** 22 van de 150 geplande aangekondigde apps en 62 van de 100 geplande uitgebrachte apps uit de steekproef (tijd). Kan met `data/steam-volgers-curl.sh`, met een pauze bij 429.

## Aanvulling 3, 16 nov run 07:31: controleur over beide volgersblokken, steekproef afgemaakt
Een aparte controleur heeft de twee blokken hierboven nagerekend tegen de data: **akkoord met correcties**. Daarna heb ik de steekproef afgemaakt: 84 apps erbij (06:35 tot 07:00 UTC, 1 verzoek per 10 seconden, één 429 waarbij ik 5 minuten wachtte, niets omzeild), samen 339 regels voor 332 apps op de kaart. Nieuwe analyse zonder de met de hand gekozen spellen: `data/steam-volgers-analyse3-script.py` (het oude script filterde ten onrechte niet op jaar; dat staat er nu bij).

**Correcties op de blokken hierboven:**
- Run 05:31, grootste aangekondigde lookalikes: na Birza 200 komen Boing Boing Animals 176, Occult Office 169 en MonsterGirl 3:Wukong 152. Dwarfspire (103) hoort er niet bij.
- Aanvulling 2: "255 metingen" waren 251 apps (3 dubbel, 1 regel met een 429). De steekproef was 68 willekeurig uit 609 plus Corner Dungeon (met de hand), niet 69 uit 608. Uitgebracht in 2026 waren 44 apps in run 06:31 gemeten, niet 38. In de lijst grootste aangekondigde ontbrak Travelling Home: Ever After (222, demo).
- "2 tot 3 volgers per review" (run 05:31) gold voor zeven grote, met de hand gekozen spellen (spreiding 1,1 tot 6,6), deels uit 2025. "3 tot 6" (Aanvulling 2) paste niet bij de sommen, die met 4 tot 6 rekenden. Beide vervangen door het getal hieronder.
- "300+ zet Hats bovenaan" geldt alleen voor de 127 spellen die op Hats lijken, niet voor de hele hoek (zie hieronder).

**Nieuwe cijfers, alleen willekeurig gekozen apps (GEZIEN):**
- **Uitgebracht in 2026, betaald (106 van 565):** mediaan 19,5 volgers; 25% onder 10, 51% 10 tot 99, 19% 100 tot 999, 5% 1.000+. Wie 10 tot 99 volgers heeft, heeft mediaan 3 reviews (n=54); 100 tot 999 volgers mediaan 29 reviews (n=20, 6 tot 174).
- **Volgers per review:** mediaan **5** bij 5+ reviews (n=46, middelste helft 2,6 tot 9,5), 5,1 bij 10+ (n=36), 5,3 bij 20+ (n=25). Andersom, bij 20+ volgers: mediaan 0,13 reviews per volger (n=53), dus ±8 volgers per review. De spreiding is groot.
- **Aangekondigd, lijkt niet op Hats (90 van 609):** mediaan 7 volgers, 59% onder 10, 9% 100 tot 999, 3% 1.000+. Er zitten 5 van de 90 boven de 300; omgerekend ±30 tot 35 aangekondigde apps in de hele hoek. De grootste zijn bureaubladhuisdieren: Character House -Desktop Companion- 9.732 en Amarillo's Desktop Pets 5.822 (beide met demo), daarna Meowniverse 1.435.
- **Demo:** lookalikes met demo mediaan 22 tegen 7 zonder (48 tegen 79); bij de rest 15 tegen 6 (27 tegen 63). Twee tot drie keer zoveel. Samenhang, geen bewezen oorzaak: grotere makers met een uitgever doen vaker een demo.

**Wat dit verandert voor Hats (GOK met onderbouwing):**
1. Reken met **±5 volgers per review** ruim na de lancering, maar met een brede band (±3 tot 10). 300 volgers past dan bij ±60 reviews, eerlijk gezegd ergens tussen 30 en 110. Om bij de 100+ reviews van de kaart te horen heeft Hats na de lancering ±500 volgers nodig (300 tot 1.000). Met ±30 verkopen per review is 60 reviews ±1.800 verkopen; ook die factor is onzeker, dus lees dit als orde van grootte.
2. De lat op het fest: binnen de spellen die op Hats lijken is 100+ volgers top 10% en 300+ bovenaan (alleen Bondoq 460 zit hoger). In de hele bureaubladhoek staan er ±30 aangekondigde apps boven de 300, vooral huisdieren en companions; die spelen in een andere hoek van het fest, maar trekken wel dezelfde bezoekers.
3. Het advies blijft: een demo vóór het fest, en de winkelpagina vanaf 1 dec wekelijks meten naast Don't Rob My Dungeon, Traymon World, Bondoq en Fish Tankfully.

## Aanvulling 4, 16 nov run 08:31: de kalender van Steam voor 2027 (maandadvies precies gemaakt)
In het advies stond "niet in de week van een grote uitverkoop, niet zelf nagekeken voor maart 2027". Nu wel: de Steamworks-pagina Upcoming Steam Events (`partner.steamgames.com/doc/marketing/upcoming_events`, GEZIEN 16 nov 07:45 UTC) noemt:

| wanneer (2027) | wat | wat het voor Hats betekent |
|---|---|---|
| 14 tot 18 jan | Desktop Companion Fest | wij doen mee als "binnenkort" met demo (staat al in `platformen/steam/planning-fest-2027.md`) |
| 25 jan tot 1 feb | Shop Keeper Fest | niet onze hoek |
| **22 feb tot 1 mrt** | **Next Fest februari** | alleen voor spellen die nog niet uit zijn, met speelbare demo; aanmelden uiterlijk 10 jan (planning) |
| 8 tot 15 mrt | Rhythm Fest | niet onze hoek, kleine drukte |
| **18 tot 25 mrt** | **Spring Sale** (seizoensuitverkoop) | meedoen kan alleen als het spel 30 dagen vóór de start uit is, dus uiterlijk 16 feb; dat botst met Next Fest, dus Hats doet niet mee |
| 14 tot 21 jun | Next Fest juni | reserve als we februari missen |
| 24 jun tot 8 jul | Summer Sale | |

Ook gezien: Winter Sale 17 dec 2026 tot 4 jan 2027, en Black Friday 26 tot 30 nov 2026 als thema op de kortingspagina (geen eigen fest).

**Advies, nu met data (GOK met onderbouwing):**
- **Uitbrengen in de week van di 2 tot do 4 maart 2027**, direct na Next Fest. Wie op het fest de demo speelde en het spel op de verlanglijst zette, krijgt dan meteen de melding "nu te koop", terwijl het spel nog vers in het geheugen zit.
- De **korting van de eerste week** (15%) loopt dan af rond 9 tot 11 maart, ruim vóór de Spring Sale van 18 maart. Dan staat ons spel niet met een kleine korting tussen duizenden spellen met grote kortingen.
- **Niet uitbrengen van 11 tot 25 maart**: de week vóór en tijdens de Spring Sale gaat de aandacht van kopers naar kortingen, en wij mogen niet meedoen.
- **Schuift het?** Dan eerst ma 29 mrt tot half april (na de Spring Sale, februari en maart scoorden in de kaart het best, april nog redelijk met 26% 100+). Schuift het verder, dan Next Fest juni met uitbrengen na de Summer Sale, maar juli en augustus scoorden slecht (augustus 10% 100+), dus dat is de zwakste keuze.
- **Regels voor de lanceerkorting** (Steamworks-pagina Discounting, `partner.steamgames.com/doc/marketing/discounts`, GEZIEN 16 nov 07:40 UTC): de lanceerkorting begint bij het uitbrengen, loopt 7 tot 14 dagen, minimaal 10% en maximaal 40%; Valve raadt zelf ±10 tot 15% aan. Je stelt hem in naast de releasedatum op de app-pagina, niet in het gewone kortingenscherm. Daarna geldt een wachttijd: 30 dagen na het uitbrengen mag er geen andere korting, en een spel in die wachttijd mag niet meedoen aan een seizoensuitverkoop. Een korting van 20% of meer kan een melding sturen aan wie het spel op de verlanglijst heeft. Gevolg voor Hats: 15% gedurende 7 dagen past precies binnen de regels en loopt bij uitbrengen op 2 tot 4 maart af vóór 18 maart; de eerste gewone korting kan pas begin april. Of we 20% nemen om die extra verlanglijstmelding te krijgen, is een keuze voor Olaf en de hoofdchat; de melding "nu te koop" bij het uitbrengen gaat waarschijnlijk hoe dan ook naar de verlanglijsten (GOK uit algemene kennis, niet nagekeken; staat op de Steamworks-pagina Wishlists).

Doorgegeven aan Fenna (berichten/fenna.md), zodat de lanceerdatum in de planning komt.

## Aanvulling 5, 16 nov run 08:31: nulmeting voor een proef "wat doet een fest met volgers?"
Vraag voor Hats: hoeveel volgers levert een thema-fest van Steam op? Dat bepaalt wat we van het Desktop Companion Fest (14 tot 18 jan) mogen verwachten. Er loopt nu een fest dat op onze hoek lijkt: het **Auto-Battler RPG Fest, 16 nov 18:00 UTC tot 23 nov 2026** (Steamworks, GEZIEN). Desktop Defender en een deel van de kerkerspellen op de kaart hebben het label Auto Battler.

**Nulmeting, vóór de start (GEZIEN 16 nov, 04:40 tot 08:15 UTC, openbare volgers-XML, 1 verzoek per 10 s, bij 429 vijf minuten gewacht, niets omzeild):** van de 144 bureaubladapps met het label Auto Battler zijn er nu 144 gemeten (48 al eerder vandaag, de rest deze run), plus 284 apps zonder dat label als controle. Ruwe data: `data/steam-volgers-autobattler-2026-11-16.jsonl` naast `data/steam-volgers-2026-11-16.jsonl`.

| groep (16 nov, vóór het fest) | aantal | mediaan volgers |
|---|---|---|
| Auto Battler, binnenkort | 82 | 9 |
| Auto Battler, uit | 62 | 73,5 |
| controle, binnenkort | 177 | 8 |
| controle, uit | 107 | 20 |

**Plan:** op 24 nov (dag na het fest) en op 1 dec dezelfde apps opnieuw meten en de groei van de Auto Battler-groep vergelijken met de controle, met `data/steam-fest-effect-script.py`. Wie echt meedeed is nu nog niet te zien (de festpagina is pas na de start gevuld); op 17 nov of later de deelnemers van de festpagina halen als dat lukt, anders blijft het label de grove maat. Eerlijk: niet elke app met het label doet mee, en de controlegroep doet soms aan andere acties mee; dit wordt een grove orde van grootte, geen bewijs.

**Vervolg 17 nov, run 05:31 NL: de festlijst is binnen (GEZIEN, 04:40 UTC).** De oude link (`/sale/autobattlerrpgfest`) stuurt door naar de voorpagina; het fest staat op `store.steampowered.com/category/auto_battler_rpg/`. In die pagina staan het clan-nummer en de event-GID; daarmee geeft de openbare lijst-API van Steam (`saleaction/ajaxgetsaledynamicappquery`) **1.506 spellen** op de festpagina, waarvan ik er 1.502 kreeg (drie sorteringen samen, één sortering mist er ±300 omdat de volgorde schuift). Daarvan 648 binnenkort en 249 met korting. De festinstellingen in de pagina zeggen `optin_only: true`, dus GOK (sterk): dit zijn de echte deelnemers. Lijst: `data/steam-autobattlerfest-lijst-2026-11-17.json` (alleen appids), opnieuw te halen met `data/steam-fest-lijst-script.py`.

| groep in de nulmeting | aantal | mediaan volgers 16 nov |
|---|---|---|
| in festlijst, binnenkort | 57 | 10 |
| in festlijst, uit | 43 | 94 |
| label Auto Battler, niet in lijst, binnenkort | 26 | 7,5 |
| label Auto Battler, niet in lijst, uit | 21 | 56 |
| controle, binnenkort | 176 | 8 |
| controle, uit | 105 | 20 |

- Van de 144 apps met het label staan er 97 op de festlijst (56 binnenkort, 41 uit; 18 van die 41 hebben korting). 47 met het label doen dus niet mee. Van de controle staan er 6 op de lijst; die tellen nu als deelnemer. Van die 103 hebben er 100 een geldige volgersmeting (de tabel). Nagekeken door een controleur: akkoord, alle getallen gelijk.
- De groep die meedoet had al vóór het fest meer volgers (binnenkort 10 tegen 8), dus op 24 nov kijk ik naar de **groei**, niet naar het aantal.
- `data/steam-fest-effect-script.py` neemt nu als tweede argument de festlijst en groepeert dan op "in festlijst" in plaats van op het label. Nameting 24 nov: `python3 -I steam-fest-effect-script.py nameting.jsonl steam-autobattlerfest-lijst-2026-11-17.json`. De groep "label, niet in lijst" is een tweede controle: zelfde soort spel, geen fest.
- Bruikbaar voor Hats in januari: dezelfde route werkt voor elk fest met een `category`-pagina (clan 41316928 is de vaste groep `store_contenthubs` van Steam); alleen de event-GID uit `data-event` verschilt.

## Aanvulling 6, 16 nov run 09:31: welke talen? Reviews per taal bij de grote bureaubladspellen

**Vraag:** de hoofdchat kiest later de eerste vertaaltalen voor Hats (Olaf maakt de vertaaltabel na de speeltest van 20 nov). Waar komen de reviews van de bureaubladspellen vandaan?

**Hoe gemeten (GEZIEN, 16 nov):** de winkelpagina van Steam met `?l=<taal>` geeft in `itemprop="reviewCount"` het aantal reviews in die taal, maar alleen als Steam voor dat spel een eigen score per taal toont ("When there are enough reviews written in a particular language", Valve, 2025, volgens PC Gamer en heise). Anders valt de pagina terug op alle talen; dat herken ik aan de zin "for this game" (per taal vertaald) of aan een getal gelijk aan het totaal. De gewone review-API (`appreviews`) stuurt vanaf hier door naar de voorpagina, ook met andere opties geprobeerd. 8 talen per spel, 1 verzoek per ±2,5 s, 274 pagina's, 0 fouten, geen 429. Script `data/steam-talen-script.py`, analyse `data/steam-talen-analyse-script.py`, ruwe data `data/steam-talen-2026-11-16.jsonl`.

**Grens, eerlijk:** gepland waren alle 101 betaalde bureaubladspellen met 100+ reviews; 32 zijn gemeten (eerst de spellen die het meest op Hats lijken, daarna de grootste), de tijd van de run was op. En Steam toont een eigen taalscore pas vanaf ±200 reviews in die taal (laagste die ik zag: 205), en niet bij elk spel (Burgie's Cozy Kitchen, 1.662 reviews, heeft er geen). Bij 19 van de 32, allemaal onder 2.100 reviews, toont Steam geen enkele taal apart. Dus: dit zegt iets over de **13 grootste**, niet over kleine spellen, en "niet getoond" betekent "onder de drempel", niet nul.

**Uitkomst bij de 13 spellen met taalscores (samen 83.508 reviews, GEZIEN):**
- **Vereenvoudigd Chinees is bijna zo groot als Engels.** Mediaan per spel: Engels 30%, Vereenvoudigd Chinees 26% (samen met Traditioneel 29%). Chinees is 10%+ bij 10 van de 13, Engels bij 12 van de 13. Bij 6 van de 13 is Chinees de grootste taal (To Be or Not to Be 97%, Tiny Pasture 64%, Deskrawl 57%, Maltese's Fluffy Onsen 51%, Fish to Dish 45%, Crusaders Quest 39%).
- **Rusty's Retirement:** Engels 47%, Chinees 26% + 4%, Koreaans 6%, Japans 3%, Braziliaans 3%, Duits 2%. Past bij de 46% uit Azië in `platformen/succes/verhalen-spellen.md`.
- **Daarna een lange staart:** Koreaans 10%+ bij 2 spellen (Crusaders Quest 27%, Maltese 13%), Russisch bij 1 (Your Mother 40%, een Russische maker), Braziliaans bij 1 (How to Train Your Cock 57%). Duits en Japans kwamen nergens boven 5%.
- **Chinese kopers zijn strenger, maar weinig:** bij de meeste is de score in het Chinees gelijk of één tiende lager dan in het Engels (Cast n Chill 10 tegen 9, Tiny Aquarium 10 tegen 9).
- Alle 13 hebben Vereenvoudigd Chinees in het spel. Of het vertalen de Chinese kopers bracht of andersom, zegt deze meting niet (samenhang).

**Wat het betekent voor Hats (advies):** als de hoofdchat één extra taal kiest naast Engels, dan Vereenvoudigd Chinees; dat is in deze hoek met afstand de tweede markt. Daarna pas Traditioneel Chinees, Koreaans en Braziliaans-Portugees; Duits, Frans en Japans laten deze cijfers niet zien als prioriteit. Let op: de grappen en namen in Hats (wrok, bijnamen) moeten in het Chinees echt goed zijn, anders zakt juist daar de score. Hoe we vertalen (met AI en de AI-melding van Steam) zoekt Fenna uit.

**Volgende stap (open):** de overige 69 spellen meten met hetzelfde script (het gaat verder waar het stopte); voor kleine spellen onder de drempel werkt deze methode niet. Daarvoor zou de nieuwste reviewlijst per taal op steamcommunity.com kunnen (datum van de 10e review per taal geeft een tempo), maar die site geeft na ±45 verzoeken een 429, dus dat is werk voor meerdere runs.

## Aanvulling 7, 16 nov run 10:31: talen afgemaakt (alle 101 gemeten)

**Wat er bij kwam (GEZIEN, 16 nov):** de overige 69 betaalde bureaubladspellen met 100+ reviews gemeten met hetzelfde script (`data/steam-talen-script.py`), 546 pagina's erbij, 0 fouten, geen 429. Ruwe data aangevuld in `data/steam-talen-2026-11-16.jsonl` (nu 820 regels, 101 spellen). Steekproef met de hand nagekeken: Mini Cozy Room Koreaans 1.023, Cornerpond Chinees 211, beide opnieuw opgehaald en gelijk.

**Grens blijft:** Steam toont een eigen taalscore pas vanaf ±200 reviews in die taal. Van de 101 spellen hebben er nu **17** minstens één eigen taalscore (samen 94.925 reviews); de andere 84, allemaal onder ±2.000 reviews, tonen geen enkele taal apart. Erbij gekomen: Mini Cozy Room: Lo-Fi, The NOexistenceN of Lilith, Ithya: Magic Studies, en Cornerpond is nu compleet (stond in run 09:31 half).

**Uitkomst bij de 17 (mediaan per spel, niet getoond telt als 0):**
- Engels 30%, 10%+ bij 16 van de 17.
- Vereenvoudigd Chinees 24% (met Traditioneel 29%), 10%+ bij 13 van de 17, en bij 8 van de 17 groter dan Engels.
- Koreaans 10%+ bij 3 (nieuw: Mini Cozy Room 28%, meer dan Engels 21%), Russisch bij 2 (nieuw: Lilith 13%), Braziliaans bij 1. Japans en Duits bij geen enkel spel boven 5%.
- Het beeld van run 09:31 blijft dus staan: Chinees is de tweede markt, Koreaans een duidelijke derde.

**Nieuw, over oorzaak en gevolg (GEZIEN, kaart van 1.714 apps, betaalde spellen):** Vereenvoudigd Chinees in het spel hebben 63% van de spellen met 0 tot 9 reviews, 75% bij 10 tot 99, 92% bij 100 tot 999 en 93% bij 1.000+. Voor Koreaans 42%, 56%, 77%, 89%; voor Japans 55%, 70%, 88%, 89%. Bij de 101 met 100+ reviews hebben er 93 Chinees. Dat is samenhang, geen bewijs dat vertalen verkoopt: grotere makers vertalen ook meer. Wel één tegenvoorbeeld dat iets zegt: **Cornerpond** is alleen in het Engels (appdetails, nagekeken) en haalt toch 8% Chinese reviews; spellen met Chinees halen mediaan 24%. Chinese kopers komen dus ook zonder vertaling, maar met vertaling ±3 keer zoveel (één spel, GOK hoe algemeen).

**Japans, eerlijk:** bijna elk succesvol spel heeft Japans (88%), maar Japanse reviews halen bij geen enkel spel de drempel. Of Japanse kopers minder reviews schrijven of weinig kopen, zegt deze meting niet (GOK: allebei een beetje).

**Advies voor Hats (aangescherpt):** Engels plus Vereenvoudigd Chinees bij de lancering, dat is de norm bij 93 van de 101 spellen die 100+ reviews haalden. Koreaans als derde taal (77 tot 89% van de succesvolle spellen, en bij 3 van de 17 een eigen markt van 10%+). Japans is goedkoop mee te nemen als de tabel toch vertaald wordt, maar levert in deze cijfers weinig zichtbaars op. Duits, Frans, Russisch en Braziliaans pas later.

**Wat nu nog niet gemeten is:** talen bij kleine spellen (onder de drempel). Dat kan alleen via de reviewlijst per taal op steamcommunity.com, die na ±45 verzoeken een 429 geeft; werk voor meerdere runs en voor de keuze van Hats niet nodig, want de grote spellen laten het al duidelijk zien.
