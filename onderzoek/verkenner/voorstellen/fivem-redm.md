# Voorstel: FiveM en RedM (Cfx.re)

Vera, 9 nov 2026 run 11:31 (Amsterdam). Platformrun.

FiveM en RedM zijn de mod-platforms voor roleplay-servers in GTA V en Red Dead Redemption 2, van Cfx.re (sinds aug 2023 onderdeel van Rockstar; DERDEN, nieuws van toen, niet nagekeken in deze run). Servereigenaren kopen scripts (Lua, voor de frameworks ESX, QBCore, Qbox, vRP) bij makers. Verkopen mag alleen via Tebex, met de versleuteling (Asset Escrow) van Cfx. Sinds 12 jan 2026 is er ook een officiële Cfx Marketplace.

## Advies: nee voor nu, cijfer 3

Er wordt echt betaald (gewoon script ±$30, ±430 betaalde releases per maand op het forum), maar het bereik van een nieuwe maker is zwak en ik vond geen enkele kleine maker met een aantoonbaar bedrag. De servers draaien vooral scripts van een vaste groep studio's (de grootste met 15.000 tot 32.000 Discord-leden). Daarbij komt dat wij niet zelf in het spel kunnen testen zonder een GTA V-licentie en een Cfx-account (alleen Thijs kan die aanmaken).

## Cijfers

### Bereik
- GEZIEN (eigen meting, open serverlijst `frontend.cfx-services.net/api/servers/streamRedir/`, 9 nov ±10:37 UTC, geen robots.txt op die host): 33.513 servers in de lijst, 81.389 spelers op dat moment (Europese ochtend, dus geen piek). 31.154 GTA V, 1.875 RedM, 484 GTA V Enhanced. 4.986 servers van GTA V plus Enhanced hadden minstens 1 speler (alleen GTA V: 4.942).
- GEZIEN (eigen steekproef, resources per server via de open endpoint `/api/servers/single/<id>`, 588 servers: de 200 drukste plus 388 willekeurige met minstens 1 speler; spelersnamen niet opgeslagen): mediaan 223 resources per server. Frameworks: es_extended (ESX) 208, qb-core 99, qbx_core 97, vrp 71; ox_lib 494 (84%).
- GEZIEN, zelfde steekproef, scripts van bekende studio's (servers met minstens één resource met dat voorvoegsel): LB (lb-, telefoon en tablet) 226 (38%), rcore 218, kq_ 179, jg- 173, renewed 153, rtx_ 149, ps- 128, cd_ 124, wasabi_ 117, 0r- 112, 17mov 107, okok 98, loaf_ 91, qs- 81, lation_ 78. 418 van de 588 servers (71%) draaien iets van minstens één van deze 15 voorvoegsels; zonder renewed en ps- (grotendeels gratis open-source scripts, GOK) 383 (65%). Let op: een voorvoegsel kan soms ook van iemand anders zijn (GOK, klein effect bij de grote namen).
- NIET GEMETEN: hoeveel servers een betaald script van een nieuwe kleine maker na 3 tot 6 maanden draait. Resourcenamen staan niet in de forumtitels. Hoe het wel kan: per release uit mei of juni 2026 de resourcenaam uit de documentatie of de GitHub-link halen en in `data/fivem-resources-2026-11-09.json` opzoeken.
- GEZIEN (onderzoeker, forum.cfx.re, alle 381 betaalde releases van sep 2026): mediaan 260 views, 3,7% haalt 1.000+, 15% haalt 500+. Mediaan 1 like, 47% heeft 0 likes, mediaan 0 reacties. Alleen scripts: mediaan 227 views, 0 likes. Bovenaan bekende namen (RTX Gym 1.844 views, 70 likes).

### Geld
- GEZIEN (onderzoeker, marketplace.cfx.re, steekproef 119 van 1.088 pakketten): scripts mediaan $29,99 (kwartielen $17,99 en $41,99, van $2,99 tot $259,99). 469 producten op makerpagina's: ook mediaan $29,99.
- GEZIEN (docs.tebex.io/creators/llms-full.txt): Tebex rekent 15% voor FiveM (5% bij andere games), plus betaalkosten (PayPal 2,49% + $0,40). Maker houdt dus ±80%.
- GEZIEN (marketplace): ONX 152 pakketten, Popcorn RP 147, CodeM 69, RTX 52, rcore 37, JG 7 ($18,99 tot $78,99). Grote makers leven ervan (JG werkte 6+ maanden fulltime aan één script, DERDEN, tebex.io creator spotlight).
- NIET GEVONDEN: een bedrag van een kleine maker die sinds 2024 begon. TrustMRR heeft geen FiveM-profielen, interviews noemen geen omzet, verkoopaantallen staan nergens. Het geld is er op marktniveau, maar voor kleine makers niet aangetoond.

