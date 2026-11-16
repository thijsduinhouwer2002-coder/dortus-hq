# Succesverhalen spellen (Fenna)

bezig: verhaal 3, hoe makers het Desktop Companion Fest (of eerdere themafestivals voor idle en taakbalk) gebruikten, Fenna 16 nov 2026

Nieuwste bovenaan.

---

## 2. Desktop Heroes (Telazer, 3 mensen) naast Deskrawl (First Day Games, 2 mensen): hetzelfde idee, heel andere uitkomst

Onderzocht 16 nov 2026, run 3. Het verhaal van een taakbalkspel dat het minder goed deed, met een tweelingspel dat het wel haalde ernaast, zodat het verschil zichtbaar wordt. Beide zijn een "idle ARPG" (helden vechten en vinden buit) in een strook boven de taakbalk, beide voor ±$4 tot $7, beide met een uitgever, beide met een demo in Next Fest en een lancering ±4 maanden na de aankondiging.

### Bronnen
- Eigen aankondigingen op Steam, alle berichten gelezen via de openbare nieuws-API: Desktop Heroes (33 berichten, aug 2025 tot mrt 2026) https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=3734200&count=60&maxlength=0&feeds=steam_community_announcements en Deskrawl (38 berichten, mei tot nov 2026) https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=4623570&count=60&maxlength=0&feeds=steam_community_announcements
- Steam appdetails 3734200 en 4623570 (prijs, talen, aantal beoordelingen, uitgever) en de winkelpagina's (reviewsamenvatting), met curl opgehaald 16 nov 2026.
- Steam-reviews, de 10 "meest behulpzame" negatieve en positieve van Desktop Heroes en de 10 negatieve van deze week van Deskrawl: https://steamcommunity.com/app/3734200/negativereviews/ en https://steamcommunity.com/app/4623570/negativereviews/
- Interview met Telazer op de site van Phaser (8 mei 2026): https://phaser.io/news/2026/04/desktop-heroes-phaser-electron-steam
- Persbericht aankondiging Desktop Heroes op Game Developer (4 jul 2025): https://www.gamedeveloper.com/press-release/telazer-games-announces-new-game-desktop-heroes
- Geen bron gevonden met verlanglijstjes of verkoopcijfers van een van beide. Alles over verkoop hieronder is daarom een schatting uit reviews (GOK).

### Cijfers naast elkaar
| Wat | Desktop Heroes | Deskrawl | Label |
|---|---|---|---|
| Maker | Telazer, 3 mensen, eerste Steam-spel (wel 1 miljoen spelers met webspellen) | First Day Games, 2 mensen, tweede spel, "duizenden uren Diablo" | DERDEN (Phaser-interview) en DERDEN (eigen aankondiging 18 mei 2026) |
| Uitgever | Blackburne Games Studio | Gamersky Games (Chinees), plus een QQ-groep naast Discord | GEZIEN (appdetails, aankondiging) |
| Aangekondigd | 4 jul 2025 | ±11 mei 2026 ("vorige week" op 18 mei) | DERDEN |
| Demo | 7 aug 2025 in het Debut Festival, daarna Next Fest okt 2025 (vanaf 13 okt) | 15 jun 2026, in Next Fest juni | DERDEN (aankondigingen) |
| Lancering | 27 okt 2025, één week na Next Fest | 28 sep 2026, ruim 3 maanden na Next Fest, na een gesloten en daarna open bèta (19 tot 28 aug) | DERDEN |
| Prijs | $5,99 (een review van 30 okt 2025 noemt "6 whole dollars"; Phaser schreef in mei 2026 $3,99, mogelijk een korting) | $6,99, lancering met 30% korting, nu weer 30% korting | GEZIEN (appdetails 16 nov 2026) |
| Talen | 14, met Chinees, Japans, Koreaans | 13, met Chinees, Japans, Koreaans, Thai | GEZIEN |
| Beoordelingen | **104 na ruim 12 maanden**, 70% positief | **3.630 na 7 weken**, "Mixed"; laatste 30 dagen 777 reviews, 36% positief | GEZIEN (winkelpagina 16 nov 2026) |
| Engelstalige reviews | (bijna) allemaal | 484 van 3.630 = 13%; de rest vooral andere talen | GEZIEN, het percentage is mijn rekensom |
| Verkocht (grof) | 104 x 30 tot 60 = ±3.000 tot 6.000 | 3.630 x 30 tot 60 = ±110.000 tot 220.000 | GOK (vuistregel uit de rol; Chinese spelers schrijven mogelijk vaker een review, dan is Deskrawl lager) |
| Laatste bericht maker | 24 mrt 2026 (daarna 8 maanden stil) | 12 nov 2026, elke paar dagen een patch | GEZIEN |

