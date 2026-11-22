# Meta-brillen (Ray-Ban Meta, Oakley Meta, Meta Ray-Ban Display), apps via de Wearables Device Access Toolkit

Onderzocht 8 nov 2026 door Noor (pionier). Onderzoeker: één agent (groei, stand van de toolkit, geld, vraag, wie er bouwt). Zelf nagekeken: de FAQ van Meta (indienen nog niet open) en de community-catalogus glassapps.io (39 apps). Herhaalscript `data/meta-brillen-meet.py` (eerste regel in `data/meta-brillen.csv`). Controleur (agent) keek de cijfers na en ving een fout: de categorie recepten die ik eerst koos, is op Connect 2026 al ingenomen door NYT Cooking met Meta erachter. Verwerkt; cijfer 5 naar 4.

**Cijfer: 4. Advies: nog niet klaar (volgen).** Dit is de meest pionierachtige kans tot nu toe qua timing: een groot en groeiend apparaat (±9 miljoen brillen) waarvan de app-plekken nog dicht zijn en waar nu alleen hobbyisten bouwen. Maar er is geen datum om uit te brengen, geen betaalroute van Meta zelf, en de vindplekken worden gecureerd door Meta. Bovendien pakt Meta de duidelijke categorieën zelf of met grote merken (vertalen, teleprompter, en recepten via NYT Cooking). Zodra Meta de inzendingen opent, opnieuw wegen met een andere categorie; dan kan dit een 6 worden.

## De vijf vragen

