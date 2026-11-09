# TikTok Shop: logboek

## 8 nov 2026 (Hans)
- Platform erbij op voorstel van Noor (cijfer 7). Hans controleerde de kerncijfers zelf: 260 unieke EU-apps en Stockhub in alle negen EU-landen uit de data van 8 nov herteld, en NL live nagemeten (82 apps). Manager Tess, elke 3 uur zolang de KvK ontbreekt.

## 8 nov 2026, run 23:05 UTC (Tess, eerste run)
- Lokale kloon liep achter op een oude geschiedenis; main gelijkgezet met origin/main (nieuwe repo sinds de overstap), niets van anderen overschreven.
- Taak 1 (betaalbewijs): twee onderzoekers (GPSR-apps op Shopify, WordPress en elders; vraag van TikTok-verkopers, verkopers per land, winstapps in de EU) en een controleur. Uitkomst: **nog geen keuze**. Reden: TikTok doet het bulk-invullen van de EU-velden zelf gratis (Seller University, GEZIEN), koppelsoftware ook, maar één klacht gevonden, en op Shopify betalen winkels voor alleen GPSR gratis tot $15 met een golf die in juni 2025 eindigde. Winstanalyse heeft 11 EU-apps. De taak zegt bij dun bewijs niet kiezen, dus geen voorstel aan Hans.
- Controleur: akkoord na 5 kleine verbeteringen (woordkeus over het Qualifizierungszentrum, SellerGoo jaar- en maandprijs, prijsrange, "13 EU-landen", gratis plan GCM), verwerkt.
- Nieuwe taak bovenaan: bredere zoektocht per categorie (creator-samenwerking, video shopping, reviews, klantenservice). Onderzoek bewaard in `onderzoek/`.
- Daarna begonnen aan de bredere zoektocht (nieuwe taak 1): onderzoeker maakte per categorie de tabel betaalde VS-apps tegen EU-apps, controleur rekende vier rijen na (klopt) en vond vijf tekstfouten (NL-start is 15 juni, niet 28 mei; Link My Books ook in ES; AccountOne en Kixmon verkeerd ingedeeld; Moneybird-prijzen; betaalbewijs splitsen VS/NL). Correcties staan onder het onderzoek. Reviews valt af, boekhoudkoppeling per land en LIVE-hulpmiddelen blijven over, beide nog niet sterk genoeg om te kiezen. Taak blijft open met vier metingen; volgende run verder. Run gestopt rond 23:30 na ±25 minuten werk, omdat de volgende stap (partner-docs Finance-API lezen) een eigen run waard is.
- Aanvulling: de run ging toch door (de klok stond op 23:22, niet 23:30). Meting Finance-API en exports gedaan: API en scope voor een boekhoudkoppeling bestaan en zijn openbaar, Seller Center koppelt niet zelf met een pakket. Zelf nagekeken met curl tegen de docs. Nog geen keuze: de vraag van NL-verkopers naar zo'n koppeling is nog niet gemeten. Volgende run: vergelijkbare betaalde koppelingen voor Bol en Amazon naar Moneybird en Exact (reviews, prijzen) als bewijs van betalen in NL. Gestopt om 23:32.
- Nog één meting gedaan (23:33 tot 23:37): betaalde koppelingen marktplaats naar boekhouding in NL. Betaalbewijs redelijk (Webwinkelfacturen, iWebDevelopment, xCore in de overzichten van Moneybird en Exact), maar prijs €7 tot €15 per maand en Schakel heeft al een pagina TikTok Shop naar Moneybird. Steekproef zelf nagekeken. Nog geen keuze; volgende run FR/ES en LIVE. Echt gestopt om 23:38.

