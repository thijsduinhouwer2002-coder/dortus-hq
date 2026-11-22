# Iets erbij naast Het Hol (opdracht Thijs 13 nov 14:10)

Vera, eerste versie 13 nov 2026, run 16:16 (Amsterdam). Uiterlijke datum voor de eerste versie was ma 16 nov 12:00. Controleur: zie onderaan.

Labels: GEZIEN (zelf gemeten), DERDEN (bron), GOK (schatting).

## Advies in vier zinnen
1. **Bouw een klein betaald spelletje voor Garmin-horloges met Gloop uit Het Hol, in Blender gerenderd** (kandidaat 1, cijfer 6). Betaalde spelletjes doen het op Garmin beter dan andere betaalde apps: van de nieuwe betaalde spellen van kleine makers die niet eerst gratis waren haalt ±58 tot 61% de 100+ en ±16 tot 21% de 1.000+ downloads, tegen 42% en 11% voor alle betaalde apps (zelfde opbouw). Het bewijs is dun (±31 spellen) en de nieuwste lichtingen halen veel minder, dus de verwachting voor de eerste maand is klein.
2. Maak met dezelfde plaatjes een betaalde wijzerplaat (kandidaat 2, cijfer 5): een paar dagen extra werk, kleiner geld, extra zichtbaarheid en reclame voor Ebb en Het Hol.
3. Kandidaat 3 (een Blender-add-on die 3D-figuren omzet in sprites, op Superhive, cijfer 4) is alleen reserve: het bewijs is dun en geld hangt aan de Superhive-aanvraag die nog loopt.
4. **Niet doen: 3D-modellen of assetpakketten verkopen op Superhive.** Van 2.199 betaalde modellen van 0 tot 7 maanden oud heeft ±0,5% 10 of meer verkopen; er komen ±1.150 modellen per maand bij (GEZIEN, vandaag).

Waarom Garmin voor de top 2: de opdracht vraagt geld vanaf dag 1 zonder KvK. Bij Garmin betaalt de koper vóór het downloaden en is er geen proefperiode (forum Garmin, zie `platformen/garmin/concurrenten-2026-11-13.md` punt 7), het verkopersaccount bestaat en Ebb zit al in de keuring. JetBrains heeft een verplichte proef van 30 dagen, Steam vraagt een tweede fee en weken wachten, Obsidian heeft geen kassa (Rollwright: 0 verkopen), Superhive wacht nog op goedkeuring.

## Hoe gemeten
- Garmin: eigen analyse van de dataset van 9 nov (6.244 apps zonder wijzerplaat uit de open winkel-API, `data/garmin-niet-wijzerplaten-2026-11-09.json.gz`) en die van 6 nov (27.935 apps sinds juni 2025, met wijzerplaten, `data/garmin-nieuw-sinds-jun2025-2026-11-06.json`). Vandaag alle reviews gelezen van de 42 betaalde spellen uit jan t/m 15 aug 2026 (`data/garmin-spellen-gratis-eerst-script.py`, uitkomst `data/garmin-spellen-gratis-eerst-2026-11-13.jsonl`). Spellen = categorie 206 in de API.
- **Correctie op eerder werk:** in de dataset van 9 nov betekent `pay=1` niet "betaald in de winkel" maar "gratis, ontgrendelen buiten de winkel" (paymentModel 1; Caffeine Tracker noemt zichzelf "Free to use. Optional one-time Premium unlock", GEZIEN; controleur zag hetzelfde bij 4 andere). Niet altijd: 46 van de 807 apps met pay=1 hebben ook een winkelprijs (37 van RiversideArt). Betaald in de winkel is: het veld `pricing` heeft een prijs. Alle cijfers hier gebruiken `pricing`. Eerdere stukken die `pay` als "betaald" lazen (onder meer de tabel met zwakke betaalde apps in `kansen/garmin-zwakke-nummer-een.md`) moeten worden nagekeken.
- Superhive: 2.213 modelpagina's uit de categorie 3D-modellen (elke 3e lijstpagina van 1 tot 150 en elke 6e van 151 tot 417, nieuwste eerst), met verkoopteller (Superhive toont die vanaf 10). Script `data/superhive-modellen-script.py`, data `data/superhive-modellen-2026-11-13.jsonl.gz`. Add-ons uit de meting van 9 nov (`data/superhive-nieuwe-addons-2026-11-09.jsonl`).
- Geen onderzoeker-agent; wel een controleur (zie onderaan).

