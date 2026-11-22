# Voorstel: Discord (apps en bots)

**Advies: nee voor nu. Cijfer: 5 van 10** (was 4, nog niet klaar). Herzien op 6 nov 2026, run 21:31, nu met een eigen meting. Het geld is beter dan bij de meeste platformen die we bekeken: er zijn nu drie kleine, jonge bots met geverifieerd meer dan $300 per maand, en 1 op de 7 nieuwe apps in de officiële App Directory heeft Discords eigen betaalfunctie aangezet. Maar het bereik haalt de grens die we vooraf vastlegden ruim niet: een nieuwe app in de directory zit na 3 tot 6 maanden op een mediaan van 14 servers. Om €350 per maand te verdienen heb je volgens de drie voorbeelden met bekende aantallen ruwweg 170 tot 10.000 servers nodig. 100+ servers haalt ±15% van de nieuwe apps, 1.000+ haalt ±2%. Geen manager voorlopig.

## Hoe gemeten (GEZIEN, 6 nov 2026)
- **Officiële App Directory van Discord**: de openbare zoek-API (`discord.com/api/v9/application-directory-static/search`, geen sleutel) met 17 zoektermen en 6 categorieën uitgelezen. 18.343 unieke apps, van de ±19.600 die de directory zelf telt (±93%). Per app: aantal servers (`guild_count`, door Discord afgerond), betaalvlag (`is_monetized`) en de aanmaakdatum, die in het id van elke app zit.
- **Discords eigen winkel**: voor alle 445 betaalde apps uit feb tot aug 2026 de producten en prijzen opgehaald (`store/published-listings/skus`).
- **discordbotlist.com**: alle 25.598 bots uit de sitemap via de openbare API per bot. 23.612 gelezen, 1.985 fout of weg. Per bot: datum op de lijst, en het serveraantal als de bot dat zelf doorgeeft.
- top.gg geeft nog steeds 403 met curl, ook de sitemap. discord.bots.gg heeft maar 1.281 bots en sinds 2024 bijna geen nieuwe meer (1 in 2025), dus niet bruikbaar.
- Scripts en data: `data/discord-haal-script.py`, `data/discord-dbl-script.py`, `data/discord-sku-script.py`, `data/discord-analyse-script.py`, en de bestanden `data/discord-*-2026-11-06.json` en `data/discord-sku-feb-aug-2026.json`.

**Let op bij de meting:**
- De aanmaakdatum is de dag dat de maker de app aanmaakte in het ontwikkelaarsportaal, niet de dag van lancering. Apps zijn dus soms ouder dan de datum doet denken, wat de cijfers eerder te mooi maakt dan te somber.
- De directory bevat alleen apps die de maker zelf vindbaar maakte. Bots die dat niet doen zijn hier niet geteld; die doen het waarschijnlijk niet beter (GOK).
- Oudere groepen zien er beter uit, maar dat komt deels doordat dode apps uit de directory verdwijnen (GOK, niet gemeten).

## Cijfers

**Bereik (GEZIEN, App Directory)**

| Aangemaakt | Aantal apps | Mediaan servers | 100+ servers | 1.000+ servers |
|---|---|---|---|---|
| mei tot aug 2026 (2 tot 6 maanden) | 2.089 | 14 | 15% | 1,9% |
| feb tot aug 2026 (2 tot 9 maanden) | 3.257 | 18 | 18% | 2,2% |
| jan tot jun 2025 (16 tot 22 maanden) | 1.826 | 50 | 36% | 9,3% |

- Strak 3 tot 6 maanden oud (aangemaakt 6 mei tot 6 aug 2026, nagerekend door de controleur): 1.554 apps, mediaan 15, 16% haalt 100+, 2,1% haalt 1.000+.
- Alleen de betaalde apps van mei tot aug 2026 (271): mediaan 14 servers, 18% haalt 100+, 1,8% haalt 1.000+. Betaald zijn doet het bereik dus geen kwaad, maar helpt ook niet.
- Per maand ziet het er zo uit: apps uit februari 2026 mediaan 39, uit augustus 2026 mediaan 10. Oudere apps zitten dus hoger; of één app zo groeit is niet gemeten, en survivorship speelt mee (GOK).
- Beste nieuwe betaalde apps (feb tot aug 2026): rbxsociety v2 10.700 servers, DisDubs 9.360, Server Manager 5.960, SpiderEye 4.650, WoS Oracle 4.560. Daarna zakt het snel onder de 1.600.

