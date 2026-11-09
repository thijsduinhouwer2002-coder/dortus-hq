Akkoord: ja 9 nov 2026 21:55 UTC, voor het ontwerp van alle zes schermen (bouwen mag), nu ook scherm 3 rekeningen en btw (`kunst/6-rekeningen.png`, zie "Scherm 3" onder Oordeel Daan). Op voorwaarde dat de schermen de schetsen in `kunst/` en de punten onder "Oordeel Daan" volgen. Dit is geen akkoord voor indienen: dat geef ik pas op de echte schermen (test via GitHub Actions, plaatjes op de tak `schermen`).

Oud: Akkoord: ja 9 nov 2026 21:05 UTC, voor het ontwerp van koppelen, proef, overzicht, uitbetaling in detail en de staten (bouwen mag); scherm 3 (rekeningen en btw) wacht op mijn schets in de volgende run. Op voorwaarde dat de schermen de schetsen in `kunst/` en de punten onder "Oordeel Daan" volgen. Dit is geen akkoord voor indienen: dat geef ik pas op de echte schermen (test via GitHub Actions, plaatjes op de tak `schermen`).

Oud: Akkoord: nee (Hans zei 9 nov 20:44 ja op het product; Daan gevraagd 9 nov 20:25 UTC via taken.md, nog niet bekeken)

# Ontwerp: TikTok Shop naar je boekhouding (concept)

Tess, 9 nov 2026, run 19:03 UTC. **Concept: geldt pas na het ja van Hans** op `platformen/tiktok-shop/voorstel-boekhoudkoppeling.md` (hij beslist 9 nov 20:44 NL). Bij nee vervalt dit stuk. Geschreven vóór het besluit zodat Daan bij een ja meteen een korte, complete vraag krijgt; Daan werkt nu eerst voor Steam (bericht Thijs 19:00), dus hoe minder hij zelf hoeft uit te zoeken, hoe beter. De rekenkern staat los in `producten/tiktok-shop-basis/ontwerp-rekenkern.md` (Jet). Naam van het product: nog open (Chris en Daan); werknaam hier "de app".

## Waarom wij (bovenaan, ook op de winkelpagina)
De eerste app in de TikTok Shop App Store die je TikTok-uitbetalingen per bestelling vanzelf in je eigen lokale pakket boekt, te beginnen met Moneybird; de EU-apps nu bieden alleen DATEV, losse exports of Xero en QuickBooks (GEZIEN, zie voorstel). Tegen Schakel (doet TikTok naar Moneybird buiten de App Store, vanaf €10 per maand, GEZIEN in het voorstel): wij staan in de App Store waar verkopers zoeken, boeken per bestelling met elk verschil zichtbaar, en je ziet eerst gratis hoe je uitbetalingen geboekt worden voordat er iets in Moneybird komt. De belofte voor de verkoper: "Elke TikTok-uitbetaling netjes in Moneybird, zonder Excel, en wat niet klopt zie je meteen."

## Versie 1 (wat wel en niet)
- Wel: Nederland, Moneybird, één winkel per abonnement, uitbetalingen (afrekeningen) als memoriaalboekingen, met alle soorten uit de rekenkern elk op een eigen grootboekrekening: `omzet`, `korting`, `terugbetaling`, `korting_terug`, `overig_omzet`, `verzendkosten`, `commissie`, `belasting_op_kosten`, `belasting`, de groepstotalen `omzet_totaal`, `verzendkosten_totaal`, `kosten_en_belasting_totaal`, en `verschil` (altijd op een vaste tussenrekening, nooit omzet). Daarbij `correctie`: aanpassingen (`adjustment_amount`) en andere transacties zonder bestelling, die de product-laag uit `transactiesVanAfrekening` haalt (rekenkern, kop "Eenheid van boeken"); ook op een eigen rekening.
- Wat "klopt" betekent: per uitbetaling sluit de boeking op het bedrag dat op de bank kwam, omdat correcties meegaan. Een verschil binnen één SKU-transactie wordt geboekt op de tussenrekening; een verschil op het niveau van de hele bestelling (kop) wordt niet geboekt (zo beslist in de rekenkern) maar staat als gele waarschuwing bij die uitbetaling, met het bedrag.
- Btw: geen eigen berekening; de gebruiker kiest per soort een Moneybird-btw-tarief (met een voorstel, bijvoorbeeld "geen btw" voor uitbetaling en verschil).
- Niet in versie 1: Exact (Developer-abonnement €15 per maand, GEZIEN, zie voorstel), Pennylane en Fatture in Cloud, meerdere winkels in één scherm, andere talen dan NL en EN. Prijs: gratis proef en gratis grens (werkwaarde 30 bestellingen per maand), daarna €15 per maand per winkel (GOK, werkprijs; Chris maakt prijs en gratis grens). Uitgewerkt in `platformen/tiktok-shop/plan-betalen.md` (Tess, 9 nov 21:12 UTC), dat gaat voor bij betalen.

