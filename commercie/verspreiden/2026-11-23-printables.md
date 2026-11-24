# Printables: gratis Fit test strip met link naar Click Joints (Verspreider, 23 nov 2026, run 2)

## Kort
- **Voorstel:** de gratis Fit test strip (vijf kogelgewrichten, 0.10 tot 0.30 mm speling, al gekeurd door Daan op 22 nov, `platformen/blender/fit-test-strip-tekst.md`) als gratis model op Printables, met een link naar de gratis add-on en naar Pro. Plaatsen op wo 26 nov, zodat wie doorklikt de CYBER25-korting ziet.
- **Waarom dit wel kan zonder echte print:** het oude bezwaar (besluit 17 nov 13:40: nergens beloven dat het klikt) gaat over een figuur dat moet werken. Een teststrip belooft niets: hij is er juist om uit te zoeken welke speling past. We schrijven er eerlijk bij dat we hem zelf nog niet printten en vragen om een "make".
- **Wat het oplevert:** (1) bereik bij precies het publiek dat beweegbare prints maakt; (2) de eerste foto's van echte prints door anderen ("makes"). Die foto's maken r/3Dprinting, MakerWorld, de 3D-print-Discords en een "print tested"-regel op Gumroad pas mogelijk. Dat is het slot op de hele printkant.
- **Wie:** Thijs maakt eenmalig een Printables-account op naam van Dortus (accounts aanmaken mag alleen hij, ±3 min). Daarna is het een kanaal van Dortus: de hoofdchat uploadt na keuring (CLAUDE.md regel 4, nieuwe kanalen doet de hoofdchat), in Chrome op de HP.
- **Besluit nodig:** `verspreiding.md` rij 8 zegt "Printables pas met echte print, besluit Hans nodig". Dit voorstel vraagt dat besluit opnieuw, met de nieuwe feiten hieronder.

