# Echte print voor Click Joints Pro (20 nov 2026, agent print-onderzoek, opdracht hoofdchat ±14:45 NL)

## Voorstel voor Thijs (geld: alleen na zijn ja)
1. **Laat de 4 testdelen (scharnier 115° en kogel, 1 bestand, 26 cm³) in PLA printen bij Elektronica Voor Jou** (Nederlandse winkel, Bambu Lab H2D, STL uploaden en direct prijs zien). **Totaal ±€15 met btw en brievenbuspost (GOK)**, opgebouwd uit hun tarieven: start €3,99 per bestand, €0,06 per gram PLA, €1,45 per printuur, alles zonder btw, brievenbus vanaf €3,99 (GEZIEN, zie A1).
2. **Binnen:** zij versturen binnen 3 werkdagen (GEZIEN). Besteld vóór ma 23 nov: binnen do 26 of vr 27 nov (GOK).
3. **Wat we ermee doen:** Thijs buigt het scharnier tot de stop en draait de kogel, filmpje van 10 s met de telefoon. Werkt het: filmpje naar de Maker van Roep (na keuring), post op r/3Dprinting (zijn account, zijn ja op de tekst), "print tested" op Gumroad, gratis testmodel op Printables. Werkt het niet: we weten het vóór een koper het merkt en passen de speling aan. Eén verkoop van Pro ($19) betaalt de print terug.
4. **Tweede keus:** een hobbyprinter via Marktplaats (Bambu Lab, €0,05 per gram, minimaal €5, GEZIEN), ±€10 met verzending (GOK), maar dat vraagt een bericht en een betaalverzoek vanaf zijn eigen account.
5. **Eerlijk alternatief, niets uitgeven:** "not print tested yet" blijft staan en we bieden de eerste koper of maker die een printfoto stuurt een gratis Pro-licentie. Kost geen geld, maar r/3Dprinting, Printables en Thangs blijven dicht tot iemand dat doet, en wanneer dat is weet niemand.

**Keuring: nog niet gedaan.** In deze sessie kon ik geen aparte keurder starten (geen Agent-gereedschap; de losse `claude` in de shell geeft een inlogfout). De hoofdchat zet er een keurder op (skill `keuren`, uitkomst in `echte-print-KEURING.md`) vóór dit naar Thijs gaat.

Wat al besloten is: 17 nov 13:40 "geen testprint" (Thijs, `organisatie/archief/besluiten-t-m-2026-11-18.md` regel 456) en 19 nov 14:00 "geen eigen 3D-printer, betaalde testprint nog niet goedgekeurd" (`organisatie/besluiten.md` regel 161). Dit stuk bestelt niets; het legt de keuze opnieuw voor met een exacte prijsopbouw.

---

## A. Printdiensten die in Nederland leveren

Prijzen alleen waar ik ze zelf met `curl` op de site las (GEZIEN, 20 nov), anders DERDEN met link of GOK. Nergens een account gemaakt of een bestand geüpload.

| Dienst | Prijs voor onze 4 delen | Levertijd naar NL | STL uploaden en direct betalen? | Oordeel |
|---|---|---|---|---|
| **A1. Elektronica Voor Jou** (NL, Bambu Lab-verkoper) | ±€15 met btw en brievenbus (GOK op grammen en uren, tarieven GEZIEN) | verzonden binnen 3 werkdagen (GEZIEN), PostNL/GLS/DHL | ja, calculator op de site (GEZIEN) | **beste keus** |
| **A2. Marktplaats, hobbyprinters** | €5 minimum (GEZIEN, 1 aanbieder) + post ±€5 (GOK) = ±€10 | hangt van de printer af, GOK 2 tot 5 dagen | nee, eerst een bericht en prijsopgave | goede tweede, wel contact nodig |
| A3. JLC3DP (China) | hars vanaf $0,30 per deel (GEZIEN); totaal GOK €10 tot €15 gewone post, €25 tot €35 met DHL; plus €3 invoerrecht per soort artikel (GEZIEN) | 2 tot 3 dagen maken (GEZIEN) plus GOK 7 tot 15 dagen post: begin dec | ja, met account | te laat en hars, zie onder |
| A4. Craftcloud (netwerk van printers, ook NL) | onbekend: site geeft 403 op curl | onbekend | offerte vraagt eerst hun voorwaarden accepteren (`testprint/LEESMIJ.md`) | niet te toetsen zonder Thijs |
| A5. Treatstock | geen prijs zonder upload (site laadt, GEZIEN) | onbekend | ja, met upload | niet getoetst |
| A6. Shapeways (weer gestart in Eindhoven) | onbekend; op de site alleen technische FDM-materialen (ABS, ASA, PETG en meer), geen PLA (GEZIEN) | onbekend | zakelijk gericht | GOK duurder, niet nodig |
| A7. Hubs (Protolabs) | voorbeelden FDM $2,80 tot $7,92 per stuk (GEZIEN op hun NL-pagina), totaal GOK €30 of meer | SLA vanaf 2 werkdagen (GEZIEN) | ja | zakelijk, duurder dan A1 |

