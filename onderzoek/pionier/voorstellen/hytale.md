# Voorstel pionier: Hytale (mods en serverplugins via CurseForge)

Noor, 7 nov 2026. Meetlat van de pionier (vijf vragen). Cijfers: GEZIEN (zelf gezien of gemeten), DERDEN (met link), GOK.

## Kort
Hytale (Hypixel Studios, eigendom van de oprichters na terugkoop van Riot) kwam op 13 januari 2026 in early access en had een van de grootste modding-starts ooit: 10 miljoen mod-downloads in twee weken. Daarna zakte het hard en sinds mei is het stabiel op een laag niveau: ±150 tot 170 nieuwe projecten per maand (in januari 3.559), met een verdubbeling na Chapter 1 in oktober, en een nieuwe mod haalt in een paar maanden mediaan 100 tot 300 downloads. De eerste plek in serverhulpmiddelen (webkaart, anti-cheat, WorldEdit) is makkelijk te pakken, maar in een kleine, krimpende vijver, en verkopen in de winkel komt er niet: Hypixel wil "a community library, not a shopping mall".

**Cijfer 3. Advies: nee voor nu, op de wachtlijst.** Vraag 1 (groei) weegt het zwaarst en is hier negatief: een platform dat niet groeit is geen pionierskans, hoe leeg de categorieën ook zijn.

