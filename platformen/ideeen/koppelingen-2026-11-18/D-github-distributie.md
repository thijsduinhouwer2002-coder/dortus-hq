# D. Wat makers op GitHub inzetten voor distributie (zoeker D, 18 nov 2026)

Werkwijze: blobless clones (`git clone --filter=blob:none --no-checkout --depth 1`) van 31 repo's (GEZIEN), daarna `git show` op elke workflow in `.github/workflows` en zoeken naar Discord, Bluesky, Mastodon, X, Reddit, butler, Steam, nieuwsbrief, changelog en winkel-uploads. READMEs van Marketplace-actions via raw.githubusercontent.com. MCP-servers getest met `npx` en `uvx` in deze sessie. Let op: de GitHub-API (stars tellen) is in onze sessie dicht voor repo's die niet gekoppeld zijn, dus ik noem geen stars.

Bekeken repo's: Blender (MolecularNodes, Ucupaint, mmd_tools, glTF-Blender-IO, dream-textures, BlenderKit, Sverchok, Blender-Launcher-V2), JetBrains (intellij-platform-plugin-template, IdeaVim, AceJump, Key Promoter X, StringManipulation, TranslationPlugin), Obsidian (obsidian-git, Dataview, Excalidraw, Tasks, Templater, Linter, Omnisearch, Kanban), spellen (Unciv, Pixelorama, Endless Sky, Mindustry, OpenTTD, Pixel Wheels, Bitburner, Shattered Pixel Dungeon, OpenRCT2, Material Maker, Cataclysm DDA, Wesnoth, Bevy).

## Wat de makers echt doen (kort)
- **Winkel bijwerken bij een release is normaal; aankondigen bijna nooit.** Van de 31 repo's post er maar één vanzelf een aankondiging bij een release (Unciv, naar Discord). Niemand post vanzelf naar Bluesky, Mastodon, X of Reddit, en niemand stuurt vanzelf een nieuwsbrief (GEZIEN in alle workflows). Andere Discord-stappen die ik vond zijn foutmeldingen van de bouw (Wesnoth) of Discord-koppeling in het spel zelf (OpenRCT2), geen aankondigingen.
- **Uploaden naar de winkel doen ze wel:** MolecularNodes naar extensions.blender.org met `curl` bij elke gepubliceerde release, de JetBrains-sjabloon en Key Promoter X en TranslationPlugin met `publishPlugin` plus changelog in de winkel, Pixelorama en Unciv naar itch met butler, OpenTTD en Bitburner naar Steam met steamcmd, Material Maker met `game-ci/steam-deploy` naar een prerelease-tak, Unciv ook naar Google Play, AUR en Homebrew, Blender-Launcher naar winget. **Dat hebben wij al** (Blender, JetBrains, Steam).
- **De nieuwe stap bij de groten is Claude in de uitgave:** IdeaVim (JetBrains zelf) laat `anthropics/claude-code-action@v1` elke dag de changelog bijwerken, per versie een "What's new"-pagina schrijven die in de IDE opent na een update, en die pagina's als site publiceren (GEZIEN: `updateChangelogClaude.yml`, `prepareWhatsNewClaude.yml`, `publishWhatsNewPages.yml`, `WhatsNewHelper.kt`).
- **Onze eigen stand:** het secret `DISCORD_WEBHOOK` staat er, maar geen enkele workflow gebruikt het (GEZIEN: `grep` in `.github/workflows`). `KIT_API_KEY` ook niet.

## Top 5