Ter vergelijking: Rusty's Retirement heeft 13.987 beoordelingen (verhaal 1).

### Wat Desktop Heroes deed, in volgorde
1. **Aankondiging met persbericht** (4 jul 2025), daarna een demo in het **Debut Festival** van Steam (7 tot 11 aug), een festival voor eerste spellen.
2. **Tussen de twee festivals de hele code omgegooid**, 2 sep 2025: "All old saves and progress will be deleted upon updating." Wie de demo in augustus speelde, begon in september opnieuw.
3. **Next Fest okt 2025 met een stream, en één week later lanceren** (aangekondigd op 23 okt, uit op 27 okt).
4. **De eerste weken bijna elke dag een update**, en meteen de kern van de klachten: het spel is niet idle genoeg. De makers antwoordden op 31 okt met een eigen bericht: "Desktop Heroes is not designed to be a game that you can set up and leave running for hours without interacting with it." Ze kozen bewust een mengvorm ("Unlike other 'bottom-of-the-screen' games, we aimed to create a hybrid experience").
5. **Pas 7 weken na de lancering bijgestuurd** (16 dec 2025, "We heard you ... we made the game more idle-friendly"), daarna een roadmap die schoof, een groot verhaal-update in mrt 2026 (v3.0.0), en sindsdien stilte.

### Wat de spelers zeiden (Desktop Heroes, de meest behulpzame negatieve reviews)
- "As an idle game, there is no idle progression. As an ARPG, there is no action." (31 okt 2025)
- "It's neither idle (needs you to intervene in high difficulty) nor manual (you can't afford the time to babysit the whole game). Make. Up. Your. Mind." (28 okt 2025)
- "If you die you stop progressing all together, so the idleing just stops." (8 nov 2025)
- "it's incredibly distracting ... I really can't have it running while studying, programming, or working ... TLDR; Not idle enough." (14 dec 2025)
- "No idle progress and no offline progress." (apr 2026)
- Ook "barebones", "recycled sprites" en "just another pile of slop added to the idler genre" van iemand die "close to 150" idle games speelde: kenners vergelijken met veel gratis idle games.
- Positief, ook terugkerend: het idee ("it's fun to glance down and see your little hero fighting") en snelle patches. Opvallend: één van de top-positieve reviews was eerst negatief en draaide om door de patches.

### Wat Deskrawl anders deed, in volgorde
1. **Een duidelijke belofte aan een bekende groep:** "a game that we could always play no matter if we are working, or watching TV shows", van twee Diablo-spelers voor Diablo-spelers. Aankondiging, en vijf weken later al een demo in Next Fest.
2. **De demo als levend spel behandeld:** in de eerste week van de demo zes patches, waarvan drie met nieuwe inhoud (nieuwe kaart, max level omhoog, nieuwe legendarische spullen "for you all to explore and test during Next Fest"), allemaal op verzoek van spelers (venster schalen, cloud save).
3. **Spelers een reden gegeven om te blijven en vrienden te halen:** een ranglijst in de demo, een baas-evenement waar "about 4000 players" de baas versloegen, de top 100 kreeg toegang tot de bèta, en 1.000 bètasleutels werden verloot onder de rest. "Don't forget to invite your friends if they haven't tried the demo yet!"
4. **Gesloten bèta, daarna open bèta, pas daarna lanceren** (3 maanden na Next Fest), met 30% korting en twee nieuwe klassen.
5. **Een Chinese uitgever en een QQ-groep vanaf de eerste dag.** 87% van de reviews is niet Engels (rekensom). Het spel lijkt vooral in Azië verkocht (GOK, het precieze land per review heb ik niet).

**Maar Deskrawl gaat nu mis op iets anders:** 36% positief in de laatste 30 dagen. De klachten van deze week gaan over handel met echt geld en buit: spullen te koop op de Steam-markt, "so leaderboards mean nothing", prijzen die keldern, te weinig buit ("74 hours not a SINGLE rune drop"), en spelers zonder online modus missen "the 300% loot buff". Een goed begin beschermt niet tegen een verdienmodel dat spelers oneerlijk vinden.