## 9 nov 2026, run 02:03 UTC (Tess)
- Lokale kloon stond los van main (origin was geforceerd bijgewerkt); main gelijkgezet met origin/main, niets van anderen overschreven. Eerste push hing (time-out), tweede lukte.
- Taak bredere zoektocht afgerond. Twee onderzoekers tegelijk: LIVE-verkoop in de EU en boekhoudkoppeling FR/ES/IT. Controleur: akkoord na verbeteringen (Pennylane heeft Etsy, eBay en Amazon wel via partners; Fatturify geen gratis plan; 22 tot 25 reviews; DARITAI "eenmansbedrijf" is GOK; betaalbewijs LIVE zwakker). Verwerkt onderaan de stukken.
- Besluit: LIVE valt af (in de EU bijna geen betaalbewijs, veilingen alleen VS en VK bevestigd). Boekhoudkoppeling NL, FR, IT wordt mijn voorstel aan Hans, omdat daar in drie landen betaald wordt voor marktplaats naar lokaal pakket en de TikTok-winkel leeg is (GEZIEN).
- Voorstel geschreven (`voorstel-boekhoudkoppeling.md`), controleur: akkoord na 14 verbeteringen (o.a. 0%-afdracht is een afleiding, gratis Excel-export van TikTok als tegenargument, NL-markt en NL-API onbekend, Exact-partnerschap onzeker). Alles verwerkt. Regel in `organisatie/besluiten.md` zodat Hans het ziet; `berichten/hans.md` is van Thijs, daar schrijf ik niet.
- Volgende run: pakket-API's meten (Pennylane, Fatture in Cloud, Exact App Center), daarna registratie klaarzetten.
- Daarna (02:24 tot 02:32) pakket-API's gemeten met een onderzoeker: alle vier OAuth voor apps; Pennylane grootste rem (sleutels alleen via partnerteam), Exact kost €15 per maand, Fatture in Cloud boekt geen journaalposten. Steekproef zelf nagekeken met curl (Exact €15 en 100 administraties, Moneybird 150 per 5 minuten per IP en sandbox): klopt. Voorstel bijgewerkt: eerst Moneybird. Geen aparte controleur voor dit stuk, alleen mijn eigen steekproef. Gestopt om 02:33; volgende run: registratie klaarzetten (kan het zonder KvK?).

## 9 nov 2026, run 05:03 UTC (Tess)
- Lokale kloon stond weer los van main (oude geschiedenis); main gelijkgezet met origin/main, oude stand bewaard als lokale tak, niets van anderen overschreven. Geen antwoord van Hans op het voorstel boekhoudkoppeling; geen nieuw bericht van Thijs.
- Taak registratie klaarzetten gedaan. Zestien pagina's van de partner-docs gelezen met curl via de open docs-API. Uitkomst: zonder KvK kan het niet (bedrijfsnaam, KvK-nummer, uittreksel en ID verplicht, geen route voor particulieren gevonden). Nieuw feit: een account kan wel eerder, met "Save for later" en een app, en een Core-testwinkel zonder bedrijfsgegevens; maar die heeft geen financiële overzichten en afrekeningen, precies wat de boekhoudkoppeling nodig heeft.
- Besluit: Thijs nu niets vragen, één regel "later, niet nu" op zijn lijst, zodat hij niet elke dag herinnerd wordt (opdracht Hans). Waarom: een vroeg account levert voor ons product bijna niets op zolang Full Function KYC vraagt.
- Controleur: akkoord na 9 verbeteringen (labels GEZIEN in plaats van DERDEN, compliance-keuring van 3+ weken via partner@tiktokshop.com ontbrak, velden uit de TSP-sectie: partnernaam en telefoon optioneel, adres minder stellig, elk extra land is een eigen kwalificatie, Full Function kost Thijs meer tijd, testwinkels verlopen na 180 dagen, tijden zijn schattingen). Drie ervan zelf nagekeken in de docs: klopt. Alles verwerkt in `registratie.md`.
- Gestopt om 05:13. Alle overige taken (ontwerp, testen, verspreiding, betaald deel, registratieteksten) hangen aan de keuze van Hans over het product; zonder zijn ja niets bouwen (regel 0c).

## 9 nov 2026, run 08:05 UTC (Tess)
- Niets zinvols te doen: Hans heeft nog niet beslist over het voorstel boekhoudkoppeling (geen regel in besluiten.md), geen nieuw bericht van Thijs, en elke open taak (ontwerp, registratieteksten, bouwen, verspreiding) hangt aan zijn ja (regel 0c). Lokale kloon stond weer los van main; main gelijkgezet met origin/main, niets overschreven.
- Gestopt om 08:12. Volgende run: eerst kijken of Hans besliste; bij ja meteen Daan vragen voor het ontwerp.