## Betaalde Garmin-apps in de winkel, eerste goedkeuring 1 jan tot 15 aug 2026 (GEZIEN)
| Soort | Aantal | Mediaan | 100+ | 1.000+ |
|---|---|---|---|---|
| Betaald in de winkel, alle soorten | 241 | 10+ | 46% | 10% |
| Gratis, ontgrendelen buiten de winkel | 164 | 100+ | 74% | 17% |
| Gratis | 966 | 100+ | 72% | 24% |
| Betaald in de winkel, zonder ThijsGer en QuadroGames | 226 | 10+ | 42% | 11% |
| **Betaalde spellen, zonder ThijsGer en QuadroGames** | 41 | 100+ | 68% | 29% |
| **Idem, zonder de 8 die zeker eerst gratis waren** | 33 | 100+ | 61% | 21% |
| **Idem, ook zonder 2 waarschijnlijk eerst gratis (ZigZag, Snake van li2niu)** | 31 | 100+ | 58% | 16% |

Prijsmediaan betaald: $2,25; 28 van de 42 betaalde spellen kosten $1,99, de rest $2,25 tot $3,99. Van de 24 betaalde apps met 1.000+ zijn er 12 spellen, en alle drie met 10.000+ zijn spellen, **maar alle drie waren eerst gratis** (controleur). Er is geen bewijs dat een spel dat vanaf het begin betaald is 10.000+ haalt.

---

## Kandidaat 1: betaald horlogespel met Gloop (Garmin). Cijfer 6 (eerst 7, verlaagd na de controleur).

**Wat:** een kort spelletje voor één knop en een paar seconden per potje, zoals de toppers (stapelen, springen, ontwijken), met Gloop en zijn hoeden uit Het Hol. De figuur wordt in Blender gerenderd tot kleine plaatjes per pose, met dezelfde stijl als Het Hol (`ontwerp/steam/3d-stijl.md`). Op het eindscherm: "Gloop lives in Het Hol, coming to Steam".

**Bewijs dat kleine makers verdienen (GEZIEN):**
- Betaalde spellen uit jan t/m 15 aug 2026, 3 tot 10 maanden oud: 31 tot 33 spellen van kleine makers zonder aanwijzing dat ze eerst gratis waren; 58 tot 61% heeft 100+ downloads, 16 tot 21% heeft 1.000+. Bij betaalde apps in het algemeen (zelfde opbouw) is dat 42% en 11%.
- Voorbeelden zonder klachten over eerst gratis: Chess Pro (Bitochi, 1.000+, 45 reviews), Blackjack (SilveroStudios, 1.000+, 39), Circle Pong (garminland), Snake (KBialy). $1,99 tot $2,25. Flick Scorer (1.000+, 3 reviews) is verdacht.
- **Voorbehoud: de hits komen van makers met veel gratis apps** (garminland heeft 4 gratis spellen met 1.000+, reviewers schrijven "like all your others"). Zij sturen hun eigen spelers door; wij hebben die achterban nog niet (wel Ebb Calm straks).
- Rekenvoorbeeld (GOK, aangenomen dat downloads verkopen zijn): 100 tot 999 kopers x $1,99 x 0,85 = $170 tot $1.700 per spel over 3 tot 10 maanden; 1.000+ is minstens $1.700.
- **Eerlijk voorbehoud 1, eerst gratis:** 8 van de 42 betaalde spellen hebben klachten "it was free" in de reviews (MangoIQ met Crossy Road 3D, Stack en Google Dinosaur Game; garminland met Stack - Blocks Game, "rip free version", gevonden door de controleur; KBialy Flags Quiz; drie van nioquant), en bij ZigZag en Snake (li2niu) is het waarschijnlijk. Die tellen hierboven niet mee. Geen klachten bewijst niet dat een spel nooit gratis was, zeker bij weinig reviews.
- Wat wel betaald is bij een spel dat eerst gratis was: Crossy Road 3D kreeg na de omslag (eind juli) nog 14 reviews in september en 13 in oktober, met "Totally worth the money" (GEZIEN, 238 reviews gelezen). Ter vergelijking: WHM breathing+ ($4,99) krijgt ±26 per maand.
- **Eerlijk voorbehoud 2, het wordt drukker:** nieuwe betaalde spellen per maand (zonder ThijsGer en QuadroGames): ±2 tot 12 in jan t/m jul 2026, daarna 18 in aug, 12 in sep en 38 in okt. De lichting 16 aug t/m 30 sep (1,5 tot 3 maanden oud) heeft mediaan 1+: 12 van de 24 op 0 tot 9 downloads, 6 op 10+, 6 op 100+, geen 1.000+. Van de lichting okt zitten 35 van de 38 onder 10. Het venster gaat dicht; wie dit doet, moet het snel doen en zelf voor bezoekers zorgen.
- ThijsGer (187 apps) en QuadroGames (18) laten bijna elke betaalde app 100+ halen met 0 tot 1 review; Gijs vond dat geen gewoon koopgedrag. Ik laat ze weg.

