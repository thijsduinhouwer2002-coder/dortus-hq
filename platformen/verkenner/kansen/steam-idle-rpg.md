# Productkans Steam: een eerlijke, gepolijste idle-RPG voor in de hoek van het scherm

Vera, verkenner, 9 nov 2026 run 13:31 (Amsterdam). Voor Sanne (Steam, geparkeerd tot 15 nov) en Hans.

## In het kort
- **Cijfer 6, advies: ja als eerste product voor Steam, als Steam doorgaat.** Binnen de Desktop Companion-apps is de idle-RPG (helden of een team dat onderaan je scherm vecht en buit verzamelt terwijl jij werkt) de soort met de **meeste vraag** van 2026 en de **zwakste top**.
- Vraag: van de 27 betaalde idle-RPG's die in jan t/m sep 2026 uitkwamen haalde **67% 10+ reviews en 26% (7) 100+**. Mediaan 25 reviews. Idle-RPG heeft de hoogste mediaan en de meeste reviews; alleen vriendin/anime haalt een hoger aandeel (73% 10+, 45% 100+), maar met 11 apps (GEZIEN). De grootste van de soort is zelfs gratis: TBH: Task Bar Hero (mei 2026), 8.813 reviews, 62% positief (GEZIEN door de controleur).
- Zwakke top: de meeste reviews (en dus waarschijnlijk verkopen) gaan naar matig beoordeelde spellen (onder 80%; 74% heet op Steam "Mostly Positive", niet slecht). Gewogen naar reviews is maar **74% positief**, en **85% van alle reviews** in deze soort hoort bij spellen onder 80% positief. Bij huisdier-apps en focus-apps is dat 3% en 7% (GEZIEN).
- Wat kopers missen, volgens de negatieve reviews van de 10 grootste: een eerlijke voortgang zonder muur (ook na 100+ uur), geen betaalde helden of handel in buit, geen bugs of verloren saves, goed Engels (GEZIEN, 89 negatieve reviews met woordtelling geteld, van 6 spellen ook zelf gelezen).
- Het gat in één zin: **mensen kopen massaal desktop-idle-RPG's en spelen er honderden uren in, maar de spellen die ze krijgen zijn onaf, slecht vertaald, met een grindmuur of betaalde extra's; een eerlijk, stabiel en goed uitgebalanceerd spel voor één prijs heeft weinig concurrenten: alleen Book of Fei (92%, 357 reviews) is goed beoordeeld (GOK, op basis van de tabel).**
- Grootste risico: de soort loopt nu vol (2 tot 5 per maand in het voorjaar, 9 in september, 18 in oktober) en zo'n spel moet er goed uitzien. Daarom 6 en geen 7.

## Hoe gemeten (GEZIEN)
- Alle 405 apps met het Steam-label Desktop Companion (tag 1320952) via de openbare zoekpagina, met reviews en % positief (stand 9 nov 2026). Daarna per app de winkelpagina (labels, korte tekst, maker en uitgever) en de laatste aankondigingen via de open ISteamNews-API. Script `data/steam-kans-haal-script.py`, data in `data/steam-kans-2026-11-09/`.
- Soort per app op titel plus korte tekst, eerste treffer in een vaste volgorde (idle-RPG, vriendin/anime, focus, vissen, huisdier, tuin, winkel/fabriek, kamer/muziek, toetsenteller, overig). Script `data/steam-kans-soort-script.py`. Ongeveer de helft van de 27 is volgens de controleur geen echte idle-RPG (onder meer Deadline Savior, WinMon, Motivation Monsters, My Pocket Paradise, Tiny Monster Haven, CompaDesk, My Shelter, Your Furry Mother). Met alleen de echte 14 is het 57% 10+, 43% 100+, 74% gewogen positief en 89% van de reviews bij spellen onder 80%. De conclusie wordt er sterker van (GEZIEN). Gratis apps tellen niet mee in de tabel.
- Negatieve reviews: de 10 meest nuttige per spel van de openbare communitypagina (steamcommunity.com, robots.txt staat het toe), met een woordtelling per soort klacht. Script `data/steam-kans-klachten-script.py`, teksten in `klachten.json`. De woordtelling is grof; ik heb de teksten van 6 spellen ook zelf gelezen.
- **Grens:** Steam toont onder 10 reviews geen getal ("0" is 0 tot 9). De exacte reviewteller (appreviews) is vanaf hier niet bereikbaar. Reviews naar verkopen: ±30 verkopen per review (DERDEN, zie `voorstellen/steam-bureaublad.md`).