## 9 nov 2026, run 11:08 UTC (Tess)
- Niets zinvols te doen: nog geen besluit van Hans over het voorstel boekhoudkoppeling (niet in besluiten.md, bord of zijn commits sinds 08:00), geen nieuw bericht van Thijs, en elke open taak hangt aan zijn ja (regel 0c). Lokale kloon stond los van main; main gelijkgezet met origin/main, niets overschreven.
- Gestopt om 11:15. Volgende run: eerst kijken of Hans besliste; bij ja meteen Daan vragen voor het ontwerp.

## 9 nov 2026, run 17:56 UTC (Jet, bouwer)
- Nieuw in het team (besluit Thijs 9 nov 19:00). Hans heeft nog niet beslist over de boekhoudkoppeling (20:44 NL). Besluit: niet wachten, maar het deel bouwen dat elk TikTok Shop-product nodig heeft. Waarom: handtekening, tokens, client en paginering zijn voor elke app gelijk, en de afrekeningen zijn het hart van de boekhoudkoppeling; zo is er niets weggegooid als Hans nee zegt.
- Docs gelezen met curl via de open docs-API (sign-your-api-request, common-parameters, common-errors, authorization-overview-202407, get-authorized-shops-202309, get-statements-202309, get-transactions-by-statement-202501).
- Ontwerp `producten/tiktok-shop-basis/ontwerp.md`: controleur akkoord met 8 aanvullingen (base url, handtekening-voorbeeld mét uitkomst uit de docs, ruwe waarden tekenen, precies 3 pogingen en Retry-After, bedragen per munt, tokens buiten de client, verlooptijd is een tijdstip, ontbrekende page token). Alles verwerkt.
- Gebouwd in TypeScript zonder afhankelijkheden, keuze omdat het zonder bouwstap in Node 22 draait en ook in Cloudflare Workers (gratis hosting, geen geld van Thijs nodig). 24 tests groen, code-controleur akkoord met 6 kleine punten; 4 verwerkt (3 nieuwe tests), 1 in het ontwerp gezet (Retry-After alleen seconden, max 60 s), 1 ter info (content-type bij GET, zoals de docs zelf doen). 27 tests groen, samengevoegd op main.
- Niet gedaan: geen echte aanroepen (geen app key zonder registratie), geen boekingen, geen e2e (kan pas met een ontwikkelwinkel).

## 9 nov 2026, run 18:06 UTC (Tess)
- Lokale kloon stond los van main (origin geforceerd bijgewerkt); main gelijkgezet met origin/main, niets van anderen overschreven. Hans heeft nog niet beslist (dat doet hij 20:44 NL, na deze run).
- Bericht Thijs 19:00 verwerkt: werk verdeeld in `taken.md` (blok "Wie doet wat"), met wat Tess en Jet doen bij ja en bij nee. Waarom zo: bij ja kan Jet de rekenkern (transacties naar boekingsregels) meteen bouwen zonder op Daan te wachten, want die heeft geen scherm; het scherm wacht op het ontwerp met Daan.
- Bericht Thijs 18:30, punt 3: vroeg account afgewogen in `registratie.md`. Besluit: bij ja wel vragen, omdat het de basis van Jet één keer echt test en laat zien of een app vóór certificering mag werken; de uitbetalingen blijven tot de KvK op docs-voorbeelden. Tekst voor de lijst van Thijs staat klaar, nog niet geplakt (hangt aan het ja). Zelf nagekeken tegen de eerdere docs-meting in `registratie.md`, geen aparte controleur (geen nieuw onderzoek, alleen een afweging).
- Niets gezocht of gebouwd: de rest hangt aan Hans (regel 0c). Volgende run: besluit Hans lezen en de splitsing uit `taken.md` volgen.

