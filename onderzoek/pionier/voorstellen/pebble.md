# Voorstel: Pebble (nieuwe horloges van Core Devices, appstore apps.rePebble.com)

Noor (pionier), 8 nov 2026. Meetlat: de vijf vragen uit `organisatie/rollen/pionier.md`.
Labels: GEZIEN (zelf gezien, met link), DERDEN (anderen, met link), GOK.

## Wat is het
Pebble is terug. Core Devices (oprichter Eric Migicovsky) brengt sinds 2025 nieuwe Pebble-horloges uit: Pebble 2 Duo, Pebble Time 2 ($225) en Pebble Round 2. Ze draaien alle oude Pebble-apps en hebben een eigen appstore (apps.rePebble.com, ook in de Pebble-telefoonapp). Ontwikkelen kan in C, en sinds 2026 ook helemaal in JavaScript (Alloy), in de browser via CloudPebble (GEZIEN, https://repebble.com/blog/cloudpebble-returns-plus-pure-javascript-and-round-2-sdk).

## 1. Groeit het platform hard en zichtbaar?
Ja, vanaf nul, maar het blijft een klein hardwareplatform.
- Pebble Time 2: "built over 23,000", meer dan 80% van de voorbestellingen geleverd op 14 juli 2026 (GEZIEN, https://repebble.com/blog/pebble-mega-update-july-2026). Sinds augustus op voorraad, verzonden binnen 48 uur (GEZIEN, https://repebble.com/blog/new-pebble-weather-app-software-updates).
- Pebble Round 2: ±14.000 voorbestellingen, levering gestart 30 sep 2026, alles geleverd eind december (GEZIEN, https://repebble.com/blog/pebble-round-2-starts-shipping).
- In januari 2026: 25.000 voorbestellingen voor horloges, geen geld van buiten ("not a startup") (DERDEN, https://techcrunch.com/2026/01/12/pebble-founder-says-his-new-company-is-not-a-startup/).
- Schatting eind 2026: 35.000 tot 40.000 nieuwe horloges in omloop, plus oude Pebbles (GOK op GEZIEN). Ter vergelijking: TRMNL zit op 50.000+ apparaten.
- Motor: nostalgie, een maker die zijn bedrijf winstgevend houdt, en een open systeem (de software is open source gemaakt). Geen grote partij erachter. De ruzie met Rebble (de vrijwilligers die de oude winkel in leven hielden) is sinds nov 2025 bijgelegd (GEZIEN, https://rebble.io/2025/11/24/rebble-in-your-own-world.html).

## 2. Is de app-winkel jong?
Ja, met een vaste instroom sinds de zomer (niet versnellend).
- Eigen meting van de hele winkel via de open API `https://appstore-api.repebble.com/api/v1/apps/collection/all/{watchapps-and-companions|watchfaces}` (GEZIEN, 8 nov 2026, script `data/pebble-appstore-meet.py`): **3.785 apps en 4.325 watchfaces**, de meeste oud (uit 2014 tot 2016). Nieuw in 2026 (eerste upload, `created_at`): **1.215 apps en 2.092 watchfaces**.
- Nieuwe apps per maand op eerste upload (GEZIEN, eigen meting, nagekeken): apr 215 (wedstrijd), mei 93, jun 173, jul 125, aug 155, sep 169, **okt 157**, nov 1 t/m 8: 52. Sinds juni dus vlak rond 150 tot 170 per maand. Mijn eerste telling (248 in okt) gebruikte de datum van de laatste update en was te hoog; de controleur ving dat. Watchfaces: ±200 tot 350 per maand sinds april.
- Rebble houdt een eigen winkel bij, maar daar kwamen in 2026 maar 176 apps bij; nieuwe makers publiceren bij Core (DERDEN, onderzoeker met de API van Rebble).
- Bereik is niet te zien: de winkel toont "hearts" (vind-ik-leuks), geen installs. Nieuwe apps van 2026: mediaan 11 hearts, 67 met 100 of meer (GEZIEN).

## 3. Kan er betaald worden, of komt dat eraan?
Niet in de winkel; er is een vaag plan en een omweg.
- Geen betaalfunctie in de winkel, geen prijsvelden in de API, geen aankondiging in de blogs (GEZIEN, https://repebble.com/blog en de API). Core beloont makers alleen met wedstrijden (25 horloges als prijs in het voorjaar) (GEZIEN, https://repebble.com/blog/spring-2026-pebble-app-contest).
- Wie verdient, doet dat buiten de winkel: de nummer één, Music Boss (9.300 hearts), verkoopt een betaalde telefoonapp met proefperiode (GEZIEN, https://forum.rebble.io/t/214); MirrorMap vraagt $3 per maand via Google Play (GEZIEN, https://mirrormap.app/). Die route is open voor ons, maar dan verkopen we een telefoonapp, met de afdracht van Apple of Google, aan een paar tienduizend horlogedragers.
- Plan zonder datum: Eric Migicovsky schreef op 5 nov 2025 over een "Humble Bundle-like pay-what-you-want donation subscription" in de Pebble-app "that funnels money towards developers", en op 24 nov 2025 "working on other ways for Pebble developers to earn money" (DERDEN via de controleur, https://ericmigi.com/blog/ ). In de blogs van 2026 staat er niets meer over.
- Betalen op het horloge zelf kan via KiezelPay, een dienst van derden (DERDEN via de controleur).
- Daarmee geldt de nee-regel ("geen enkel plan") niet strikt, maar het is een zwakke ja.

## 4. Is er al vraag te zien?
Ja, deels. Reddit (r/pebble) gaf een 403; vraag gemeten aan de hearts van nieuwe apps (GEZIEN, eigen meting en onderzoeker):
- Muziek en Spotify-bediening (Music Boss 9.300, Playback for Spotify 607).
- Home Assistant (Home Assistant WS 496, 5 apps).
- AI-assistent op de pols (18 apps; Wrist AI Evo 252, Gemini Voice 240, "Claude" 214). Er komt ook een "Plugins"-voorvertoning in de telefoonapp die AI-diensten koppelt (GEZIEN in de beschrijving van Talk 2 Agent in de API; niet in de blog).
- Gezondheid en sport (Pebble Fit 397, Pebble Meds 235), OV en navigatie (15 OV-apps, Navi App 367).

## 5. Is de eerste plek in een categorie nog te pakken?
Ja, op hearts. In bijna elke categorie heeft de beste nieuwe app een paar honderd hearts: Remotes top 607, Health & Fitness top 397, Notifications top 82 (GEZIEN). Home Assistant en AI-assistent hebben geen sterke nummer één. Maar wat een nummer één hier waard is, weet niemand: geen installs, geen betaling, en de hele markt is ±40.000 horloges.

## Risico dat het platform het niet haalt
- Klein bedrijf zonder buitengeld, hardware met leverproblemen; één mislukt model en de groei stopt.
- Tekens van stokken: de instroom van nieuwe apps zakt na de Round 2-levering (eind december) terug onder 100 per maand, of Core kondigt geen nieuw model aan voor 2027.
- Het plafond: zelfs als Pebble verdubbelt, blijft het een niche van tienduizenden mensen.

## Categorie en eerste productidee (als het later wel kan)
Home Assistant op de pols: knoppen, status en meldingen van je huis, met een gratis horloge-app en een betaalde telefoonkant (abonnement) voor meerdere huizen of widgets. Past bij de vraag (Home Assistant komt ook bij TRMNL en Godot-gebruikers terug), en de huidige beste (496 hearts) is een hobbyproject.

## Wat ik niet kon meten
- Installs per app en het aantal actieve horloges.
- Wat gebruikers vragen op Reddit en Discord (403 of besloten).
- Herhaalmeting: draai `data/pebble-appstore-meet.py` rond 8 dec 2026 en eind januari 2027. Blijft de instroom boven 200 apps per maand na de Round 2-levering, dan groeit het platform echt.

## Cijfer en advies
**Cijfer 4. Advies: nee voor nu, wachtlijst.**
Waarom: dit is een echte pionierswinkel (van bijna niets naar ±160 nieuwe apps per maand in 2026, zwakke nummers één, open API, makkelijk bouwen in JavaScript). Maar de markt is ±40.000 horloges, de instroom staat sinds juni stil rond 150 tot 170 apps per maand, de winkel kan niet betalen (alleen een vaag plan uit 2025 en KiezelPay of een eigen telefoonapp), en of een eerste plek installs oplevert, is niet te zien.

Nagekeken door een controleur (agent) met curl: totalen en verkoopcijfers kloppen; de maandreeks was fout (laatste update in plaats van eerste upload) en is verbeterd; plan van Eric en KiezelPay toegevoegd. Cijfer 4 blijft.

Wat het zou veranderen: Core kondigt betaalde apps of een makersdeel aan, of de horlogeverkoop gaat boven 100.000 en de instroom stijgt na december boven 200 apps per maand (nu ±160).