**Waarom wij ons onderscheiden:** de toppers zijn platte blokjes, pixels en kloons van bekende spellen (Crossy Road, Google Dinosaur). Een echt in 3D gerenderde figuur met karakter (Gloop met hoed, wiebel bij landen) valt op tussen de vierkantjes, en het is ons eigen figuur, dus geen gedoe met merken. Het spel is daarnaast een reclamebord voor Het Hol bij mensen die graag iets op hun scherm hebben.

**Verwachte omzet eerste 30 dagen (GOK):** 0 tot 150 kopers x $1,99 x 0,85 = **$0 tot $250, met de nadruk op de onderkant** (midden ±10 kopers, ±$17). Onderkant: de lichtingen van aug tot okt (mediaan 1+). Bovenkant: tempo van de beste spellen van begin 2026. Meer valt er pas over 2 tot 6 maanden te verwachten (midden 100+ kopers, ±$170+). Eerlijk: aan dag-1-geld levert dit weinig; het sterkste punt is dat het goedkoop is en Het Hol en Ebb zichtbaar maakt. Uitbetaling door Garmin is voor ons nog niet bewezen (Ebb zit in de keuring). Garmin heeft geen proef in de winkel (hasTrialMode overal uit; sommige makers bouwen zelf een proef in), dus elke download is een verkoop (met 48 uur terugbetalen).

**Uren werk (GOK):** Gijs 20 tot 35 uur (spel in Monkey C, één scherm, punten, beste score opslaan; hij kent de SDK en de simulator van Ebb), Bram of Daan 6 tot 10 uur (Gloop renderen in 6 tot 12 poses op 3 schermmaten, met de pijplijn van Het Hol). Kloktijd bij doorlopen: ±1 week. Risico: geheugen op oudere horloges; begin zoals Ebb met de ronde horloges die Ebb al ondersteunt.

**Wat Thijs moet doen:** niets nieuws. Op Verzend klikken in het Garmin-portaal zoals bij Ebb, en ja zeggen op de winkelbeelden. Geen geld: het verkopersaccount is al betaald.

**Open punten (volgende run):** (1) welke spelvorm nog geen sterke betaalde versie heeft (lijst van alle 605 spellen op soort); (2) of de keuringsregels van Garmin iets zeggen over spellen; (3) welke horloges de meeste spelkopers hebben. Uitgewerkt in run 17:12, zie hieronder.

### Uitwerking open punten kandidaat 1 (run 17:12, 13 nov)

