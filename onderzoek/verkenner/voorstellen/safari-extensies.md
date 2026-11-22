# Safari-extensies in de App Store (iPhone, iPad, Mac)

Vera, 9 nov 2026 run 15:31 (Amsterdam). Advies: **nee. Cijfer 3.**

## Wat het is
Een Safari-extensie wordt verkocht als app in de App Store, gratis, betaald of met abonnement. Sinds iOS 15 (2021) werken ze ook op de iPhone, en de App Store heeft een eigen categorie. Waarom ik keek: Apple neemt de kassa voor zijn rekening, en sinds sep 2025 kun je een web-extensie als zip uploaden in App Store Connect, zonder Mac of Xcode. Dat past bij onze opzet.

## Eigen meting (GEZIEN)
- Bron: de open iTunes Search API (ratings per land, prijs, releasedatum). 42 zoektermen ("safari extension", "for safari", "safari dark mode", "safari ad blocker" enzovoort) in de winkels van de VS en het VK, voor iPhone en Mac apart, alleen apps waarvan de beschrijving "Safari" en "extension" noemt. Gevonden: 538 iPhone-apps en 694 Mac-apps (daarin ook Safari zelf, Brave, LastPass en Airmail; voor de nieuwe-blokcijfers maakt dat niets uit). Universele apps krijgen op iPhone en Mac vaak hetzelfde aantal ratings, dus het zijn geen twee losse metingen. Apps zonder US-rating tellen als 0 (21 op iPhone, 15 op Mac); de mediaan verandert daar niet door.
- **Beperking:** de API geeft per zoekterm hoogstens 200 resultaten, en mijn filter ("Safari" en "extension" in de beschrijving) mist contentblockers die het woord extension niet gebruiken: AdBlock Pro (74.512 ratings), AdGuard for Safari (20.354), wBlock (okt 2025, 189) en uBlock Origin Lite (aug 2025, 990) ontbreken (controleur). Het beeld kan dus ook te somber zijn. Een volledige lijst van de categorie kon ik niet lezen.
- **Nieuwe extensies (nov 2025 tot en met aug 2026), ratings in de VS:**
  - iPhone: 142 apps. Mediaan **1** rating. 10 met 10 of meer (7%), 2 met 50 of meer. Betaald (vooraf): 48, waarvan 1 echte Safari-extensie met 10 of meer ratings.
  - Mac: 172 apps. Mediaan **0**. 2 echte extensies met 10 of meer (1%), geen met 50 of meer (Skyscraper Social en CastReader zijn apps met een extensie erbij). Betaald: 63, geen enkele met 10 of meer.
  - Beste nieuwe: V-Shield (267, gratis), ScrollGuard (127, gratis), Cookie Editor (41). De beste betaalde: een blocker voor YouTube, FB en LinkedIn van $1,99 met 11 ratings. Tegenvoorbeeld net buiten het venster: wBlock (okt 2025) haalde in een jaar 189 ratings, dus bereik is niet onmogelijk, wel zeldzaam.
- **Drukte groeit:** gevonden nieuwe per maand (iPhone plus Mac) van ±10 tot 15 begin 2025 naar ±40 tot 50 in aug tot okt 2026. Dat valt samen met de zip-route van Apple (sep 2025). GOK dat de echte aantallen hoger zijn, want de zoek-API toont niet alles.
- Hoeveel downloads bij een rating horen weet ik niet zeker; vaak genoemd is 1 rating op 50 tot 100 downloads (GOK). Dan haalt ±7% van de nieuwe iPhone-extensies ruwweg 500 tot 1.000 downloads in de VS, en verdient bijna niemand er vooraf aan.

## Bronnen (onderzoeker)
- Jeff Johnson (StopTheMadness): zijn Safari-extensie levert meer dan 93% van zijn App Store-omzet, maar pas na iOS 15 (2021) en na vijf jaar zonder succes; hij noemt het zelf survivorship bias (GEZIEN, lapcatsoftware.com/articles/2026/8/3.html).
- Een Safari-adblocker uit 2026: $59 per maand met 5 klanten, verkocht voor $1.000 (GEZIEN, microns.io/startup-listings/safari-ad-blocker-app).
- Voor Noir, Hush en Wipr geen openbare omzet gevonden.
- De categorie in de App Store zit "nogal verstopt" (DERDEN, tidbits.com 2021).
- Kosten: Apple Developer Program $99 per jaar, als particulier zonder KvK mogelijk (GEZIEN, developer.apple.com/programs/enroll). Small Business Program: 15% commissie (GEZIEN).
- **EU-regel (DSA):** wie als handelaar verkoopt, krijgt adres, telefoon en e-mail openbaar op de App Store-pagina (GEZIEN, developer.apple.com/help/app-store-connect/.../trader-requirements). Wie geld verdient is in de praktijk handelaar. Voor Thijs betekent dat zijn adres openbaar, tenzij hij een zakelijk adres regelt.
- Bouwen: zip uploaden via de Safari Web Extension Packager in App Store Connect, Apple bouwt iPhone- en Mac-app, testen via TestFlight (GEZIEN, developer.apple.com/tutorials/.../packaging-and-distributing-safari-web-extensions-with-app-store-connect). Op het Apple-forum melden makers dat de packager soms ontbreekt of het exporteren mislukt (DERDEN, alleen titels).

## Scores op "Wat een 8 is"
1. Nieuwe kleine makers verdienen: **nee**. Mediaan 1 rating, betaalde nieuwe extensies vrijwel zonder ratings, geen nieuwe maker met openbare omzet gevonden.
2. Bereik voor nieuwkomers: **zwak**. ±7% op iPhone haalt 10 of meer ratings, op Mac 1%.
3. Bouwen en testen: **ja**, sterk, sinds de zip-route (geen Mac nodig; anders een macOS-runner op GitHub Actions).
4. Thijs kan binnen een week verkopen: **redelijk**. $99, account als particulier, maar zijn adres en telefoon komen openbaar onder de DSA.

## Voor en nadelen
- Voor: Apple regelt kassa en btw, 15% commissie, weinig bouwdrempel, extensies kunnen we ook voor Chrome en Firefox gebruiken (één code).
- Tegen: weinig vraag naar nieuwe extensies, gratis concurrenten in elke hoek (adblockers, donkere modus, video), drukte stijgt door de zip-route, adres van Thijs openbaar.

## Wat we er zouden bouwen
Alleen als bijvangst: een extensie die we toch al voor Chrome of Firefox maken, ook als Safari-versie uitbrengen via de zip-route. Niet als eigen platform.

## Cijfer en advies
**3, nee.** Bouwen kan makkelijk, maar nieuwe extensies krijgen weinig gebruikers en betaalde bijna geen. Nagekeken door de controleur: akkoord, 6 correcties verwerkt (filter mist contentblockers, twee apps zijn geen echte extensie, cijfers daardoor iets lager). Opnieuw kijken als Apple de categorie beter toont (bijvoorbeeld een eigen tabblad of lijsten met nieuwe extensies).

Data: `data/safari-extensies-ios-2026-11-09.json`, `data/safari-extensies-mac-2026-11-09.json`, script `data/safari-extensies-haal.py` (argumenten: software of macSoftware, landen, uitvoerbestand).
