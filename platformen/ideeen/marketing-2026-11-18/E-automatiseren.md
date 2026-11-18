# E: de machine. Distributie en marketing zo veel mogelijk vanzelf

Agent E, 18 nov 2026, opdracht hoofdchat (BRIEF.md in deze map). Alle webpagina's gelezen met curl op 18 nov. GEZIEN = zelf gelezen in de officiële documentatie of in onze repo. DERDEN = iemand anders zegt het, met link. GOK = niet nagekeken.

**Wat al bekend is (niet overgedaan):** skill `update-tekst` bestaat (commits naar changelog en drie lengtes, alles CONCEPT); `UITKOMST.md` van het afkijken zegt al "upload naar extensions.blender.org automatisch", "gratis versie ook als $0+ op Gumroad (maillijst)" en "Steam uploaden via een workflow"; `platformen/patrick/voorstellen/11-toegang.md` (10 nov) heeft de sleutellijst; filmpjes gaan al als release-URL naar Metricool (`commercie/filmpjes/planning.md`). Hieronder gaat het verder waar dat ophoudt: de hele keten aan elkaar, per stap wat echt kan.

**De grens blijft:** automatisch tot "klaar voor goedkeuring". Zelf plaatsen mag alleen op eigen winkelpagina, changelog en README (BRIEF.md). Alles onder de naam van Thijs gaat via één wachtrij: `organisatie/goedkeuren.md`, gebundeld om 12:00 en 20:00.

---

## 1. De keten in één schema

```
 ┌───────────────────────────────────────────────────────────────────────────────────────────┐
 │ STAP 0  Code klaar, keuring Daan "Akkoord: ja", tests groen                               │
 │         Tool: wat er nu is (e2e-workflows). Thijs: niets. Kosten: 0.                      │
 └───────────────────────────────┬───────────────────────────────────────────────────────────┘
                                 │ tag zetten, bv. click-joints-v0.1.2
                                 v
 ┌───────────────────────────────────────────────────────────────────────────────────────────┐
 │ STAP 1  Uitgavepakket (GitHub Actions, NIEUW: uitgave-pakket.yml, start op elke tag)      │
 │         git log vorige-tag..tag -- producten/<naam>/  +  keuringen  ->  bron.md            │
 │         + beeldpakket (stap 4) als release-assets op <tag>-beelden                        │
 │         Thijs: niets. Kosten: 0 (openbare repo, Actions gratis).                          │
 │         Bestaat al: losse workflows per product, skill update-tekst, git-tags.            │
 └───────────────────────────────┬───────────────────────────────────────────────────────────┘
                                 v
 ┌───────────────────────────────────────────────────────────────────────────────────────────┐
 │ STAP 2  Tekst (Claude-run van de eigenaar of een geplande taak, skill update-tekst)        │
 │         CHANGELOG.md -> winkel "wat is nieuw" + korte post + Steam-aankondiging           │
 │         Keuring (skill keuren). Concept in commercie/concepten/<tag>.md                   │
 │         Thijs: niets. Kosten: 0 extra (loopt in de Claude-runs die er al zijn).            │
 └───────────────┬───────────────────────────────────────────────┬───────────────────────────┘
                 │ EIGEN KANALEN: mag zonder Thijs                │ ONDER NAAM VAN THIJS
                 v                                                v
 ┌───────────────────────────────────────────┐   ┌───────────────────────────────────────────┐
 │ STAP 3  Winkels uploaden (workflows)       │   │ STAP 5  Wachtrij goedkeuren.md             │
 │  Blender: API versions/upload + notes      │   │  hoofdchat bundelt 12:00 en 20:00:         │
 │  JetBrains: API updates/upload (staat er)  │   │  tekst + beeld-URL + tijdstip per post     │
 │  Steam: steamcmd naar beta-tak (staat er)  │   │  Thijs: één "ja" per bundel                │
 │  GitHub release + README-GIF               │   └──────────────────┬────────────────────────┘
 │  Gumroad/Superhive Pro: hoofdchat met hand │                      v
 └───────────────────────────────────────────┘   ┌───────────────────────────────────────────┐
                                                  │ STAP 6  Inplannen (hoofdchat)              │
                                                  │  Metricool MCP createScheduledPost:        │
                                                  │  media = release-URL, tijd uit             │
                                                  │  getBestTimeToPostByNetwork                │
                                                  │  Steam-aankondiging: Steamworks, met hand  │
                                                  │  Maillijst: Gumroad-mail als concept, na   │
                                                  │  ja versturen. Reddit: Thijs zelf.         │
                                                  └──────────────────┬────────────────────────┘
                                                                     v
 ┌───────────────────────────────────────────────────────────────────────────────────────────┐
 │ STAP 7  Cijfers terug (workflow Scorebord elke dag 06:41 UTC + wekelijkse Claude-run)     │
 │         winkels (openbaar, staat er) + Gumroad-verkopen + Polar + YouTube + Metricool     │
 │         -> organisatie/scorebord.md; elke actie na 14 dagen: doorgaan of stoppen          │
 └───────────────────────────────────────────────────────────────────────────────────────────┘
```

