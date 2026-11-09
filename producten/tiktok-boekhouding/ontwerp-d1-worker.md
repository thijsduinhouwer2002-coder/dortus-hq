# Ontwerp: opslag in D1 en de Worker (bouwstuk 4)

Jet, 9 nov 2026, versie 2 (22:20 UTC) na controleur ronde 1 (7 moet-punten, zie onderaan). Hoort bij `ontwerp-productlaag.md` (kop "Slot en opslag") en de vondst van 21:19 UTC in `platformen/tiktok-shop/taken.md`. Bronnen, GEZIEN 9 nov 22:10 UTC met curl (controleur las ze ook): developers.cloudflare.com `workers/platform/limits` (gratis: 10 ms CPU per aanroep, ook cron en consumer; 50 subrequests per aanroep, "any request ... to Cloudflare services like ... D1"; aparte regel "subrequests to internal services 1,000"; 5 cron triggers), `d1/platform/limits` en pricing (gratis: 50 queries per aanroep, `db.batch()` telt als één en is een transactie; 500 MB per database; 5 miljoen gelezen en 100.000 geschreven rijen per dag; rij hoogstens 2 MB), `queues/platform/pricing` en limits (gratis: 10.000 bewerkingen per dag, ±3 per bericht, 24 uur bewaard; minstens één keer afgeleverd).

## Waarom wij (voor dit stuk)
Alles op het gratis plan van Cloudflare, zonder geld van Thijs, en toch veilig: geen boeking dubbel, niets kwijt als een aanroep halverwege stopt.

## Eén pot van 50 (GOK, veilige lezing)
Of fetch en D1 elk 50 hebben of samen 50 delen staat niet eenduidig in de docs. Ontwerp gaat uit van **samen 50**: het bestaande `Budget` uit `src/budget.ts` telt voortaan fetch én D1-queries (batch is één). Meten in Cloudflare komt bij de uitrol. Blijkt het twee potten, dan alleen de startwaarde aanpassen.
- **Nieuw werk weigert, afmaken nooit.** Het budget weigert (fout `budgetOp`, niets verstuurd) alleen bij nieuw werk: externe leesverzoeken, D1-leesacties en `neemSlot`. Schrijven (status, wachtrij, markering, `geefSlotTerug`, `klaar()`) gaat altijd door; daarvoor ligt een **vaste reserve van 6** vast die nieuw werk niet mag aanspreken.
- **Vóór het boeken** moet er nog minstens de Moneybird-reserve (12, bestaand) plus deze 6 over zijn, anders stopt de run netjes vóór de boeking. De startwaarde blijft 45 + D1, dus in de praktijk 2 tot 4 afrekeningen per aanroep in plaats van 6; meer aanroepen is goedkoop (zie Worker).

## Wat het doet
**1. Kleine wijziging in `verwerk.ts`: "boeking gestart".** Vlak vóór `boekAfrekening`, in dezelfde batch als de controle van het slot, wordt de status `onzeker` met reden `boeking gestart` (het bewaarde `documentId` blijft). Na de boeking komt de echte status. Stopt de aanroep ertussen (CPU-grens 1102, D1-fout, afbreken), dan vangt de bestaande regel het op: 10 minuten wachten, dan zoeken op kenmerk (de sandbox liet zien dat zoeken exact is). Geeft `boekAfrekening` `budgetOp` (niets verstuurd), dan komt de oude status terug. De `GeheugenOpslag`-toetsen gelden ook hiervoor.

**2. `D1Opslag` (`src/d1/opslag.ts`)**, de echte versie van de interface `Opslag`, één exemplaar per winkel:
- `leesStatus` leest **alleen de status, altijd vers** (één query), want `verwerk.ts` leest hem na het slot opnieuw.
- **`neemSlot` maakt het geheugen van die afrekening leeg.** De eerste `leesTransacties` of `leesBestelling` daarna haalt in één batch de transacties en alle bewaarde bestellingen van die afrekening op; volgende leesacties komen uit het geheugen. Afrekeningen die geboekt zijn of wachten laden dus niets.
- `schrijfBestelling` en `schrijfTransacties` gaan in een wachtrij én meteen in het geheugen (eigen schrijfacties terug te lezen). Elke `schrijfStatus`, `schrijfMarkering`, `slotTot` en `geefSlotTerug` stuurt de wachtrij mee in dezelfde batch (alles of niets). Zo staat alles wat opgehaald is vast vóór elke statuswissel en vóór de slotcontrole voor het boeken. `klaar()` schrijft de rest.
- **Slot:** `INSERT INTO sloten ... ON CONFLICT(winkel, statement_id) DO UPDATE SET eigenaar = excluded.eigenaar, tot = excluded.tot WHERE sloten.tot <= :nu OR sloten.eigenaar = excluded.eigenaar`; genomen als `meta.changes = 1` (door de controleur nagespeeld in SQLite). `slotTot` leest vers.
- Teller `schrijfacties` zoals `GeheugenOpslag`, voor de bestaande toetsen.
- **Read replication blijft uit**, zodat alles de hoofddatabase leest.

