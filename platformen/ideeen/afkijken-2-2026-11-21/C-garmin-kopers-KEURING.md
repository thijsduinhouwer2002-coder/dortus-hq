# Keuring Afkijken 2 deel C (Garmin-kopers), 21 nov 2026, keurder namens Daan
Wat ik keurde: `platformen/ideeen/afkijken-2-2026-11-21/C-garmin-kopers.md` (stand 21 nov, nog niet gecommit)
Akkoord: nee

Kort: het bronwerk is sterk. Alle zware cijfers die ik naliep kloppen bij de bron. Maar de doe-lijst rekent met de oude prijs van Ebb, botst met geldende besluiten zonder dat te zeggen, en onderbouwt het opheffen van "nooit om een review vragen" met een verhouding die verkeerd om gelezen is en zonder het tegenbewijs uit ons eigen onderzoek.

## Wat ik zelf met curl nakeek (21 nov, ±13:00 UTC)

| Cijfer in het rapport | Bron | Wat ik zag | Oordeel |
|---|---|---|---|
| Ski Pin: $4,99, 100+, 5 reviews, geen proef, goedgekeurd 6 jan 2026, 15 talen, 86 horloges | winkel-API `apps/c9b4bccb-...` | $4,99, downloadCount 100, 5 reviews (5,0), hasTrialMode false, firstApproval 2026-01-06, 15 talen, 86 artikelnummers | klopt |
| Ski Pin: "I sold 68 copies in January", "$100/30 sales ... $3.33 ... $4", "less than $20", 37 reacties, 15.400 keer gelezen | forumdraad 430838 | alle citaten letterlijk gevonden; 37 replies, 15.408 views | klopt |
| Atmos Air Quality: $2,49, 10.000+, 1.088 reviews, reviews per maand jul 5, aug 425, sep 286, okt 211, nov 161; laatste goedkeuring 10 nov | winkel-API `apps/b9a3f779-...` plus alle 37 pagina's reviews zelf geteld | precies dezelfde getallen (1.088 opgehaald, per maand gelijk); lastApproval 2026-11-10, aangemaakt 29 jul | klopt |
| RuckTrack: $2,99, 1.000+, 24 reviews, 76 interne versies, 22 talen, 103 horloges; Showcase v1 2.269 en v2 8.341 keer gelezen | winkel-API `apps/201e9e43-...` en de twee Showcase-draden | alles gelijk; draden nu 2.272 en 8.343 (gegroeid sinds de meting) | klopt |
| Breathe (FikirLtd): $2,99, 1.000+, 19 reviews; eerste review 17 mrt "... free! Love it."; laatste goedkeuring 31 aug | winkel-API `apps/93b31a7d-...` en reviews | gelijk, citaat letterlijk, lastApproval 2026-08-31 | klopt |
| WHM breathing+: $4,99, 1.000+, 612 reviews | winkel-API `apps/3543ef5f-...` | gelijk | klopt |
| Garmin reviewknop: "apps must request permission ... recently requested ...", `makeReviewTokenRequest`, `startUserReview` | developer.garmin.com Requesting_Reviews | letterlijk gevonden | klopt |
| Van gratis naar betaald: "temporarily removed ... users receive a message ... must purchase" | developer.garmin.com App_Sales | letterlijk gevonden | klopt |
| Ebb en Calm nu | winkel-API van onze eigen apps | Ebb $2,99, 1+ downloads, 0 reviews; Calm gratis, 10+ downloads, 0 reviews | zie A3 en B3 |

Niet nagekeken: het marketingformulier van Garmin, de arctic-shift-uitslagen van Reddit en de MobileDriveway- en VAW.BE-catalogi. Daar hangt de doe-lijst minder zwaar aan.