## Vraag per soort (betaalde apps uit jan t/m sep 2026, GEZIEN)
| Soort | Apps | Mediaan reviews | 10+ | 100+ | Reviews samen | Gewogen % positief | Deel reviews bij spellen onder 80% |
|---|---|---|---|---|---|---|---|
| **Idle-RPG / gevecht** | 27 | **25** | **18 (67%)** | **7 (26%)** | 3.793 | **74%** | **85%** |
| Huisdier / dier verzorgen | 31 | 14 | 18 | 4 | 2.679 | 95% | 3% |
| Vriendin / anime-figuur | 11 | 22 | 8 | 5 | 2.262 | 91% | 26% |
| Focus / werkhulp | 40 | 14 | 24 | 4 | 2.131 | 94% | 7% |
| Tuin / boerderij | 15 | 11 | 10 | 2 | 569 | 87% | 23% |
| Vissen | 14 | 0 | 4 | 0 | 94 | 91% | 0% |
| Winkel / fabriek / stad | 6 | 13 | 4 | 1 | 188 | 85% | 7% |
| Overig (ook toetsenteller, kamer) | 35 | 0 | 13 | 1 | 540 | 86% | 18% |

Lezen: in huisdier, focus en tuin zijn de beste spellen al goed (95%, 94%) en verdeelt de vraag zich over veel apps. Bij vissen gaat bijna alles naar de oude leiders (Cast n Chill 5.344 reviews, 95%, nog bijgewerkt; Cornerpond 1.772); nieuwkomers halen daar niets (mediaan 0). Alleen bij de idle-RPG is de vraag groot én de kwaliteit laag.

## De top 3 (en verder) van de idle-RPG en hoe sterk ze zijn (GEZIEN)
| Spel | Uit | Prijs | Reviews | % positief | Maker / uitgever |
|---|---|---|---|---|---|
| TBH: Task Bar Hero | mei 2026 | gratis | 8.813 | 62% | Nugem Studio / Tesseract Studio. Verreweg de grootste, gratis met betaalde extra's (controleur, live). Ook gratis: My Party Is Grinding (731, 44%), Crusaders Quest: Mini (526, 80%). |
| Desktop Defender | nov 2025 | $4,99 | 1.789 | 92% | Conradical Games / Poysky. Torenverdediging, geen buit-RPG. Sterk en bijgewerkt (2 nov). |
| Your Big, Cute Monster Farm | nov 2025 | $7,99 | 1.215 | 77% | KaiPlay / Gamersky. Klachten: kosten schieten omhoog (5.000 naar 10 miljoen), eindeloze grind. |
| Tap Tap Loot | apr 2026 | $6,99 | 868 | 76% | Turtle Knight / Irox. Klachten: bugs, grind. |
| Duelist: Idle Expedition | okt 2026 | $8,99 | 735 | 77% | One Interactive / Infini Fun. Al 735 reviews in een maand. |
| Desktop Raid | mrt 2026 | $8,99 (nu $5,39 in de uitverkoop) | 702 | 75% | Lee_Studio / Lee_Studio + Gamersky Games. Klachten: "meer een bèta", vertaling, bugs, save weg na 86 uur. |
| Lootborne | sep 2026 | $1,99 | 479 | 57% | Fate Rate, zelf. Klachten: progressie na honderden uren dicht, valsspelers in de ranglijst. |
| Deskrawl: Idle ARPG | sep 2026 | $6,99 | 472 | 69% | First Day Games / First Day Games + Gamersky Games. Klachten: zeldzame buit valt nooit (0 in 230 uur), buit te koop op de Steam-markt. |
| Crusaders Quest: Hero Town | mrt 2026 | $6,99 | 362 | 79% | CQ Labs / LoadComplete. Klachten: nieuwe helden als betaalde DLC. |
| Book of Fei | feb 2026 | $2,99 | 357 | 92% | TAO Studio, zelf. Goed beoordeeld, laatst bijgewerkt 28 jul. |
| Incremental Infinity | jul 2026 | $4,99 | 166 | 57% | Rablo Games, zelf. Klachten: te weinig inhoud. |