**Bereik (GEZIEN, discordbotlist.com)**
- 1.827 bots kwamen van feb tot aug 2026 op de lijst. 777 daarvan (43%) geven zelf een serveraantal door: mediaan 98, de helft haalt 100+. De andere 57% geeft niets door; dat zijn vooral bots die niet actief bijgehouden worden (GOK).
- 661 van die 1.827 (36%) staan ook in de directory. Hun aantal servers volgens Discord: mediaan ±100. Dat is veel beter dan de 14 tot 18 van de hele directory. Bots die hun maker ook op botlijsten zet, doen het dus duidelijk beter, maar of dat komt door de lijst of door een actievere maker is niet te scheiden.
- Let op: de datum op discordbotlist.com is de dag waarop de bot op de lijst kwam, niet de aanmaakdatum. Daar zitten ook oude bots tussen.

**Geld**
- GEZIEN: 2.938 van de 18.343 directory-apps (16%) hebben de betaalvlag. Bij apps van feb tot aug 2026: 445 van 3.257 (14%). 347 daarvan hebben producten in Discords eigen winkel. Prijzen: 641 producten met bekende prijs, mediaan $4,99. Discords eigen betaalfunctie wordt dus volop gebruikt, ook door nieuwe makers.
- GEZIEN (via TrustMRR, dat de omzet zelf uit Stripe of Polar haalt; onderzoeksagent las de pagina's met curl):
  - **BabelBot** (vertaalbot, Nederlandse maker, app aangemaakt maart 2025): $920 per maand, $2.043 in de laatste 30 dagen, $7.009 totaal. Volgens de directory 2.310 servers, met betaalvlag. [trustmrr](https://trustmrr.com/startup/babelbot)
  - **CopyKitten** (stem klonen, app juli 2025): $333 per maand, 68 abonnementen. Directory: 8.950 servers, met betaalvlag. [trustmrr](https://trustmrr.com/startup/copykitten)
  - **ShotCaller** (bedrijf januari 2026, app aangemaakt juli 2025): $819 per maand, 71 abonnementen. Directory: "ShotCaller Bot", 343 servers, zonder betaalvlag (verkoopt via Stripe buiten Discord). [trustmrr](https://trustmrr.com/startup/shotcaller)
  - OneBump ($684 per maand) telt niet mee: het bedrijf is van 2025, maar de app is in oktober 2022 aangemaakt en zit op 37.900 servers.
- Rekenvoorbeeld (GOK, op drie gevallen): ShotCaller haalt ±$2,40 per server per maand, BabelBot ±$0,40, CopyKitten ±$0,04. Voor €350 (±$400) per maand heb je dan ruwweg 170 tot 10.000 servers nodig. Van de nieuwe apps haalt ±15% de 100 en ±2% de 1.000 binnen 3 tot 6 maanden. Het verschil per server is enorm: een nichebot waar beheerders echt voor betalen verdient veel meer per server dan een brede gratis bot met een betaald extraatje.
- DERDEN: afdracht 15% over de eerste $1 miljoen per team sinds 6 juni 2024, daarna 30%, plus betaalkosten. Uitbetaling via Stripe, eerste keer na $100 met een handmatige controle, binnen 45 dagen na de maand. [Discord](https://support-dev.discord.com/hc/en-us/articles/17299902720919)
- DERDEN: makers in de VS, het VK en de EU (Nederland kan), app geverifieerd en van een team, eigenaar 18+, 2FA, voorwaarden en privacybeleid. [Discord](https://support-dev.discord.com/hc/en-us/articles/17297949965079). Wie elders verkoopt, moet het ook via Discord aanbieden voor hooguit dezelfde prijs. [Discord](https://support-dev.discord.com/hc/en-us/articles/23810643331735)
- Geen cijfer van Discord zelf over wat makers samen verdienen gevonden.

**Drukte (GEZIEN)**
- Nieuwe apps in de directory, naar aanmaakmaand: januari 2026 328, april 396, juli 547, oktober 587. Ongeveer 1,8 keer zo veel als begin dit jaar. Per jaar: 2.748 (2024), 3.686 (2025), 4.821 (2026 tot nu).
- Op discordbotlist.com kwamen in oktober 2026 539 bots bij, in januari 160.

**Vindbaarheid**
- App Directory (zoeken en categorieën), botlijsten zoals top.gg en discordbotlist.com, en beheerders die elkaar bots aanraden. De meting laat zien dat bots die ook op een botlijst staan een veel hoger mediaan halen (±100 tegen 14 tot 18).
- DERDEN: sinds 6 nov 2026 geldt voor bijzondere rechten (privileged intents) een grens van 10.000 gebruikers in plaats van 100 servers, met een jaarlijkse herkeuring. [Discord](https://support-dev.discord.com/hc/en-us/articles/40281523410967)

**Past het bij ons**
- Een bot in 1 tot 2 weken: ja (GOK). Maar een bot moet altijd draaien: een server, dus kosten (geld, dus Thijs vragen) en toezicht. Verificatie en uitbetaling onder de naam van Thijs.

## Toets aan de grens die we vooraf vastlegden
1. **Bereik: mediaan minstens 100 servers na 3 tot 6 maanden.** Niet gehaald: 14 in de directory (2.089 apps). Alleen bij bots die ook op discordbotlist.com staan komt het rond de 100, en dat is een selectie van actieve makers.
2. **Geld: minstens 2 bots jonger dan 2 jaar met een eigen cijfer boven $300 per maand.** Gehaald: BabelBot, ShotCaller en CopyKitten, geverifieerd via de betaalprovider.

De afspraak was: alleen ja als beide kloppen. Daarom nee voor nu.

## Voor
- Geverifieerd geld bij kleine, jonge makers, waaronder een Nederlander die via Polar verkoopt (Polar gebruiken wij al voor Olaf).
- Betalen zit in Discord zelf, 15% afdracht, en 14% van de nieuwe apps gebruikt het al.
- Open API's: het bereik is elke week opnieuw te meten.
- ShotCaller laat zien dat het met weinig servers kan: 343 servers, $819 per maand. Een betaalde nichebot hoeft niet groot te worden.

## Tegen
- Gewone nieuwe apps blijven klein: mediaan 14 servers na 3 tot 6 maanden.
- Je hebt veel servers nodig, tenzij de bot iets doet waar beheerders flink voor betalen (ruwweg 170 tot 10.000 voor €350 per maand).
- Steeds drukker: bijna twee keer zo veel nieuwe apps per maand als in januari.
- Een bot moet altijd online zijn: hostingkosten en onderhoud, anders dan een plugin.

## Eerste idee (als het ooit ja wordt)
Een betaalde bot voor één duidelijke taak waar beheerders voor betalen, zoals BabelBot met vertalen, meteen op de directory en de grote botlijsten, met een eigen site die zich vergelijkt met de grote bots. Nog niet gemeten welke taak.

## Wat dit zou veranderen
- Een steekproef op top.gg (als die ooit leesbaar wordt) die laat zien dat nieuwe bots daar wel een mediaan van 100+ halen.
- Een herhaalmeting over 4 weken met dezelfde scripts: als de apps van mei tot aug 2026 dan sneller groeien dan nu te zien is.

## Nakijken
Op 6 nov 2026 (run 21:31) door de controleur nagekeken: akkoord met zeven correcties, alle verwerkt. Hij rekende de tabel, de winkelcijfers en de TrustMRR-bedragen na, controleerde BabelBot en CopyKitten live, en vond ShotCaller in de directory (343 servers). Oordeel nee voor nu, cijfer 5, blijft staan.
