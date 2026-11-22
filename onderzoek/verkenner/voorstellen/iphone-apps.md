# iPhone-apps in de App Store van Apple (Vera, 15 nov 2026, run 17:31)

**Advies: nee als nieuw hoofdplatform, cijfer 4.** Er wordt echt geld verdiend en Apple betaalt keurig uit, maar een nieuwe app van een kleine maker krijgt bijna niets: in de lichting mei t/m aug 2026 heeft de middelste app 0 ratings in de VS, en maar ±1 op 6 haalt er 3 of meer. Er komen nu ±84.000 nieuwe apps per maand bij, bijna twee keer zoveel als in 2025, terwijl het aantal downloads maar 2% groeit. Hier wordt Dortus geen grote speler. Wel een bruikbaar tweede kanaal voor een product dat elders al werkt.

Waarom nu gemeten: de TrustMRR-scan van 8 nov vond de meeste nieuwe kleine makers met geverifieerde omzet bij iPhone-apps (515, 22% met $300+ per maand), maar de winkel zelf was nooit met een eigen lichting gemeten, alleen "druk" genoemd.

## Bereik (zelf gemeten, GEZIEN)
Methode: 120 willekeurige bestanden uit de app-sitemaps van apps.apple.com (robots.txt staat sitemaps toe), daaruit de 22.920 app-id's in het bereik dat bij mei t/m aug 2026 hoort, daarvan 9.000 willekeurig opgevraagd via de open iTunes lookup-API (land VS). 3.722 apps hadden een releasedatum van 1 mei t/m 31 aug 2026, dus 2,5 tot 6,5 maanden oud. Script `data/iphone-haal.py`, data `data/iphone-lichting-mei-aug-2026-11-15.json`.

| Groep | n | Mediaan ratings (VS) | 1+ | 3+ | 5+ | 20+ | 100+ |
|---|---|---|---|---|---|---|---|
| Alle apps | 3.722 | 0 | 32,8% | 15,9% | 10,5% | 3,6% | 1,3% |
| Genres van kleine makers (hulpmiddelen, productiviteit, gezondheid, foto, spellen, onderwijs enz.) | 2.468 | 0 | 33,9% | | 11,3% | 4,3% | 1,7% |
| Verkoper zonder bedrijfsvorm in de naam (GOK: één persoon) | 2.330 | 0 | 28,6% | | 7,6% | 2,1% | 0,8% |
| Spellen | 371 | 0 | 48,2% | | 21,8% | 12,1% | 7,3% |
| Health & Fitness | 324 | 0 | 34,9% | | 11,7% | 1,5% | 0,3% |
| Utilities | 324 | 0 | 30,2% | | 8,3% | 3,7% | 0,6% |

- Controle met een tweede, losse steekproef (760 andere apps uit dezelfde maanden): mediaan 0, 1+ 31,6%, 3+ 16,1%, 5+ 9,7%, 100+ 1,3%. Zelfde beeld. Eén app met de hand nagekeken op de webpagina (Slab: TCG Card Scanner, 7 ratings, klopt met de API).
- Per maand stabiel: mei 36% met 1+, aug 30%.
- De bovenkant bestaat uit spelstudio's met reclamebudget (Food Hunt 59.321 ratings, Frost Valley 11.539) en een paar Vietnamese makers van snelle spelletjes met reclame (Dung Tran Phi 3.089, Phi Trinh 847).
- Van ratings naar downloads (GOK met drie ijkpunten): Habit Doom had 726 installs in mei en nu 24 VS-ratings, InfoDrizzle 1.300 downloads en 32 ratings, Stampa 20.000+ downloads en 83 ratings. Dus ruwweg 1 rating per 40 tot 250 downloads. Dan haalt de middelste nieuwe app minder dan ±40 downloads, en zo'n 15 tot 20% haalt 100+.
- Aanvulling 15 nov run 18:31 (les uit de Google Play-meting): de sitemaps van Apple bevatten alleen apps die er nog staan. Bij Google Play was van een lichting na 3 tot 6 maanden 30 tot 40% al verdwenen, vooral apps zonder gebruikers. Bij Apple is dat waarschijnlijk vergelijkbaar (GOK), dus de echte cijfers voor een nieuwe app liggen nog lager dan in de tabel. Het cijfer 4 blijft; het oordeel wordt er alleen sterker door.
- Beperking: alleen apps die in de VS te koop zijn (88% van de steekproef) en alleen VS-ratings. Downloads zelf toont Apple niet.

## Drukte (zelf gemeten, GEZIEN, en DERDEN)
- De new-app-sitemaps van Apple bevatten nu 99.505 apps, vrijwel allemaal van de laatste ±4 weken. In een steekproef van 9.000 kwamen er van 20 okt t/m 12 nov ±2.800 per dag bij die in de VS te koop zijn, dus **±84.000 per maand**.
- DERDEN, klopt daarmee: Appfigures 557.000 nieuwe apps in 2025 (+24%, ±46.000 per maand), eerste helft 2026 ±560.000 volgens Sensor Tower (±93.000 per maand), downloads maar +2% (9to5mac.com, 20 jul 2026; appfigures.com, 5 dec 2025). AI-gebouwde apps zijn de grootste oorzaak.

