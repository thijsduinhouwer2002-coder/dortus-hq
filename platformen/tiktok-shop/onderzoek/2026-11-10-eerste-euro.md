# TikTok Shop: wanneer de eerste euro, en kan het sneller? (Tess, 10 nov 2026, 00:10 NL)

Aanleiding: bericht van Thijs aan Hans en Patrick (10 nov 00:05): bijna €1000 uitgegeven, nog geen euro binnen, de eerste echte euro is de mijlpaal. Hier eerlijk wat TikTok Shop daaraan doet.

## 1. Huidige route (app in de TikTok Shop App Store)
- Klopt kan pas geld vragen als (a) Thijs een KvK heeft (na de verhuizing, datum onbekend), (b) de registratie als partner erdoor is, en (c) de keuringen van de app voorbij zijn: 4 tot 8 weken volgens schattingen van TikTok (GOK, zie `registratie.md`).
- Dus: **eerste euro niet eerder dan 4 tot 8 weken na de KvK** (langer als de juridische keuring nodig is), **plus de tijd tot de eerste betalende verkoper** (proefperiode, gevonden worden). GOK. Zonder KvK-datum is er geen datum. Daarmee is het een van de traagste routes naar geld binnen Dortus (GOK).
- Wat al klaar is, scheelt die weken niet maar wel dagen erna: code (Jet, tests groen), Moneybird-sandbox getest, webpagina's met privacy en prijs, registratie- en listingteksten.

## 2. Snellere variant bekeken: zonder TikTok-registratie, met upload van de export
Idee: de verkoper downloadt zijn afrekening uit Seller Center en uploadt die bij ons; wij boeken hem in Moneybird; betalen via Polar. Geen KvK, geen TikTok-keuring.

Wat kan (GEZIEN):
- Seller Center heeft een export per afrekening: Finance > Statements > Export, per afrekeningsdatum (Link My Books helpcentrum, 22 juli 2026, https://help.linkmybooks.com/en/articles/8727688-how-to-download-tiktok-shop-finance-statement). Ook TikTok Seller University noemt een Excel van uitbetalingen voor het afstemmen (zie `2026-11-08-finance-api.md`).
- Een Moneybird OAuth-app registreer je zelf op moneybird.com/user/applications/new, zonder keuring in de docs (https://developer.moneybird.com/authentication/). Polar is er al. Jets Moneybird-kant en rekenkern zijn grotendeels te hergebruiken; er moet een lezer voor het bestand bij.

Waarom ik het nu **niet** voorstel:
1. **Geen echt voorbeeldbestand.** De kolomnamen verschillen per regio en veranderen geregeld (DERDEN: Peanelle-helpcentrum, 24 april 2026, https://peanelle.vercel.app/help/csv-import-common-issues; Hubfluence zegt hetzelfde voor de VS). Zonder één echte NL- of EU-export bouwen we op een gok, en wij hebben geen winkel om er een te halen.
2. **Geen kanaal.** De App Store was juist de reden voor dit product ("waar verkopers zoeken"). Zonder die winkel moet iemand ons vinden via dortus.com of mogelijk een app-overzicht van Moneybird (niet nagekeken of dat bestaat en of het een keuring vraagt), en Chris (verspreiding) staat uit.
3. **Zwakker dan de concurrent.** Handmatig uploaden tegen Schakel, dat een koppeling TikTok naar Moneybird aanbiedt (GEZIEN, https://schakel.app/koppelingen/) voor €10 per maand bij een jaar vooruit, €15 maandelijks, en gratis tot 25 items per maand (GEZIEN, https://schakel.app/prijzen/). NL-vraag is al dun (besluit Hans 9 nov 20:44).
4. **Het kost Jet dagen** (GOK) die nu naar de echte route gaan (D1, Worker, betaalstuk).

Mijn schatting (GOK): de upload-variant brengt de eerste euro niet aantoonbaar eerder dan de App Store-route, en kost wel bouwtijd. **Advies: niet doen**, tenzij we een echte export van een NL- of IT-verkoper krijgen en een kanaal hebben. Goedkope stap om zo'n export te krijgen: via het vroege Partner Center-account met de testwinkel (op de lijst van Thijs) zien welke export Seller Center geeft, of later één verkoper vragen via Chris. Italië (tweede markt, besluit Hans) maakt de variant breder dan alleen NL.

## 3. Wat dit betekent voor de keuze waar het verbruik heen gaat
- Klopt verdient vóór de KvK niets. Bouwwerk dat nu loopt is geen verspilling (dan zijn we direct na de KvK klaar), maar levert de komende weken geen euro.
- Als het verbruik krap is of Patrick werk wil stoppen dat niets oplevert: **TikTok mag terug naar laag tempo** (bijvoorbeeld Tess en Jet elk 3 uur in plaats van elk uur) tot de KvK-datum bekend is. De code en teksten zijn dan klaar, de rest wacht toch op Thijs.
- Wat het sneller maakt: alleen de KvK zelf, en het vroege Partner Center-account (op de lijst van Thijs, ±20 min) om de koppeling met TikTok één keer echt te testen. Dat account versnelt de keuring niet, wel het vinden van fouten.

Bronnen in de tekst. Labels: GEZIEN (zelf gelezen met curl), DERDEN (anderen zeggen het), GOK (schatting).
