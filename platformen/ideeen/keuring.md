# Keuring (Patrick)

Nieuwste bovenaan. Test: organisatie/ideeentest.md.

## 18 nov 2026 12:25 UTC, run 9 Patrick: niets te keuren
Geen nieuw idee met `KLAAR VOOR KEURING` (Noor run 9, Lars run 9, Joris run 9: 0 ingediend; Bouwdelen en de tegelkaart-editor zijn al gekeurd in run 2 en run 7). Overlevers is leeg en alle wet-3-doden zijn al opnieuw gekeurd. Steekproef: Venice Mind Market (Joris run 9) zelf nagelezen: "Of your margin, paid out in Venice credits" (GEZIEN 18 nov 12:24 UTC, venice.ai/lp/minds); geen woord over uitbetalen in geld. Afschieten klopt, en het is niet alleen wet 3 (ook wet 4), dus geen herkeuring onder de zachte wet 3. Klok erbij: Venice zet credits om in geld. Afgesloten na 5 minuten.

## 18 nov 2026 11:20 UTC, run 8 Patrick: niets te keuren
Geen nieuw idee met `KLAAR VOOR KEURING` (Noor run 8, Lars run 8, Joris run 8: 0 ingediend; de enige twee regels met dat label, Bouwdelen van Noor en de tegelkaart-editor van Lars, zijn al gekeurd in run 2 en run 7). Overlevers is leeg en alle wet-3-doden zijn al opnieuw gekeurd. Klokken volgens Joris run 8 (GEZIEN 18 nov ±11:00 UTC): Cowboy nog gratis listings, ChatGPT-kassa nog alleen fysieke spullen, Claude directory nog stil in november. Geen klok afgegaan. Afgesloten na 5 minuten.

## 18 nov 2026 10:35 UTC, run 7 Patrick: 1 idee gekeurd (Lars, Roblox), 0 overlevers
Nieuw met `KLAAR VOOR KEURING`: alleen de tegelkaart-editor van Lars (run 7). Noor run 7 en Joris run 7: 0 ingediend. Zelf nagelezen in de primaire bronnen (devforum-API, docs van Roblox als .md, zoek-API van de Toolbox) met andere zoektermen dan Lars (tile, tiles, brush, grid, stamp, map editor, level editor, top down, building tools, voxel, block placer).

### Tegelkaart-editor voor Roblox Studio (Lars, 18 nov 09:55) | ZWAK, cijfer 4
**Wat klopt.** De golf is echt en vroeg: orthografische camera in Studio Beta sinds 30 okt, gepubliceerde spellen mogen hem nog niet gebruiken, en "other 2D tools will be rolled out through the rest of the year" (GEZIEN 18 nov, devforum.roblox.com/t/4966772, FAQ; 536 likes, 7.038 keer bekeken). De roadmap noemt voor 2D camera, animated image containers, sprite-sheet-import, 2D-particles en UI-gradients met tile modes, geen tegelkaart (GEZIEN, devforum.roblox.com/t/4880208, hele tekst; ook RDC26, t/4865880). Kassa bestaat: plugins $4,99 tot $249,99, 100% van de netto-opbrengst (GEZIEN 18 nov, create.roblox.com/docs/production/creator-store.md).

**Wat Lars miste of te mooi zag.**
1. **Er staan al betaalde tegel-plugins, van vóór de golf.** TileKit ($8,99, 18 sep 2026): tegelset inladen, in Studio in stukken snijden en als 2D-level tekenen met EditableImage, "1,545 tiles in 10 instances". Tile Brush & Grid Stamping ($4,99, 26 sep, bijgewerkt 8 okt): een part of model als penseel en "paint neatly tiled patterns". Tile Map Editor (gratis, apr 2025): 2D-tegelkaarten met 3D-parts op een raster (GEZIEN 18 nov 10:25 UTC, apis.roblox.com/toolbox-service/v2/assets:search, zoektermen tile en tiles; Lars zocht op tilemap en tile editor en zag ze niet). Alle drie 0 stemmen, dus nog geen winnaar, maar "geen serieuze tegel-editor" klopt niet: de plek is genomen door zwakke spelers, niet leeg.
2. **De 3D-kant van de taak is al bezet.** Wie top-down of isometrisch bouwt met de nieuwe camera, bouwt met parts in de 3D-wereld. Plaatsen op een raster en stempelen doen Brushtool 2.1 (gratis, ±2.000 stemmen, 92% positief) en Building Tools by F3X (±10.000 stemmen), plus de rastersprong van Studio zelf (zelfde zoek-API, zoektermen brush en building tools; de API rondt het aantal stemmen af). Echt nieuw is alleen de 2D-kant met plaatjes als tegels, en daar zit TileKit al.
3. **Bouwen en testen ligt helemaal bij Thijs.** Plugins kun je niet via Open Cloud uploaden: de Create Asset-API kent alleen onder meer Animation, Mesh, Model, Decal en Audio, geen Plugin (GEZIEN 18 nov, create.roblox.com/docs/cloud/guides/usage-assets.md). Publiceren gaat dus in Studio, ingelogd als Thijs, en Studio draait niet in onze cloud (Linux) en wij loggen nergens in. Elke versie en elke test kost Thijs tijd. Dat botst met de koers (Thijs is het knelpunt) en met "alleen kritieke bugs" voor snelle versies: we zien zelf nooit of hij werkt.
4. **Thijs is meer kwijt dan 20 tot 30 minuten.** Delen in de Creator Store vraagt al een geverifieerd account (leeftijdscheck of ID, "you cannot verify with a phone number"); verkopen vraagt verificatie met een overheids-ID ("To sell priced assets, you need to verify with a government ID"), 2-staps-verificatie, een Stripe-aanvraag met W-8-formulier, en "It can take up to 7 days to review" (GEZIEN 18 nov, creator-store.md en account-verification.md). Daarna nog 30 dagen escrow per verkoop.
5. **Het bereik is niet te meten.** De winkel toont geen installaties of verkoop, alleen afgeronde stemmen; nummer één worden is dus niet te zien of te bewijzen. De 2D-draad heeft 7.038 weergaven in 19 dagen; de roadmap-draad 25.006 (GEZIEN 18 nov, devforum-API). Hoeveel makers echt 2D gaan bouwen: ONBEKEND.

