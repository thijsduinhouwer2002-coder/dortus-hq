# Waar komen de beelden vandaan? Onderzoek voor Het Hol (en Ebb 1.1)

Geschreven 13 nov 2026 door een onderzoeksagent van de hoofdchat. Alleen gelezen, niets gekocht, nergens ingelogd. Labels: GEZIEN (zelf gelezen of gemeten, met bron en datum), AFGELEID (eigen redenering uit wat ik zag), GOK (niet nagegaan), DERDEN (een site van een ander zegt het, niet de maker zelf).

## Samenvatting (voor Thijs)

1. **Advies:** laat de kern van Het Hol door mensen maken: een pixelartiest voor Gloop, de helden en een set voorwerpen, en een illustrator voor de capsule (de winkelafbeelding). Geen AI-beeld in wat de koper ziet.
2. **Waarom:** in onze eigen hoek (232 bureaublad-apps met reviews, vandaag gemeten) heeft geen enkele van de 18 apps met 1.000+ reviews een AI-verklaring, en de grote apps die er wel een hebben schrijven er vrijwel allemaal bij dat het beeld met de hand is gemaakt. Kopers in deze hoek straffen AI-beeld (Librarian, Vapor World, Heartopia).
3. **Kosten:** capsule $400 tot $700, pixelwerk kern ongeveer $800 tot $1.300. Samen ongeveer 1.200 tot 2.000 euro. Met een paar honderd euro: alleen de capsule laten maken. Met nul: blijven bij de huidige code-pixelart plus gratis CC0-pakketten.
4. **Tijd:** haalbaar vóór 1 december als je deze week (uiterlijk ma 16 of di 17 nov) bestelt; capsules duren 1 tot 3 weken. Gloop en twee helden eerst, de rest vóór 14 januari.
5. **Wat jij doet (ongeveer 6 tot 8 uur verspreid):** 1 uur kiezen uit drie portfolio's per opdracht, 4 keer 20 minuten keuren op vaste momenten (schets, eerste figuur in het spel, set, capsule), betalen. Agents schrijven de opdracht, zetten alles in het spel, maken de vergelijkingsbladen en regelen de toets met een frisse kijker.
6. **Vaste regels uit Ebb:** eerst één figuur (Gloop) helemaal goed op het echte scherm, dan de rest; jij keurt smaak, op vaste momenten, met hoogstens drie beelden per keer; herkennen toetst iemand die niet weet wat het is; vooraf opgeschreven wat klaar is.
7. **De proef van een uur:** maak met PixelLab (ongeveer $12 voor een maand, opzegbaar) Gloop in drie houdingen en één loopje van een held; een agent zet ze in het spel naast de huidige figuren. Wint PixelLab niet duidelijk bij jou en bij een frisse kijker, dan is de AI-route af en gaat het geld naar een tekenaar. Wint het wel, dan beslis je bewust of je de AI-verklaring op de winkelpagina wilt.
8. **Garmin:** plaatjes mogen in Connect IQ en lossen het herkenprobleem van Ebb op als een tekenaar de dieren maakt; geheugen is te doen voor kleine plaatjes. Voor 1.1, niet nu.

## 1. Wat er nu is (GEZIEN in de repo, 13 nov)

- **Ebb** (`ontwerp/garmin/ebb-blad-voor-thijs-1.png`, `winkel-echt/0-poster-v5.png`): nette schermen, goede tekst, maar de dieren zijn vlakke vormen uit code. De krab in de zwemband werkt, kleinere voorwerpen niet (slipper, telescoop: besluiten 12 nov 06:00 en 11:50). Op de poster ogen de 24 dieren als clipart: verschillende dikte van randen, verschillende stijl per dier.
- **Het Hol** (`platformen/steam/`, `ontwerp/steam/`): een bureaublad-strook (120 px hoog) waarin jij het hol bent; helden lopen naar binnen, de eenogige slijm Gloop eet ze op en draagt hun hoeden als toren. Stijl volgens `ontwerp/steam/mila/stijl.md` en `overdracht.md`: pixelart, cellen 16 x 16, schaal 3, pruimkleurige aarde, warm licht van fakkels en goud, Gloop muntgroen. Alles getekend uit Python (`kunst-bron/maak_kunst.py`, `maak_karakter.py`, `mila/bron/*.py`).
- `kunst-bron/voorbeeld-strook.png` bekeken: dit is veel beter dan de Ebb-dieren. AFGELEID: pixelart op 16 pixels is precies het soort beeld dat code redelijk kan, omdat er per figuur maar een paar honderd pixels zijn. Wat ontbreekt is karakter: de helden zijn generieke poppetjes, Gloop is herkenbaar maar niet om verliefd op te worden, en er is geen enkele "dat wil ik hebben"-figuur. Dat is precies wat een winkelpagina verkoopt.
- `winkelpagina/vergelijk-v5-header.png`: onze header ("Hats of the Fallen") staat naast Rusty's Retirement, Tiny Pasture en Spirit City. Die drie hebben een getekende, glanzende illustratie; de onze is een opgeschaalde spelstrook. AFGELEID: de capsule is het zwakste punt, en het punt waar een mens het meeste verschil maakt.

