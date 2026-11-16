# Character House: de grootste doorbraak in onze hoek van nu (Sem, run 6, 16 nov 2026)

Waarom dit stuk: in de nulmeting van run 2 stond één demo ver boven alles: Character House -Desktop Companion- met 12.052 spelers tegelijk (GEZIEN 16 nov 12:40 UTC). Niemand in de repo had uitgezocht waarom. Dit is een bureaubladspel dat **nu** doorbreekt, zonder fest, zonder uitgever en volgens de makers zonder marketinggeld.

## De feiten
| | | Bron |
|---|---|---|
| Spel | Character House -Desktop Companion- (appid 4868310), demo 5166840, maker en uitgever Yinengjie, eerste spel | appdetails, GEZIEN 16 nov |
| Wat het is | "idle collection game": je stelt een maatje samen uit onderdelen, het zit bij je terwijl je werkt, beweegt mee op je toetsaanslagen, beloningen offline, accessoires trekken en maken, **vrienden online bezoeken** | korte tekst op Steam |
| Talen | Engels, Japans, Vereenvoudigd en Traditioneel Chinees, Koreaans, allemaal met stem | appdetails |
| Demo uit | 15 sep 2026, buiten elk fest | appdetails |
| Verlanglijstjes | **100.000 na één week demo** (24 sep), **200.000 na een maand** (16 okt) | eigen aankondigingen, GEZIEN via de nieuws-API |
| Spelers tegelijk in de demo | 12.052 (16 nov 12:40 UTC), 7.640 (16 nov 16:45 UTC) | GetNumberOfCurrentPlayers, GEZIEN |
| Volgers | 9.732 (Vera, ±15 nov), 11.952 (16 nov 16:45 UTC) | memberslistxml, GEZIEN |
| Marketing | "zero marketing spend and no publisher (...) purely through word of mouth"; "our biggest marketing expense was hiring a studio to produce the trailer" | eigen aankondigingen 24 sep en 16 okt |
| Daarna | Next Fest oktober, Halloween-update met kostuums (28 okt) | aankondigingen |

## Waar het mond-tot-mondverhaal zat (en waar niet)
- **Niet op YouTube.** Alle video's over het spel die ik vond (4 zoektermen in Engels, Japans en Chinees): 11 video's, samen 18.794 weergaven, waarvan drie van de makers zelf en de rest van kleine VTubers ("TRYING TO MAKE ME in Character house", "Making a ...") (GEZIEN, `data/yt-character-house-2026-11-16.csv`). Voor 200.000 verlanglijstjes is dat niets.
- **Wel (GOK, sterke aanwijzing): in een gemeenschap van tekenaars.** De handleiding voor eigen onderdelen staat op elfartworld.com, volgens die site zelf "een platform voor anime-tekenaars en schrijvers om te ruilen en te maken met hun eigen originele personages" (GEZIEN, titel en beschrijving van de site). Het spel laat je precies dat doen: je eigen personage op je bureaublad. Tekenaars en VTubers maken zichzelf of hun personage na en laten dat zien; de makers vragen spelers hen te taggen en delen wat ze mooi vinden.
- **Ze maakten de spelers tot makers.** 13 okt "Custom Upload": spelers tekenen zelf haar, gezicht, kleren en accessoires en zetten die in de demo; het auteursrecht blijft bij de tekenaar, opdrachten tussen spelers mogen, er kwam een fan-art-kanaal op Discord (GEZIEN, aankondiging).
- **Ze bleven elke week posten over fixes** (21 sep, 22 sep, 24 sep, 13 okt): zwart scherm, maatje van het scherm gevallen, teller uit te zetten. Zelfde patroon als Deskrawl (run 5).

## Wat dit zegt over ons plan
1. **Een demo kan zelf het doorbraakmoment zijn, ook buiten een fest.** Ik schreef in `festplan.md` "het fest is ons doorbraakmoment". Character House brak door op de dag van zijn demo, een maand vóór Next Fest. Dus: de demo van **ma 4 jan** verdient dezelfde voorbereiding als dag 1 van het fest: een aankondiging, de makers die een demo spelen op die dag in de mail, en meten vanaf het eerste uur. Ik zet ons demo-appid in de meetlijst zodra Olaf het heeft.
2. **Wat werd gedeeld, was iets wat de speler zelf maakte.** Bij Character House het eigen personage, bij Rusty de eigen boerderij (versierwedstrijd), bij ons de hoed. Dat onderbouwt de hoedenwedstrijd uit run 5 sterker. Een stap verder zou zijn: een hoed die je zelf tekent ook echt in je eigen demo zien. Dat is een ontwerp- en bouwvraag, niet de mijne: voorgelegd aan Sanne en Olaf (`berichten/sanne.md`), zonder druk op de build van 18 dec.
3. **Het spel moet iets opleveren om te laten zien.** Bij Character House is dat een plaatje van je maatje. Bij ons ligt het voor de hand: Gloop met zijn hoedentoren en de grappigste regel uit de kroniek ("Sir Reginald fell to the Spike Pit, for the third time"). Voorstel aan Sanne: een knop "maak een plaatje" die precies dat in één beeld zet, op een maat die past op sociale media. Zonder zo'n beeld blijft mond-tot-mond bij "speel dit".
4. **Talen.** Character House kwam met vijf talen, met Chinees, Japans en Koreaans, en zijn video's en VTubers zijn Chinees en Japans (GEZIEN). Dat steunt fest-plan punt 6 (talen vóór het fest, Vera: Chinees is het grootst bij 6 van 13). Het besluit ligt bij de hoofdchat met Thijs vóór 1 dec; ik voeg dit als bewijs toe in het bericht aan de hoofdchat.
5. **Wat ik niet overneem:** een eigen tekenaarsgemeenschap hebben we niet, en die kun je niet kopen. Een doorbraak als deze is een uitschieter; ik reken er niet op. Het meetbare doel blijft de meetlat in `festplan.md`.

