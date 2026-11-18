# Toegang: wie kan waar bij, en wat er nog moet (18 nov 2026)

Doel (Thijs, 18 nov 21:12): de ploeg en de hoofdchat kunnen overal bij wat nodig is, zodat werk niet blijft liggen op een klik. Grens die blijft: wachtwoorden, sleutels en betaalgegevens typt **alleen Thijs**. Agents en de hoofdchat typen nooit een sleutel in; ze gebruiken hem alleen via een GitHub-secret of een koppeling.

## Drie manieren van toegang
1. **GitHub-secret** (voor workflows in Actions; de agents starten die workflow met een tag-push, zie onder). Thijs zet de sleutel één keer in GitHub: dortus-hq, Settings, Secrets and variables, Actions, New repository secret. Een sleutel mag maar één ding kunnen.
2. **Chrome van Thijs** (alleen de hoofdchat, op de HP): inloggen met zijn Google en doorklikken mag (besluit 17 nov). Geld, ID, bank en eigen gegevens blijven bij Thijs.
3. **Koppeling in Claude** (hoofdchat): Metricool werkt. Gmail, Polar-koppeling en de andere uit harde regel 7: niet.

## Workflows starten zonder GitHub-sleutel
De GitHub-sleutel in onze sessies werkt niet (GH_TOKEN ongeldig, GEZIEN 18 nov), dus "Run workflow" kan de ploeg niet. Oplossing: **elke uitgave-workflow start ook bij het pushen van een tag** (bijvoorbeeld `click-joints-v0.1.3`, `bison-flex-v2026.1.2`), met dezelfde controles als nu (tests groen, Daan akkoord). Een tag pushen kan iedereen met git. Dit bouwen de eigenaars (Bram voor Click Joints, Chris voor Bison & Flex, Olaf voor Steam).

## Stand per dienst
| Dienst | Waarvoor | Hoe | Stand | Wat Thijs nog doet |
|---|---|---|---|---|
| GitHub dortus-hq | alles | git (push werkt) | werkt | niets |
| Garmin | uploaden of signeren | secret `GARMIN_DEV_KEY` | staat er | niets |
| JetBrains Marketplace | Bison & Flex uploaden | secret `JETBRAINS_MARKETPLACE_TOKEN` | staat er (8 nov) | niets |
| Polar | verkopen lezen | secret `POLAR_TOKEN` (alleen lezen gebruiken) | staat er (10 nov) | niets |
| Amami | bezoekers dortus.com | secret `AMAMI_API_KEY` | staat er (16 nov) | niets |
| Blender extensions | Click Joints uploaden | secret `BLENDER_EXTENSIONS_TOKEN` | staat er (18 nov 21:31) | niets |
| Gumroad | verkopen en doorkliks lezen | secret `GUMROAD_ACCESS_TOKEN` (alleen lezen gebruiken) | staat er (18 nov 21:34) | niets |
| Kit (maillijst) | aanmeldingen en mails als concept | secret `KIT_API_KEY` | account en sleutel staan er (18 nov 21:39), naam Dortus, gratis plan | bevestigingsmail van Kit aanklikken; postadres (geen woonadres) pas bij de eerste mail |
| Steam (uploaden) | build naar verborgen tak | secrets `STEAM_USERNAME`, `STEAM_CONFIG_VDF` | wacht op Valve | na goedkeuring: apart bouwaccount met alleen uploadrechten, ±15 min |
| Steam verlanglijsten | verlanglijsten per dag lezen (`GetAppWishlistReporting`) | secret `STEAM_FINANCIAL_API_KEY`: een sleutel van een **Financial API Group** in Steamworks, een gewone Web API-sleutel werkt hier niet (GEZIEN in de Steamworks-documentatie door zoeker B, 18 nov) | na paginadag | groep en sleutel aanmaken, ±5 min |
| YouTube Data API | video's en cijfers lezen | secret `YOUTUBE_API_KEY` | **ontbreekt** | Google Cloud, API-sleutel alleen voor YouTube Data, ±10 min (mag later) |
| Google Search Console | zoekcijfers dortus.com | Chrome (hoofdchat) | geverifieerd 18 nov 21:43 (HTML-bestand in de root van dortus.com; laten staan) | niets |
| Google Alerts | vermeldingen volgen | secret `GOOGLE_ALERTS_FEEDS` (4 RSS-adressen, één per regel: Click Joints, Hats of the Fallen, Bison & Flex, Dortus) | staat er (18 nov 21:46) | niets |
| Metricool | inplannen en cijfers | koppeling (hoofdchat) | werkt (Free, 20 posts per maand) | TikTok @hatsofthefallen koppelen als we dat kanaal gebruiken |
| Discord | Hats-community | Chrome (hoofdchat); berichten via secret `DISCORD_WEBHOOK` | server Hats of the Fallen staat, account thijs@dortus.com; webhook staat er (18 nov) | niets |
| Anthropic API | automatische keurder (`.github/workflows/keurder.yml`) | secret `ANTHROPIC_API_KEY` (sleutel `dortus-keurder`, Standaardwerkruimte); model kiezen kan met variabele `KEURDER_MODEL` | aangemaakt 18 nov ±22:30; betaald uit het API-tegoed van Thijs ($200 per maand, GEZIEN in de console) | maandlimiet in de console in de gaten houden |
| Meldingenrepo Bison & Flex | bugtracker-link in de listing | GitHub `thijsduinhouwer2002-coder/bison-flex` (openbaar) | aangemaakt 18 nov 21:47, alleen README | niets; Chris vult hem en zet hem in de listing |
| Superhive, Gumroad, Garmin, Steamworks, JetBrains-dashboard | instellingen, teksten, keuringen | Chrome (hoofdchat) | werkt | niets |

Samen ±1 uur voor Thijs, in één keer te doen. De hoofdchat opent in Chrome de juiste pagina's; Thijs maakt en plakt de sleutels zelf.