## 2. Route 1: beeldgeneratoren die Thijs zelf bedient

| Hulpmiddel | Wat het goed kan | Prijs | Commercieel gebruik | Bron, datum |
|---|---|---|---|---|
| **PixelLab** | Echte pixelart (eigen modellen), figuur in 4 of 8 richtingen, animaties (lopen, rust, aanval), tilesets, doorzichtige achtergrond, stijlreferentie, vaste palette | Gratis proef (40 snelle generaties, daarna 5 per dag, DERDEN). Abonnement ongeveer $12, $29 tot $35 en $50 per maand (DERDEN, knowara.com; de prijspagina van PixelLab laadt alleen met JavaScript). Animatie vraagt minstens Tier 1 (GEZIEN, docs) | "Yes, we only ask that you do not train new models with the images" (GEZIEN, FAQ in pixellab.ai/llms-full.txt, 13 nov) | pixellab.ai/llms.txt en llms-full.txt, 13 nov |
| **Retro Diffusion** | Pixelart van 12 tot 256 px, vaste palette (`input_palette`), doorzichtige achtergrond (`remove_bg`), animaties lopen/rust/springen vanaf een eigen beginbeeld (32 tot 256 px), eigen stijl uit één referentiebeeld | Per beeld: RD Fast ongeveer $0,03, RD Pro $0,18, RD Core met referentie $0,10 (GEZIEN). Losse Aseprite-uitbreiding $65 of Lite $20 (DERDEN, cinevva) | Lokale uitvoer commercieel bruikbaar (DERDEN, cinevva noemt verklaring van de maker) | github.com/Retro-Diffusion/api-examples README, 13 nov |
| **Scenario** | Eigen stijlmodel trainen op je eigen beelden (30 minuten tot een paar uur), veel algemene modellen | Starter $15, Pro $45 per maand (training pas bij Pro), Max $75 (GEZIEN) | Voorwaarden staan commercieel gebruik toe; geen garantie op uniek of auteursrecht (DERDEN, cinevva over voorwaarden 4.3 tot 4.5) | scenario.com/pricing, 13 nov |
| **Midjourney** | Mooiste losse illustraties, stijlreferentie (`--sref`) en figuurreferentie (Omni Reference) | Basic $10, Standard $30, Pro $60, Mega $120 per maand; zonder Pro zijn je beelden openbaar; bedrijven boven $1 miljoen omzet moeten Pro of Mega (DERDEN, eesel.ai 2026; de site van Midjourney gaf 403 op curl) | Betaalde abonnementen mogen commercieel (DERDEN) | eesel.ai/en/blog/midjourney-pricing, 13 nov |
| **ChatGPT / OpenAI-beeld** | Goed in opdrachten volgen, bewerken met referentiebeelden, doorzichtige achtergrond (`background: transparent`), sinds kort ook bewegende GIF van 2 tot 16 beeldjes | Via abonnement van ChatGPT, of API (zie route 2) | GOK: voorwaarden niet gelezen | developers.openai.com image-generation guide, 13 nov |
| **Leonardo, Ludo, Sprixen, Sprite-AI** | Algemeen beeld (Leonardo), animatie van een bestaande sprite (Ludo, Sprixen, Sprite-AI) | Leonardo gratis 150 tokens per dag (beelden openbaar); Ludo $20 per maand (zonder betaling watermerk); Sprixen $10; Sprite-AI $8 (DERDEN, cinevva, nagekeken 8 nov 2026) | Volgens cinevva bij betaalde plannen commercieel | app.cinevva.com/guides/ai-pixel-art-generators, 13 nov |