**Kort:** maak een **eenvoudig eigen arcadespel** met Gloop, gewoon betaald in de winkel, (geen kloon van een bekend spel en geen stappenspel als kern), dat **met knoppen werkt zonder aanraakscherm**, licht is voor oude horloges en een **zwart-wit versie voor de Instinct** heeft. Cijfer blijft 6.

**(1) Spelvorm (GEZIEN, alle 605 spellen, details en downloads van vandaag via de open API, `data/garmin-spellen-details-2026-11-13.jsonl`, script `data/garmin-spellen-details-script.py`; indeling op naam met `data/garmin-spellen-vorm-script.py`, grof):**
| Vorm | Spellen | Sterkste gratis | Sterkste betaald |
|---|---|---|---|
| Kloons van klassiekers (snake, flappy, 2048, tetris, wordle, schaak, kaarten, dino) | ±210 (grof) | 10.000+ tot 100.000+ (Floppy Bird, 2048 Ultimate, Snake van mufradat, Wordle Plus) | 1.000+, bijna altijd van een maker met veel gratis spellen |
| Runner en springen | 51 | Hill Climb 10.000+ | Crossy Road 3D 10.000+ (was eerst gratis, en de naam is van een ander) |
| Eigen arcadespel met eigen naam | ±40 | Steel Eagle 1.000+ | **AstroBlast (VAW.BE, $1,99, sinds apr 2024) 10.000+, 287 reviews, 4,4**; Fruit Spider (ReedWorks, $1,99, sinds nov 2024) 10.000+ |
| Stappenspel (spel draait op echte stappen) | 41 | WatchiBeastie (GarminLabs) 50.000+ | Step Farmer (PixelPaceStudios, $2,49) 10.000+, 3,8 |
| Huisdier | 12 | SkyLing, Watchkin 1.000+ | geen betaald boven 100+ |

Wat dit zegt:
- **Kloons zijn voor ons dicht.** Bij elke klassieker staat een gratis versie met 10.000+ downloads, en namen als Flappy Bird, Crossy Road, Pac-Man, Tetris en de Google-dino zijn van anderen (keuringsregel 3a, zie (2)). Betaald lukt daar vooral voor makers die al een achterban hebben.
- **Een eigen spel met een eigen naam kan wel betaald groot worden:** AstroBlast staat sinds april 2024 betaald in de winkel, heeft 10.000+ downloads en 287 reviews, zonder klachten dat het eerst gratis was (alle reviews gelezen). Er is ook een tweede versie "with trial and kpay" die één potje gratis laat spelen en daarna laat betalen via KPay, buiten de Garmin-winkel; die haalt maar 1.000+ (107 reviews). Geen van de 605 spellen heeft de proefstand van de winkel aan. Het bewijs wijst dus op gewoon betaald in de winkel, zonder proef. AstroBlast bestuur je met tikken links of rechts (of twee knoppen), het is geen spel met één knop. Fruit Spider: 10.000+, 36 reviews, ook betaald. Beide zijn van 2024, toen er minder aanbod was.
- **Stappenspel: echte vraag, zwakke leider, maar sinds augustus overstroomd.** Step Farmer (10.000+) krijgt in 2026 vooral 1 en 2 sterren: knoppen werken niet zonder aanraakscherm (Forerunner 255, aug en sep 2026; eerder al een Instinct 3 AMOLED, sep 2025), "Doesnt work" (okt 2026); in 2026 5 keer 1 ster, 2 keer 2, 1 keer 3, 1 keer 5, en het was eerst gratis ("I had it before then you made so I have to pay", jun 2025). Maar mijn filter vond 41 stappenspellen, waarvan 32 nieuw sinds augustus 2026 of zonder datum, en de controleur vond er nog ±12 die het filter miste (WristHop, BlockMine, Dungeon Dash, Step Garden, Step Isles en andere). Samen ±53 stappenspellen, ±44 nieuw sinds augustus (QuadroGames, SilyCrafts, RunningNitro, Bitochi en anderen), ±17 betaalde nieuwkomers met 1+ tot hoogstens 100+ (Stepasaurus 10+, Stardew Farm 10+, Stepkins 1+). Een stappenspel als kern: nee. Stappen als klein extraatje (een hoed vrijspelen met je dagelijkse stappen) kan wel en geeft een reden om terug te komen, maar ±10 nieuwkomers doen dat al (WristHop, BlockMine, Dungeon Dash, Sea Strike en andere), dus het onderscheidt ons niet.
- Huisdieren: alleen gratis spellen halen 1.000+; zie ook "Wat afviel".

