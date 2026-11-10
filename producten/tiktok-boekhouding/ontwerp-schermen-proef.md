# Bouwontwerp: de schermen, deel 2 (de proef, de bon)

Jet, 10 nov 2026, versie 1 (run 05:56 UTC). Bouwt op deel 1 (`ontwerp-schermen.md` versie 3: router, sessie, csrf, winkelslot, budget van 50 per verzoek) en volgt `ontwerp.md` (stap 3 van de stroom, "Moet in de bouw" punt 1, 2 en 4, "Stijl voor de bouw") en de schetsen `kunst/2-proef.png` en `kunst/5-proef-telefoon.png`. De rekenkern bestaat al: `proef()` in `src/ophalen.ts` (eis a, nooit Moneybird).

## Wat de verkoper ziet
Kop "Zo boeken wij je uitbetalingen in Moneybird", de zin "Een proef met je laatste drie. Er gaat nog niets naar Moneybird; straks kies je zelf vanaf welke datum we boeken." Stappenteller "Stap 2 van 3". Daaronder hoogstens drie bonnen naast elkaar (op 390 breed onder elkaar), nieuwste links, en onderaan de balk "Ziet het er goed uit?" met de knop "Verder naar rekeningen" (link naar `/app/rekeningen`, tot deel 3 een eenvoudig scherm "Volgt"). De knop "Bekijk per bestelling" uit de schets komt pas met het detailscherm (deel 4); tot dan staat hij er niet.

## De bon (per `ProefAfrekening`)
- Kop: "Uitbetaling <datum>" (dag en maand in Europe/Amsterdam uit `statementTime`) en, als bekend, het aantal bestellingen. Groot: "€ 1.284,60" uit `uitbetaaldCenten`, met "op je bank gekomen". Bij PROCESSING in plaats daarvan het label "nog niet uitbetaald" (pil wacht, paars).
- Regels uit `perSoort` in de vaste volgorde van `SOORTEN` (`src/moneybird/memoriaal.ts`), alleen soorten met een bedrag, met de omschrijving uit één tabel `BON_NAMEN` in `schermen-proef.ts` (gewone woorden zoals de schets: Omzet, Kortingen, Terugbetaald, Verzendkosten, Commissie TikTok, Affiliate-commissie, Btw over kosten, Correctie van TikTok, Apart gezet). Minbedragen met een echt minteken (−), label zacht, bedrag in inkt (kan-punt Daan). Stippellijn van label naar bedrag.
- Som-streep met "Naar Moneybird" en de som van de regels zonder "Apart gezet" plus "Apart gezet" apart (de som moet gelijk zijn aan het bedrag op de bank; zo niet, dan klopt de rekenkern niet: niet tonen als "klopt" maar als "onvolledig", en een logregel `ALARM`).
- Stempel: "Klopt" (groen) als er geen verschil is; "€ 44 apart" (amber) bij een regel `verschil`, met de noot "€ 44,00 apart gezet. TikTok telt bij <n> bestellingen zelf niet goed op. Wij zetten het verschil op een tussenrekening, je omzet blijft kloppen." Rood alleen voor niet geboekt (status `onvolledig` of `fout_gegevens`): stempel "Niet te boeken" met `reden` in gewone woorden. Nergens het woord "fout" bij een verschil (Daan punt 2).
- Bedragen: één functie `euro(centen)` met `Intl.NumberFormat("nl-NL", {style: "currency", currency: "EUR"})`, toets op "€ 1.284,60" en "−€ 3,20".

## Ophalen, budget en slot
- **Route `GET /app/proef`**, alleen met een geldige sessie, TikTok, Moneybird en administratie gekoppeld (anders door naar `/app`). `GET /app` stuurt na koppelen hierheen zolang `$.koppeling` (rekeningen, deel 3) ontbreekt.
- **Onder het winkelslot** (60 s, `onderSlot` uit `moneybird.ts`, verplaatst naar `basis.ts`), TikTok-tokens via `TokenBron.met` (vers gelezen, ververst bij een 401). Slot bezet: "Even geduld". Moneybird wordt niet aangeroepen en de proef krijgt geen Moneybird-client (toets met een nagebootste Moneybird die bij elk verzoek faalt).
- **`proef()` krijgt de `D1Opslag` van de winkel** met reserve 0. `haalSamen` bewaart opgehaalde transacties per afrekening (een dag geldig), dus een tweede opening gaat verder waar de eerste stopte. Is `nogBezig` true: staat "Uitbetalingen ophalen" uit `4-staten.png` met "<k> van <n> opgehaald" en `<meta http-equiv="refresh" content="3">` (geen JavaScript nodig; de CSP blokkeert dat niet), hoogstens 10 keer via een teller in de query (`?poging=`), daarna de knop "Vernieuwen".
- **Niets wordt geboekt en de proef schrijft geen statussen** die de consumer als "af" kan lezen: alleen de tijdelijke opslag van transacties en bestellingen die `haalSamen` al gebruikt. Na "Zet aan" (deel 3) kiest de startdatum wat er geboekt wordt; standaard vandaag, dus deze drie niet.
- **Geen uitbetalingen:** lege staat "Nog geen uitbetalingen" met het grote merkteken, "Zodra TikTok iets uitbetaalt, staat het hier.", en toch de knop naar rekeningen (de verkoper kan alvast instellen).
- **Winkelfout** (WinkelStop: 401 na verversen, 403, 429, 5xx): foutstaat van deel 1 met de juiste kant, knop rustig "Opnieuw proberen" naar `/app/proef`. Geen belofte "vanzelf opnieuw".

