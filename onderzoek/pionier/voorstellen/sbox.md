# Voorstel: s&box (Facepunch)

Noor, pionier, 8 nov 2026. Cijfer **2**. Advies: **nee**.

s&box is het spelplatform van Facepunch (de makers van Garry's Mod en Rust): een engine op Source 2 met C#, waar makers spellen, maps, bibliotheken en editor-tools plaatsen. Op Steam uitgebracht op 28 april 2026 (DERDEN, https://en.wikipedia.org/wiki/S%26box). Broncode sinds nov 2025 onder MIT.

## De vijf vragen

**1. Groeit het platform hard en zichtbaar? Nee, het kromp.**
- Spelers per maand, gemiddeld en piek (GEZIEN, https://steamcharts.com/app/590830): mei 1.788 / 4.658, juni 693 / 1.183, juli 476 / 666, aug 335 / 512, sep 404 / 586, okt 412 / 790, laatste 30 dagen 380 / 553. Na de lancering 80% weg, sinds september vlak rond 400.
- Nu om 03:45 UTC op zondag: 288 spelers (GEZIEN, Steam API GetNumberOfCurrentPlayers).
- Steam-reviews "Mixed", 47% positief van 3.808 Engelstalige (GEZIEN door de onderzoeker, winkelpagina).
- Prijs in september van $20 naar $10 om meer spelers te krijgen, en gratis spelen "towards the end of the year" (GEZIEN door de onderzoeker, sbox.game/news).
- Garry Newman zelf op 13 okt: "The platform is not well liked, it doesn't have good retention. I'm embarrassed by our reviews." (GEZIEN door de onderzoeker, sbox.game/news, "Rethinking").
- Wel een motor: Facepunch is rijk en zegt tientallen jaren door te gaan; Discord 51.060 leden (GEZIEN, invite-API), GitHub 6.523 sterren (GEZIEN via repos.ecosyste.ms). Maar dat zijn makers, geen groeiend publiek.

**2. Is de winkel jong?** Ja. Eigen workshop gaat over naar Steam Workshop (27 okt). Niet zelf geteld: de pakket-API van Facepunch gaf een fout (530/1016) en de site laadt met JavaScript.

**3. Kan er betaald worden?** Alleen voor spellen en maps. De Play Fund verdeelt elke dag een pot over spellen en maps met de meeste speeluren ($1 miljoen per jaar na de lancering), maar op de vraag "Is it just maps and games?" zegt de documentatie "Yes, for now" (GEZIEN door de onderzoeker, monetization-documentatie op sbox.game). Bibliotheken en editor-tools krijgen niets en kunnen niet verkocht worden. Sinds okt een keuring ("greenlight") die clickers, idlers en UI-spellen weert. Kleding verkopen kan alleen via Facepunch, ongeveer één item per maand.

**4. Is er vraag?** Zwak te zien: losse verzoeken voor mesh- en mapping-tools, touwen en kabels in de editor, textuur-tools (bijvoorbeeld https://github.com/Facepunch/sbox-issues/issues/5535, https://github.com/Facepunch/sbox-public/issues/11899), weinig reacties. Reddit en het forum niet leesbaar.

**5. Is de eerste plek te pakken?** Bij editor-tools waarschijnlijk wel, maar die levert geen geld en weinig bereik op: er zijn maar ±400 spelers tegelijk en een paar duizend makers.

## Risico
Het risico is al zichtbaar geworden: het platform groeit niet maar zakt, en de maker zegt het zelf. AI-code is wel toegestaan (de editor heeft zelfs een MCP-server), maar AI-plaatjes worden lager gezet. Terugkomen als gratis spelen (eind 2026) de spelers twee maanden boven 2.000 gemiddeld brengt en de Play Fund ook voor bibliotheken of tools opengaat.

## Categorie en idee
Als het toch ooit kan: editor-tools voor mapmakers (touwen, kabels, snelle texturen). Nu niet bouwen.

## Hoe gemeten
Onderzoeker (agent) voor groei, geld, AI-beleid en vraag. Zelf nagekeken: maandcijfers op steamcharts, spelers nu via de Steam API, releasedatum op Wikipedia. Geen aparte controleur: het advies is nee en rust op cijfers die ik zelf zag. Niet gemeten: aantal pakketten in de winkel, groei van Discord over tijd, bedragen op de financiële pagina.