### Per stap: tool, wat Thijs één keer doet, kosten, wat er al is

| Stap | Tool | Thijs één keer | Kosten per maand | Bestaat al in de repo |
|---|---|---|---|---|
| 1 Uitgavepakket | GitHub Actions, `git log`, `gh release` | niets | € 0 | tags (`click-joints-v0.1.1`, `bison-flex-2026.1.0-20261108`), `.claude/skills/update-tekst/` |
| 2 Tekst | Claude-run met skill `update-tekst`, keuring Daan | niets | € 0 extra | skill; alleen `producten/obsidian-rollwright/CHANGELOG.md` bestaat, Click Joints en Bison & Flex hebben nog geen CHANGELOG.md |
| 3a Blender | `POST https://extensions.blender.org/api/v1/extensions/<id>/versions/upload/` met token en `release_notes` | token maken op zijn profielpagina van extensions.blender.org, als secret `BLENDER_EXTENSIONS_TOKEN` (3 min) | € 0 | `click-joints-uitgave.yml` (zip, sha256, Blender-validatie) |
| 3b JetBrains | `POST https://plugins.jetbrains.com/api/updates/upload` | niets meer: `JETBRAINS_MARKETPLACE_TOKEN` staat sinds 8 nov | € 0 | `jetbrains-bison-flex-upload.yml` (met alle poorten) |
| 3c Steam | steamcmd via game-ci/steam-deploy naar een beta-tak | bouwaccount + `STEAM_CONFIG_VDF` (staat al in `berichten/hoofdchat.md`, 18 nov); live zetten op default blijft met de hand | € 0 | `steam-uitbrengen.yml` (proefdraai groen) |
| 3d Gumroad Pro, Superhive | met de hand (hoofdchat) | niets | € 0 (Gumroad 10% + $0,50 per verkoop) | `click-joints-pro-uitgave.yml` (zip als artefact) |
| 4 Beelden | Godot Movie Maker, Blender Cycles, Xvfb, ffmpeg in Actions | niets | € 0 | zie punt 4 hieronder |
| 5 Wachtrij | `organisatie/goedkeuren.md` | niets | € 0 | bestaat, met berichten 12:00 en 20:00 |
| 6 Social | Metricool via MCP (hoofdchat) | niets voor 1 merk; tweede merk @hatsofthefallen kost Starter | € 0 nu; € 16 tot 20 bij Starter (voorstel, zie 3) | merk "screencuts.co" met TikTok en YouTube gekoppeld (GEZIEN in Metricool, 18 nov) |
| 6 Mail | Gumroad volgers + `/v2/emails` (concept), of Buttondown | Click Joints Free als $0+ op Gumroad zetten (hoofdchat kan dit, eerste keer nieuw product = hoofdchat) | € 0 | Gumroad-winkel "Dortus" |
| 7 Cijfers | `scorebord.py` + Gumroad-API + YouTube Data API + Metricool MCP | Gumroad-token (5 min), optioneel YouTube-API-sleutel (5 min) | € 0 | `scorebord.yml`, `scorebord.py` (Blender, Garmin, Obsidian, JetBrains, Superhive, Amami) |

