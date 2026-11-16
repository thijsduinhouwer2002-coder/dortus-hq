# Steam-curatoren voor Hats of the Fallen (Sem, versie 1, 16 nov 2026)

Opdracht: fest-plan punt 2, deel Curator Connect. Curator Connect is de gratis weg van Steam om een sleutel aan een curator te geven, zonder mail. Wie een sleutel stuurt is Thijs (Steamworks, zijn inlog); niets verstuurd.

## Hoe ik keek (GEZIEN 16 nov 2026 ±13:40 UTC)
- De openbare lijst "Curators reviewing this game" van 12 winnaars en bijna-winnaars: Rusty's Retirement, Desktop Defender, Deskrawl, Tiny Pasture, Ropuka's Idle Island, Bao Bao's Cozy Laundromat, Desktop Survivors 98, TBH: Task Bar Hero, Black Cat Book Club, Desktop Raid, Cozy Mining, Spirit City: Lofi Sessions. Bron: `store.steampowered.com/curators/ajaxgetcurators/render/?filter=top_curators_reviewing&appid=...` (zonder inlog, met curl). Script `data/curatoren.py`, uitkomst `data/curatoren-bureaubladspellen-2026-11-16.csv` (alleen namen, links en getallen).
- Aantal curatoren per spel: Spirit City 190, Rusty 145, Tiny Pasture 105, TBH 48, Ropuka 41, Desktop Survivors 98 37, Bao Bao 31, Desktop Defender 23, Deskrawl 15, Desktop Raid 13, Black Cat Book Club 11, Cozy Mining 4. Samen **478 verschillende curatoren**, waarvan 298 in de laatste 60 dagen nog een recensie schreven.
- Per curator geeft Steam twee getallen: volgers, en "high value followers" (Valve's eigen telling van volgers die meetellen). Dat tweede getal gebruik ik als echtheidstoets.

## Belangrijkste les: de helft van de grote curatoren rond Tiny Pasture heeft nepvolgers
- Van de 105 curatoren van Tiny Pasture hebben er **50** meer dan 10.000 volgers maar minder dan 30% "high value". Voorbeelden: Game Chronicles Collective 32.574 volgers, 3.474 hoge waarde (11%); Democracy Brothers 27.189 / 3.569 (13%); KZ Gaming Group 24.185 / 2.715 (11%). Bij Desktop Raid zijn het er 6 van de 13. Ook Indie Signal (Steam-curator, niet het YouTube-kanaal) heeft 23.659 volgers waarvan 251 hoge waarde (1%).
- Echte curatoren zitten rond 80 tot 100%: Wholesome Games 132.320 / 107.407 (81%), SteamDB 77%, GamingTaylor 76%, The Cozy Gaming Club 89%.
- GOK over de oorzaak: een netwerk van curatorpagina's dat sleutels verzamelt via Curator Connect (bekend verschijnsel; sleutels komen dan soms op de grijze markt). Het kost ons alleen sleutels, maar het levert geen echte lezers.
- **Regel voor ons:** een curator krijgt alleen een sleutel als "high value" minstens 50% van de volgers is, of als hij precies ons soort spel bespreekt (lijst hieronder). Volgers alleen zegt niets.

## Eerste ronde: actief, echt, en speelt ons soort spel (18)
Gekozen op: recensie in de laatste 60 dagen, minstens 2 van de 12 spellen, of meer dan 1.000 echte volgers met een passend spel. Gesorteerd op hoeveel van onze 12 ze deden.
| # | Curator | Echte volgers (van totaal) | Van de 12 | Laatste recensie | Waarom |
|---|---|---|---|---|---|
| 1 | Desktop Games | 277 (295) | **11** (alle behalve Bao Bao) | 16 nov | bestaat alleen voor "games you can play without interrupting your work"; klein maar precies |
| 2 | Wholesome Games | 107.407 (132.320) | 5 | 9 nov | grootste in cozy; Rusty kwam in hun Wholesome Snack (blurb GEZIEN), ook Black Cat 9 nov. Ook showcase, zie makers #40 |
| 3 | The Cozy Gaming Club | 2.549 (2.852) | 5 | 12 nov | cozy, echte volgers |
| 4 | Eliani Plays | 573 (595) | 6 | 15 nov | indie, goedkoop, met TBH erbij (dus ook de gevechtskant) |
| 5 | frumpy & frands | 467 (515) | 5 | 13 nov | deed ook Desktop Survivors 98 |
| 6 | Is The Price Polished? | 3.947 (3.761) | 4 | 16 nov | prijs-curator; past als onze prijs laag is; deel 2 deed Deskrawl en Desktop Defender |
| 7 | Hidden Gems Review | 1.754 (2.469) | 3 (Deskrawl, Desktop Raid, Tiny Pasture) | 12 nov | de gevechtskant van het genre |
| 8 | VaporLens | 251 (244) | 3 (Deskrawl, Desktop Raid, TBH) | 14 nov | gevechtskant; vat reviews samen, pas na lancering nuttig |
| 9 | CozyAriGames | 41 (45) | 6 | 11 aug | is ook YouTube-maker #19 (first looks), dus één sleutel, twee kanalen |
| 10 | Higher Plain Games | 126 (125) | 3 (met Desktop Defender) | 14 nov | is ook YouTube-maker #4 |
| 11 | Tchii's gameplay | 130 (159) | 3 | 7 nov | is ook YouTube-maker #9 |
| 12 | The Indie Brew | 515 (545) | 3 | 8 jun | is ook YouTube-maker #15, heeft een openbaar adres |
| 13 | やぶから堂 | 31.419 (38.590) | 2 (Rusty, Tiny Pasture) | 10 nov | Japans, groot en echt; alleen met Japanse demo of Engelstalig spel zonder veel tekst |
| 14 | 游戏叙事批评 (Untame Cat) | 2.996 (5.493) | 3 | 15 nov | Chinees en Engels; alleen zinvol met Chinees |
| 15 | Ѕtеам 250 | 15.643 (19.001) | 2 | 16 nov | groot; let op de rare letters in de naam (nakijken vóór een sleutel) |
| 16 | GrabTheGames | 45.214 (96.748) | 1 (Desktop Defender) | 29 okt | groot, 47% echt, deed precies de dichtste concurrent |
| 17 | GamingTaylor | 42.972 (56.363) | 1 (Rusty) | 16 nov | "most underrated hidden gems" |
| 18 | Just Some Cozy Gaming | 1.624 (1.981) | 2 | 13 nov | cozy |

Niet in de lijst, wel gezien: SteamDB (42.485 echt, deed TBH) is een cijfer-curator, geen tip; Humble Bundle's Bundles en Achievement Scouts zijn lijsten van bundels en prestaties, geen lezers.

## Let op: een curator die AI-gebruik opspoort
**Does This Game Use GenAI?** (2.789 echte volgers van 2.912, laatste 27 okt) recenseerde Cozy Mining en TBH. De omschrijving: "I will be utilizing Steam's AI warning along with social media posts that indicate if a game is using generative AI". Dit gaat ons zeker ook vinden zodra de AI-melding op onze pagina staat. Dat is geen reden om te verbergen (dat mag niet en het komt toch uit), wel een reden om de melding eerlijk en precies te schrijven: wat AI deed en wat niet. Zie de correctie in `makers.md` punt 3 en het open punt voor de hoofdchat in `logboek.md` run 2. Gemeld in `berichten/hoofdchat.md`.

## Wanneer (voorstel, past in het plan van `makers.md`)
| Wanneer | Wat |
|---|---|
| pagina live (±8 dec) | eerste ronde 1 tot 12 volgen we op Steam (Thijs, met zijn account; kost niets) zodat we hun nieuwe recensies zien |
| vr 18 dec, demo af | Curator Connect: demosleutel aan 1 tot 12 en 16 tot 23 (zie "Tweede helft"), met één zin haak en de GIF. Curator Connect werkt per app; een aparte demo-app heeft eigen sleutels (GOK, nakijken in Steamworks door Thijs) |
| 8 jan | herinnering via Curator Connect aan wie de sleutel niet gebruikte: "the demo is in the Desktop Companion Fest" |
| na een doorbraak in de meetlat | 13 tot 15 (Japans, Chinees) als die talen in de demo zitten |

## Tweede helft: curatoren van kerkerspellen (run 3, GEZIEN 16 nov ±13:46 UTC)
Hats is half bureaubladspel, half kerker (helden met een wrok, `platformen/succes/onderscheid-hats.md`). Daarom dezelfde meting op zes kerkerspellen: Dungeon Keeper 2 (28 curatoren), Legend of Keepers (appid 978520), Dungeons 4 (80), Dungeon Tycoon (28), Dungeon Clawler (93), War for the Overworld (135). Samen 468 curatoren; uitkomst `data/curatoren-kerkerspellen-2026-11-16.csv`.

**70 curatoren deden spellen uit beide helften.** Dat zijn de beste kandidaten, want ze kennen allebei de werelden die Hats samenbrengt. Actief en echt:
| Curator | Echte volgers (van totaal) | Kerker | Bureaublad | Laatste |
|---|---|---|---|---|
| Is The Price Polished? (staat al als #6) | 3.947 (3.761) | Dungeon Clawler, War for the Overworld | 4 | 16 nov |
| Is The Price Polished: Part 2 | 739 (711) | Dungeon Tycoon, Dungeons 4, Legend of Keepers | Deskrawl, Desktop Defender | 16 nov |
| Hidden Gems Review (staat al als #7) | 1.754 (2.469) | Dungeon Clawler, Legend of Keepers | 3 | 12 nov |
| Hype or Yikes | 4.411 (4.342) | Dungeon Clawler | Rusty, Spirit City | 15 nov |
| Eliani Plays (staat al als #4) | 573 (595) | Dungeon Clawler | 6 | 15 nov |
| Big Boss Battle | 792 (1.057) | Dungeons 4, Legend of Keepers | Rusty | 30 okt |
| Pirate Loot | 321 (422) | Dungeon Keeper 2, Dungeon Tycoon | Rusty, Spirit City | 5 nov |
| Yee or Nee | 134 (141) | Dungeon Clawler, Dungeon Tycoon | Desktop Defender, Rusty | 12 nov |
| Tchii's gameplay, Higher Plain Games (staan al als #10, #11) | | Dungeon Clawler | 3 | nov |

**Groot en echt, alleen kerker** (lage kans, want ze doen vooral bekende spellen; wel één sleutel waard na een doorbraak): Just Good PC Games 372.549 echt (van 604.185), Original Curators Group 81.396 (163.465), Yah or Nah 53.830 (61.210), Gaming Masterpieces 26.097 (31.880), TechRaptor 23.046 (34.108, ook een nieuwssite).

**Wat dit toevoegt aan de eerste ronde:** Hype or Yikes, Is The Price Polished: Part 2, Big Boss Battle, Pirate Loot en Yee or Nee erbij (nummers 19 tot 23). De eerste ronde wordt daarmee **23 curatoren**. En de regel blijft: Is The Price Polished, Hidden Gems Review en Eliani Plays doen beide helften, dus die drie eerst.

## Open
- Hoeveel curatoren van de 12 spellen een gratis sleutel kregen: het veld `received_for_free` geeft Steam alleen voor de laatste paar recensies per curator, dus mijn telling (kolom `gratis_gekregen`) is te laag en zegt niets. Niet gebruiken.
- ~~Curatoren van de kerkerspellen.~~ Gedaan, zie "Tweede helft" hierboven.
- Of de curatoren een mailadres of Curator Connect-instellingen openbaar hebben (sommigen schrijven "send keys via Curator Connect only"): per curator de pagina lezen vóór 18 dec.
