# Voorstel: Android Automotive (auto's met Google built-in, apps via Google Play)

Noor, pionier, 8 nov 2026. Onderzoeker: één agent (groei, winkel, geld, vraag, risico). Zelf nagekeken: de blog van Google (okt 2026), de pagina's over Play Billing en de Car Hardware API, en installs van apps die alleen voor de auto zijn (AppGoblin en Google Play). Geen controleur, want het advies is geen ja en de kerncijfers heb ik zelf gezien.

**Advies: nee voor nu, wachtlijst. Cijfer 4.**

In één zin: het platform groeit gestaag, maar het aantal kopers per app is klein (een app die alleen voor de auto is haalt 1.000 tot 6.500 installs per maand), de winkel is al vijf jaar open en vult nu met grote merken, en wat wij het best zouden kunnen bouwen (een rittenlog) mag niet, omdat de kilometerstand dicht zit.

## 1. Groeit het platform hard en zichtbaar? Matig, gestaag

- Mei 2025: Google built-in in "over 50 models", "over 300 apps" in Play (DERDEN, https://android-developers.googleblog.com/2025/05/android-for-cars-google-io-2025.html).
- 13 okt 2026: "16 brands and more than 100 models", "more than 700 apps" (GEZIEN, https://blog.google/products-and-platforms/platforms/android/cars-with-google-built-in-google-play-updates/). Dus in ±17 maanden twee keer zoveel modellen en ruim twee keer zoveel apps.
- GM: ±4 miljoen auto's in de VS met Google built-in (DERDEN, https://news.gm.com/home.detail.html/Pages/news/us/en/2026/apr/0428-Google-Gemini.html). GM schrapt CarPlay en Android Auto in nieuwe auto's (DERDEN, https://www.carexpert.com.au/car-news/general-motors-dumps-apple-carplay-and-android-auto). Volvo zet 2,5 miljoen auto's om (DERDEN, https://paultan.org/2024/09/05/volvo-to-update-2-5-million-vehicles-with-google-built-in-with-ex90-ex30-interface-from-as-early-as-2020/).
- Totaal op de weg: 8 tot 12 miljoen auto's (GOK). Ter vergelijking: Android Auto (via de telefoon) staat in ±250 miljoen auto's, maar dat is een ander platform.
- Motor: geloofwaardig. Google zelf, GM, Volvo, Renault, Honda, Mazda en BYD; Geely-groep vanaf eind 2027 (DERDEN, https://en.wikipedia.org/wiki/Android_Automotive). Maar groei gaat met het tempo van autoverkoop: een auto vervang je eens in de 8 tot 12 jaar.
- Gebruik zichtbaar in installs: Vivaldi voor de auto (alleen auto) 140K installs, ±6.500 in de laatste 4 weken, "strong growth" (DERDEN, schatting AppGoblin, https://appgoblin.info/apps/com.vivaldi.browser.automotive; Play-bucket 100K+ GEZIEN).

## 2. Is de app-winkel jong? Nee, wel nieuwe hoeken

- De Play Store zit sinds 2020 in auto's (Polestar 2). Games in geparkeerde auto's sinds april 2023, browsers juli 2023, weer sinds mei 2025 (DERDEN, wijzigingslog https://developer.android.com/docs/quality-guidelines/car-app-quality; blog I/O 2025).
- Toegestane soorten: tijdens rijden alleen media, navigatie, POI (laden, parkeren, tanken), IoT en weer; geparkeerd ook video, games en browsers (DERDEN, https://developer.android.com/training/cars). Apps voor tijdens het rijden zijn vaste sjablonen van Google: weinig ruimte om op te vallen.
- "Car ready mobile apps" (sinds feb 2025): bestaande telefoonapps voor video en games komen vanzelf naar de auto, op uitnodiging. Zo kwamen Angry Birds, Candy Crush, STARZ, Firefox, Ludo King en JioHotstar binnen (GEZIEN, blog okt 2026). De geparkeerde hoek vult dus met grote titels.
- Nog in aantocht (mei 2026): widgets ("later"), mediasjablonen, Maps SDK voor POI en weer (DERDEN, https://android-developers.googleblog.com/2026/05/android-for-cars-unifying-platforms-premium-experiences.html). Widgets kunnen een jonge hoek worden; datum onbekend.
- Aantal apps per categorie kon ik niet tellen: de Play Store op internet heeft geen filter voor auto's.

## 3. Kan er betaald worden? Ja, maar omslachtig

- Google Play Billing werkt, "the purchase flow is not completed on device but is instead completed on another device" (telefoon of website) (GEZIEN, https://developer.android.com/training/cars/platforms/automotive-os/google-play). Play Licensing werkt, dus betaalde apps kunnen.
- Voor navigatie, POI, IoT en weer: in de auto geen abonnement afsluiten en geen betaalmethode instellen (DERDEN, quality guidelines PA-1). Dus verkopen via de telefoon.
- Afdracht zoals Play: 15% op abonnementen (GOK, standaard Play-tarief).

## 4. Is er vraag te zien? Zwak gemeten

- Reddit gaf 403 voor de onderzoeker; daardoor geen eigen telling van verzoeken. Eerlijk: dit punt is niet goed gemeten.
- Wel gezien: klachten over Spotify op Android Automotive (DERDEN, https://community.spotify.com/t5/Android/AAOS-Spotify-for-Android-Automotive-desperately-need-improving/td-p/5276508), vraag naar Home Assistant in de auto (DERDEN, https://community.home-assistant.io/t/ha-companion-app-for-android-automotive/316338) en Plexamp (DERDEN, https://forums.plex.tv/t/plexamp-for-android-automotive/808763).
- Wat bezitters vaak willen (dashcam, Sentry-bewaking, rittenlog) kan een buitenstaander niet bouwen: camera's zijn voor het merk en de kilometerstand is "Data not available to Android Automotive OS apps installed from Google Play" (GEZIEN, https://developer.android.com/training/cars/apps/library/car-hardware-api).

## 5. Is de eerste plek in een categorie nog te pakken? Klein

- Rittenlog: valt af (zie hierboven, en past in geen toegestane soort).
- Laden en ritplanning: bezet door ABRP, PlugShare en Chargemap (elk 1M+ installs, telefoon en auto samen; DERDEN via onderzoeker).
- Weer (open sinds mei 2025): Foreca Weather Automotive, alleen auto, uit nov 2025: 9.600 installs, ±1.200 in de laatste 4 weken (DERDEN, AppGoblin https://appgoblin.info/apps/com.foreca.car.automotive; Play 10K+ GEZIEN). Weather & Radar en Weather Navigation (80K, telefoon plus auto) zitten er ook. De nummer één is dus niet sterk, maar de hele categorie levert misschien enkele duizenden installs per maand op.
- IoT: Home Assistant heeft al een eigen Android Automotive-app (DERDEN, https://www.apkmirror.com/apk/home-assistant/home-assistant-android-automotive/home-assistant-android-automotive-2025-6-2-full-release) en er is een onofficiële met dashboard (DERDEN, https://community.home-assistant.io/t/ha-automotive-unofficial-app-for-android-automotive-os/1020221).
- Rekensom (GOK): stel dat wij de beste weer-app worden met 2.000 installs per maand en 3% betaalt $2 per maand: na een jaar ±700 betalers is optimistisch; realistischer een paar honderd, dus € 200 tot € 600 per maand na een jaar, en dat alleen als we Foreca en Weather & Radar verslaan binnen een vast sjabloon.

## Risico en waaraan je ziet dat het stokt

- Google maakt de grote apps zelf (Maps, Gemini, YouTube, Play) en de merken hun eigen (Polestar, Volvo, GM). Grote telefoonapps komen vanzelf mee via car ready.
- Merken die afhaken of Android Automotive zonder Google Play gebruiken: Stellantis (2022), Ford Explorer EV, Hyundai, Rivian, Lucid (DERDEN, Wikipedia hierboven).
- Android Auto krijgt nu ook geparkeerde video, games en widgets (blog mei 2026): de eigen plek van Google built-in wordt kleiner.
- Teken van stokken: Google noemt in mei 2027 minder dan 1.000 apps of minder dan 120 modellen, of de installs van Vivaldi en Foreca vlakken af.

## Eerste productidee (alleen als het later wel klopt)

Een weer-app voor onderweg die op Google built-in en Android Auto tegelijk draait: regen en gladheid langs de route in het weersjabloon, abonnement verkocht in de telefoonapp. Onderscheid: één app voor beide, met waarschuwingen per rit in plaats van een kaart. Pas zinvol als widgets opengaan voor derden.

## Wat zou het cijfer veranderen

- Omhoog (6): Google opent widgets voor derden met een eigen plek in de winkel, of geeft kilometerstand en ritdata vrij aan Play-apps (dan wordt een rittenlog mogelijk, met echte vraag bij zakelijke rijders), of auto-apps halen 10.000+ installs per maand.
- Omlaag (2): Google voegt Google built-in en Android Auto samen zodat de winkel van de auto verdwijnt, of de installs van auto-apps zakken.

## Herhaalmeting

`python3 platformen/pionier/data/aaos-meet.py` (installs van Foreca, Vivaldi en Weather Navigation via AppGoblin en Play), rond 8 feb 2027, en de aantallen uit de I/O-blog van mei 2027.
