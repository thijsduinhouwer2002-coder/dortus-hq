# Teachers Pay Teachers (TpT)

Vera, 9 nov 2026, run 14:31 (Amsterdam). Nagekeken door een controleur: akkoord met 4 correcties, verwerkt. Platformrun (bericht Thijs 9 nov 13:35: terug naar 100% platformen, op zoek naar een 8).

## Wat het is
De grootste winkel voor lesmateriaal: leraren verkopen werkbladen, Google Slides, Easel-activiteiten en bundels aan andere leraren. TpT rekent af en betaalt maandelijks uit via Hyperwallet (PayPal of bank). Eigendom van IXL sinds 2023. Waarom gekozen: nog nooit bekeken, een echte kassa, één persoon koopt voor zichzelf, en de producten (pdf, slides) kunnen wij met code maken en testen.

## Eigen meting (GEZIEN)
- Productnummers lopen op: 15.500.000 is 8 feb 2026, 17.000.000 is 12 jul 2026, 18.000.000 is 18 okt 2026. Dat is ±9.700 nummers per dag.
- Steekproef: 360 willekeurige nummers tussen 15.400.000 en 16.900.000 (eind jan t/m eind jun 2026, dus nu 4 tot ruim 9 maanden oud). Per pagina de productgegevens die TpT zelf in de pagina zet (releaseDate, prijs, aantal ratings, winkel). Script `data/tpt-haal-script.py`, data `data/tpt-steekproef-2026-11-09.jsonl`. 3 verzoeken tegelijk, rustig.
- Uitkomst: 199 nummers zijn een product (55%), 146 geven 404 (verwijderd of nooit gepubliceerd), 14 sturen door naar de winkel (product weg), 1 fout. Dus ±5.000 tot 5.300 nieuwe producten per dag die blijven staan, ±150.000 tot 160.000 per maand (raming uit de steekproef). 194 verschillende winkels in 199 producten.
- Van de 187 betaalde producten (mediaanprijs $3,75): **mediaan 0 ratings, 6 met 1 of meer (3%), 1 met 3 of meer, geen enkele met 10 of meer. Hoogste: 3 ratings.** Gratis producten (12): 1 met een rating.
- Omgerekend met de vuistregel van verkopers (5 tot 10% van de kopers geeft een rating, dus 10 tot 20 verkopen per rating, DERDEN hieronder): de beste twee producten van de 187 brachten in 4 tot 9 maanden elk ruwweg $150 tot $500 op voor de maker (3 ratings bij $15, 1 rating bij $27,60), de rest bijna niets. Mediaan: 0 verkopen zichtbaar.
- Zoeken: "fractions" geeft 256.832 resultaten (gezien door de onderzoeker). Geen gekochte advertentieplekken in de zoekpagina gevonden.

## Bronnen van derden (DERDEN)
- **TpT wordt "AI-free".** Rond 8 okt 2026 (town hall) kondigde TpT aan dat AI-gemaakt lesmateriaal verboden wordt; het beleid is aangekondigd maar nog niet ingegaan ("forthcoming"), en TpT bouwt tools om AI-materiaal op te sporen en te verwijderen. Volgens een verkopersblog (mikellane.com/tpt-ai-policy/, niet zelf nagelezen) geldt het ook voor covers, voorbeelden, beschrijvingen en bestaande producten. Zelf gelezen: "should be unique, expertly crafted, and AI-free" en "we're building tools that will speed up our ability to identify and remove AI-generated resources" (chalkbeat.org/2026/10/15/teachers-pay-teachers-to-ban-ai-generated-teaching-resources/). In augustus zei IXL al dat winkels met AI-materiaal lager in de zoekresultaten komen (chalkbeat.org/2026/08/03/ai-slop-on-teachers-curriculum-marketplace/).
- Nieuwe tarieven vanaf 1 jan 2027 (sellerblog.teacherspayteachers.com/tpt-exclusive-seller/, zelf gelezen: 77,5%): Basic $29 eenmalig, 55% plus $0,30 per verkoop; Exclusive $59,95 per jaar, 77,5%, maar dan mag je lesmateriaal nergens anders verkopen.
- Ratings: 5 tot 10% van de kopers geeft een rating (missbeccasclassroom.com, chaylorandmads.com).
- Inkomen: een enquête onder 967 verkopers (okt 2025) toont dat wie verdient meestal al 9+ jaar verkoopt met 100 tot 600+ producten. Een nieuwe tweede winkel met 23 producten: $538 in heel 2025. Een nieuwe verkoper die aantoonbaar $300+ per maand haalt: niet gevonden.

## Toets aan wat een 8 is
1. Nieuwe kleine makers verdienen er nu: **nee**. 3% van de nieuwe betaalde producten heeft na 4 tot 9 maanden één rating; geen nieuwe maker met $300+ per maand gevonden.
2. Bereik voor nieuwkomers: **nee**. ±150.000 tot 160.000 nieuwe producten per maand, zoeken beloont oude winkels met veel ratings.
3. Wij kunnen het bouwen en testen: technisch ja (pdf en slides met code), maar **het mag niet**: TpT heeft een verbod op AI-materiaal aangekondigd en bouwt tools om het te verwijderen. Dortus maakt alles met Claude. Verstoppen doen we niet.
4. Thijs kan snel verkopen: ja, $29 eenmalig vanaf 2027, uitbetaling via PayPal.

## Cijfer en advies
**Cijfer 1, nee.** Het aangekondigde AI-verbod alleen is al genoeg om af te vallen, en de eigen meting laat zien dat ook zonder dat verbod nieuwe producten bijna niets verkopen in een vloed van ±150.000 per maand. Ook geen productkans: de vraag zit bij leraren die een maker met ervaring in de klas vertrouwen.

Les voor andere markten met lesmateriaal of sjablonen (Boom Learning, Etsy, Creative Market): kijk eerst naar het AI-beleid, want de grote winkels gaan de kant van TpT op of zitten al vol met AI-werk.