**Totaal nu: € 0 per maand.** Er is één betaalvoorstel (Metricool Starter), zie punt 3.

---

## 2. Wat echt kan, per onderwerp (met bron)

### (1) Van commit of tag naar changelog en conceptposts
- **Kan, zonder geld.** Actions doet het vaste werk (log verzamelen, beelden maken), een Claude-run die al draait schrijft de tekst met `update-tekst`. Geen taalmodel in Actions nodig. Een Claude in Actions vraagt een Anthropic-sleutel of abonnementstoken (GOK, niet nagekeken) en dat voegt niets toe: de geplande taken bestaan al (`organisatie/geplande-taken.md`).
- **JetBrains:** de officiële Gradle-plugin `org.jetbrains.changelog` haalt de notities voor een versie uit CHANGELOG.md (`getChangelog`, `patchChangelog`) en vult `changeNotes` (GEZIEN, https://github.com/JetBrains/gradle-changelog-plugin README). Nu staan de notities met de hand in `plugin.xml` (`<change-notes>`, GEZIEN regel 41). Eén bron, geen dubbel werk.
- **Blender:** de upload-API neemt `release_notes` mee in dezelfde aanroep (GEZIEN, https://developer.blender.org/docs/features/extensions/ci_cd/). Dus CHANGELOG.md gaat in één keer mee met de zip.
- **Steam:** Steam maakt zelf een RSS-feed van elke aankondiging, `https://steamcommunity.com/games/<appid>/rss` (GEZIEN, https://partner.steamgames.com/doc/marketing/event_tools). Daarmee kan een workflow een nieuwe aankondiging zien en er een conceptpost van maken.

### (2) Automatisch uploaden naar winkels
| Winkel | Wat kan | Wat niet | Bron |
|---|---|---|---|
| Blender extensions | Nieuwe versie van een bestaande extensie uploaden met `Authorization: bearer <token>`, zip en release_notes. Token maak je op je profielpagina. | De eerste inzending van een nieuwe extensie (gaat met de hand en wordt gekeurd, GOK uit 11-toegang.md). | GEZIEN, ci_cd-pagina hierboven. Onze 0.1.1 stond 16 nov binnen ±40 min na uploaden live (GEZIEN, `platformen/blender/status.md` 07:40 en 08:20 UTC). |
| JetBrains Marketplace | Upload met permanent token, `pluginId`, kanaal, en `isHidden=true` om na goedkeuring nog niet openbaar te zijn. Elke update gaat langs de keuring van JetBrains. | Niets extra nodig; workflow staat. | GEZIEN, https://plugins.jetbrains.com/docs/marketplace/plugin-upload.html |
| Gumroad | API v2 heeft producten, verkopen, mails (`/v2/emails`: maken, voorbeeld, inplannen, versturen), UTM-links, en bestanden (`files/presign`). `/v2/emails` en `/v2/sales` antwoorden 401 zonder sleutel, dus ze bestaan live (GEZIEN, curl op api.gumroad.com). | Uploaden van een nieuw Pro-bestand via de API: in de broncode gezien (https://github.com/antiwork/gumroad, `config/routes.rb`), niet getoetst. Tot het getoetst is: met de hand. | GEZIEN broncode; de docs-pagina gumroad.com/api is met curl niet leesbaar (alleen JavaScript). |
| Superhive | Geen verkopers-API gevonden. | Uploaden blijft met de hand. | GOK (niet gevonden) |
| Steam | Build uploaden met steamcmd en automatisch live zetten op een beta-tak (`SetLive`). | **De default-tak kan niet automatisch live: "That must be done through the App Admin panel."** Winkelpagina en aankondigingen: geen API in de documentatie gevonden; aanmaken gaat in Steamworks. | GEZIEN, https://partner.steamgames.com/doc/sdk/uploading en event_tools |
| Garmin | Geen upload-API; elke upload met de hand. | | DERDEN (onze eigen notitie, 11-toegang.md: verzoek CIQQA-4193 bij Garmin) |
| Obsidian | Updates komen uit GitHub-releases. | Geparkeerd. | 11-toegang.md |

### (3) Inplannen op social: Metricool, Buffer en anderen
**Metricool (wat we hebben, GEZIEN in de tool-beschrijvingen van de Metricool-koppeling en op https://metricool.com/pricing/):**
- `createScheduledPost`: inplannen met tekst, `media` als openbare URL (release-assets van GitHub werken, zo gingen filmpjes 7, 9 en 2), TikTok-titel, YouTube-titel en "madeForKids". Twee nuttige standen: `draft: true` (concept in Metricool) en `autoPublish: false` (Metricool stuurt op het moment zelf een melding naar de Metricool-app op de telefoon en Thijs drukt zelf op plaatsen).
- `createScheduledPostForReview` en `sendScheduledPostForReview`: echte goedkeuringsstroom met reviewers en "any/all/optional". **Vraagt een plan met teambeheer**; op de prijspagina staat "Post approval system" pas bij **Advanced, vanaf € 43 per maand (jaar) of € 54 (maand)**. Niet nodig: onze wachtrij plus het ja in de chat doet hetzelfde voor € 0.
- `getBestTimeToPostByNetwork`: beste uren per netwerk (twitter, facebook, instagram, linkedin, youtube, tiktok) voor maximaal een week.
- `getAnalyticsDataByMetrics` + `getAnalyticsAvailableMetrics`: per TikTok-filmpje weergaven, bereik, likes, delen, kijkduur, % helemaal bekeken, en waar de weergaven vandaan komen (For You, zoeken, profiel, geluid, hashtag) (GEZIEN, velden TKPO01 tot TKPO22).
- **Plannen:** Free = 1 merk, alle netwerken behalve LinkedIn en X, **20 posts per maand**, 30 dagen cijfers, MCP inbegrepen. Starter vanaf € 16 per maand (jaar) of € 20 (maand) voor tot 5 merken en onbeperkt plaatsen. De Metricool REST-API (voor GitHub Actions) zit alleen in Advanced. Wij hebben nu 1 merk met TikTok @dortusstudio en YouTube @Dortusapps (GEZIEN, 18 nov). Welk plan we hebben staat niet in de repo; 1 merk past bij Free (GOK).
- **Gevolg:** met één filmpje per dag (planning.md) zitten we op ±30 per maand, boven de 20 van Free. Of een post naar twee netwerken als één telt, is niet nagekeken (GOK). **Voorstel aan Thijs (geld):** Metricool Starter, € 16 per maand bij jaarbetaling of € 20 per maand los. Levert op: onbeperkt inplannen en een tweede merk voor @hatsofthefallen (nu niet gekoppeld). Verwachte opbrengst: GOK; pas doen als we de 20 echt halen en de filmpjes-meting van 1 dec niet "stoppen" zegt.

**Buffer (GEZIEN, https://buffer.com/pricing en https://developers.buffer.com/):** Free = 3 kanalen, 10 ingeplande posts per kanaal, **API-toegang met 1 sleutel** (1.000 verzoeken per kanaal per maand), concepten maken via de API ("Create Draft Post"). Essentials $5 per kanaal per maand. Het voordeel boven Metricool: de API werkt gratis vanuit GitHub Actions. Het nadeel: een tweede wachtrij naast Metricool. **Advies: niet nu.** Alleen als reserve als Metricool Free te krap wordt en Thijs geen Starter wil.

**Anders:** BrightBean Studio (open bron, zelf hosten) staat al op MISSCHIEN in `platformen/succes/tools-producthunt.md`; vraagt een server, dus niet nu.

### (4) Clips en GIF's uit de build (wat we al hebben)
| Workflow | Wat het maakt | Gereedschap |
|---|---|---|
| `steam-hol.yml` | film van een minuut spelen, GIF op 5 fps, losse beelden | Godot `--write-movie`, `producten/steam-hol/e2e/gif.py` (PIL) |
| `steam-hol-clips.yml` | mp4-clips van 12 s rond een moment uit het spellog ("ate", "is back for") | Movie Maker + `e2e/clips.py` (ffmpeg) |
| `click-joints-render.yml` | eerlijke Cycles-render en film van de geëxporteerde delen | Blender headless |
| `click-joints-pro-film-release.yml` | demofilm en GIF als release, met ffprobe-controle 1920x1080 H.264 | ffmpeg |
| `filmpjes-week-1.yml` | staande 9:16 filmpjes met tekst uit echte beelden | ffmpeg, PIL, Inter |
| `filmpjes-geluid.yml` | zelfgemaakt geluid onder de filmpjes, beeld 1 op 1 | code-geluid + ffmpeg |
| `jetbrains-bison-flex-film.yml` | beelden en film in de echte IDE | Xvfb, xdotool, ImageMagick |

**Wat ontbreekt:** één vast beeldpakket per uitgave, met vaste namen, zodat stap 6 altijd dezelfde URL's heeft:
`<tag>-beelden/gif-5s.gif` (README en winkel), `kort-9x16-geluid.mp4` (TikTok, Shorts), `16x9.mp4` (Steam, YouTube), `still-1.png` tot `still-3.png`. Maak het als herbruikbare workflow (`workflow_call`) die de bestaande stappen per product aanroept. Spel: Movie Maker + clips.py. Click Joints: Cycles-film. Bison & Flex: IDE-film. Alles echte beelden uit het product, zoals de brief eist.

### (5) Cijfers vanzelf in `organisatie/scorebord.md`
| Bron | Hoe | Thijs één keer | Status |
|---|---|---|---|
| Blender, JetBrains, Garmin, Obsidian, Superhive, dortus.com (Amami) | `scorebord.py`, openbaar of `AMAMI_API_KEY` | niets | draait elke dag (GEZIEN, `scorebord.yml`) |
| Gumroad (Click Joints Pro, later Free $0+) | `GET /v2/sales` en `/v2/sales/summary`; alleen aantallen per product wegschrijven, nooit namen of mailadressen | in Gumroad een app maken en een toegangssleutel, secret `GUMROAD_TOKEN` (5 min). Let op: welke rechten zo'n sleutel heeft is niet nagekeken (GOK); script alleen lezen. | nieuw; nu "zie hoofdchat" |
| Polar (Rollwright) | `GET /v1/orders` of `/v1/metrics` met `POLAR_TOKEN`, alleen lezen (besluit 10 nov) | niets, staat er | nieuw in het scorebord; Rollwright is geparkeerd, dus laag |
| YouTube @Dortusapps | YouTube Data API: standaard 10.000 eenheden per dag gratis (GEZIEN, https://developers.google.com/youtube/v3/getting-started) | Google-API-sleutel maken (5 min), secret `YOUTUBE_API_KEY` | nieuw, optioneel (Metricool geeft het ook) |
| TikTok per filmpje | Metricool MCP `getAnalyticsDataByMetrics` (TKPO07 weergaven, TKPO13 helemaal bekeken, TKPO16 For You) | niets | kan alleen in een Claude-run (geen REST-API zonder Advanced): wekelijks door de hoofdchat of Chris naar `organisatie/scorebord-social.csv` |
| Steam verlanglijst | `IPartnerFinancialsService/GetAppWishlistReporting` per app per dag, met een "Financial API Group"-sleutel (GEZIEN, https://partner.steamgames.com/doc/webapi/IPartnerFinancialsService). Valve raadt een lijst met vaste IP-adressen aan; GitHub-runners hebben geen vast IP. | groep en sleutel in Steamworks (pas na de app) | besluit nodig: 11-toegang.md zei "niet aanmaken". Mijn advies: wel doen na paginadag; de sleutel kan alleen lezen, het script schrijft alleen totalen weg. Tot dan: Thijs leest het cijfer, de hoofdchat zet het erin. |
| Steam openbaar | spelers tegelijk (`GetNumberOfCurrentPlayers`, al in `steam-fest-meting.yml`), recensies (openbare `appreviews`-JSON, GOK) | niets | na paginadag |

**Plus de 14-dagenregel vanzelf:** elke marketingactie krijgt in `scorebord.md` een regel "actie, doel, start, dag 14". De workflow zet bij dag 14 "BESLIS" erachter, zodat niemand het vergeet (besluit 17 nov 16:50).

### (6) Maillijst
| Optie | Kosten | API | Past bij |
|---|---|---|---|
| **Gumroad volgers** | € 0 (geen maandprijs; 10% + $0,50 alleen bij betaalde verkoop, GEZIEN https://gumroad.com/pricing) | `/v2/emails` met publiek "followers" of "customers"; maken is standaard een concept, daarna `preview`, `schedule` of `send` (GEZIEN, `app/controllers/api/v2/emails_controller.rb` in de open broncode) | Click Joints en Pro: kopers en wie Free als $0+ haalt staan er al in. Follow-knop kan op dortus.com (GEZIEN, gumroad.com/features). |
| **Buttondown** | gratis tot 100 abonnees; RSS-naar-mail +$9, automations +$29 per maand (GEZIEN, https://buttondown.com/pricing) | concept maken en "Sending a draft email" via de API (GEZIEN, https://docs.buttondown.com/api-emails-create) | Eén Dortus-brief over alle producten, later. |
| **Steam volgen en verlanglijst** | € 0 | geen API; Steam mailt verlanglijsters zelf bij uitkomen en korting (GEZIEN, https://partner.steamgames.com/doc/marketing/wishlist) | Hats: dit ís de maillijst. Daarom altijd "wishlist en follow". |
| Kit, MailerLite | niet nagekeken (kit.com weigert curl) | | GOK |

**Advies:** begin met Gumroad (er is al een winkel, € 0, geen nieuw account). Elke mail is onder de naam van Thijs, dus: API maakt het concept, Thijs zegt ja, dan pas `send`. Mailadressen zijn persoonsgegevens: nooit in de repo, ook niet in een log van Actions.

---

## 3. Volgorde om te bouwen (meeste opbrengst voor de minste moeite)

| # | Wat | Moeite | Thijs | Waarom eerst |
|---|---|---|---|---|
| 1 | **Weekpakket social:** elke maandag één bundel van 5 tot 7 posts (tekst, beeld-URL uit releases, tijd uit `getBestTimeToPostByNetwork`) in `goedkeuren.md`; één ja, de hoofdchat plant alles in Metricool | klein (alleen afspraak en sjabloon) | één ja per week in plaats van per post | Kost het minst en spaart Thijs de meeste vragen. De filmpjes-meting van 1 dec heeft regelmaat nodig. |
| 2 | **Blender-upload in `click-joints-uitgave.yml`:** stap met `curl` naar versions/upload, release_notes uit CHANGELOG.md, alleen bij invoer "uploaden" en na keuring | 1 run | token, 3 min | Elke update van Click Joints Free gaat dan zonder Thijs live. Nu kost elke versie hem een upload (0.1.1 op 16 nov). |
| 3 | **Scorebord erbij:** Gumroad-verkopen, wekelijkse Metricool-cijfers per filmpje, 14-dagenregel | 1 tot 2 runs | Gumroad-sleutel, 5 min | Nodig voor de meting van wo 9 dec en om acties op tijd te stoppen. |
| 4 | **CHANGELOG.md voor Click Joints en Bison & Flex**, en JetBrains `changeNotes` uit die CHANGELOG (Gradle-changelogplugin) | 1 run | niets | Eén bron voedt winkel, release, post. Voorwaarde voor 5. |
| 5 | **`uitgave-pakket.yml` + beeldpakket:** op elke tag bron.md en vaste beeldnamen; de eigenaar draait `update-tekst` | 2 tot 3 runs | niets | Daarna is een uitgave: tag zetten, één keuring, één ja. |
| 6 | **Maillijst:** Click Joints Free als $0+ op Gumroad, follow-knop op dortus.com, eerste mail als concept bij Pro 1.1 | 1 run + hoofdchat | ja op de mailtekst | Bouwt een eigen lijst die geen algoritme nodig heeft. |
| 7 | **Steam (vanaf paginadag ±8 dec):** bouwaccount (staat al klaar), aankondiging elke twee weken via `update-tekst`, Steam-RSS naar conceptposts, besluit over de wishlist-sleutel | 2 runs | bouwaccount, en wel of geen Financial-sleutel | Hoofdzaak, maar kan pas na de pagina. |
| 8 | Pas als het knelt: Metricool Starter (€ 16 tot 20 per maand) | geen bouw | ja op geld | Alleen als we boven 20 posts per maand komen of @hatsofthefallen erbij moet. |

---

## 4. Per product: de drie automatiseringen met de meeste kans

**Hats of the Fallen (Steam)**
1. `steam-hol-clips.yml` vast maken als beeldpakket per build (spellog kiest het moment, dus elke build nieuwe echte clips voor @hatsofthefallen en de Steam-pagina).
2. `steam-uitbrengen.yml` met bouwaccount: elke speeltestbuild vanzelf op een beta-tak; Thijs zet alleen default live (moet van Valve met de hand).
3. Vanaf paginadag: wishlist per dag in het scorebord (Financial-sleutel, besluit nodig) en elke twee weken een aankondiging-concept met "wishlist en follow".

**Click Joints Free en Pro (Blender)**
1. Blender-upload met token in de bestaande uitgave-workflow (Free).
2. Free als $0+ op Gumroad: elke download wordt een volger voor de Pro-mail.
3. Gumroad-verkopen en UTM-links (`/v2/utm_links` bestaat in de API) in het scorebord: zien welke post tot een Pro-verkoop leidt.

**Bison & Flex (JetBrains)**
1. `changeNotes` uit CHANGELOG.md, dan is uploaden echt één knop (token en workflow staan al).
2. IDE-film (`jetbrains-bison-flex-film.yml`) als vast beeldpakket per versie, voor de pluginpagina en een post.
3. Downloads en beoordelingen staan al in het scorebord; voeg "proeflicenties naar betaald" toe zodra JetBrains dat via een verkopers-API geeft (niet nagekeken, GOK).

**Garmin (licht)**
1. Geen upload-API: niets bouwen. 2. Downloads staan al in het scorebord. 3. Gloop's Hat Tower meenemen in het weekpakket als verwijzing naar Hats, alleen met echte beelden.

---

## 5. Wat niet werkt of te duur is (niet proberen)
- **Steam default-tak automatisch live zetten:** kan niet volgens Valve (GEZIEN). Winkelpagina en aankondigingen: geen API gevonden, dus met de hand in Steamworks.
- **Metricool Advanced (€ 43 tot 54 per maand) voor de goedkeuringsknop of de REST-API:** te duur voor wat onze wachtrij gratis doet.
- **Buffer naast Metricool:** twee wachtrijen, dubbel werk. Alleen als reserve.
- **Zelf plaatsen door een agent, ook niet "even snel":** breekt harde regel 4 en de brief. Reddit, forums en Discord blijven met de hand (Reddit door Thijs).
- **"Link in bio" en muziek onder TikTok via Metricool:** werkt niet op een persoonlijk account (DERDEN via Joris, `planning.md`). Geluid zit daarom in de mp4 en de zoekregel in de tekst.
- **Garmin en Superhive automatisch uploaden:** geen API (Garmin DERDEN, Superhive GOK).
- **Een taalmodel in GitHub Actions voor de teksten:** kost een sleutel of geld (GOK) en de Claude-runs doen het al.
- **Gumroad-API voor Pro-bestanden zonder proef:** eerst één keer met de hand toetsen; een betaalde build mag nooit in een openbare release (besluit 15 nov 19:52).