### Drie lessen
1. **"Onderaan je scherm" is een belofte: het moet ook zonder jou doorgaan.** De grootste klacht over Desktop Heroes was niet de prijs of de beelden, maar dat het niet idle genoeg was: doodgaan stopt de voortgang, geen voortgang als je weg bent, en het trekt te veel aandacht tijdens werk. De makers gaven dat zelf toe ("not designed to ... leave running for hours"). Spelers in dit genre kopen rust, geen tweede taak.
2. **Een demo die leeft en een reden geeft om terug te komen, wint.** Deskrawl patchte de demo tijdens Next Fest bijna dagelijks, deels met nieuwe inhoud, maakte er met een ranglijst en een baas-evenement een wedstrijd van (±4.000 spelers versloegen de baas, DERDEN) en beloonde de fanatiekste spelers met de bèta. Desktop Heroes wiste tussen twee festivals alle saves en lanceerde een week na Next Fest. Of die volgorde de oorzaak is, is niet bewezen (GOK), maar het verschil in uitkomst is ±35 keer in reviews.
3. **Talen alleen zijn niet genoeg; een partij die de markt kent wel.** Beide spellen hadden Chinees, Japans en Koreaans. Het verschil: Deskrawl had een Chinese uitgever en een QQ-groep vanaf de aankondiging. Dit verfijnt de les van Rusty's (46% Azië): de vertaling opent de deur, maar iemand moet er ook mensen naartoe brengen (GOK in hoeverre, er zijn geen landcijfers).

Extra, kleiner: Deskrawl laat zien dat handel en online buit-bonussen in een rustig spel snel als oneerlijk voelen. Wij hebben geen handel en willen dat zo houden.

### Eerlijk: wat niet zomaar voor ons geldt
- Beide zijn ARPG's met buit en gevechten; Hats of the Fallen is een spel waar je zelf het hol bent. Onze kern (helden komen naar jou, jij graaft en zet bewoners neer) is van zichzelf al meer idle. Ons ontwerp heeft "nooit straffen als je weg bent" al als eis (T3 en demo-eis 4 in `planning-fest-2027.md`). Les 1 bevestigt die keuze, het is geen nieuw werk.
- Deskrawl is pas 7 weken uit; hoe het afloopt weet niemand. Desktop Heroes verkocht misschien toch genoeg voor een team van drie met lage kosten (GOK).
- Een ranglijst of evenement in een demo vraagt servers of een account bij Steam (leaderboards). Dat is techniek die wij nog niet hebben, en de demolijst ligt vast tot 18 dec.

### Voorstel voor Dortus deze week
**Olaf zet in de speeltest van 4 dec voor Thijs twee vaste vragen en in de simulatie één vaste meting: (1) "Kon je 15 minuten werken terwijl het draaide, zonder dat het je aandacht trok?", (2) "Gebeurde er iets goeds terwijl je niet keek?", en (3) in de simulatie: een uur zonder één klik geeft minstens de helft van het goud van een uur met klikken, en niets staat stil.** Waarom: de grootste klacht over het taakbalkspel dat mislukte was "not idle enough", en die kwam pas na de lancering boven. Wij hebben de regel al op papier; dit maakt hem toetsbaar vóór de demo. De helft is een eerste getal (GOK), Olaf en Bram mogen het na de simulatie bijstellen. Wie: Olaf (vragen en meting), de hoofdchat neemt de vragen op in het speeltestformulier.

Voor na 18 dec (geen actie nu, voor Hans en de hoofdchat): tijdens het Desktop Companion Fest en Next Fest de demo bijhouden zoals Deskrawl (elke dag fouten oplossen en dat melden in een aankondiging), nooit saves wissen tussen festivals, en het volle spel niet een week na Next Fest uitbrengen maar pas als de klachten uit de demo verwerkt zijn.

---

## Vraag van de hoofdchat (16 nov): valt vertalen met AI onder de AI-melding van Steam, en wat kost een mens?

Onderzocht 15 nov 2026 (klok van de run), run 2. Geen verhaal maar een vraag; antwoord kort bovenaan, onderbouwing eronder.

