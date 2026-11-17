# Groep D: Apple, apparaten en Android (17 nov 2026)

Alle bronnen zelf gelezen met curl op 17 nov 2026. Hoofdbron Apple: https://developer.apple.com/news/ (de lijst met berichten, met datum per bericht).

Belangrijke vaststelling vooraf: de meeste Apple-tips BESTAAN, maar de data in de tips kloppen vaak niet. Op 15 en 16 nov 2026 staat op developer.apple.com/news maar één bericht (16 nov: strengere regels voor Full Disk Access en Device Control op macOS 27.3 bèta 2). De andere dingen zijn ouder (juni tot begin november).

Harde beperking voor alles van Apple: Dortus heeft geen Mac. Een iOS- of Mac-app bouwen en indienen gaat officieel via Xcode op een Mac. Er bestaan omwegen (cloud-Mac huren, Flutter of React Native met een cloud-bouwdienst), maar dat is GOK qua tempo en kost geld. Daarbij komt: apps zonder "trader status" zijn uit de EU-App Store gehaald (GEZIEN op developer.apple.com/news, bericht "New requirement for apps on the App Store in the European Union"). Wie als handelaar verkoopt, moet adres en telefoon opgeven en Apple toont die openbaar op de winkelpagina (dat laatste weet ik uit de regels van 2024 en 2025, vandaag niet opnieuw gecontroleerd, dus GOK dat het nog zo is). Dat botst met de privacy van Thijs zolang er geen bedrijfsadres is.

---

