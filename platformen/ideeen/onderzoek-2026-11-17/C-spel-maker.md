# Groep C: spellen, 3D en makers (17 nov 2026)

Alles gelezen met curl op 17 nov 2026, tenzij anders vermeld. GEZIEN = zelf op de bron gelezen. GOK = mijn inschatting.

### 1. Minecraft-pluginwinkels (PixelEast, voxel.shop, BuiltByBit, SpigotMC)
- Bestaat: JA. GEZIEN: PixelEast-blog "The 5 Best Minecraft Plugin Marketplaces in 2026", 16 nov 2026, https://pixeleast.com/blog/best-minecraft-plugin-marketplaces . Daarin: PixelEast 6,9%, voxel.shop 2 tot 8%, BuiltByBit 9,9% plus promotiekosten, SpigotMC 0% (betaling via PayPal rechtstreeks), MCModels 10%. Betaalmiddelen PixelEast: kaart, Apple Pay, Google Pay, PayPal. voxel.shop heet sinds april 2026 zo (was Polymart), is in bèta, en de eigenaar is volgens de blog in nov 2026 "een paar maanden grotendeels afwezig".
- Wat het echt is: PixelEast (Lootridge s.r.o., Tsjechië) is een nieuwe winkel uit 2026 voor Minecraft en Hytale. GEZIEN op https://pixeleast.com/about-us : 1.028 producten, 221 makers. Op de voorpagina hebben de uitgelichte producten 1 tot 5 aankopen; Hytale-plugins 0 aankopen. Het is een kleine winkel met weinig kopers.
- Meting: BuiltByBit blokkeert curl (Cloudflare 403), aantallen daar ONBEKEND. SpigotMC premium via de Spiget-API (https://api.spiget.org): de best verkochte betaalde plugins zijn PetBlocks (131.605 downloads, uit 2015), BlockBall (2015), mcMMO, Citizens, LiteBans (2015). De markt is dus oud en vast verdeeld.
- Wet 1: NEE. Minecraft-plugins bestaan al 13 jaar; PixelEast is nieuw maar heeft geen kopersstroom. Hytale (early access jan 2026) is 10 maanden oud, geen weken.
- Wet 2: NEE. De echte basistools (rechten, economie, essentials, anti-cheat) bestaan al jaren, vaak gratis (LuckPerms, EssentialsX). GOK: er ontbreekt geen brede basistool meer.
- Wet 3: JA. Kassa en betaalcultuur bestaan (BuiltByBit, PixelEast, Spigot premium).
- Wet 4: JA. Mojang maakt geen serverplugins.
- Vraag 5: DEELS. BuiltByBit en Spigot voeren kopers aan; PixelEast en voxel.shop nauwelijks (1 tot 5 verkopen per uitgelicht product).
- Mogelijk product: geen. Een Minecraft-plugin is een verzadigde markt, niet vroeg.
- Cijfer: 3. Kassa ja, maar oud, vol en geen gat voor een basistool.

### 2. Meta Horizon Store: promotie- en prijstools
- Bestaat: DEELS. GEZIEN: blogpost "Build Faster, Earn More: New Tools for Pre-Launch, Pricing, and Distribution on Meta Quest", https://developers.meta.com/horizon/blog/build-faster-earn-more-new-tools-pre-launch-pricing-distribution-quest/ (omschrijving: langere pre-launch, bredere bèta-kanalen, flexibele prijscontrole, builds uploaden via het web). Datum ONBEKEND: de pagina laadt de tekst met JavaScript, curl krijgt alleen de titel. Of dit "najaar 2026" is kon ik niet bevestigen.
- Wat het echt is: extra knoppen voor bestaande Quest-ontwikkelaars (prijs, kortingen, pre-launch). Geen nieuwe winkel en geen nieuwe API.
- Wet 1: NEE. De Horizon Store bestaat sinds 2019; dit zijn verbeteringen.
- Wet 2: NEE. Het zijn tools van Meta zelf, geen gat voor een tool van ons.
- Wet 3: JA. Quest-winkel heeft een kassa.
- Wet 4: NEE. Meta doet het hier juist zelf.
- Vraag 5: JA voor de winkel, maar niet relevant.
- Extra: VR-app bouwen vraagt een Quest-bril om te testen; staat niet bij Dortus.
- Mogelijk product: geen.
- Cijfer: 2. Platform doet het zelf.

### 3. Blender 5.3: Gaussian Splats en wat er nog ontbreekt
- Bestaat: JA. GEZIEN: Blender 5.3 uitgebracht 10 nov 2026, https://developer.blender.org/docs/release_notes/5.3/ . Rendering-pagina https://developer.blender.org/docs/release_notes/5.3/rendering/ : import van PLY en SPZ (ook glTF en USD), opslag als point cloud, Geometry Nodes, renderen in Workbench, EEVEE en Cycles. Letterlijk: "There is currently no export support", "Apply Transform ... does not work correctly", "Performance is not ideal".
- Wat het echt is: Blender kan splats nu openen en renderen, maar niet bewerken (bijsnijden, losse vlekjes opruimen) en niet opslaan als splat.
- Wat er al is: op extensions.blender.org alleen "Splats" (Dev.Patel, 3.953 downloads, maakt trainingsbeelden, geen bewerking) en "Point Cloud I/O" (gewone puntenwolken). Geen enkele gratis extensie voor bijsnijden, opruimen of exporteren van splats. GEZIEN via zoeken op extensions.blender.org. Op Superhive staan al betaalde: Splat Studio ($12,99, bijsnijden, opruimen, relight, export .ply), Splat Stage ($39, bèta, alleen 5.3), Splatlight, en KIRI 3DGS Render (gratis, oudere aanpak). Superhive is dus al een week bezet.
- Ander nieuws in 5.3 zonder extensie: asset-bibliotheken kunnen nu als extensie (https://developer.blender.org/docs/release_notes/5.3/assets/). De categorie Asset Libraries op extensions.blender.org heeft maar 8 bibliotheken (Poly Haven Lite 3K, ambientCG Lite 2K downloads). Alleen CC0, dus gratis; betaalde bibliotheken kunnen alleen via een eigen repo met toegangscode. Verder: projectsysteem, Loop Tools nu ingebouwd (die extensie is dood), compositor-effectenstapel.
- Wet 1: JA. 7 dagen oud. Let op: de keuringsrij op extensions.blender.org staat op 2.450 (alle statussen), sommige wachten een maand. GOK: 3 tot 14 dagen tot live.
- Wet 2: DEELS. Iedereen die een splat in Blender opent heeft bijsnijden, opruimen en export nodig. Maar splats gebruikt maar een deel van de Blender-gebruikers. Groeiend, geen nis meer, ook geen "iedereen".
- Wet 3: JA. Gratis basis op Blender Extensions, Pro op Superhive (Dortus heeft daar al Click Joints Pro). Werkt al zo bij ons.
- Wet 4: DEELS. Export staat letterlijk als "nog niet" in de notes. GOK: export komt in 5.4 (rond maart 2027, Blender brengt elke ±4 maanden uit) of later; bijsnijden en opruimen waarschijnlijk niet zo snel.
- Vraag 5: JA. Blender Extensions is ingebouwd in Blender; Click Joints kreeg ±205 downloads vanzelf.
- Mogelijk product: "Splat Tools" gratis op extensions.blender.org: kader bijsnijden, vlekjes en zwevers opruimen, Apply Transform dat wel klopt, export naar PLY en SPZ. Pro op Superhive met relight en presets. Wie betaalt: 3D-scanners, archviz, VFX-makers die splats in een scène zetten. De gratis versie moet de eerste en beste op extensions.blender.org zijn; op Superhive zijn we niet de eerste.
- Cijfer: 7. Zelfde recept als Click Joints, plek op de gratis winkel nog leeg, maar splats is smaller dan een echte basistaak en Blender kan export binnen enkele maanden zelf doen.

### 4. Home Assistant 2026.11: winkel ingebouwd?
- Bestaat: JA. GEZIEN: "2026.11: A lot in store!", 4 nov 2026, https://www.home-assistant.io/blog/2026/11/04/release-202611/ . HACS is nu ingebouwd als "Marketplace" onder Instellingen, op elke installatie, zonder GitHub-account. Toont downloads, sterren, vereiste versie.
- Kassa: NEE. Letterlijk: "Everything in the Marketplace is free, and that will not change."
- Wat het echt is: de bekende HACS-catalogus (integraties, kaarten, thema's) zit nu standaard in Home Assistant. De catalogus komt nog steeds uit de bestaande HACS-lijst op GitHub; wie er niet in staat, kan alleen via "Add from link".
- Wet 1: JA. 13 dagen oud, en miljoenen installaties zien de winkel nu voor het eerst. Erin komen loopt via de HACS-standaardlijst (GOK: keuring kan weken duren).
- Wet 2: ONBEKEND per product; HACS heeft al duizenden projecten, de basis (Mushroom-kaarten, kaarten, thema's) is al bezet.
- Wet 3: NEE. Gratis en dat blijft zo. Harde nee.
- Wet 4: JA voor losse integraties.
- Vraag 5: JA. Ingebouwde etalage met zoeken en downloadaantallen.
- Mogelijk product: alleen als bereik-project zonder geld. Valt af op wet 3.
- Cijfer: 4. Groot bereik, maar de winkel verbiedt geld vragen.

### 5. Adobe Firefly Graph en Splice Create
- Firefly Graph bestaat: JA, maar datum anders dan de tip. GEZIEN: persbericht Adobe MAX, 10 nov 2026 (niet 17 nov), https://news.adobe.com/news/downloads/pdfs/2026/11/firefly-release-max-2026.pdf : "Firefly Graph (beta): ... custom, repeatable workflows". Geen woord over delen, verkopen of een winkel voor workflows.
- Splice Create bestaat: JA, datum anders. GEZIEN: https://splice.com/blog/introducing-splice-create/ , 5 nov 2026 (niet 9 nov). Een eigen DAW, bèta, alleen Mac ("Windows and web coming soon"), gratis met Create Pro voor $9,99 per maand. Werkt met bestaande VST-plugins, geen pluginwinkel.
- Wat het echt is: twee nieuwe makerstools van grote bedrijven, zonder kassa of winkel voor derden.
- Wet 1: JA (nieuw). Wet 2: NEE. Wet 3: NEE, geen kassa voor makers. Wet 4: NEE, Adobe en Splice doen het zelf. Vraag 5: NEE.
- Extra: Splice Create is alleen Mac; Dortus heeft geen Mac.
- Mogelijk product: geen.
- Cijfer: 1. Geen winkel, geen kassa.

### 6. Retrovibe by GOG en Steam-wijzigingen (kort, voor een klein Steam-spel met pagina in jan of feb 2027)
- Retrovibe by GOG: JA. GEZIEN: https://www.gamingonlinux.com/2026/10/gog-and-retrovibe-team-up-for-indie-game-publishing/ , 29 okt 2026. Een uitgever (geld, QA, marketing) voor indiespellen, op PC-winkels en consoles. Voor Dortus: alleen zinvol als we een spel willen pitchen; een uitgever kiest zelf en wil een sterk spel. Geen winkel, geen tool-kans.
- Steam keuring: JA. GEZIEN: https://www.invenglobal.com/articles/28152/valve-says-steam-pre-release-reviews-now-take-up-to-12-business-days , 4 nov 2026 (Steamworks-aankondiging 3 nov). Buildkeuring duurt nu tot 12 werkdagen (doel 3 tot 5). Nieuwe checklist: het spel minstens 5 minuten via de Steam "Play"-knop gespeeld hebben voor inzenden. Officiële doc zegt nog: pagina 7 werkdagen van tevoren inzenden (https://partner.steamgames.com/doc/store/review_process).
- Discounts & Events: JA. GEZIEN: https://gamedeveloper.com/pc/steam-s-discounts-and-events-tab-will-soon-be-fully-algorithm-driven , 29 sep 2026. Vanaf begin 2027 geen handmatige kalender meer (Daily/Weekend/Midweek Deals gepauzeerd), maar persoonlijke aanbevelingen; Valve zag 10x meer spellen per dag in dat vak.
- Achievement Sets: JA. GEZIEN: https://gaminghq.eu/2026/11/14/steam-achievement-sets-tracking-overhaul/ , breed uitgerold 11 nov 2026 (bèta sinds 15 okt). Makers kunnen prestaties in sets verdelen (hoofdspel, DLC).
- Wat betekent het voor ons: (1) reken 3 weken voor pagina plus build in plaats van 1 week; zend de pagina vroeg in januari in. (2) Speel de build 5 minuten via Steam voor inzenden, anders afgekeurd. (3) Kortingen worden door het algoritme verdeeld: een klein spel met weinig wenslijsten wordt niet meer handmatig uitgelicht, maar kan door personalisatie juist vaker opduiken; wenslijsten en klikratio worden nog belangrijker. (4) Achievement Sets: meteen gebruiken, kost niets, helpt bij prestatiejagers.
- Cijfer: n.v.t. (geen productkans, alleen planning).

## Top 2
1. Blender 5.3 Splat Tools (cijfer 7): gratis basis op extensions.blender.org (bijsnijden, opruimen, export PLY/SPZ, correcte Apply Transform), Pro op Superhive. Zelfde recept als Click Joints, de plek op de gratis winkel is nog leeg, Blender zegt zelf dat export ontbreekt. Risico's: splats zijn smaller dan een echte basistaak, Superhive heeft al 3 betaalde concurrenten, Blender 5.4 (GOK maart 2027) kan export toevoegen, en de keuringsrij kan langer dan 7 dagen duren. Snel zijn is alles.
2. Home Assistant Marketplace (cijfer 4): alleen als bereik zonder geld; de winkel is ingebouwd en nieuw, maar "alles gratis, dat blijft zo" is een harde nee op wet 3.

Strikt genomen haalt alleen Splat Tools een 7, en dan net. De rest is dood of alleen planning (Steam).
