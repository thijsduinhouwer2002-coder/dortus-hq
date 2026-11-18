# D: Steam-marketing voor Hats of the Fallen (agent D, 18 nov 2026)

Opdracht: `BRIEF.md` in deze map, plus de vraag van de hoofdchat: het werk van Sem kritisch toetsen tegen wat we nu weten, echte voorbeelden van kleine bureaubladspellen met 5.000+ verlanglijsten in 2 maanden, wat we vóór de Steam-pagina kunnen doen, en wat automatisch kan. Alle webpagina's met curl gelezen op 18 nov 2026 ±19:00 tot 20:30 UTC. Niets geplaatst, niets verstuurd.

## Wat er al ligt (één regel per stuk, niet overgedaan)
- `platformen/steam/fest-plan.md`: zeven punten na Fenna's flops (samen spelen, makerslijst, festplan, pagina eerder, TikTok, talen, nooit wissen).
- `marketing/festplan.md` (Sem, 73 KB): fasen met doelen (500 verlanglijsten vóór 4 jan, 2.500 en 300 volgers vóór het fest), paginadag met achtergehouden trailer, demodag, Steam-mail op 14 jan, meetlat na dag 2, plan bij stilte, microtrailer, Next Fest feb, verlanglijstbegroting, drempel Most Wanted Upcoming (±270 tot 350 volgers).
- `marketing/makers.md`, `teksten-makers.md`, `curatoren.md`, `pers.md`, `festivals.md`: eerste ronde van 15 makers op bereik, Indie Game Joe, 18 echte curatoren, persmail alleen bij doorbraak, Laughs & Smiles ingestuurd.
- `marketing/routekaart.md`, `lanceerplan.md`: routekaart pas na de uitgave (0 van 13 winnaars deed hem vooraf), korting en lanceermeetlat.
- `plan-b-id-controle.md` (Olaf): tabel per moment dat de app er is; itch.io afgeraden.
- Workflows die er al zijn: `steam-hol-clips.yml` (mp4's uit de build), `steam-hol-winkel.yml` (winkelopname), `steam-fest-meting.yml`, `steam-uitbrengen.yml` (upload naar een niet-openbare tak).

Dat werk is grondig en ik neem het over. Het rust op één aanname die niet meer klopt: **pagina live ±8 dec**. Daar gaat deel 0 over.

## 0. Kritische toets: wat niet meer klopt

**Feit 1 (GEZIEN door de hoofdchat, bord 18 nov 16:47):** Steamworks weigert een app tot Valve bank, belasting en ID goedkeurt; documenten binnen 15 nov, Valve noemt tot 45 werkdagen. Mijn rekensom: 45 Amerikaanse werkdagen na 15 nov, zonder Thanksgiving en de kerstdagen, is **vr 22 jan 2027** (GOK op welke feestdagen Valve vrij is). De Steamworks-docs zeggen zelf over de belastingcontrole: "This process may take up to 30 days" (GEZIEN, `partner.steamgames.com/doc/gettingstarted/onboarding`).

**Feit 2 (DERDEN, nieuw sinds 3 nov, staat nergens in onze plannen):** Valve meldt "a significant increase in submissions for store page and build review" en: "We aim to test every game build in a timely manner, typically within 3-5 days. However, we're running a little behind right now and taking up to 12 business days." ([VGC 4 nov 2026](https://www.videogameschronicle.com/news/steam-says-its-running-behind-when-reviewing-pre-release-games-because-of-how-many-re-reviews-it-has-to-do/), [Inven Global](https://www.invenglobal.com/articles/28152/valve-says-steam-pre-release-reviews-now-take-up-to-12-business-days)). Een maker: "Took us 2 weeks for our playtest to be approved!" Plus nieuwe eisen: het spel minstens 5 minuten via Steam gedraaid vóór indienen, redistributables opgeven, Steam Cloud moet een save schrijven als je het aanzet, en **minstens 5 schermafbeeldingen gemarkeerd als gameplay** (menu's, concept art en filmbeelden tellen niet).
- `planning-fest-2027.md` rekent 7 werkdagen voor de pagina en demo indienen 21 dec. Een demobuild op vr 18 dec kan met 12 werkdagen pas **vr 8 jan** goedgekeurd zijn (rekensom, GOK op feestdagen). Krap, maar vóór 14 jan.
- `winkelpagina-klaar.md` heeft precies 5 schermen, waarvan `5-kaartje.png` een kaartje is. Als Valve of wij dat als menu markeren, zijn het er 4 en wordt de pagina afgekeurd. **Actie Olaf/Daan: 6 tot 8 echte spelschermen** (winnaars hebben er mediaan 8, Sem).

**Wat dat betekent per moment dat de app er is** (scherper dan plan B, want het fest hoeft niet alles of niets):
| App er op... | Pagina live (5 werkdagen) | Desktop Companion Fest 14 jan | Next Fest feb (aanmelden vóór 10 jan, app nodig) | Laughs & Smiles 21 jan (appid beloofd) |
|---|---|---|---|---|
| uiterlijk ma 14 dec | ±21 dec | **ja, met demo** (demobuild indienen dezelfde week, uiterlijk goedgekeurd ±8 jan) | ja | ja |
| 15 dec tot ma 4 jan | ±21 dec tot ±11 jan | **ja, maar alleen met de pagina in het vak "Upcoming"**; demo pas na het fest (12 werkdagen) | ja | ja |
| 5 tot 10 jan | ±12 tot 18 jan | GOK: alleen als de pagina vóór of tijdens het fest live komt | ja, aanmelden op de dag zelf | GOK |
| na 10 jan | ±eind jan tot half feb | nee | nee, volgende Next Fest (±juni 2027, GOK) | waarschijnlijk niet |

Wat plan B mist: **meedoen in het vak "Upcoming" kan met alleen een pagina** (Sanne, `ontwerp/steam/winkelpagina/fest.md`: "Spellen die nog niet uit zijn doen mee in een eigen vak Upcoming", GEZIEN door haar in de docs). Een pagina zonder demo staat laag in het vak, maar staat er wel, en het kost niets. Plan B zegt bij "eind december: reken op nee"; ik zou zeggen: pagina mee, demo niet.

**Beslisdata voor de hoofdchat:** ma 14 dec (demo nog in het fest?), ma 4 jan (pagina nog in het fest?), zo 10 jan (Next Fest feb of juni). Elke maandag de stand in Steamworks lezen staat al in plan B.

**Wat er aan de doelen verandert:** 2.500 verlanglijsten en 300 volgers vóór 14 jan rekenen op vijf weken pagina plus makers plus clips (Sem gaf zelf al aan dat het een stuurgetal is, geen verwachting). Met 0 tot 3 weken pagina is dat niet meer eerlijk. De ijking: mediaan aangekondigd bureaubladspel 9,5 volgers (GEZIEN, Sem), Pocket Cat Desktop 777 verlanglijsten in de eerste week (DERDEN, zie deel 1). **Voorstel: het festdoel hangt aan de datum van de pagina** (bijvoorbeeld 100 verlanglijsten per week pagina, GOK), en het echte werk vóór de pagina is niet "verlanglijsten" maar **mensen vangen die we op de paginadag kunnen roepen** (deel 2, actie 1).

**Wat blijft staan:** paginadag als één moment, Steam-mail pas op 14 jan, routekaart na de uitgave, persmail alleen bij doorbraak, makers op bereik, hoedenwedstrijd, microtrailer met ingezoomde strook. Die hangen niet aan 8 dec.

**Eén regel van Sem die nu schuurt:** "tot de paginadag TikTok alleen kleine maak-clips met follow us, nooit de haak" (festplan, op grond van Little Writer: 100k weergaven zonder pagina gaf 12 volgers, GEZIEN Fenna verhaal 13). Dat was goed bij drie weken wachten. Bij mogelijk tien weken wachten is het tien weken niets. De les van Little Writer is niet "zwijg", maar "aandacht zonder iets om op te klikken verdampt". Met een vangnet (actie 1) is er wél iets om op te klikken. De haak (trailer, sterkste clip) blijft voor de paginadag; de kleine clips krijgen een bestemming.

## 1. Wat werkt aantoonbaar (bron en getal)

**Kleine bureaublad- en idlespellen met 5.000+ verlanglijsten binnen ±2 maanden na de pagina:**
| Spel | Wat | Getal | Wat ze deden | Bron |
|---|---|---|---|---|
| **Gamblers Table** (idle/clicker, Godot, 2 makers) | prototype eerst gratis in de browser op itch.io, eind mrt 2025; Steampagina 27 apr 2025 | **10.000 verlanglijsten in 18 dagen**, 20.000 op 5 jun 2025 | itch-algoritme pakte het op via tags (incremental, idle, clicker) en "free + web"; één gif op r/incremental_games; Discordlink op de itch-pagina toen er nog geen Steampagina was; **een grote verlanglijstknop in het spel zelf**; elke YouTuber met 30k+ abonnees gaf een piek | eigen devlog ([itch](https://greenpixels.itch.io/gamblers-table/devlog/945763/wishlists-0-to-10000-in-just-three-weeks-)), DERDEN |
| Ropuka's Idle Island ($3,99, 3 mensen) | van idee in december tot uitgave 29 jan 2025, pagina dus korter dan 2 maanden | ±5.400 verlanglijsten bij de uitgave | lanceerweken van Steam, Idler Fest 5 dagen later, pers die het zelf vond | Fenna verhaal 27 (GEZIEN) |
| Character House | demo buiten een fest | 100.000 verlanglijsten in een week | TikTok van anderen (@lemon.stones 318.900) | `character-house.md` (eigen melding maker, DERDEN) |
| Rusty's Retirement | pagina 4 dec 2023, uit 26 apr 2024 | ±140.000 verlanglijsten bij de uitgave; eerste TikTok op de paginadag 493.800 | "a lot of success posting about the game on Twitter and Instagram Reels (which I then used to cross promote on TikTok)"; Twitch-functie; uitgebracht vlak voor het Farming Fest | [GameDiscoverCo](https://newsletter.gamediscover.co/p/how-rustys-retirement-idle-farmed) (DERDEN), TikTok GEZIEN door Sem |
| Tiny Glade (geen bureaubladspel, wel klein team) | maillijst vóór de pagina | 10.000 verlanglijsten in 24 uur bij de pagina; **28% doorklik uit de maillijst** tegen "1% or less" uit sociale media | maillijst gevuld vanuit virale clips zonder naam; pagina op een festival gelanceerd | [How To Market A Game](https://howtomarketagame.com/2023/06/12/marketing-your-steam-game-before-you-have-a-steam-page-the-tiny-glade-story/) (DERDEN) |

**De ijkpunten onderaan (eerlijk, want dat is de gewone uitslag):**
| Spel | Getal | Bron |
|---|---|---|
| Pocket Cat Desktop (kat op het bureaublad, sep 2026) | **777 verlanglijsten in week 1**; twee Telegramkanalen met samen 40.000+ weergaven gaven maar ±200; eigen posts met UTM 269 | [wnhub 8 okt 2026](https://wnhub.io/news/stores-and-publishing/item-52326) (DERDEN) |
| Desktop Defender | ±200 verlanglijsten in 3 maanden pagina; alles kwam uit Next Fest | Fenna verhaal 5 (GEZIEN) |
| Idlewood Outpost | ook eerst een browserdemo op itch (6 jul 2025), pagina 29 jul, nu 4 reviews | Fenna verhaal 8 (GEZIEN) |
| Mediaan aangekondigd bureaubladspel | 9,5 volgers (±70 tot 190 verlanglijsten) | Sem (GEZIEN) |

**Wat de 5.000+ gemeen hebben (mijn lezing, GOK op oorzaak, het zijn 5 spellen):**
1. **Eén moment van grote aandacht** uit een korte video of een algoritme dat ze niet zelf kochten (TikTok, itch-tags, een fest). Geen van hen kwam er met posts alleen.
2. **Iets om de aandacht vast te houden toen die kwam**: een maillijst (Tiny Glade), een Discordlink plus een knop in het spel (Gamblers Table), of de Steampagina zelf (Rusty's).
3. **Weinig tijd tussen aandacht en pagina.** Gamblers Table zag de itch-weergaven zakken "from thousands to hundreds" in de maand dat ze op de verificatie wachtten, en het kwam terug op de dag dat de pagina live ging. Dat is precies onze situatie.
4. Itch alleen is geen garantie (Idlewood Outpost). Het verschil bij Gamblers Table: een spel dat in 10 seconden in de browser leuk is, en de juiste tags.

**Over itch.io moet één ding vooraf gezegd (GEZIEN, `itch.io/docs/creators/quality-guidelines`):** "Accurately tag your use of generative AI", met keuzes voor graphics, sound, text en **code**; projecten die "predominantly created by algorithms or AI with minimal human intervention" zijn, ziet itch als spam en die kunnen uit browse en search verdwijnen. Onze code en teksten komen van Claudes. Eerlijk taggen is verplicht (harde regel 5), en dan staat Hats op de pagina "AI Assisted". Dat botst met de geest van het besluit "geen AI-melding op Steam" (16 nov 21:05). **Dat is een keuze voor Thijs, niet voor ons.** Zonder zijn ja geen itch.

## 2. Per product: de 3 acties met de meeste kans

### Hats of the Fallen (hoofdzaak)

**Actie 1: een vangnet nu, vóór de Steampagina (maillijst plus Discord, één pagina op dortus.com).**
- Wat: `dortus.com/hats` (repo `dortus`) met één gif uit de build (Gloop met hoed, een held die valt), twee zinnen, een aanmeldvak "Tell me when Hats of the Fallen is on Steam (free demo)" en een Discordlink. Bio van @hatsofthefallen en elke kleine maak-clip wijzen daarheen tot de pagina er is. Op de paginadag één mail en één Discordbericht op hetzelfde uur als trailer en makers (Sems paginadag, plus deze twee).
- Waarom: Tiny Glade 28% doorklik uit mail tegen 1% uit sociale media (DERDEN); Gamblers Table hield zijn publiek via Discord vast tijdens de verificatie (DERDEN); onze TikTok heeft 1 volger (bord) en geen bestemming. Het kost geen geld en past op elk moment dat Valve kiest.
- Doel en 14 dagen (besluit "elke marketingactie een doel"): **100 aanmeldingen op wo 2 dec** (GOK; bij ±2,5 volgers per 1.000 weergaven uit Sems begroting vraagt dat ±40.000 weergaven, dus het is een rekdoel). Onder de 20: stoppen met clips voor Hats tot de paginadag, het lekt dan niet door.
- Wie: hoofdchat zet het op de lijst van Thijs; Chris clips; de site-agent bouwt de pagina; Sem telt.

**Actie 2: een speelbare proef buiten Steam, alleen als Thijs het AI-label op itch accepteert.**
- Wat: de speeltestbuild van na 21 nov (eerste ±30 minuten, save blijft geldig) gratis op itch.io: Windows-download, en een webversie als Olaf zegt dat de Godot 4.3-export de strook in de browser goed draait (GOK of de 3D-helden dat trekken). In het spel een knop "Get notified" naar het aanmeldvak, later "Wishlist on Steam". Tags idle, incremental, desktop pet, Godot. Thijs post zelf één gif in de feedbackdraad van r/incremental_games (Reddit kan alleen hij).
- Waarom: het enige voorbeeld in onze hoek dat aandacht haalde zónder Steampagina (Gamblers Table, en Survival Idle: 1.000 spelers in 24 uur met een itch-webbuild, [devlog](https://bearlikelion.itch.io/survival-idle/devlog/1108868/survival-idle-from-prototype-to-1000-players), DERDEN). En het levert echte spelers en hun klachten vóór de demo vastligt op 18 dec, wat we anders pas na 4 jan hebben.
- Waarom misschien niet: het AI-label (deel 1), itch-aandacht zakt zonder pagina (Gamblers Table), en Idlewood Outpost liet zien dat het ook niets kan doen. Olaf raadde het in plan B af; mijn nieuw feit is Gamblers Table (zelfde engine, zelfde wachten op verificatie) plus de lange wachttijd.
- Doel en 14 dagen: 1.000 downloads of webspelers en 50 aanmeldingen via de knop (GOK). Haalt het dat niet: pagina laten staan, geen moeite meer in.
- Wie: hoofdchat legt de AI-vraag aan Thijs voor (lijst-thijs); Olaf de builds en de knop; Thijs het itch-account en de Redditpost.

**Actie 3: het fest losmaken van de demo, en de pagina "klaar op de plank" zonder afkeur.**
- Wat: (a) de beslisdata uit deel 0 op het bord; (b) 6 tot 8 spelschermen in plaats van 5 (nieuwe eis van Valve); (c) de demo-app en demobuild **dezelfde dag** als de hoofdapp indienen, met de checklist van 3 nov (5 minuten via Steam gedraaid, Steam Cloud aan of uit, redistributables), want elke afkeur kost tot 12 werkdagen; (d) ook bij een pagina na 14 dec de pagina in het vak Upcoming van het fest.
- Waarom: één afgekeurde pagina of build schuift alles een fest op; de reviewrij is nu twee keer zo lang als in onze planning (DERDEN). Meedoen in Upcoming kost niets.
- Wie: Olaf en Daan (schermen, build), hoofdchat (bord, beslisdata).

### Click Joints Free en Pro, Bison & Flex, Garmin (kort, vanuit wat ik voor Steam vond)
- **Click Joints en Bison & Flex:** dezelfde maillijst-les (hoofdles 11 in `lessen.md` zegt het al voor Click Joints): één aanmeldvak per productpagina op dortus.com, en de changelog-naar-aankondiging-stap uit deel 3 werkt ook voor Superhive, Gumroad en de JetBrains-changelog. Verder is dit niet mijn onderwerp; andere agents in deze ronde gaan erover.
- **Garmin, Gloop's Hat Tower:** is als reclame voor Hats bedoeld. Zodra `dortus.com/hats` er is, hoort die link in de beschrijving van de horloge-app (als Garmin een link toestaat, GOK). Het kost niets.

## 3. Wat te automatiseren is

| # | Wat | Hoe | Kost | Thijs één keer |
|---|---|---|---|---|
| A1 | **Steam-aankondiging klaarzetten uit de changelog** | Steam heeft **geen API om aankondigingen te plaatsen**; wel een editor met "import HTML" (b, i, u, a, img en kopjes worden BBCode), concepten bewaren, een post "stagen" voor een latere datum en vertalingen via CSV (GEZIEN, `doc/marketing/event_tools` en `/import`). Script in de repo: leest de changelog van de demo of het spel, maakt Engels HTML in onze stijl (skill `update-tekst`), plus een omslag van 800 x 450 en een kop van 1920 x 622 (maten GEZIEN, `doc/store/assets/eventassets`) gesneden uit de winkelopname van `steam-hol-winkel.yml`. Uitkomst in een map met een vaste naam. Thijs plakt, keurt en zet het op "stage". | 0 | niets; per post plakken en publiceren (±2 min, GOK) |
| A2 | **Clips uit de build** | `steam-hol-clips.yml` bestaat (met de hand te starten). Uitbreiden: elke week vanzelf 5 tot 7 varianten (andere hoed, andere held, andere hoogte), en klaarzetten in Metricool als "ter keuring" (`createScheduledPostForReview`), nooit zelf plaatsen. Dat dekt het ritme van één clip per dag van Sem zonder gat in de kerst. | 0 (Metricool-account bestaat al, besluit 16 nov) | per week één keer keuren in Metricool |
| A3 | **Goedgekeurde Steampost door naar Discord** | Steam maakt voor elk spel een RSS-feed `steamcommunity.com/games/<appid>/rss` (GEZIEN, werkt met curl); een workflow elk uur zet nieuwe items via een Discord-webhook in ons eigen kanaal. Alleen tekst die Thijs al op Steam zette, dus geen nieuwe tekst onder zijn naam. Of dit onder "eigen kanaal" valt, beslist de hoofdchat. | 0 | Discordserver en één webhook maken |
| A4 | **Makerslijst bijhouden** | Elk YouTube-kanaal heeft een openbare feed `youtube.com/feeds/videos.xml?channel_id=...` (GEZIEN, werkt zonder sleutel). Dagelijkse workflow over de ±86 kanalen van Sem: nieuwe video met "upcoming", "desktop", "idle", "Next Fest" of "wishlist" in de titel komt als regel in `berichten/sem.md`. Zo weet Sem wanneer een lijstvideo in voorbereiding is (Fleurs, Gaming In The Wild maken maandlijsten). Contactgegevens blijven waar ze nu staan. | 0 | niets |
| A5 | **Festivals van derden** | Wekelijks `howtomarketagame.com/festivals/` ophalen (GEZIEN 200 met curl), verschil met vorige week in een bericht aan Sem. Sem kijkt nu met de hand; Taskbar Treasure Week (IndieLab en Mister Morris) kwam vorig jaar in december. | 0 | inzenden blijft bij Thijs |
| A6 | **Maillijst** | Kit (gratis tot 10.000 abonnees, [DERDEN](https://marcandrews.com/kit-free-plan-2026-is-10000-subscribers-really-free/)) met dubbele aanmelding; welkomstmail één keer door Thijs goedgekeurd en daarna automatisch; elke latere mail is een concept dat Thijs verstuurt. Aantal aanmeldingen per dag naar het scorebord via de Kit-API (GOK of de gratis laag de API heeft). | 0 | account maken; afzendernaam en **afzenderadres** kiezen (wet: een herkenbare afzender, Kit vraagt een postadres in de voet; geen woonadres in de repo, "staat bij Thijs"); privacyregel op de pagina goedkeuren |
| A7 | **Volgers tellen** | bestaat al (`memberslistxml`, `steam-fest-meting.yml`); alleen aanzetten op de dag dat het appid er is. Verlanglijsten blijven alleen zichtbaar voor Thijs. | 0 | appid als GitHub-variabele (staat al in Olafs lijst) |

## 4. Wat niet werkt of te duur is (niet proberen)
- **Aandacht zonder iets om op te klikken.** Little Writer: ±100k weergaven zonder pagina, 12 volgers (GEZIEN Fenna). Gamblers Table: itch-weergaven van duizenden naar honderden per dag tijdens het wachten op verificatie (DERDEN). Dus geen trailer en geen haak-clip vóór de paginadag; wel het vangnet.
- **Grote algemene kanalen voor een klein spel.** Pocket Cat Desktop: 40.000+ weergaven in twee Telegramkanalen, ±200 verlanglijsten (DERDEN); Desktop Survivors 98 kreeg IGN en GameGrumps en haalde 551 spelers tegelijk (GEZIEN Fenna).
- **Itch zonder plan voor de pagina, of itch met een verzwegen AI-label.** Het eerste deed Idlewood Outpost (4 reviews). Het tweede breekt de regels van itch en onze eigen regel.
- **Alles op het fest van 14 jan zetten** terwijl de app er niet is. Liever de beslisdata uit deel 0.
- **De demo vroeg uitbrengen om "toch iets" te hebben:** de Steam-mail naar verlanglijsten kan maar één keer, binnen 14 dagen na de eerste demodag (GEZIEN Sem). Een demo op een pagina met weinig verlanglijsten verbrandt die mail.
- **Beloningen voor verlanglijsten, volgen of reviews** (Valve verbiedt het; Bongo Cat moest stoppen, Fenna verhaal 16).
- **Betaalde festivals en showcases zonder besluit**, en betaalde advertenties: ik vond geen voorbeeld van een klein bureaubladspel waar advertenties vóór de pagina iets deden. Geen voorstel met bedrag, want ik heb geen getal om de opbrengst op te baseren.
- **Een routekaart vóór de uitgave** (Sem: 0 van 13 winnaars).

## Bronnen die nieuw zijn in deze ronde (allemaal met curl gelezen, 18 nov 2026)
- Valve reviewrij en nieuwe checklist: [VGC](https://www.videogameschronicle.com/news/steam-says-its-running-behind-when-reviewing-pre-release-games-because-of-how-many-re-reviews-it-has-to-do/), [Inven Global](https://www.invenglobal.com/articles/28152/valve-says-steam-pre-release-reviews-now-take-up-to-12-business-days)
- Onboarding (belastingcontrole tot 30 dagen, pagina 2 weken openbaar): `partner.steamgames.com/doc/gettingstarted/onboarding`
- Aankondigingen (geen API, HTML-import, stagen, RSS): `partner.steamgames.com/doc/marketing/event_tools`, `/event_tools/import`, `doc/store/assets/eventassets`
- Gamblers Table: [devlog](https://greenpixels.itch.io/gamblers-table/devlog/945763/wishlists-0-to-10000-in-just-three-weeks-)
- Survival Idle: [devlog](https://bearlikelion.itch.io/survival-idle/devlog/1108868/survival-idle-from-prototype-to-1000-players)
- Pocket Cat Desktop: [wnhub](https://wnhub.io/news/stores-and-publishing/item-52326)
- Rusty's Retirement: [GameDiscoverCo](https://newsletter.gamediscover.co/p/how-rustys-retirement-idle-farmed)
- Tiny Glade en maillijsten: [How To Market A Game](https://howtomarketagame.com/2023/06/12/marketing-your-steam-game-before-you-have-a-steam-page-the-tiny-glade-story/)
- itch.io-regels over generatieve AI: `itch.io/docs/creators/quality-guidelines`
- Kit gratis laag: [marcandrews.com](https://marcandrews.com/kit-free-plan-2026-is-10000-subscribers-really-free/)

Niet gelukt: de festpagina `themed_sales/desktop_companion_2027` gaf vandaag "Sorry, an error occurred" (ik vertrouw op Sanne's lezing van 9 nov). Getallen voor de eerste 2 maanden van Rusty's, Tiny Pasture en Bao Bao vond ik niet; die makers deelden alleen totalen.