Volgens de harde regel: de nummer één van de buit-RPG's is geen groot bedrijf met duizenden goede reviews. De echte leiders (Monster Farm, Tap Tap Loot, Duelist, Desktop Raid) zitten op 75 tot 77%. Desktop Defender is sterk, maar is torenverdediging; daar gaan we niet tegenaan. De grootste in de soort is gratis (TBH, 8.813 reviews, 62%). We concurreren dus ook met een gratis spel; "één prijs, geen betaalde kracht" moet daartegen opwegen (GOK). Let op: Desktop Raid belooft zelf al "no grind"; de belofte alleen is geen onderscheid, het moet echt waargemaakt worden.

**Kleine makers:** 18 van de 27 idle-RPG's van jan t/m sep zijn helemaal zelf uitgegeven (maker = enige uitgever). Daarvan haalden er 11 10+ reviews en 3 100+ (Lootborne 479, Book of Fei 357, Incremental Infinity 166). Desktop Raid en Deskrawl hebben Gamersky Games als mede-uitgever (ook uitgever van Monster Farm), WinMon heeft Smilegate (GEZIEN). Desktop Raid met 702 reviews is bij ±30 verkopen per review ±21.000 verkopen, ruwweg $55.000 netto voor een kleine maker met een uitgever (GOK, rekensom; de prijs wisselt door kortingen).

## Wat kopers klagen (10 grootste betaalde spellen onder 80%, 89 negatieve reviews, GEZIEN; Goblin Attack en Desktop Hellfarmer leverden maar 5 per spel)
| Soort klacht | In hoeveel van de 10 spellen | Reviews met de klacht |
|---|---|---|
| Balans, grindmuur, te traag | 10 | 30 |
| Te weinig inhoud of eentonig | 9 | 23 |
| Betaalmodel: betaalde helden, DLC, handel in buit | 6 | 19 |
| Neemt scherm of pc in beslag | 7 | 9 |
| Bugs, crash, save weg | 7 | 15 |
| Onaf, "bèta", te vroeg uitgebracht | 5 | 8 |
| Slechte vertaling | 3 | 7 |
| Te veel klikken voor een idle-spel | 6 | 8 |
(Woordtelling, grof; een review kan meer klachten hebben.) Opvallend: kopers spelen deze spellen 80 tot 700+ uur. Ze blijven, maar ze zijn boos.

## Wie betaalt, hoeveel, hoe vaak
- Pc-spelers die werken of studeren achter hun scherm en een spel op de achtergrond willen. Eenmalig, mediaanprijs $4,99 (GEZIEN, 27 apps).
- Rekensom (GOK): mediaan van de soort 25 reviews ≈ 750 verkopen ≈ $1.900 netto in 2 tot 10 maanden; een van de vier haalt 100+ reviews ≈ 3.000+ verkopen ≈ $7.500+ netto. Eén keer per koper, dus het geld komt vooral in de eerste maanden. Extra: een betaalde uitbreiding met nieuwe inhoud (geen helden met meer kracht, zie hieronder) en korting in de Steam-uitverkopen.
- Bewijs dat zulke mensen betalen: de 3.793 reviews van 2026 in deze soort, bij spellen van $1,99 tot $8,99 (GEZIEN).

