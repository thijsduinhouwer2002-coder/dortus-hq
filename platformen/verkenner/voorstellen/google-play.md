# Google Play, gewone Android-apps en spellen (Vera, 15 nov 2026, run 18:31)

**Advies: nee als nieuw hoofdplatform, cijfer 4.** Google Play geeft een nieuwe app iets meer bereik dan de App Store van Apple: van de apps die er na 3 tot 6 maanden nog staan heeft de middelste 38 installs en een op de drie haalt 100+. Maar een derde tot de helft van elke lichting is dan al verdwenen, er komen ±82.000 apps per maand bij, en een install brengt op Android ongeveer 2,5 keer minder op dan op iOS. Geld verdienen kleine makers hier wel, maar niet aantoonbaar vaak, en Dortus wordt hier geen grote speler. Wel een goede tweede uitgang voor een product dat elders al werkt (Expo bouwt Android en iOS uit één code).

Waarom nu gemeten: tegenhanger van de iPhone-meting van 15 nov 17:31. Google Play toont per app een installklasse, dus bereik is hier beter te meten dan bij Apple. Alleen wijzerplaten en icon packs waren eerder gemeten (beide nee).

## Bereik (zelf gemeten, GEZIEN)
Methode: 300 willekeurige bestanden uit de sitemaps van play.google.com (robots.txt staat sitemaps en /store/apps/details toe; 87.663 bestanden van 8 nov 2026, ±43 apps per bestand, samen ±3,4 miljoen live apps, dus bijna de hele winkel). Daaruit 13.726 app-id's, allemaal opgevraagd met google-play-scraper (land VS). Daarvan 1.331 al weg (404), 2.973 zonder releasedatum (Google toont die niet altijd), 9.422 met datum. Scripts `data/googleplay-*-script.py`, data `data/googleplay-steekproef-13726-2026-11-15.jsonl`.

Lichting met release 1 mei t/m 31 aug 2026 (2,5 tot 6,5 maanden oud), installs wereldwijd (exact getal van de bibliotheek):

| Groep | n | Mediaan installs | 100+ | 1.000+ | 10.000+ |
|---|---|---|---|---|---|
| Alle apps | 1.397 | 38 | 34,7% | 14,0% | 5,2% |
| Spellen | 272 | 54 | 41,2% | 25,4% | 10,7% |
| Apps (geen spel) | 1.125 | 37 | 33,2% | 11,2% | 3,9% |
| Maker met 1 tot 3 apps op zijn makerpagina | 734 | 35 | 33,0% | 11,4% | 3,3% |
| idem, naam zonder bedrijfsvorm (GOK: één persoon) | 547 | 33 | 31,8% | 11,2% | 3,3% |
| idem, met in-app-aankopen | 204 | 80 | 45,6% | 20,1% | 4,9% |
| idem, spellen | 98 | 25 | 32,7% | 13,3% | 1,0% |
| Maker met 4 tot 20 apps | 663 | 44 | 36,7% | 16,7% | 7,4% |
| Betaalde apps (prijs boven 0) | 37 | 5 | 8,1% | 0% | 0% |

- Per maand: mei mediaan 38, juni 72, juli 33, aug 30. Lichting sep t/m okt 2026: mediaan 14, 21% 100+.
- Ratings: de middelste app heeft er 0, maar 3% heeft 10+.
- **Overlevers (controleur, belangrijkste correctie):** de sitemap bevat alleen apps die er (bijna) nog staan. Per releasemaand telt de steekproef okt 595, aug 417, mei 294, jan 175, midden 2025 ±100, terwijl de instroom ongeveer gelijk bleef. Van een lichting is na 3 tot 6 maanden dus naar schatting 30 tot 40% weg, vooral apps met weinig installs. Tel je die mee als bijna 0, dan is de echte mediaan ±5 tot 13 en haalt 21 tot 24% de 100+ (GOK op basis van GEZIEN). Om dezelfde reden zegt "jan t/m jun 2025 mediaan 258" niets over groei: dat is het overlevende vijfde.
- Ook de bovenkant is niet van ons soort: spelstudio's met reclamebudget (Overgeared Hero 2,5 miljoen, Fair Shot 1 miljoen), kloonfabrieken van autospellen, en bedrijfsapps met bestaande klanten (een kledingwinkel 390.000, banken). realInstalls telt wereldwijd.
- De 2.973 apps zonder datum zijn een mengsel van nieuw en oud (mediaan 86, 48% 100+); weglaten maakt de lichting eerder iets slechter dan beter, het effect is klein (controleur).
- Controleur: 12 van 12 apps op de webpagina gecontroleerd, installklasse en releasedatum kloppen; alle getallen herrekend. De eerste makertelling was fout (namen dubbel gecodeerd, 725 makers onterecht op 0 apps); hersteld en opnieuw gedraaid, de tabel hierboven is de herstelde versie.

Vergelijking met iPhone (15 nov): Apple toont geen downloads; daar haalde de middelste nieuwe app 0 ratings en volgens een ruwe omrekening minder dan ±40 downloads, 15 tot 20% 100+. Google Play ligt in dezelfde orde, iets beter. Beide met dezelfde overlevingsvertekening.