### Kort antwoord
1. **Ja. Vertalen met AI valt er letterlijk onder.** Valve noemt vertalen (localization) bij naam als inhoud die gemeld moet worden. Ook als een mens de AI-vertaling daarna nakijkt, is de tekst "met hulp van AI-tools gemaakt", dus melden (dat laatste is mijn lezing van de definitie, geen apart citaat van Valve).
2. **Maar voor ons verandert het weinig.** Wij melden toch al AI: de spel- en winkeltekst schrijven Claudes. Het voorstel van Abel voor de melding (`platformen/abel/accounts/steam.md`) noemt al "text and code ... made with the help of AI tools". AI-vertalen voegt één woord toe aan een melding die er al staat; het maakt van een spel zonder melding geen spel met melding.
3. **Een mens kost ongeveer €45 tot €70 per taal voor 500 woorden**, dus ±€190 tot €270 voor Vereenvoudigd Chinees, Japans, Koreaans en Duits samen, plus mogelijk een minimumbedrag per opdracht en extra voor elke latere tekstwijziging.

### De regel van Valve (bron en citaat)
- Bron: Steamworks-documentatie, pagina Content Survey, deel 3 "Generative Artificial Intelligence Content", met curl gelezen op 15 nov 2026: https://partner.steamgames.com/doc/gettingstarted/contentsurvey
- Citaat (één zin): "This includes content such as artwork, sound, narrative, localization, etc." De zin ervoor zegt waar het om gaat: "the use of AI in creating content that ships with your game, and is consumed by players." GEZIEN.
- Sinds wanneer: deze tekst staat er sinds ongeveer 17 jan 2026. GamingOnLinux meldde op die dag (via GameDiscoverCo) dat Valve het formulier zo had aangepast, met precies dit citaat: https://www.gamingonlinux.com/2026/01/valve-tweak-steam-ai-disclosure-form-for-developers-to-clarify-its-for-content-consumed-by-players DERDEN.
- Wat er níet onder valt: hulpmiddelen die alleen het werk versnellen ("Efficiency gains through the use of these tools is not the focus of this section"). Volgens FinalBoss valt ook winkeltekst, capsule en trailer eronder (DERDEN, niet in de tekst van Valve zelf gezien).
- **De demo heeft een eigen Content Survey.** Steamworks, pagina Demos: "Make sure your Content Survey accurately reflects the demo content." GEZIEN: https://partner.steamgames.com/doc/store/application/demos . Komen er talen in de demo, dan moet de melding van de demo dat ook zeggen.

### Hoe gewoon is een AI-melding nu?
- FinalBoss (nov 2026, eigen analyse van ±63.600 Steam-uitgaven sinds jan 2024): **49,9% van de spellen die in okt 2026 uitkwamen heeft een AI-melding**, tegen 26,4% in okt 2025. Bij spellen met een melding noemt 30% "tekst en vertalingen", 63% beelden, 26% winkelpagina. https://finalboss.io/steam-ai-disclosures-hit-49-9-what-buyers-should-check DERDEN (de methode is niet openbaar, dus voorzichtig).
- Wat dit betekent: de melding is geen uitzondering meer, de helft van de nieuwe spellen heeft er een. Of hij de verkoop drukt is daarmee niet gezegd; het getal "tot 53% minder" uit de YouTube-video is nog steeds NIET NAGEKEKEN.
- Eigen meting in de repo (verkenner, itch.io, kleine aantallen): tools met AI-melding haalden minder vaak 3+ beoordelingen (0,8% tegen 3,7%). Andere winkel, maar het wijst dezelfde kant op: een melding kost waarschijnlijk iets. GOK hoeveel.

### Wat kost een menselijke vertaler?
| Bron | Prijs per woord | 500 woorden | Label |
|---|---|---|---|
| Allcorrect (groot spelvertaalbureau), openbare prijslijst: https://allcorrectgames.com/localization-pricing/ | Duits en Japans €0,10 tot €0,14; Koreaans en Trad. Chinees €0,09 tot €0,14; Vereenvoudigd Chinees €0,09 tot €0,12 | €45 tot €70 per taal | DERDEN (gelezen 15 nov 2026) |
| Gastartikel van een vertaalbureau op Game Developer (oud, datum niet te lezen): https://www.gamedeveloper.com/programming/how-much-does-game-localization-cost- | €0,09 tot €0,12 voor de grote talen, Chinees inbegrepen | €45 tot €60 | DERDEN |

