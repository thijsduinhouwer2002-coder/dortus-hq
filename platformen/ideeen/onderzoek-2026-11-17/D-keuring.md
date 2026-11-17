# Keuring van groep D (Apple, apparaten, Android), 17 nov 2026

Keurder: zelf opnieuw nagelezen met curl op 17 nov 2026. Vier hoofdbeweringen gecontroleerd, plus een zoektocht naar een gemiste kans.

## Bewering 1: Siri AI. Indienen pas in het voorjaar van 2027, en op iOS niet in de EU
**KLOPT.**
- Bron: https://developer.apple.com/news/ , bericht "Siri AI is now open to all developers", 3 nov 2026. Letterlijk: "This preview provides early access before first shipping to customers in a few months; and with submission to the App Store opening up in the spring". En: "Siri AI is currently unavailable in the EU in iOS, iPadOS, and watchOS."
- macOS en visionOS staan niet in die EU-uitsluiting, dus "op macOS wel" klopt ook.
- Ook waar: de voorwaarden voor Siri AI volgen nog ("we will follow up with more details about the terms and usage policies"). Wet 3 "onbekend" is dus terecht.
- Kanttekening op het oordeel: de EU-blokkade is voor Dortus minder erg dan het stuk zegt. Kopers hoeven niet in de EU te zitten; de App Store is wereldwijd. Het echte probleem is de tijd (indienen pas voorjaar 2027) en dat Apple Siri AI zelf in vijftien eigen apps stopt (Agenda, Herinneringen, Notities, Bestanden enz., zelfde bericht). Wet 1 blijft dus nee, alleen om een andere hoofdreden.

## Bewering 2: Apple HomeView heeft geen eigen app-winkel
**KLOPT, maar er mist iets belangrijks.**
- Geen winkel: https://www.macworld.com/article/3261804/ zegt letterlijk "there's no app store for downloading more", 14 vaste apps. Apps van anderen komen via de iPhone binnen: CarPlay-audio- en video-apps vanzelf, en widgets. De licentie-afspraak van 13 okt 2026 (developer.apple.com/news, "Updated Apple Developer Program License Agreement now available") noemt "iOS app widgets on Apple HomeView and availability of iOS apps for CarPlay on Apple HomeView". Dat bevestigt de route via de iPhone. Macworld is een tweede bron; de lijst van 14 apps heb ik niet bij Apple zelf gezien.
- Gemist: Apple zegt in het persbericht zelf dat HomeView NIET in de EU te koop is. https://www.apple.com/newsroom/2026/11/apple-homeview-available-today/ (13 nov 2026): "Apple HomeView is not available for sale in the European Union, as Siri AI is currently unavailable in iOS in the EU." Te koop in Australië, Canada, India, Nieuw-Zeeland, Singapore, het VK en de VS. Het stuk schrijft alleen "select regions". Thijs kan het apparaat dus niet eens kopen om te testen.
- Prijs $299 en datum 13 nov: niet als bedrag in de platte tekst teruggevonden (het bedrag staat in een los element), datum klopt.

## Bewering 3: "ruim 100.000 iPhone Duo-apps" (6 nov), niet 200.000
**KLOPT.**
- https://www.macrumors.com/2026/11/06/apple-says-100k-apps-optimized-for-iphone-duo/ citeert Apple: "Today there are well over 100,000 apps built for iPhone Duo already live on the App Store, and thousands of optimized apps are being added to the store each day."
- Zoeken op "iPhone Duo 200,000 apps" geeft alleen artikelen over 100.000 (9to5Mac, MacRumors, Gizbot en andere, allemaal 6 nov). Geen bron voor 200.000 gevonden. Het getal uit de tip is verzonnen of een eigen rekensom.
- Datum toestel (te koop 23 okt) klopt: developer.apple.com/news, "Prepare and submit your apps for iPhone Duo", 5 okt 2026. Extra feit: vanaf april 2027 moeten alle nieuwe inzendingen iPhone Duo-schermafbeeldingen hebben (zelfde bericht).