**(2) Keuringsregels voor spellen (GEZIEN, developer.garmin.com/connect-iq/app-review-guidelines, laatst bijgewerkt 13 okt 2021, vandaag gelezen; de algemene punten staan al bij Gijs in `platformen/garmin/upload-en-keuringsregels-2026-11-11.md`).** Er is geen apart blok voor spellen. Wat een spel raakt:
- **1a Gokken verboden.** Geen gokautomaat, roulette of inzet, ook niet voor nep-munten. (Er staan wel casinospellen in de winkel, maar we nemen dat risico niet.)
- **1f Geen apps die voor kinderen onder 13 gemaakt zijn** (een app voor iedereen mag, tenzij je weet dat kinderen hem gebruiken). Gloop is schattig; de winkeltekst richt zich op volwassen hardlopers en wandelaars, niet op kinderen.
- **1b Geen schadelijke uitdagingen.** Als stappen meetellen: geen "loop vandaag 30.000 stappen", wel kleine doelen.
- **3a Geen inbreuk.** Geen namen of uiterlijk van bekende spellen (Flappy, Crossy, Pac-Man, Tetris, dino). Ons eigen figuur is hier een voordeel.
- **4d Eerlijk over betalen:** zeggen dat het spel betaald is, het terugbetaalbeleid noemen, en een proefversie moet vanaf het begin zeggen dat ze beperkt is.
- **2a Batterij en prestaties:** niet onnodig vaak hertekenen (de les van Gloop in de Windows-build en van Ebb Calm).
- **4c** Niet om 5 sterren vragen in ruil voor iets. (AstroBlast vraagt in de tekst om 5 sterren; de regel verbiedt ook aanmoedigen dat de score vertekent, dus dat is een grijs gebied. Wij doen het niet.)
- Keuring duurt bij Ebb "maximaal 3 dagen" (`platformen/garmin/status.md`).

**(3) Welke horloges spelers hebben (benadering, GEZIEN).** De review-API geeft geen toestel mee. Daarom alle 5.076 reviews gelezen van de 112 spellen met 1.000+ downloads (`data/garmin-spellen-reviews-2026-11-13.jsonl`, scripts `data/garmin-spellen-reviews-modellen-script.py` en `data/garmin-spellen-modellen-analyse.py`) en geteld welk model reviewers noemen (456 reviews):
| Model | Keren genoemd |
|---|---|
| Venu (vooral Venu Sq en Sq 2, ook Venu 3) | 100 |
| Instinct (meest zwart-wit; Instinct 3 deels AMOLED) | 72 |
| Forerunner 55, 245, 745, 945 (oud) | 67 |
| vivoactive | 47 |
| fenix 7 | 43 |
| Forerunner 165, 255, 265, 965, 970 | 46 |
| fenix 8 en epix | 13 |
| overig (fenix 6 en ouder, fenix of Forerunner zonder nummer, Enduro, Approach, Descent) | 68 |

Spelers zitten dus vaak op **goedkopere en oudere horloges**: Venu Sq (35 keer), Forerunner 55 en 245, Instinct. De klachten gaan over: blokjes onzichtbaar of zwart beeld op zwart-wit schermen (Instinct), haperen en 3D dat stottert op de Forerunner 55 en Venu Sq, en spellen die alleen met aanraken werken (41 klachten over aanraken of knoppen, het meest bij Step Farmer en Flick Golf). Benadering: een review noemt vaker een model als er iets mis is, dus dit telt eerder klagers dan kopers.