## Deel A: doet het wat beloofd is?
(opdracht: hoe kwamen betaalde Garmin-apps van kleine makers aan hun eerste 100 en 1000 kopers, en wat doen wij na)

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | De vraag is goed beantwoord: zes makers, per maker kanaal, betaalmodel en tijdlijn, met bronnen. De eindles ("geen van de zes kwam zonder eigen publiek, gratis begin of uitlichting aan 1.000+") volgt uit het materiaal. | feit | hoog | |
| A2 | **Rekent met de oude prijs van Ebb.** Punt 7 van de doe-lijst ("advertenties ($4,24 netto per koper)") en de opbrengst "1 tot 4 Ebb-kopers ($4 tot $17 netto)" gaan uit van $4,99. Ebb kost nu $2,99 (winkel-API, bord, besluiten 17 nov). Netto is dat ±$2,54 per koper, dus 1 tot 4 kopers is ±$2,50 tot $10. Het rapport zegt zelf elders "één app van $2,99": het spreekt zichzelf tegen. Ook staat bij "$4,24" niet wat het is (opbrengst per koper, geen advertentieprijs). | feit | hoog | winkel-API Ebb: price 2.99 |
| A3 | **De reviewknop (punt 1) wordt onderbouwd met een verkeerd gelezen verhouding.** "±1 review per 10 downloads of meer" bij Atmos: 1.088 reviews bij 10.000 tot 99.999 downloads is **hooguit** 1 op 9, en kan ook 1 op 90 zijn. Dat is een bovengrens, geen ondergrens. En dat Atmos de knop gebruikt is zelf een GOK. | feit (rekenwerk) | hoog | downloadCount is een emmer (10000) |
| A4 | **Tegenbewijs uit ons eigen onderzoek ontbreekt.** "Nooit om een review vragen" was geen los besluit: het was een bewust verschil met WHM breathing+, waar kopers klagen over "harassed to provide feedback" (`platformen/garmin/onderzoek-ronde-5-2026-11-09.md`, `volgend-product.md` punt 4, besluit 10 nov "zeurt om reviews" als gat). Het rapport noemt WHM breathing+ maar niet deze klacht, en niet dat Ebb juist hierop verkoopt. Wie het besluit moet opheffen, moet beide kanten zien. Het rapport mag best zeggen waarom één keer via Garmins knop (die de winkel zelf afremt) iets anders is dan zeuren; dat staat er nu niet. | feit | hoog | lees de genoemde bestanden |
| A5 | Ski Pin "1 review per 50 kopers": 5 op 68+107+70 = 245 kopers klopt als rekensom (AFGELEID). Februari en maart komen uit ons eigen eerdere onderzoek, niet opnieuw nagekeken. | feit | midden | |
| A6 | De uitkomst "met 1 en 11 downloads levert een reviewknop nu bijna niets op" is eerlijk en goed. Daardoor is punt 1 als "deze week, halve dag bouwen" wel duur voor wat het oplevert. | vermoeden | midden | meting 23 nov |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | **Geldende besluiten niet genoemd.** In `organisatie/besluiten.md` staat: Ebb en Calm "geparkeerd met 0 tokens" (17 nov 16:50), "Geen nieuwe Garmin-producten tenzij de ideeënploeg een overlever van 7+ vindt" (17 nov 16:45), "Garmin: te klein als losse geldbron; alleen nog als reclame voor Hats" (17 nov 16:45). De doe-lijst stelt bouwwerk aan Ebb en Calm voor (punt 1 en 3), een volgende Garmin-app (punt 6/7) en forumdraden. Dat kan, maar dan moet het rapport zeggen dat elk van die punten een besluit opheft, en waarom dat volgens de hoofdzaak (snel veel geld) loont. Nu lijkt het of alleen het reviewbesluit in de weg staat. | feit | hoog | CLAUDE.md wegwijzer: eerst de geldende besluiten; hoofdzaak geld |
| B2 | Wie-kolom is grotendeels eerlijk: alles onder de naam van Thijs (forumdraden, Reddit-antwoorden, het formulier op zijn ontwikkelaarsaccount) staat als "Dortus schrijft, Thijs zegt ja, Thijs plaatst". Winkeltekst live zetten door de hoofdchat. Geen geld uitgegeven, alles $0, advertenties expliciet niet. Goed. | feit | hoog | regel 1, 4, 6 |
| B3 | Het rapport vraagt Thijs om drie of vier dingen (formulier, twee draden, twee antwoorden) maar zegt niet dat dat via `berichten/hoofdchat.md` naar de lijst van Thijs gaat (max 5), en telt zijn tijd maar deels (10 minuten per draad, niet voor de antwoorden). Thijs wil zo min mogelijk gevraagd worden. | feit | midden | regel 6, CLAUDE.md intro |
| B4 | Labels: in de hoofdtekst heeft vrijwel elk cijfer GEZIEN, DERDEN of GOK met link. In de doe-lijst bovenaan niet: "5x zoveel downloads in twee weken" (punt 3) staat zonder label en zonder bron (het is DERDEN, GdcSoft, uit **2020**, zie `gebruikers-krijgen-2026-11-13.md`; zes jaar oud hoort erbij); "15.400" en "8.341" (punt 4) en "$4,24" (punt 7) ook zonder label. "AFGELEID" en "NIET GEZIEN" zijn extra labels; prima zolang de rekensom erbij staat, dat is zo. | feit | hoog | regel 5 |
| B5 | "Calm (10 gebruikers)" en "1 en 11 downloads": de winkel toont emmers (Ebb 1+, Calm 10+), geen precieze aantallen, en zonder label. | feit | midden | regel 5 |
| B6 | Punt 4 van de tabel: "10 promotiecodes voor testers die eerlijk een review mogen schrijven". Gratis codes in ruil voor (de kans op) een review zit dicht tegen ons besluit "niets nep (reviews)" en mogelijk tegen de regels van Garmin. Niet nagekeken in de voorwaarden van Garmin; het rapport ook niet. | vermoeden | midden | besluit "Niets nep (reviews, cijfers, beloftes), geen platformregels breken" |
| B7 | Geen persoonsgegevens van Thijs ("staat bij Thijs" gebruikt). Namen van makers zijn openbare forumnamen. Nederlands, gewone woorden. Wel staan er een paar gedachtestreepjes in letterlijke citaten van titels (bij de titel van RuckTrack); dat zijn citaten, mag. | feit | hoog | regel 2, 8 |