### A1. Elektronica Voor Jou: hoe ik op ±€15 kom
Bron: https://elektronicavoorjou.nl/3d-print-service/ en https://elektronicavoorjou.nl/retour-verzendbeleid/ (GEZIEN met curl, 20 nov).
- Tarieven zonder btw: startkosten **€3,99 per bestand** ("ongeacht het aantal stuks"), **PLA €0,06 per gram**, **€1,45 per printuur**. Geen minimum aantal, particulier mag, "binnen 3 werkdagen verzonden" (gebaseerd op vijf objecten), verkeerde print door hun fout wordt gratis opnieuw gemaakt. Geprint op Bambu Lab H2D.
- Verzenden: brievenbus (alleen NL) **vanaf €3,99**, pakket GLS €6,45 of PostNL €6,95 (GEZIEN; of daar btw in zit staat er niet).
- Rekensom (GOK op gewicht en tijd): 26 cm³ massief is 32 g PLA (eigen som, dichtheid 1,24); met wanden en vulling GOK 20 tot 32 g = €1,20 tot €1,94. Printtijd vier kleine staafjes GOK 1,5 tot 3 uur = €2,18 tot €4,35. Plus €3,99 start = €7,37 tot €10,28 zonder btw, **€8,92 tot €12,44 met 21% btw**, plus brievenbus €3,99 = **€12,91 tot €16,43, afgerond ±€15**.
- Belangrijk: **upload één bestand**, niet vier. Vier losse STL's kosten 4 x €3,99 = €15,96 alleen al aan startkosten. Daarom staat er nu `testprint/testset-4-delen.stl` (zie B).
- Open: of bestellen zonder account kan, zag ik niet (de site heeft een inlogknop). Het afleveradres vult Thijs zelf in; dat komt nooit in de repo.

