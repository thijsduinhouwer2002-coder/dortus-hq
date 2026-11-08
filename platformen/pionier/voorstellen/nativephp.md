# Voorstel: NativePHP Plugin Marketplace (pionier)

Noor, pionier. Run 8 nov 2026, 01:40 tot ±02:20 UTC. Eigen meting van de hele winkel (alle 109 plugins, prijs per plugin) en van Packagist (160 pakketten van type nativephp-plugin), onderzoeker (agent) voor groei, geld en vraag, controleur (agent): cijfers kloppen, maar hij vond een betaalde sync-plugin (Tether) die ik over het hoofd zag; cijfer 6 naar 5 en advies aangepast.

**Cijfer: 5 van 10. Advies: nog niet klaar. Herhaalmeting rond 8 dec.** Dit is het eerste platform uit mijn lijst waar je nu al kunt verkopen in de winkel zelf, met 70% voor de maker. Het platform is jong (mobiel pas sinds mei 2025, winkel sinds februari 2026) en groeit snel, maar de markt is klein: een paar duizend Laravel-ontwikkelaars, geen miljoenen gebruikers. En de winkel loopt al snel vol: 47 betaalde plugins van derden, waarvan twee makers (partek en firsthand) bijna dagelijks nieuwe uitbrengen. De categorie die ik eerst leeg dacht, offline sync tussen de app en de eigen Laravel-server, heeft al een betaalde speler (Tether, $99) met weinig gebruik. Een lege, grote categorie heb ik niet gevonden. Daarom nog geen ja: eerst zien of het platform blijft groeien en of er iets verkocht wordt.

Wat is NativePHP: een framework waarmee je met Laravel (PHP) echte mobiele apps voor iOS en Android bouwt, en ook desktop-apps. De app draait PHP op de telefoon zelf. Plugins voegen native functies toe (kaarten, betalen in de app, NFC, widgets).

## 1. Groeit het platform hard en zichtbaar? Ja, snel, maar klein in aantallen.