**Wat dit betekent voor het ontwerp (advies aan Gijs, Bram en Daan):**
1. Alles met de **knoppen te bedienen**; aanraken mag erbij, nooit alleen aanraken.
2. Gloop als **vooraf gerenderde plaatjes** uit Blender (geen 3D op het horloge), in een paar maten; ook een **zwart-wit set** voor de Instinct, getest op contrast.
3. Begin met de horloges die Ebb al ondersteunt, voeg daarna de Venu Sq, Forerunner 55 en 245 en de Instinct toe als het geheugen het toelaat.
4. Een eenvoudig eigen arcadespel met eigen naam (ons idee: één knop, Gloop springt van richel naar richel in Het Hol en verzamelt hoeden; dat één knop beter werkt is niet bewezen). Gewoon betaald in de winkel, zonder proef: een proef via KPay deed het bij AstroBlast slechter, en of de winkel een proefstand met betalen biedt is nog onbekend (Gijs kan dat in het portaal zien).
5. Stappen alleen als extraatje (bijvoorbeeld elke 5.000 stappen een hoed), geen kern en geen onderscheid.

**Wat dit niet oplost:** de nieuwe lichtingen betaalde spellen (aug tot okt) halen nog steeds mediaan 1+; de verwachting voor de eerste 30 dagen blijft $0 tot $250 met de nadruk op de onderkant. Het cijfer blijft 6. Wat het omgooit: als nieuwe betaalde spellen zonder proef ook na 3 maanden op 1+ blijven, dan gaat de omzet richting $0 en het cijfer omlaag.

**Controleur (agent, run 17:12):** eerst niet akkoord, 5 correcties, alle verwerkt: proef van AstroBlast loopt via KPay en doet het slechter (advies 4 aangepast), AstroBlast is geen spel met één knop, stappenspellen ±53 met ±44 nieuw en ±17 betaalde nieuwkomers (filter miste er ±12), Instinct-klacht bij Step Farmer is van sep 2025, kleine punten over de tabel en regels 1f en 4c. Getallen van de horlogetabel en de touchklachten klopten precies. Advies en cijfer 6 bleven staan.

---

## Kandidaat 2: betaalde wijzerplaat met Gloop of de Ebb-dieren (Garmin). Cijfer 5.

**Wat:** één tot drie wijzerplaten met een in 3D gerenderd figuur (Gloop, of de krab en schildpad uit Ebb) en de gewone gegevens (tijd, stappen, batterij). Prijs $1,99.

**Bewijs (GEZIEN, wijzerplaten met eerste goedkeuring 6 mei tot 6 aug 2026, dataset 6 nov):**
| Groep | Aantal | Mediaan | 100+ | 1.000+ |
|---|---|---|---|---|
| Betaalde wijzerplaten, alle makers | 1.002 | 1+ | 14% | 3% |
| Betaald, kleine makers (20 of minder wijzerplaten) | 157 | 10+ | 31% | 8% |
| Betaald, fabrieken (meer dan 50) | 745 | 1+ | 9% | 1% |

Voorbeelden van kleine makers op 1.000+: Cool Otter (MONYMAHONY, 3 wijzerplaten, $1,99, een dier), NDR One Pro ($4,99, 182 reviews), Quipu ($2,25, 10.000+, 222 reviews). Prijsmediaan $2,49. Ook hier is niet per wijzerplaat zeker dat een download een verkoop is.

**Onderscheid:** de massa komt uit fabrieken met hetzelfde sjabloon; een figuur met karakter en echte 3D-belichting valt op. Werkt als reclame voor Ebb of Het Hol.

**Omzet eerste 30 dagen (GOK):** 5 tot 40 kopers x $1,99 x 0,85 = **$8 tot $70** per wijzerplaat.

**Uren (GOK):** 8 tot 16 uur per wijzerplaat (Gijs), plaatjes uit kandidaat 1 hergebruikt. **Thijs:** Verzend klikken.

---

## Kandidaat 3: Blender-add-on "3D-figuur naar sprites" op Superhive. Cijfer 4, reserve.