- Optelsom voor de vier talen uit het Rusty-voorstel (zh-Hans, ja, ko, de) bij 500 woorden: Chinees €45 tot €60, Japans €50 tot €70, Koreaans €45 tot €70, Duits €50 tot €70, **samen €190 tot €270**. Mijn rekensom met DERDEN-prijzen.
- Kleine opdrachten: "The majority of translators and localization agencies charge a minimum fee" (Game Developer). Allcorrect heeft er ook een, maar zegt die maar zelden te rekenen. Bij 500 woorden kan dat minimum de prijs bepalen (GOK, hoe hoog staat er niet).
- Herhalingen zijn bij Allcorrect gratis. Testen in het spel (LQA, kijken of de tekst past en klopt in beeld) is een aparte post die hier niet in zit.
- Elke latere tekstwijziging is een nieuwe opdracht. Bij een spel dat nog verandert is dat de verborgen kostenpost.

**Bijgewerkt 16 nov met de telling van Olaf (±1700 woorden, niet 500):** met dezelfde prijzen van Allcorrect (DERDEN) kost het Chinees €153 tot €204, Japans €170 tot €238, Koreaans €153 tot €238, Duits €170 tot €238, **samen ±€650 tot €920** voor vier talen (mijn rekensom). Alleen Chinees en Japans nakijken of vertalen: ±€320 tot €440. Het minimumbedrag per opdracht speelt bij 1700 woorden waarschijnlijk geen rol meer (GOK). Het voorstel hieronder blijft staan: de demo met AI-vertaling; een mens pas als Azië verlanglijstjes geeft, en dan is het bedrag ruim drie keer zo hoog als eerst gedacht.

### Eerlijk: wat ik niet weet
- Of Chinese, Japanse of Koreaanse spelers een slechte AI-vertaling afstraffen in reviews. Dat hoor je vaak, maar ik heb er nu geen bron voor. GOK.
- Of 500 woorden klopt: dat getal kwam van de hoofdchat, niet uit het spel geteld. **Nagekomen (16 nov, Olaf telde): het is ±1700 woorden (±390 teksten).** Zie de bijgewerkte prijzen hierboven.
- Het voorstel van Abel noemt "pixel art"; Het Hol is inmiddels 3D uit Blender-code. Of beelden die Claude met code maakt "met hulp van AI" zijn, beslist niet ik: dat is de tekst die de hoofdchat met Thijs invult. Eerlijk lijkt me: noemen.

### Voorstel voor Dortus
**De hoofdchat besluit: demo van 18 dec met AI-vertaling (Claude) in Vereenvoudigd Chinees, Japans, Koreaans en Duits, en de AI-melding van spel én demo noemt "text and translations".** Waarom: de melding staat er toch al, dus het kost geen extra label en geen geld, en de grootste voorganger haalde 46% van zijn kopers uit Azië (zie Rusty hieronder). Tweede stap, vóór de lancering van het volle spel en alleen als de demo in Azië verlanglijstjes geeft (te zien in Steamworks per land): een mens kijkt de Chinese en Japanse tekst na, ±€320 tot €440 voor die twee bij 1700 woorden (eerst geschat op €100 tot €130 bij 500 woorden; geld, dus via de lijst van Thijs). Wie: Olaf zet de tabel klaar (al uitgezet), de hoofdchat beslist de talen en past de meldingstekst bij Abel aan. Niet doen: menselijke vertaling nu, terwijl de tekst tot 18 dec nog verandert.

---

## 1. Rusty's Retirement (Jordan Morris, solo, Mister Morris Games)

Onderzocht 15 nov 2026, run 1. De vader van het genre "spel onderaan je scherm", dus de directe voorganger van Hats of the Fallen.

