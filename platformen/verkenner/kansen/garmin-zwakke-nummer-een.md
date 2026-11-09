# Productkans Garmin Connect IQ: betaalde apps met een zwakke nummer één

Onderzocht door Vera, 9 nov 2026 run 10:31 (Amsterdam). Nagekeken door een controleur: akkoord met cijfer en advies, 5 correcties verwerkt.

## Kort
- **Cijfer: 4 van 10. Advies: nog niet bouwen.** Garmin heeft geen manager en geen verkopersaccount ($100 per jaar, Thijs). Opent Hans ooit Garmin, dan is dit het eerste productidee.
- **Beste gat: koppelen van een loopband of walking pad (en andere fitnessapparaten via Bluetooth FTMS) aan een Garmin-horloge.** Garmin kan dit zelf niet, er wordt voor betaald, en de betaalde nummer één scoort 2,5 tot 2,9 met vooral klachten in 2026.
- **Waarom geen ja:** hoeveel er verkocht wordt is niet te zien (betalen loopt via Gumroad, dat geen verkopen toont), we hebben geen apparaat om mee te testen, en sinds september komen er nieuwe gratis apps bij.
- Tweede gat, slimme wekker (SmartWake PRO, betaald, 50.000+, 2,5): valt af omdat Garmin sinds 2025 zelf een Smart Wake-wekker op de nieuwe horloges zet.

