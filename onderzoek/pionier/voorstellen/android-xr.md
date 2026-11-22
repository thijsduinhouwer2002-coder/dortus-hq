# Voorstel: Android XR (Google)

Noor, pionier, 8 nov 2026. Cijfer **4**. Advies: **nog niet klaar**, herhaalmeting rond 8 jan 2027 (na de eerste brillen).

Android XR is het besturingssysteem van Google voor headsets en brillen. Apps komen via Google Play. Eerste apparaat: Samsung Galaxy XR ($1.799, sinds okt 2025). In okt 2026 kwam XREAL Aura (bril met kabel, $1.099 tot $1.499, verzending vanaf half november), en Samsung-brillen met Gentle Monster en Warby Parker worden half december verwacht.

## De vijf vragen

**1. Groeit het platform hard? Nee, nog niet. Klein en langzaam.**
- Google-app Immersive View (alleen voor XR) als maat voor het aantal headsets: 23.780 installs vandaag (GEZIEN, Google Play, script `data/androidxr-meet.py`), 10.672 op 10 dec 2025 (DERDEN, https://reddit.sentinel-team.org/posts/1pj4fs3/snapshots/2025-12-10T21%3A50%3A02.009906Z). Dat is ±1.200 per maand erbij, totaal rond 25.000 headsets (GOK op GEZIEN).
- Galaxy XR ±40.000 verscheept in 2025 (DERDEN, IDC/Counterpoint via https://www.vrarwiki.com/wiki/Samsung_Galaxy_XR).
- De hele markt voor headsets daalde in de eerste helft van 2026 met 38,7% (DERDEN, Omdia, https://www.ictbusiness.biz/analysis/xr-headwear-shipments-fell-39-percent-in-1h26). Bij AI-brillen heeft Meta 94% (DERDEN, Counterpoint, https://9to5google.com/2026/09/22/smart-glasses-growth-h1-2026/).
- Wel een sterke motor: Google, Samsung en Qualcomm, en vijf soorten apparaten in 2026. De kans zit in de brillen: met Jetpack Projected kan een gewone telefoonapp een stuk op de bril tonen (GEZIEN, https://android-developers.googleblog.com/2026/06/what-is-new-android-xr.html). Of die brillen verkopen, is pas in januari te zien.

**2. Is de winkel jong? Ja, heel jong.** Google: "over 100 apps made to take full advantage of XR" in april 2026, dubbel zoveel als bij de lancering (GEZIEN door de onderzoeker, blog.google). Dat is ±6 tot 8 nieuwe per maand (GOK). De onderzoeker telde in de XR-weergave van Play 93 apps, waarvan ±35 echt voor XR; de rest zijn gewone 2D-apps (GEZIEN door de onderzoeker).

**3. Kan er betaald worden? Ja.** Gewoon Google Play Billing, 15% over de eerste $1M per jaar (DERDEN, https://support.google.com/googleplay/android-developer/answer/112622). Betaalde XR-apps bestaan: Virtual Desktop $24,99, Pencil XR $14,99 (GEZIEN door de onderzoeker). Daarnaast het Developer Catalyst Program: vroege brillen, begeleiding naar Google Play (GEZIEN, blog hierboven); een subsidie die je niet terugbetaalt volgens de onderzoeker (niet zelf gezien). Aanmelden moet Thijs doen.

**4. Is er vraag?** De klacht die terugkomt: "weinig te doen", de headset wordt vooral gebruikt als pc-scherm en voor pc-VR (DERDEN, https://reddit.sentinel-team.org/posts/1u1azac/snapshots/2026-06-09T21%3A41%3A35.480246Z). Vraag naar meerdere schermen; PC Connect van Google werkt alleen met Windows (DERDEN, https://www.androidcentral.com/gaming/virtual-reality/heres-why-galaxy-xr-is-replacing-my-monitor-tv-desk-etc).

**5. Is de eerste plek te pakken? Ja, maar die is weinig waard.** De beste XR-apps hebben een paar duizend installs: Virtual Desktop 3.167, Asteroid 3.215, Adobe Project Pulsar 1.432, ShapesXR 585, Pencil XR 32 (GEZIEN door de onderzoeker). Voor notities, whiteboards of een speler voor eigen video's is er geen sterke XR-app (GOK op de lijst). Met een paar honderd installs sta je bovenaan, maar het hele publiek is ±25.000 mensen.

## Risico
Het grootste risico: headsets verkopen niet (markt -39%) en de brillen komen te laat tegen Meta. Teken dat het stokt: Immersive View blijft onder 2.000 nieuwe installs per maand, en de Samsung-brillen en Aura halen in Q1 2027 geen 100.000 stuks. Teken dat het opengaat: de brillen verkopen goed en Google opent een eigen lijst voor bril-apps in Play.

Extra drempel voor Dortus: bouwen in Kotlin voor Android, testen kan in de XR-emulator op GitHub Actions (nog niet geprobeerd), en publiceren vraagt een Google Play-ontwikkelaarsaccount ($25, Thijs).

## Categorie en eerste idee
Als het opengaat: een bril-app voor korte notities en lijstjes vanaf de telefoon (Jetpack Projected), of een XR-whiteboard. Op de headset alleen al is het te klein.

## Cijfer en advies
4, nog niet klaar. Winkel jong, betalen werkt, leiders zwak, maar het platform groeit niet hard en het publiek is klein. Over twee maanden opnieuw meten met `python3 data/androidxr-meet.py` en de verkoop van de brillen opzoeken.

## Hoe gemeten
Onderzoeker (agent) voor groei, winkel, geld en vraag. Zelf nagekeken: installs van Immersive View op Google Play (23.780) en het blog van Google over I/O 2026 (Catalyst Program, Jetpack Projected). Geen aparte controleur: het advies is geen ja. Niet gemeten: de volledige XR-catalogus (Play toont alleen verzamelpagina's), verkoopcijfers 2026, Reddit zelf.

## Aanvulling 17 nov 2026 (Noor): audiobrillen, nieuw cijfer 6

Nieuw feit sinds 8 nov, en precies wat Thijs zoekt (een groot merk dat net een nieuw apparaat met een winkel krijgt):
- **Google Play neemt sinds ±20 okt 2026 apps voor audiobrillen aan.** Op 28 sep stond er nog dat Play alleen voor headsets en bedrade brillen werkte; nu ook "for augmented experiences on audio glasses". Er is geen aparte releasetrack: de bril-functie zit in de gewone telefoon-app (een projected activity met `requiredDisplayCategory` XR_PROJECTED), en Gemini opent die met "open <appnaam>" (GEZIEN, https://vr.org/articles/google-play-audio-glasses-phone-track-samsung-mid-december-2026; de quality guidelines van Google dragen "Last updated 2026-10-20 UTC", GEZIEN, https://developer.android.com/docs/quality-guidelines/android-xr). Play services 26.42 (26 okt): "You can now connect Android XR glasses to your phone" (DERDEN, zelfde artikel).
- **Twee niveaus:** "Compatible" (elke gewone app met meldingen, vanzelf, meldingen worden voorgelezen) en "Differentiated", gebouwd met Jetpack XR (Projected, Glimmer, ARCore) (GEZIEN, https://developer.android.com/docs/quality-guidelines/android-xr/augmented.md.txt, kopjes Compatible en Differentiated). Een badge "Differentiated for Glasses" in Play noemt alleen vr.org ("which Google says"); bij Google zelf staat het woord badge niet (DERDEN, controleur 17 nov: 0 treffers op beide pagina's van Google).
- **Apparaat:** Samsung Intelligent Eyewear (camera, microfoons, speakers, geen scherm; montuur van Gentle Monster en Warby Parker) komt half december in de VS en Zuid-Korea (DERDEN, ChosunBiz via https://9to5google.com/2026/11/02/samsungs-android-xr-intelligent-eyewear-reportedly-launches-in-december/, GEZIEN). Voorverkoop $395, levering 10 dec (DERDEN, https://www.talkandroid.com/534903-samsung-intelligent-eyewear-smart-glasses-preorder-price/, curl geblokkeerd, alleen de kop gezien). Verwachting in mei: "may see 2 million shipments this year" (DERDEN, kop van https://www.sammobile.com/news/samsung-and-googles-smart-eyewear-may-see-2-million-shipments-this-year/; dat was vóór het uitstel naar december, dus voor 2026 te hoog, GOK: honderdduizenden in 2027).

**De meetlat van 17 nov:**
| Eis | Uitkomst |
|---|---|
| Groot publiek (100.000+) | Nog niet: apparaat komt 10 tot ±15 dec. Merk en verwachting wijzen op 100.000+ in 2027 (GOK). Meta verkocht 7 mln+ Ray-Bans (DERDEN, UC Today mei 2026), dus de soort verkoopt. |
| Winkel jonger dan 3 maanden of binnen 8 weken | Ja: Play voor audiobrillen ±20 okt, apparaat binnen 4 weken. |
| Minder dan ±200 apps | Ja voor "Differentiated" (geen telling mogelijk, Play toont geen bril-lijst; GOK: tientallen). |
| Betalen | Ja, gewoon Google Play Billing in de telefoon-app (15% tot $1M). |
| Eerste versie binnen een week, in de cloud | Ja: Kotlin, Gradle in GitHub Actions, emulator voor audiobrillen in Android Studio. Let op: Jetpack Projected is nog 1.0.0-alpha14 (kan nog veranderen). |

**Waarom 6 en nog geen 7:**
1. **Vindbaarheid is onbekend.** Er is geen bril-track en geen bril-lijst in Play die wij kunnen zien. Een badge alleen maakt nog geen ranglijst. Zonder plek waar bril-kopers zoeken, kun je ook geen nummer één worden (zelfde les als Ebb op Garmin: goed product, niemand vindt het). Dat is de eerste meting zodra het apparaat uit is: heeft de Play-app of de companion-app van Samsung een sectie "voor je bril"?
2. **Het publiek is nog nul** tot half december.
3. **Google en Samsung pakken het voor de hand liggende zelf** (Gemini doet vragen, vertalen, navigatie, muziek). Wij moeten een taak kiezen die Gemini niet doet.

**Categorie en eerste idee:** spiekbriefje in je oor voor sprekers. Je zet je punten op de telefoon, de bril fluistert het volgende punt bij een tik op het pootje, met een oefenstand die meet hoe lang je per punt praat. Gemini doet dit niet. Concurrentie: Meta heeft een teleprompter op de Ray-Ban Display (met scherm, DERDEN, https://petapixel.com/2026/01/06/meta-adds-teleprompter-to-ray-ban-display-glasses-pauses-international-rollout), Glass Prompter op iOS en Even Realities hebben er een voor schermbrillen; voor audiobrillen op Android vonden wij niets (zoekresultaten, niet uitputtend). Andere kandidaten: handsfree stappen voorlezen bij koken of klussen (risico: Gemini), interval-coach voor hardlopen in je oor. Concurrentiecheck volgens de regel van 16 nov nog doen vóór een keuze.

**Advies: ja om klaar te zetten, beslissen vóór 10 dec.** Kleine inzet: één bouwer maakt in ±4 runs een eerste versie met de emulator in Actions, zodat we in de eerste week na levering in Play staan met de badge. Kosten: Google Play-ontwikkelaarsaccount $25 eenmalig (Thijs, als die er nog niet is). Stopregel: heeft Play eind januari nog geen vindplek voor bril-apps of blijft de verkoop van de bril onder ±100.000 (Counterpoint of IDC, Q1 2027), dan stoppen. **Wordt een 7** zodra de bril echt levert en er een bril-sectie in Play of de Samsung-app blijkt te zijn.

**Nagekeken:** controleur (agent) las alle GEZIEN-bronnen opnieuw met curl, 17 nov: klopt, behalve de badge (bij Google zelf niet te vinden, nu DERDEN). Cijfer 6 volgens hem terecht.

**Niet gemeten:** aantal "Differentiated" apps (Play toont geen lijst), voorverkoop van de bril, of de emulator voor audiobrillen in GitHub Actions draait (nog niet geprobeerd).
