# Voorstel: Printables (3D-printmodellen, Prusa)

Vera, 8 nov 2026 run 10:33 UTC (tweede platform van deze run). Zelf toegevoegd als vergelijking met MakerWorld, omdat Printables wel een winkel voor betaalde modellen heeft.

## In het kort
- **Advies: nee voor nu, cijfer 3.**
- **Geld kan echt:** in de Printables Store verkoopt iedereen betaalde modellen (minimum $5), Prusa houdt 20% plus Stripe-kosten, de rest gaat contant naar je eigen Stripe-account (GEZIEN, voorwaarden en blog Prusa).
- **Maar nieuwe betaalde modellen verkopen bijna niet:** van de 1.727 modellen met een losse prijs uit mei t/m aug 2026 heeft 94% geen enkele beoordeling (5,6% heeft er minstens één). Bij makers met minder dan 20 betaalde modellen: 80 van 932 (8,6%) (GEZIEN, nagerekend door de controleur).
- **Gratis bereik is gewoon:** nieuwe gratis modellen mei t/m aug mediaan 11 downloads, 8,6% haalt 100+ (GEZIEN, steekproef 324). Ongeveer gelijk aan MakerWorld, maar met minder publiek (22 miljoen bezoeken per maand tegen 63 miljoen, DERDEN).
- Gratis modellen leveren alleen Prusameters op, winkeltegoed voor filament, geen geld (GEZIEN).

## Wat ik gemeten heb (GEZIEN)
Bron: de openbare GraphQL-API die de site zelf gebruikt, `api.printables.com/graphql/` (geen robots.txt op die host; robots.txt van printables.com staat alles toe behalve /world/). De gewone webpagina's geven 403; niet omzeild. De API knijpt bij te veel verzoeken ("Request was throttled"); daarna ben ik gestopt, heb gewacht en ben trager doorgegaan (1 verzoek per 1,5 tot 2,5 s).

Velden per model: firstPublish (eerste publicatie; datePublished verschuift bij een update), downloadCount, likesCount, makesCount, ratingCount, price, premium (Club), aiGenerated, maker, categorie. **Bij betaalde modellen zijn downloads en aankopen verborgen** (downloadCount en purchaseCount zijn leeg).