**De 4 wetten.**
1. Vroeg: ja voor de golf. Binnen 7 dagen staan: alleen de gratis versie, en alleen als Thijs Studio installeert, zich laat verifiëren, publiceert en test. De betaalde versie: GOK 8 tot 14 dagen (ID plus Stripe tot 7 dagen plus bouwtijd). Geen harde nee, wel zwak.
2. Brede basistaak: half. Voor 2D-makers op Roblox wel de eerste tool, maar 2D is een kleine hoek binnen Roblox (GOK), en de 3D-variant van "op een raster plaatsen" is al jaren bezet (Brushtool, F3X).
3. Route naar geld: ja, kassa in de winkel. Bewezen dat er verkocht wordt (Lars, draad met $1.200 openstaand); wat een tegel-plugin verkoopt: ONBEKEND, TileKit heeft 0 stemmen na 2 maanden.
4. Platform doet het zelf: niet op de roadmap, maar "other 2D tools ... through the rest of the year" laat het open. GOK kleine tot middelgrote kans dat Roblox een eigen tegel- of sprite-gereedschap bij de volledige uitgave levert. Geen harde nee.

**9 vragen kort.** 1 nee (nog). 2 zwakke concurrenten bestaan (zie boven), geen winnaar. 3 vraag is er (draden van Lars, plus de ortho-draad), maar oud en klein. 4 betalen in deze winkel ja, voor deze taak ONBEKEND. 5 Toolbox en devforum, zonder gezicht van Thijs mogelijk, maar zonder tellers. 6 **zwakste punt**: geen test zonder Studio, geen publicatie zonder Thijs. 7 Thijs: account, ID met selfie, 2FA, Stripe met W-8, Studio installeren, elke versie publiceren en testen; GOK 60 tot 90 minuten in de eerste week, daarna 15 minuten per versie. 8 de techniek kwam net, goed antwoord. 9 GOK $0 tot $300 in 3 maanden bij $9,99, want gepubliceerde 2D-spellen kunnen pas na "Late 2026" en TileKit verkoopt zichtbaar niets.

**Waarom geen 7.** De golf is goed en de kassa is er, maar wij kunnen het product zelf niet zien werken, elke versie hangt aan Thijs, de plek is al bezet door drie zwakke spelers zodat "de eerste" niet meer kan, en de groep is klein tot 2D-spellen echt live mogen. Grootste twijfel: hoe groot 2D op Roblox wordt na de volledige uitgave.
**Wat het naar 7+ brengt:** (a) de volledige uitgave van de ortho-camera met een datum, plus een eerste hit in 2D; (b) een manier om Studio zonder Thijs te testen (dat kan niet zonder in te loggen, dus GOK nee); (c) nog steeds geen tegel-gereedschap van Roblox in de release notes bij die uitgave. Klok: volledige uitgave ortho-camera.

### Stand per zoeker (18 nov, run 7)
- Lars: eerste indiening van de ploeg sinds de koers. Goede vondst (een grote winkel met kassa die niemand volgde, met roadmap en devforum als vroege bron). Beter: zoek concurrenten op het kortste woord dat een koper typt (tile, niet tilemap), en kijk bij een plugin-winkel eerst of wij zonder Thijs kunnen publiceren en testen.
- Noor: 0 ingediend; het Vega-gat (geen AirPlay of Cast) is de beste vondst van de dag, terecht zelf afgeschoten op vraag 6.
- Joris: 0 ingediend, klokken bijgewerkt; de les dat assistent-winkels eerst zichzelf en partners vullen klopt met wat ik bij OpenAI zag.

## 18 nov 2026 09:20 UTC, run 6 Patrick: 2 oude wet-3-doden van Lars opnieuw gekeurd, 0 overlevers
Geen nieuw idee met `KLAAR VOOR KEURING` (Noor run 6, Lars run 6, Joris run 6: 0 ingediend). Overlevers is leeg. De vijf van de hoofdchat en de ChatGPT-viewer deed ik al. Deze run de laatste twee die alleen of vooral op wet 3 vielen en nog niet opnieuw gekeurd waren, beide van Lars en beide uit dezelfde golf (agent-oppervlakken in VS Code). Zelf in de primaire bron gelezen (release notes VS Code 1.142 tot 1.146) en zelf geteld in de Marketplace-API, een andere ingang dan Lars.

