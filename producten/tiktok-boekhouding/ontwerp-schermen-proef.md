# Bouwontwerp: de schermen, deel 2 (de proef, de bon)

Jet, 10 nov 2026, versie 2 (run 05:56 UTC; versie 2 verwerkt de 6 moet-punten en de kan-punten van controleur ronde 1, zie onderaan). Bouwt op deel 1 (`ontwerp-schermen.md` versie 3: router, sessie, csrf, winkelslot, budget van 50 per verzoek) en volgt `ontwerp.md` (stap 3 van de stroom, "Moet in de bouw" punt 1, 2 en 4, "Stijl voor de bouw") en de schetsen `kunst/2-proef.png` en `kunst/5-proef-telefoon.png`. De rekenkern bestaat al: `proef()` in `src/ophalen.ts` (eis a, nooit Moneybird).

## Wat de verkoper ziet
Kop "Zo boeken wij je uitbetalingen in Moneybird", de zin "Een proef met je laatste drie. Er gaat nog niets naar Moneybird; straks kies je zelf vanaf welke datum we boeken." Stappenteller "Stap 2 van 3". Daaronder hoogstens drie bonnen naast elkaar (op 390 breed onder elkaar), nieuwste links, en onderaan de balk "Ziet het er goed uit?" met de knop "Verder naar rekeningen" (link naar `/app/rekeningen`, tot deel 3 een eenvoudig scherm "Volgt"). De knop "Bekijk per bestelling" uit de schets komt pas met het detailscherm (deel 4); tot dan staat hij er niet.

## De bon (per `ProefAfrekening`)
- Kop: "Uitbetaling <datum>" (dag en maand in Europe/Amsterdam uit `statementTime`) en "<n> bestellingen" uit het nieuwe veld `bestellingen`. Groot: "€ 1.284,60" uit `uitbetaaldCenten`, met "op je bank gekomen". Bij PROCESSING in plaats daarvan het label "nog niet uitbetaald" (pil wacht, paars). Ontbreekt `uitbetaaldCenten` (payable leeg): geen groot bedrag, amber notitie "TikTok gaf voor deze uitbetaling geen bedrag op de bank door."
- Regels uit `perSoort` in de vaste volgorde van `SOORTEN` (`src/moneybird/memoriaal.ts`), alleen soorten met een bedrag, met de omschrijving uit één tabel `BON_NAMEN` in `schermen-proef.ts` met een naam voor **elk** van de 15 soorten (Omzet, Kortingen, Terugbetaald, Korting terug, Overige omzet, Omzet (totaal), Verzendkosten, Verzendkosten (totaal), Commissie TikTok, Affiliate-commissie, Btw over kosten, Belasting, Kosten en belasting (totaal), Correctie van TikTok, Apart gezet); toets "elke soort heeft een naam". Minbedragen met een echt minteken (−), label zacht, bedrag in inkt. Stippellijn van label naar bedrag.
- Som-streep met "Naar Moneybird" = de som van **alle** `perSoort`, inclusief "Apart gezet" (gelijk aan `totaalCenten` van het memoriaal, zoals de schets).
- Stempel en noot:
  - Groen "Klopt": `apartBij` = 0 en de som gelijk aan `uitbetaaldCenten`.
  - Amber "€ 44 apart" bij `apartBij` > 0 (nieuw veld: aantal bestellingen met een verschilregel, dus ook bij netto 0 door +3 en −3), noot "€ 44,00 apart gezet. TikTok telt bij <apartBij> bestellingen zelf niet goed op. Wij zetten het verschil op een tussenrekening, je omzet blijft kloppen." Het bedrag op de stempel is de som van de absolute verschillen per bestelling (nieuw veld `apartCenten`), zodat +3 en −3 als "€ 6 apart" staat.
  - Amber "€ 2,80 open" als de som afwijkt van `uitbetaaldCenten` (payable tegen total_settlement, RESERVE, kop-verschil): regel "Open, niet geboekt −2,80" en noot zoals `4-staten.png`: "Kijk het na in Seller Center; wij boeken alleen wat we kunnen verklaren." Gewone logregel, geen ALARM, want het memoriaal boekt dan ook met alleen een waarschuwing.
  - Rood "Niet te boeken" alleen bij status `onvolledig` of `fout_gegevens`, met een vaste zin per soort reden (te groot, transacties niet opgehaald, gegevens kloppen niet), nooit de ruwe `reden` en nooit bestelnummers.
  Is een bon zowel apart gezet als open, dan wint de stempel "open" en staat de noot van apart gezet eronder. Bij +3 en −3 (netto 0) blijft de regel "Apart gezet 0,00" staan, met in de noot "per bestelling".
  Nergens het woord "fout" bij een verschil (Daan punt 2).
- **Kleine uitbreiding rekenkern:** `proef()` geeft per afrekening ook `bestellingen` (uit `Samenstelling.bestellingen`), `apartBij` en `apartCenten` door; `samenstel.ts` telt die bij het maken van de verschilregels. Eigen toetsen in `test/samenstel.test.ts` en `test/verwerk.test.ts`.
- Bedragen: één functie `euro(centen)` met `Intl.NumberFormat("nl-NL", {style: "currency", currency: "EUR"})`, toets op "€ 1.284,60" en "−€ 3,20".