Bestanden in `data/`: `printables-betaald-2026-11-08.jsonl` (alle 7.650 betaalde modellen van 8 nov terug tot 4 mrt 2026, via de lijst met `paid: paid`, nieuwste eerst), `printables-steekproef-2026-11-08.jsonl` (459 willekeurige id's tussen 1.700.000 en 1.830.000), scripts `printables-betaald-script.py`, `printables-haal-script.py`, `printables-analyse-script.py` (`vrij <bestand>` of `betaald <bestand>`).

### Betaalde modellen (allemaal, eerste publicatie mei t/m aug 2026)
| Groep | Aantal | 1+ beoordeling | 5+ | 10+ | Mediaan likes |
|---|---|---|---|---|---|
| Alle | 3.812 | 3% | 0,2% | 0,1% | 1 |
| Mei | 803 | 4% | 0,1% | 0,1% | |
| Augustus | 1.714 | 2% | 0,1% | 0% | |
| Makers met minder dan 20 betaalde modellen in die maanden | 1.136 (508 makers) | 95 (8%) | 9 | 3 | 2 |
| Alleen modellen met een losse prijs (geen Club) | 1.727 | 5,6% | | | |
| Daarvan makers met minder dan 20 | 932 | 80 (8,6%) | | | |

Let op: de lijst `paid: paid` bevat ook 2.085 modellen alleen voor Club-leden zonder losse prijs (55%). Dat zijn geen losse verkopen; de bovenste rijen tellen die mee, de onderste twee niet. Alle: 96,4% zonder beoordeling.

- Een beoordeling kan alleen wie het model gedownload heeft (DERDEN, beheerder Prusa op het forum, 2022), en een betaald model downloaden kan alleen na kopen. Het aantal beoordelingen is dus een **ondergrens** voor het aantal verkopen. Hoeveel kopers er per beoordeling zijn weet ik niet; ik reken met 1 op 10 tot 1 op 30 (GOK). Makes en beoordelingen lopen hier bijna gelijk op.
- Drukte betaald: mei 803, jun 735, jul 560, aug 1.714, sep 1.376, okt 1.101 nieuwe betaalde modellen. De piek in augustus komt vooral van twee uploaders (913 en 447 modellen in mei t/m aug samen; 941 daarvan in augustus). De grootste, ModelMagic, zette 913 Club-modellen neer, allemaal met AI-label (GEZIEN).
- 1.214 van de 3.812 hebben het AI-label, maar bij de modellen met een losse prijs maar 72 (GEZIEN).
- Mediaanprijs $5, het minimum (GEZIEN).
- **Het beste voorbeeld van een kleine maker:** BruceLeedleLe (speelgoedblasters met foam darts), 10 betaalde modellen van $5 tot $8 sinds maart. Beste model (jul): 42 beoordelingen, 46 makes, 272 likes. Samen ±157 beoordelingen. Met 1 op 10 tot 1 op 30 is dat ±1.600 tot 4.700 verkopen; netto ±$5,1 per verkoop ($7 min 20% en Stripe) geeft ±$8.000 tot $24.000 in 8 maanden (GOK). Dit is één maker; per model hebben alle andere nieuwe modellen van kleine makers 7 beoordelingen of minder, per maker komen Afrikaners (11, met prijs) en Wekster (16, Club) het dichtst in de buurt.

### Gratis modellen (steekproef)
459 id's, waarvan 350 een zichtbaar model; 324 gratis met eerste publicatie mei t/m aug.

| Eerste publicatie 2026 | Aantal | Mediaan downloads | 100+ | 0 downloads |
|---|---|---|---|---|
| Mei | 99 | 19 | 11,1% | 0% |
| Juni | 88 | 8 | 6,8% | 1% |
| Juli | 85 | 9 | 7,1% | 1% |
| Augustus | 52 | 8 | 9,6% | 6% |
| Alle | 324 | 11 | 8,6% | 2% |
| Met AI-label | 66 | 33 | 18,2% | 0% |

- Opvallend: modellen met AI-label doen het hier beter (mediaan 33), tegen MakerWorld in. Kleine groep, oorzaak onbekend (GOK: veel daarvan zijn figuren of plaatjes die mensen snel downloaden).
- Drukte gratis: ±76% van de id's is een zichtbaar model, ±105.000 id's in 4 maanden, dus ±20.000 nieuwe modellen per maand (GOK; de controleur komt via de id-reeks per maand op 20.000 tot 24.000). Vijf keer rustiger dan MakerWorld.

## Geld en regels (onderzoeker, bronnen onderaan)
- Store sinds 13 dec 2023. Iedereen mag verkopen; je begint met 1 plek voor een betaald model, na 5 verkopen 5 extra (DERDEN, een verkoper). Aanmelden met echte gegevens en Stripe-controle, Prusa mag weigeren (GEZIEN). Voor Dortus betekent dat: Thijs moet zich aanmelden en Stripe koppelen.
- Afdracht 20% plus Stripe, geen maandbedrag. Maker regelt zelf btw (GEZIEN).
- Clubs: abonnement per maker, $3 tot $100 per maand, 10% afdracht (GEZIEN).
- Prusameters: 10 tot 200 per model per 30 dagen bij 30 tot 400 downloads; 350 punten is een tegoedbon voor 1 rol filament. Geen geld (GEZIEN).
- AI: filter om AI-modellen te verbergen, veel klachten over "AI slop" op het forum, geen verbod op verkoop gevonden (DERDEN, GOK).
- Geen bedragen van kleine makers gevonden, Prusa noemt geen totaal dat aan makers is uitbetaald.

## Past het bij ons?
- Bouwen: functionele modellen met code kan, maar we hebben geen printer om te testen, en bij betaalde modellen verwacht een koper dat het in één keer goed print. Het enige sterke voorbeeld (blasters) draait om mechaniek die je echt moet testen.
- Verkopen: Thijs moet een Stripe-account koppelen (lijst Thijs), en bij 1 betaalde plek in het begin is het traag op te bouwen.

## Voor- en nadelen
- Voor: echte contante verkoop met 80%, open voor iedereen, rustiger dan MakerWorld, gratis modellen krijgen bijna altijd een paar downloads.
- Tegen: 94% van de nieuwe modellen met een prijs heeft na 3 tot 6 maanden geen beoordeling; verkopen zijn verborgen; kleiner publiek dan MakerWorld; zonder printer niet te testen.

## Wat het oordeel zou veranderen
Een betrouwbare verhouding tussen beoordelingen en verkopen (een maker die beide deelt), of meer kleine makers zoals de blastermaker. Herhaalmeting over 4 weken: zelfde betaald-lijst opnieuw ophalen en kijken of de beoordelingen bij de lichting mei t/m aug groeien.

## Controle
Controleur akkoord met correcties (8 nov 2026): alle tellingen met eigen code gelijk, 8 van 8 live gelijk. Correcties verwerkt: Club-modellen apart gezet (55% van de betaald-lijst), 96% in plaats van 97%, uitspraak over andere makers per model, rekensom gelijkgetrokken en netto per verkoop.

## Bronnen (gelezen 8 nov 2026)
- api.printables.com/graphql/ (eigen meting), printables.com/robots.txt
- blog.prusa3d.com/printables-store_87810/
- prusa3d.com/page/printables-club-store-terms-and-conditions-for-creators_236503
- blog.prusa3d.com/printables-clubs-are-live-you-can-now-support-the-creators-you-love-on-printables_81063/
- help.prusa3d.com/article/how-do-prusameters-on-printables-work_365065
- forum.prusa3d.com: printables-rating-system-issue, printables-filter-out-ai-models, ai-slop-has-to-stop-no-pun-intended, printables-rewards
- tildes.net/~games.tabletop/1dhf (verkoper, jan 2024)
- cw.semrush.com/website/printables.com/overview