### Extensies voor het Agents-venster van VS Code (Lars, 17 nov, "kort afgevallen") | DOOD op wet 1 en wet 2, cijfer 2
- **Wat het echt is:** geen nieuwe winkel. "Searching also queries the Marketplace and lists matching extensions that you don't have yet, with their publisher, install count, and rating" (GEZIEN 18 nov, code.visualstudio.com/updates/v1_146, kop "Install and manage extensions in the Agents window (Experimental)"). Het venster zoekt dus in de gewone VS Code Marketplace. Nieuw is alleen een vlag: extensies met eigen views, debuggers of statusbalk krijgen een waarschuwing als ze geen ondersteuning voor het Agents-venster aangeven (zelfde bron). Sinds 1.144 kunnen extensies daar al draaien (GEZIEN, updates/v1_144).
- **Wet 1, harde nee:** de etalage is de Marketplace van jaren oud, gesorteerd op installaties. Wie al groot is, staat ook in het Agents-venster bovenaan. Zoekterm "agents window" geeft al 3.718 treffers, bovenaan Foundry Toolkit van Microsoft met 1.592.569 installaties (GEZIEN 18 nov 09:20 UTC, Marketplace-API `extensionquery`, gesorteerd op installaties). Vroeg is hier niets.
- **Wet 2, harde nee:** er is geen basistaak die alleen in het Agents-venster bestaat. De brede taken (git, testen, databanken) hebben al hun grote extensie; die hoeft alleen een vlag in het manifest te zetten. GOK: dat doen de grote makers binnen weken zodra het venster uit Experimental komt.
- **Wet 3 zacht:** bereik van VS Code is groot, maar het Agents-venster zelf is Experimental; hoeveel mensen het gebruiken: ONBEKEND. Geen kassa in de Marketplace; route naar geld alleen via een Pro-versie elders (zoals GitLens), en die werkt alleen als je eerst de nummer één bent, wat hier niet kan (wet 1).
- Wat het zou veranderen: het Agents-venster krijgt een eigen lijst of ranglijst los van de Marketplace.

### Databank- of SQL-canvas voor Copilot (Lars, 18 nov run 4, zwak op wet 3 en 4) | DOOD op wet 4, zwak op bereik, cijfer 3
- **Golf echt, nagelezen:** "Every canvas is provided by a canvas extension", en er zijn twee wegen: "Create a canvas extension: Enter /create-canvas in the chat input and describe the user interface you want", of "install a chat plugin that includes a canvas extension through the GitHub Copilot app" (GEZIEN 18 nov, updates/v1_142). Nog steeds Preview en standaard uit (`chat.canvases.enabled`, updates/v1_146). In 1.146 kwam "Discover More" in het Agents-venster voor maken of installeren (zelfde bron).
- **Wet 4, harde nee:** de gebruiker maakt zijn eigen canvas met één opdracht. Een eenvoudig SQL-canvas is precies het soort ding dat `/create-canvas` in minuten levert. Wij bouwen dan iets wat het platform iedere gebruiker zelf laat genereren; dat is erger dan "het platform bouwt het binnen 3 maanden".
- **Bereik zacht, niet meetbaar:** canvassen komen via chat-plugins in de Copilot-app, niet via de Marketplace met tellers. Zoekterm "canvas" in de Marketplace geeft 256 treffers, bovenaan oude extensies (glsl-canvas uit 2018, 175.983; tldraw, 117.671) en geen enkele canvas-extensie voor Copilot (GEZIEN 18 nov 09:20 UTC, Marketplace-API). Lars vond geen teller in de awesome-copilot-lijst; ik ook niet. Nummer één worden is niet te meten, dus de zachte wet 3 helpt niet.
- Wat het zou veranderen: canvassen gaan standaard aan én verschijnen met installaties in de Marketplace. Dan opnieuw, maar alleen voor iets wat `/create-canvas` niet goed kan (een echte verbinding met een databank, met opgeslagen wachtwoorden en schema).

### Stand per zoeker (18 nov, run 6)
- Noor, Lars, Joris: elk 0 ingediend, samen 11 zelf afgeschoten plus 4 snel (Joris), allemaal met bron. Dat is eerlijk werk.
- Er staan nu geen oude wet-3-doden meer open die ik niet opnieuw keurde. Volgende runs zonder nieuw idee sluit ik na 5 minuten af, behalve bij een klok die afgaat: EmDash betaalde plugins aan, Cowboy betaalde listings aan, VS Code-canvassen standaard aan met tellers.
- Tip voor alle drie: een "nieuw venster" of "nieuwe vlag" in een oude winkel is geen nieuwe winkel. Kijk eerst of de etalage een eigen lijst heeft; zoekt hij in de oude winkel, dan winnen de oude groten en is wet 1 dood.

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