## Ophalen, budget en slot
- **Route `GET /app/proef`**, alleen met een geldige sessie, TikTok, Moneybird en administratie gekoppeld (anders door naar `/app`). `GET /app` stuurt na koppelen hierheen zolang `$.koppeling` (rekeningen, deel 3) ontbreekt.
- **Onder het winkelslot** (60 s, `onderSlot` uit `moneybird.ts`, verplaatst naar `basis.ts`), TikTok-tokens via `TokenBron.met` (vers gelezen, ververst bij een 401). Slot bezet: "Even geduld". Moneybird wordt niet aangeroepen en de proef krijgt geen Moneybird-client (toets met een nagebootste Moneybird die bij elk verzoek faalt).
- **`proef()` krijgt de `D1Opslag` van de winkel**, met `OphaalOpties.reserve` 0 (dat is de reserve binnen het ophalen) maar `c.budget.reserve = 2` in de route (1 voor `opslag.klaar()`, 1 om het slot terug te geven). Binnen `doe()` roept de route na `proef()` altijd `opslag.klaar()` aan, ook als `nogBezig` true is, zodat de opgehaalde transacties en bestellingen echt in D1 staan; de volgende opening gaat verder waar de eerste stopte. Client: `snelleTikTok` (1 poging); een 429 geeft "Even geduld" in plaats van de foutstaat.
- **Ophaalstaat:** is `nogBezig` true, dan de staat "Uitbetalingen ophalen" uit `4-staten.png` met "<k> van <n> opgehaald" (k = afrekeningen niet `bezig_met_ophalen`, n = `afrekeningen.length`; staat de lijst zelf nog niet binnen, dan zonder getallen) en de kopregel `refresh: 3; url=/app/proef?poging=<p+1>` (p is de pogingteller, niet de n van "k van n"; via `kopregels`, geldig zonder iets in `<head>`, de CSP raakt het niet). `poging` wordt gelezen als geheel getal van 0 tot 10; bij 10 geen refresh meer maar de knop "Vernieuwen".
- **Opruimen (privacy):** rijen die de proef bewaart krijgen nooit een status als de startdatum later ligt. Daarom ruimt de cron (`src/d1/opruimen.ts`) per keer begrensd (`rowid IN (SELECT ... LIMIT 500)`) rijen in `transacties` en `bestellingen` op met `opgehaald_op` ouder dan een dag, als er voor die afrekening geen status is of de status af is: de lijst `AF` uit `opslag.ts` plus `wacht_ouder`, zonder `opnieuw_sinds`. Rijen bij `wacht_op_abonnement`, `bezig_met_ophalen`, `onvolledig` en `onzeker` blijven staan; `fout` en `fout_gegevens` volgen het opruimen uit ontwerp-d1-worker.md punt 3. Open afrekeningen blijven staan. Zo geldt weer "alleen bewaren tot de afrekening af is" (ontwerp-d1-worker.md punt 3).
- **`Ontkoppeld`** uit `TokenBron` geeft het scherm "uitgelogd" met wissen van het sessie-cookie, geen 500.
- **Niets wordt geboekt en de proef schrijft geen statussen** die de consumer als "af" kan lezen: alleen de tijdelijke opslag van transacties en bestellingen die `haalSamen` al gebruikt. Na "Zet aan" (deel 3) kiest de startdatum wat er geboekt wordt; standaard vandaag, dus deze drie niet.
- **Geen uitbetalingen:** lege staat "Nog geen uitbetalingen" met het grote merkteken, "Zodra TikTok iets uitbetaalt, staat het hier.", en toch de knop naar rekeningen (de verkoper kan alvast instellen).
- **Winkelfout** (WinkelStop: 401 na verversen, 403, 5xx; 429 is "Even geduld"): foutstaat van deel 1 met de juiste kant, knop rustig "Opnieuw proberen" naar `/app/proef`. Geen belofte "vanzelf opnieuw".

## Beweging
Daan wil dat de regels kort optellen en de stempel landt. Zonder JavaScript (de CSP staat geen script toe) doe ik het met CSS: de regels verschijnen na elkaar (`animation-delay`, samen onder 0,5 s) en de stempel landt daarna met een korte schaal- en draaibeweging. Optellen van het getal zelf kan niet zonder script; dat is de afwijking. Uit bij `prefers-reduced-motion`. "Alleen de eerste keer": cookie `__Host-klopt_gezien` (1 jaar, geen gegevens), pas gezet als de bonnen echt getoond zijn (niet bij de ophaalstaat), zet bij een volgende opening de klasse zonder beweging.

## Bestanden
`src/web/proef.ts` (route), `src/web/schermen-proef.ts` (HTML van de bon, de balk, de lege en ophaal-staat, `BON_NAMEN`, `euro`), CSS erbij in `stijl.ts` (bon met kartelrand via `mask`, alleen de bon). `router.ts` krijgt de routes `GET /app/proef` en `GET /app/rekeningen`. Plaatjes: `schermen/maak.ts` krijgt de proef met drie bonnen (één met apart gezet bedrag, één PROCESSING), de ophaalstaat en de lege staat.