## Bewering 4: Samsung-bril pas op 10 dec, en is er een SDK
**KLOPT, en het SDK-deel is nu bij de primaire bron bevestigd.**
- Datum en landen: https://news.samsung.com/global/samsung-announces-december-release-for-intelligent-eyewear-bringing-a-smarter-way-to-see-the-world (12 nov 2026): "Set for release in the U.S. and South Korea on Dec. 10 with pre-orders beginning today". Warby Parker alleen in de VS vanaf $395, Gentle Monster in VS en Korea, $449 tot $489. Geen EU.
- SDK: ja. https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/first-activity : je breidt je bestaande telefoon-app uit met een "projected activity"; de bril draait geen eigen APK. De bibliotheken zijn alpha (bijv. androidx.xr.projected 1.0.0-alpha14, glimmer 1.0.0-alpha22). De onderzoeker kon dit niet direct lezen; het klopt.
- Niet zelf nagekeken: dat Play geen eigen release-track voor de bril heeft (alleen via vr.org, 2 nov 2026). Blijft GEZIEN via secundaire bron.
- Extra feiten uit het Samsung-bericht: de bril werkt ook met iPhone 13 en nieuwer, en vraagt leeftijdscontrole (18+) voor activeren en app-downloads.
- Kleine fout in het stuk: bij wet 2 staat als reden "Google en Samsung leveren de basis zelf". Dat is een wet 4-reden. Uitkomst blijft hetzelfde.

## Overige punten
- Trader status: het stuk zegt dat dit botst met de privacy van Thijs. Dat geldt alleen voor de EU-winkel. Buiten de EU kan een app zonder trader-gegevens wel in de App Store staan (GOK op basis van de regels van 2024 en 2025, vandaag niet opnieuw nagekeken). Voor HomeView en Siri AI, die toch niet in de EU werken, is dit dus geen extra blokkade.
- "Geen Mac": er bestaan clouddiensten die iOS-apps vanaf Windows bouwen en indienen (bijv. Expo EAS, Codemagic). Dat is geen gok dat ze bestaan, wel een gok hoe snel en goed het gaat met widgets en App Intents. Het maakt "geen Mac" een rem, geen muur. Het verandert de cijfers hieronder niet, want die vallen al op wet 1, 4 en vraag 5.

## Eens met de cijfers?
Ja, op één na. Alle Apple- en apparaat-tips vallen terecht op wet 1, wet 4 of vraag 5.
- Siri AI: 2 wordt bij mij 3, alleen als agendapunt. Indienen in het voorjaar van 2027 is precies het soort "platform gaat open"-moment dat bij Dortus past, en de EU-blokkade raakt de kopers buiten de EU niet. Nu bouwen heeft geen zin.
- HomeView: 2 klopt, eerder lager. Niet in de EU te koop, geen winkel, Apple doet agenda en herinneringen zelf.
- Samsung-bril: 2 klopt.
- iPhone Duo, Touch on Mac, Bundles, Group Purchases, EU-voorwaarden, API 36, adb QR: eens.

## Gemiste kans gezocht (Windows-kant of web)
Gezocht naar iets binnen Apple, apparaten en Android dat wel de 4 wetten en vraag 5 haalt zonder Mac en zonder Play-account.
- Windows "Agent Launchers" en de agent-winkel in Windows: bestaan (https://learn.microsoft.com/windows/ai/agent-launchers , laatst bijgewerkt 12 dec 2025; de winkel werd volgens nieuwssites aangekondigd op Build 2026 in mei). Dat is maanden oud, dus wet 1 nee. Hoort bovendien bij een andere groep. Status van de winkel niet bij Microsoft zelf bevestigd: ONBEKEND.
- Microsoft Store: geen nieuws uit november 2026 gevonden; gratis inschrijving voor makers is van 2025, voor bedrijven van mei 2026. Niet vroeg.
- Samsung-bril via Galaxy Store in plaats van Play: ONBEKEND of dat kan, en de bril komt niet naar de EU. Wet 4 blijft nee.
- Web: geen enkele van deze golven heeft een webroute met een eigen etalage.

## Mijn top
**Niets haalt een 7.** Ik sluit me aan bij de onderzoeker. Alleen volgen: Siri AI (3) voor het voorjaar van 2027, met een clouddienst als vervanging voor een Mac.