**3. Bewaren en opslag.** Bewaarde bestellingen en transacties gaan weg **zodra een afrekening af is** (geboekt, leeg, `wacht_op_abonnement` niet: die moet nog boeken). `verwerk.ts` leest ze daarna niet meer; opnieuw boeken haalt opnieuw op en scherm 5 haalt zelf op. Bewaard wordt alleen wat `boekingsregels` en `samenstel` gebruiken (geen hele antwoorden). Een rij boven 1,5 MB wordt niet bewaard en de afrekening wordt `onvolledig` "te groot" (bestaande uitweg). **Statussen gaan nooit weg**: die voorkomen herboeken. Opruimen van rijen van afgeronde afrekeningen die bleven staan: één query per cron met `WHERE rowid IN (SELECT ... LIMIT 500)` (D1 kent geen `DELETE ... LIMIT`).
**Capaciteit**, het kleinste van: queue-bewerkingen (10.000 per dag, ±3 per bericht, ±3.300 aanroepen), geschreven rijen (100.000 per dag; per afrekening met 30 bestellingen ±70 inclusief indexen en weggooien) en opslag (alleen open afrekeningen, ruim onder 500 MB). Bij gemiddeld 1 afrekening per winkel per dag en 6 aanroepen per winkel per dag: ±500 winkels door de queue, ±1.400 door de rijen. Grens dus ±500 winkels; daarvoor zijn er betalende klanten en is Workers Paid ($5 per maand) gedekt.

**4. Tabellen (`schema.sql`).** `winkels` (id, TikTok shop_id en shop_cipher, versleutelde tokens met verloopmomenten en `token_versie`, Moneybird-administratie, instellingen als JSON, markering, winkelfout, `volgende_run`, `snel_teller`), `sloten`, `statussen` (status, statement_time en `opnieuw_sinds` als eigen kolommen, de rest als JSON), `transacties`, `bestellingen`. Sleutels beginnen met de winkel-id. Indexen op `statussen(winkel, status)`, `statussen(winkel, opnieuw_sinds)` en `winkels(volgende_run)`.

**5. Tokens (`src/d1/tokens.ts`).** AES-GCM (WebCrypto), nieuwe IV per keer, winkel-id als extra gegevens (AAD), sleutelversie in de opgeslagen tekst zodat de sleutel kan wisselen; sleutel in een Worker-secret. Verversen als een token binnen een uur verloopt. **Opslaan voorwaardelijk:** `UPDATE winkels SET ... , token_versie = token_versie + 1 WHERE id = ? AND token_versie = ?`; bij `changes = 0` heeft een andere aanroep al ververst: tokens opnieuw lezen, geen fout. Het nieuwe paar staat vast vóór het gebruikt wordt. Na een 401 één keer verversen en opnieuw in dezelfde aanroep (binnen hetzelfde budget); dan winkelfout `koppeling_verlopen`. Waarschuwing aan de verkoper als het refresh token van TikTok binnen 14 dagen verloopt.

**6. De Worker (`src/worker.ts`).**
- **Cron**, één trigger elke 15 minuten: leest winkels met `volgende_run <= nu` (index, hoogstens 100), stuurt eerst één `sendBatch` (een dubbel bericht is onschuldig, zie winkelslot), schuift dan `volgende_run` op naar **nu + 30 minuten als korte lease** (één batch), en ruimt op (één query).
- **Consumer** met `max_batch_size: 1`, `max_concurrency: 5` (D1 doet één query tegelijk, Moneybird 150 verzoeken per 5 minuten per IP) en `max_retries: 0`; hij vangt alle fouten zelf af en bevestigt het bericht altijd (de cron pakt de winkel vanzelf weer op). Eerst een **winkelslot** (regel in `sloten` met statement_id `__winkel`, 15 minuten): bezet, dan niets doen. Daarna tokens, `verwerkWinkel`, uitkomst en `klaar()`, en de echte `volgende_run`: over 6 uur, of over 15 minuten als er nog werk is (iets `bezig_met_ophalen`, of het budget raakte op), hoogstens 8 keer achter elkaar (`snel_teller`), daarna weer 6 uur. Winkelslot terug.