**Eén stijl en één figuur vasthouden (AFGELEID uit de docs hierboven):** de pixel-specifieke hulpmiddelen hebben er knoppen voor die algemene generatoren missen: vaste palette (Retro Diffusion, PixelLab "forced palettes"), een stijlbeeld als referentie, en animatie vanaf jouw eigen eerste beeldje (dat beeldje blijft frame 1, GEZIEN in PixelLab-docs). Voor Het Hol betekent dat: geef altijd de huidige strook en het pruimpalet mee. Midjourney en ChatGPT maken mooiere losse plaatjes, maar geen schone pixels op 16 px; die moeten daarna door "image to pixel art" of door een agent teruggebracht worden, en dan gaat juist het mooie eraf.

**Valkuil voor Het Hol:** onze figuren zijn 10 tot 16 pixels hoog. De meeste hulpmiddelen werken vanaf 32 x 32 (PixelLab-canvas minimaal 32 x 32 voor veel gereedschap; Retro Diffusion-animaties vanaf 32 px, GEZIEN). AFGELEID: je maakt dan op 32 px en snijdt bij, of je kiest bewust voor grotere figuren (Gloop past in de schatkamer van 32 spelpixels hoog). Verkleinen van pixelart met factor 2 maakt het kapot.

## 3. Route 2: beeld via een API die een agent aanroept

Alles hieronder vraagt een sleutel die Thijs aanmaakt en als geheim in GitHub zet (nooit in de repo). Dan kan een agent zelf beelden maken en Thijs alleen kiezen.

- **PixelLab API en MCP-server** (GEZIEN, pixellab.ai/pixellab-api en /mcp, 13 nov): werkt met Claude Code, met Godot als aanbevolen motor. Voorbeeldprijzen: één pixelbeeld met doorzichtige achtergrond 32 x 32 tot 128 x 128 ongeveer $0,024 tot $0,029; bewerken $0,023; "image to pixel art" ongeveer $0,02 tot $0,03; figuur in 8 richtingen in één aanroep. De site noemt het schattingen, geen vaste prijzen.
- **Retro Diffusion API** (GEZIEN, README 13 nov): sleutel aanmaken op retrodiffusion.ai/app/devtools, vooraf tegoed in dollars, mislukte beelden worden terugbetaald, gratis prijscheck vooraf (`check_cost`), ook een MCP-server met 33 functies. Prijzen zie tabel.
- **OpenAI** (GEZIEN, developers.openai.com/api/docs/pricing en image-generation, 13 nov): gpt-image-2 $15 per miljoen uitvoertokens beeld (batch), gpt-image-2.6 $30 per miljoen; prijs per beeld via hun rekenhulp, ruwweg $0,03 tot $0,06 per gewoon beeld (DERDEN, unifically.com). Doorzichtige achtergrond en GIF-uitvoer gedocumenteerd.
- **Google Gemini-beeld** (GEZIEN, ai.google.dev/gemini-api/docs/pricing, 13 nov): ongeveer $0,017 tot $0,15 per beeld, afhankelijk van model en maat (1K, 2K, 4K).

AFGELEID: technisch kan een agent dus wel beelden maken. Het probleem van Ebb blijft: een agent kan niet betrouwbaar kiezen welk van de tien het mooiste is. De API helpt alleen als Thijs per ronde een blad van hoogstens drie kandidaten krijgt.

## 4. Route 3: gereedschap speciaal voor spelbeeld

PixelLab en Retro Diffusion zijn de twee die echt voor pixelart en sprites gemaakt zijn (zie boven). Daarnaast:
- **Aseprite** (pixel-editor, ongeveer $20 eenmalig, GOK op de prijs): nodig als iemand met de hand pixels bijwerkt; PixelLab en Retro Diffusion hebben er een uitbreiding voor. Gratis alternatieven: Piskel, LibreSprite (DERDEN, cinevva).
- **Ludo, Sprixen, Sprite-AI**: maken van één figuur een animatie; Ludo levert zonder betaalde aankoop alleen beelden met watermerk (DERDEN).
- Geen van deze kan ik zelf testen. GOK: op 16 px blijven animaties van AI wiebelig (pixels die per beeldje verspringen). Dat is precies wat de proef moet laten zien.

## 5. Route 4: kant-en-klare pakketten (GEZIEN op de pagina's, 13 nov)