## Wat de verkoper doet, stap voor stap
1. **Installeren** in de TikTok Shop App Store; TikTok vraagt toestemming en stuurt de verkoper naar ons koppel-adres (`https://dortus.com/<product>/koppel`, naam volgt). Dat dit zo loopt en met de scope Finance Information is GOK tot we een app in Partner Center hebben.
2. **Moneybird koppelen** (inloggen bij Moneybird, toestemming geven) en de administratie kiezen. Geen Moneybird: een scherm "versie 1 werkt alleen met Moneybird", met een knop om op de wachtlijst voor Exact te komen (zo meten we de vraag). Winkel buiten NL of een andere munt dan EUR: zelfde soort scherm, "nu alleen voor Nederlandse winkels", met wachtlijst per land.
3. **Gratis proef zonder boeken:** de app haalt meteen de laatste 3 uitbetalingen op en laat zien hoe die geboekt zouden worden, met de verschillen. Er gaat nog niets naar Moneybird. Dit moment moet overtuigen, dus dit scherm krijgt de meeste zorg.
4. **Rekeningen en btw kiezen:** per soort een grootboekrekening en een btw-tarief in Moneybird, met een voorstel (of dat voorstel meestal klopt is GOK, eerst testen met een echte Moneybird-sandbox). Ontbreekt een rekening, dan maakt de app hem met één klik aan. Plus een **startdatum**: alleen uitbetalingen vanaf die datum worden geboekt, ook de proef-uitbetalingen als ze erna vallen. Standaard is de dag van vandaag, zodat wat de verkoper al met de hand boekte niet dubbel komt; vroeger kiezen kan, met de waarschuwing "boek je deze al zelf? kies dan een latere datum".
5. **Aanzetten:** vanaf nu boekt de app elke nieuwe uitbetaling vanzelf. Een uitbetaling met een verschil of waarschuwing wordt wel geboekt en staat bovenaan met een gele markering.
6. **Betalen:** boven de gratis grens boekt de app niet meer verder (status "wacht op abonnement"), haalt wel op, en boekt na betalen de wachtende uitbetalingen van de lopende en de vorige maand; oudere blijven wachten (begrensd inhalen, zie `plan-betalen.md`). Afrekenen via Polar, het account dat Dortus al heeft.

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


## Oordeel Daan (9 nov 2026, 20:55 UTC)

**Kort:** goed ontwerp, de stroom klopt en de proef-zonder-boeken is de juiste haak. Akkoord voor bouwen. Schetsen van vijf schermen staan in `kunst/` (bron `kunst/maak.py`, HTML erbij, zelf bekeken met Read): `1-koppelen.png`, `2-proef.png`, `3-overzicht.png`, `4-staten.png` (leeg, laden, fout, nog niet voor jou), `5-proef-telefoon.png`. Bedragen in de schetsen tellen echt op (nagerekend).

**Wat ons onderscheidt, in één zin (uiterlijk):** de concurrenten (A2X, Link My Books, Schakel) tonen een tabel met getallen; wij tonen elke uitbetaling als een **bonnetje dat zichtbaar optelt tot het bedrag op je bank, met een stempel "Klopt"**. Dat bonnetje met stempel is het eigen gezicht: in de app, in het icoon en op het eerste winkelplaatje.

