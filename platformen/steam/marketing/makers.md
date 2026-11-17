# Makerslijst Hats of the Fallen (Sem, versie 1, 16 nov 2026)

Opdracht: fest-plan punt 2, klaar di 24 nov. Dit is **versie 1**: 40 YouTube-kanalen die aantoonbaar een bureaublad-, idle- of cozy spel speelden. Twitch en TikTok volgen (zie "Open").
Niemand is benaderd. Versturen is iets plaatsen op internet en gaat via de hoofdchat en de lijst van Thijs.

## Eerste ronde in één blik (bijgesteld run 13, 16 nov ±23:40 UTC; voorstel voor de hoofdchat en Thijs; niets verstuurd)
De 15 die als eerste een mail of sleutel krijgen, nu gekozen op **wat een video van ons soort op dat kanaal gewoonlijk haalt** (mediaan weergaven van zijn recente video's over idle, cozy, desktop, demo, fest of komende spellen; meting en grenzen in "Bereik per maker" hieronder). Run 4 koos op "maakt precies ons soort video" en pakte daardoor kanalen waar zo'n video ±200 weergaven haalt. Mediaan per kanaal: oude ronde 5.000, nieuwe ronde 45.000 (GEZIEN, `data/yt-bereik-2026-11-16.csv`).
| # | Wie | Ons soort video haalt (mediaan) | Route | Wanneer |
|---|---|---|---|---|
| 23 | Easily Distracted Games | 89.000 (2,5x abonnees); "16 Upcoming Management Games That Look Incredible" 119.000, "18 Upcoming ..." 243.000 | bureau | paginadag (±8 dec), voor hun volgende "upcoming"-lijst |
| 73 | OKtrix | 37.000 alle soorten; "Top 25 Upcoming Cozy Games You Need to Wishlist Now" 10.000 | gmail in kanaaltekst (Thijs kopieert) | paginadag |
| 25 | Fleurs | 18.000; maandlijst "All the COZY games releasing November 2026!" 31.000 | kanaaltekst | begin februari, voor haar lijst van de lanceermaand (alleen spellen die die maand uitkomen) |
| 22 | Gaming In The Wild | 13.000 (0,8x); "The Indie Game Guide To November" 26.000, Next Fest-keuzes 23.000 tot 34.000 | bureau | paginadag kort, daarna begin februari voor de "Indie Game Guide" van de lanceermaand |
| 68 | I Dream of Indie Games | 6.950, wekelijkse lijst | eigen domein | paginadag |
| 69 | Cozy With Toxi | 4.300, "upcoming cozy" | eigen domein | paginadag |
| 44 | Idle cub | 191.000 (0,9x), half zijn titels idle | YouTube-knop (komt op lijst-thijs bij demo af) | demo af (18 dec) |
| 10 | Gohjoe | 156.000, roguelites en "controls your PC" | zakelijk gmail in kanaaltekst | demo af |
| 11 | Dex | 129.000, incrementals | kanaaltekst | demo af |
| 17 | JGigs | 427.500 (4,9x); alleen "I Played 20 [soort] For 2 Hours Each" van uitgebrachte spellen (Tycoon 252.000, eerder idle 812.820) | YouTube-knop (nieuw) | na de lancering, met een sleutel van het volle spel; vóór die tijd niets |
| 29 | MaxPalaro | 104.500 (0,04x, 2,82M abonnees, Portugees) | eigen domein | demo af, in het Engels |
| 28 | 강한오빠 (strongbro) | 4.800 (0,9x), kantoorwerkers, speelde Deskrawl | kanaaltekst | demo af |
| 71 | Rusty Champaign | 5.900, bijna elke dag een demo | via kanaal | demo af |
| 20 | Nookrium | 45.000, "best from Next Fest" | via kanaal | festweek (14 jan) |
| 39 | Dekaff (Dekaif) | 486.000 (2,5x), "unhinged games on Next Fest" | zakelijk adres in kanaaltekst | festweek (14 jan) |
Paginadag aangevuld met 75 Kaganath, 76 GameGen, 77 Get To It en 78 Sloth Vibes (zie "Nieuwe kanalen via zoeken"; run 13). Titels en timing nagekeken op hun laatste 12 video's (run 13, ±23:40 UTC): Fleurs en Gaming In The Wild maken lijsten van wat in een maand **uitkomt**, JGigs alleen van uitgebrachte spellen; daarom later. Eruit gehaald uit de eerste ronde (blijven op de lijst, naar Curator Connect bij demo af, geen eigen mail): The Indie Brew (mediaan 208; de 16.602 was een uitschieter), Maybe Sarisa (566, ook haar bureaubladvideo maar 927), Conkbot (27), NextBigGames (1.400), CozyAriGames (1.500), Kosh Idle (1.600), GriffyBit TV (5.000, streams). Waarom: een mail kost Thijs evenveel tijd bij 200 als bij 90.000 weergaven.
Verwachting (GOK): het totaal aan weergaven van video's waarin Hats kan staan gaat omhoog, maar in een lijstvideo zijn we 1 van 15 tot 30 spellen en grote kanalen geven weergaven, geen kopers (Desktop Survivors 98, Fenna verhaal 9). De begroting in `festplan.md` (makers ±10.000 tot 60.000) laat ik staan tot de paginadag echte doorkliks laat zien.

**Correctie run 5 (16 nov ±15:50 UTC): abonneegetallen van 19 kanalen waren fout.** Mijn script `data/yt-kanaal.py` nam het eerste "subscribers" op de pagina, en dat is vaak een ander, uitgelicht kanaal. Nu leest het de kop van het kanaal zelf (GEZIEN: bij Dekaif staat 192K naast zijn eigen zakelijke adres, de 705K hoorde bij een uitgelicht kanaal). Alle 67 kanalen opnieuw gemeten; wat meer dan 10% afweek staat nu in de tabellen als "nieuw (was oud)". Fenna had de goede getallen. Wat dit verandert aan de eerste ronde: **MaxPalaro is 2,82M, niet 22,7K** (blijft erin: zijn kanaaltekst vraagt zelf om sleutels, maar reken op minder kans op antwoord); Nookrium 191K en I Dream of Indie Games 64,3K zijn groter dan gedacht; GriffyBit TV 9,63K kleiner. Olexa (298K), Wanderbots (522K) en JGigs (87,8K) zijn ook groter. Kansen heb ik verder niet aangepast: die hingen aan wat ze maken en of ze actief zijn, niet aan de grootte (Fenna: grote kanalen geven weergaven, geen kopers).

## Hoe ik keek (alles GEZIEN 16 nov 2026, ±11:20 tot 11:45 UTC)
- YouTube-zoekpagina, met curl, gesorteerd op weergaven en op relevantie, 18 zoektermen (Rusty's Retirement, Desktop Defender, Deskrawl, Desktop Survivors 98, Bao Bao's Cozy Laundromat, Ropuka's Idle Island, Tiny Pasture, Task Bar Hero, Minimon, "desktop companion games", "idle games to play while you work", "games that sit at the bottom of your screen", "taskbar games steam", Next Fest idle). Script: `data/yt-zoek.py`. 246 kanalen gevonden; video's over Windows Defender en dergelijke eruit gefilterd.
- Per kanaal de openbare "about"-pagina met curl: abonnees, land, kanaaltekst. Script: `data/yt-kanaal.py`. Het aantal video's dat het script geeft is niet betrouwbaar, dat laat ik weg.
- **Contact:** alleen wat het kanaal zelf in zijn openbare kanaaltekst zet. Een adres op een eigen domein of van een bureau schrijf ik uit. Een gewoon gmail- of naver-adres noem ik alleen als "staat in kanaaltekst": de repo is openbaar en ik wil geen lijst met privé-ogende adressen maken. Wie verstuurt, zoekt het op het kanaal op.
- Weergaven en abonnees zijn één meting op één dag. Zoekresultaten verschillen per land.

## Indeling
- **A. Speelt precies ons soort spel** (een bureaublad- of strookspel als eigen video). Hoogste kans, want hun kijkers kozen al voor dit soort.
- **B. Lijstjes en cozy-overzichten** ("speel dit terwijl je werkt", fest-overzichten). Volgens verhaal 4 van Fenna komen bij de kleine succesjes de meeste weergaven hiervandaan.
- **C. Andere talen.** Bij Rusty was de grootste video Koreaans (908.000), bij Deskrawl Japans en Taiwanees. Alleen zinvol als de demo die taal heeft (fest-plan punt 6).
- **D. Groot, lage kans, wel proberen** via een mail of Curator Connect, zonder verwachting.

Kans per maker is een GOK op basis van: speelde al zo'n spel, kanaal speelt kleine spellen, nodigt zelf uit om spellen te sturen.

## De 40

### A. Speelt precies ons soort spel (14)
| # | Kanaal | Land | Abonnees | Bewijs (video, weergaven) | Speelt klein? | Contact openbaar | Kans |
|---|---|---|---|---|---|---|---|
| 1 | Buckeye Bunny (@BuckeyeBunny) | VS | 19,1K | "Rusty's Retirement Review", 66.642; "31 FREE Chill & Cozy Games, Next Fest Feb 2025" 17.410 (met Bao Bao) | ja, cozy nieuws en reviews | nee in tekst | ~~hoog~~ **laag: laatste video ±1 jaar oud** (run 3) |
| 2 | Olexa (@OlexaYT) | VS | 298K (was 11,2K) | "This New Idle Farming Game is Pure Genius" 66.436, twee Rusty-video's (27.164, 11.574) | ja, indie | nee | hoog |
| 3 | Orbital Potato (@orbitalpotato) | VK | 197K | "The ULTIMATE Idle Distraction Game!? Rusty's Retirement" 29.153 | ja, management en kolonie | nee in tekst | middel |
| 4 | Higher Plain Games (@HigherPlainGames) | VK | 29 (klein) | reviews van Desktop Defender 2.612 en Tiny Pasture 3.861 ("Bottom Screen Idler") | ja, niche | nee | hoog (klein, maar recenseert precies dit) |
| 5 | SpiritAnden (@SpiritAnden) | Zweden | 1,53K | "Time to Game While Gaming! Desktop Defender Review" 1.738 | ja, "as many games as I can, mostly indie" | nee | hoog |
| 6 | RinKa Plays (@RinKaPlays) | VS | 4,45K | Ropuka 11.818, Tiny Pasture 2.040 ("Let's Try") | ja, "indie games you might otherwise miss" | staat in kanaaltekst | hoog |
| 7 | Kosh Idle (@KoshIdle) | VS | 12,9K (was 17,4K) | "IDLE SCREENSAVER // ROPUKA'S IDLE ISLAND" 4.161 | ja, alleen idle en incremental | nee | hoog |
| 8 | W A R D E N (@n.warden97) | VK | 24,7K | "TINY PASTURE, little desk buddies!" 3.543 | ja | staat in kanaaltekst ("Contact me") | ~~hoog~~ middel (run 3: 1 video in 30 dagen) |
| 9 | Tchii (@Tchii) | België | 2,59K (was 10,7K) | "Tiny Pasture, another must-have super cute idle" 1.499 | ja, indie | staat in kanaaltekst | hoog |
| 10 | Gohjoe (@Gohjoe) | ? | 201K | "This Roguelite Controls Your PC to Survive" (Desktop Survivors 98) 82.126 | ja, "indies/roguelites daily" | gohjoebusiness (gmail, "all business inquiries") | middel |
| 11 | Dex (@DexTag) | Duitsland | 316K | "Windows 98 Horde Survivor is CRAZY" 23.762; maakt incrementals | ja | staat in kanaaltekst | middel |
| 12 | knekroTV (@knekroTV) | Spanje | 158K | "DESKRAWL is like DIABLO but AFK" 30.423 (stream) | ja, variëteit | nee | middel (Spaans) |
| 13 | Starker MMOs (@StarkerMMOs) | Brazilië | 11,6K | "The next Task Bar Hero!?" over Deskrawl 8.752, TBH-gidsen 51.375 | ja | staat in kanaaltekst ("parcerias") | middel |
| 14 | Wanderbots (@wanderbots) | VS | 522K (was 10,5K) | "Incremental Farm Sim To Play While Playing Other Incremental Games" (Rusty) 18.058 | ja, "100% human-made videogames" | nee | ~~hoog: hij zoekt bewust spellen zonder AI; Hats is zonder AI-beeld~~ **laag, niet als "zonder AI" benaderen** (correctie run 2: Hats wordt gemaakt door AI-agents, ook de code die de 3D-beelden maakt en de teksten in het spel; zie "Correctie" onder) |

### B. Lijstjes en cozy-overzichten (12)
| # | Kanaal | Land | Abonnees | Bewijs | Contact openbaar | Kans |
|---|---|---|---|---|---|---|
| 15 | The Indie Brew (@theindiebrew) | Australië | 3,98K | "The BEST Idle Games to play While You Work" 16.602 | **hello@theindiebrew.com.au** ("Want coverage for your indie game? Shoot us an email") | hoog |
| 16 | Conkbot (@Conkbot) | Australië | 778 | "Cozy Idle Games You Can Run While You Study/Work (Tier List)" 16.064 | nee | hoog (lijst precies ons soort) |
| 17 | JGigs (@JGigs) | VS | 87,8K (was 4,15K) | "I Played 20 Idle Games For 2 Hours Each" 812.820 en 316.348 | nee | middel (één uitschieter, maar wel ons publiek) |
| 18 | Best Indie Games (@ClemmyGames) | Singapore | 195K | "MOST ADDICTIVE Incremental/Idle Games" 43.224 (met Ropuka) | nee in tekst | middel |
| 19 | CozyAriGames (@CozyAriGames) | Canada | 4,03K | "Exclusive First Look at Tiny Pasture" 2.586 (vóór de lancering, dus via de maker) | nee | hoog (doet al "first look" voor kleine makers) |
| 20 | Nookrium (@Nookrium) | VS | 191K (was 3,23K) | "Thousands of New Games This Week, Next Fest 2026" 97.186; "best overlooked" spellen, dagelijks | nee | hoog in de fest-week |
| 21 | Indie Games Hub (@IndieHub01) | Indonesië | 283K | "Top 30 Pixel Arts Games in Steam Next Fest October 2026" 45.452 | zegt "contact me via email below", adres stond niet in de gelezen tekst | middel |
| 22 | Gaming In The Wild (@GamingInTheWild) | IJsland | 15,5K (was 1,85K) | "25 Next Fest Picks In Three Minutes, June 2026" 42.114 | **gaminginthewild@digitalfoxtalent.com** (bureau) | middel |
| 23 | Easily Distracted Games (@easilydistractedgames) | ? | 35,7K | "18 Best Cozy Management Games in 2026" 203.063 | **easilydistractedgames@puka.agency** (bureau) | middel |
| 24 | Lex Play (@LexPlayy) | VS | 222K | "50 Cozy Games To Play This Year" 516.434 | nee | laag tot middel |
| 25 | Fleurs (@Fleurs_) | VK | 120K (was 3,61K) | "TOP 20 highest rated Cozy Games of 2026 so far" 48.179 | staat in kanaaltekst | middel |
| 26 | KultZ (@KultZz) | VS | 11,6K | "Top 5 Incremental Games You NEED to Play in 2026" 34.069 | nee | middel |

### C. Andere talen (9)
| # | Kanaal | Taal | Abonnees | Bewijs | Contact openbaar | Kans |
|---|---|---|---|---|---|---|
| 27 | 우주하마 (@uzuhama) | Koreaans | 2,2M | Rusty, "중독성 쩌는 방치형 게임" 907.979 (de grootste video over Rusty) | nee | laag, maar enorme hefboom; alleen met Koreaanse demo |
| 28 | 강한오빠 (@strongbro) | Koreaans | 5,52K | Deskrawl, 17.001; maakt video's "vanuit kantoorwerkers" | staat in kanaaltekst | hoog (kantoor-invalshoek past precies) |
| 29 | MaxPalaro (@MaxPalaro) | Portugees (BR) | 2,82M (was 22,7K) | "GAME PRA JOGAR ENQUANTO TRABALHA, Rusty's Retirement" 51.757 | **"For keys and gaming offers"**: adres op eigen domein maxpalaro.com.br in kanaaltekst | hoog (vraagt zelf om sleutels) |
| 30 | Felps LIVE (@FelpsLIVE) | Portugees (BR) | 758K | Rusty-reeks 46.681, 15.744, 13.787 | nee | laag tot middel |
| 31 | 狐狸牧場 foxranch (@foxranch) | Chinees (TW) | 188K (was 14,9K) | Rusty "可以邊上班邊玩" 44.791 | **foxranch1216@mesports.tw** ("有要合作的也歡迎聯絡我") | hoog met Chinese demo |
| 32 | 老頭Z (@LaotouZ_Gaming) | Chinees (TW) | 6,63K | "Desktop Diablo" (Deskrawl) 29.429 | nee | middel |
| 33 | ひろてく (@hirotech-games) | Japans | 3,39K | Rusty 8 uur laten draaien, 19.442 | nee | middel |
| 34 | FineByMeh (@FineByMeh) | Thai | 7,87K | Ropuka "เพื่อนแก้เหงาเวลาคุณทำงาน" 5.696 | nee | middel |
| 35 | 陈汉西 (@ChenHanxi) | Chinees | 19,6K | Deskrawl "Desktop Diablo" 17.463 | alleen een WeChat-nummer, niet overnemen | middel |

### D. Groot, lage kans (5)
| # | Kanaal | Abonnees | Bewijs | Contact | Kans |
|---|---|---|---|---|---|
| 36 | Vinesauce (Vinny, @vinesaucefullsauce, archief) | 1,25M | "Vinny, Desktop Survivors 98 (Demo)" 50.234: speelt fest-demo's | nee | laag, maar Fenna noemt zijn Next Fest-stream (40.008) |
| 37 | GameGrumps (@GameGrumps) | 5,45M (was 1,27M) | Desktop Survivors 98, 270.087 | nee | laag |
| 38 | Kripparrian (@Kripparrian, VOD-kanaal) | 901K (was 33,4K, verkeerd gelezen) | Deskrawl-stream 21.318 | nee | laag (ARPG-publiek, Hats is minder grind) |
| 39 | Dekaff (@Dekaif) | 192K (was 705K) | "I Played 7 Unhinged Games on Steam Next Fest" 751.500 | **Partners@saltraiders.com** (zakelijk) | laag tot middel: "unhinged" past bij Gloop die hoeden eet |
| 40 | Wholesome Games (@WholesomeGames) | 62,7K | trailers Ropuka 26.846, Rusty 20.242, Bao Bao 7.280 | via hun showcase (oude inzendpagina bestaat niet meer, Fenna) | middel als we een showcase halen |

## Aanvulling 16 nov, run 2: 19 kanalen uit Fenna's verhaal 9 (nummer 41 tot 59)
Bron: `platformen/succes/data/youtube-kanalen-winnaars-2026-11-16.csv` (Fenna, GEZIEN 16 nov). Per kanaal de grootste video over een winnaar. Contact nog niet nagekeken (volgende run, zelfde regel als boven). Fenna's bak tussen haakjes.
| # | Kanaal | Abonnees | Grootste video (spel, weergaven) | Bak / kans |
|---|---|---|---|---|
| 41 | Hadomancer (@Hadomancer) | 100K | TBH, "The game you don't even play is breaking Steam" 350.336 (3,5x abonnees) | A, middel: maakt video's over wat al groot is |
| 42 | Maybe Sarisa (@MaybeSarisa) | 1,63K | Ropuka, "Cozy Idle Games Under $10 for Multitasking" 3.140 | A, hoog: klein, precies onze lijst |
| 43 | Indie Signal (@IndieSignal) | 27 (run 5) | Ropuka, "10 Idle Games on Steam That Will Quietly Ruin Your Life" 7.233 | A, hoog (lijstje) |
| 44 | Idle cub (@idlecub) | 203K | Desktop Survivors 98, 28.231 | A, middel |
| 45 | Krayn (@Krayn) | 95K | Deskrawl, "THE PERFECT GAME TO PLAY WHILE DO(ing other things)" 7.547 | A, middel |
| 46 | Gaming Meets Experience | 2,21K | Deskrawl, 6.478 | A, middel (vooral gidsen) |
| 47 | Plano Plays Games (@PlanoPlaysGames) | 566K | Desktop Raid, "The Ultimate Productivity RPG?" 23.940 | B (groot), laag tot middel |
| 48 | Mattastic ASMR (@MattasticASMR) | 293K | Desktop Survivors 98, 110.002 | B, laag: actief spel, ASMR-publiek |
| 49 | Bijuu Mike (@BijuuMike) | 3,78M | Desktop Survivors 98, 38.967 | B, laag |
| 50 | EuSouOGiba (@EuSouOGiba) | 17,3K | Deskrawl, 6.029 (Portugees) | C, alleen met Portugees |
| 51 | Task Bar Hero Dicas (@tbhdicas) | 13,4K | TBH-gids 137.668 (10x abonnees, Portugees) | C, laag: gidsen komen pas na succes |
| 52 | 小月歡樂星 | ? | Deskrawl-stream 13.902 (Chinees, TW) | C, alleen met Chinees |
| 53 | しんじさん | ? | Deskrawl-demo 37.451 (Japans) | C, middel met Japans: speelde een demo |
| 54 | くろろじちゃんねる (@KUROROJI) | 41,7K | Deskrawl, "eindelijk Diablo spelen terwijl je werkt" 6.753 (Japans) | C, middel met Japans |
| 55 | Tietie TH. (@TietieTHAI) | 43,9K | Desktop Raid, 19.835 (Thai) | C, alleen met Thai |
| 56 | Diomio (@Diomio-Game) | 180K | TBH, "everyone is playing AFK games now" 98.806 (Vietnamees) | C, laag |
| 57 | GameStar (@gamestar) | 1,59M | TBH, "#2 on Steam" 81.403 (Duits, pers) | C/pers, laag: schrijft over succes |
| 58 | IlloRubiu (@Illorubiu3) | 1,63K | Deskrawl-stream 6.282 (Spaans) | C, middel met Spaans |
| 59 | Alex Baena (@alexpolybius) | 59,3K | Rusty, video-essay over het genre 30.403 (Spaans) | C, middel: essay over "het genre", Hats past in een vervolg |

**Contact van deze 19 (GEZIEN 16 nov ±12:55 UTC, openbare kanaaltekst, script `data/yt-kanaal.py`; 小月歡樂星, しんじさん, GameStar niet gelezen):**
- Adres op eigen domein of bureau: **Maybe Sarisa: contact@maybesarisa.com** (eigen domein, VS); **くろろじちゃんねる: kuroroji.ch@youdaoads.com** (bureau, Japan).
- "Staat in kanaaltekst" (gewoon mailadres, niet overgenomen): Hadomancer (Brazilië), Gaming Meets Experience (Turkije), Task Bar Hero Dicas, Diomio.
- Geen adres in de tekst: Indie Signal, Idle cub, Krayn, Plano Plays Games, Mattastic ASMR, Bijuu Mike, EuSouOGiba, Tietie TH., IlloRubiu, Alex Baena.
- Let op: mijn script gaf bij vier kanalen een ander abonneegetal dan Fenna (Krayn 16,6K tegen 95K, Mattastic ASMR 3,79K tegen 293K, くろろじ 10K tegen 41,7K, Indie Signal 27). Mogelijk leest mijn script een ander getal van de pagina; nakijken voor de eerste mail. Hadomancer zit in Brazilië, dus een Engelse mail kan, Portugees ook.
- Maybe Sarisa schuift daarmee naar de eerste ronde mails (groep B, lijstje "Cozy Idle Games Under $10 for Multitasking").

**Wat ik meeneem uit Fenna:** de echte doorbraken kregen hun grote video's ná het succes (TBH, GameStar, Hadomancer). Die kanalen zijn dus voor de week ná een doorbraak in de meetlat (`festplan.md`), niet voor de aanloop. Voor de aanloop tellen de kleine lijstjesmakers met veel weergaven per abonnee (The Indie Brew 4x, JGigs 9x, Maybe Sarisa, Indie Signal, Conkbot).

## Nog actief? Laatste 30 video's per kanaal (run 3, GEZIEN 16 nov ±13:40 UTC)
Per kanaal de pagina /videos met curl, de nieuwste ±30 video's: hoe lang geleden de laatste, hoeveel in de laatste 30 dagen, mediaan weergaven, en hoeveel titels over idle, desktop, taakbalk, cozy, demo of fest gaan. Script `data/yt-recent.py`, uitkomst `data/yt-recent-makers-2026-11-16.csv`. "30" bij "laatste 30 dagen" betekent 30 of meer. Leeftijd is afgerond zoals YouTube hem toont ("1 year ago").

**Gevallen af of lager (niet meer actief):**
- #1 Buckeye Bunny: laatste video ±1 jaar oud. Van hoog naar laag.
- #34 FineByMeh: laatste ±3 maanden, mediaan 275. Laag.
- #43 Indie Signal (YouTube): 11 video's, laatste ±7 maanden. Laag. (Hun Steam-curatorpagina heeft 23.659 volgers waarvan 1% echt, zie `curatoren.md`.)
- #8 W A R D E N: 1 video in 30 dagen, geen enkele titel in ons soort. Van hoog naar middel.
- #27 uzuhama, #59 Alex Baena, #48 Mattastic ASMR: 1 tot 2 video's in 30 dagen. Blijven laag.

**Sterker dan gedacht (actief én ons soort, dit zijn de eerste mails):**
| # | Kanaal | Video's laatste 30 dagen | Mediaan weergaven | Titels in ons soort (van 30) | Wat opvalt |
|---|---|---|---|---|---|
| 42 | Maybe Sarisa | 14 | 225 | 2 | maakte "Cozy Idle Desktop Companion Taskbar Games You've Missed" en "Steam Next Fest October 2026 Tiny Game List": precies onze plank, eigen domein-adres |
| 16 | Conkbot | 10 | 55 | 15 | maakt **maandlijsten** ("15 Cozy, Creative & Co-op Games Coming in November 2026"): de lijst voor januari 2027 is ons doel, mail begin december |
| 7 | Kosh Idle | 18 | 1.600 | 14 | alleen idle, elke dag |
| 19 | CozyAriGames | 14 | 1.050 | 12 | "First Look"-video's van demo's; ook Steam-curator (6 van onze 12 spellen) |
| 11 | Dex | 30+ | 129.500 | 10 | groot en elke dag incrementals |
| 44 | Idle cub | 30+ | 199.500 | 15 | groot en half zijn titels zijn idle; van middel naar middel-hoog |
| 18 | Best Indie Games (ClemmyGames) | 23 | 28.000 | 7 | wekelijks "Indie Gaming This Week" en "100 Next Fest Demos": fest-overzicht |
| 25 | Fleurs | 20 | 17.500 | 11 | cozy, vaak vooruitblik |
| 13 | Starker MMOs | 6 | 3.000 | 29 | bijna alles idle-gidsen; gidsen komen pas na de lancering |
| 3 | Orbital Potato | 30+ | 59.000 | 3 | groot, speelt "idlers"; middel |
| 14 | Wanderbots | 30+ | 27.000 | 5 | speelt demo's ("[Demo]" in titels); blijft laag om de AI-reden |

**Fest-overzichten (actief, voor 14 tot 18 jan):** Nookrium (30+, mediaan 17.000, "The Best Games from Next Fest"), Gaming In The Wild (5, 12.500, Next Fest-lijsten), Easily Distracted Games (10, 61.000), Dekaff (2, mediaan 238.000, "Wildest Demos on Steam"), Best Indie Games.

**Kleine kanalen met heel lage mediaan** (Higher Plain Games 222, SpiritAnden 224, The Indie Brew 214, RinKa Plays 20, Tchii 109): een video daar brengt weinig kijkers. Ze blijven op de lijst omdat ze precies ons soort spellen recenseren en vaak ook een Steam-curatorpagina hebben (Higher Plain Games, Tchii, The Indie Brew, zie `curatoren.md`): één sleutel geeft dan een video plus een curatorrecensie.

**Eerlijke rekensom (GOK):** de mediaan per video van de 11 kanalen hierboven loopt van 55 (Conkbot) tot 199.500 (Idle cub). Als 4 van de 11 een video maken met hun mediaan, is dat grofweg 5.000 tot 200.000 weergaven, en met een klikratio naar Steam van 1 tot 3% (GOK) 50 tot 6.000 bezoekers. Dat is genoeg om in het vak te stijgen, niet om alleen daarmee door te breken. Makers zijn de aanloop; het fest zelf blijft het moment (`festplan.md`).

## Twitch: streamers gevonden via hun VOD-kanalen (run 4, GEZIEN 16 nov ±14:40 tot 14:55 UTC)
**Waarom zo:** SullyGnome, TwitchTracker en Streams Charts geven 403 met curl (GEZIEN, run 1 en nu), en de Twitch-API vraagt een sleutel van Thijs. Veel streamers zetten hun streams als "VOD" of "archive" op YouTube; die vind je met dezelfde zoekpagina. Zoektermen: "<spel> stream" en "<spel> twitch" voor Rusty's Retirement, Deskrawl, Desktop Defender, Task Bar Hero, Desktop Survivors 98, Tiny Pasture, plus "idle desktop game stream vod" (11 zoekopdrachten, video's langer dan een uur = stream). Activiteit uit `data/yt-recent-streamers-2026-11-16.csv` (laatste 30 video's).
| # | Streamer (VOD-kanaal) | Twitch | VOD-kanaal abonnees | Bewijs (stream, weergaven van het archief) | Actief? (dagen sinds laatste VOD, mediaan) | Kans |
|---|---|---|---|---|---|---|
| 60 | Laimu (@LimeArchives) | ja, VTuber | 65,2K (was 411K) | "Idle Farm Game with Chat ~ Laimu plays Rusty's Retirement" 1.740, en Rusty na Heavy Rain 2.488 | 0 dagen, mediaan 8.600, speelt cozy | middel: speelde Rusty **met haar chat**, juist de functie hieronder |
| 61 | GriffyBit TV (@GriffyBitTV) | ja | 9,63K (was 43,5K) | streams met "Some Other Idle Games" (1.528) en Idle Monster TD (2.565); vooral IdleOn | 10 dagen, mediaan 3.550, 21 van 30 titels idle | hoog: idle-streamer die nieuwe idle-spellen probeert |
| 62 | Krayn (#45, @Krayn) | ja, krayn_live (staat in zijn kanaaltekst) | 16,6K (VOD-kanaal) | Deskrawl-stream 7.547 | 0 dagen, mediaan 9.500 | middel (Frans) |
| 63 | Kripparrian (al in D) | ja | 901K (was 33,4K, verkeerd gelezen) | "VARIETY! Lootbound / Deskrawl!" 21.318 | dagelijks | laag tot middel: groot, speelt wel kleine ARPG-achtige spellen in variety-streams |
| 64 | CallMeCarson (@CallMeCarsonVODS) | ja (groot) | 196K (was 2,45M) | "Every 5 Minutes, I add another Idle Game" 4.893 | 4 dagen, mediaan 11.000 | laag: één idle-stream, groot kanaal; alleen via Curator Connect of mail zonder verwachting |
| 65 | Edouard_EMB (@edouard_emb) | ja (staat in kanaaltekst) | 347K | "Un jeu en BARRE DE TACHE ?!" (Rusty) 3.911 | 0 dagen, mediaan 28.000 | laag tot middel (Frans; bureau-adres staat in kanaaltekst, niet overgenomen) |
| 66 | Phenexa (@Phenexa) | ja | 1,86K | Rusty 1.428, Tiny Pasture 230 | 6 dagen, klein | hoog voor een klein kanaal: speelt elk cozy spel als "First Look" |
| 67 | Game Launch Central (@GameLaunchCentral) | nee, YouTube | 17,3K | "10 Upcoming Idle Games for Endless Fun..." 525; TBH-gidsen tot 11.732 | 0 dagen, 30 video's in 30 dagen | **hoog voor de aanloop**: maakt lijsten van *komende* idle-spellen, precies waar een spel met alleen een pagina in past (zakelijk adres in kanaaltekst, gmail, niet overgenomen) |
- Ook gezien, niet opgenomen: AceTo (stream van 9 uur Desktop Defender, 103 tot 173 weergaven, 139 abonnees), Felps LIVE (Rusty 46.682, staat al in groep C via Fenna), GRINDING CURRENCY (12 Deskrawl-gidsen, 1,74K, maakt alleen gidsen over spellen met een markt), Zhain Gaming (volledige doorspeelvideo's, geen idle).
- **Eerlijk:** de streams over bureaubladspellen hebben op YouTube kleine archiefcijfers (100 tot 21.000). Live kijkers op Twitch zie ik zo niet. Wat telt is dat deze streamers het spel **uren** laten draaien, met chat erbij.

### Gevonden tijdens het zoeken: Rusty's Retirement heeft Twitch-koppeling, de rest niet
- Rusty's winkelpagina (GEZIEN, appdetails 2666510): "Twitch Integration available: Streamers and viewers can build a farm together. Viewers can control what task their robot should focus on through chat commands like !plant !water !harvest."
- Ik heb de beschrijving van 190 spellen gelezen (Steam-zoekpagina op "desktop idle", "taskbar", "desktop companion", "bottom of your screen", "idle desktop pet", plus 10 bekende bureaubladspellen; script `data/twitch-koppeling.py`, cijfers in `data/twitch-koppeling-2026-11-16.csv`; "reviews" is het getal "recommendations" uit de winkel-API). Van de bureaublad- en idle-spellen met meer dan 400 reviews noemt **alleen Rusty** (13.987 reviews, de grootste) een koppeling met chat. Deskrawl (3.642), Tiny Pasture (7.142), Ropuka (4.113), Desktop Defender (1.788) en Task Bar Hero niet. Andere met iets voor streamers: Spirit City (muziek mag op stream), Burgie's Cozy Kitchen (streamermodus), Kukoro (919 reviews, een heel spel van chat-minispellen).
- Wat het **niet** bewijst: dat Rusty groot werd door de koppeling (GOK, één spel). Wat het wel laat zien: een open plek bij precies ons soort spel, en het past op Hats beter dan op een boerderij, want onze helden hebben al een naam, een wrok en een hoed. Voorstel aan Sanne (optie D, "chat-helden") staat in `berichten/sanne.md`.

## Aanloop: kanalen met lijsten van *komende* spellen (run 4, GEZIEN 16 nov ±15:00 UTC, nummer 68 tot 73)
**Waarom deze groep:** tussen de pagina live (±8 dec) en de demo (4 jan) hebben we alleen een pagina en een GIF. De makers in A spelen een spel; deze kanalen zetten een spel dat nog niet uit is in een lijst ("wishlist these"). Gevonden met 8 zoekopdrachten ("upcoming idle games 2026/2027", "upcoming cozy games 2027", "upcoming desktop games steam", "new idle games steam demo", "upcoming taskbar games", "best steam demos idle", "upcoming indie games january 2027"). Activiteit uit `data/yt-recent-aanloop-2026-11-16.csv`. Kanalen met alleen mobiele gacha-lijsten of AAA-lijsten weggelaten.
| # | Kanaal | Abonnees | Bewijs (video, weergaven) | Actief (laatste video, video's in 30 dagen, mediaan) | Contact openbaar | Kans |
|---|---|---|---|---|---|---|
| 68 | I Dream of Indie Games (@IDreamofIndie) | 64,3K (was 1,72K) | "I Found 70 NEW Indie Games You Should Grab This Week!" 11.629 (8 dagen oud); is een eigen indie-mediasite | 1 dag, 30, 11.500 | adres op eigen domein in kanaaltekst | **hoog**: wekelijkse lijst, 7x abonnees per video, mediasite met eigen adres |
| 69 | Cozy With Toxi (@CozyWithToxi) | 9,71K | "20 HUGE Upcoming Cozy Games Worth Waiting For! (2026 & Beyond)" 19.063 | 4 dagen, 17, 10.500 | adres op eigen domein in kanaaltekst | **hoog**: cozy, komende spellen, eigen adres |
| 70 | NextBigGames (@thenextbiggames) | 2,61K | "October 2026 Promising Idle Games: 106 Games + 12 Categories" 748 (5 dagen oud) | 1 dag, 18, 1.450 | adres op eigen domein in kanaaltekst | hoog voor zichtbaarheid bij makers en uitgevers: maandlijst van idle-spellen die nog komen; klein publiek |
| 71 | Rusty Champaign (@RustyChampaign) | 25,3K (was 4,83K) | "A Cozy Idle Game About Turning a Desert Into an Oasis! (Quiet Bloom demo)" 4.486 | 0 dagen, 28, 5.750 | niet in tekst | hoog: speelt bijna elke dag een cozy of idle demo |
| 72 | Gameskeys (@Gameskeysnet) | 96,6K | "NEW Indie Games Coming in 2026 & 2027" 9.025 (6 video's in mijn zoektermen) | 1 dag, 30, 6.200 | niet in tekst | middel: grote lijsten, wij zijn er één van veel |
| 73 | OKtrix (@OKtrix) | 46,3K (was 9,65K) | "28 NEW Upcoming Unique Simulation Games You Need on Your Wishlist" 58.836 | 1 dag, 30, 27.000 | zakelijk adres in kanaaltekst (gmail, niet overgenomen) | middel: veel weergaven per abonnee (±3x), lijsten op "unique" |
| (74) | ~~Indie Games Hub~~ | | staat al als #21 in groep B; dubbel, geen nieuw nummer | | | |
- **Wanneer:** de dag dat de pagina live is (±8 dec) een korte mail aan 68, 69 en 70 (eigen adres), met GIF en "free demo January 4, Desktop Companion Fest Jan 14 to 18". 71 krijgt een demosleutel zodra de demo af is (18 dec). 72 en 73 pas met een getal (verlanglijstjes of de festuitslag).
- **Eerlijk:** de mediaan van deze kanalen is 1.450 tot 27.000 weergaven per video, maar wij staan in een lijst van 20 tot 106 spellen. Per vermelding zijn het eerder tientallen dan honderden bezoekers (GOK). Het telt omdat het in de weken vóór de demo de enige weg is naast onze eigen clips.

## Wat ik eruit haal (eerste lezing)
1. **De kanalen die precies ons soort spel speelden zijn klein**: 14 kanalen in A, mediaan ±11K abonnees, en de video over het bureaubladspel haalde meestal 1.500 tot 30.000 weergaven. Dat is het eerlijke plafond per video: geen doorbraak uit één mail.
2. **Drie zeggen zelf dat je spellen mag sturen** (The Indie Brew, MaxPalaro, Gohjoe "all business inquiries") en vier hebben een bureau-adres (Gaming In The Wild, Easily Distracted, Dekaff, foxranch). Daar beginnen.
3. ~~**Wanderbots zoekt bewust "100% human-made" spellen.** Hats heeft geen AI-beeld (onderscheid-hats.md, punt 3); dat is hier een echte haak in de mail.~~ **Correctie run 2 (16 nov):** dit was fout. Hats is niet met een AI-beeldtool gemaakt, maar wel door AI-agents: de code die Gloop en het hol in Blender bouwt en rendert, de spelcode en de teksten in het spel (kroniek, namen). "Human-made" of "no AI" zeggen is dan misleidend, en Valve vraagt een AI-melding voor wat spelers zien. Regel voor alle teksten: **we zeggen nergens "no AI" of "human-made"**. Wat we wel eerlijk kunnen zeggen: "no AI image generators", alleen als de hoofdchat de AI-melding op de winkelpagina zo vastlegt. Gemeld in het logboek voor de hoofdchat.
4. **De grote uitschieters zijn niet Engels** (uzuhama 908K, foxranch, strongbro). Zonder Koreaans en Chinees in de demo valt groep C grotendeels weg. Dit weegt mee in het besluit over talen (fest-plan punt 6).

## Plan: wie krijgt wanneer een sleutel (voorstel, nog niets versturen)
| Wanneer | Wie | Wat |
|---|---|---|
| zodra de winkelpagina live is (±8 dec) | groep A en B met openbaar adres (15, 22, 23, 29, 31 en wie in A een adres in tekst heeft), **plus Maybe Sarisa (42) en de aanloopgroep met eigen adres (68, 69, 70)** (run 4) | korte mail: één zin haak ("Every hero who falls in leaves a hat on Gloop's head"), GIF, link naar de pagina, "demo-sleutel vóór het fest als je wilt" |
| vr 18 dec, demo af | wie ja zei | vroege demo-sleutel (Steam-sleutels via Steamworks, of Curator Connect) |
| vr 18 dec, demo af (run 4) | streamers 61, 66 en 71 (GriffyBit, Phenexa, Rusty Champaign), via de route die ze zelf noemen | demosleutel; als chat-helden (optie D bij Sanne) er komt, is dat de eerste zin |
| ±8 dec, 18 dec en lanceerdag (run 11) | TikTok: T3 en T4 bij pagina live, T1 en T5 bij demo af, T2 op de lanceerdag | zelfde korte mail; voor TikTok de zin "sits on top of your taskbar while you work" vooraan |
| 8 jan (Valve-trailer, wij mogen melden) | alle 40, ook zonder adres via Curator Connect | herinnering: demo staat in het Desktop Companion Fest, Fest Hat alleen te halen do 14 jan 19:00 tot ma 18 jan 19:00 NL (run 14), dus een video die dag 1 of 2 uitkomt laat iets zien wat kijkers nog kunnen halen |
| 14 tot 18 jan | groep B (lijstjes) en Nookrium | fest-dag 1: "nieuw in het fest", onze GIF |

Teksten per groep staan in `platformen/steam/marketing/teksten-makers.md` (A, B, D, E, Curator Connect, showcase).

## Open (volgende runs)
- ~~Twitch: wie streamde Rusty, Desktop Defender, Deskrawl.~~ Gedaan run 4 via VOD-kanalen: 60 tot 67 hierboven. Live kijkers op Twitch blijven onbekend zonder Twitch-sleutel.
- ~~TikTok: makers met bureaubladspellen.~~ Deels gedaan run 11: T1 tot T10 onderaan (zoekmachine plus openbaar profiel met curl). Open: idle-RPG-makers op TikTok. Keymailer: besluit "niet nu" (run 11).
- ~~Curator Connect: andere route zoeken.~~ Gedaan run 3: `curatoren.md` (478 curatoren van 12 spellen, eerste ronde van 18, regel tegen nepvolgers).
- ~~Per kanaal de laatste video's.~~ Gedaan run 3, zie "Nog actief?" hierboven. Kripparrian (VOD-kanaal) las niet goed door de handle, nog doen.
- ~~Teksten per groep.~~ Gedaan (run 2 tot 4).
- Stand run 4: **73 makers** (59 YouTube, 8 streamers, 6 aanloopkanalen; Indie Games Hub stond er al als #21), plus 23 curatoren in `curatoren.md`. Vóór di 24 nov: een korte eerste ronde van ±15 namen bovenaan dit bestand zetten, zodat de hoofdchat die in één blik aan Thijs kan laten zien.

## Contact van 41 tot 71 nagelopen (run 7, 16 nov ±17:37 UTC)
Kanaaltekst van 22 kanalen opnieuw gelezen (`data/contact.py`, uitkomst `data/contact-41-71-2026-11-16.csv`; adressen zelf niet overgenomen, alleen het soort). 
| Soort | Aantal | Wie | Route |
|---|---|---|---|
| eigen domein of bureau | 2 | くろろじちゃんねる (#54, via een advertentiebureau), GameStar (#57, redactie) | mail, alleen als de taal in de demo zit (groep C) of als pers bij een doorbraak |
| gratis adres in de kanaaltekst | 5 | Hadomancer (#41), Task Bar Hero Dicas (#51), Diomio (#56), Edouard_EMB (#65), Game Launch Central (#67) | Thijs kopieert het adres zelf van het kanaal (repo is openbaar, daarom hier niet) |
| geen adres in de tekst | 15 | o.a. Idle cub, Krayn, GriffyBit TV, Phenexa, Rusty Champaign, Laimu | de knop "View email address" op YouTube (vraagt inlog en een captcha, dus stap voor Thijs), of Curator Connect zodra de pagina live is |
**Gevolg voor de eerste ronde:** van de 15 namen in "Eerste ronde in één blik" hebben er nu 5 een eigen-domein-adres (Maybe Sarisa, I Dream of Indie Games, Cozy With Toxi, NextBigGames, plus GameStar alleen als pers) en 1 een gratis adres (Game Launch Central). Voor de anderen (GriffyBit TV, Rusty Champaign, Idle cub, Phenexa) is Curator Connect de route: geen adres nodig, en Valve laat zien wie de sleutel gebruikte. **Besluit Sem:** Thijs hoeft geen captcha's op te lossen voor kanalen onder de 10K; die gaan via Curator Connect. Alleen voor Idle cub (203K, half zijn titels idle; Hadomancer heeft al een adres in zijn tekst) zet ik de knop op de lijst van Thijs zodra de pagina live is. Waarom: een captcha per kanaal kost Thijs tijd, en bij kleine kanalen is de kans op een video klein (GOK) terwijl Curator Connect hetzelfde doet zonder adres. **Kanttekening (zelf gevonden, ±18:08 UTC):** Curator Connect bereikt alleen makers die bij Steam een curatorpagina hebben of hun kanaal daar gekoppeld hebben. Of deze kleine kanalen dat hebben, kon ik van buiten niet nakijken (de zoekfunctie van de curatorlijst negeert de zoekterm zonder inlog). Thijs ziet het in Curator Connect zelf als hij de naam intypt; wie er niet staat, krijgt op 4 jan een reactie onder een recente video met de demolink (door Thijs, klaargezette zin volgt), of valt af.

## Bereik per maker (run 13, GEZIEN 16 nov ±23:36 tot 23:40 UTC)
Vraag: wie geeft een onbekend spel de meeste ogen? Script `data/yt-bereik.py`, uitkomst `data/yt-bereik-2026-11-16.csv`: van 66 YouTube-kanalen uit deze lijst de abonnees en de laatste ±30 video's (curl). "Ons soort video" = titel met idle, incremental, desktop, taskbar, cozy, demo, fest, upcoming, wishlist, hidden gem, first look, you missed of overlooked. Per kanaal de mediaan van die video's, en die mediaan gedeeld door de abonnees.
**Bovenaan** (mediaan ons soort, keer abonnees): Dekaif 486.000 (2,5x), JGigs 427.500 (4,9x), Idle cub 191.000 (0,9x), Gohjoe 156.000 (0,8x), Dex 129.000 (0,4x), MaxPalaro 104.500, Easily Distracted 89.000 (2,5x), Nookrium 45.000, OKtrix 37.000 (0,8x), Fleurs 18.000, Gaming In The Wild 13.000 (0,8x).
**Onderaan, terwijl ze in de eerste ronde van run 4 stonden:** The Indie Brew 208, Maybe Sarisa 566, Conkbot 27, NextBigGames 1.400, CozyAriGames 1.500, Kosh Idle 1.600. Ook laag: Tchii 108, RinKa Plays 6, Phenexa 49, Higher Plain Games 268 (allemaal precies ons soort spel, bijna geen kijkers).
**Lezing:** passend en groot gaan hier niet samen; de kanalen die precies bureaubladspellen recenseren zijn bijna allemaal klein. De lijstmakers met "upcoming" en "hidden gems" (Easily Distracted, OKtrix, Fleurs, Gaming In The Wild) zitten ertussenin en nemen onbekende spellen op, dus die passen bij de paginadag. Grote kanalen (Idle cub, Dex, Gohjoe, JGigs) maken één spel per video en kiezen zelf, dus die krijgen een demosleutel zonder verwachting.
**Grenzen van deze meting (eerlijk):** woorden in de titel zijn grof (bij CallMeCarson telt "GTA 6 First Look" mee, bij GameStar een nieuwsvideo); 30 video's is een kort venster; bij kanalen met 1 tot 3 treffers is de mediaan wankel (Dekaif 2, JGigs 2, Gohjoe 3). Weergaven zijn geen kopers.

## Nieuwe kanalen via zoeken (run 13, GEZIEN 16 nov ±23:45 UTC, nummer 75 tot 86)
Omdat de paginadag maar 6 lijstmakers had, 14 zoektermen (upcoming idle, upcoming cozy wishlist, desktop companion, taskbar games, idle games while working, upcoming incremental, ...) op de YouTube-zoekpagina, video's van hooguit 12 maanden, kanalen die nog niet in deze lijst stonden: 114 kanalen (`data/yt-lijstmakers.py`, `data/yt-lijstmakers-2026-11-16.csv`; veel ruis zoals tech en mobiel). 30 die bij ons passen gemeten met `data/yt-bereik.py` (`data/yt-bereik-nieuw-2026-11-16.csv`), contact gelezen met `data/yt-kanaal.py`. Gratis adressen (gmail) staan niet in de repo; Thijs kopieert ze van het kanaal.
| # | Wie | Abonnees | Ons soort video haalt (mediaan, keer abonnees) | Voorbeeld | Route | Wanneer |
|---|---|---|---|---|---|---|
| 75 | Kaganath (@Kaganath) | 30,3K | 108.500 (3,6x) | "5 Upcoming Cozy Games That ARE NOT Farm Sims" 522.714; zijn plank is cozy waarin je slecht bent ("5 Cozy Games Where You Can Be EVIL" 339.000), maar maar 3 "upcoming"-lijsten in 11 maanden | geen adres in tekst, knop nakijken | **paginadag** (mail uitgeschreven) |
| 76 | GameGen (@gamegen7745) | 158K | 112.000 (0,7x), 23 van 30 titels lijsten | "Top 16 Upcoming Cozy Games 2026" 371.748 | geen adres in tekst | **paginadag** |
| 77 | Get To It (@Get_To_It) | 90,4K | 47.000 (0,5x) | "The Most Wishlisted Steam Games" 187.000 | zakelijk gmail in kanaaltekst | **paginadag** |
| 78 | Sloth Vibes (@SlothVibes-YT) | 3,65K | 6.800 (1,9x) | "Cozy Games to Play When You're Too Tired for Anything Else" 87.000; "10 Cozy Idle Games You Need to Try!" | **hello@theslothvibes.com** (eigen domein) | **paginadag** |
| 79 | The Backlogs (@TheBacklogs) | 652K | 222.000 (1 treffer, wankel) | "18 Cozy Games You Can Relax With" | geen adres in tekst | festweek, zonder verwachting |
| 80 | Dragoon (@Dragoon45) | 1,05M | 724.000 (2 treffers) | "The Most Addicting Idle Game" 979.000, "Top 100 Idle Games" 469.961 | geen adres in tekst | demo af, sleutel zonder verwachting |
| 81 | DangerouslyFunny (@DangerouslyFunny) | 2,78M | 622.500 (2 treffers) | "This Is Absolutely One Of The Best Incremental Games Ever" 2.301.295 | zakelijk adres van zijn manager (onder "email address", niet in de tekst) | demo af, zonder verwachting |
| 82 | The Spiffing Brit (@thespiffingbrit) | 4,5M | 1.300.000 (2 treffers) | "ORC INCREMENTAL Is A Perfectly Balanced Game ..." 1.410.359 | zakelijk gmail in kanaaltekst | na de lancering (zoekt "exploits" in volle spellen) |
| 83 | Insym (@Insym) | 1,25M | recente titels geen treffer; zoekhit "Playing New Incremental Games That Look MEGA Satisfying" 116.922 | Nederland, elke dag een video en stream | geen adres in tekst | demo af, zonder verwachting |
| 84 | Sifd (@Sifd) | 149K | 27.500 (0,2x), incrementals en autobattlers | "In This Wall-Defence Incremental YOU HAVE ONLY ARCHERS!" 36.000 | geen adres in tekst | demo af |
| 85 | The Cozy Gaming Club (@Cozygamingclub) | 16,1K | 8.200 (0,5x), 21 van 30 titels cozy | "The BIGGEST Month for New Cozy Games" 24.000 | gmail in kanaaltekst | begin februari (maandlijst) |
| 86 | Sir Eat Alot (@SirEatAlot) | 4,88K | 16.000 (3,3x), Task Bar Hero-gidsen | "TASK BAR HERO: Ultimate Guide Part 1" 109.919 | geen adres | na de lancering (gidsen) |
**Besluit (Sem):** Kaganath, GameGen, Get To It en Sloth Vibes erbij voor de paginadag; daarmee 10 kanalen op de paginadag (van de 4 zonder adres moet Thijs de knop "View email address" of een reactie gebruiken, dus eerst de 6 met adres). Waarom: Kaganath en GameGen maken precies de lijst "upcoming cozy" waar Hats in kan voordat er een demo is, met 100.000+ weergaven per lijst. Niet meegenomen ondanks de grootte: Linus, gameranx, Bozuse (algemene lijsten van grote spellen).
**Volgorde op de paginadag (run 13):** wat ons aandeel in een lijst is hangt af van hoeveel spellen erin staan: Kaganath (lijsten van 5) ±21.700 per spel, Easily Distracted ±7.000 tot 15.000, GameGen ±6.000, de rest onder 1.000 (rekensom in `festplan.md`, begroting). Dus eerst Kaganath en Easily Distracted.
**Grenzen:** zelfde als hierboven; bij Dragoon, DangerouslyFunny, Spiffing Brit en The Backlogs 1 of 2 treffers, dus de mediaan is eigenlijk één video. Een "knop" voor het zakelijke adres kan curl niet zien (YouTube toont die alleen na inloggen), dus "geen adres" betekent: niet in de tekst.

## TikTok: makers die bureaublad- en idle-spellen lieten zien (run 11, GEZIEN 16 nov ±21:42 UTC, nummer T1 tot T10)
**Hoe ik keek:** TikTok-zoek- en tagpagina's geven met curl geen video's (alles wordt pas in de browser geladen; 8 pagina's geprobeerd, 0 namen). Wel werkt: video's vinden met de zoekmachine (7 zoekopdrachten op tiktok.com naar Rusty's Retirement, Ropuka, Spirit City, Bongo Cat, "sits at the bottom of your screen", "games to play while working") en daarna het openbare profiel lezen met curl (volgers, aantal video's, bio). Zo is het "Open"-punt TikTok uit run 4 deels af. Adressen: alleen het soort; een adres op een bureau- of eigen domein staat in de bio en Thijs kopieert het daar zelf.

| # | Account | Volgers | Bewijs (video over ons soort spel) | Contact in bio | Kans |
|---|---|---|---|---|---|
| T1 | @cozyteagames | 711.600 (597 video's) | Rusty's Retirement ("This shouldnt interfere with my productivity", 4 jan 2024, **160.500 weergaven**), Ropuka twee keer, Feather Land ("Use this while you study/work"), Furry Company (gemarkeerd AD) | geen adres in bio | middel: groot en speelt precies onze plank telkens opnieuw; doet ook betaalde video's (AD), dus een gratis mail kan stil blijven |
| T2 | @cozywithronnie | 123.900 (876) | Ropuka "sits anywhere on your desktop" op de lanceerdag (31 jan 2025, **167.100 weergaven**, meer dan haar volgers) | bureau-adres in bio (management) | middel tot hoog: post op de lanceerdag met prijs erbij, dat is ons lanceermoment |
| T3 | @imjustjarrod | 53.200 (864) | Rusty "a cozy game that sits at the bottom of your screen while you work" (6 apr 2024, 9.659 weergaven) | zakelijk adres in bio ("Business inquiries") | middel: precies onze zin en een zakelijk adres, maar de video bleef klein |
| T4 | @cozyreni | 58.600 (874) | "This cozy game boosts your productivity" (26 aug 2025, 18.100 weergaven) | zakelijk adres in bio (eigen domein) | hoog: "I help you find YOUR next cozy game" |
| T5 | @cozyboardgames | 146.400 (886) | Rusty-demo "lives at the bottom of your screen", vóór de uitgave | geen adres | middel: speelde een demo, ons moment van 4 jan |
| T6 | @dailyalissa | 184.900 (1.061) | Spirit City als focushulp, "body doubling" | bureau-adres in bio | laag tot middel: productiviteit, geen kerker |
| T7 | @zelinka21 | 16.600 (473) | Spirit City, sleutel via **Keymailer** (staat in de video) | gratis adres in bio | middel, alleen met Pools; wel een les: makers van TikTok krijgen sleutels via Keymailer |
| T8 | @herrbanause | 35.500 (384) | "Der HYPE um die Bongo Cat" | gratis adres in bio | laag tot middel (Duits, "Geheimtipps") |
| T9 | @theymakegames | 1.665 (261) | Ropuka "sits anywhere on your screen" | eigen domein in bio | laag bereik, maar zet makers in het licht en vraagt erom |
| T10 | @rosy.ree | 4.641 (121) | Spirit City "always on my background while i work" | gratis adres in bio | laag |

Ter vergelijking, geen makers maar wel meetpunten: @wholesomegames 364.600 (al trailer-plek), @mister.morris.games (maker Rusty) 12.900, @conradicalgames (maker Desktop Defender) 18.300.

Weergaven per video gelezen uit de openbare videopagina (curl, `playCount`, GEZIEN ±21:50 UTC).

**Grootste vondst: op TikTok telt de video, niet het account.** @lemon.stones (346 volgers) zette op 27 sep 2026 een video over de demo van Character House ("This is not sponsored I just found the game spontaneously"): **318.900 weergaven, 41.900 likes**. Twee dagen later @astrolillyu ("you can make your OC's into cute desktop pets"): 3.672. Beide komen uit tekenaars- en OC-hoeken, precies wat ik in run 6 als GOK schreef over Character House (`character-house.md`). Gevolg: een makerslijst op volgers mist op TikTok het belangrijkste; wat gedeeld wordt is iets wat de speler zelf maakte of herkent. Voor Hats is dat de hoed op Gloop en de wrok van een held met een naam; de Postcard (Sanne) is het ding dat een speler zelf kan laten zien.

**Wat ik eruit haal:**
1. Op TikTok is de taal "sits at the bottom of your screen while you work" en "productivity", niet "idle" of "dungeon". Dat past bij de korte winkeltekst (Z5: soort en plek eerst). Voor Chris: dezelfde woorden in de koppen van @hatsofthefallen (bericht in `berichten/chris.md`).
2. Drie TikTok-makers (T2, T3, T4) hebben een zakelijk adres en posten over precies dit soort spel. **Besluit: T3 en T4 bij de mails op de dag dat de pagina live is (±8 dec), T2 op de lanceerdag in maart** (zij post op lanceerdagen en haalde daar 167.100), T1 en T5 met een demosleutel als de demo af is (18 dec). Waarom: zelfde regel als bij YouTube, eerst wie een openbaar zakelijk adres heeft en ons soort spel speelt.
3. **Keymailer** is een tweede route naast Curator Connect: daar halen makers zelf sleutels (T7 kreeg Spirit City zo). Prijspagina gelezen (curl, ±21:45 UTC, GEZIEN): "Get started free, add promotions and service when you need them", "Always free for content creators", geen bedragen; het makersdeel heet nu Partnier. Wat gratis precies inhoudt staat er niet (GOK: sleutels aanbieden gratis, gericht uitnodigen betaald). **Besluit: niet nu.** Waarom: Curator Connect van Valve is gratis, laat zien wie de sleutel gebruikte en vraagt geen nieuw account; Keymailer pas als Curator Connect na de demo weinig oplevert, dan als stap voor Thijs (account).
4. Eerlijk: 10 zoekopdrachten zijn geen volledige lijst. Ik vond vooral cozy-makers. Kerker- en idle-RPG-makers op TikTok vond ik niet: zoeken op Task Bar Hero en Deskrawl gaf alleen verzamelpagina's (vooral Portugees en Spaans) zonder namen. Die makers zitten voor ons op YouTube (groep A).