| Pakket | Link | Prijs | Licentie | Past bij Het Hol? |
|---|---|---|---|---|
| Kenney, Tiny Dungeon (16 x 16, 130 bestanden) | kenney.nl/assets/tiny-dungeon | gratis | CC0, ook commercieel ("all game assets ... public domain licensed (CC0)", kenney.nl/support) | Kerker en helden op 16 px; heel bekend |
| 0x72, 16x16 DungeonTileset II | 0x72.itch.io/dungeontileset-ii | zelf prijs kiezen | CC0; pagina zegt "No generative AI was used" | Bijna exact ons formaat, met helden en monsters; zeer veel gebruikt |
| Pixel_Poem, 2D Pixel Dungeon Asset Pack | pixel-poem.itch.io/dungeon-assetpuck | zelf prijs kiezen | gratis en commercieel, niet doorverkopen | Kerker, val, helden met rust-animatie |
| Pixel Frog, Tiny Swords | pixelfrog-assets.itch.io/tiny-swords | gratis, extra pakket vanaf $15 | commercieel mag, niet doorverkopen | Mooi, maar 64 x 64 raster: te groot voor onze strook |
| Cup Nooble, Sprout Lands | cupnooble.itch.io/sprout-lands-asset-pack | gratis alleen niet-commercieel; vanaf $3,99 commercieel | commercieel na betaling, niet doorverkopen | Gezellig boerderijdieren-gevoel, niet ons hol |
| Kenmi, Cute Fantasy RPG (16 x 16) | kenmi-art.itch.io/cute-fantasy-rpg | vanaf $3,99 voor commercieel | idem | Gezellig 16 px, dieren |
| Game Endeavor, Mystic Woods (16 x 16) | game-endeavor.itch.io/mystic-woods | betaalde versie voor commercieel | idem | Bos, slijm, helden |

**Nadeel (AFGELEID):** spelers in deze hoek kennen deze pakketten; Kenney en 0x72 zie je in honderden spellen. Ons hele plan is een eigen gezicht (pruim, Gloop met één oog, hoedentoren). Een pakket als basis voor muren, kisten en kleingoed is prima en goedkoop; voor Gloop, de helden en de capsule niet. Let op: bij Cup Nooble, Kenmi en Game Endeavor is de gratis versie niet commercieel.

## 6. Route 5: een tekenaar inhuren

**Waar (GEZIEN of DERDEN):** Fiverr (zoek "pixel art character animation", "steam capsule"), itch.io-profielen van makers van pakketten (veel nemen opdrachten aan), Reddit r/gameDevClassifieds en r/HungryArtists (GOK, niet gelezen), ArtStation, losse carrd-pagina's met vaste prijzen.

**Prijzen die ik zag:**
- Pixelfiguur: één sprite onder 64 x 64 $20; elk extra animatiebeeldje 50 procent van de basisprijs, dus ongeveer $10 per beeldje (GEZIEN, zoiskart.carrd.co, 13 nov). Andere: losse pixelfiguur $20, met 3 beeldjes $50 (ceruleanwake.carrd.co).
- Uurtarief 2D-spelbeeld: middenniveau $25 tot $50, ervaren $60 tot $100 in Europa en Noord-Amerika (DERDEN, rocketbrush.com).
- Capsule: "$300 to 600 for fully custom capsule work", bodem $250, budget $130 tot $150 als iemand jouw bestaande beeld omwerkt (DERDEN, steampageanalyzer.com, bijgewerkt 2 nov 2026). Eén illustrator: indie-capsule $500 tot $700, 8 tot 12 dagen na start voor een figuur (GEZIEN, cyanidesid.carrd.co). Een Fiverr-verkoper met 54 reviews: opdrachten van $200 tot $400 in 3 tot 4 weken, $600 tot $800 in 2 weken (GEZIEN, fiverr.com/benfun, reviews op de pagina).

**Wat Het Hol dan kost (AFGELEID uit die prijzen):**
| Onderdeel | Inhoud | Schatting |
|---|---|---|
| Gloop | basis plus rust, hap, slapen, plat, opstaan, laars spugen: 6 animaties van 4 tot 6 beeldjes | $250 tot $400 |
| Helden | 5 soorten: lopen (4) en vallen (4) beeldjes, hoeden los | $300 tot $500 |
| 20 voorwerpen | schat, kist, fakkel, put, vondsten, hoeden | $250 tot $400 |
| Capsule | header 920 x 430 plus de andere maten uit één illustratie | $400 tot $700 |
| Totaal | | **$1.200 tot $2.000** |

**Haalbaar vóór 1 december?** AFGELEID: ja voor de capsule en voor Gloop plus twee helden, als je uiterlijk 17 november bestelt; de rest van de set past vóór 14 januari. Winkelbeelden mag je na 1 december nog vervangen (GOK: niet nagelezen in de Steam-regels, wel gangbaar). Grootste risico: een tekenaar die uitloopt. Kies daarom iemand met korte levertijd op de pagina en betaal in delen (de helft vooraf is gangbaar, GEZIEN bij wardino.carrd.co).