## Eerste productidee (GOK)
Een idle-RPG die onderaan het scherm loopt, met als belofte: **"Eén prijs, geen muur, geen betaalde kracht."**
- Een klein team van helden trekt door kerkers terwijl jij werkt; buit, sterker worden, nieuwe gebieden. Ook voortgang als het spel uit staat.
- Wij doen beter: (1) een voortgang die we vooraf uitrekenen met een simulatie van honderden uren, zodat er geen muur komt (dat kan de ploeg goed: rekenen en testen op GitHub Actions); (2) geen betaalde helden, geen handel op de Steam-markt, geen ranglijst om vals te spelen; (3) saves die niet verdwijnen (Steam Cloud plus reservekopie), weinig processor; (4) Engels en Nederlands goed geschreven.
- Prijs $4,99 tot $6,99. Later een betaalde uitbreiding met nieuwe gebieden en verhalen, nooit met kracht.
- Uiterlijk is het halve werk: pixelart, met Daan vanaf dag één. Met AI gemaakte plaatjes moeten op Steam gemeld worden (DERDEN, zie voorstel Steam). Een vrije of gekochte pixelset is ook een route.
- Eerlijk geld: geen loot boxes of andere kansspellen voor geld.

## Risico's
- **Het loopt vol:** idle-RPG's per maand in 2026: feb 2, mrt 2, apr 4, mei 3, jun 4, jul 5, aug 7, sep 9, **okt 18**, nov (tot 9 nov) 6 (GEZIEN, alle prijzen). Van de 14 betaalde van oktober hebben er na ±5 weken al 7 10+ reviews, dus de vraag houdt voorlopig bij. Maar over een paar maanden kan het anders zijn.
- **Bouwtijd:** een goed spel met inhoud voor 100+ uur is meer dan 1 tot 2 weken; eerder 3 tot 6 weken (GOK). De kopers zijn kritisch op onafheid; liever later en af.
- **Gratis concurrent:** TBH (gratis, 8.813 reviews) trekt de grootste groep; kopers moeten een reden zien om te betalen.
- **Steam zelf:** $100 per app en een Steamworks-account (geparkeerd door Thijs tot 15 nov, zie besluiten 8 nov).
- **Smaak:** het gevoel van een spel kunnen we niet zelf spelen; wel meten met een simulatie en een speeltest door mensen (Thijs of vrienden).

## Advies
Ja, als Steam op 15 nov doorgaat: dit is het eerste product dat ik Sanne zou voorstellen. Het past bij de koers (mensen betalen al, bewezen in een hele lichting, top zwak). Een focus-app (het idee in het oude voorstel) heeft juist een sterke top (Virtual Cottage 2, 733 reviews, 97%; Focus Grove 197, 96%; Spirit City 9.227, 97%) en is daarom minder goed.

## Herhaalmeting
Rond 9 dec: `python3 -I data/steam-kans-haal-script.py <nieuwe map>` en dan `data/steam-kans-soort-script.py`. Kijk of de mediaan van de 14 betaalde idle-RPG's van oktober (nu 6,5 na ±5 weken) richting 25 groeit en of er een nieuwe sterke leider (85%+ met 500+ reviews, betaald of gratis) bij komt. Komt die er, dan zakt dit naar 5.

## Nakijken
Controleur akkoord met correcties (9 nov): soorttabel, klachtentabel en 4 spellen live nagerekend en gelijk. Verwerkt: gratis TBH als grootste toegevoegd, kleine makers 18 in plaats van 21 (Gamersky als mede-uitgever), prijs Desktop Raid, strengere soortindeling (26% wordt 43%), "geen concurrent" afgezwakt, reviews zijn geen verkopen, mediaan focus 14, herhaalmeting scherper. Cijfer 6 blijft.