## Drukte (DERDEN, klopt met GEZIEN)
- AppBrain: in okt 2026 82.200 nieuwe apps op Google Play, 30.400 verwijderd, 2,1 miljoen live (appbrain.com/stats/number-of-android-apps, 15 nov 2026). Appfigures: Q1 2026 60% meer nieuwe apps dan een jaar eerder, vooral door AI-gebouwde apps (techcrunch.com, 18 apr 2026).
- Eigen steekproef: oktober is de grootste maand tot nu toe (595 van 13.726, vaker dan elke eerdere maand).

## Geld (DERDEN)
- Afdracht sinds 30 jun 2026 in de EER, het VK en de VS (nieuw model van 4 mrt 2026): 10% op de eerste $1 miljoen per jaar, plus 5% factureringsvergoeding als je Play Billing gebruikt; eigen betaalroutes mogen (android-developers.googleblog.com/2026/03/a-new-era-for-choice-and-openness.html). Gunstig.
- RevenueCat 2025: mediane omzet per installatie na 60 dagen $0,14 op Google Play tegen $0,38 op de App Store (Noord-Amerika $0,35 tegen $0,66). 10 tot 14% van de apps haalt alles uit Android. RevenueCat 2026: 77% van de nieuwe abonnementsapps is voor iOS; op Google Play komt 32% van de opzeggingen door mislukte betalingen.
- Rekensom (GOK): een nieuwe app met in-app-aankopen van een kleine maker heeft na 3 tot 6 maanden mediaan ±80 installs (overlevers). Keer $0,14 is dat ±$11. Pas bij de beste ±5% (10.000+ installs) wordt het ±$1.000 of meer.
- Betaalde apps (prijs vooraf) zijn bijna verdwenen: 2,6% van de lichting, mediaan 5 installs. Vrijwel alles is gratis met reclame (33%) of in-app-aankopen (25%).
- TrustMRR-scan van 8 nov (eigen meting): 70 Android-makers met geverifieerde omzet, 11% met $300+ per maand (iPhone 515 makers, 22%). Weinig bewijs dat nieuwe kleine Android-makers vaak verdienen.
- Voorbeeld (DERDEN): HabitKit, solo, 290.000 downloads op Google Play in 2025 en $602.000 omzet over beide winkels samen; begon vóór 2024.

## Vindbaarheid
- Vooral zoeken in de winkel; harde cijfers over het aandeel van zoeken tegenover aanbevelingen niet gevonden (GOK). Google meldt dat Apps Home 18% meer bezoekers trekt dan een jaar eerder.
- Advertenties: een install op Android kost meestal tot $3 à $3,50 (mapendo.co, H1 2026); spellen wereldwijd mediaan hypercasual ±$0,40, hybridcasual $0,95 (Adjust via foxdata.com). Tegenover $0,14 tot $0,35 omzet per install is reclame kopen voor een gewone app verlies; voor reclamespelletjes werkt het alleen met grote schaal.

## Past het bij ons, en kan Thijs verkopen
- Bouwen kan op Linux en in GitHub Actions (Android SDK, Gradle, Expo of gewone Kotlin), en testen met de Android-emulator. Dat is beter dan bij iPhone.
- Account: eenmalig $25 en een ID-controle (Thijs). **Een persoonlijk account moet eerst een gesloten test doen met 12 testers, 14 dagen aan één stuk**, en sinds 2026 wijst Google af bij te weinig echt gebruik; makers verliezen daar 3 tot 6 weken (dev.to, testerscommunity.com, jun tot aug 2026). Een organisatie-account (KvK en een D-U-N-S-nummer, tot ±30 dagen) heeft die regel niet.
- Wie geld vraagt is handelaar: vóór 1 feb 2027 opgeven, en vanaf 1 mrt 2027 staan bij een persoonlijk account adres en telefoonnummer openbaar in de winkel. Voor Thijs betekent dat een zakelijk adres en nummer nodig (staat bij Thijs). Een eerste betaald product kan dus niet binnen een week verkopen.
- Android developer verification: vanaf 2027 wereldwijd, ook voor apps buiten de winkel.

## Tegen de lat van een 8
1. Nieuwe kleine makers verdienen: niet aangetoond. Geen verkoopcijfers in de winkel, omzet per install laag, weinig makers met $300+ op TrustMRR. Zwak.
2. Bereik voor nieuwkomers: matig. Na correctie voor verdwenen apps mediaan ±5 tot 13, ±een op vijf 100+, in een vloed van 82.000 per maand. Zwak tot matig.
3. Bouwen en testen: ja, goed. Sterk.
4. Binnen een week verkopen: nee, testerregel en handelaarsadres. Zwak.
Eén van de vier sterk: cijfer 4.

## Wat we er zouden bouwen (als tweede uitgang)
Geen eigen Android-product als hoofdzaak. Wel: zodra een Dortus-product met Expo of een webtechniek elders betalende gebruikers heeft, een Android-versie erbij. Een organisatie-account (na de KvK) bespaart dan de testerregel.

## Wat het cijfer kan veranderen
- Een eigen meting van geld: als er een openbare bron komt met omzet per app voor nieuwe Android-apps (bijv. TrustMRR met 50+ nieuwe Android-makers waarvan 20%+ $300+), opnieuw wegen.
- Geen herhaalmeting gepland: dit is een volwassen winkel, het beeld verandert niet snel. De scripts staan klaar om dezelfde meting over een half jaar te herhalen.
