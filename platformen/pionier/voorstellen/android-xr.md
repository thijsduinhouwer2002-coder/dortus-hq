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