### 1a. iPhone Duo (opvouwbare iPhone), Xcode 27.1 Device Hub
- Bestaat: JA. "Prepare and submit your apps for iPhone Duo", 5 okt 2026, https://developer.apple.com/news/ . Te koop sinds 23 okt 2026 (https://www.apple.com/newsroom/2026/10/developers-bring-incredible-new-app-experiences-to-iphone-duo/ , 22 okt 2026). Device Hub in Xcode 27.1 bestaat echt (simulator die vouwt en draait).
- Het getal "verdubbeld naar 200.000 in één week": NIET GEVONDEN. Wat wel bestaat: Apple zei op 6 nov 2026 "well over 100,000 apps built for iPhone Duo", met duizenden erbij per dag (https://www.macrumors.com/2026/11/06/apple-says-100k-apps-optimized-for-iphone-duo/). 200.000 is dus verzonnen of een eigen rekensom van Google.
- Wat het echt is: de eerste vouw-iPhone ($1.999) met een groot binnenscherm en nieuwe standen; apps met standaard SwiftUI/UIKit passen zich grotendeels vanzelf aan. Er is een badge "Made for iPhone Duo" en Apple maakt eigen lijstjes in de App Store.
- Wet 1: nee. Het toestel is ruim 3 weken uit en er staan al meer dan 100.000 aangepaste apps; zonder Mac halen we 7 dagen niet.
- Wet 2: nee. "Een app geschikt maken voor een vouwscherm" is werk voor elke bestaande app zelf, geen nieuwe basistaak.
- Wet 3: ja. App Store heeft kassa en betaalcultuur.
- Wet 4: nee. Apple doet het meeste aanpassen al automatisch via SwiftUI/UIKit.
- Vraag 5: ja, er zijn redactielijstjes en een badge, maar die gaan naar grote namen.
- Mogelijk product: geen.
- Cijfer: 2. Te laat, te druk, en we hebben geen Mac.

### 1b. Touch on Mac (MacBook Pro met aanraakscherm)
- Bestaat: JA. "Say hello to Touch on Mac", 28 okt 2026, https://developer.apple.com/news/ en persbericht 28 okt 2026 https://www.apple.com/newsroom/2026/10/apple-unveils-groundbreaking-macbook-pro-with-proled-xdr-display/ . Te koop sinds 6 nov 2026. Ontwikkelaarspagina: https://developer.apple.com/touch-on-mac/
- Wat het echt is: de nieuwe MacBook Pro (M5 Pro/Max, OLED) kan voor het eerst met aanraking bediend worden, plus Dynamic Island op de Mac. Ontwikkelaars passen bestaande Mac-apps aan met gewone gebaarherkenners.
- Wet 1: deels. Twee weken oud, maar alleen voor de duurste MacBook Pro; kleine groep.
- Wet 2: onbekend. Een "touch-laag voor apps die het niet ondersteunen" zou breed zijn, maar macOS laat zo diep ingrijpen steeds minder toe (zie de nieuwe beperkingen op Device Control van 16 nov 2026).
- Wet 3: ja, Mac App Store en eigen verkoop met Developer ID.
- Wet 4: nee. Apple bouwt touch in macOS zelf; standaard bedieningselementen werken vanzelf.
- Vraag 5: deels, Mac App Store heeft weinig bereik vergeleken met iOS.
- Mogelijk product: geen. Zonder Mac kunnen we niet eens testen.
- Cijfer: 2. Kleine doelgroep en Apple doet het zelf.

### 1c. App Store Bundles & Suites
- Bestaat: JA. "Get your subscriptions ready for iOS 27", 16 sep 2026, https://developer.apple.com/news/ en https://developer.apple.com/app-store/subscriptions/bundles-and-suites/
- Wat het echt is: meerdere abonnementen samen verkopen in één aankoop (Bundle, tot 5 abonnementen, ook samen met andere makers, tot 5 makers) of één abonnement over tot 15 eigen apps (Suite). Alleen op aanvraag via een formulier; Apple zet het in batches live.
- Wet 1: nee. Aangekondigd in september, op aanvraag, en je moet eerst zelf abonnement-apps hebben.
- Wet 2: nee. Het is een verkoopvorm, geen product.
- Wet 3: ja, maar alleen voor wie al abonnementen verkoopt.
- Wet 4: nee, Apple levert het zelf.
- Vraag 5: ja, de App Store toont alle apps van de bundel bij aankoop.
- Mogelijk product: geen. Pas nuttig als Dortus later meerdere iOS-apps met abonnement heeft.
- Cijfer: 1. Geen kans, wel een handige feit voor later.

### 1d. Group Purchases (meerdere plekken voor een abonnement)
- Bestaat: JA. 16 sep 2026 en 22 okt 2026 op https://developer.apple.com/news/ . Volume Purchasing (voor bedrijven en scholen) live sinds 22 okt 2026. Group Purchases: testen in Sandbox vanaf november 2026, live in de App Store "this winter".
- Wat het echt is: iemand koopt meerdere plekken van een abonnement en nodigt anderen uit; Apple regelt de uitnodigingen. Staat standaard aan in App Store Connect.
- Wet 1: nee. Nog niet live, en het is een functie van bestaande abonnement-apps.
- Wet 2: nee. Verkoopvorm, geen product.
- Wet 3: ja, binnen de App Store.
- Wet 4: nee, Apple doet het zelf.
- Vraag 5: onbekend.
- Mogelijk product: geen.
- Cijfer: 1.

### 1e. Eerste Apple Developer Center in Europa
- Bestaat: JA, maar niet van nov 2026. "Apple Developer Centers are expanding to Berlin", 3 juni 2026, https://developer.apple.com/news/ . "Later this year" opent een vijfde centrum in Berlijn.
- Wat het echt is: een gebouw met workshops en afspraken met Apple-mensen. Geen platform, geen winkel.
- Wet 1 tot 4 en vraag 5: niet van toepassing, het is geen markt.
- Mogelijk product: geen.
- Cijfer: 0. Nieuws, geen kans.

### 2a. Apple HomeView ($299, 13 nov 2026)
- Bestaat: JA. "Apple HomeView available today", 13 nov 2026, https://www.apple.com/newsroom/2026/11/apple-homeview-available-today/ . Prijs $299 staat in het bericht. "Select regions", Siri AI daarop is bèta.
- Wat het echt is: een scherm van 7 inch voor thuis (tafel of muur) met Siri AI, FaceTime, Muziek en de Woning-app. Er is GEEN eigen App Store: ongeveer 14 vaste Apple-apps, en apps van anderen komen alleen via de iPhone binnen (CarPlay-audio/video-apps en iPhone-widgets) (https://www.macworld.com/article/3261804/ ; licentie-afspraak 13 okt 2026 op developer.apple.com/news noemt "iOS app widgets on Apple HomeView" en "iOS apps for CarPlay on Apple HomeView").
- Wet 1: ja qua tijd, 4 dagen oud.
- Wet 2: deels. Een widget die op HomeView mooi staat (bijv. gezinsagenda, boodschappen) is breed, maar het blijft een iPhone-app met widget.
- Wet 3: ja via de iPhone-app in de App Store, maar dat is gewone iOS-concurrentie.
- Wet 4: nee. Apple levert zelf Agenda, Herinneringen, Woning en foto's op HomeView, juist de brede basistaken.
- Vraag 5: nee. Geen eigen winkel op het apparaat, dus geen etalage "voor HomeView".
- Mogelijk product: geen. Zonder eigen winkel en zonder Mac is er geen route.
- Cijfer: 2. Echt nieuw, maar dicht platform zonder winkel.

### 2b. Siri AI open voor alle ontwikkelaars (iOS/macOS 27.3 bèta)
- Bestaat: JA. "Siri AI is now open to all developers", 3 nov 2026, https://developer.apple.com/news/
- Wat het echt is: met App Intents kan elke app acties en inhoud aan Siri AI geven, plus "skills" om meerdere acties te koppelen. Het is een Developer Preview; indienen bij de App Store opent pas "in the spring" (voorjaar 2027).
- Wet 1: nee. Indienen kan pas in het voorjaar, en Siri AI is "currently unavailable in the EU in iOS, iPadOS, and watchOS" (zelfde bericht). Op macOS wel, maar wij hebben geen Mac.
- Wet 2: deels. Elke app kan meedoen; een losse "Siri-tool" is geen basistaak.
- Wet 3: onbekend. Apple zegt dat de voorwaarden voor Siri AI-gebruik nog volgen.
- Wet 4: nee. Apple bouwt Siri AI zelf in tientallen eigen apps (Agenda, Notities, Bestanden enz.).
- Vraag 5: onbekend; misschien vindt Siri apps "door te vragen", maar dat is GOK.
- Mogelijk product: geen voor nu.
- Cijfer: 2. Interessant voor voorjaar 2027, niet nu, en niet in de EU.

### 3. Apple EU-voorwaarden (commissie, web-checkout, Core Technology Fee weg)
- Bestaat: JA. "Changes for apps in the European Union", 18 aug 2026, ingegaan op 1 okt 2026, https://developer.apple.com/news/ en tarieven op https://developer.apple.com/support/apps-in-the-eu/ . Niet okt tot nov, maar aangekondigd in augustus.
- Wat het echt is: één set regels voor alle EU-makers. App Store met Apple-betaling 26% (15% in het Small Business Program en voor abonnementen na jaar 1); eigen betaling in de app 20% (10%); link naar je eigen webwinkel 15% (10%) over verkopen binnen 7 dagen na de klik; buiten de App Store (web-distributie, andere winkels) 5% Core Technology Commission. De Core Technology Fee per installatie, Initial Acquisition Fee en Store Services Fee zijn geschrapt. De "5 tot 26%" uit de tip klopt dus.
- Wet 1: nee. Het is een prijswijziging, geen nieuw platform; al 7 weken van kracht.
- Wet 2: niet van toepassing.
- Wet 3: ja, het maakt verkopen via de eigen kassa (bijv. Stripe of Polar) goedkoper toegestaan.
- Wet 4: niet van toepassing.
- Vraag 5: niet van toepassing.
- Mogelijk product: geen eigen product. Wel nuttig: als Dortus ooit een iOS-app heeft, is 10% (eigen betaling, Small Business) of 15% (link naar web) de goedkoopste route. Een "web-checkout tool voor EU-iOS-makers" bestaat al bij grote partijen (Stripe, RevenueCat en dergelijke, GOK maar zeer waarschijnlijk).
- Cijfer: 1 als kans, 6 als achtergrondkennis.

### 4a. Samsung Galaxy Glasses
- Bestaat: DEELS. Samsung noemt het "Intelligent Eyewear" (Gentle Monster en Warby Parker), niet verscheept in november: release 10 dec 2026, alleen VS en Zuid-Korea, vanaf $395, voorverkoop sinds 12 nov 2026. Bron: https://news.samsung.com/global/samsung-announces-december-release-for-intelligent-eyewear-bringing-a-smarter-way-to-see-the-world (12 nov 2026).
- SDK of app-winkel: er is GEEN eigen winkel voor de bril. Google Play laat sinds ongeveer eind oktober "augmented experiences on audio glasses" toe, maar zonder eigen release-track: het brilstuk zit in je gewone telefoon-app (APK) op het mobiele spoor. Gewone Android-apps werken vanzelf mee (meldingen worden voorgelezen). Een badge "Differentiated for Glasses" krijg je met een "projected activity"; de bibliotheken zijn deels nog alpha. Bron: https://vr.org/articles/google-play-audio-glasses-phone-track-samsung-mid-december-2026 (2 nov 2026), die de tekst van developer.android.com citeert. De Play-tekst zelf heb ik op developer.android.com niet letterlijk teruggevonden (pagina's laden hun inhoud deels via scripts), dus dit deel is GEZIEN via secundaire bron.
- Wet 1: nee. Release in VS/Korea op 10 dec, geen EU; en Dortus heeft geen Play-ontwikkelaarsaccount (een nieuw persoonlijk Play-account moet bovendien eerst een testperiode met testers doorlopen voor je mag publiceren, GOK dat dit nog geldt, het gold in 2024 en 2025).
- Wet 2: nee. Google en Samsung leveren de basis zelf: Gemini, vertalen, navigatie via Maps, meldingen samenvatten, Samsung Notes.
- Wet 3: deels. Play heeft een kassa, maar een "brilfunctie" verkoop je niet los; die zit in een telefoon-app.
- Wet 4: nee, zie wet 2.
- Vraag 5: nee. Geen eigen etalage voor bril-apps, alleen een badge in Play.
- Mogelijk product: geen.
- Cijfer: 2. Echt apparaat, maar geen winkel, geen EU, geen Play-account.

### 4b. VONDER Smart Glasses
- Bestaat: JA. Van Viture. Voorverkoop sinds 28 sep 2026, vanaf $299, verzending "in november" zonder vaste datum. Geen camera en geen scherm; spraak wordt tekst ("memories") in de VONDER-app, en verzoeken gaan naar Claude, ChatGPT of Gemini. Abonnement $9,99 tot $99 per maand. Bronnen: https://www.androidauthority.com/vonder-smart-glasses-debut-3713717/ en https://www.tomsguide.com/computing/smart-glasses/vonder-may-have-solved-the-pervert-glasses-problem-and-the-nerd-factor-too (geen exacte datum op de pagina gezien, rond sep 2026).
- SDK of app-winkel: NIET GEVONDEN. Geen ontwikkelaarspagina, geen SDK, geen winkel. Tom's Guide noemt alleen een toekomstige bèta om met spraak samen te werken met Claude Code en Codex.
- Wet 1: nee, er is niets om op te bouwen.
- Wet 2 tot 4: niet te beoordelen zonder platform.
- Vraag 5: nee.
- Mogelijk product: geen.
- Cijfer: 1. Gesloten product van één fabrikant.

### 5a. Google Play: target API 36-verplichting en 1 november 2026
- Bestaat: JA, maar anders dan de tip. https://developer.android.com/google/play/requirements/target-sdk (laatst bijgewerkt 28 okt 2026) en https://support.google.com/googleplay/android-developer/answer/11926878 : nieuwe apps en updates moeten Android 16 (API 36) targeten. Bestaande apps moesten API 35 halen vóór 31 aug 2026. 1 november 2026 was de uiterste datum van het uitstel dat je kon aanvragen, niet een nieuwe API 36-plicht.
- Wat het echt is: jaarlijkse regel van Google zodat apps op nieuwe Android-versies veilig werken.
- Wet 1 tot 4 en vraag 5: niet van toepassing. Het is een regel, geen markt. Een "tool die je app op API 36 helpt" doet Android Studio zelf (Upgrade Assistant), en het moment is voorbij.
- Mogelijk product: geen.
- Cijfer: 0.

### 5b. Platform Tools 37 met `adb pair --qr`
- Bestaat: DEELS. https://developer.android.com/tools/releases/platform-tools : versie 37.0.3, "Canary: November 2026", met "Add support for wireless pairing using a QR code in the terminal (the adb pair --qr command)". Het is een Canary (testversie), geen gewone release; de datum 10 nov staat er niet bij.
- Wat het echt is: je telefoon draadloos koppelen aan adb door een QR-code in de terminal te scannen, in plaats van een code over te typen.
- Wet 2: nee, kleine gemakfunctie voor ontwikkelaars.
- Wet 4: nee, Google doet het nu zelf in adb, en Android Studio had dit al in de grafische schil.
- Mogelijk product: geen. Juist het bewijs dat een "QR-koppel-tooltje" geen zin meer heeft.
- Cijfer: 0.

---

## Top 2

Niets haalt een 7.

Als ik toch twee moet noemen, alleen om te volgen, niet om nu te bouwen:
1. Siri AI voor alle ontwikkelaars (2): het enige echt nieuwe, brede platform hier, maar App Store-indiening pas voorjaar 2027, niet beschikbaar op iOS in de EU, en wij hebben geen Mac. Zet een herinnering voor het voorjaar.
2. Apple HomeView (2): 4 dagen oud en echt nieuw, maar zonder eigen app-winkel; apps van anderen komen alleen als iPhone-widget of CarPlay-app binnen, en Apple levert agenda en herinneringen zelf.

Les uit deze groep: de Google-tips over Apple bestaan grotendeels, maar de data en getallen zijn vaak verschoven of verzonnen (200.000 apps bestaat niet, het is ruim 100.000; Berlijn is van juni; de EU-regels van augustus; de Samsung-bril komt in december en alleen in VS/Korea; API 36 op 1 nov was een uitsteldatum). Voor Dortus blijven Apple en Play dicht zolang er geen Mac en geen Play-account is, en EU-verkoop op de App Store vraagt een openbaar adres (trader status).