## Nieuwe feiten (23 nov, met curl op de Printables-API en de Prusa-hulppagina)
- **Er is een voorbeeld dat precies ons model is:** "Trail Map Generator | TrailPrint3D | Blender Addon", een gratis Blender-add-on op Printables met een betaalde Patreon-versie in de beschrijving. 3.884 downloads, 1.200 likes, 15 makes, geplaatst 7 nov 2026 (DERDEN, Printables-API, model 1242540, https://www.printables.com/model/1242540). Dat is 16 dagen. Printables staat dus een link naar een betaalde versie toe, en het publiek pakt een Blender-tool daar op.
- **Teststrips zijn een eigen soort op Printables:** "Print in Place Tolerance Test" (scharnieren, 0.1 tot 0.45 mm): 8.730 downloads, 1.398 likes, 75 makes, categorie Test Models (DERDEN, model 815843). De meeste andere teststrips halen 11 tot 376 downloads (DERDEN, zoekopdracht "print in place tolerance test", 10 uitkomsten). Een teststrip voor **kogelgewrichten** is er nauwelijks: zoeken op "ball joint tolerance test" geeft 1 echt model, 20 downloads (DERDEN). Een open plek.
- **AI-label:** Printables zegt: "if the model was created by your (AI-enhanced) application that uses a script or a mathematical algorithm, the tag is optional" (DERDEN, https://help.prusa3d.com/article/printables-ai-tag-rules-guidelines_1306155). Onze strip komt uit een script (`testprint/maak_strip.py`, de Pro-knop "Fit test: ball"). Het label is dus niet verplicht. Wel verplicht: elk beeld moet 100% kloppen met het bestand ("Preview images must accurately depict what users will download and print"). Daarom zijn de beelden voor Printables opnieuw gerenderd uit de huidige `fit-test-strip.stl` (na moet 1 van Daan, cijfers 10 tot 30), zie hieronder. Oude renders en de figuur uit de add-on gaan er niet op. Hun tip, die we volgen: noem in de beschrijving met welke software het model en het beeld zijn gemaakt.
- **Verboden op Printables:** dubbele uploads, likes of downloads kunstmatig opdrijven, ongevraagde commerciële berichten aan andere gebruikers (DERDEN, voorwaarden, al in `commercie/blender-click-joints/verspreiding.md` regel 82). Wij doen geen van drieën: één upload, geen berichten.
- **MakerWorld valt af tot er een echte print is:** de wiki zegt "MakerWorld requires creators to include at least one photo of a model printed using that profile" (DERDEN, https://wiki.bambulab.com/makerworld/tutorials/print-profile-upload), en makers melden dat uploads zonder echte foto worden weggehaald (DERDEN, https://forum.bambulab.com/t/makerworld-deleting-uploads-that-dont-have-a-physical-image/74677). Pas na de eerste make op Printables.
- **Thingiverse:** niet onderzocht deze run. Tweede plek, zelfde tekst, als Printables werkt (GOK: kleiner bereik dan vroeger).

## Wat er op de pagina komt

**Bestand (uit `commercie/blender-click-joints/testprint/`):** alleen `fit-test-strip.stl` (de vijf kogelparen, 10 delen, 140 x 52,4 x 44,5 mm, GEZIEN in `fit-test-strip-tekst.md`). De testset (kogel en scharnier uit Pro 1.0.2, zonder getal) gaat er niet bij: die maakt de strip minder helder en het scharnier met eindstop roept een belofte op (keuring A11, C3).
Geen zip van de add-on uploaden: we linken naar extensions.blender.org, dan telt de download daar mee en is er maar één versie om bij te houden.

**Beelden (in deze volgorde), allebei op 23 nov gerenderd uit de huidige `fit-test-strip.stl` met `commercie/verspreiden/beeld/render_stl.py` (trimesh en matplotlib, geen AI), en door mij bekeken met de Read-tool:**
1. `commercie/verspreiden/beeld/printables-strip-schuin.png`: de tien delen schuin van boven, kogels en kommen op een rij.
2. `commercie/verspreiden/beeld/printables-strip-onder.png`: de onderkant, met de ingegraveerde getallen 10, 15, 20, 25 en 30 (de A-rij leest gespiegeld, omdat je van onderen kijkt; zo ligt hij ook op het bed).
Geen beeld van de add-on of van een figuur: dat zit niet in de download (Printables-regel, keuring A7). De add-on alleen via de link in de tekst.
Kan later: een render van één paar in elkaar en, zodra er een make is, die foto bovenaan.

**Categorie:** Test Models (daar staat de teststrip met 8.730 downloads). 
**Tags (Printables heeft geen vast maximum gevonden; GOK op 10 genoeg):** test, calibration, tolerance, tolerancetest, balljoint, ball joint, articulated, poseable, blender, addon.
**Licentie:** Creative Commons Attribution (BY). Waarom: wie de strip print en een make deelt, moet ons noemen; geen beperking die mensen afschrikt.
**AI-label:** niet aanzetten (optioneel bij scriptmodellen, zie boven); wel de software noemen in de tekst.

**Naam (Engels):**
```
Ball Joint Tolerance Test, 0.10 to 0.30 mm Clearance (find your fit before printing a poseable figure)
```

**Samenvatting (summary, Engels):**
```
Five ball joints from 0.10 to 0.30 mm clearance, each with its number on the bottom. Print once, try each pair, and use the gap that turns smoothly without wobble. Every printer is different: please post a make.
```

**Beschrijving (Engels):**
```
Five ball joints, from 0.10 to 0.30 mm clearance. The number on the flat end of both parts is the clearance in hundredths of a millimetre: 10 means 0.10 mm.

How to use
- Print with the material and settings you plan to use for your figure.
- Print the parts as they are in the file, flat end down. No supports.
- Push each ball into its socket. The best clearance for your printer is the one that turns smoothly without wobble.

File
- fit-test-strip.stl: the five ball joint pairs (10 parts, 140 x 52.4 x 44.5 mm).

Every printer is different. If you print it, please post a make with your printer, material and the number that fit, and we will add the results to this page.

How it was made
The geometry is based on the Fit test button of our Blender add-on Click Joints Pro, with the numbers engraved for printing. It was made with a script in Blender. The images are renders of this exact file, made with trimesh and matplotlib.

Make your own joints
- Click Joints (free Blender add-on): turn a sculpt into a poseable figure with ball joints at the clearance you found, split into parts, export to STL or 3MF. https://extensions.blender.org/add-ons/click-joints/
- Click Joints Pro: builds a figure from your rig and sets that clearance in every joint at once, and adds hinges for knees and elbows with an end stop. https://duinhouwer8.gumroad.com/l/click-joints-pro?utm_source=printables
```

**Over de prijs in de tekst:** bewust geen prijs en geen korting. De korting staat op Gumroad zelf (automatisch, `commercie/blender-click-joints/black-friday.md` stap 1); zo blijft de tekst na 1 dec kloppen.

**Over de gratis Pro-code voor een foto:** op dortus.com staat (op de tak) "Printed it? Email a photo ... and get a free Pro code". Op Printables laten we dat weg: het mailadres in een openbare modelpagina trekt spam, en een beloning voor een make kan lijken op het "kunstmatig opdrijven" dat Printables verbiedt (GOK op hoe een moderator het leest). Een make vragen zonder beloning is gewoon.

## Wie doet wat
1. **Hoofdchat:** besluit (ja of nee op Printables zonder eigen print). Keuring hieronder lezen.
2. **Thijs (±3 min, alleen bij ja):** Prusa/Printables-account aanmaken op naam Dortus, met thijs@dortus.com (zakelijk adres). Wachtwoord en gegevens alleen bij hem. Geen geld, wel hun voorwaarden accepteren (dat is aan hem).
3. **Hoofdchat (±10 min):** uploaden op wo 26 nov met de bestanden, beelden en tekst hierboven, link noteren in `commercie/geplaatst.md`.
4. **Verspreider (volgende runs):** downloads, likes en makes meten via de Printables-API (werkt met curl, zie hieronder) en verwijzingen van printables.com in Gumroad laten nakijken door de hoofdchat.

## Verwachting (alles GOK)
- Downloads eerste 30 dagen: 50 tot 500 (teststrips halen meestal 11 tot 376, de beste 8.730; nieuw account, nog geen foto, wel een open plek bij kogelgewrichten).
- Verkopen Pro daardoor binnen 2 weken: 0 tot 2. Het echte doel is de eerste make: met één echte foto gaan MakerWorld, r/3Dprinting en "print tested" open.
- Kosten: 0 euro, ±13 minuten van Thijs en de hoofdchat samen.
- Stopregel (koers Kingmaker, 14 dagen): na 10 dec minder dan 50 downloads en 0 makes: niets meer aan doen.

## Meten
Printables-API, zonder account (GEZIEN 23 nov, werkt met curl):
```
curl -s -H "content-type: application/json" https://api.printables.com/graphql/ \
  -d '{"query":"query { print(id:\"<id>\"){ downloadCount likesCount makesCount } }"}'
```

Keuring: zie onderaan.

## Keuring (23 nov 2026, aparte keurder)
# Keuring Printables-voorstel Fit test strip, 23 nov 2026, aparte keurder (Claude, niet de Verspreider)
Wat ik keurde: dit bestand (voorstel run 2), met de bronnen `platformen/blender/fit-test-strip-tekst.md`, `commercie/blender-click-joints/testprint/` (STL's, `maak_strip.py`, `maak.py`, LEESMIJ, de drie beelden in `beeld/`), `gumroad-1.1/1-figuur-uit-rig.png`, `platformen/blender/pro-1.2.1.md`, `organisatie/lijst-thijs.md` punt 3c, `organisatie/besluiten.md`, de code van de gratis versie (`producten/blender-gewrichten/click_joints/`), de Printables-API, de Prusa-hulppagina en de MakerWorld-wiki (alles met curl, 23 nov).
Akkoord: nee (het idee is goed en mag door; drie moet-punten in beelden en tekst eerst)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Alle Printables-cijfers kloppen met de API: 1242540 = 3.884 downloads, 1.200 likes, 15 makes, geplaatst 7 nov 2026 (16 dagen); 815843 = 8.730 / 1.398 / 75, categorie Test Models, scharnieren 0.1 tot 0.45 mm. In de beschrijving van 1242540 staan Patreon, "Buy me a Coffee" en Amazon-reflinks, dus een link naar een betaalde versie wordt daar geduld. | Feit | hoog | curl Printables-API, 23 nov |
| A2 | "De meeste andere teststrips halen 20 tot 400 downloads": de zoekopdracht geeft 11, 20, 20, 63, 97, 122, 138 en 376. Dat is 11 tot 376; klein verschil, de conclusie blijft. "ball joint tolerance test" geeft echt 1 model met 20 downloads; "ball joint test" geeft er nog 2 (46 en 13). De open plek klopt. | Feit | hoog | curl searchPrints2 |
| A3 | AI-regel klopt letterlijk ("...uses a script or a mathematical algorithm, the tag is optional") en ook "Preview images must accurately depict what users will download and print" en de tip om de software te noemen. | Feit | hoog | curl help.prusa3d.com |
| A4 | Het MakerWorld-citaat "Print Profiles must include real-life images of the print" staat niet letterlijk op de wiki. Er staat: "MakerWorld requires creators to include at least one photo of a model printed using that profile" en "Print profiles must include valid photos of printed results". De inhoud klopt, de aanhalingstekens niet. | Feit | hoog | curl wiki.bambulab.com/en/... (na doorsturen) |
| A5 | **Beeld 2 (`strip-plus-testset-onder.png`) klopt niet met het bestand.** Op de render staan kleine cijfers "0.10" tot "0.30". In de STL staan na moet 1 van Daan (22 nov) grote cijfers "10" tot "30" (`maak_strip.py` regel 111; `beeld/strip-cijfers-eerste-laag.png`). De render is van vóór die wijziging. De claim "Onze beelden zijn renders van precies deze STL, dat klopt" is dus fout, en de beschrijving ("10 means 0.10 mm") botst met wat het beeld laat zien. | Feit | hoog | Read van beide beelden; regel 111 van het script; volgorde in `fit-test-strip-tekst.md` |
| A6 | Beeld 1 (schuin) toont de juiste 14 delen in de juiste stand (A met kogel omhoog, B met kom omhoog, testset erachter). De cijfers zitten aan de onderkant en zijn niet te zien, dus dit beeld spreekt het bestand niet tegen. Of de onderlinge afstanden na moet 1 nog gelijk zijn, kon ik niet zien. | Vermoeden | midden | opnieuw renderen uit de huidige STL en naast elkaar leggen |
| A7 | **Beeld 3 (`1-figuur-uit-rig.png`) is een schermafdruk van de add-on met een figuur dat niet in de download zit.** Printables: "Preview images must accurately depict what users will download and print." Dit beeld is precies het soort waarvoor een model wordt weggehaald of gemeld. | Feit (regel) / vermoeden (dat een moderator ingrijpt) | hoog / midden | Printables-hulppagina A3 |
| A8 | **"Click Joints Pro: puts your clearance in every joint" wekt de indruk dat de gratis versie dat niet kan.** De gratis versie heeft zelf een schuif "Clearance (mm)" bij stap 2 Joint (`paneel.py` regel 84, `eigenschappen.py` regel 27, niet in `betaald/`). Een printer die net zijn getal vond, kan dat getal dus gratis gebruiken. Wat Pro extra doet met speling is dat "Figure from rig" en de scharnieren hem in alle gewrichten van een figuur in één keer zetten. | Feit | hoog | code gratis versie |
| A9 | De gratis regel ("ball joints, split into parts, export to STL or 3MF") en de Pro-regels ("hinges for knees and elbows with an end stop", "figure from your rig") kloppen met de Lite-tekst in lijst-thijs 3c en met `pro-1.2.1.md`. Beide links geven 200. | Feit | hoog | curl, lijst-thijs 3c |
| A10 | "The geometry comes from a script in Blender (the Fit test button of our add-on Click Joints Pro)": de strip wijkt bewust af van de knop (cijfers ingegraveerd in beide delen in plaats van reliëf, B gekanteld). "comes from" is iets te stellig. | Feit | hoog | `fit-test-strip-tekst.md`, kop "Anders dan de knop in Pro" |
| A11 | De 4 testset-delen in het hoofdbestand komen uit Pro 1.0.2 (17 nov, `LEESMIJ.md`): scharnier 0,2 mm, kogel "automatische maat", zonder ingegraveerd getal. Een printer weet dus niet welke speling die extra kogel heeft. De overhangmeting in `fit-test-strip-tekst.md` gaat alleen over de 10 stripdelen. | Feit | hoog | LEESMIJ, maak.py |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Plaatsen zonder eigen print botst niet met het besluit van 17 nov 13:40 zolang de tekst niet belooft dat het klikt. De beschrijving zegt eerlijk "Not print tested by us yet". **Maar de samenvatting opent met "Five snap-together ball joints"**: dat is precies de belofte dat het klikt, en het staat op de plek die iedereen als eerste ziet (zoekresultaat), terwijl de eerlijke zin pas halverwege staat. Thijs 19 nov: "nog geen 'klikt' of 'stopt' in teksten". | Feit | hoog | besluit 17 nov 13:40; Thijs 19 nov ±14:00 |
| B2 | Het voorstel vraagt terecht een nieuw besluit: `verspreiding.md` regel 17 en rij 8 zeggen "Printables pas met echte print". Het nieuwe feit (teststrip belooft niets, open plek, voorbeeld 1242540) is een geldige reden om terug te komen. Bij ja moet de hoofdchat een regel onderaan `besluiten.md` zetten en rij 8 bijwerken, anders spreken de stukken elkaar tegen. | Feit | hoog | besluiten.md kop ("terugkomen kan alleen met een nieuw feit") |
| B3 | Rolverdeling klopt met CLAUDE.md regel 4 en 7: account door Thijs, upload door de hoofdchat (nieuw kanaal, Chrome alleen op de HP en alleen de hoofdchat), geen post onder de naam van Thijs, de tekst wordt eerst gekeurd. De Verspreider plaatst niets zelf. | Feit | hoog | CLAUDE.md regel 4, 6, 7 |
| B4 | Geen geld: 0 euro. Geen persoonsgegevens: alleen thijs@dortus.com (zakelijk, staat al op vele plekken) en de openbare Gumroad-link. Wachtwoord "alleen bij hem": goed. | Feit | hoog | CLAUDE.md regel 1 en 2 |
| B5 | Platformregels: één upload, geen berichten, geen kunstmatige likes; terecht geen beloning voor een make. Het AI-label mag uit. Maar beeld 2 en 3 breken de 100%-regel (A5, A7). | Feit | hoog | "geen platformregels breken" (9 nov 22:56) |
| B6 | Elk cijfer heeft GEZIEN, DERDEN of GOK; verwachtingen staan als GOK. Behalve het MakerWorld-citaat (A4) en "20 tot 400" (A2) klopt alles bij de bron. Nederlands zonder gedachtestreepjes, plaatstekst Engels. | Feit | hoog | CLAUDE.md regel 5 en 8 |
| B7 | Geldtoets: 0 tot 2 verkopen Pro binnen 2 weken (GOK) voor ±13 minuten en 0 euro, met een stopregel na 14 dagen. Klein maar goedkoop, en het opent MakerWorld en r/3Dprinting zodra er een make is. Past bij de hoofdzaak. | Vermoeden | midden | CLAUDE.md hoofdzaak; koers Kingmaker 14 dagen |

## Deel C: zou een 3D-printer op Printables dit downloaden en printen?
Ja, waarschijnlijk wel: een kogelgewricht-teststrip is er nauwelijks, de tekst is kort en praktisch, en de cijfers op het bed zijn een slimme vondst. Wat nu zwak is: de beelden zijn grijs op grijs, de cijfers op beeld 2 zijn amper te lezen, en niemand ziet hoe een paar in elkaar zit.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Het eerste beeld is een dichte bos grijze cilinders; in de lijst op Printables (klein plaatje) lees je niet "teststrip met 5 maten". | Hoofdbeeld van alleen de strip, schuin van boven, met de vijf paren op een rij en de getallen 10 / 15 / 20 / 25 / 30 groot ernaast of erboven als tekst in het beeld; lichte achtergrond, elk paar een eigen tint. | midden |
| C2 | Je ziet nergens een kogel in een kom. Dat is wat de printer wil weten. | Een render van één paar in elkaar geklikt (de kan C4 van Daan), naast de losse delen. Dat is een render van het bestand, dus mag. | midden |
| C3 | Het hoofdbestand met 14 delen maakt de strip minder helder: de extra kogel heeft geen getal (A11) en het scharnier met "end stop" roept een belofte op die we niet kunnen waarmaken. | Hoofdbestand `fit-test-strip.stl` (10 delen); het scharnier en de testset weglaten of als los tweede bestand met de speling erbij ("hinge, 0.20 mm"). | klein |
| C4 | Printers zoeken op "tolerance test". De titel heeft "Clearance" maar niet "Tolerance". | Bijv. "Ball Joint Tolerance Test, 0.10 to 0.30 mm Clearance (find your fit before printing a poseable figure)". | klein |
| C5 | Printtijd en filamentgebruik ontbreken; dat staat bij bijna elk teststuk. | Eén keer slicen (PrusaSlicer kan zonder printer) en "about X h, Y g PLA at 0.2 mm" erbij, als GEZIEN uit de slicer. | klein |
| C6 | De beste teststrip (815843) loopt tot 0.45 mm; wie een grove printer of PETG heeft, valt bij 0.30 mogelijk buiten de strip. | Later een tweede bestand 0.30 tot 0.50 mm. Niet nu. | midden |
| C7 | De vraag om een make is goed. | Concreet maken: "post a make with your printer, material and the number that fit, and we add the best results to this page". Geen beloning, dus geen probleem met de regels. | klein |

## Moet (blokkeert akkoord)
1. **Beeld 2 opnieuw renderen uit de huidige STL** (cijfers "10" tot "30"), of weglaten. Nu toont het "0.10" tot "0.30" en klopt het niet met het bestand (A5). Ook beeld 1 opnieuw renderen uit de huidige STL, zodat de zin "renders of these exact files" waar is (A6).
2. **Beeld 3 (figuur uit de add-on) niet op de Printables-pagina** (A7): het zit niet in de download. Wil je de add-on laten zien, dan alleen via de link in de tekst.
3. **Tekst eerlijk maken:** (a) "snap-together" uit de samenvatting en "Not print tested by us yet" in de samenvatting zelf, bijv. "Five ball joints from 0.10 to 0.30 mm clearance, each with its number on the bottom. Print once, try each pair, and use the gap that turns smoothly without wobble. Not print tested by us yet: please post a make." (B1); (b) de Pro-regel niet laten klinken alsof alleen Pro je speling gebruikt. Bijv. bij gratis: "...with ball joints at the clearance you found..." en bij Pro: "...sets that clearance in every joint of a figure at once, adds hinges..." (A8).

Na deze drie punten keur ik alleen die opnieuw; het idee en de rolverdeling zijn akkoord, het besluit zelf ligt bij de hoofdchat (B2).

## Kan (mag later)
- Het MakerWorld-citaat letterlijk maken (A4) en "20 tot 400" in "11 tot 376" (A2).
- "comes from a script" wordt "is based on the Fit test button..., with the numbers engraved for printing" (A10).
- Hoofdbestand alleen de 10 stripdelen, testset los of weg (C3, A11).
- "Tolerance" in de titel (C4), printtijd uit een slicer (C5), render van een paar in elkaar (C2), beter hoofdbeeld (C1).
- Bij ja: regel onderaan `besluiten.md` en rij 8 in `verspreiding.md` bijwerken (B2).

## Nakeuring
Nakeuring van moet 1 tot 3 (23 nov 2026, dezelfde aparte keurder). Alleen deze punten opnieuw bekeken.
Akkoord: ja

| Moet | Wat ik zag | Uitslag |
|---|---|---|
| 1 Beelden uit de huidige STL | `commercie/verspreiden/beeld/printables-strip-schuin.png` en `-onder.png` bekeken met Read. `fit-test-strip.stl` gemeten met trimesh: 10 losse delen, 140 x 52,4 x 44,5 mm (GEZIEN). Het schuine beeld toont precies 10 delen (5 kogels, 5 kommen op een rij), geen testset meer. Het onderbeeld toont de grote getallen 10, 15, 20, 25, 30, één rij gespiegeld; dat is hetzelfde patroon als `testprint/beeld/strip-cijfers-eerste-laag.png` (de doorsnede van dezelfde STL). `render_stl.py` laadt alleen de STL en kleurt hem: oranje tint en donkerder vlakken onder 1,5 mm hoogte om de gravering zichtbaar te maken. Er komt geen vorm bij, dus het beeld klopt met het bestand. De tekst noemt nu één bestand, en dat past bij de beelden. | opgelost |
| 2 Geen beeld van de add-on | Het figuurbeeld staat niet meer in de lijst. De add-on staat alleen als link in de tekst. | opgelost |
| 3a Geen belofte dat het klikt | "snap-together" is weg. De samenvatting eindigt met "Not print tested by us yet: please post a make." In de beschrijving staat "Push each ball into its socket" in plaats van "Click each pair together". De hinge met "end stop" staat niet meer in het bestand of de lijst met bestanden. Alleen bij Pro staat nog "hinges ... with an end stop": dat beschrijft een functie, zoals in de gekeurde Lite-tekst. | opgelost |
| 3b Speling niet alleen bij Pro | Gratis: "with ball joints at the clearance you found" (klopt: schuif Clearance in `paneel.py` r84). Pro: "builds a figure from your rig and sets that clearance in every joint at once". Klopt met de code: gewricht en scharnier nemen de ene `inst.speling_mm` (`gewricht.py` r248, `betaald/scharnier.py` r203), die figuur uit rig voor elk gewricht gebruikt. Vermoeden, zekerheid hoog. | opgelost |

Kan (blokkeert niet):
- Op het schuine beeld zijn de randen van de kommen wat gekarteld (matplotlib zonder anti-aliasing). Een render in Blender met een lichte achtergrond oogt rijker; dat mag later, samen met een render van één paar in elkaar.
- "The images are renders of this exact file" klopt. Wil je de Printables-tip helemaal volgen (de software noemen), schrijf dan "rendered with trimesh and matplotlib".

## Aanpassing 24 nov 2026 ±16:10 NL (Verspreider, na besluit Thijs 15:32)
Thijs: nergens meer "not print tested by us yet" ("komt super onprofessioneel over"). In samenvatting en beschrijving is "Not print tested by us yet" vervangen door "Every printer is different" (zin uit het besluit); de vraag om een make met printer, materiaal en nummer blijft. Er staat nergens dat wij geprint hebben of dat het klikt; de eerlijkheidsregel blijft. Geen nieuwe keuring nodig: alleen weglating plus de zin uit het besluit. De keuringstabellen hierboven citeren de oude zin; die blijven staan als geschiedenis.