### Drukte
- GEZIEN (onderzoeker, forum.cfx.re categorie Releases, tag paid, per aanmaakmaand): nov 2025 474, dec 306, jan 2026 322, feb 317, mrt 512, apr 407, mei 526, jun 325, jul 375, aug 737, sep 432, okt 431. Gemiddeld ±430 per maand (430,3), ±2/3 scripts. Nov 2026: 268 in 8 dagen. Zie `data/fivem-forum-betaald-per-maand.txt`.

### Vindbaarheid
- Forum (aandacht laag, zie boven), eigen Tebex-winkel, Discord van de maker, YouTube-showcases.
- Cfx Marketplace sinds 12 jan 2026: gecureerd, 55 makers en 1.088 pakketten in de sitemap; elke Tebex-partner met FiveM-spullen mag aanvragen, Cfx keurt elk pakket, geen extra commissie (GEZIEN, docs.tebex.io creators cfx-marketplace). Dit is de enige echte winkel, en daar staan vooral de grote studio's.

### Regels
- Betaald verkopen alleen via Tebex met de levering van Cfx (forum releases-regels, nov 2024; Creator PLA 10 sep 2026). Max 1 release per 48 uur, verplicht tabelletje, geen eigen versleuteling.
- AI: geen verbod gevonden. Releaseregels: LLM's zijn prima hulpmiddelen, maar plak hun tekst niet als beschrijving. Gemeenschapsreactie niet te meten (forum-zoeken verboden door robots.txt, Reddit niet gelezen).
- Lekken: in aug 2025 erkende Cfx een lek in escrow; gelekte scripts zijn een bekend probleem (forum asset-security-update, 44.064 views).

### Past het bij ons
- Bouwen: Lua-scripts voor ESX of Qbox kan Claude schrijven, 1 tot 2 weken haalbaar (GOK).
- Testen: een server draaien kan zonder de game, maar vraagt een sleutel van portal.cfx.re (Cfx-account). In het spel testen vraagt een GTA V-licentie (±€15 tot €30, GOK). Accounts en licentie kan alleen Thijs regelen. Zonder echte test in het spel is een script kwetsbaar, en reviews in Discord zijn hard.
- Verkopen: Tebex-account (Thijs), bij voorkeur ook toelating tot de Cfx Marketplace.

## Controleur
Akkoord met cijfer 3 en nee voor nu. 6 correcties verwerkt: 418 (71%) in plaats van 384 (65%) servers met een studio-script, ±430 in plaats van ±450 releases per maand, 4.942 alleen GTA V, Qbox niet "snelst groeiend" (groei niet gemeten), Discord-getallen alleen voor de grootste studio's, Rockstar-overname zonder bron gemarkeerd.

## Voor- en nadelen
Voor: echte betalende markt met een vaste prijs rond $30, groot (tienduizenden servers), AI niet verboden, een officiële winkel die net open is.
Tegen: druk (±430 betaalde releases per maand), aandacht per release laag, servers vol met scripts van een vaste top, geen kleine maker met een bedrag gevonden, testen alleen met licentie en account van Thijs, lekproblemen, 15% afdracht.

## Eerste idee als we het ooit doen
Een klein, goed getest script voor Qbox (vaker op kleinere servers: 83 van 388 (21%) tegen 14 van de drukste 200 (7%); één meting, groei niet gemeten), verkocht via Tebex rond $15 tot $25, met een gratis versie op GitHub voor bereik.

## Herhaalmeting
Rond feb 2027: serverlijst en resources opnieuw met `data/fivem-stream-script.py`, `fivem-server-script.sh` en `fivem-resources-analyse-script.py`; dan ook releases uit het najaar van 2026 opzoeken in de resourcetelling (bereik van nieuwe makers). Opnieuw kijken als GTA V Enhanced of GTA 6 de markt omgooit (oude scripts die niet meer werken).