**1. Groeit het platform hard? Ja, maar de groei vlakt af.**
- ±2 miljoen Ray-Ban Meta tot februari 2025; meer dan 7 miljoen in 2025 alleen, ruim drie keer zoveel als 2024; samen ±9 miljoen begin 2026, nu meer (DERDEN, https://uploadvr.com/meta-essilorluxottica-sold-7-million-smart-glasses-in-2025/).
- Q2 2026 omzet uit de brillen bijna verdubbeld (DERDEN, https://www.visionmonday.com/eyecare/article/ai-smart-glasses-and-myopia-management-portfolio-drive-q2-and-first-half-revenue-growth-for-essilorluxottica/); Q3 2026 wearables €486 mln, +20% op jaarbasis, inclusief Nuance Audio (DERDEN, https://www.channelnews.com.au/ray-ban-meta-smart-glasses-boost-essilorluxottica-sales/). Groei gaat dus van ×3 naar +20%.
- Ray-Ban Display ($799): uitrol buiten de VS in jan 2026 uitgesteld door vraag (DERDEN, https://www.engadget.com/social-media/meta-has-delayed-the-international-rollout-of-its-display-glasses-120056833.html); sinds sept 2026 online en in CA, VK, FR, IT, DE (DERDEN, https://roadtovr.com/meta-ray-ban-display-int-launch-connect-2026/). Aantallen Display niet bekend.
- Motor: Meta investeert miljarden per jaar in Reality Labs; Google en Samsung komen ook met brillen (zie `android-xr.md`). Dit apparaat verdwijnt niet snel (GOK).

**2. Is de winkel jong of gaat hij net open? Hij gaat open, datum onbekend.**
- Toolkit preview sinds 4 dec 2025, alleen camera en audio, niet uitbrengen (DERDEN, https://www.uploadvr.com/meta-wearables-device-access-toolkit-public-preview/). Sinds 14 mei 2026 kan de Display beeld tonen, via een telefoonapp of via web apps in HTML/JS (600×600) (DERDEN, https://vr.org/articles/meta-ray-ban-display-developer-sdk-2026). Versie 1.0 vanaf 30 sept 2026 (DERDEN via agent, https://developers.meta.com/wearables/faq/).
- "Can people discover what I build? Soon, yes." Twee plekken komen: een selectie op de Display zelf en een gecureerde lijst in de Meta AI-app. "We'll have more to share on submission and publishing timing soon." (GEZIEN, https://developers.meta.com/wearables/faq/, 8 nov 2026).
- Nu alleen verspreiding via een privé bètakanaal per app of een web-app-URL, met ontwikkelaarsmodus aan (DERDEN via agent, documentatie op https://wearables.developer.meta.com/llms.txt).
- Community-catalogus glassapps.io: 39 apps, ongeveer de helft spelletjes (GEZIEN, https://glassapps.io). Vroege partners: Twitch, Streamlabs, Microsoft Seeing AI, Disney, 18Birdies (DERDEN, UploadVR).

**3. Kan er betaald worden? Alleen via je eigen telefoonapp, en dat is niet bevestigd.**
- Geen betaalde laag of winkel van Meta; de voorwaarden noemen geen betalingen (DERDEN via agent, https://wearables.developer.meta.com/terms). Verboden: data van de bril verkopen, surveillance, gezichts- en stemherkenning (behalve toegankelijkheid met toestemming) (DERDEN, https://wearables.developer.meta.com/acceptable-use-policy).
- Een toolkit-app is een gewone iOS- of Android-app; daar kan een abonnement of aankoop via App Store of Google Play in (GOK: geen verbod gezien, ook geen expliciete toestemming). Web apps hebben geen betaalroute.
- Dus: wel een weg naar geld (gewone app-winkels), geen plan van Meta zelf. Volgens de rol net genoeg om geen nee te zijn.

**4. Is er vraag? Ja, maar weinig gemeten.**
- Reviewers: "weinig apps, alles van Meta"; gemist: recepten tijdens het koken, video, betere kaarten (DERDEN, https://www.engadget.com/2173297/meta-is-bringing-third-party-apps-and-games-to-its-display-glasses/, https://www.tomsguide.com/au/computing/smart-glasses/meta-ray-ban-display-hands-on-this-is-the-future).
- Forumdraad "needs YouTube and streaming apps" (DERDEN, alleen titel, https://communityforums.atmeta.com/discussions/ai-tips-tricks/meta-ray-ban-display-needs-youtube-and-streaming-apps-like-netflix-hbo-etc/1354446).
- Meta noemt zelf als gewenst: sport en inspectie vastleggen, toegankelijkheid, vertalen, coaching, werkprocessen (DERDEN via agent, acceptable-use-gids).
- Reddit gaf 403; echte tellingen van verzoeken ontbreken.

**5. Is de eerste plek te pakken? Ja, buiten wat Meta zelf doet.**
- Bezet door Meta of sterke partijen: vertalen, ondertitels, teleprompter (ingebouwd), toegankelijkheid (Be My Eyes, Seeing AI), streamen (Twitch, Instagram), en **recepten**: NYT Cooking aangekondigd op Connect 2026, een handsfree kookmodus met elke stap als kaart op de Display (DERDEN via controleur, https://www.remio.ai/post/nyt-cooking-on-meta-glasses-turns-a-failed-demo-into-a-real-kitchen-test en https://www.meta.com/ai-glasses/food-and-cooking-tips/).
- Open, alleen hobbyisten: sport-HUD op de Display (Ghost Run, GymRep, een tennisteller), klus- en werkchecklists (DisplayList bestaat al), navigatie (DamamMap) (DERDEN via agent, glassapps.io en UploadVR).
- Categorie waar wij nummer één kunnen worden: nog niet hard te kiezen. Beste kandidaten: **handsfree checklists en werkinstructies** (inspectie, klussen, onderhoud; Meta noemt dit zelf) of een **sport-HUD** voor de gym (sets, herhalingen, rust). In beide alleen hobbyisten, maar ook kleiner dan recepten. Waarom wij: het werkt als web app (snel te bouwen) en past bij wat Meta wil promoten.

## Risico
- Meta kan de vindplekken klein en gecureerd houden: dan bepaalt Meta wie bereik krijgt, en een klein bedrijf komt er misschien niet in.
- Meta bouwt de beste categorieën zelf of haalt grote merken binnen (vertalen, teleprompter, en recepten met NYT Cooking). Dat gebeurt al, niet pas later.
- De Display (het scherm waar onze app op leunt) is een klein deel van de ±9 miljoen; de rest heeft geen scherm, dan blijft alleen audio en camera.
- Tekenen dat het stokt: indienen blijft tot maart 2027 dicht, of de Q4- en Q1-cijfers van EssilorLuxottica tonen geen groei meer. Teken dat het doorbreekt: Meta opent inzendingen met datum en een open lijst, of meldt Display-aantallen boven 500.000.

## Eerste productidee
"Stap voor stap" voor werk en klussen op de Ray-Ban Display: plak een checklist of werkinstructie, de app toont één stap tegelijk, afvinken met spraak of de Neural Band, later met een foto als bewijs per stap (camera via de toolkit). Eerst als web app, later als toolkit-app met een betaalde laag in de telefoon-app (lijsten delen met een team, rapport als PDF). Recepten bewust niet: daar staat NYT Cooking. Opmerking: Dortus kan de Display niet zelf testen zonder bril; er is een simulator in de toolkit (GOK, nakijken).

## Wat ik niet kon meten
Aantal Display-brillen, verkoop in stuks in 2026, gebruik van apps, hoe de gecureerde lijst gaat werken, Reddit. Herhaalmeting: `python3 data/meta-brillen-meet.py` elke paar weken; het script meldt zodra de FAQ niet meer "soon" zegt.

## Advies
Nog niet klaar (4). Volgen, niet nu bouwen. Wordt een ja (6) als Meta inzendingen opent met een datum en de lijst niet alleen voor grote partners is. Dan is een account in het Wearables Developer Center nodig (stap voor Thijs, nu nog niet op zijn lijst gezet omdat Hans eerst moet beslissen).
