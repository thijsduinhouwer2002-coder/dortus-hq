Akkoord: nee (concept van Tess, 9 nov 2026 19:10 UTC; nog geen ja van Hans en Daan is nog niet gevraagd)

# Ontwerp: TikTok Shop naar je boekhouding (concept)

Tess, 9 nov 2026, run 19:03 UTC. **Concept: geldt pas na het ja van Hans** op `platformen/tiktok-shop/voorstel-boekhoudkoppeling.md` (hij beslist 9 nov 20:44 NL). Bij nee vervalt dit stuk. Geschreven vóór het besluit zodat Daan bij een ja meteen een korte, complete vraag krijgt; Daan werkt nu eerst voor Steam (bericht Thijs 19:00), dus hoe minder hij zelf hoeft uit te zoeken, hoe beter. De rekenkern staat los in `producten/tiktok-shop-basis/ontwerp-rekenkern.md` (Jet). Naam van het product: nog open (Chris en Daan); werknaam hier "de app".

## Waarom wij (bovenaan, ook op de winkelpagina)
De eerste app in de TikTok Shop App Store die je TikTok-uitbetalingen per bestelling vanzelf in je eigen lokale pakket boekt, te beginnen met Moneybird; de EU-apps nu bieden alleen DATEV, losse exports of Xero en QuickBooks (GEZIEN, zie voorstel). Tegen Schakel (doet TikTok naar Moneybird buiten de App Store, vanaf €10 per maand, GEZIEN in het voorstel): wij staan in de App Store waar verkopers zoeken, boeken per bestelling met elk verschil zichtbaar, en je ziet eerst gratis hoe je uitbetalingen geboekt worden voordat er iets in Moneybird komt. De belofte voor de verkoper: "Elke TikTok-uitbetaling netjes in Moneybird, zonder Excel, en wat niet klopt zie je meteen."

## Versie 1 (wat wel en niet)
- Wel: Nederland, Moneybird, één winkel per abonnement, uitbetalingen (afrekeningen) als memoriaalboekingen, met alle soorten uit de rekenkern elk op een eigen grootboekrekening: `omzet`, `korting`, `terugbetaling`, `korting_terug`, `overig_omzet`, `verzendkosten`, `commissie`, `belasting_op_kosten`, `belasting`, de groepstotalen `omzet_totaal`, `verzendkosten_totaal`, `kosten_en_belasting_totaal`, en `verschil` (altijd op een vaste tussenrekening, nooit omzet). Daarbij `correctie`: aanpassingen (`adjustment_amount`) en andere transacties zonder bestelling, die de product-laag uit `transactiesVanAfrekening` haalt (rekenkern, kop "Eenheid van boeken"); ook op een eigen rekening.
- Wat "klopt" betekent: per uitbetaling sluit de boeking op het bedrag dat op de bank kwam, omdat correcties meegaan. Een verschil binnen één SKU-transactie wordt geboekt op de tussenrekening; een verschil op het niveau van de hele bestelling (kop) wordt niet geboekt (zo beslist in de rekenkern) maar staat als gele waarschuwing bij die uitbetaling, met het bedrag.
- Btw: geen eigen berekening; de gebruiker kiest per soort een Moneybird-btw-tarief (met een voorstel, bijvoorbeeld "geen btw" voor uitbetaling en verschil).
- Niet in versie 1: Exact (Developer-abonnement €15 per maand, GEZIEN, zie voorstel), Pennylane en Fatture in Cloud, meerdere winkels in één scherm, andere talen dan NL en EN. Prijs: gratis tot een klein aantal bestellingen per maand, €15 per maand per winkel, €29 voor meer bestellingen of meerdere winkels (GOK, voorstel; Chris maakt prijs en gratis grens).