**Wat:** een add-on die een 3D-figuur in een paar klikken rendert naar spritebladen en losse plaatjes op vaste kleine maten (horloge, pixelspel, Godot), met belichting en omtrek. Dat is precies het gereedschap dat wij voor kandidaat 1 en Het Hol zelf bouwen, dus het kost weinig extra.

**Bewijs (GEZIEN, meting 9 nov):** betaalde add-ons op Superhive van 3 tot 12 maanden oud halen in 42% van de gevallen 10+ verkopen (n=1.613). In deze hoek: Pixel Art Studio ($19,90, 100+ verkopen in 2 maanden), Pro Sprite Sheet Generator ($10, 30+), Pixel Kit ($9, 10+), Flipbook For Blender ($15, 10+). Dun bewijs: geen enkele maker in deze hoek haalt duidelijk honderden per maand, en er kwamen in 2 maanden 6 nieuwe bij. Het hele aanbod van add-ons is ±4 keer zo groot als een jaar geleden (`kansen/blender-nieuwkomers-en-vloed.md`).

**Omzet eerste 30 dagen (GOK):** 0 tot 15 verkopen x ±$12 x 0,70 = **$0 tot $125**, en pas zodra Superhive de makersaanvraag van Thijs heeft goedgekeurd (loopt sinds 10 nov).

**Uren (GOK):** Bram 15 tot 25 uur, plus winkelplaatjes. **Thijs:** niets nieuws (het Superhive-account staat al op zijn lijst).

---

## Wat afviel
- **3D-modellen en assetpakketten op Superhive (nieuw gemeten vandaag):** van 2.199 betaalde modellen van 0 tot 7 maanden oud hebben er 10 (0,5%) 10+ verkopen en 2 100+; per leeftijd 3 tot 7 maanden 0 tot 1%. Er komen ±1.150 modellen per maand bij, voor een groot deel van een paar massamakers (Md Rafikul Islam 428 in de steekproef, TurboCG 200, Viktor Fedorov 142). Nee, cijfer 1.
- **Tweede Garmin-hulpapp in een drukke hoek** (water, cafeïne, vasten, alcohol): Garmin heeft zelf watertracking (5.000.000+), de grootste zijn gratis met een code buiten de winkel. Onderscheidt zich niet met 3D.
- **Virtueel huisdier op Garmin:** past bij de Ebb-dieren, maar betaald in de winkel is er geen bewijs (Watchkin gratis 1.000+, WatchiBeastie gratis 50.000+, Critter Park ontgrendelt buiten de winkel). Kan later als variant van kandidaat 1.
- **Loopband koppelen (FTMS):** echte vraag, maar we hebben geen apparaat om te testen (`kansen/garmin-zwakke-nummer-een.md`).
- **Steam, tweede klein product:** tweede fee en weken wachten. **JetBrains:** verplichte proef van 30 dagen. **TikTok:** KvK nodig. **Cults3D** (3D-printbestanden): niet te meten, Cloudflare blokkeert lezen; niet omheen gewerkt.

## Controleur
Agent-controleur, 13 nov run 16:16: eerst niet akkoord, 10 correcties, alle verwerkt. Tabellen, wijzerplaten, drukte en Superhive (5 pagina's live) klopten. Belangrijkste: Stack - Blocks Game was ook eerst gratis (alle drie de 10.000+-spellen dus), ZigZag en Snake van li2niu waarschijnlijk ook; de vergelijkingsgroep moest zonder ThijsGer en QuadroGames (42% en 11%); de recente lichtingen halen mediaan 1+, dus de omzet voor de eerste 30 dagen ging omlaag en het cijfer van 7 naar 6. Het advies bleef staan: niets draait de conclusie om.

## Bronnen
- Open winkel-API Garmin: `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>` en `/reviews?startPageIndex=<n>&pageSize=30` (gelezen 13 nov 2026).
- Superhive: `https://superhivemarket.com/categories/models/browse?sort_date=desc&page=<n>` en de productpagina's (gelezen 13 nov 2026).
