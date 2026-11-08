# Voorstel: Overwolf Appstore (apps in en naast pc-games)

Vera, 8 nov 2026 run 01:32 (UTC). Nagekeken door een controleur (akkoord, correcties verwerkt).

## Wat het is
Overwolf is een platform voor apps die naast of over een pc-game draaien: trackers, kaarten, coaches, clips, companions. Apps zijn HTML en JavaScript (of Electron). De maker verdient met advertenties in de app (maker 70%, Overwolf 30%) en met abonnementen of aankopen via Tebex. Sinds 1 nov 2026 keurt Overwolf alleen nog apps goed die Overwolf-advertenties, Tebex of allebei gebruiken (DERDEN: https://dev.overwolf.com/ow-native/monetization/overview).

## Cijfers

### Bereik
- GEZIEN: alle game- en categoriepagina's van de web-appstore doorgelopen: 234 geldige app-pagina's (276 namen, 36 gaven terecht 404, 2 later alsnog gevonden: Lunar Client en Among Us Notes). Elke pagina toont downloads en ratings. Data: `data/overwolf-apps-2026-11-08.jsonl` (232, zonder die 2), script `data/overwolf-haal-script.py`.
- GEZIEN: mediaan van alle 234 apps 30.188 downloads, 196 halen 1.000+ (84%), 84 halen 100.000+. Let op: dit zijn alle apps in de winkel, oud en nieuw door elkaar. Een publicatiedatum staat nergens op de pagina, dus een echte lichting nieuwe apps is niet compleet te meten.
- GEZIEN, beste benadering van een lichting: apps voor games die pas kort in Overwolf zitten. Arc Raiders kwam uit op 30 okt 2025, dus elke Arc Raiders-app is hooguit ±12 maanden oud. De game-pagina toont alle 16 ("viewed 10 of 16", alle 16 in de pagina-data). De apps alleen voor Arc Raiders van kleine makers:
  - MetaForge (een groep vrienden): 211.664 downloads, maar ook voor andere games, dus niet alles Arc Raiders
  - Arc Raiders Companion (Treestn Dev, waarschijnlijk dezelfde maker als Tarkov Companion, dus geen nieuwkomer): 172.309
  - ARCTracker.io (fansite): 141.017
  - ARC Forge (Jikouken, solo of klein, meer apps): 15.997
  - ArcTerminal (KofimBadam, klein, ook Deadlock Companion 15.065): 2.086
  - Startdatum is een aanwijzing op basis van de eerste review (5 nov tot 20 dec 2025), niet bewezen.
- GEZIEN, andere games: Deadlock-apps van kleine makers 92 tot 37.000 (mediaan van alle 20 Deadlock-apps 28.949), Roblox-apps van kleine makers 92 tot 54.000 (mediaan van alle 26: 9.845). Apps met een eerste review in 2026 van kleine makers: Killer Vibe 1.387, Deadlock Signal 1.519, Echoclip 685, Minecraft Companion 584, SysCubes 180.
- Conclusie bereik (GOK op basis van het bovenstaande): een goede app voor een nieuwe, populaire game haalt binnen een jaar 2.000 tot 200.000 downloads. Een app voor een rustige game of zonder eigen idee blijft bij honderden. Dat is veel beter dan bijna alle winkels die ik eerder mat. Wat we niet zien: apps die nooit door de keuring kwamen of uit de winkel zijn gehaald.

### Geld
- DERDEN: Overwolf betaalde in 2024 $240 miljoen en in 2025 meer dan $300 miljoen aan makers, maar dat is samen met CurseForge-modmakers en Tebex-servers (https://blog.overwolf.com/in-game-creators-earn-big-overwolf-pays-out-240-million-in-2024/, https://gamesbeat.com/overwolf-paid-out-300m-to-creators-so-far-this-year/). Hoeveel naar apps gaat staat nergens.
- DERDEN (oud): in 2020 kregen app-makers samen ±$10 miljoen per jaar (https://www.calcalistech.com/ctech/articles/0,7340,L-3843757,00.html).
- DERDEN: advertenties 70% voor de maker, uitbetaling vanaf $200 via Payoneer, 60 dagen na de maand (https://legal.overwolf.com/docs/overwolf/developers/developer-terms). Tebex: vergoeding sinds okt 2026 verlaagd naar 5% (https://blog.overwolf.com/the-new-tebex-new-fees-new-features/).
- NIET GEVONDEN: geen enkele kleine maker die openbaar zegt wat hij per maand verdient, en geen openbaar cijfer voor opbrengst per dagelijkse gebruiker. Overwolf toont dat alleen in het eigen ontwikkelaarsdashboard.
- GOK: per 1.000 dagelijkse gebruikers ±$100 tot $500 per maand voor de maker. Geen bron, niet op rekenen.
- Teken dat het werkt (GOK): bijna alle apps van kleine makers draaien advertenties (op 1 na alle Arc Raiders-apps), en makers bouwen er meerdere apps (Jikouken 3, KofimBadam 2, Treestn 2, Allory Dante 2). Dat doe je niet als het niets oplevert. Maar dat is geen bewijs.

### Drukte
- GEZIEN: per game 13 tot 30 apps in de winkel, totaal 234 zichtbaar. Heel rustig vergeleken met andere winkels (Elgato ±700 nieuwe per maand, itch.io duizenden). Overwolf geeft geen officieel totaal.

### Vindbaarheid
- DERDEN: appstore in de Overwolf-client en op het web, per game gesorteerd, 45 miljoen+ gamers per maand. Bij een nieuwe game is de lijst voor die game kort, dus je staat meteen bovenaan. Overwolf promoot apps zelf (meldingen bij andere apps) vanaf ±500 dagelijkse gebruikers, 50% terugkeer in week 2 en een rating van 4 (https://dev.overwolf.com/ow-native/getting-started/grow-your-app). Verder eigen werk via Discord, Reddit en YouTube.

### Past het bij ons
- Voor: apps zijn HTML en JavaScript, AI-hulp mag en Overwolf heeft er zelfs een handleiding voor (https://dev.overwolf.com/ow-native/guides/dev-tools/ai-coding-assistants-config). Een companion of tracker voor één game is in 1 tot 2 weken te bouwen.
- Tegen: eerst een voorstel indienen en wachten op goedkeuring door Overwolf (whitelist), daarna een QA-keuring; hoe lang dat duurt is niet gevonden. Riot-games (LoL, Valorant, TFT) vragen ook goedkeuring van Riot. Testen in de echte app op GitHub Actions is lastig: de Overwolf-client draait op Windows en vraagt een ontwikkelaarsaccount. Wij hebben ook niemand die de games speelt, dus we moeten de game kennen uit wiki's en data.
- Account: Thijs moet een ontwikkelaarsaccount maken en het app-voorstel indienen.

## Voor- en nadelen
Voor: echt bereik voor kleine makers (honderdduizenden downloads bij nieuwe games), weinig concurrentie per game, geld zit ingebouwd (70% advertenties), elke maand nieuwe games met Game Events (bijv. Battlefield 6, Palworld 1.0, Subnautica 2), en een duidelijk ritme: wie er vroeg bij is bij een grote nieuwe game, wint.
Tegen: opbrengst per gebruiker onbekend, keuring vooraf, afhankelijk van de populariteit van één game, en wij spelen zelf geen games.

## Eerste idee
Een companion voor een grote game die net Game Events in Overwolf kreeg en nog weinig apps heeft (bijvoorbeeld Subnautica 2 of de volgende grote lancering): kaart, voortgang, wat je nog mist, met advertenties en later Tebex-premium. Elke nieuwe grote game is een nieuwe kans, dus dit kan een reeks worden.

## Cijfer en advies
**Cijfer 6, nog niet klaar.** Bereik is het beste dat ik tot nu toe zag bij een winkel met ingebouwd geld. Wat ontbreekt is één hard getal: wat een app met 1.000 tot 10.000 gebruikers per maand opbrengt.
Wat er nog gemeten moet worden:
1. Opbrengst per gebruiker: zoeken naar makers die het delen (Discord van Overwolf, YouTube-interviews), of na goedkeuring van een voorstel vragen aan de DevRel-manager van Overwolf.
2. Hoe lang de keuring duurt en hoe vaak voorstellen worden afgewezen.
3. Herhaalmeting over 4 weken met `data/overwolf-haal-script.py`: nieuwe namen in de lijst zijn dan echte nieuwe apps met een bekende startdatum, en de groei van downloads per app wordt zichtbaar.