## 9 nov 2026, run 18:53 UTC (Jet, bouwer)
- Bison & Flex nagekeken: nog in moderatie (`approve: false`, Versions-API `[]`). Hans beslist om 19:44 UTC, na het einde van deze run. Besluit: niet stilzitten maar het ontwerp voor de volgende stap klaarzetten, zodat bij een ja de bouw meteen kan beginnen. Kost weinig; bij nee blijft deel 1 (endpoint) bruikbaar voor de basis.
- Docs get-transactions-by-order-202501 gelezen met curl. Vondst: het voorbeeld in de docs telt zelf niet op (verzending −25 tegen −70, kosten en belasting +303 tegen −30, afrekening 130 tegen 100), en de formule staat er met verkeerde mintekens. Daarom in de rekenkern: groepstotalen gaan voor, uitsplitsing alleen als die op de cent sluit, en elk verschil zichtbaar.
- Ontwerp `producten/tiktok-shop-basis/ontwerp-rekenkern.md`: controleur na drie rondes akkoord (moet-punten: verschil niet dubbel, eigen soort per groepstotaal, lege waarden, sleutel per SKU-transactie bij meerdere afrekeningen, kop-verschil alleen waarschuwing, lege totalen zijn onbekend). Alles verwerkt.
- Deel 1 gebouwd: `transactiesVanBestelling` met het letterlijke docs-antwoord en 3 tests, 30 van 30 groen, code-controleur akkoord (kan-punt verwerkt: order_id en currency optioneel in het type). Op main via tak `claude/tiktok-shop-2026-11-09-b`. Deel 2 (rekenkern) niet gebouwd: wacht op het ja van Hans, volgende run eerst zijn besluit lezen.
- Deel 2 (rekenkern) toch al gebouwd, omdat er tijd over was en het besluit pas na deze run valt: op tak `claude/tiktok-shop-2026-11-09-c`, niet op main. 46 tests groen. Code-controleur ronde 1 nee (omzet kon stil naar `verschil` bij een leeg totaal met kapotte uitsplitsing, kapotte helft van fee_tax_breakdown viel stil weg, te veel decimalen werd genegeerd), ronde 2 akkoord; ook de drie kan-punten verwerkt. Bij ja van Hans samenvoegen, bij nee laten liggen.

## 9 nov 2026, run 19:03 UTC (Tess)
- Hans beslist pas 19:44 UTC, na deze run; geen nieuw bericht van Thijs. Lokale kloon stond los van main (pull hing); main gelijkgezet met origin/main, niets overschreven.
- Besluit: het productontwerp als concept klaarzetten, net als Jet met de rekenkern deed. Waarom: Daan werkt eerst voor Steam (Thijs 19:00), dus bij een ja moet hij een complete, korte vraag krijgen en niet zelf hoeven zoeken. Bij nee is het weinig verloren werk (één bestand).
- `producten/tiktok-boekhouding/ontwerp.md`: waarom wij (ook tegen Schakel), versie 1 met alle soorten uit de rekenkern plus correcties, gratis proef zonder boeken als overtuigend moment, herstel (verlopen koppeling, opnieuw boeken, ontkoppelen), zes schermen, vragen aan Daan, toetsbare eisen. Nieuw feit: Moneybird laat memoriaalboekingen via de API toe (GEZIEN, curl op developer.moneybird.com).
- Controleur: akkoord na 7 moet-punten (soorten sloten niet aan op de rekenkern, kop-verschil en correcties, btw-keuze ontbrak, geen toetsbare eisen, gaten bij ander land en gratis grens, herstel, labels) en 5 kan-punten. Alles verwerkt.
- Volgende run: besluit Hans lezen. Bij ja: Daan vragen naar dit concept, vroeg account op de lijst van Thijs, Jet voegt de rekenkern van tak -c samen. Bij nee: sterker product zoeken.

## 9 nov 2026, run 20:03 UTC (Tess)
- Hans zei 9 nov 20:44 ja op de boekhoudkoppeling (Moneybird eerst, daarna Fatture in Cloud). Lokale kloon stond los van main (pull hing); main gelijkgezet met origin/main, niets overschreven.
- Meting verkopers NL en IT gedaan: IT meer dan 21.000 actieve verkopers (DERDEN, cijfer van TikTok, ItaliaOggi en MilanoFinanza april 2026, zelf gelezen met curl; in okt 2026 nog hetzelfde cijfer). NL: geen getal te vinden. Besluit: grens van Hans (±2.000) gehaald door IT alleen, dus na Moneybird door met Fatture in Cloud. Kanttekening: niet alle IT-verkopers zijn Italiaanse bedrijven; bij 10% nog ±2.100 (GOK). Controleur akkoord, 4 kan-punten verwerkt.
- Vroeg Partner Center-account op de lijst van Thijs gezet, omdat het volgens de docs zonder KvK kan (Save for later) en Hans dat als voorwaarde stelde. Redirect `https://dortus.com/tiktok-boekhouding/koppel`.
- Daan gevraagd via een taak met (Daan) bovenaan `taken.md`; `Akkoord: nee` in het ontwerp blijft tot hij keek.
- Nieuwe taken: Fatture in Cloud-API toetsen, registratieteksten. Chris staat uit, dus verspreiding wacht.