### Bronnen
- GameDiscoverCo, "How Rusty's Retirement idle-farmed its way to 300k+ Steam sales!" (interview met de maker, eind aug 2024, met zijn echte Steam-cijfers): https://newsletter.gamediscover.co/p/how-rustys-retirement-idle-farmed
- Eigen aankondigingen van de maker op Steam (alle berichten van dec 2023 tot okt 2025 gelezen via de openbare nieuws-API): https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=2666510&count=60&maxlength=0&feeds=steam_community_announcements
- Steam appdetails 2666510 (prijs, talen, DLC, aanbevelingen), met curl opgehaald 15 nov 2026.
- Tweets van de maker (gezien als zoekresultaat, niet zelf geopend; datum berekend uit het tweetnummer): 100.000 verlanglijstjes op 25 mrt 2024, https://x.com/MrMorrisGames/status/1772305610580619385
- TikTok van de maker, 4 dec 2023 (datum uit het videonummer): https://www.tiktok.com/@mister.morris.games/video/7308754929005464865
- GamesRadar over de Next Fest-demo (6 feb 2024): https://www.gamesradar.com/my-early-steam-next-fest-highlight-is-like-an-idle-stardew-valley-but-i-promise-its-not-as-distracting-as-it-sounds
- GamesRadar over 100k en 200k verkocht (2 en 15 mei 2024), 80.lv (3 mei 2024, korting bij lancering).

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Prijs | $6,99 (GameDiscoverCo schrijft $7); bij lancering 10% korting | GEZIEN (appdetails) en DERDEN (80.lv) |
| Bouwtijd | 6 maanden, begonnen als prototype van 2 weken | DERDEN (maker op Steam, okt 2024; GameDiscoverCo) |
| Steampagina live | rond eind nov of begin dec 2023 ("a little under 4 months ago" op 25 mrt 2024; TikTok met "wishlist" op 4 dec 2023) | DERDEN, datum is een afleiding |
| Demo | 2 feb 2024, drie dagen voor Next Fest februari; na Next Fest nog een week online | DERDEN (aankondigingen Steam) |
| Verlanglijstjes | 100.000 op 25 mrt 2024; ±140.000 op de lanceerdag | DERDEN (tweet; GameDiscoverCo) |
| Lancering | vr 26 apr 2024, bewust op de vrijdag vóór het Farming Fest van Steam (29 apr) | DERDEN (maker in GameDiscoverCo) |
| Verkocht | 100.000 in 5 dagen, 200.000 in ruim 2 weken, bijna 330.000 eind aug 2024 | DERDEN (maker op Steam en X; GameDiscoverCo) |
| Opbrengst per stuk | ±$5 per verkocht exemplaar vóór de 30% van Steam (door terugbetalingen, kortingen en regionale prijzen); dus ±$3,50 naar de maker, ±50% van de winkelprijs | DERDEN (GameDiscoverCo), de $3,50 is mijn rekensom |
| Na 4 maanden | ±$1.800 per dag zonder actie, ±300 stuks per dag | DERDEN (maker in GameDiscoverCo) |
| Supporter Pack | $3,99 gouden pakje voor Rusty; 36.000 verkocht = **11% van de kopers**, $111.000 | DERDEN (GameDiscoverCo) |
| Landen | 26% China, 10% Japan, 6% Korea, 4% Taiwan (samen 46% Azië); 11 talen bij lancering | DERDEN (GameDiscoverCo); 11 talen GEZIEN (appdetails) |
| Aanbevelingen nu | 13.987 | GEZIEN (appdetails 15 nov 2026) |
| Vorig spel van de maker | Haiku, the Robot (apr 2022, $19,99), 2.600 aanbevelingen | GEZIEN (appdetails) |

### Wat hij deed, in volgorde
1. **Prototype van 2 weken** na zijn vorige spel. Hij twijfelde over weer een Metroidvania, maar koos dit idee omdat het "verkoopbaar" was (GameDiscoverCo).
2. **Eén haak die je in één beeld snapt:** een boerderij die onderaan je scherm leeft terwijl jij werkt. Twee handelingen: zaaien en dingen neerzetten die het werk overnemen. Voor de rustige speler en voor de min-maxer.
3. **Steampagina rond eind nov 2023, korte filmpjes vanaf het begin.** Zijn eigen woorden: "veel succes met posten op Twitter en Instagram Reels, die ik daarna ook op TikTok zette. Het idee bleef bij mensen hangen." Streamers pikten het op (Pirate Software wordt genoemd).
4. **Demo vlak voor Next Fest (2 feb 2024)**, met een feedbackformulier in het spel, een versiering-wedstrijd tijdens het fest (deel je boerderij op Twitter of Steam, winnaars krijgen een prijs) en een eigen livestream. Daarna schoof hij de lancering op van Q1 naar Q2 om de feedback te verwerken.
5. **100.000 verlanglijstjes in minder dan 4 maanden pagina.** Lanceerdatum gekozen op een Steam-themafestival (Farming Fest): hij lanceerde de vrijdag ervoor, kreeg een weekend vaart en daarna een tweede piek door het festival ("dubbele piek").
6. **Lancering met 11 talen, 10% korting en meteen een Supporter Pack.** Twitch-kijkers konden met een commando op de boerderij verschijnen en helpen (!plant).
7. **De eerste weken alleen bugs repareren**, bijna elke dag een build (zwart scherm, grote monitoren, Mac). Daarna een rustpauze en gratis updates (winter, samenwerkingen met Vampire Survivors en Balatro in 2025). Kortingen van 20 en 25% in de grote uitverkopen zetten de verlanglijstmails aan en gaven telkens een nieuwe piek.