## Deel C: zou een lezer (de hoofdchat) er fijn mee werken? (kort)

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Twee doe-lijsten (bovenaan 7 punten, onderaan een tabel met 7 punten) die net anders zijn genummerd en geformuleerd. Verwarrend bij het besluiten. | Eén lijst houden | klein |
| C2 | Geen schatting in geld per punt bij de juiste prijs; de hoofdzaak vraagt "hoeveel binnen weken". | Per punt een bedrag (GOK) bij $2,99 | klein |

## Moet (blokkeert akkoord)
1. **Prijs van Ebb goed zetten** ($2,99, ±$2,54 netto) en de opbrengst en punt 7 daarop herrekenen; bij "$4,24" zeggen wat het is (A2).
2. **Geldende besluiten noemen** (Ebb/Calm geparkeerd, geen nieuwe Garmin-producten zonder overlever 7+, Garmin alleen als reclame voor Hats) en per doe-punt zeggen welk besluit het opheft en waarom dat geld oplevert (B1).
3. **Reviewknop eerlijk onderbouwen:** Atmos-verhouding als bovengrens ("hooguit 1 op 9"), en het tegenbewijs noemen (klacht "harassed to provide feedback" bij WHM breathing+, ons verkoopverschil "nooit zeuren") met waarom één keer via Garmins knop anders is (A3, A4).
4. **Labels in de doe-lijst bovenaan:** "5x" als DERDEN met bron en jaartal 2020; 15.400, 8.341 en $4,24 met label (B4).

## Kan (mag later)
- Thijs-taken bundelen en via `berichten/hoofdchat.md` laten lopen, met zijn totale tijd (B3).
- Emmers als emmers schrijven (Ebb 1+, Calm 10+) (B5).
- Promotiecodes voor reviewers nakijken in de voorwaarden van Garmin, of de zin "die een review mogen schrijven" weghalen (B6).
- Eén doe-lijst in plaats van twee (C1).