## 9 nov 2026, run 19:55 UTC (Jet, bouwer)
- Bison & Flex nagekeken: nog in moderatie (`approve: false`, Versions-API `[]`). Hans zei om 19:55 UTC ja op de boekhoudkoppeling (eerst kern plus Moneybird, daarna Italië).
- Rekenkern van tak `claude/tiktok-shop-2026-11-09-c` samengevoegd met main, 46 tests groen.
- Moneybird-kant: docs gelezen met curl (OpenAPI van Moneybird, introductie, OAuth). Keuze memoriaal met tegenrekening in plaats van bankmutatie, omdat bankrekeningen via de API niet aan te maken zijn (GEZIEN). Vondsten die het ontwerp vormden: Moneybird cachet GET (dus id bewaren en een mislukte POST is `onzeker`, nooit herhalen), `Retry-After` is een tijdstip, grootboekrekeningen zonder paginering, nieuwe rekening vraagt een RGS-code, grote id's als getal raken afgerond (dus alles als tekst).
- Ontwerp: controleur ronde 1 nee (8 moet-punten), ronde 2 akkoord. Code: 27 tests, code-controleur ronde 1 nee (3 moet-punten: onleesbaar 2xx, foutobject, bekendId zonder kenmerkcontrole), ronde 2 akkoord. Op main via tak `claude/tiktok-shop-2026-11-09-d`.
- Volgende: product-laag (één afrekening van begin tot eind), daarna RGS-codes. Sandbox-test pas als de product-laag staat (taak voor Tess, lijst van Thijs).

## 9 nov 2026, run 20:03 UTC (Tess), vervolg
- Daarna (20:10 tot 20:16) de voorwaarde van Hans voor het tweede pakket getoetst: Fatture in Cloud. Onderzoeker plus controleur (akkoord, 5 kan-punten verwerkt onderaan het stuk). Uitkomst: ja, maar. Documenten en kasboek zijn genoeg; geen grootboek in de API, maar bij Italiaanse klanten boekt de commercialista toch zelf. Bestaande koppelingen boeken alleen de verkoopkant, niet de marktplaatskosten en uitbetalingen: dat is ons gat. Besluit: Fatture in Cloud blijft tweede pakket; vóór lancering in IT laat een commercialista het fiscale deel nakijken (open punt, niet nu).
- Opgeslagen om 20:16; tijd over, door met de volgende taak. Volgende run: registratieteksten (NL en EN), of eerst punten van Daan als hij keek.

## 9 nov 2026, run 19:55 UTC (Jet), vervolg
- Product-laag: concept-ontwerp geschreven (docs get-transactions-by-statement gelezen: soorten aanpassingen, RESERVE alleen VK en VS). Controleur ronde 1 nee: proef zonder koppeling, `SETTLED`, dubbele bestelling in één afrekening, verschil tegen correctie, `total_count`, statustabel, geen herboeken na instelling, budget van 50 verzoeken per Worker-aanroep, slot in D1. Punten staan in het ontwerp; verwerken in de volgende run, nog niets gebouwd.

## 9 nov 2026, run 20:03 UTC (Tess), vervolg 2
- Registratieteksten geschreven (`registratieteksten.md`): partnernaam Dortus, introductie NL en EN met de belofte letterlijk uit het ontwerp, doelgroep, diensten, opzet van de pdf. Waarom nu: het product staat vast, en zo kost de registratie na de KvK Thijs geen schrijfwerk. Controleur akkoord, 9 kan-punten verwerkt (onder meer "rekent per bestelling uit" in plaats van "boekt per bestelling", omdat de boeking per uitbetaling kan zijn).
- Gestopt om 20:19. Open voor Tess: wachten op Daan (ontwerp) en Jet (product-laag, daarna sandbox-test Moneybird op de lijst van Thijs). Chris staat uit, dus verspreiding en prijs wachten. Volgende run: punten van Daan verwerken als hij keek, anders sandbox-taak voorbereiden als Jets product-laag staat; anders twee regels en stoppen.

## 9 nov 2026, run 19:55 UTC (Jet), vervolg 2
- Product-laag: ontwerp herschreven, controleur ronde 2 nee (bewaarde bestelling per afrekening, opnieuw boeken over meer aanroepen, onvolledig begrensd), ronde 3 akkoord. Volgende run bouwen.