- Downloads van het hoofdpakket nativephp/mobile op Packagist, gemiddeld per dag: 432 (feb 2026), 508 (apr), 918 (jul), 1.690 (sep), 1.574 (okt), 1.982 (nov, pas 6 dagen). Ongeveer 4,5 keer zo veel in negen maanden, maar niet elke maand omhoog: mei, augustus en oktober zakten (controleur, https://packagist.org/packages/nativephp/mobile/stats/all.json?average=daily). Totaal 243.000, laatste 30 dagen 47.385 (GEZIEN door de onderzoeker en zelf nagekeken, https://packagist.org/packages/nativephp/mobile.json). Let op: CI en herhaalde installs tellen mee, dit zijn geen mensen.
- nativephp/desktop: van 226 naar 905 per dag sinds februari (GEZIEN door de onderzoeker, Packagist).
- Plugin-makers groeien mee: nieuwe pakketten van type nativephp-plugin per maand: 9 (jan), 6 (feb), 11 (mrt), 17 (apr), 14 (mei), 7 (jun), 12 (jul), 29 (aug), 15 (sep), **37 (okt)** (GEZIEN, eigen meting, eerste release per pakket op Packagist, `data/nativephp-plugins-meet.py`).
- GitHub-sterren: mobile-air 1.213, laravel 3.889 (GEZIEN door de onderzoeker, via Packagist). Discord 3.295 leden (GEZIEN door de onderzoeker, Discord-uitnodiging met tellers).
- Bij versie 2 (28 nov 2025) meldden de makers "2.500 klanten" (DERDEN, https://nativephp.com/blog/mobile-v2-is-here). Eigen claim: "on track to 10x adoption in 2026 vs 2025" (DERDEN, https://nativephp.com/blog/why-we-built-nativephp).
- Motor: twee oprichters (Simon Hamp en Shane Rosenthal, bedrijf Bifrost Technology) fulltime sinds eind 2025, een release ongeveer elke drie weken (4.7 op 30 okt 2026), sinds januari gratis en open source, sinds juli echte native schermen zonder webview ("SuperNative"). Geld komt uit eigen diensten: Bifrost (bouwen in de cloud, 10.000 builds in het eerste jaar, $100 per jaar tot $129 per maand) en Ultra (vanaf $35 per maand) (DERDEN, https://nativephp.com/blog/bifrost-turns-one en GEZIEN door de onderzoeker, https://bifrost.nativephp.com/pricing). Geen investeerders gevonden; sponsors zijn onder meer JetBrains en The PHP Foundation.
- Rem: buiten de Laravel-wereld weinig aandacht (geen Hacker News-post boven 5 punten, GEZIEN door de onderzoeker via hn.algolia.com). OpenCollective klein: 238 backers, ±$10.500 per jaar. Showcase: naar schatting 30 tot 40 echte apps in de winkels (GEZIEN door de onderzoeker, https://nativephp.com/showcase/mobile).

## 2. Is de winkel jong? Ja.

- De marketplace opende op 1 feb 2026 met alleen eigen plugins, derden volgden in de weken erna (DERDEN, https://nativephp.com/blog/nativephp-for-mobile-is-now-free).
- Nu **109 plugins** van **37 makers**: 22 van NativePHP zelf, 87 van derden (GEZIEN, eigen meting, alle 10 pagina's van https://nativephp.com/plugins/marketplace, 8 nov 2026).
- **56 betaald**, waarvan **47 van 18 makers van buiten**. Prijzen in vaste niveaus: $29 (15 plugins), $49 (21), $99 (20) (GEZIEN, eigen meting per pluginpagina).
- Grootste makers: partek (13 plugins, 12 betaald, o.a. kaarten, passkeys, wallet, print), firsthand (7, o.a. health, wallet, rich push), codingwithrk (6, gratis), codypchristian (5, o.a. Stripe, betalen in de app, AdMob). Partek en firsthand werken plugins bij van uur tot uur; dat wijst op veel werk met AI (GOK).
- Op Packagist staan 160 pakketten van type nativephp-plugin; die van derden hebben samen maar 28.068 downloads in totaal (GEZIEN, eigen meting). De beste gratis plugin van een derde zit rond 2.900 (splashscreen). De gratis eigen plugins van NativePHP halen veel meer: mobile-ui 48.208, camera 31.345 (GEZIEN, Packagist).

## 3. Kan er betaald worden? Ja, nu al, in de winkel zelf.

- Voorwaarden voor makers: 70% voor de maker, uitbetaling via Stripe Connect na 15 dagen; NativePHP keurt elke plugin en **bepaalt de prijs** ("sole and absolute discretion"), en mag het percentage met 30 dagen opzegging wijzigen (GEZIEN, https://nativephp.com/developer-terms, artikel 4). Wie zelf Ultra heeft, krijgt tot 90%.
- Sinds 26 okt 2026 krijgen Ultra-klanten tot 30% korting op plugins van derden, en de maker houdt dan 100% van die prijs (DERDEN, https://nativephp.com/blog/ultra-third-party-plugin-discount). Voorbeeld: kaarten $99, met Ultra $70 (GEZIEN, https://nativephp.com/plugins/partek/native-maps).
- Kopen gaat via een privé Composer-repo met licentiesleutel (GEZIEN door de onderzoeker, docs).
- Niet gezien: verkoopcijfers. Geen tellers, geen makers die omzet melden. Wat een plugin opbrengt, weet ik niet. Schatting: als 1 tot 3% van een paar duizend actieve ontwikkelaars een plugin van $49 koopt, is dat 30 tot 90 verkopen, dus $1.000 tot $3.000 per jaar voor de maker (GOK).

## 4. Is er al vraag te zien? Indirect wel.

- De issues en discussies op GitHub en Reddit waren vanuit onze sessie niet bereikbaar (403). Vraag is dus gemeten aan wat makers bouwen en wat NativePHP zelf verkoopt.
- Wat steeds terugkomt bij makers: lokale meldingen, biometrie, veilige opslag, scannen, push, plaats, advertenties, betalen in de app (3 plugins), widgets (2), health (2), NFC (GEZIEN door de onderzoeker en zelf, Packagist en winkel).
- Veel gratis klonen zitten precies op functies die NativePHP zelf verkoopt (push, biometrie, opslag). Teken dat er vraag is, en dat goedkoop kopiëren makkelijk is.
- Offline sync: in de winkel staat al **Tether** (tether/nativephp-client, $99, met serverpakket en eigen site laravel-tether.com); het serverpakket tether/server heeft 583 downloads in totaal (GEZIEN, https://nativephp.com/plugins/marketplace?search=sync en Packagist). Verder losse pogingen met 2 tot 124 downloads (techparse/offline-sync, cboxdk/laravel-sync, hardimpactdev/sync-engine). In de issues van mobile-air vraagt niemand om sync (controleur, 11 treffers op "sync", geen verzoek). Laravel-mensen willen wel sync elders: nathanheffley/laravel-watermelon (voor React Native) heeft 52.919 downloads (controleur, Packagist). Vraag binnen NativePHP is dus niet aangetoond.

## 5. Is de eerste plek in een categorie nog te pakken? In een paar wel, in de meeste niet meer.

- Bezet, met betaalde spelers: betalen in de app (codypchristian, developernauts), widgets (rubenvdb, all1web), kaarten (partek), wallet (partek, firsthand), health (firsthand), NFC (weswecan), Stripe (codypchristian), AdMob (twee betaald, twee gratis), live activities (vos, ook gratis). Hier is de eerste plek over een jaar niet meer te pakken door later te beginnen.
- Zwak bezet: **offline sync** (Tether, $99, weinig gebruik; zie 4). Leeg: apps op het horloge en CarPlay, Sentry-achtige foutmeldingen (alleen gratis Crashlytics), deep links (één pakket met 3 downloads) (GEZIEN, zoeken in de winkel op sync, offline, watch, carplay, sentry, deep, 8 nov). Maar leeg kan ook betekenen dat niemand het koopt (les van Grafana).
- Beste categorie als het later ja wordt: **offline sync**. Waarom: probleem aan twee kanten (plugin in de app en pakket op de server), dus lastiger te klonen dan een dunne laag om een iOS-functie; past bij Laravel-mensen met een eigen backend; nodig voor apps voor buitendienst, inspectie of voorraad. De eerste plek is niet beslist (Tether heeft weinig gebruik), maar ook niet meer leeg. Wij moeten dan duidelijk beter zijn: conflictregels per veld, gratis basis voor bereik.
- Grootste gevaar voor de eerste plek: NativePHP maakt zelf de populaire plugins en verkoopt ze (achtergrondtaken, push, meldingen, $99). Dezelfde les als bij TRMNL. Als sync bovenaan hun eigen lijst komt, zijn wij de klos.

## Eerste productidee

**"Sync" voor NativePHP** (alleen als het later ja wordt): een Laravel-pakket voor de server en een plugin voor de app die gekozen Eloquent-modellen tussen de SQLite op de telefoon en de database van de server synchroon houdt, ook na dagen zonder netwerk. Conflicten op te lossen per veld (laatste wint, of eigen regel). Een gratis basis op Packagist voor bereik (één model, alleen ophalen) en een betaalde versie in de winkel ($99) met twee kanten op, conflictregels en sync op de achtergrond. Toetsbaar af als: een demo-app met een takenlijst werkt offline, synct bij netwerk, en een conflict tussen twee telefoons gaat goed.

Inzet als het ja wordt: klein. Eerst alleen de gratis basis en meten (downloads op Packagist); de betaalde versie pas als die downloads dat rechtvaardigen. Eén bouwer, ontwerp eerst (regel 0), proef in een Laravel-app zonder telefoon (de serverkant en de sync-logica zijn gewoon PHP). Het native deel is dun, want NativePHP draait de PHP al op de telefoon.

## Wat Thijs moet doen als het ja wordt

- Een account op nativephp.com en Stripe Connect om als maker uitbetaald te worden, en de developer terms accepteren. Dat kan alleen Thijs. Pas nodig als de betaalde versie klaar is; de gratis basis kan op Packagist via GitHub.

## Risico: haalt het platform het?

- Bewijs dat het blijft: twee oprichters fulltime met eigen inkomsten (Bifrost, Ultra, plugins), snelle releases, downloads 4,5 keer zo hoog in negen maanden, aantal plugin-makers stijgt elke maand.
- Wat het zou laten stokken: Laravel-ontwikkelaars die met AI liever twee echte apps bouwen (de oprichters schreven zelf "Why Not Write It Twice?", 10 sep 2026, over Claude Code die twee native apps bouwt). Of een prijsbeleid dat makers wegjaagt: NativePHP bepaalt de prijs.
- Tekens om op te letten (herhaalmeting rond 8 dec met `data/nativephp-plugins-meet.py`, en de daggemiddelden van nativephp/mobile op Packagist): daggemiddelde twee maanden op rij niet meer gestegen, nieuwe plugin-pakketten per maand onder 15, NativePHP kondigt een eigen sync aan (Ultra bevat elke eigen premium plugin, dat zou ons wegdrukken), of Tether groeit hard. Ook: NativePHP verlaagt het percentage voor makers. Dan stoppen volgens regel 4b.
- Wat het naar ja zou tillen (8 dec): daggemiddelde nativephp/mobile boven 2.000, weer 25+ nieuwe plugin-pakketten per maand, en een eerste teken van verkoop (een maker die omzet noemt, of NativePHP die verkoopcijfers deelt).

## Wat ik niet kon meten

- Verkopen per plugin (geen tellers). Later: vragen aan makers via hun GitHub, of bij NativePHP; of zelf meten met onze gratis basis (downloads op Packagist) voor we de betaalde bouwen.
- Vraag op Reddit en Laracasts (403 vanuit de sessie). De GitHub-API werkte voor de controleur wel; een volgende run kan de issues van NativePHP/mobile-air op meest gevraagde functies tellen.
- Hoeveel mensen NativePHP echt gebruiken; Packagist telt ook CI.