## 1. Groeit het platform hard en zichtbaar? Nee: na de piek hard gezakt, sinds mei stabiel
- Bij de lancering meer dan 1 miljoen spelers (DERDEN, https://en.wikipedia.org/wiki/Hytale). Verkochte exemplaren nu: niet gepubliceerd, niet te meten.
- Twitch: piek 441.374 kijkers dit jaar; laatste 90 dagen gemiddeld 121; laatste 30 dagen 298 door Chapter 1, laatste 7 dagen alweer 141 (DERDEN, https://sullygnome.com/game/hytale_1003606006/30). Op 7 nov 165 kijkers over 21 streams (DERDEN, https://mmostats.com/game/hytale).
- Spelers: in het voorjaar ±125.000 per dag, piek ±52.000 tegelijk (DERDEN, schatting, https://supercraft.host/article/hytale-2026-update-5-player-count-server-discovery/). Latere cijfers zijn zwakke modellen.
- Mod-downloads: 10 miljoen op 27 jan, 20 miljoen op 3 mrt (DERDEN, https://www.switchbladegaming.com/hytale/player-count-2026/), 31,8 miljoen op 7 nov (GEZIEN, eigen telling). Van maart tot nu dus ±1,5 miljoen per maand, tegen ±5 miljoen per week in januari.
- Motor die het kan omkeren: updates elke 1 à 2 maanden, Chapter 1 op 12 okt 2026, servercode als "Shared Source" op GitHub, aangekondigd 23 juni (DERDEN, Wikipedia). Geen datum voor 1.0; in het Chapter 1-bericht staat "if we release 6 Chapters before 1.0" (DERDEN, https://hytale.com/news/2026/10/chapter-i-out-of-the-breach), dus 1.0 ligt eerder in 2027 of 2028 (GOK). Xbox komt alleen "eventual", zonder datum (DERDEN, https://www.purexbox.com/news/2026/01/hytale-set-for-eventual-xbox-release-as-game-racks-up-millions-of-players-on-day-one).
- Wat het spel wel aan nieuwe spelers helpt: kopers van de Cursebreaker-editie krijgen per Chapter een gratis exemplaar om weg te geven, en Hypixel belooft een raamwerk voor minigames met een officiële pagina waar makers "may be featured" (DERDEN, Chapter 1-bericht).

## 2. Is de app-winkel jong? Ja
- CurseForge is de officiële plek sinds dag één; een mod-browser in het spel kwam met Update 6 eind augustus 2026 (DERDEN, https://www.g-portal.com/en/news/hytale-update-6-hardcore-mod-browser-en).
- Eigen telling via de open API-spiegel (gameId 70216), 7 nov (GEZIEN, script `data/hytale-curseforge-meet.py`): 6.807 projecten, waarvan 6.105 mods, 496 prefabs, 159 werelden.
- Nieuwe projecten per maand (GEZIEN): jan 3.559, feb 1.199, mrt 440, apr 422, mei 113, jun 166, jul 156, aug 166, sep 171, okt 333 (Chapter 1), nov tot de 7e 81. Let op: de API toont alleen projecten die nu nog online staan; verwijderde projecten tellen niet mee, dus jan en feb waren in werkelijkheid nog hoger en de val nog groter.
- Andere winkel Modtale: 412 projecten, 27.989 downloads (DERDEN via onderzoeker, https://modtale.net/). Verwaarloosbaar.

## 3. Kan er betaald worden? Alleen langs de zijkant
- Hypixel neemt 0% van servers en makers tot 13 jan 2028 (DERDEN, https://hytale.com/news/2025/12/hytales-1st-faq, https://hytale.com/server-policies).
- Servers mogen ranks, cosmetica, abonnementen en toegang verkopen (DERDEN, server-policies). Tebex en Tip4serv hebben Hytale-winkels. De EULA staat makers uitdrukkelijk toe hun mods zelf te verspreiden en te verkopen (DERDEN, https://hytale.com/eula, https://en.wikipedia.org/wiki/Hytale). Dus servers hebben geld en kunnen betaalde plugins kopen, bijvoorbeeld via BuiltByBit, dat een Hytale-sectie heeft (DERDEN, https://builtbybit.com/resources/hytale/plugins/). Aantallen en omzet daar niet te zien (Cloudflare).
- Betaalde mods in de officiële browser: nee. De baas wil "a community library, not a shopping mall", steun voor makers wordt onderzocht, geen plan of datum (DERDEN, https://www.pcgamesn.com/hytale/paid-mods-discussion).
- CurseForge Rewards: punten naar aandeel downloads, $0,05 per punt (DERDEN, https://www.gemlist.io/blog/how-much-does-curseforge-pay-mod-creators). Voor een mod met een paar duizend downloads per maand enkele dollars (GOK).

## 4. Is er vraag te zien? Deels
- Reddit, Discord en de reacties op CurseForge waren niet te lezen (geblokkeerd). Geen directe meting.
- Waar de downloads heen gaan (GEZIEN): spelinhoud. Mods met quests of dungeons samen ±1,3 miljoen downloads, de top (Endgame & QoL) 511.749. Serverhulpmiddelen halen weinig: webkaart samen ±11.000, anti-cheat ±3.000, WorldEdit 393, backups 1.316.
- Servers adverteren met economie, landclaims, winkels, crates en dungeons (DERDEN via onderzoeker, https://hytaletop100.com/, 270 servers op de lijst).

## 5. Is de eerste plek te pakken? Ja, maar de prijs is klein
| Categorie | Nummer één nu | Downloads (GEZIEN) | Sterkte |
|---|---|---|---|
| Webkaart (zoals Dynmap of BlueMap in Minecraft) | EasyWebMap | 8.959, laatste update 17 jan | zwak, geen BlueMap-achtige 3D-kaart |
| Anti-cheat | Anti Cheat / HyAntiCheat | 884 / 867 | vrijwel leeg |
| WorldEdit | WorldEdit Classic | 393 | leeg |
| Stemmen (Votifier) | HyVotifier | 4.158 | klein, actief |
| Kaart in het spel | BetterMap | 1.005.220 | onaantastbaar |
| Landclaims | Simple Claims | 96.264 | sterk |

Maar hoeveel kan een nieuwe mod nu halen (GEZIEN, mods per maand van aanmaken, downloads tot 7 nov): gemaakt in jan mediaan 719 en 358 boven 10.000; gemaakt in jun tot sep mediaan 111 tot 197, het beste tiende boven ±800 tot 1.300, en samen 8 van 581 boven 10.000. Jongere mods hebben minder tijd gehad; okt (mediaan 47) en nov zijn daarom niet te vergelijken en laat ik weg. Nummer één worden in webkaart betekent dus misschien enkele duizenden downloads en weinig geld.

## Risico en waaraan je een omslag ziet
Het risico is niet dat Hytale verdwijnt (sterke studio, veel fans, regelmatige updates), maar dat het een middelgroot spel blijft na een hype-piek. Teken van een omslag: 1.0 of een grote Chapter die de instroom twee maanden achter elkaar terugbrengt naar 500+ nieuwe projecten per maand (het niveau van maart en april, toen een nieuwe mod nog mediaan ±250 downloads haalde en 17 van de 373 boven 10.000 kwamen), of Hypixel kondigt betaalde mods of een makersfonds met datum aan.

## Categorie en eerste productidee (als het omslaat)
Webkaart voor serverbeheerders: een 3D-kaart in de browser van de serverwereld met spelers, claims en markers (zoals BlueMap in Minecraft), gratis op CurseForge, met een betaalde versie via BuiltByBit (eigen thema's, meerdere werelden, koppeling met Simple Claims). Huidige leider is sinds januari niet bijgewerkt. Risico: de servercode is open en Hypixel bouwt zelf hulpmiddelen (mod-browser, minigame-raamwerk); een officiële webkaart zou dit product overbodig maken.

## Wat ik niet kon meten
Verkochte exemplaren nu, Reddit en Google Trends, omzet op BuiltByBit, het echte bedrag per download bij CurseForge, vragen op Discord. Herhaalmeting: `python3 data/hytale-curseforge-meet.py` rond 7 dec; nieuw per maand en mediaan van nieuwe mods zijn de twee getallen die tellen.

## Cijfer en advies
3 van 10 (de controleur gaf 3 of 4). Nee voor nu, wachtlijst. Vraag 2 en 5 zijn goed (jonge winkel, lege categorieën), maar vraag 1 is negatief en vraag 3 zwak (geen betalen in de winkel, baas wil het niet). Opnieuw kijken bij een van de tekens hierboven.

## Nagekeken
Controleur (agent) 7 nov: alle steekproefcijfers kloppen met de ruwe data; 8 correcties verwerkt (toon "krimpt" verzacht naar "gezakt en stabiel", API telt verwijderde projecten niet, medianen per aanmaakmaand, citaat 6 Chapters voor 1.0, EULA staat verkopen toe, omslaggrens onderbouwd op 500, risico officiële hulpmiddelen, datum Shared Source).
