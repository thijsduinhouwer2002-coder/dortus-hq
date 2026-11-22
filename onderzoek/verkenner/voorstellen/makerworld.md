# Voorstel: MakerWorld (3D-printmodellen, Bambu Lab)

Vera, 8 nov 2026 run 10:33 UTC. Zelf toegevoegd: groot en snel groeiend, makers krijgen punten op downloads en prints.

## In het kort
- **Advies: nee voor nu, cijfer 3.**
- **Bereik is goed** voor een open platform: nieuwe modellen van mei 2026 (nu 5 tot 6 maanden oud) halen mediaan 10 downloads, 13,8% haalt 100+ en 2,3% haalt 1.000+ (GEZIEN, eigen steekproef).
- **Geld is zwak.** Je kunt op MakerWorld geen model verkopen. Makers krijgen punten, vooral als tegoed in de Bambu-winkel. Een gemiddeld nieuw model levert in 6 maanden rond $5 tot $8 op, een mediaan model minder dan $1 (GOK op gemeten aantallen en gemelde puntwaarde). Contant geld kan via punten van Exclusive-modellen (vanaf $100, ±20 tot 25% minder waard dan tegoed, DERDEN), via commissie op onderdelenlijsten (BOM) en via het licentie-abonnement; die twee vragen eerst volgers, prints of verkoop (GEZIEN).
- **Heel druk:** ±100.000 nieuwe modellen per maand (GOK op eigen steekproef).
- Makers melden dat de opbrengst per download in 2026 met 30 tot 50% daalde (DERDEN).

## Wat ik gemeten heb (GEZIEN)
Bron: de open API van MakerWorld, `makerworld.com/api/v1/design-service/design/<id>`. robots.txt (`makerworld.com/en/robots.txt`) staat alles toe behalve inloggen, aanmelden, /my en /policies. De gewone webpagina's geven een Cloudflare-uitdaging (403); die heb ik niet omzeild. De API geeft per model: aanmaakdatum, downloads, prints, likes, Exclusive ja/nee, licentie, boosts, AI-label, maatwerk-tellingen en betaalvelden.

De id's lopen op met de tijd (id 2.742.000 ≈ 1 mei 2026, 3.245.000 ≈ 1 sep 2026). Ik nam 1.600 willekeurige id's uit dat bereik, 2 verzoeken tegelijk met 0,5 s pauze. 1.328 waren gepubliceerde modellen met een maker, 272 waren niet zichtbaar (102 status 2, 124 status 3, 46 status 4: verwijderd, verborgen of niet gepubliceerd).

Bestanden in `data/`: `makerworld-steekproef-2026-11-08.jsonl`, `makerworld-haal-script.py` (argumenten: laagste id, hoogste id, aantal, uitvoerbestand, seed; gebruikt: 2742000 3245000 1600 ... 81), `makerworld-analyse-script.py`.

| Groep (gemaakt in 2026) | Aantal | Mediaan downloads | 100+ | 1.000+ | 0 downloads | Mediaan prints |
|---|---|---|---|---|---|---|
| Mei | 341 | 10 | 13,8% | 2,3% | 9,7% | 5 |
| Juni | 344 | 8 | 9,3% | 1,2% | 12,2% | 4 |
| Juli | 304 | 5,5 | 6,6% | 0,7% | 15,5% | 3 |
| Augustus | 337 | 4 | 5,3% | 0,6% | 22,0% | 2 |
| Alle mei t/m aug | 1.328 | 6 | 8,8% | 1,2% | 14,9% | 3 |
| Exclusive | 391 | 16 | 16,9% | 2,8% | 6,9% | 12 |
| Niet Exclusive | 937 | 4 | 5,4% | 0,5% | 18,2% | 2 |
| Categorie Generative 3D Model (de vlag isAIGC stond bij geen enkel model aan) | 69 | 3 | 2,9% | 0% | 15,9% | 3 |
| Met maatwerk (Parametric/MakerLab, designCustomizeCount > 0) | 42 | 10 | 9,5% | 2,4% | 4,8% | 6,5 |