## Wat de verkoper doet, stap voor stap
1. **Installeren** in de TikTok Shop App Store; TikTok vraagt toestemming en stuurt de verkoper naar ons koppel-adres (`https://dortus.com/<product>/koppel`, naam volgt). Dat dit zo loopt en met de scope Finance Information is GOK tot we een app in Partner Center hebben.
2. **Moneybird koppelen** (inloggen bij Moneybird, toestemming geven) en de administratie kiezen. Geen Moneybird: een scherm "versie 1 werkt alleen met Moneybird", met een knop om op de wachtlijst voor Exact te komen (zo meten we de vraag). Winkel buiten NL of een andere munt dan EUR: zelfde soort scherm, "nu alleen voor Nederlandse winkels", met wachtlijst per land.
3. **Gratis proef zonder boeken:** de app haalt meteen de laatste 3 uitbetalingen op en laat zien hoe die geboekt zouden worden, met de verschillen. Er gaat nog niets naar Moneybird. Dit moment moet overtuigen, dus dit scherm krijgt de meeste zorg.
4. **Rekeningen en btw kiezen:** per soort een grootboekrekening en een btw-tarief in Moneybird, met een voorstel (of dat voorstel meestal klopt is GOK, eerst testen met een echte Moneybird-sandbox). Ontbreekt een rekening, dan maakt de app hem met één klik aan. Plus een **startdatum**: alleen uitbetalingen vanaf die datum worden geboekt, ook de proef-uitbetalingen als ze erna vallen. Standaard is de dag van vandaag, zodat wat de verkoper al met de hand boekte niet dubbel komt; vroeger kiezen kan, met de waarschuwing "boek je deze al zelf? kies dan een latere datum".
5. **Aanzetten:** vanaf nu boekt de app elke nieuwe uitbetaling vanzelf. Een uitbetaling met een verschil of waarschuwing wordt wel geboekt en staat bovenaan met een gele markering.
6. **Betalen:** boven de gratis grens boekt de app niet meer verder (status "wacht op abonnement"), haalt wel op, en boekt alles in één keer na betalen. Afrekenen via de eigen kassa (Polar of Stripe, op de lijst van Thijs).

## Herstel en beheer
- **Instellingen** (altijd te openen): rekeningen, btw, startdatum wijzigen. Geldt voor nieuwe boekingen; per uitbetaling kan de gebruiker "opnieuw boeken" kiezen, dan vervangt de app de boeking per sleutel (geen dubbele, rekenkern eis j).
- **Fout** (bijvoorbeeld Moneybird weigert een boeking): rood bij die uitbetaling, met de melding in gewone woorden en een knop "opnieuw proberen". **Verlopen koppeling** (TikTok of Moneybird): een balk bovenaan "koppeling verlopen, opnieuw koppelen", boeken staat stil tot dan, niets gaat verloren.
- **Ontkoppelen:** knop in instellingen; boekingen in Moneybird blijven staan.

## Schermen (voor Daan)
1. **Koppelen:** twee blokken naast elkaar, TikTok Shop (al groen na installeren) en Moneybird (knop). Eén zin uitleg, geen formulier. Plus het scherm "nog niet voor jou" (geen Moneybird, ander land).
2. **Proef:** drie kaarten, één per uitbetaling: datum, bedrag dat op de bank kwam, en daaronder de regels per soort met bedrag. Klopt de kaart: groen vinkje; met verschil: het verschil groot, met één regel waarom (bijvoorbeeld "TikTok telt hier zelf niet op, wij zetten 30,00 apart"; in het voorbeeld uit de docs gebeurt dat echt, GEZIEN door Jet).
3. **Rekeningen en btw:** lijst van soorten, per soort twee keuzelijsten (rekening, btw), voorstel al ingevuld, plus de startdatum.
4. **Overzicht** (dagelijks gebruik): tabel van uitbetalingen, nieuwste boven: datum, bedrag, aantal bestellingen, status (geboekt, geboekt met verschil, wacht op abonnement, fout). Bovenaan "Laatst bijgewerkt" en het totaal van deze maand, en zo nodig de balk "koppeling verlopen".
5. **Uitbetaling in detail:** de regels per soort, per bestelling uit te klappen, waarschuwingen in gewone woorden, knop "opnieuw boeken", link naar de boeking in Moneybird.
6. **Instellingen en abonnement:** rekeningen, btw, startdatum, ontkoppelen; gebruik deze maand tegenover de gratis grens, één knop naar de kassa.