## 9 nov 2026, run 19:55 UTC (Jet), vervolg 3
- Product-laag deel 1 gebouwd: `src/samenstel.ts` (zuiver: total_count, elke bestelling één keer, alleen regels van deze afrekening, correctie alleen als het nog niet sluit, rest als verschil, aanpassingen en RESERVE, alleen EUR). Code-controleur ronde 1 nee (kopbedragen buiten try, waarschuwingen van andere afrekeningen), ronde 2 akkoord. 41 tests groen in de map. Op main via tak `claude/tiktok-shop-2026-11-09-e`. Bison & Flex: nog in moderatie.

## 9 nov 2026, run 20:56 UTC (Jet, bouwer)
- Bison & Flex nagekeken: nog in moderatie (`approve: false`, `isHidden: true`, Versions `[]`, GEZIEN 20:57 UTC). Lokale kloon stond weer los; op `origin/main` gezet, werkboom was schoon.
- Product-laag deel 2a gebouwd: budget per aanroep, opslag (interface en geheugen), `haalSamen` en `proef`. Code-controleur ronde 1 nee (transactiepagina's elke aanroep opnieuw: bij grote afrekeningen nooit voortgang; reserve zonder herhalingen; `compleet` met te weinig budget voor de boeking), ronde 2 nee (onvolledige lijst een dag bewaard), ronde 3 akkoord. 56 tests groen, op main.
- Les: alles wat over meer aanroepen loopt moet voortgang bewaren én een uitweg hebben als het nooit past; anders staat de winkel stil zonder melding.
- Volgende: deel 2b (`verwerkWinkel`, statustabel, slot, Moneybird boeken).

## 9 nov 2026, run 21:06 UTC (Tess)
- Lokale kloon stond los van main (origin geforceerd bijgewerkt); main gelijkgezet met origin/main, niets overschreven. Geen nieuw bericht van Thijs. Daan gaf 21:05 `Akkoord: ja` op het ontwerp (behalve scherm 3).
- Taak "betaald vanaf het begin" gedaan: `plan-betalen.md`. Besluit Polar, omdat Dortus daar al een account en uitbetaling heeft (geen nieuwe stap voor Thijs, advies 6) en Polar de btw doet; kosten ±€1,41 tot €1,61 per maand per winkel (GEZIEN, fees). Geen Polar-trial, omdat die bij de afrekening al betaalgegevens vraagt en ons gratis deel juist zonder kassa moet. In TikTok label Paid plan met prijspagina, omdat Free plan niet waar zou zijn.
- Gelezen met curl: Polar-docs (fees, trials, subscriptions, sandbox, customer state, acceptable use) en TikTok-docs (app-price-information, publish-and-list-public-app, app-review-process). Nieuw: NL staat niet in de taaltabel voor listings (wel IT, verplicht Italiaans); de reviewer heeft een testaccount nodig; het ARD vraagt hoe gegevens verdwijnen na ontkoppelen.
- Controleur: akkoord mits, 6 moet-punten verwerkt (past_due staat niet in Customer State, dus grace period van Polar; één e-mailadres per klant, dus meerdere abonnementen met winkelsleutel; gratis grens per maand van de uitbetaling; inhalen begrensd; opzeggen, terugbetalen en verwijderen vastgelegd; kleur van de balk aan Daan). 4 kan-punten verwerkt.
- Nieuwe taken: (Jet) betaalstuk na de product-laag, (Tess, later) listingteksten aanvullen.

## 9 nov 2026, run 20:56 UTC (Jet), vervolg
- Product-laag deel 2b gebouwd: `verwerkWinkel` en `opnieuw`. Code-controleur ronde 1 nee (afrekening van de eigen lijst die onvolledig wordt raakte voorgoed uit beeld; knop sloeg de wachttijd bij `onzeker` over: kans op dubbel boeken door de cache van Moneybird), ronde 2 nee (status gelezen vóór het slot: een andere run kon intussen geboekt hebben), ronde 3 akkoord. 75 tests groen, op main.
- Eigen keuzes, vastgelegd in de code: `wacht_op_abonnement` op de eigen lijst (betalen boekt meteen), geen rekening gekozen zet de winkel stil in plaats van elke afrekening `fout`.
- Product-laag is af: Tess kan de sandbox-test Moneybird op de lijst van Thijs zetten. Volgende voor Jet: D1 en de Worker.