## 7. Route 6: Steam en AI-beeld

**Wat Valve vraagt (GEZIEN, partner.steamgames.com/doc/gettingstarted/contentsurvey, 13 nov):** deel 3 van de Content Survey gaat over generatieve AI. Hulpmiddelen die alleen het werk versnellen tellen niet; het gaat om "content that ships with your game, and is consumed by players", zoals "artwork, sound, narrative, localization". Twee vakjes: vooraf gemaakt (Pre-Generated) en tijdens het spel (Live-Generated). Volgens VGC (17 jan 2026) telt ook beeld op de winkelpagina en in marketing, en komt jouw uitleg op de winkelpagina in het blok "AI Generated Content Disclosure". AFGELEID: schetsen en moodboards die Thijs met AI maakt om een tekenaar uit te leggen wat hij wil, gaan niet mee in het spel en vallen er dus niet onder.

**Hoe kopers reageren:**
- Librarian: Tidy Up the Arcane Library, gezellig hit van 2026: vier bewerkte beelden plus taalcorrectie met AI gaf negatieve reviews, streamers die afhaakten, en twijfel of de verklaring wel volledig was; bleef wel "Very Positive" (GEZIEN, Kotaku 4 juni 2026).
- Vapor World: 100.000 verlanglijsten, maar AI-tussenfilmpjes gaven "mostly negative" (64 reviews); de studio verving ze binnen een week (GEZIEN, PC Gamer 24 aug 2026).
- Heartopia (gezellige sim, jan 2026): niet-gemelde AI-beelden, reviews zakten naar 65 procent gemengd (DERDEN, aicerts.ai).
- Peiling onder pc-spelers: 43 procent heeft geen probleem met een AI-verklaring, 31 procent ziet het negatief, 8 procent koopt dan niet (GEZIEN, pcguide.com, nov 2026).
- Bijna de helft van de nieuwe Steam-spellen in oktober 2026 had een AI-verklaring (49,9 procent); bij spellen met 1.000+ reviews maar 14 procent (GEZIEN, finalboss.io, 3 nov 2026).

**Eigen meting in onze hoek (GEZIEN, 13 nov 07:30 tot 07:58 UTC):** van alle 232 bureaublad-apps met minstens één review uit de lijst van Vera heb ik de winkelpagina opgehaald en gekeken of het AI-blok er staat. Data: `ontwerp/beelden-onderzoek-2026-11-13-ai-verklaringen.json`.
- 63 van 232 (27 procent) hebben een AI-verklaring.
- Van de 18 apps met 1.000+ reviews: **0**. Van de 53 met 300+: 6. Van de 88 met 100+: 14.
- De grote die er wel een hebben, zeggen er bijna allemaal bij dat het beeld met de hand is: Sill Cats (767 reviews, 93 procent: "All cat sprite art consists of hand-drawn work"), Mushroom Nook (486, 98 procent: alle kerninhoud door henzelf), The Dream Globe (381, 94 procent: alleen een paar winkelbeelden uit AI-schetsen).
- Apps die AI voor het beeld zelf gebruiken scoren vaak laag: Desk Top Racer 61 procent, Task Bar Cube 27 procent (AI voor de winkelpagina), fanxiu 8 procent, My Shelter 45 procent. Er zijn uitzonderingen met weinig reviews: Corgi Corgi Cor! 97 procent (42 reviews), Daily Botanica 96 procent (25).
- AFGELEID, met voorbehoud: dit is samenhang, geen bewijs van oorzaak (kleine makers gebruiken vaker AI en hebben ook om andere redenen minder reviews). Maar in deze hoek is "handgemaakt" duidelijk wat de toppers uitdragen, en een AI-blok onder een gezellig spel is iets wat kopers lezen.

**Wat het betekent voor de keuze:** AI-beeld in Het Hol kan, mits gemeld, maar het kost een deel van de kopers en geeft een vlek op de pagina in precies de hoek waar handgemaakt telt. Ook auteursrecht op puur AI-beeld is onzeker (GOK, niet nagelezen voor 2026), dus een ander mag een AI-Gloop mogelijk gewoon namaken. Advies: geen AI in wat de koper ziet; AI mag als kladblok voor Thijs.

## 8. Route 7: Garmin, kort