## Beweging
Daan wil dat de regels kort optellen en de stempel landt. Zonder JavaScript (de CSP staat geen script toe) doe ik het met CSS: de regels verschijnen na elkaar (`animation-delay`, samen onder 0,5 s) en de stempel landt daarna met een korte schaal- en draaibeweging. Optellen van het getal zelf kan niet zonder script; dat is de afwijking. Uit bij `prefers-reduced-motion`. "Alleen de eerste keer": cookie `__Host-klopt_gezien` (1 jaar, geen gegevens) zet bij een volgende opening de klasse zonder beweging.

## Bestanden
`src/web/proef.ts` (route), `src/web/schermen-proef.ts` (HTML van de bon, de balk, de lege en ophaal-staat, `BON_NAMEN`, `euro`), CSS erbij in `stijl.ts` (bon met kartelrand via `mask`, alleen de bon). `router.ts` krijgt de routes `GET /app/proef` en `GET /app/rekeningen`. Plaatjes: `schermen/maak.ts` krijgt de proef met drie bonnen (één met apart gezet bedrag, één PROCESSING), de ophaalstaat en de lege staat.

## Af als (unittests via de router, nagebootste TikTok, Moneybird en D1)
- (a) Na koppelen toont `/app/proef` drie bonnen; geen enkel verzoek naar Moneybird (de nep telt) en geen rij in `statussen` met een eindstatus.
- (b) De som op de bon is gelijk aan het bedrag op de bank, ook bij een apart gezet bedrag; bij een rekenkern die niet sluit: rood "Niet te boeken" en een `ALARM`-regel.
- (c) Amber stempel en noot bij `verschil`, groen "Klopt" zonder; nergens het woord "fout" in de bonnen.
- (d) PROCESSING krijgt "nog niet uitbetaald" en geen groot bedrag.
- (e) Budget op midden in de tweede afrekening: ophaalstaat met meta refresh; de volgende opening haalt niets opnieuw op wat al bewaard is (fetch-teller) en toont alle drie.
- (f) Slot bezet: "Even geduld", geen verzoek. 401 van TikTok: één keer verversen, dan opnieuw; tweede 401: foutstaat TikTok.
- (g) Geen uitbetalingen: lege staat met de knop naar rekeningen.
- (h) Zonder sessie, of zonder Moneybird of administratie: uitgelogd of door naar `/app`.
- (i) `euro()` geeft "€ 1.284,60" en "−€ 3,20"; regels in de volgorde van `SOORTEN`.
- (j) Kopregels, geen inline stijl, geen script; `prefers-reduced-motion` zet de beweging uit (CSS bevat de media-query).
- (k) Elke opening blijft binnen het budget van 50.

## Controleur
Ronde 1 (agent, 10 nov 06:30 UTC): **nee**, nog niet bouwen. Te verwerken in versie 2 (volgende run van Jet):
1. Opslag tussen openingen werkt zo niet: `D1Opslag` schrijft transacties pas weg via `klaar()`, en met `Budget.reserve` 0 is de pot op 0 en gooit `klaar()` en het slot teruggeven `BudgetOp`. Oplossing: `c.budget.reserve = 2` in de route, `opslag.klaar()` in `doe()` ook bij `nogBezig`; "reserve 0" in dit ontwerp gaat over `OphaalOpties`. Toets over twee routeraanroepen.
2. Privacy: rijen van de proef in `transacties` en `bestellingen` krijgen nooit een status en blijven staan. Oplossing: de cron ruimt begrensd op (ouder dan een dag, zonder status of met een afgeronde status). Toets erbij.
3. Som-regel: een som die afwijkt van de bank is gewoon (payable tegen total_settlement, RESERVE, kop-verschil) en wordt geboekt met een waarschuwing. Dus "Naar Moneybird" is de som van alle `perSoort` inclusief "Apart gezet", en een afwijking van `uitbetaaldCenten` is de amber staat "€ x open" uit `4-staten.png`, zonder ALARM. Ontbreekt `uitbetaaldCenten`: geen groot bedrag, amber notitie.
4. `ProefAfrekening` mist het aantal bestellingen en het aantal bestellingen met een verschil (`apartBij`); netto +3 en −3 gaf ten onrechte "Klopt". Kleine uitbreiding van `proef()` en `samenstel.ts`, met toets.
5. `BON_NAMEN` moet een naam hebben voor alle 15 soorten uit `SOORTEN`, met toets.
6. Meta refresh in `<body>` is ongeldig en telt `poging` niet op. Oplossing: kopregel `refresh: 3; url=/app/proef?poging=<n+1>`, `poging` als geheel getal 0 tot 10.
Kan-punten: vaste zin per reden bij rood (geen ruwe `reden`), 429 als "Even geduld", `Ontkoppeld` als uitgelogd scherm, bron van "k van n" vastleggen, toetsen (a) en (k) scherper, cookie `gezien` pas na de bonnen, geen bestelnummers in de reden.