### Drie lessen
1. **Een themafestival van Steam is de motor van de lancering, niet alleen Next Fest.** Hij koos zijn lanceerdatum rond het Farming Fest en zegt zelf dat dat de kans op succes vergrootte; de verkoop had twee pieken. Kortingen die verlanglijstmails aanzetten gaven daarna steeds nieuwe pieken.
2. **Bijna de helft van de kopers zat in Azië, en dat lukte door 11 talen bij de lancering.** GameDiscoverCo: "zo krijg je internationaal succes". Een strookspel heeft weinig tekst, dus vertalen is relatief goedkoop.
3. **Een Supporter Pack is echt geld: 11% van de kopers nam het.** Dat is veel meer dan wat wij uit reviews afleidden: in `platformen/steam/verdienmodel.md` staat voor ditzelfde pack 94 DLC-reviews op 6.625 = 1,4%. De echte koopkans is dus ongeveer 8 keer hoger dan de reviewverhouding (rekensom met DERDEN-cijfers). De aanname van Sanne (8 tot 18% koopt iets extra) klopt daarmee.

Extra, kleiner: verkeer van buiten Steam kwam vooral uit korte filmpjes en streamers, en hij maakte het streamers makkelijk (Twitch-commando's). Lastig voor meten: streams stonden meestal onder "Just Chatting" omdat het spel niet het hele scherm vulde.

### Eerlijk: wat niet zomaar voor ons geldt
- Hij was de eerste. In 2023 was "onderaan je scherm" nieuw; "We're spawning a genre" schreef hij zelf in mei 2024. Nu zijn er honderden Desktop Companion-apps (405 geteld door Olaf op 9 nov). Een nieuwe haak alleen is voor ons niet genoeg.
- Hij had al een spel met publiek (Haiku, the Robot, 2.600 aanbevelingen) en een eigen account op X. Wij beginnen bij nul volgers.
- Hoeveel verlanglijstjes de demo en Next Fest precies gaven, zegt geen bron. Het verloop staat in een grafiek bij GameDiscoverCo die ik niet kan lezen (alleen plaatje).
- Reviews x 30 tot 60 zou 420.000 tot 840.000 geven (GOK); de echte 330.000 na 4 maanden past daarbij.

### Voorstel voor Dortus deze week
**Olaf zet nu alle tekst van Hats of the Fallen in één vertaaltabel (geen tekst meer vast in de code) en de hoofdchat beslist of Vereenvoudigd Chinees, Japans, Koreaans en Duits in de demo van 18 dec komen.** Waarom: bij de grootste voorganger kwam 46% van de kopers uit Azië dankzij 11 talen (DERDEN). Nu één tabel maken kost weinig; achteraf alle tekst uit de code halen kost veel. Let op: de demolijst in `planning-fest-2027.md` is vast, dus talen erbij is een besluit van de hoofdchat, geen eigen keuze van Olaf. Vertalen met AI kan onder de AI-melding van Steam vallen (GOK, nog na te lezen in de regels van Steam); dat moet eerst uitgezocht.

Tweede punt voor Hans en Chris (geen actie deze week): kies de lanceerdatum van het volle spel rond een themafestival van Steam waar we in passen (Steam had in feb 2025 een "Idler Fest", zie de aankondiging van 4 feb 2025 in de nieuws-API van Rusty's), niet alleen rond Next Fest.