- **Mag het?** Ja. Plaatjes zet je als `<bitmap id=... filename=...png/>` in `resources/drawables/drawables.xml`; Ebb doet dat al voor het icoon (GEZIEN, `producten/garmin-proef/resources/drawables/drawables.xml`). Een getekend dier wordt dan een klein PNG in plaats van code.
- **Kleuren:** een buffer-plaatje mag een eigen palet hebben van hoogstens 256 kleuren (GEZIEN, developer.garmin.com api-docs Toybox/Graphics). Uit mijn hoofd, niet nagelezen (de pagina over resources laadt alleen met JavaScript): de resource-compiler zet een PNG om naar de kleuren van het horloge, met een keuze voor dithering en een eigen palet per plaatje. AFGELEID: laat een agent elk PNG vooraf zelf terugbrengen naar het palet van 64 kleuren en geen dithering gebruiken; dan zie je in de simulator precies wat de koper ziet.
- **Geheugen:** AFGELEID: een plaatje van 60 x 60 pixels met 64 kleuren is ruwweg 2 tot 4 KB; 25 dieren in één houding samen minder dan 100 KB. Op nieuwere horloges (API 4 en hoger) gaan plaatjes in een aparte grafische geheugenpool (uit mijn hoofd; Ebb mat die pool al, zie besluiten 12 nov 01:20). Voor de kleinste horloges moet Gijs het meten, niet aannemen.
- **Gevolg:** voor Ebb 1.1 lost "dieren als plaatjes van een tekenaar" het herkenprobleem beter op dan meer code. Een set van 25 kleine dieren bij dezelfde pixelartiest als Het Hol: ruwweg $500 tot $750 (AFGELEID uit $20 tot $30 per sprite).

## 9. Drie werkwijzen voor Het Hol

Vaste regels in alle drie (lessen van Ebb):
- **Eén voorbeeld eerst:** Gloop in rust en hap, in de echte build, op ware grootte op een echt bureaublad. Pas als dat goed is komt de rest.
- **Thijs is de poort voor smaak**, op vier vaste momenten, met hoogstens drie beelden per keer, altijd op een blad naast de huidige versie en naast Rusty's Retirement en Tiny Pasture.
- **Herkennen** toetst een frisse kijker die alleen het plaatje op ware grootte ziet en zegt wat het is (eerst een frisse agent als filter, dan één mens die het spel niet kent).
- **Klaar is vooraf opgeschreven:** (1) de frisse kijker noemt Gloop, een held en drie willekeurige voorwerpen goed op ware grootte; (2) Thijs zegt "ja" op het blad naast de twee toppers; (3) geen veeg: alleen hele schalen, nearest; (4) alleen kleuren uit het palet in `stijl.md`; (5) doorzichtige achtergrond, vaste maat per cel.

### Werkwijze A: mensen maken de kern (advies)
| Stap | Wie | Uren Thijs | Kosten | Waar het mis kan gaan |
|---|---|---|---|---|
| 1. Opdracht schrijven: stijl.md, palet, maten, lijst figuren en animaties, voorbeeldstrook, toppers ter vergelijking | agent | 0 | 0 | te vaag: dan tekent de tekenaar zijn eigen stijl |
| 2. Drie pixelartiesten en drie capsule-tekenaars zoeken met prijs, levertijd en portfolio dat op ons lijkt | agent (lezen) | 0 | 0 | agent kiest op smaak; daarom alleen een korte lijst |
| 3. Kiezen en bestellen, aanbetaling | Thijs | 1 | helft vooraf | lange levertijd; kies op levertijd |
| 4. Schets Gloop en capsule-opzet | tekenaar | 0,3 keuren | in prijs | te veel rondes: spreek twee correctierondes af |
| 5. Gloop in de build, blad op ware grootte, frisse kijker | agent | 0,3 keuren | 0 | schalen of kleuren verkeerd in Godot; agent toetst op veeg |
| 6. Rest van de set (helden, voorwerpen) | tekenaar | 0 | in prijs | stijl loopt weg: elke levering naast Gloop leggen |
| 7. Set in de build, blad, frisse kijker | agent | 0,3 keuren | 0 | |
| 8. Capsule af, alle Steam-maten afgeleid, naast toppers | tekenaar en agent | 0,3 keuren | in prijs | tekst onleesbaar klein: agent toetst op 231 x 87 |
| Totaal | | **ongeveer 3 uur keuren plus 1 uur kiezen, met overleg 6 tot 8 uur** | **$1.200 tot $2.000** | |