### 1. Uitgave vanzelf naar Discord, met de changelog die al gekeurd is
- **Wat:** als een uitgave-workflow klaar is (Click Joints, Bison & Flex, later Hats), plaatst een extra stap de sectie van die versie uit `CHANGELOG.md` in een Discord-kanaal, met een link naar de winkel. Unciv doet precies dit: rol-ping, versienaam, release-tekst, en bij een kleine patch géén bericht (`if: release_body != ''`).
- **Probleem dat het oplost:** de plan-regel "wat een versie oplevert is de post erbij en de bestaande gebruikers" (PLAN.md punt 4). Nu blijft elke versie stil. Voor Hats: elke speeltestbuild en later de demo meldt zich vanzelf in de Hats-Discord, zodat de verzamelplek leeft.
- **Hoe het koppelt:** GitHub Action. Ik raad een gewone `curl` naar de webhook aan (onze `click-joints-uitgave.yml` haalt de changelogsectie al op met `awk`, regel 74 tot 78), of `npx @humanwhocodes/crosspost --discord-webhook -f bericht.txt` (zie voorstel 2). Niet `SethCohen/github-releases-to-discord`: die draait op `node16` (GEZIEN in zijn `action.yml`), een runtime die GitHub uitfaseert.
- **Waar:** Actions (secret staat er). Discord is ook vanuit onze sessie bereikbaar (GEZIEN: `discord.com/api/v10/gateway` gaf 200), maar het secret alleen in Actions.
- **Kosten:** gratis.
- **Getest:** nee, niets gepost (mag niet). Wel gezien dat het secret er staat en dat geen workflow het gebruikt.
- **Moeite:** 1 tot 2 uur (GOK) voor de stap in drie workflows.
- **Harde regel 4 (bijgesteld 18 nov 23:17):** de Discord van Hats is een kanaal van Dortus, dus een post mag na een keuring door een ander, zonder ja van Thijs. Voorstel: de stap post alleen als er in `winkel/aankondiging-<versie>.md` een regel `Gekeurd: <naam keurder>, <datum>` staat (Daan of de automatische keurder). Zonder die regel slaat de stap over en meldt dat in de run. De hoofdchat zet de tag; agents plaatsen dus niet zelf.
- **Wat Thijs doet:** niets verplicht; als Click Joints en Bison & Flex niet in de Hats-server horen, een tweede webhook voor een kanaal `#dortus-updates` (±3 minuten, of de hoofdchat via Chrome).
- **Gezien in:** [yairm210/Unciv `buildAndDeploy.yml`](https://github.com/yairm210/Unciv/blob/master/.github/workflows/buildAndDeploy.yml) (stap "Post announcement on Discord", `Ilshidur/action-discord@0.3.2`).

### 2. crosspost: één stap voor Bluesky, Mastodon, Discord, Telegram en dev.to (ook als MCP)
- **Wat:** een open pakket van Nicholas Zakas (maker van ESLint) dat één tekst naar meerdere netwerken stuurt: Bluesky, Mastodon, X, LinkedIn, Discord (bot of webhook), Telegram, dev.to, Slack, Nostr. Werkt als bibliotheek, als CLI voor CI, en als MCP-server. Het repo zelf is actief (laatste commit 4 nov 2026, GEZIEN).
- **Probleem:** per versie één post op meerdere plekken zonder dat een agent elk netwerk apart moet leren. Past bij voorstel 1 (zelfde stap, meer kanalen) en bij het weekpakket: de goedgekeurde tekst gaat in één keer naar alle kanalen. Metricool Free blijft voor inplannen; dit is voor de uitgavepost.
- **Hoe:** CLI in een GitHub Action (`npx @humanwhocodes/crosspost -b -m --discord-webhook -f bericht.txt --image gif.png`), sleutels als env-variabelen (`BLUESKY_IDENTIFIER`, `BLUESKY_PASSWORD` met een app-wachtwoord, `MASTODON_ACCESS_TOKEN`, `DISCORD_WEBHOOK_URL`). De MCP-modus (`--mcp`) is iets voor de hoofdchat, niet voor agents.
- **Waar:** Actions. Bluesky en Mastodon zijn ook vanuit de sessie bereikbaar (GEZIEN: `bsky.social/xrpc/_health` en `mastodon.social/api/v1/instance` gaven 200).
- **Kosten:** gratis (open bron, Apache-2.0 volgens npm; netwerken zelf gratis, X-API niet: X laten we weg).
- **Getest:** ja. `npx -y @humanwhocodes/crosspost --version` gaf `1.0.4`; als MCP gestart met alleen Discord-webhook: antwoordt op `initialize` en `tools/list` geeft o.a. `crosspost`, `list-services`, `post-to-social-media`, `check-message-length` (GEZIEN). Niets gepost. Gebruik: 4.126 downloads in de laatste maand (GEZIEN via api.npmjs.org).
- **Moeite:** 1 uur bovenop voorstel 1 (GOK).
- **Harde regel 4:** zelfde poort als voorstel 1: alleen posten met een `Gekeurd`-regel in het aankondigingsbestand. Dat geldt alleen voor kanalen van Dortus; nooit een eigen account van Thijs erin zetten (dan is zijn ja op de tekst nodig).
- **Wat Thijs doet:** kiezen of Dortus op Bluesky en Mastodon komt (hoek A weegt de kanalen); zo ja: account aanmaken en een app-wachtwoord (Bluesky) en toegangstoken (Mastodon) als secret zetten, ±10 minuten.
- **Gezien in:** [humanwhocodes/crosspost](https://github.com/humanwhocodes/crosspost) (README, CLI en MCP); in de lijst [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) staan meer social-MCP's, maar die zijn betaald of vragen een dienst ertussen.

### 3. "Wat is nieuw" in het product zelf na een update (vraag daar om een review)
- **Wat:** na een update opent de plugin één keer een klein venster of tabblad "Wat is nieuw in 2026.1.2", met de wijzigingen, één link naar de uitleg (rekenmachine-tutorial bij Bison & Flex, video bij Click Joints) en een vraag om een beoordeling in de winkel. IdeaVim doet dit: `WhatsNewHelper.kt` opent `whatsnew-<versie>.html` uit de plugin in een HTML-tabblad, en een workflow zet dezelfde pagina's als site online.
- **Probleem:** bestaande gebruikers zijn onze beste bron (PLAN.md punt 4), maar zien nu niets van een versie. Bison & Flex heeft beoordelingen nodig voor de zoekbalk van JetBrains; Click Joints (234 downloads, GEZIEN op het bord) idem op extensions.blender.org. De link naar Pro en naar de uitleg zit dan precies bij wie het al gebruikt.
- **Hoe:** code in het product (JetBrains: `HTMLEditorProvider.openEditor` zoals IdeaVim; Blender: bij het laden de versie vergelijken met een opgeslagen voorkeur en één keer een popup tonen). De pagina komt uit de changelog; die maken we al.
- **Waar:** in het product; bouwen en testen in Actions zoals nu.
- **Kosten:** gratis.
- **Getest:** nee (bouwwerk). Wel de code van IdeaVim gelezen (GEZIEN).
- **Moeite:** 3 tot 4 uur per product (GOK), plus keuring door Daan.
- **Harde regel 4:** de tekst staat in ons eigen product, niet onder de naam van Thijs; hij gaat langs de skill `update-tekst` en Daan zoals elke winkeltekst. De reviewvraag houden we kort en eenmalig per versie (niet zeuren).
- **Wat Thijs doet:** niets.
- **Gezien in:** [JetBrains/ideavim `WhatsNewHelper.kt`](https://github.com/JetBrains/ideavim/blob/master/src/main/java/com/maddyhome/idea/vim/group/WhatsNewHelper.kt), [`publishWhatsNewPages.yml`](https://github.com/JetBrains/ideavim/blob/master/.github/workflows/publishWhatsNewPages.yml), bestanden `src/main/resources/whatsnew-2.40.0.html` tot `whatsnew-2.43.0.html`.

### 4. Uitgavepakket door Claude in Actions: bij elke tag de concepten per kanaal
- **Wat:** bij een uitgave-tag draait `anthropics/claude-code-action@v1` (dezelfde sleutel als onze keurder) met de skill `update-tekst`: uit de nieuwe changelogsectie maakt hij de Discord-tekst, de Bluesky/Mastodon-post, de BlenderArtists- of r/Jetbrains-post, de "Wat is nieuw"-pagina (voorstel 3) en een Kit-mail als concept, en zet ze in een PR of in `organisatie/goedkeuren.md`. IdeaVim doet dit voor changelog en What's New: Claude bewerkt de bestanden, de workflow maakt de PR, Claude mag zelf niet pushen (`persist-credentials: false`).
- **Probleem:** PLAN.md "Automatiseren" punt 1 (weekpakket) en 5 (uitgavepakket) vragen nu handwerk van een agent per versie. Hiermee ligt het pakket klaar op het moment dat de versie live gaat, en voorstel 1 en 2 hoeven alleen nog de goedgekeurde tekst te plaatsen.
- **Hoe:** GitHub Action (`claude-code-action`), secret `ANTHROPIC_API_KEY` staat er al.
- **Waar:** Actions.
- **Kosten:** API-tegoed van Thijs. Proefkeuring Hats kostte 39.368 tokens in en 11.054 uit (GEZIEN op het bord), dus per uitgave ±$0,30 (GOK), bij ±4 uitgaven per week ±$5 per maand (GOK). Valt binnen de $200 per maand (GEZIEN in toegang.md), maar het is geld: Thijs zegt ja.
- **Getest:** nee (vraagt een run in Actions). Workflows van IdeaVim gelezen (GEZIEN).
- **Moeite:** 2 tot 3 uur (GOK); de keurder-workflow is een goed sjabloon.
- **Harde regel 4:** maakt alleen concepten. Een ander keurt (Daan of de automatische keurder, niet dezelfde run die schreef); daarna mogen voorstel 1 en 2 posten op kanalen van Dortus. Alles onder de naam van Thijs (mail, Reddit) blijft wachten op zijn ja.
- **Wat Thijs doet:** ja op het verbruik (±$5 per maand, GOK).
- **Gezien in:** [JetBrains/ideavim `updateChangelogClaude.yml`](https://github.com/JetBrains/ideavim/blob/master/.github/workflows/updateChangelogClaude.yml) en [`prepareWhatsNewClaude.yml`](https://github.com/JetBrains/ideavim/blob/master/.github/workflows/prepareWhatsNewClaude.yml); tldraw heeft er een skill voor (`dotcom-release-marketing`, zie `afkijken-2026-11-18/K-ai-opzet-5-voorbeelden.md`).

### 5. Steam-MCP zonder sleutel: tags, reviews en patch-effect van vergelijkbare spellen
- **Wat:** een open MCP-server met 41 alleen-lezen tools voor Steam (GEZIEN in `tools/list`): community-tags, reviews en hun trend, spelers nu, vergelijken van 2 tot 5 spellen, en "hoe bewoog elke patch de reviews". De meeste tools zonder API-sleutel.
- **Probleem:** Hats moet in de zoekbalk en de "meer zoals dit"-rijen van Steam komen. Een agent kan nu zelf de tags en reviewklachten van de bureaublad- en idle-spellen naast ons leggen (voor de 20 tags op de pagina, de capsuletekst en de lijst van makers), en na de paginadag onze eigen reviews volgen. Ook bruikbaar voor het scorebord.
- **Hoe:** MCP (`uvx steam-mcp`), in `.mcp.json` naast Context7.
- **Waar:** agentsessie. Steam-winkel is vanuit de sessie bereikbaar (GEZIEN: echte antwoorden hieronder).
- **Kosten:** gratis; met de `STEAM_WEB_API_KEY` uit toegang.md komen er accounttools bij, die hebben we niet nodig.
- **Getest:** ja. `uvx steam-mcp` start, 41 tools; `steam_get_app_tags` met `{"params":{"appid":2666510}}` gaf voor Rusty's Retirement: "Idler, Farming Sim, Desktop Companion, Automation, Management, ..." (GEZIEN). Let op: de argumenten moeten in een `params`-object.
- **Moeite:** 15 minuten om toe te voegen, 1 uur voor een eerste vergelijking voor Hats (GOK).
- **Harde regel 4:** leest alleen, plaatst niets.
- **Wat Thijs doet:** niets. Overlapt met hoek B (Steam); Olaf of Sanne beslist of het in `.mcp.json` komt.
- **Gezien in:** [Sarg338/steam-mcp](https://github.com/Sarg338/steam-mcp), gevonden via [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) (sectie Gaming).

## Afgevallen
- **bluwy/release-for-reddit-action** (post bij elke release op Reddit): vraagt het Reddit-wachtwoord als secret en een eigen Reddit-app; automatisch posten op subreddits botst met hun regels en met PLAN.md (handmatige post per versie).
- **SethCohen/github-releases-to-discord**: mooi opgemaakt, maar draait op `node16`; een `curl` of crosspost doet hetzelfde.
- **Ilshidur/action-discord** (Unciv): werkt, maar is een Docker-action uit 2021 (versie 0.3.2); `curl` is eenvoudiger.
- **itch.io met butler** (Pixelorama zet zelfs een speelbare webversie per release op itch): Olaf raadt een demo buiten Steam af (`platformen/steam/plan-b-id-controle.md`), itch vraagt een account van Thijs en een AI-melding (keuze 1 in PLAN.md).
- **Steam-upload met TOTP** (OpenTTD: `CyberAndrii/steam-totp` met wachtwoord en Steam Guard-geheim): wij hebben al `game-ci/steam-deploy`; deze route vraagt het wachtwoord als secret. Alleen bekijken als ons config.vdf-bestand gaat verlopen (Olaf).
- **winget, Homebrew, AUR, Google Play** (Blender-Launcher, Unciv): niet onze platformen.
- **obsidianmd/obsidian-workflows** (officiële controle en release voor Obsidian-plugins, Linter en Tasks gebruiken hem): kwaliteit, geen distributie, en Rollwright is geparkeerd. Tip voor hoek E.
- **intellij-platform-plugin-template `patchChangelog`**: zet de changelog vanzelf in de winkel; Bison & Flex heeft al `change-notes` in `plugin.xml`.
- **coreyhaines31/marketingskills** (±40 marketing-skills voor Claude Code): gemaakt voor SaaS (prijspagina's, cold e-mail, advertenties); `launch` en `directory` lezen kan, maar het is gereedschap om gereedschap.
- **Social-MCP's uit awesome-mcp-servers** (postwire, postfast, postmcp, posthive, content-distribution-mcp): meestal een betaalde dienst ertussen of een account per dienst; hoek A weegt de kanalen.
- **Kit-mail bij een release**: geen voorbeeld in een open repo gevonden, en "mails als concept" staat al gepland in toegang.md; past wel als uitvoer van voorstel 4.
- **Docs-site per release** (MolecularNodes, Blender-Launcher, Bevy met GitHub Pages): goed voor uitleg, maar dortus.com hebben we al; geen nieuwe koppeling.

## Bronnen
- Unciv: https://github.com/yairm210/Unciv/blob/master/.github/workflows/buildAndDeploy.yml
- MolecularNodes (upload naar Blender extensions): https://github.com/BradyAJohnston/MolecularNodes/blob/main/.github/workflows/upload.yml
- IdeaVim: https://github.com/JetBrains/ideavim/tree/master/.github/workflows en https://github.com/JetBrains/ideavim/blob/master/src/main/java/com/maddyhome/idea/vim/group/WhatsNewHelper.kt
- JetBrains-sjabloon: https://github.com/JetBrains/intellij-platform-plugin-template/blob/main/.github/workflows/release.yml
- Pixelorama (butler): https://github.com/Orama-Interactive/Pixelorama/blob/master/.github/workflows/release.yml
- OpenTTD (Steam met TOTP): https://github.com/OpenTTD/OpenTTD/blob/master/.github/workflows/upload-steam.yml
- Material Maker (steam-deploy): https://github.com/RodZill4/material-maker/blob/master/.github/workflows/dev-desktop-builds.yml
- Wesnoth (Discord bij bouwfout): https://github.com/wesnoth/wesnoth/blob/master/.github/workflows/ci-main.yml
- crosspost: https://github.com/humanwhocodes/crosspost en https://www.npmjs.com/package/@humanwhocodes/crosspost
- github-releases-to-discord: https://github.com/SethCohen/github-releases-to-discord
- release-for-reddit-action: https://github.com/bluwy/release-for-reddit-action
- Steam-MCP: https://github.com/Sarg338/steam-mcp
- obsidian-workflows: https://github.com/obsidianmd/obsidian-workflows
- marketingskills: https://github.com/coreyhaines31/marketingskills
- awesome-mcp-servers: https://github.com/punkpeye/awesome-mcp-servers
- awesome-claude-code: https://github.com/hesreallyhim/awesome-claude-code
