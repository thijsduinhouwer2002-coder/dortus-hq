# Voorstel: Fire TV Vega OS (Noor, pionier)

Onderzocht 9 nov 2026, 15:55 tot 16:30 UTC. Nagekeken door een controleur-agent: alle acht kernbronnen opnieuw gelezen met curl. Alles klopt; 42matters wijkt een fractie af (nu 88.440 apps, 35,45% betaald).

## In één alinea
Amazon vervangt Android op al zijn Fire TV Sticks door een eigen besturingssysteem, Vega OS (Linux met React Native erin). Oude Android-apps draaien er niet op en sideloaden kan niet. Amazon vult het gat met Android-apps die in de cloud draaien, maar **games en utilities mogen daar niet aan meedoen**. Die twee hoeken zijn dus bijna leeg en blijven leeg tot iemand ze native bouwt. Betalen werkt nu al via Amazon In-App Purchasing, ook met abonnementen. Dit is de soort kans die Thijs zoekt: een groot merk zet een nieuw platform neer en de catalogus begint opnieuw.

## De vijf vragen

### 1. Groeit het platform hard en zichtbaar?
- Amazon: "Starting with Fire TV Stick 4K Select, all future Fire TV Sticks will run on Vega" (DERDEN, https://www.aftvnews.com/amazon-confirms-all-future-fire-tv-sticks-will-run-vega-os-no-more-android-or-sideloading-on-new-models/, citaat van Amazons ontwikkelaarspagina sinds okt 2025).
- Tijdlijn: Fire TV Stick 4K Select (okt 2025, eerste Vega-stick), Fire TV Stick HD (apr 2026, vervangt de Android-versie helemaal), nieuwe Fire TV Stick 4K 3e generatie (30 sep 2026, $59,99, vervangt 4K Select en 4K Plus; alleen de 4K Max blijft Android). Verkocht in VS, Canada, Japan, Mexico, VK, Duitsland, Frankrijk, Italië, Spanje, Zwitserland en Australië (DERDEN, https://www.aftvnews.com/amazon-announces-new-3rd-gen-fire-tv-stick-4k-running-vega-os-with-an-all-new-remote/).
- Motor: Amazon zelf. Elke nieuwe stick die vanaf nu verkocht wordt (ook in de Black Friday-golf van nov 2026) is een Vega-apparaat. Amazon: "more compatible devices on the way in 2026" (DERDEN, https://developer.amazon.com/apps-and-games/blogs/2025/12/2025-year-in-review).
- Niet gemeten: hoeveel Vega-apparaten er nu in gebruik zijn. Amazon noemt geen getal. Schatting: enkele miljoenen na een jaar en drie modellen (GOK).

### 2. Is de app-winkel jong?
- Bij de start (okt 2025) had Vega 1.257 apps, **inclusief** Android-apps uit de cloud, tegen "Over 30,000" voor Fire OS. Per categorie: Games 0, Utilities 1, Weather 0, Productivity 6, Photo & Video 16, Customization 4, Books 0, Finance 0, Movies & TV 490 (DERDEN, https://www.aftvnews.com/amazon-vega-os-app-report-11-year-old-fire-tvs-support-more-top-apps-than-the-new-fire-tv-stick-4k-select/). Volgens de schrijver lopen "nearly all" daarvan via de cloud.
- Het Cloud App Program is alleen voor apps die Amazon kiest, de app moet op de 4K Max werken en mag geen game of utility zijn (DERDEN, https://developer.amazon.com/docs/cloud-app-program/amazon-cap.html, nagelezen door de controleur). Het is nu gratis; komt er een prijs, dan meldt Amazon dat minstens 6 maanden vooraf. Dan vallen er cloud-apps weg en wordt de catalogus nog leger.
- April 2026: "Vega doesn't offer any games for download, only cloud-based streaming from Xbox or Amazon's Luna", en "no file managers, no screen mirroring" (DERDEN, https://www.pcworld.com/article/3128166/the-new-fire-tv-os-is-for-amazon-not-you.html).
- Een nieuwere telling: niet gevonden, ook niet door de controleur. **Zelf tellen kon niet**: amazon.com verbiedt Claude in robots.txt (ClaudeBot en Claude-User: Disallow /). Niet omzeild.

### 3. Kan er betaald worden?
- Ja, nu al. Vega heeft Amazon In-App Purchasing: "present, process, and fulfill purchases of digital content and subscriptions", met abonnementen, abonnement wijzigen, promotieprijzen en een sandbox (GEZIEN, https://developer.amazon.com/docs/vega/2.0/vega-iap-overview.html). RevenueCat ondersteunt Vega (DERDEN, https://www.revenuecat.com/docs/getting-started/installation/vega).
- Afdracht: de gewone Amazon Appstore-regels, 70/30, en 80/20 met het Small Business Accelerator Program (GOK uit bekende regels, niet opnieuw gelezen).
- Kosten vooraf: een Amazon Developer-account is gratis (GOK, niet opnieuw nagekeken). Een echte Vega-stick om op te testen kost $30 tot $60; niet strikt nodig dankzij de Vega Virtual Device.
- Let op: in 2022 waren betaalde Fire TV-apps tijdelijk niet te koop in Nederland, Polen en Zweden (DERDEN, https://www.aftvnews.com/tag/appstore/). Kopers zitten vooral in VS, VK en DE, dus voor de omzet weinig verschil.

### 4. Is er vraag te zien?
- Veel klachten van kopers die een "upgrade" kochten en hun apps kwijt zijn; slechte reviews bij elk nieuw Vega-model (DERDEN, aftvnews 2 en 5 okt 2026, https://www.aftvnews.com/tag/vega-os/).
- Bij de start ontbraken: een mediaspeler voor USB, games, VPN, bestandsbeheer, screen mirroring (DERDEN, https://www.aftvnews.com/20-missing-or-worse-features-on-the-fire-tv-stick-4k-select/).
- Wie een gat vult, komt er ook: één maker bouwde in ±twee weken Astra, een gratis Jellyfin-client, omdat zijn vriendin een Vega-stick kocht (DERDEN, https://forum.jellyfin.org/t-astra-%E2%80%94-a-jellyfin-client-for-the-new-vega-os-fire-tv-sticks-free?pid=72988, 8 juli 2026). VideoLAN bracht VLC uit "with some support from Amazon" (DERDEN, https://jbkempf.com/blog/2026/vlc-vegaos/, 23 juli 2026). Proton VPN heeft een Vega-app (DERDEN, https://protonvpn.com/support/release-notes-vegaos).
- Niet gemeten: installs of reviews van native Vega-apps (amazon.com is voor ons verboden).

### 5. Is de eerste plek in een categorie nog te pakken?
- **Mediaspeler:** nee, VLC staat er al, met steun van Amazon. Jellyfin: Astra (gratis), en het officiële Jellyfin-team werkt eraan.
- **Games** (casual spellen voor de afstandsbediening: puzzel, kaarten, quiz, woordspel): leeg. Geen enkele native game gevonden, en games mogen niet in het cloudprogramma. Op Fire OS zijn er "Over 7,000". Nadeel: tv-games verkopen meestal goedkoop.
- **Utilities en sfeer-apps** (schermbeveiliger, fotolijst, klok en weer op het tv-scherm, haardvuur of aquarium, tv als dashboard): bij de start 1 utility, 0 weer, 4 customization, en ook uitgesloten van de cloud. Op Fire OS zijn dit klassieke apps met een abonnement voor extra's.
- Waarom wij: we bouwen snel in React Native (de eigen taal van Vega), we kunnen meerdere kleine apps neerzetten, en de grote makers van Android-tv-games en utilities moeten alles herschrijven en wachten nog af.

## Kunnen wij het bouwen en testen?
- De Vega SDK installeert op macOS en **Ubuntu**, met een Vega Virtual Device om apps te draaien en te testen (GEZIEN, https://developer.amazon.com/docs/vega/2.0/install-vega-sdk.html). Apps zijn React Native; WebView mag ook.
- Niet nagekeken: of de Vega Virtual Device op een GitHub Actions-runner start (waarschijnlijk is KVM nodig, en die hebben de Linux-runners van GitHub; GOK). Dat is de eerste proef voor een bouwer.
- Het apparaat is klein: 32-bit ARM en 1 GB RAM. Zware spellen gaan niet; lichte 2D-spellen en utilities wel.

## Het risico dat het platform het niet haalt
- Vega wordt slecht ontvangen; aftvnews raadt lezers Google TV aan. Toch verkoopt Amazon de sticks zelf, met grote kortingen, en de meeste kopers kiezen op prijs.
- Fire TV-gebruikers betalen weinig: betaalde Fire TV-apps kosten meestal $1 tot $2 (DERDEN, https://data.42matters.com/amazon-fire-tv-app-store-statistics-and-trends: 88.440 apps, 35% betaald), en de lijst met best verkochte betaalde apps is bijna helemaal tablet-apps (DERDEN, aftvnews-appreport).
- Amazon kan zelf games of utilities maken, of grote makers met steun naar Vega halen (zoals bij VLC).
- Teken dat het stokt: Amazon brengt toch weer Android-sticks uit of stopt met nieuwe Vega-modellen; of over 2 maanden zijn er nog steeds geen betaalde native apps met reviews.

## Eerste productidee
Een sfeer- en fotolijst-app voor de tv: "je tv als mooi scherm als je niet kijkt". Klok, weer, eigen foto's (van de telefoon), rustige bewegende scènes. Gratis basis; $1,99 per maand of $14,99 per jaar voor eigen foto's en alle scènes. Als tweede, als de eerste loopt: een rij kleine casual games voor de afstandsbediening. Daan kan hier echt iets moois van maken, en dat is in deze lege hoek het onderscheid.

## Cijfer en advies
**Cijfer 6 (krap 7). Advies: ja met kleine inzet, maar eerst één meting.**
- Sterk: een groot merk zet het hele stick-assortiment om (1); de catalogus begint opnieuw en games en utilities zijn bewust uitgesloten van de cloud (2 en 5); betalen werkt nu al, met abonnementen (3); bouwen past bij ons (React Native, Ubuntu).
- Zwak: geen getal voor het aantal Vega-apparaten, geen eigen telling van de catalogus van nu (amazon.com verbiedt ons), en geen bewijs dat kleine makers op Fire TV per maand betaald krijgen. Dat laatste houdt het onder de 7.
- **De meting die de doorslag geeft (voor Kees of mijn volgende run):** hoeveel native games en utilities staan er nu op Vega, met reviews en prijzen. Dat kan alleen op een echt apparaat of via een bron die Amazon ons laat lezen. Opties: (a) Thijs koopt een Vega-stick ($30 tot $60) en kijkt met ons de categorieën na, alleen als Hans dat wil; (b) een nieuw appreport van aftvnews afwachten; (c) los daarvan: proef of de Vega Virtual Device op GitHub Actions draait.
- Herhaalmeting: 9 dec 2026. Lees aftvnews (tag vega-os) en de Amazon-blog op nieuwe tellingen en nieuwe Vega-apparaten (Fire TV Cube, smart-tv's).