### Werkwijze B: Thijs met een pixel-AI, agent maakt het schoon
| Stap | Wie | Uren Thijs | Kosten | Waar het mis kan gaan |
|---|---|---|---|---|
| 1. Referentieblad en exacte opdrachten per figuur | agent | 0 | 0 | |
| 2. Per figuur 4 tot 8 versies maken, beste kiezen | Thijs in PixelLab of Retro Diffusion | 4 tot 8 (voor 40 figuren en voorwerpen) | $12 tot $50 per maand | eindeloos rerollen; zet een grens van 8 pogingen per figuur |
| 3. Terug naar palet, rasters gelijk, bijsnijden, in de build | agent | 0 | 0 | wiebelige animaties, pixels die verspringen |
| 4. Blad en frisse kijker, keuren | agent, Thijs | 1 | 0 | |
| 5. Capsule: bij voorkeur toch een mens; anders Thijs met Midjourney of ChatGPT | tekenaar of Thijs | 1 tot 2 | $400 tot $700 of $30 | AI-capsule valt het meest op en wordt het snelst afgebrand |
| 6. AI-verklaring invullen op de winkelpagina | agent | 0 | 0 | kopers die afhaken, reviews over AI |
| Totaal | | **6 tot 11 uur** | **$50 tot $750** | |

### Werkwijze C: nul euro
| Stap | Wie | Uren Thijs | Kosten | Waar het mis kan gaan |
|---|---|---|---|---|
| 1. Muren, kisten, vondsten uit CC0 (0x72, Kenney) als basis, omgekleurd naar pruim | agent | 0 | 0 | herkenbaar als "dat pakket" |
| 2. Gloop en helden blijven code-pixelart, maar per figuur één ronde: drie varianten op een blad | agent, Thijs kiest | 1 | 0 | agent kan geen karakter verzinnen; Thijs kiest uit middelmaat |
| 3. Capsule uit een echte schermafbeelding van de strook op een bureaublad, met logo | agent, Thijs keurt | 0,5 | 0 | zwakker dan de getekende capsules van de toppers |
| Totaal | | **ongeveer 2 uur** | **0** | |

## 10. Advies per budget

- **Nul:** werkwijze C. Het Hol ziet er dan netjes uit maar niet onderscheidend. Eerlijk: de code-pixelart van Het Hol is al beter dan de Ebb-dieren, dus dit is geen ramp, maar de capsule blijft het zwakke punt.
- **Een paar honderd euro:** alleen de **capsule** laten tekenen ($400 tot $600), de rest werkwijze C. Reden: de capsule bepaalt of iemand klikt, en is het enige beeld dat iedereen ziet; het kost hetzelfde of de klikratio nu 1 of 2 procent wordt (DERDEN, steampageanalyzer). Laat de tekenaar Gloop in de capsule ontwerpen en gebruik die tekening daarna als voorbeeld voor de pixel-Gloop.
- **Duizend tot tweeduizend euro:** werkwijze A volledig, bij één pixelartiest voor alle sprites (één hand, één stijl) en één illustrator voor de capsule. Zelfde pixelartiest later voor de Ebb-dieren (1.1).
- **Mijn keuze:** A, met in elk geval de capsule nu bestellen. Reden: Thijs wil dat Het Hol echt mooi en onderscheidend is, de agents kunnen dat aantoonbaar niet beoordelen, en in deze hoek is handgemaakt beeld wat de toppers verkoopt. De proef hieronder is goedkoop genoeg om B eerlijk een kans te geven voordat het geld weg is.

## 11. De proef van een uur

**Vraag:** kan Thijs met PixelLab in een uur figuren maken die bij een frisse kijker en bij hem duidelijk winnen van de huidige code-pixelart?

**Vooraf (agent, geen tijd van Thijs):** in `ontwerp/steam/proef-beeld/` zet een agent:
- `referentie.png`: de huidige strook en Gloop op 8 keer vergroot (nearest), plus één held;
- `palet.png`: de kleuren uit `stijl.md` als strook;
- `opdrachten.txt`: de exacte teksten hieronder, en de klaar-criteria.

