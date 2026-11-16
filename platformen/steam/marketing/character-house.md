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