## Hoe gemeten
- Eigen meting via de open winkel-API van apps.garmin.com (pad `/api/appsLibraryExternalServices/...`; robots.txt verbiedt alleen de webpagina's `/apps/mostPopular`, `/apps/trending` en `/developer`, niet de API). Alle apps per soort opgehaald op "nieuwst": watch-app, datafield en widget. Wijzerplaten bewust weggelaten (die zijn op 6 nov al gemeten, en daar is de nummer één een fabriek).
- **6.244 unieke apps zonder wijzerplaat** (GEZIEN). De sortering schuift tijdens het ophalen (±18% dubbele rijen), dus ±10 tot 15% kan ontbreken (GOK). Sorteren op populair of beste beoordeling stopt na 120 stuks, dus dat kon niet als aanvulling.
- Per app: download-emmer, beoordeling, aantal reviews, betaald (in de winkel of met extern abonnement), toestellen. Reviews gelezen via `/apps/<id>/reviews` (tot 90 per app).
- Prijzen staan sinds kort niet meer in de API (veld leeg), dus prijzen komen van de sites van makers.
- Scripts: `data/garmin-kans-haal.py`, `data/garmin-kans-analyse.py`, `data/garmin-kans-trefwoorden.py` (61 thema's op naam), `data/garmin-kans-reviews.py`. Data: `data/garmin-niet-wijzerplaten-2026-11-09.json.gz`.

## Eerste uitkomst: verlaten betaalde apps zijn er niet
- 852 betaalde apps zonder wijzerplaat, 307 met 1.000+ downloads (GEZIEN, controleur).
- De datum van de laatste versie zegt weinig: Garmin zet apps zelf massaal over naar nieuwe toestellen. Op 28 aug 2026 kregen 619 apps een nieuwe versie en op 27 t/m 29 okt samen 1.324 (GEZIEN, controleur). Van de 307 werken er 264 al op de Forerunner 970.
- De betaalde toppers (f3b, RH-SPORTS, mappicus, Trudelta) zijn seriemakers die bijhouden. Hier geen kans.

## Waar de top wel zwak is (GEZIEN, betaald, 1.000+, beoordeling onder 3,6, 10+ reviews: 35 apps)
| App | Maker | Downloads | Beoordeling | Waarom niet voor ons |
|---|---|---|---|---|
| Navigation through Google Maps | ProgApps | 50.000+ | 2,9 (122) | telefoonapp nodig |
| SmartWake PRO | SmartWakePro | 50.000+ | 2,5 (180) | Garmin heeft nu zelf Smart Wake |
| Music Remote (Spotify) | IqFmDev | 50.000+ | 3,0 (79) | telefoon en Spotify nodig |
| FTMSTreadmill, FTMSBiking, FTMS All Sync | Jeff_Crystal | 1.000+ elk | 2,8 / 2,9 / 2,5 | **de kans, zie hieronder** |
| Core Temperature (3 apps) | Trudelta, FeliXGear | 1.000 tot 10.000+ | 2,8 tot 3,3 | vraagt een CORE-sensor, klein |
| August, ecobee, Meross | Turner_TeKnologies | 1.000+ | 2,7 tot 3,5 | slimme huis, merk-API's |

Gratis apps met veel downloads en een zwakke top bestaan ook (cameraknop voor de telefoon: Camera Remote Watch 100.000+, 2,0; Insta360 2,0), maar die hebben allemaal een telefoonapp nodig.

## De kans: loopband en walking pad koppelen (FTMS)
**Vraag (GEZIEN):**
- Jeff_Crystal (Absolute Bollocks Creations) heeft 7 FTMS-apps (loopband, fiets, roeier, crosstrainer, stepper, klimmer, All Sync), elk 1.000+.
- WalkingPad (Jens-Duttke, gratis): 10.000+, 4,3, werkt alleen met KingSmith WalkingPad R1, R2, Z1; reviews vragen om andere merken (X21, Z3, UREVO) (controleur).
- ArduRower-IQ (gratis, 10.000+), F3b Elliptical (betaald, 100.000+, niet nagekeken of die met een apparaat koppelt).
- Garmin koppelt zelf geen FTMS-loopband. Op het Garmin-forum stuurde een medewerker op 4 aug 2026 een verzoek door naar het ideeënformulier, en op 30 okt 2026 vroegen fenix 9-gebruikers nog om loopbandondersteuning (DERDEN, forums.garmin.com, controleur).

**Betalen (GEZIEN op abscreations.netlify.app/apps/ftms/purchase/):** $4,99 per jaar per app, $7,99 per 2 jaar, bundel $8,99 per jaar of $13,99 per 2 jaar, via Gumroad met een ontgrendelcode. 14 dagen proef. Gumroad toont geen verkoopaantal (sales_count leeg). Hoeveel van de 1.000+ downloads betalen is dus **niet te meten** (zou kunnen via een openbaar omzetprofiel van de maker, niet gevonden).

**Top zwak (GEZIEN, controleur):** van 28 reviews uit 2026 op de drie grootste zijn er 18 met 1 of 2 sterren (FTMSTreadmill 8 van 9). Klachten: kan niet verbinden, data wordt niet in de activiteit opgeslagen, stopt na 1:47 min, na een update geen vermogen meer, proef van 10 minuten te kort.

**Waarom die klachten blijven (DERDEN, FAQ van de maker):** een dataveld van Connect IQ kan niet naar de eigen velden snelheid, afstand en vermogen van Garmin schrijven. De maker van de nieuwe gratis app Indoor Endurance Coach (sep 2026) zegt dat een volledige app dat wel kan via de eigen FIT-velden (DERDEN, forum, niet zelf nagekeken). Klopt dat, dan is dat ons verschil.

**Drukte:** 32 FTMS-achtige apps in totaal; sinds 1 sep 2026 kwamen er ±11 bij op naam, waarvan ±7 echte koppelapps, bijna allemaal gratis, voor roeien of fietsen, 1 tot 100 downloads (GEZIEN, controleur). Een loopband aansturen doet alleen Indoor Endurance Coach.

## Het gat in één zin
Een betrouwbare Garmin-app die veel merken loopbanden en walking pads koppelt en de training als echte loopactiviteit met snelheid en afstand opslaat; de betaalde nummer één doet dat slecht en Garmin doet het niet.

## Wie betaalt, hoeveel, hoe vaak
Thuissporters met een Garmin en een walking pad of loopband. Prijspunt in deze markt $4,99 per jaar of een paar dollar eenmalig (betaald in de winkel is mediaan $2,25, zie voorstellen/garmin-connect-iq.md). Omvang: GOK, enkele honderden tot een paar duizend kopers per jaar; niet hard te maken.

## Eerste productidee
"Pad Sync": volledige Garmin-app (geen dataveld) die via Bluetooth FTMS en de bekende eigen protocollen (KingSmith, UREVO) de loopband leest, snelheid, afstand en helling in de activiteit schrijft, en hartslag terugstuurt. Proef van 7 dagen in plaats van 10 minuten. Bouwen: Monkey C, 1 tot 2 weken (GOK), maar testen vraagt een echt apparaat of een nagebootst Bluetooth-apparaat.

## Voor en tegen
- Voor: echte vraag die Garmin zelf laat liggen, betalers bestaan, top met veel 1-sterren, zoeken op "treadmill" in de winkel levert weinig goeds.
- Tegen: verkoop niet te bewijzen, nieuwe gratis concurrentie, Garmin kan het zelf toevoegen (fenix 9 of later), testen zonder apparaat lastig, $100 per jaar en een nieuw platform zonder manager.

## Advies
Nog niet bouwen, cijfer 4. Als Hans Garmin ooit opent (platform staat op 5), dan is dit het eerste product. Vooraf meten: (1) of een volledige Connect IQ-app echt snelheid en afstand in de eigen velden krijgt (SDK-documentatie, ActivityRecording en FitContributor), (2) welke walking-pad-merken FTMS spreken, (3) een omzetbewijs van een FTMS-maker. Herhaalmeting rond 9 feb 2027: downloads en beoordelingen van Jeff_Crystal, WalkingPad en Indoor Endurance Coach opnieuw halen met `data/garmin-kans-haal.py`.

## Bronnen
- apps.garmin.com open API (eigen meting)
- https://abscreations.netlify.app/apps/ftms/purchase/ en /apps/ftms/faq/
- https://forums.garmin.com/outdoor-recreation/outdoor-recreation/f/fenix-7-series/397753/ftms-support-is-coming
- Garmin Smart Wake: https://www8.garmin.com/manuals/webhelp/GUID-8C2C402F-55AC-431F-9CF2-1442B89CE149/EN-US/GUID-5F030BAF-DBBA-4201-A99C-5F3E1C16CC4D.html , https://androidauthority.com/garmin-vivoactive-6-smart-wake-alarm-3558403