**Stappen voor Thijs (60 minuten):**
1. (5 min) Maak een PixelLab-account en neem één maand Tier 1 (ongeveer $12, direct opzeggen kan). Animatie zit niet in de gratis proef.
2. (15 min) "Create image" met stijlreferentie `referentie.png` en vaste palette `palet.png`, canvas 32 x 32, doorzichtige achtergrond, zijaanzicht. Opdracht: "one-eyed mint green slime, crooked grin, one tooth, side view, cute, pixel art, figure about 14 pixels tall, transparent background". Maak er hoogstens 8, kies de beste 1.
3. (15 min) Van die ene Gloop twee houdingen: "mouth wide open, biting" en "asleep, eye closed, flattened". Hoogstens 4 pogingen per houding.
4. (15 min) "Animate with text" op de huidige held (upload uit `referentie.png`): "walking to the right, 4 frames". Hoogstens 4 pogingen.
5. (5 min) Download de 3 Gloop-PNG's en het loopje, en upload ze via de GitHub-website naar `ontwerp/steam/proef-beeld/aangeleverd/`. Klaar; de rest doet een agent.

**Daarna (agent, geen tijd van Thijs):** terug naar het palet, rasters gelijk, in een proefbuild van Het Hol, schermafbeelding op ware grootte en op 3 keer, naast de huidige figuren. Een frisse agent en daarna één mens die het spel niet kent zeggen wat ze zien. Thijs krijgt één blad met twee kolommen (nu, PixelLab) en kiest (10 minuten, buiten het uur).

**Klaar-criteria, vooraf vastgelegd:** de PixelLab-route gaat alleen door als (1) Thijs zonder twijfel de PixelLab-kolom kiest, (2) de frisse kijker Gloop als "slijm of monster met één oog" en de held als "ridder of avonturier die loopt" herkent, en (3) het loopje op ware grootte niet wiebelt. Haalt het één punt niet, dan is route B af en gaat het geld naar werkwijze A. Haalt het alles, dan beslist Thijs bewust of hij de AI-verklaring wil, met de meting uit hoofdstuk 7 erbij.

## 12. Wat ik niet kon nagaan

- De officiële prijzen van PixelLab en Midjourney (pagina's laden alleen met JavaScript of gaven 403); die komen van derden.
- Kwaliteit van alle hulpmiddelen: ik heb niets gemaakt, alleen gelezen.
- De Garmin-pagina over resources (dithering, palet per plaatje) laadt niet met curl; dat deel komt uit mijn hoofd.
- Of Steam-winkelbeelden na goedkeuring vrij te vervangen zijn, en de stand van het auteursrecht op AI-beeld in 2026.
- Of de genoemde tekenaars nu plek hebben vóór 1 december.
- Reddit r/gameDevClassifieds en r/HungryArtists niet gelezen.

## Bronnen (allemaal gelezen met curl op 13 nov 2026, tenzij anders vermeld)
- Valve: partner.steamgames.com/doc/gettingstarted/contentsurvey
- videogameschronicle.com/news/valve-has-significantly-rewritten-steams-rules-for-how-developers-much-disclose-ai-use (17 jan 2026); gamingonlinux.com/2026/01/valve-tweak-steam-ai-disclosure-form-for-developers-to-clarify-its-for-content-consumed-by-players
- kotaku.com/librarian-tidy-up-arcane-library-steam-game-cozy-ai-2000702089 (4 juni 2026); pcgamer.com "Steam Week in Review: A touch of AI ..." (24 aug 2026); aicerts.ai/news/heartopias-52k-peak-amid-ai-art-backlash; pcguide.com poll over AI-verklaringen; finalboss.io/steam-ai-disclosures-hit-49-9-what-buyers-should-check (3 nov 2026)
- Eigen meting: store.steampowered.com/app/<id> voor 232 apps, data in `ontwerp/beelden-onderzoek-2026-11-13-ai-verklaringen.json`
- pixellab.ai/llms.txt, pixellab.ai/llms-full.txt, pixellab.ai/pixellab-api, pixellab.ai/mcp; knowara.com/ai-tools/image/pixellab-review
- github.com/Retro-Diffusion/api-examples (README)
- scenario.com/pricing; eesel.ai/en/blog/midjourney-pricing; app.cinevva.com/guides/ai-pixel-art-generators (nagekeken door cinevva 8 nov 2026)
- developers.openai.com/api/docs/pricing en /api/docs/guides/image-generation; ai.google.dev/gemini-api/docs/pricing
- kenney.nl/support, kenney.nl/assets/tiny-dungeon; de itch.io-pagina's in hoofdstuk 5
- zoiskart.carrd.co, ceruleanwake.carrd.co, cyanidesid.carrd.co, wardino.carrd.co, fiverr.com/benfun/do-professional-game-illustration, rocketbrush.com/blog/2d-character-art-prices-and-tips-to-cut-costs, steampageanalyzer.com/blog/indie-game-marketing-1000-budget
- developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html en BufferedBitmap.html