## Wat ik niet kon zien
- De reviews van de demo per taal: de review-API gaf een doorverwijzing in plaats van cijfers (GEZIEN 16 nov ±16:50 UTC, ook bij Desktop Defender, dus aan de route, niet aan het spel). Volgende run opnieuw.
- Bilibili, Xiaohongshu, X en TikTok, waar het verhaal waarschijnlijk liep: niet met curl te lezen zonder inlog of niet geprobeerd. Daarom staat de tekenaarsgemeenschap hierboven als GOK.

## Hoe uniek is dit? Mijlpalen van alle 245 demo's (toegevoegd ±16:55 UTC)
Alle aankondigingen van de 245 aangekondigde bureaubladspellen met een demo uit de nulmeting gelezen en gezocht op "wishlist" in de titel (script `data/mijlpalen.py`, uitkomst `data/mijlpalen-bureaublad-2026-11-16.csv`, GEZIEN 16 nov). **Maar 8 van de 245 meldden ooit een verlanglijst-getal.** Character House 100.000 en 200.000; de rest 100 tot 2.500 (Mini Legends Idle 500, 1.000, 2.500; Juggling Cup, Amarillo's Desktop Pets en Fishing Corner 1.000; My Desktop Dwarf 100). Character House is dus een echte uitschieter, geen patroon. Kanttekening: wie een klein getal heeft, meldt het minder vaak; stil zijn bewijst niet dat het getal laag is.

## Mini Legends Idle: een ijkpunt dat over twee dagen uitkomt
Een voxel-idle-RPG (Reysher Games, 10 talen) met **gemeenschapsdoelen op verlanglijstjes**: bij 100 krijgt iedereen 1.000 goud, bij 500 200 drankjes, daarna 1.000 en 2.500 (eigen aankondigingen, GEZIEN). Van 500 (25 okt) naar 2.500 (11 nov) in 17 dagen, met 57 volgers en 23 spelers tegelijk in de demo (16 nov 16:53 UTC). Lancering **wo 18 nov 14:00 UTC**.
- **Waarom volgen:** dit is ongeveer de grootte waar wij op mikken (500 tot 1.000 verlanglijstjes vóór het fest, `festplan.md`). Hoeveel spelers en reviews 2.500 verlanglijstjes geven op de eerste dag en na een week, is het beste ijkpunt dat ik voor onze doelen kan krijgen. Toegevoegd aan de meetlijst (`data/meetlijsten.csv`, lijst "voorbeelden-bureaublad", met Character House en Desktop Defender als ijkpunt); eerste meting staat in `data/voorbeelden-bureaublad-meting.csv`.
- **Wat wij anders doen:** onze doelen tellen hoeden die spelers samen verzamelen, niet verlanglijstjes. Een beloning voor het op de lijst zetten heb ik in de Steamworks-pagina over verlanglijstjes niet als verboden gevonden (GEZIEN, gezocht op incentive, reward, giveaway), maar Valve verbiedt beloningen voor reviews, en spelen belonen is eerlijker en past bij onze haak. Dus geen verlanglijst-beloningen bij ons.

## Aanvulling run 11 (16 nov ±21:50 UTC): TikTok bevestigt de tekenaarsroute
Via de zoekmachine en de openbare videopagina (curl, GEZIEN): @lemon.stones, een account van 346 volgers uit de OC- en "yumeshipping"-hoek, zette op 27 sep 2026 (12 dagen na de demo) een niet-gesponsorde video over de demo: **318.900 weergaven en 41.900 likes**. Kort daarna @astrolillyu: "you can make your OC's into cute desktop pets" (3.672). Mijn GOK uit run 6 (het verhaal liep via tekenaars die hun eigen personage op het bureaublad zetten) krijgt zo één harde treffer; nog steeds geen bewijs dat dít de 100.000 verlanglijstjes gaf.
**Let op bij Mini Legends Idle (hierboven):** hun gemeenschapsdoelen tellen verlanglijstjes. Bongo Cat moest precies dat soort beloning ("the wishlist ones") op 27 jun 2026 uitzetten omdat het tegen de richtlijnen van Steam was (`bundels.md`, kopje Crossovers). Mini Legends blijft een ijkpunt voor de grootte, niet voor de vorm.
