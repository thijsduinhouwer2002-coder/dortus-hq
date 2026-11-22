# Voorstel: DriverCentral (drivers voor huisautomatisering)

Vera, 15 nov 2026, run 23:31 (Amsterdam). Snelle schifting met eigen meting plus een onderzoeker voor bronnen, geen aparte controleur.

## Advies: nee, cijfer 2
DriverCentral (drivercentral.io) is een echte markt met echte prijzen ($75 tot $250 per driver is gewoon), maar hij past niet bij ons. Alleen erkende installateurs (dealers) kunnen kopen, en een Control4-driver testen kan alleen met Composer Pro, dat elke 30 dagen met een dealeraccount geactiveerd moet worden. Wij hebben geen dealeraccount en geen hardware. Crestron en RTI zitten ook achter een inlog of dealertraining. Daarbij: verkoopcijfers zijn niet openbaar en reviews zijn schaars, dus ook het geld van kleine makers is niet aan te tonen.

## Eigen meting (GEZIEN, 15 nov 2026)
- Bron: de categoriepagina's per platform (gesorteerd op nieuwste, page-1 tot het einde) en de productpagina's. robots.txt staat alles toe behalve /app/. Lijst: `data/drivercentral-lijst-2026-11-15.jsonl` (487 adressen, inclusief subcategorieën), scripts `data/drivercentral-lijst-script.py` en `data/drivercentral-ontleed-script.py`.
- Omvang: Control4 ±423 producten, Nice 34, RTI 14, Crestron 9, URC 8. Volgens de pagina /developers/ 34 ontwikkelaars met samen ±450 producten. Klein en rustig.
- Prijzen Control4 (onderzoeker telde alle ±423): 355 betaald, 68 gratis, mediaan $110, middelste helft $75 tot $179, van $15 tot $600.
- Grootste aanbieders: Cindev 120 producten, Domosapiens 49, 4Drivers 38. Cindev lijkt nauw verbonden met DriverCentral zelf (zelfde schrijver op beide sites, eigen Cindev-sectie in de helpdesk; eigen afleiding van de onderzoeker, niet bewezen).
- Bereik: verkoopaantallen zijn niet openbaar (alleen in het dashboard van de maker). Reviews wel: van 339 gelezen productpagina's hebben er 32 een review, samen 90. Koplopers: Home Connect for Apple Home van Finite Labs (19 reviews, $250) en Siri Voice Module van DTI (9).
- Drukte: de lijst "Latest Releases" op de voorpagina bestaat bijna helemaal uit één maker (Finite Labs, meerdere drivers per week in november). Revisiedatums staan maar op 13 van de 340 pagina's in de html, dus een lichting per maand kon ik niet betrouwbaar tellen.

## Bronnen (onderzoeker, 15 nov 2026)
- Verkopen kan alleen na aanmelding per mail met bedrijfsgegevens; een aparte Developer Agreement is niet openbaar. Commissie niet gevonden. Uitbetaling volgens oude pagina's via PayPal, direct. GEZIEN: help.drivercentral.io (artikel "I Want to Sell My Drivers on DriverCentral"), drivercentral.io/marketplace/, drivercentral.io/terms-of-use/.
- Kopen: bij registratie vraagt de site een dealer-ID, "Must be a licensed dealer". GEZIEN: drivercentral.io/profiles-add/.
- Testen: DriverWorks-documentatie is openbaar te lezen (snap-one.github.io), maar gebruik zonder licentie van Snap One is "strictly prohibited". Composer Pro en de Virtual Director (werken zonder controller) vragen een dealeraccount, elke 30 dagen opnieuw. Crestron-portaal vraagt inlog; RTI-SDK alleen na dealertraining. GEZIEN: control4.com/docs (Composer Pro Getting Started), developer.crestron.com, avproglobal.com/pages/rti-driver-developers.
- Markt: Snap One noemde ±20.000 actieve installateurs in de VS (10-K boekjaar 2023, alle merken samen); Resideo nam Snap One over in juni 2024. DriverCentral zelf meldde eind 2019 5.264 dealers en 23.147 verbonden huizen; nieuwere cijfers niet gevonden.
- Concurrentie: fabrikanten laten drivers vaak gratis maken, en Control4 kocht eerder een driverbouwer over (blog Chowmain, 15 jun 2022).
- Vindbaarheid: zoeken en categorieën op de site, aanvraagformulier, maandelijkse nieuwsbrief, en koppelingen met offertesoftware (D-Tools, Portal.io, Specifi, WeQuote). c4forums.com verbiedt ClaudeBot, niet gelezen.

## Waarom nee
- Past bij ons: 1. Zonder dealer als partner kunnen we niet maken en testen, en een driver die je niet kunt testen op echte apparatuur levert storingen op bij klanten thuis.
- Geld: niet aantoonbaar voor kleine nieuwe makers. Hoge prijzen, maar weinig kopers (duizenden dealers) en een paar grote aanbieders.
- Bereik: niet te meten, reviews schaars.
- Positief, voor de volledigheid: hoge prijzen per stuk, weinig drukte, en kopers zijn vaklui die betalen voor tijdwinst. Mocht Dortus ooit een dealer als partner vinden die test en verkoopt, dan is dit een nette niche (GOK).

## Opnieuw kijken
Alleen als er een openbare emulator of testroute zonder dealeraccount komt, of als een dealer zich als partner meldt. Geen herhaalmeting gepland.