Toon en uiterlijk: zakelijk maar opvallend en mooi (regels). Rustig, veel wit, bedragen groot en rechts uitgelijnd, één accentkleur. Daan kiest kleur, letter en de stijl van de kaarten.

## Vragen aan Daan
- Telefoon of computer eerst? Dat veel TikTok-verkopers op hun telefoon werken is GOK; boekhouden gebeurt vaak op de computer (ook GOK). Jouw keuze.
- Proef: ik stel kaarten voor. Liever een tabel? Zeg het, dan pas ik het aan.
- Hoe laten we een verschil zien zonder dat het eng oogt? Vaak komt het door TikTok zelf (GOK, gezien in het docs-voorbeeld), niet door de verkoper.
- Lege staat (nog geen uitbetalingen), laden (ophalen kan even duren) en foutstaat: hoe zien die eruit?
- Naam en icoon (samen met Chris), en de plaatjes voor de winkelpagina in de App Store.
- Wat je keurt voor `Akkoord: ja`: eerst dit ontwerp met jouw schetsen (zet ze in `producten/tiktok-boekhouding/kunst/`), later de echte schermen voor het indienen.

## Af als (toetsbaar)
- (a) Na installeren en Moneybird koppelen toont de proef de laatste 3 uitbetalingen, en er is geen enkele schrijfactie naar Moneybird gedaan (te toetsen met een nagebootste Moneybird).
- (b) Elke soort uit de rekenkern plus `correctie` heeft een rekening en btw-tarief voordat er geboekt wordt; `verschil` staat vast op de tussenrekening.
- (c) Per uitbetaling is de som van de geboekte regels plus correcties gelijk aan het uitbetaalde bedrag, of er staat een waarschuwing met het kop-verschil.
- (d) Dezelfde uitbetaling twee keer ophalen of "opnieuw boeken" geeft geen dubbele boeking (vervangen per sleutel).
- (e) Niets van vóór de startdatum wordt geboekt.
- (f) Boven de gratis grens: status "wacht op abonnement", geen boeking; na betalen worden ze alsnog geboekt.
- (g) Verlopen koppeling: geen boeking, balk zichtbaar, na opnieuw koppelen gaat het verder zonder gaten.
- (h) Winkel buiten NL of zonder Moneybird ziet het scherm "nog niet voor jou" en kan op de wachtlijst.

## Open punten (niet voor Daan)
- Boeken in Moneybird: als memoriaalboeking kan het via de API (`POST /{administration_id}/documents/general_journal_documents` met `general_journal_document_entries`, GEZIEN 9 nov met curl op developer.moneybird.com). Of een bankmutatie op een eigen rekening "TikTok Shop" beter aansluit op de bank, zoekt Jet uit voordat de Moneybird-kant gebouwd wordt.
- Chris: prijs en het aantal bestellingen van de gratis grens (scherm 6 hangt ervan af).
- Waar de schermen draaien: Cloudflare Workers, net als de basis (gratis plan, keuze van Jet in `producten/tiktok-shop-basis/`). Wat de TikTok App Store eist van de pagina na installeren: nog niet gemeten, volgt bij de registratieteksten.
- Testen in een echte winkel kan pas na het vroege Partner Center-account (zie `platformen/tiktok-shop/registratie.md`, kop "Na ja van Hans").

Nagekeken: controleur 9 nov 19:09 UTC, akkoord na 7 moet- en 5 kan-punten, alles verwerkt.