## Af als (unittests via de router, nagebootste TikTok, Moneybird en D1)
- (a) Na koppelen toont `/app/proef` drie bonnen; geen enkel verzoek naar Moneybird (de nep telt), geen enkele rij in `statussen`, `markering` en `volgende_run` ongewijzigd.
- (b) "Naar Moneybird" is de som van alle regels inclusief "Apart gezet"; wijkt die af van `uitbetaaldCenten`: amber "open" met regel en noot, geen ALARM; zonder `uitbetaaldCenten`: geen groot bedrag en de amber notitie.
- (c) Amber stempel en noot bij `apartBij` > 0, ook bij netto 0 (+3 en −3); groen "Klopt" zonder; nergens het woord "fout" in de bonnen; rood alleen bij `onvolledig`/`fout_gegevens`, met de vaste zin en zonder bestelnummers.
- (d) PROCESSING krijgt "nog niet uitbetaald" en geen groot bedrag.
- (e) Twee routeraanroepen op de echte nep-D1 met het volle budget: de eerste stopt midden in de tweede afrekening met de ophaalstaat en de kopregel refresh met `poging=1`; daarna staan de rijen in D1 en is de slotrij weg; de tweede haalt niets opnieuw op (fetch-teller) en toont alle drie. Bij `poging=10` geen refresh, wel "Vernieuwen".
- (f) Slot bezet: "Even geduld", geen verzoek. 429: "Even geduld". 401: één keer verversen, dan opnieuw; tweede 401: foutstaat TikTok. Winkel ontkoppeld: uitgelogd.
- (g) Geen uitbetalingen: lege staat met de knop naar rekeningen.
- (h) Zonder sessie, of zonder Moneybird of administratie: uitgelogd of door naar `/app`.
- (i) `euro()` geeft "€ 1.284,60" en "−€ 3,20"; regels in de volgorde van `SOORTEN`; elke soort heeft een naam.
- (j) Kopregels, geen inline stijl, geen script; de CSS heeft `prefers-reduced-motion`; cookie `gezien` alleen na de bonnen.
- (k) Elke opening blijft binnen het budget van 50, geen opening eindigt in de `BudgetOp`-vangst van de router, en na elke opening is de slotrij weg.
- (l) Opruimen: na de proef en een cron een dag later zijn de rijen van afrekeningen zonder status weg; die van een open afrekening (status niet af) blijven.

## Controleur
Ronde 1 (agent, 10 nov 06:30 UTC): **nee**, nog niet bouwen. Te verwerken in versie 2 (volgende run van Jet):
1. Opslag tussen openingen werkt zo niet: `D1Opslag` schrijft transacties pas weg via `klaar()`, en met `Budget.reserve` 0 is de pot op 0 en gooit `klaar()` en het slot teruggeven `BudgetOp`. Oplossing: `c.budget.reserve = 2` in de route, `opslag.klaar()` in `doe()` ook bij `nogBezig`; "reserve 0" in dit ontwerp gaat over `OphaalOpties`. Toets over twee routeraanroepen.
2. Privacy: rijen van de proef in `transacties` en `bestellingen` krijgen nooit een status en blijven staan. Oplossing: de cron ruimt begrensd op (ouder dan een dag, zonder status of met een afgeronde status). Toets erbij.
3. Som-regel: een som die afwijkt van de bank is gewoon (payable tegen total_settlement, RESERVE, kop-verschil) en wordt geboekt met een waarschuwing. Dus "Naar Moneybird" is de som van alle `perSoort` inclusief "Apart gezet", en een afwijking van `uitbetaaldCenten` is de amber staat "€ x open" uit `4-staten.png`, zonder ALARM. Ontbreekt `uitbetaaldCenten`: geen groot bedrag, amber notitie.
4. `ProefAfrekening` mist het aantal bestellingen en het aantal bestellingen met een verschil (`apartBij`); netto +3 en −3 gaf ten onrechte "Klopt". Kleine uitbreiding van `proef()` en `samenstel.ts`, met toets.
5. `BON_NAMEN` moet een naam hebben voor alle 15 soorten uit `SOORTEN`, met toets.
6. Meta refresh in `<body>` is ongeldig en telt `poging` niet op. Oplossing: kopregel `refresh: 3; url=/app/proef?poging=<n+1>`, `poging` als geheel getal 0 tot 10.
Kan-punten: vaste zin per reden bij rood (geen ruwe `reden`), 429 als "Even geduld", `Ontkoppeld` als uitgelogd scherm, bron van "k van n" vastleggen, toetsen (a) en (k) scherper, cookie `gezien` pas na de bonnen, geen bestelnummers in de reden.
Ronde 2 (zelfde agent, 06:35 UTC): **akkoord**, bouwen mag. Kan-punten 1 tot 5 (429, naam van de pogingteller, apart en open samen, netto 0, wat "af" is bij opruimen) meteen verwerkt.