### Antwoorden op de vragen
1. **Computer eerst, telefoon moet werken.** Boekhouden en Moneybird gebeuren op de computer (GOK, maar Moneybird zelf is een webapp voor de computer). Breedte 1280 is het ontwerp; op 390 px vallen de bonnen onder elkaar en blijft alles leesbaar (`5-proef-telefoon.png`). Geen aparte telefoonversie.
2. **Proef: kaarten, geen tabel.** Elke kaart is een bonnetje: bovenaan groot het bedrag op de bank, daaronder de regels per soort met stippellijn naar het bedrag, dikke streep, "Geboekt" met hetzelfde bedrag. Wie het ziet, snapt zonder uitleg dat het sluit. Het overzicht (dagelijks gebruik) is wel een tabel: daar wil je veel uitbetalingen tegelijk zien.
3. **Verschil zonder eng te ogen:** amber, nooit rood. Rood is alleen voor iets wat niet geboekt is (fout, verlopen koppeling). Woorden: "apart gezet", niet "verschil" of "fout". Een amber stempel "€ 44 apart" en één notitie in gewone woorden eronder: wat er gebeurde, dat het op een tussenrekening staat en dat de omzet klopt. In het overzicht de status "Geboekt, € 44 apart" en een tegel "Apart gezet, nog na te kijken". Een kop-verschil dat niet geboekt wordt: dezelfde amber notitie, met "niet geboekt, kijk even na".
4. **Leeg, laden, fout:** zie `4-staten.png`. Altijd: het eigen teken of één rustig symbool groot, één vette zin, één zin uitleg, hoogstens één knop. Laden met een echte teller ("2 van 3 opgehaald"), geen draaiend rondje zonder einde. Bij een fout van TikTok of Moneybird zeggen we dat het niet aan de verkoper ligt en dat we het vanzelf opnieuw proberen.
5. **Naam en icoon (met Chris):** werknaam **Klopt** (sluit aan op de stempel en op de belofte "wat niet klopt zie je meteen"; kort, Nederlands, want versie 1 is voor Nederland). Niet "Tally": dat is al een bekend formulierenmerk (tally.so). Chris toetst de naam op merken en in de App Store voor hij vastligt; tot dan is "Klopt" werknaam. Icoon: een paars bonnetje met kartelrand en een wit vinkje (`TEKEN` in `maak.py`), leest op 30 px; op 16 px alleen bonnetje en vinkje.
6. **Plaatjes voor de App Store:** eerste plaatje is een poster met de drie bonnen uit de proef (één amber), kop "Elke TikTok-uitbetaling netjes in Moneybird". Maak ik zodra er echte schermen zijn; eerlijk tonen wat de app doet.

### Stijl voor de bouw (vast, Jet volgt dit)
- **Kleuren:** papier `#F5F3EE` (achtergrond), kaart wit, inkt `#17161C`, zacht `#6B6875`, lijn `#E4E1DA`. Eén accent: paars `#4F3BD1` (alleen voor de hoofdknop, links en het merk). Paars, omdat het niet botst met roze en cyaan van TikTok of blauw van Moneybird, en niet met de signaalkleuren. Signalen: goed `#0B6E3F` op `#E3F5EA`, apart amber `#9A5B00` op `#FFF3D6`, fout `#C2261F` op `#FDE8E6`, wacht paars op `#ECE9FF`. Alles boven 4,5:1 contrast voor tekst (te meten in de echte build).
- **Letter:** Inter (vrij te gebruiken, SIL OFL), op het web zelf meegeleverd. Bedragen altijd met `font-variant-numeric: tabular-nums`, rechts uitgelijnd, minbedragen in de zachte kleur met een echt minteken (−), euro als "€ 1.284,60".
- **Vormen:** kaarten met ronde hoek 14 px, knoppen 10 px, statuslabels als pil. De bon heeft geen ronde hoek maar een kartelrand onderaan; alleen de bon, nergens anders.
- **Eén beweging, met betekenis:** bij het openen van de proef tellen de regels van elke bon kort op (onder 0,5 s) en daarna landt de stempel met een kleine klap. Alleen de eerste keer, uit bij `prefers-reduced-motion`. Verder geen bewegingen.
- **Teksten:** kort, gewone woorden, geen uitroeptekens. Knop zegt wat er gebeurt ("Koppel Moneybird", "Verder naar rekeningen"). Nederlands en Engels (Engelse tekst volgt met Chris).
- **Logo's van TikTok Shop en Moneybird:** in de schetsen staan letters als plaatsvervanger. In de echte app de officiële logo's volgens hun merkregels, of alleen de naam als de regels dat eisen. Nooit zelf nagetekend.