## Wat het bewust niet doet
Geen schermen en geen inlogstroom (met Daans schermen), geen betaalstuk (Polar, eigen bouwstuk), geen echte uitrol (account van Thijs nodig; Tess zet het op de lijst als het product klaar is, met de meting van de 50 en de CPU). Geen Durable Objects (alleen betaald), geen KV (niet meteen overal gelijk). Geen service binding naar zichzelf (eigen limieten van de aangeroepen Worker niet zeker, GOK).

## GOK's
- Eén pot van 50 (zie boven).
- 10 ms CPU per consumer-aanroep met handtekeningen, JSON en SHA-256: toets (j) meet in Node; echt meten kan pas in Cloudflare. Stopt een aanroep op CPU, dan vangt punt 1 het op.

## Af als (tests met een nagebootste D1 op `node:sqlite`, dezelfde SQL)
- (a) De bestaande toetsen van `verwerk.ts` slagen ook met `D1Opslag` (zelfde uitkomsten en `schrijfacties`).
- (b) Fetch en D1 samen nooit boven 50 per aanroep (teller in de nagebootste D1 en in de nagebootste fetch), ook met 6 afrekeningen en 30 bestellingen elk; afrekening met 30 bestellingen hoogstens 8 queries.
- (c) Slot: twee eigenaars, één krijgt het; verlopen slot gaat over; `slotTot` leest vers; `neemSlot` leegt het geheugen.
- (d) Na `schrijfStatus` staan de bestellingen van daarvoor in D1 (zelfde batch); een batch die faalt laat niets half achter; eigen schrijfacties zijn terug te lezen.
- (e) Budget op bij nieuw werk: `budgetOp`, geen `fout` of `onzeker`, volgende aanroep verder zonder dubbel ophalen. Na het boeken weigert het budget nooit (status, wachtrij en slot gaan door).
- (f) Nagebootste afbraak tussen POST en status: status is `onzeker` "boeking gestart"; binnen 10 minuten geen tweede POST; daarna vindt zoeken op kenmerk het document (`ongewijzigd`).
- (g) Tokens: de tekst van het token staat niet in D1; verversen binnen een uur; twee aanroepen tegelijk verversen één keer en geven geen `koppeling_verlopen`; 401 geeft één keer verversen en dan `koppeling_verlopen`.
- (h) Cron: alleen winkels die aan de beurt zijn, hoogstens 100, eerst `sendBatch`, lease van 30 minuten; consumer: winkelslot, 6 uur of 15 minuten, na 8 keer weer 6 uur, bericht altijd bevestigd.
- (i) Na boeken zijn bewaarde bestellingen en transacties weg, de status blijft; opruimen raakt geen open afrekening; rij boven 1,5 MB geeft "te groot".
- (j) CPU van één consumer-aanroep met 30 bestellingen in Node onder 5 ms (`process.cpuUsage`), anders zakt de toets en gaat het als risico naar Tess.
- (k) Twee winkels in één database zien elkaars rijen niet; `EXPLAIN QUERY PLAN` toont een index voor `leesOpen` en de cron.

## Controleur
Ronde 1 (9 nov 22:17 UTC): nee. Moet-punten verwerkt in versie 2: één pot van 50 als veilige GOK; budget weigert nooit na het boeken; "boeking gestart" vóór de POST; `leesStatus` alleen status, geheugen leeg bij `neemSlot`, eigen schrijfacties terug te lezen; winkelslot en voorwaardelijk tokens opslaan, `max_retries: 0`; bewaren alleen tot de afrekening af is, daglimieten D1 en rij van 2 MB meegerekend; kolommen en indexen voor `leesOpen`, cron en `snel_teller`. Kan-punten verwerkt: lease van 30 minuten en volgorde in de cron, 100 per cron, `max_concurrency` 5, read replication uit, opruimen met `rowid IN`, AES-GCM-details en sleutelversie, waarschuwing refresh token, toetsen (e) tot (k), (j) slaagt of zakt.