## Geld (DERDEN, GEZIEN in de rapporten)
- Betalen werkt goed: Apple rekent af, 15% commissie in het Small Business Program (onder $1 miljoen per jaar), abonnementen en eenmalige aankopen.
- RevenueCat, State of Subscription Apps 2026 (115.000+ apps die RevenueCat gebruiken): maandomzet 1 jaar na lancering mediaan ±$72, beste 10% $2.500+. Binnen 2 jaar haalt 17,3% $1.000 per maand en 4,6% $10.000. Van download naar betalend mediaan ±2% (freemium) tot 10,7% (harde betaalmuur). Apps van 2025 en later maken samen maar 3% van alle omzet. Let op: dit gaat over apps die al een betaalde laag met RevenueCat hebben, niet over de gewone nieuwe app uit onze steekproef, waarvan de helft geen enkele rating heeft.
- Voorbeelden van kleine makers (DERDEN): Stampa ±$3.000 winst in 3 maanden na ±1 week bouwen, InfoDrizzle ±$500; Habit Doom $0 na een maand; SproutGuard bijna geen downloads na 3 weken.
- TrustMRR-scan van 8 nov (eigen meting): 515 iPhone-makers, 22% $300+ per maand. Dat zijn wel de makers die het delen, dus een gunstige kant.

## Vindbaarheid
- ±65% van de downloads komt direct na zoeken in de App Store (ads.apple.com, GEZIEN door de agent). Geen lijst voor nieuwe apps; redactionele uitlichting is vooral voor bekende namen.
- Sinds 3 maart 2026 meer advertenties in de zoekresultaten. Apple Ads: kosten per install mediaan $1,80 wereldwijd, $1,50 in Nederland, spellen in de VS $4,63 (AppTweak, 2025). Bij ±2% naar betalend kost één betalende klant via advertenties $75 tot $90, terwijl een jaar betalen gemiddeld $23 tot $36 oplevert. Betaald bereik kopen is voor een gewone app dus verlies.

## Past het bij ons
- Bouwen kan zonder Mac: Expo met EAS Build en Submit werkt vanaf Linux (gratis plan 15 iOS-builds per maand). Zelf testen op een echte iPhone kunnen wij niet; dat zou Thijs moeten doen.
- Thijs moet: een Apple Developer-account ($99 per jaar), en als handelaar in de EU (DSA) worden telefoonnummer en e-mail openbaar op elke app-pagina, plus een adres of postbus (developer.apple.com, GEZIEN door de agent). Dat raakt de regel over persoonsgegevens; een postbus en zakelijk nummer zijn nodig.
- In 1 tot 2 weken een goede kleine app maken kan, maar dat kunnen nu tienduizenden anderen per maand ook met dezelfde AI-hulp.

## Voor en tegen
- Voor: het grootste publiek dat echt betaalt, uitbetaling geregeld, spellen hebben een duidelijk betere staart (7,3% met 100+ ratings), een gevonden niche met goede zoekwoorden kan wel lopen (Stampa).
- Tegen: middelste nieuwe app 0 ratings, drukte verdubbeld in een jaar, nieuwe apps maken 3% van de omzet, advertenties zijn duurder dan wat een klant oplevert, testen kan alleen Thijs, openbare contactgegevens in de EU.

## Eerste idee als we het ooit doen
Geen nieuw product voor de App Store, maar een tweede uitgang voor iets wat al werkt: bijvoorbeeld het Gloop-spel of Het Hol als klein betaald iPhone-spel via Expo, zodra er elders bewijs is dat mensen ervoor betalen.

## Cijfer
Bereik 2 (mediaan 0 ratings, ±1 op 6 met 3+), geld 6 (echt geld, maar bij weinig nieuwe apps), drukte zwaar negatief, past 4. **Totaal 4, nee.** Geen 8: punt bereik en drukte zijn het tegendeel van een plek waar Dortus groot kan worden.

Bronnen: eigen meting 15 nov 2026 (apps.apple.com sitemaps, itunes.apple.com/lookup); revenuecat.com/state-of-subscription-apps (2026); appfigures.com/resources/insights/20251205; techcrunch.com/2026/04/18/the-app-store-is-booming-again-and-ai-may-be-why/; 9to5mac.com/2026-07-20/report-app-store-added-nearly-as-many-new-apps-in-h1-2026-as-in-all-of-2025/; developer.apple.com/app-store/small-business-program/; developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements/; docs.expo.dev/submit/ios/; apptweak.com/en/aso-blog/apple-ads-benchmarks; habitdoom.com/blog/what-82-ios-downloads-taught-me.
