# Keuring (Patrick)

Nieuwste bovenaan. Test: organisatie/ideeentest.md.

## 18 nov 2026 08:35 UTC, run 5 Patrick: 1 wet-3-dode opnieuw gekeurd, 0 overlevers
Geen nieuw idee met `KLAAR VOOR KEURING` (Noor run 5, Lars run 5, Joris run 5: 0 ingediend). Overlevers is leeg. De vijf wet-3-doden van de hoofdchat deed ik in run 4. Deze run de laatste die alleen op wet 3 sneuvelde en nog niet opnieuw gekeurd was: de bestandsviewer in ChatGPT (Joris, run 2). Zelf in de primaire bron gelezen, niet via de nieuwssites die Joris gebruikte.

### Bestandsviewer als ChatGPT Plugin Extension (Joris, 17 nov) | DOOD op wet 4 en vraag 1, zwak op wet 3 en 1, cijfer 2
- **Wat klopt:** plugins kunnen sinds DevDay "file viewers and editors" in ChatGPT zetten: "Open supported files in your own interface, with reading, live updates, and saving changes handled together" (GEZIEN 18 nov, developers.openai.com/plugins/build/extensions.md).
- **Wet 4 en vraag 1, harde nee: OpenAI bouwt de viewers zelf.** In de paginadata van chatgpt.com/plugins staan eigen plugins van OpenAI met het label `openai-curated`: `documents-router`, `pdf-router`, `presentations-router`, `spreadsheets-router`, `visualize`, `slide-viewer`, `structure-viewer`, `sequence-viewer` (GEZIEN 18 nov 08:30 UTC, chatgpt.com/plugins, ruwe HTML). De brede bestandssoorten (documenten, pdf, dia's, spreadsheets) zijn dus van OpenAI zelf, en zelfs nis-viewers voor biologie maken ze zelf. Het voorbeeld van OpenAI zelf (Bits & Bolts) is een CAD-onderdelenbibliotheek (zelfde pagina extensions.md). Wat overblijft (3D-print, CAD) is een nis (wet 2), en ook daar zit OpenAI al met een voorbeeld.
- **Wet 3 zacht, geen geloofwaardige route:** "Selling digital products or services, including subscriptions, digital content, tokens, or credits, is not allowed, whether offered directly or indirectly (for example, through freemium upsells)." Wel toegestaan: "Users may sign in to an existing paid account", maar "Plugins must not display subscription plans, initiate new subscriptions, or promote upgrades" (GEZIEN 18 nov, developers.openai.com/plugins/plugin-guidelines.md, kop Commerce and monetization). De plugin mag dus geen klanten werven voor een betaalde versie. Geld kan alleen komen van een eigen dienst die mensen al elders betalen; die hebben wij niet. Kassa in de winkel: "current approval is limited to plugins for physical goods purchases" (GEZIEN 18 nov, plugins/build/monetization.md, ongewijzigd).
- **Bereik kleiner dan het lijkt:** "Plugin extensions on the web are coming soon to ChatGPT Free and Go users" (extensions.md). De 1,2 miljard per week van Joris (nieuwssite) geldt dus nog niet voor deze functie. Een teller van installaties zag ik niet in de paginadata van de directory (0 keer "installs"); nummer één worden is dan niet te meten.
- **Wet 1, Thijs:** publiceren vraagt "individual or business verification" van een OpenAI-organisatie plus domeinverificatie (GEZIEN 18 nov, plugins/deploy/submission.md). GOK: de individuele verificatie is een ID-controle; ONBEKEND hoe lang de keuring duurt.
- Bijvangst voor het andere ChatGPT-idee van Joris (gratis plugin met later Pro, run 4): klopt, dood. De enige toegestane route is inloggen op een bestaand betaald account, en reclame voor upgraden is verboden.
- **Wat het zou veranderen:** OpenAI zet digitale verkoop aan ("we are actively working to support a wider range of commerce use cases", monetization.md). Dan opnieuw, maar alleen voor een bestandssoort die niet op de lijst `openai-curated` staat.

### Stand per zoeker (18 nov, run 5)
- Noor, Lars, Joris: elk 0 ingediend, samen 12 zelf afgeschoten, allemaal met bron. Lars vond de beste les van de dag (Blender test grote functies maanden vooraf op het forum; makers zijn er op dag 1). Joris telde de Claude-directory opnieuw en kwam op dezelfde cijfers als ik.
- Voor alle drie: zoek in de paginadata van een winkel naar de eigen plugins van het platform (zoals `openai-curated` hier). Dat is de snelste toets op wet 4.

## 18 nov 2026 07:25 UTC, run 4 Patrick: de vijf wet-3-doden opnieuw gekeurd met de zachte wet 3, 0 overlevers
Geen nieuw idee met `KLAAR VOOR KEURING` (Noor run 4, Lars run 4, Joris run 4: 0 ingediend). Opdracht van de hoofdchat (18 nov ±07:45 NL) gevolgd: wat op 17 nov alleen op wet 3 sneuvelde opnieuw gekeurd, nu met de vraag of wij daar de nummer één in een basistaak kunnen worden en hoe groot het bereik echt is. Zelf opnieuw gezocht in de primaire bron, met andere ingangen dan de zoekers (GitHub-zoek-API, analytics van Home Assistant, de registerpagina zelf, de changelog van Cursor).

**Uitslag: niets haalt een 7. Zonder harde wet 3 sneuvelen ze nu op wet 1, 2 of 4.** Les voor iedereen: de zachte wet 3 vraagt een etalage die gebruik meet (installaties, downloads) én een basistaak die nog open is. Van de vijf meet alleen Home Assistant echt gebruik, en daar is niets meer vroeg.

| Winkel | Oud cijfer | Nieuw | Doodsoorzaak nu |
|---|---|---|---|
| Home Assistant Marketplace | 4 | 3 | Wet 1 en 2: het is de oude HACS-catalogus met een nieuw bord, en al overspoeld |
| EmDash-plugins | 6 (hooguit) | 4 | Wet 2 en vraag 5: basistaken al 2 tot 3 keer bezet, geen teller van gebruik, bereik ONBEKEND |
| Claude connectors directory | 5 | 3 | Wet 1 en 2: golf voorbij, merken bovenaan, wij hebben geen eigen dienst |
| Hermes Marketplace | geen | 3 | Wet 4 en vraag 5: basistaken ingebouwd, etalage telt GitHub-sterren |
| Cursor Origin | 2 | 2 | Wet 2 en bereik: alleen teams op een bètaforge, basistaken op dag 1 van grote partners |

### Home Assistant Marketplace | DOOD op wet 1 en wet 2, cijfer 3
- **Bereik is echt groot:** 734.694 actieve installaties die analytics delen (GEZIEN 18 nov, analytics.home-assistant.io/data.json, veld `active_installations`). Het echte aantal is hoger, want delen is vrijwillig. En de winkel staat nu in elke installatie onder Instellingen.
- **Maar niets is vroeg.** De maker zelf: "my goal was simple: if you use HACS today, it should feel like only the name changed", en "The Marketplace brings the existing HACS experience into Home Assistant" (GEZIEN 18 nov, home-assistant.io/blog/2026/11/04/release-202611/). De catalogus is de HACS-lijst van GitHub, die sinds 2019 groeit. De basistaken (kaarten, thema's) hebben al jaren hun winnaars (Mushroom, card-mod; uit `onderzoek-2026-11-17/C-spel-maker.md`, niet zelf geteld).
- **En het stroomt al over.** In de lijst `hacs/default` zijn 1.385 pull requests samengevoegd tussen 1 en 18 nov, 1.345 in oktober, en er staan er nog 949 open (GEZIEN 18 nov, GitHub-zoek-API `repo:hacs/default is:pr is:merged`). Bijna allemaal "Adds new integration" of "Adds new plugin" voor één merk, één land of één apparaat (bijvoorbeeld een Franse waterleverancier, een Vietnamese kalender). Wie er nu bij komt, staat tussen honderden per week.
- **Wet 3 zacht:** "Everything in the Marketplace is free, and that will not change" (zelfde blog). Route naar later geld zou alleen een eigen betaalde dienst achter een integratie zijn; die hebben wij niet. Zonder eigen dienst blijft het een Rollwright: bereik, geen geld.
- Wat het zou veranderen: een brede taak die de catalogus aantoonbaar niet heeft, met een vraag van honderden stemmen op community.home-assistant.io. Niet gevonden.

### EmDash-plugins (Cloudflare) | ZWAK, cijfer 4, blijft een klok
- **Nieuw feit:** het register telt nu **321 plugins** (GEZIEN 18 nov, plugins.emdashcms.com/search, "321 in the registry"). Noor telde op 17 nov 48; dat was de eerste pagina. Het groeit dus snel, en de basistaken zijn al bezet: SEO drie keer (SEO & Schema Markup, Rank EmDash, QuixSEO) plus een AI-zichtbaarheidscheck, plus Stripe-winkel, contactformulier, onderhoudspagina, Notion-import (zelfde pagina).
- **Vraag 5, etalage:** de lijst sorteert op "Updated"; nergens een aantal installaties. Nummer één worden is daar niet te meten of te winnen met kwaliteit.
- **Wet 3:** nog steeds "All registry plugins are free for now ... we plan to add paid plugins" (GEZIEN 18 nov, emdashcms.com/blog/emdash-plugin-registry). Dat is de geloofwaardigste route naar later geld van de vijf, en de reden dat dit een 4 is en geen 2.
- **Bereik:** hoeveel echte sites EmDash draaien: ONBEKEND. De npm-telling van Noor (±500.000 per maand) telt ook bouwservers mee.
- **Wet 1, Thijs:** publiceren vraagt een Atmosphere-account (Bluesky), dus een account van Thijs (GEZIEN door Noor 17 nov, niet opnieuw nagelezen).
- Wat het zou veranderen: betaalde plugins gaan aan. Dan meteen opnieuw, met de vraag welke basistaak nog geen betaalde winnaar heeft.

### Claude connectors directory | DOOD op wet 1 en wet 2 voor ons, cijfer 3
- Zelf nageteld in de paginadata van claude.com/connectors (GEZIEN 18 nov): toegevoegd per maand jun 135, jul 166, aug 192, sep 117, okt 89, nov 8. Komt overeen met de telling van Joris (run 4). De golf is voorbij.
- Een connector is de deur naar een eigen dienst; bovenaan staan merken die hun eigen dienst koppelen, en de taken zonder merk doet Anthropic zelf (Joris, run 4, met bron). Wij hebben geen dienst. De zachte wet 3 maakt de route "eigen abonnement achter OAuth" wel toegestaan, maar dan moeten we eerst een dienst hebben die iemand wil. Dat is een ander idee, niet deze winkel.

### Hermes Marketplace | DOOD op wet 4 en zwak op vraag 5, cijfer 3
- Zelf nagelezen in de paginadata (GEZIEN 18 nov, hermes-agent.nousresearch.com/marketplace): geen veld voor installaties, downloads of prijs; "Sort by" geeft sterren of datum. Eens met Joris: de etalage beloont wie al een bekende GitHub-repo heeft, niet wie de beste basistool maakt. De basistaken (Google Workspace, Notion, GitHub, pdf, mail) zijn eigen skills van Hermes (Joris run 4, met bron). De instroom zakte na de hackathon van 11 nov naar bijna nul per dag (zelfde bron).

### Cursor Origin App Marketplace | DOOD op wet 2 en bereik, cijfer 2
- Nu met primaire bron: de changelog van Cursor (13 okt 2026, "Origin App Marketplace"): ruim 20 apps van partners (Cloudflare, Netlify, Render, Vercel, Buildkite, CircleCI ...), "open to public submissions", Cursor keurt elke inzending (GEZIEN 18 nov, cursor.com/changelog). Origin zelf: "Early beta now available on all paid plans" (GEZIEN 18 nov, cursor.com/origin).
- Bereik: alleen teams die hun code op een bètaforge van Cursor zetten; aantal ONBEKEND en zeker klein naast GitHub. Basistaken (deploy, CI, review, beveiliging) op dag 1 door grote partners. Bouwen vraagt een betaald Cursor-plan, dus geld van Thijs. Geen route naar geld in de winkel.

### Stand per zoeker (18 nov)
- Alle drie 0 ingediend in run 4, en dat is eerlijk: Joris telde zelf de etalages na (goed werk, ik kwam op dezelfde cijfers), Lars las vooruit in alpha en Insiders zoals gevraagd.
- Tip voor de volgende runs: zoek een winkel die (1) jonger is dan een maand, (2) installaties of downloads toont, en (3) waar een zoekterm voor een brede taak nog 0 of 1 treffer geeft. Alle drie tegelijk, anders niet indienen. Het canvas-spoor van Lars (VS Code) faalt nu op punt 2; het EmDash-spoor op punt 2 en de kassa.

## 17 nov 2026 17:20 UTC, run 3 Patrick: niets te keuren
- Geen nieuw idee met `KLAAR VOOR KEURING`: Noor run 3 (7 zelf afgeschoten), Lars run 3 (6), Joris run 3 (4). Overlevers is leeg, dus niets om na te keuren.
- Steekproef op de zelf afgeschoten ideeën. **Blender-MCP ("Claudian voor Blender", Lars): DOOD op vraag 1, nu met eerste bron.** Lars las alleen een README van een derde die naar blender.org verwijst. De Blender Foundation heeft zelf de repo `lab/blender_mcp` op projects.blender.org (laatst bijgewerkt 29 sep 2026): een MCP-server plus Blender-add-on, "Read the documentation at blender.org/lab/mcp-server" (GEZIEN 17 nov, projects.blender.org/lab/blender_mcp, readme.md). Ruim tien mensen hebben er al een eigen kopie van (zoek-API projects.blender.org op "mcp", GEZIEN 17 nov). blender.org zelf geeft een Cloudflare-controle op curl, dus die pagina niet gelezen. Het platform doet het dus zelf; afschieten klopt.
- De andere redenen in run 3 (EmDash wet 3 met letterlijk citaat, Grafana wet 2 met API-telling, x402 wet 3 met weekcijfers) hebben elk een bron met datum. Geen reden om er een terug te halen.
- Om te volgen (geen idee, wel een klok): EmDash zodra betaalde plugins aangaan (Noor) en Microsoft Ignite vanaf vanavond (Joris). Komt daar iets uit, dan keur ik het de eerstvolgende run.

## 17 nov 2026 16:25 UTC, run 2 Patrick: 1 idee gekeurd, 0 overlevers

### Bouwdelen voor Blender als asset-bibliotheek (Noor, 15:45 UTC) | DOOD op vraag 2, zwak op wet 1 en 2
Noor zocht alleen in de nieuwe soort Asset Libraries (8 stuks) en vergeleek met Archimesh. Ik zocht in alle 1.609 extensies voor Blender 5.3 op door, window, stair, cabinet, wall, archi, build, interior (GEZIEN 17 nov, API `extensions.blender.org/api/v1/extensions/?blender_version=5.3.0`). De taak (deuren, ramen, trappen, kasten met schuifjes) wordt al goed en gratis gedaan, in Blender 5, en actief onderhouden:
1. **Bagapie** (gratis, GPL): 112.986 downloads, 31 reviews, "Compatibility Blender 5.0 and newer", update 6 sep 2026 voor Blender 5.2. Geometry Nodes-gereedschap met onder "Architecture": Wall, Window Modern, Window Classic, Door Simple, Door Double, Stair Linear, Stair Spiral, Handrail, Fence, Column, Beam, Floor, Siding. Werkt ook met "Scatter from Asset Browser" en "Snap Asset" (GEZIEN 17 nov, extensions.blender.org/add-ons/bagapie).
2. **Home Builder 5** (gratis, GPL): 46.002 downloads sinds 27 feb 2026, 28 reviews, Blender 5.1 en nieuwer, update 14 sep 2026. "Place Cabinets & Appliances ... adjust cabinet dimensions", "Place Doors and Windows that automatically cut wall openings". Review van 5 dagen oud: "better than all add-ons I've tried to date" (GEZIEN 17 nov, extensions.blender.org/add-ons/home-builder-5).
3. **HiFi Architecture Builder** (gratis, GPL): 32.477 downloads, 14 reviews gem. 5,0, update 12 nov 2026. Muren, trappen, hellingen, raamkozijnen, deurkozijnen, balkons met live voorbeeld (GEZIEN 17 nov, extensions.blender.org/add-ons/hifi-builder).
Verder Arch Generator (4.039, juni 2026) en Bonsai/BlenderBIM (171.593, echte bouwmodellen).

Waarom dood:
- **Vraag 2:** het gat "Archimesh hapert in Blender 5 en niemand vervangt het" bestaat niet. Drie gratis, bijgehouden vervangers met samen ±190.000 downloads. Wie in Blender 5 een deur met schuifjes wil, heeft Bagapie of Home Builder.
- **Het enige nieuwe is de vorm** (een bibliotheek in de Asset Browser in plaats van een add-on). Dat is een leveringsvorm, geen behoefte van de gebruiker. Een koper zoekt "door" of "window", niet "asset library".
- **Wet 2 (brede basistaak):** bouwdelen zijn voor archviz en levels, een deel van de Blender-gebruikers, niet iets wat iedereen nodig heeft. De echte basistaak in de nieuwe soort (materialen, HDRI's) is al bezet door Blender zelf, Poly Haven en ambientCG, zoals Noor zelf vond.
- **Wet 3:** gratis concurrenten die meer doen maken een betaalde versie van $19 tot $29 lastig; ons eigen Rollwright-verhaal zegt hetzelfde.
- **Wet 1:** de keuringsrij van extensions.blender.org telt nog steeds 2.449 inzendingen (GEZIEN 17 nov, extensions.blender.org/approval-queue). Binnen 7 dagen live is daar niet in onze hand.

Wat het zou veranderen: een soort bouwdeel die Bagapie, Home Builder en HiFi alle drie niet hebben, met bewijs van vraag (bijvoorbeeld een forumdraad met stemmen).

Les voor de zoekers: bij een nieuwe winkelsoort niet alleen binnen die soort zoeken. Zoek de taak in de hele winkel (alle soorten), want de koper kiest op taak, niet op soort.

### Stand per zoeker (17 nov)
- **Noor:** 1 idee ingediend, 0 overlevers. Goed: de Essentials-lijst van Blender zelf uitgelezen, bronnen met datum, eerlijke twijfels. Beter: concurrenten zoeken op de taak in alle soorten van de winkel, niet alleen in de nieuwe soort.
- **Lars:** 0 ingediend (12 zelf afgeschoten). Zelf afschieten is goed; nu ook eens iets indienen dat 3 zoektermen overleeft.
- **Joris:** 0 ingediend (15 zelf afgeschoten). Zelfde advies.

## 17 nov 2026 15:18 UTC, run 1 Patrick: niets te keuren
- Geen enkel idee met `KLAAR VOOR KEURING` in noor.md, lars.md of joris.md. Alle drie de zoekers schoten in hun eerste run zelf alles af (Noor 3, Lars 6, Joris 10). Overlevers is leeg, dus ook niets om na te keuren.
- Wel één GOK van Joris nagekeken. **Drag-n-Drop Import voor Blender: DOOD op vraag 1, nu bevestigd.** Blender 4.1 kreeg een File Handler API voor slepen en neerzetten, en zette dat meteen aan voor Alembic, Collada, Grease Pencil SVG, OBJ, OpenUSD, PLY en STL in de 3D Viewport en de Outliner (GEZIEN 17 nov, developer.blender.org/docs/release_notes/4.1/pipeline_assets_io). Andere add-ons kunnen het via dezelfde API zelf toevoegen. Geen gat meer.
- Steekproef op de zelf afgeschoten ideeën: de redenen bij Noor (GameSnacks, Figma 3D) en Lars (Clonephaze 3MF) hebben elk een bron met datum. Geen reden om er een terug te halen.
- Kanttekening: Noor en Lars zetten bij hun run "±16:30 UTC" en "±17:00 UTC", terwijl het bij deze run pas 15:18 UTC is. Waarschijnlijk Nederlandse tijd met het verkeerde label. Graag kloktijd uit `date -u` halen.

## Al dood vóór de start (17 nov)
- Spraakmemo Garmin (opnemen en terugluisteren): ingebouwd op fēnix 8, fēnix 9, Enduro 3. Wordt door Gijs nagekeken voor horloges zonder ingebouwde notitie.
- Chrome: Google Agenda in bulk: bestaat (Calendar Bulk, 28 gebruikers na 5 weken).
- Ademhalings-app Garmin: volle hoek (Ebb, 0 downloads na een week). Erger: Garmin heeft zelf een ingebouwde Breathwork-activiteit met Tranquility (precies 4-7-8, dus Ebb Calm), Coherence en Relax and Focus (box breathing). GEZIEN 17 nov, garmin.com blog en garmin.ae.
- Click Joints (Blender): concurrenten bestonden al bij de keuze (Cleave $23, Cut Flex $34,99, JointLab $65, FigureCut $10 "pins and sockets that fit", Pose-to-Print $18; `platformen/blender/kandidaten-2026-11-07.md` regel 202).
- Dice Roller-opvolger Obsidian (Rollwright): het origineel is gratis en werkt nog (288.884 downloads); 44 downloads, 0 verkopen. Les: beter dan gratis-en-goed-genoeg verkoopt niet.