### Moet in de bouw (op volgorde)
1. **De bon** zoals in `2-proef.png`: bedrag op de bank groot bovenaan, regels met stippellijn, som-streep, stempel. Dit scherm moet overtuigen; het krijgt de meeste zorg.
2. **Amber voor apart gezet, rood alleen voor niet geboekt.** Nergens het woord "fout" bij een verschil.
3. **Overzicht** zoals `3-overzicht.png`: kop met de koppelingen en hun staat (groene of rode stip), balk bij verlopen koppeling, drie tegels, tabel nieuwste boven. Bij "wacht op abonnement" staat de gratis teller vol en de link naar het abonnement met de prijs erop (geen schreeuwende knop).
4. **Staten** zoals `4-staten.png`, voor elk scherm dat iets ophaalt.
5. **Scherm 3, rekeningen en btw** (niet geschetst, volgt de stijl): één rij per soort, links de soort in gewone woorden met één regel uitleg ("Commissie TikTok: wat TikTok per bestelling inhoudt"), rechts twee keuzelijsten. Voorstel al ingevuld en met een klein label "voorgesteld". "Apart gezet" staat vast op de tussenrekening en is niet te kiezen (grijs, met slotje en uitleg). Startdatum bovenaan, met de waarschuwing in amber als hij in het verleden ligt.
6. **Telefoon:** alles in één kolom, knoppen over de volle breedte, kop zonder de koppelingen.

### Wat ik keur voor het akkoord voor indienen
De echte schermen in een browser via GitHub Actions (Playwright, 1280 en 390 breed), met nagebootste TikTok- en Moneybird-antwoorden: koppelen, proef met één uitbetaling met apart gezet bedrag, rekeningen, overzicht met elke status, en de vier staten. Plaatjes openbaar op de tak `schermen` (map `tiktok-boekhouding/<tak>/`), zoals bij Rollwright. Plus naam, icoon en de App Store-plaatjes.

### Controleur (agent, 9 nov 21:00 UTC) en wat ik veranderde
Oordeel controleur: nee op versie 1 van de schetsen (ontwerp sterk, bon met stempel onderscheidend, bedragen kloppen), 8 moet-punten. Verwerkt in versie 2, zelf bekeken met Read:
1. Gratis teller en status kloppen nu: november heeft 42 bestellingen tegen een grens van 30 (grens en € 15 zijn GOK tot Chris beslist).
2. **Volgorde van staten vastgelegd:** koppeling verlopen gaat voor abonnement, dus de uitbetaling van 6 nov staat op "Wacht op koppeling"; de ondertitel zegt nu "Boeken staat stil tot je Moneybird opnieuw koppelt". Volgorde voor de bouw: fout > koppeling verlopen > wacht op abonnement > geboekt met apart > geboekt.
3. Op de bon staat "Naar Moneybird" in plaats van "Geboekt": in de proef is er nog niets geboekt. In het detailscherm na boeken mag het wel "Geboekt" heten.
4. Kop proef nu "Zo boeken wij je uitbetalingen in Moneybird", met de zin dat je zelf de startdatum kiest (de standaard is vandaag, dus deze drie komen er niet vanzelf in).
5. **Kop-verschil geschetst** (onderaan `4-staten.png`): som "Naar Moneybird" wijkt af van de bank, daaronder in amber "Open, niet geboekt" met het bedrag, stempel "€ 2,80 open" en een notitie met het bestelnummer en waar je het nakijkt. Zo blijft de bon eerlijk sluiten.
6. Groen donkerder (`#0B6E3F`), haalt nu ook op het groene vlak 4,5:1 (controleur mat 3,88:1 bij het oude groen).
7. Scherm 3 (rekeningen en btw): terecht, nog niet geschetst. Volgende run, vóór Jet dat scherm bouwt. Opzet: de groepstotalen niet als losse rij (die volgen uit de soorten), soorten die zelden voorkomen (korting terug, overig omzet, correctie) ingeklapt onder "meer soorten", "Apart gezet" vast met slotje.
8. **Beloftes in de staten moeten echt waar zijn:** "2 van 3 opgehaald" alleen als de bouw de voortgang echt telt, "we proberen het over 5 minuten vanzelf opnieuw" alleen als de bouw dat echt doet; anders de zin weglaten. Lege staat zegt nu alleen "Zodra TikTok iets uitbetaalt, staat het hier" (geen "al geboekt", geen gok over wekelijks).
Kan-punten: vlag-emoji vervangen door "NL" in een rondje (Windows toont geen vlag), minbedragen nu in inkt en alleen het label zacht (commissie moet je zien), tegel "Apart gezet, alles open". Nog open (kan): één doorlopende stappenteller over koppelen, administratie kiezen, proef, rekeningen, aanzetten; de tegel apart gezet klikbaar naar die uitbetalingen.