### A2. Marktplaats
- Zoekopdracht "3d print service" gaf **284 advertenties** (GEZIEN, via de zoek-API van marktplaats.nl, 20 nov).
- Voorbeeld met prijs: advertentie m2466120333, "€0,05 per gram filament, minimale besteding €5 (ca. 50 gram)", print op een Bambu Lab P2S, ophalen of verzenden (GEZIEN, https://www.marktplaats.nl/v/computers-en-software/3d-printers/m2466120333-3d-print-service-0-05-per-gram-snel-netjes). Onze set weegt minder dan 50 g, dus €5 plus post.
- Nadeel: Thijs moet een onbekende aanschrijven en betalen via een betaalverzoek (harde regel 4: zijn ja op de tekst). Snelheid en kwaliteit hangen van één persoon af. Voordeel: printer en materiaal zijn precies wat onze kopers thuis hebben.

### A3. JLC3DP: waarom niet nu
- Hars 9600: "From $0.3", bouwtijd 48 uur, **maattolerantie ±0,2 mm** en wand liever dikker dan 0,8 mm (GEZIEN, https://jlc3dp.com/help/article/photosensitive-9600-resin). Onze speling is ook 0,2 mm: het gewricht kan dus net vastzitten of net los zijn door de dienst, niet door ons. FDM bij JLC heeft minimaal 30 x 30 x 10 mm (GEZIEN, https://jlc3dp.com/3d-printing/fused-deposition-modeling); onze delen zijn 14 tot 20 mm breed.
- Sinds 1 juli 2026 betaalt een particulier in de EU **€3 invoerrecht per soort artikel** onder €150, plus mogelijk kosten van de vervoerder (GEZIEN, https://jlc3dp.com/news/eu-customs-reform2026).
- Een gebruiker betaalde $2,70 met verzending voor één klein harsdeel naar Australië in 2024 (DERDEN, https://hackaday.io/page/395320-trying-out-jlcs-3d-printing-service). Goedkoop, maar met gewone post komt het niet vóór 26 nov aan (GOK) en hars is broos voor klikdelen en niet wat de meeste lezers van r/3Dprinting thuis printen (GOK).

### Gratis wegen (geen dienst)
- Een FabLab of een bibliotheek met printer: Thijs print zelf, GOK een paar euro, kost zijn tijd en een bezoek. Geen plaats genoemd (privé).
- Iemand die hij kent met een printer (al voorgesteld op 16 nov, `berichten/hoofdchat.md`).
- Een maker uit `commercie/blender-click-joints/makers.md` vragen: dat is iemand benaderen, alleen Thijs.

## B. Welk testobject, welke bestanden

**Sturen: `commercie/blender-click-joints/testprint/testset-4-delen.stl`** (nieuw, vandaag samengevoegd uit de vier bestaande delen, niets aan de vorm veranderd).
- Inhoud: `scharnier-115-deel-A` en `-B` (staaf 14 mm dik, scharnier met eindstop 115°) en `kogel-deel-A` en `-B` (staaf 20 mm dik, kogelgewricht), naast elkaar met 10 mm ruimte, plat op z = 0.
- Maat: **98 x 20 x 44,5 mm, 26,05 cm³, 14.368 driehoeken, 702 kB** (GEZIEN, eigen meting; de vier losse bestanden samen ook 26,05 cm³).
- Gemaakt met de echte Pro-code 1.0.2 in bpy 5.3.0, speling 0,2 mm (`testprint/LEESMIJ.md`, `testprint/maak.py`). Of de gewrichtsvorm in 1.1.0 anders is, weet ik niet (GOK: nee, 1.1 voegde vooral "Figure from rig" toe). Bram kan dat in één regel bevestigen; zo niet, `maak.py` opnieuw draaien met de 1.1-zip.
- Vraag bij de bestelling: PLA, 0,2 mm laag, delen los printen; daarna zelf in elkaar klikken.

Waarom dit en niet meer:
- Een "been met knie" en een "arm met kogel" zijn precies deze twee staven: goedkoop (±€15) en ze laten de twee dingen zien die we beloven, de stop bij 115° en een kogel die draait.
- **Overtuigender maar duurder: een hele figuur** van ±200 mm uit de e2e-figuren (`producten/blender-gewrichten/e2e/proef_mens.py`). Bij A1 tellen vooral de printuren: GOK 8 tot 12 uur en 60 tot 100 g = €30 tot €45 met btw en post. Pas doen als de staven werken.
- **Fit test strip** (vijf gewrichten van 0,10 tot 0,30 mm, knop in Pro, `click_joints/betaald/testkaart.py`): beantwoordt meteen "welke speling werkt op een gewone printer". De STL's staan nog niet in de repo (de e2e-toets exporteert ze alleen naar een tijdelijke map). Kost Bram één run om ze als één bestand te bewaren; bij A1 GOK €9 tot €11 extra als tweede bestand. Goede tweede bestelling, of mee in de eerste als het bestand vóór de bestelling klaar is.

## C. Printables en MakerWorld: Pro verkopen met een gratis printbaar model

### Wat mag
- **Printables:** de regelpagina geeft 403 op curl. De gebruiksvoorwaarden verbieden wel "unsolicited messages or commercial communications to other Users" via de berichtenfunctie, maar niets over een link in een modelbeschrijving (GEZIEN, https://www.prusa3d.com/page/printables-com-terms-of-service_231249/). Op het Prusa-forum vinden gebruikers een koop-link prima zolang het model compleet en printbaar is; "teasers" (een los deel dat niets doet zonder iets te kopen) vinden ze vervelend (DERDEN, meningen uit 2022, geen officieel antwoord: https://forum.prusa3d.com/forum/english-forum-general-discussion-announcements-and-releases/is-that-okay-to-add-buy-ready-made-link-on-printables).
- **Voorbeeld dat het werkt op Printables:** TrailPrint3D, een Blender-add-on, staat er als model met een gratis add-on en links naar Patreon voor een versie met extra functies, naar de eigen site en naar Amazon: **3.882 downloads, 1.198 likes** (GEZIEN via de openbare API van Printables, 20 nov, https://www.printables.com/model/1242540). Dat is bijna ons plan: gratis iets nuttigs, betaalde versie via een link.
- **MakerWorld:** de richtlijnen geven 403. Volgens gebruikers op het Bambu-forum zegt regel 7 "Do not post advertising information or links on your account name, description, pictures, etc." en verbiedt de update van dec 2024 links naar "non-MakerWorld related businesses, organizations, online stores, or websites" (DERDEN, https://forum.bambulab.com/t/sponsored-advertising-patreons-and-exclusives/110782 en https://forum.bambulab.com/t/updated-community-guidelines-question-advertising/125791). MakerWorld zelf antwoordde in mei 2026 dat ze het "case by case" beoordelen (DERDEN, https://forum.bambulab.com/t/fiverr-link/251364). TrailPrint3D staat er ook, 8.324 downloads (GEZIEN via hun zoek-API), maar of daar een link in staat zag ik niet. Dus op MakerWorld: **geen link**, alleen "made with Click Joints Pro for Blender" in tekst (GOK dat dat mag).

### Bereik van vergelijkbare modellen (GEZIEN via de API's, 20 nov)
| Zoekwoord | Plek | Aantal | Grootste | Mediaan in steekproef |
|---|---|---|---|---|
| articulated figure | Printables | 253 | Iron Man MK3, 15.741 downloads | 428 (60 modellen) |
| dummy 13 (beweegbare figuur) | Printables | 2.756 | Dummy 13 v1.0, 331.968 downloads | 7.123 (60) |
| poseable action figure | Printables | 19 | 1.782 downloads | 160 |
| ball jointed doll | Printables | 5 | Eve, 1.023 downloads | 98 |
| tolerance test | Printables | 267 | Clearance Tolerance Test, 76.866 downloads | 376 (60) |
| hinge test | Printables | 31 | Hinge tolerance test, 367 downloads | 40 |
| articulated figure | MakerWorld | 3.425 | Dummy 13 Easy, 30.867 downloads | (eerste 20 bekeken) |
| ball jointed doll | MakerWorld | 1.478 | Ragdoll Toy, 8.005 downloads | (eerste 20 bekeken) |

Les: een **speling-testje** is een bewezen soort model (76.866 downloads voor één testje) en past precies bij Pro ("print this first"). Een gratis "Click Joints hinge and ball fit test" op Printables met de link naar Pro is dus de logische eerste upload. Hoeveel downloads tot verkopen leiden, weet niemand (GOK, geen cijfers gevonden).

### Een niet-geteste print uploaden?
**Nee, eerlijk gezegd een slecht idee.** Ik vond geen regel die het verbiedt, maar Printables en MakerWorld tonen "makes" en reacties van mensen die het printten. Zit het eerste gewricht vast of valt het uit elkaar, dan staat dat openbaar onder ons model en onder de naam van Pro. Bovendien beloven we dan wat besluit 17 nov 13:40 juist verbiedt. Eerst onze eigen print (A1), met foto's daarvan als omslag.

### Account
Printables (Prusa-account) en MakerWorld (Bambu-account) vragen een account: **eerst een ja van Thijs**. Kost geen geld.

## Wat dit oplevert in geld (GOK)
- Kosten ±€15 (A1) of ±€10 (A2). Pro kost $19; één extra verkoop betaalt het terug.
- Wat opengaat: r/3Dprinting (software zonder print: mediaan 2 punten en 6 van 13 posts weggehaald; TrailPrint3D met print: 400 tot 2.500 punten; eerder gezien door Joris, `berichten/hoofdchat.md` 16 nov), Printables, Thangs (printfoto verplicht), een filmpje met een hand, en de zin "print tested" op Gumroad. Hoeveel verkopen dat geeft is een GOK; zonder print blijven die plekken in elk geval dicht.

## Bronnen nagelezen in de repo
`platformen/blender-2/gumroad-1.1.md`, `commercie/blender-click-joints/testprint/`, `organisatie/besluiten.md` (regel 47 en 161), `organisatie/archief/besluiten-t-m-2026-11-18.md` (regel 456), `commercie/blender-click-joints/verspreiding.md` (punt 8), `platformen/blender-2/testkaart-ontwerp.md`, `berichten/hoofdchat.md` (Stijn 16 en 17 nov).