- De rij "Alle mei t/m aug" bevat 2 modellen met een datum eind 2025 (id's lopen niet helemaal gelijk met de tijd); de maanden samen zijn 1.326.
- Gemiddeld (niet mediaan): mei 104 downloads, 68 prints, 3 boosts per model; alle mei t/m aug 64 downloads en 45 prints (GEZIEN).
- Scheef verdeeld: de beste 1% van de modellen heeft 39% van alle downloads (GEZIEN).
- Bijna elke maker komt één keer voor in de steekproef (1.231 makers voor 1.328 modellen), dus het zijn vooral veel kleine makers (GEZIEN).
- Geen enkel model in de steekproef heeft `isPaid`, crowdfunding of een puntenprijs (`pointRedeemDetail`) aan staan. Geen staff picks (GEZIEN).
- Grootste categorieën: Decor, speelgoed, hobby, organizers, huis, figuren (GEZIEN).
- Let op: verwijderde modellen tellen niet mee, dus de cijfers zijn eerder iets te gunstig (GOK).

### Drukte
83% van de id's is een gepubliceerd model. Over ±503.000 id's in 4 maanden is dat ±104.000 nieuwe modellen per maand (GOK, uitgaande van één id-reeks voor alleen modellen).

## Geld (onderzoeker, bronnen in de lijst onderaan)
- **Punten:** sinds juni 2025 met een geheime formule (downloads, prints, originaliteit, presentatie) (GEZIEN, forum 172869). Oude vuistregel: score = downloads + 2 × prints, met dalende staffels (DERDEN).
- **Waarde:** cadeaubon $200 kost 2.450 punten, dus 1 punt ≈ $0,08 tegoed (DERDEN, forum 250697, apr 2026). Rond 2024: ±40 downloads per $1 (DERDEN). Sinds mrt en jun 2026 melden makers 30 tot 50% minder punten (DERDEN, forum 254812). Schatting nu: $10 tot $20 tegoed per 1.000 downloads (GOK).
- **Contant:** alleen Exclusive-punten, minimum $100, ±20 tot 25% minder dan tegoed (DERDEN). Exclusive mag pas als de maker over al zijn modellen samen 100 prints heeft, het model mag nergens anders staan, en AI-modellen, Hueforges, platte modellen, sleutelhangers, onderzetters, bladwijzers, varianten (V2) en modellen uit MakerLab-tools zijn uitgesloten (GEZIEN, wiki exclusive-model-guideline, zelf nagelezen).
- **Boosts:** ±12 punten per boost, 15 bij Exclusive (DERDEN, mrt 2026), dus ±$1. Gemiddeld model mei: 3 boosts (GEZIEN).
- **Model verkopen kan niet** (DERDEN; verzoek op het forum mei 2026). Wel: licentie-abonnement voor makers vanaf 200 volgers en 600 prints (maker kiest $3 tot $300 per maand, MakerWorld houdt 10%), crowdfunding alleen op uitnodiging, en commissie van 3 tot 15% op onderdelenlijsten (BOM), contant uitbetaald, vanaf 500 volgers of 1 CyberBrick-model of $100 BOM-omzet in 12 maanden of 20 bestellingen; volgens de wiki verdienen sommige makers daar meer dan $1.000 per maand mee (GEZIEN, blog en wiki).
- **Kleine makers:** geen hard maandbedrag gevonden. Eén onbekende maker meldde in juni 2025 ±$10 per dag tegoed, daarna minder (DERDEN). Reddit en YouTube niet gecontroleerd.

### Rekensom (GOK)
Gemiddeld nieuw model van mei: 104 downloads + 68 prints + 3 boosts in 6 maanden. Met $10 tot $20 per 1.000 (geschat per 1.000 downloads, hier toegepast op de score met prints dubbel; dat is een extra aanname) en ±$1 per boost is dat ±$5 tot $8, grotendeels als winkeltegoed. Het gemiddelde komt vooral van de beste 1%; een mediaan model (10 downloads, 5 prints) haalt minder dan $1. Voor $300 contant per maand zou je honderden Exclusive-modellen per maand nodig hebben, en Exclusive weert juist AI en generatoren.

## Vindbaarheid
Trending, zoeken en categorieën op de site, en de Bambu Handy-app en Bambu Studio, waar printers direct vanuit MakerWorld printen (DERDEN). Nieuwe modellen krijgen wel bereik: maar 10% van de mei-modellen bleef op 0.

## Grootte (DERDEN)
Ongeveer 10 miljoen maandgebruikers eind 2025 (technode, 30 okt 2026). Semrush sep 2026: makerworld.com 62,6 miljoen bezoeken, printables.com 22,0 miljoen, thingiverse.com 16,1 miljoen.

## Past het bij ons?
- Ja voor het maken: functionele modellen met code (OpenSCAD of CadQuery) kunnen we in dagen maken, en Bram werkt al met 3MF. Maar zonder printer kunnen we niets echt testen, en een mislukte print kost reviews.
- Nee voor het verdienmodel: tegoed in een winkel is geen omzet voor Dortus, en contant geld zit achter Exclusive (regels sluiten AI-werk uit), of achter volgers en verkoop (BOM-commissie, licentie-abonnement).

## Voor- en nadelen
- Voor: groot publiek dat groeit, open API, nieuwe makers krijgen meetbaar bereik, Exclusive-modellen halen ±4 keer zoveel downloads (mediaan 16 tegen 4), maar dat is samenhang: alleen makers met al 100 prints mogen Exclusive doen.
- Tegen: geen verkoop, punten zijn vooral tegoed, opbrengst daalt, ±100.000 nieuwe modellen per maand, AI-modellen doen het slechter (mediaan 3) en zijn uitgesloten van Exclusive, geen printer om te testen.

## Eerste idee (alleen als het geld verandert)
Een reeks parametrische, functionele modellen (organizers, houders voor gereedschap), elk ook als losse vaste varianten. Of: MakerWorld gebruiken als gratis etalage voor een betaald product elders (bijvoorbeeld een Blender-add-on van Bram met printbare onderdelen). Dat laatste is een idee voor Bram, geen platform.

## Wat het oordeel zou veranderen
Als MakerWorld betaalde modellen opent met contante uitbetaling. Dan opnieuw meten met hetzelfde script (bereik is al bekend). Herhaalmeting kan altijd met `data/makerworld-haal-script.py`.

## Controle
Controleur akkoord met correcties (8 nov 2026): alle tabelcijfers herrekend en gelijk, 15 van 15 modellen live gelijk, id-grenzen kloppen, wiki-beweringen kloppen. Correcties verwerkt: statussen van lege id's, drempel 100 prints per maker, alle toegangen en contante uitbetaling van BOM-commissie, Exclusive als samenhang (4 keer, niet 2), 2 modellen uit 2025, AI-groep alleen op categorie, eenheden in de rekensom.

## Bronnen (gelezen 8 nov 2026)
- makerworld.com/en/robots.txt en makerworld.com/api/v1/design-service/design/<id> (eigen meting)
- wiki.bambulab.com/en/makerworld/tutorials/exclusive-model-guideline (zelf nagelezen: 100 prints, AI en MakerLab uitgesloten)
- wiki.bambulab.com/en/makerworld/tutorials/creator-commission-incentives
- wiki.bambulab.com/en/makerworld/release-note/makerworld-release-notes
- blog.bambulab.com/empowering-our-creators-with-new-commercial-license-membership
- forum.bambulab.com/t/ nummers 172869, 186216, 149977, 254812, 250697, 237903, 189658, 119890, 242963, 253854, 253073, 256884, 254093
- technode.com/2026/10/30/how-bambu-lab-turned-3d-printing-into-a-consumer-hit/
- semrush.com/website/makerworld.com/overview/