### Scherm 3, rekeningen en btw (Daan, 9 nov 2026, 21:55 UTC)
Schetsen: `kunst/6-rekeningen.png` (versie 1: btw splitsen staat uit), `kunst/6b-rekeningen-met-btw.png` (later, na de btw-test in de sandbox), `kunst/6c-rekeningen-telefoon.png` (390 breed). Bron: functie `rekeningen` in `kunst/maak.py`.

**Opbouw:** startdatum bovenaan (amber notitie als hij in het verleden ligt), daaronder in versie 1 een paarse info-regel "Btw splitsen we nog niet", dan één rij per soort: links de soort met één regel uitleg, rechts de keuzelijst met daaronder een label. Groepstotalen staan er niet als rij. Zeldzame soorten (korting terug, overige omzet, correctie) zitten ingeklapt onder "Meer soorten". De tegenrekening "Te ontvangen van TikTok Shop" als eigen kaart, met uitleg hoe je de bankregel koppelt. Onderaan de balk met wat "Zet aan" echt doet.

**Moet in de bouw (Jet):**
1. **Labels alleen als het waar is.** "gevonden in je Moneybird" (grijze pil) alleen als de app de rekening echt vond (op naam of RGS-code, zie `rgs-codes.md`); "+ nieuw, maken we aan" (groene pil) alleen voor wat ontbreekt. Rekeningnummer alleen tonen bij een rekening die al bestaat; de app stuurt geen nummer mee bij aanmaken.
2. **Namen gelijk aan `src/moneybird/rgs.ts`** (eindigen op "TikTok Shop"), zodat de verkoper ze in Moneybird terugkent.
3. **De balk telt echt:** "We maken N rekeningen aan en boeken meteen M uitbetalingen vanaf <startdatum>. Daarna elke nieuwe vanzelf." N = wat ontbreekt (ook wat onder "Meer soorten" zit), M = uitbetalingen vanaf de startdatum die al binnen zijn. Is M nul: alleen "Daarna boeken we elke nieuwe uitbetaling vanzelf."
4. **Btw over kosten:** amber label "kies met je boekhouder", nooit "voorgesteld" (of TikTok NL-btw rekent is GOK). De info-regel zegt dat ook.
5. **Apart gezet** vast (slotje, gestippelde rand, grijs), pil "vast", uitleg als gewone zachte tekst eronder.
6. **Uitleg per soort** zoals in de schets; let op: verzendkosten is "Wat TikTok voor verzending inhoudt" (kosten, geen omzet).
7. **Voorwaarde:** "+ nieuw, maken we aan" mag pas live als het aanmaken gebouwd en getest is en de koppeling de scope `settings` vraagt (zichtbaar in scherm 1). Lukt dat niet in versie 1, dan toont dit scherm alleen bestaande rekeningen, met een lege keuzelijst en de tekst "Maak deze rekening eerst aan in Moneybird" waar er een ontbreekt.
8. Btw-kolom (6b) pas tonen na de btw-test; de tarieven daar zijn voorbeelden (GOK), geen voorstel.

**Controleur (agent, 21:45 UTC):** nee op versie 1, 7 moet-punten: aantal nieuwe rekeningen fout (correctie vergeten), namen anders dan de bouw, verzonnen rekeningnummers, uitleg verzendkosten fout, "Zet aan" zei niet dat de oude uitbetalingen meteen geboekt worden, Voorbelasting als "voorgesteld" terwijl dat GOK is, en de voorwaarde over aanmaken en scope. Alle zeven verwerkt in versie 2 (zelf bekeken met Read, licht en telefoon), plus kan-punten: "voorgesteld" grijs in plaats van paars, labels 12 px, lange pil op de telefoon opgesplitst. Niet gedaan: uitleg waarom "geen btw" bij apart gezet in 6b (komt pas na de btw-test).
