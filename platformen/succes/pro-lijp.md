# Wat maakt Click Joints Pro "lijp"? (Lars, 16 nov 2026 ±16:20 UTC)

Opdracht hoofdchat 16 nov 16:10 (SPOED, vóór wo 18 nov 09:00): (1) de 10 grootste ergernissen van makers van poseerbare en flexi-printfiguren, met bron en hoe vaak; (2) welke daarvan Pro 1.1 "Rig to Figure" kan oplossen en hoe; (3) de 3 dingen die in reviews van top-add-ons het vaakst "worth every penny" opleveren. Top 3 staat ook in `berichten/ruben.md`.

## Kort
- **De grootste wens is precies Rig to Figure.** Mensen met een eigen figuur vragen steeds opnieuw om "een sjabloon met gewrichten dat ik met mijn model samenvoeg" en weten niet hoe ze gewrichten moeten ontwerpen. Eén draadje op BlenderArtists met die vraag heeft 20.292 weergaven.
- **De grootste ergernis daarna is speling:** welke spleet klikt op míjn printer, en waarom smelt het gewricht vast. Pro heeft het testkaartje al; in 1.1 moet dat voor alle gewrichten tegelijk gelden en vóóraan staan.
- **In reviews van de beste add-ons komt "het waard" vooral terug bij:** (1) makkelijk, ook zonder voorkennis binnen minuten resultaat, (2) goede uitleg en video, (3) een maker die snel antwoordt en blijft bijwerken.

## Bronnen en hoe geteld (alles met curl, GEZIEN 16 nov 2026 15:55 tot 16:15 UTC)
- **Reddit** via het archief Arctic Shift (`https://arctic-shift.photon-reddit.com/api/posts/search` en `/api/comments/search`), want reddit.com zelf geeft 403 op curl. Berichten sinds 1 jan 2024 met in de kop "articulated", "print in place", "posable", "poseable", "action figure", "flexi" of "ball joint" in r/3Dprinting, r/blender, r/PrintedMinis, r/3dprintingdesign, r/BambuLab, r/functionalprint: **573 berichten** (tabel zonder namen: `platformen/succes/data/reddit-figuren-berichten-2026-11-16.csv`). Plus **561 reacties**: alle reacties onder 15 draadjes over figuren en gewrichten, en 212 reacties sinds 1 nov 2025 met "print in place" of "3d print" in de tekst. Een deel van de zoekopdrachten gaf "Timeout" (onder meer "flexi" en "ball joint" in r/3Dprinting); die ontbreken dus.
- **BlenderArtists** (openbare zoek-API `https://blenderartists.org/search.json` en `/t/<id>.json`): 7 zoektermen, 8 draadjes volledig gelezen (46 berichten).
- **Niet gelukt deze run:** Printables-reacties (alleen via hun GraphQL, niet geprobeerd uit tijd) en YouTube-reacties. Dat is een gat: daar zitten de makers van flexi-printjes zelf. Ik vul het aan in een volgende run vóór woensdag.
- **Superhive-reviews van top-add-ons:** alle reviewpagina's (`https://superhivemarket.com/products/<naam>/ratings?page=N`) van 14 bekende goedverkopers (Auto-Rig Pro, Scatter, Botaniq, Physical Starlight and Atmosphere, MACHIN3tools, Fluent, MESHmachine, DECALmachine, Faceit, Voxel Heat Diffuse Skinning, RetopoFlow, Random Flow, BoxCutter, True Terrain) plus CatPin en Cleave: **1.513 reviews** (1.322 keer 5 sterren). Tabel zonder namen: `platformen/succes/data/superhive-reviews-toppers-2026-11-16.tsv`. Auto-Rig Pro heb ik afgekapt op 200 (20 van 45 pagina's).
- **Hoe vaak:** ik telde met zoekwoorden in alle 1.180 teksten (berichten, reacties, BlenderArtists) en keek per ergernis een steekproef met de hand na. Zo'n tel **overtelt** (een "loose" gaat soms over een printerkop) en mist wat anders verwoord is. Zie het als volgorde, niet als precieze maat.

## (1) De 10 grootste ergernissen

| # | Ergernis | Ruwe tel (van 1.180) | Wat mensen zeggen (bron) |
|---|---|---|---|
| 1 | **Ik weet niet hoe ik gewrichten in mijn eigen figuur krijg; ik wil een kant-en-klaar sjabloon** | 58 met "STL / template / ready-made joint" (meeste zijn "mag ik het bestand?"), plus 5 hoe-vragen | r/3Dprinting 1pp1xif: "an action figure articulation template that can be merged with your model ... If it doesn't yet exist, would that be useful to anyone?" · 1sgcol1: "are there any ready-made joint models that I could just copy and paste into my project?" · BlenderArtists 1452894 "Can Blender be used for action figure modeling?" (20.292 weergaven) · 1491951 "How to Model a poseable figurine?" (2.164 weergaven) · 1656400 (okt 2026): "articulation and joints first or body first?" |
| 2 | **Speling raden: welke spleet klikt op mijn printer** | 33 | 1xrez92: "The clearance you set in CAD rarely match what actually comes off the printer plate (Speaking from painful experience)" · 1usw6ke: testkaart "0.15 mm = fused, 0.20 = breaks free but is tight, 0.25 = moves freely" · een poppenmaker: "I'm confused about tolerances on for joints" |
| 3 | **Gewricht smelt vast (fused)** | 11 | 1usw6ke: "every time the hinge fuses together. When I try to free it, the arm breaks" · 1vtkdw0: "PETG welds like it's got something to prove" |
| 4 | **Te los: figuur houdt zijn pose niet, ledematen zakken** | 20 | 1kmqm06: "inner frames were meant to be printed in PETG ... because PLA would sag pronto" · 1xb826a: koper kocht los een "joint-fixer" om kogels stroever te maken · een flexi-draak: "some joints will become loose, making glue pretty much essential" (200%) |
| 5 | **Welk materiaal voor de gewrichten (PLA, PETG, hars)** | 29 | 1xb826a: "I designed the joints separated so you can print with PETG to handle better friction" · 1sgcol1: "Does resin work well for articulated joints that will stay in place?" · 1rmrha7: "Resin is probably the best way to go" |
| 6 | **Zelf snijden in Blender geeft boolean-rommel en niet-waterdichte delen** | 21 | BlenderArtists 1112971 (1.955 weergaven): "I keep getting nasty edges" bij het uitsnijden van een kogelkom · r/blender: "boolean can be chaotic, but its so invaluable" |
| 7 | **Kogel breekt of klikt niet bij het in elkaar drukken** | 5 | 1xb826a: "Inserting the balljoints into the sockets consistently breaks them" · 1rmrha7: "the head and the hands not snapping in" |
| 8 | **Steunmateriaal in en rond gewrichten, kleine delen mislukken** | 9 | 1sbqun2 (Mario-figuur, 379 upvotes): "head attempted 2 times and failed ... Supports keep messing up" · 1xkv5jt: "0.14mm Top Z-distance, 4 interface layers, tuned tree supports" · 1vldk8y: "Took a while to get the joint mechanism working without supports" |
| 9 | **Bereik: het lid botst tegen het lijf of een pantserstuk en je ziet het pas na het printen** | 4 | BlenderArtists 1444337 (784 weergaven): "make it stop when it hits something else ... to check how far it can rotate" · 1xkv5jt: grote schouderstukken "prevent the joints" |
| 10 | **Lelijke naden en printlijnen op het figuur** | 12 | 1odgx9u: "you'll still be able to see lines" bij 0.4 mm · 1xkv5jt: matte PLA "hide the layer lines" |

Opvallend: de mooiste figuren op Reddit (KIDDO 888 upvotes, Mario 379, Batman 89) zijn in CAD of met de hand gedaan ("That's a lot of parts! ... I lost a couple of them", maker KIDDO), en de reacties gaan vooral over het bestand (onder Batman 20 van de 54 reacties, vragen plus antwoorden van de maker). Er is veel vraag naar poseerbare figuren en weinig mensen kunnen ze maken. Dat is de kans voor Rig to Figure.

## (2) Wat Pro 1.1 kan oplossen, en hoe

| # | Ergernis | Lost 1.1 het op? | Hoe (voorstel voor Ruben, zijn oordeel gaat voor) |
|---|---|---|---|
| 1 | Sjabloon voor eigen figuur | **Ja, dit is 1.1** | Eén knop op een gerigde figuur, plus de zes presets voor wie geen rig heeft. Zeg het in de woorden van de vraag: "merge your own model with articulation in one click". |
| 2 | Speling raden | **Ja, als het vooraan staat** | Het testkaartje (vijf spelingen) bestaat al in Pro. In 1.1: de gekozen printer geldt meteen voor alle acht gewrichten, en in het paneel staat "Fit: 0.25 mm (your printer)". Een nieuwe koper print eerst het kaartje; zet die stap als stap 0 in het paneel. |
| 3 | Vastgesmolten | **Deels** | Waarschuwing (oranje) als de speling onder 0,2 mm staat bij FDM, met de zin "may fuse on FDM". GOK dat 0,2 mm de goede grens is; de Reddit-testkaarten noemen 0,15 vast en 0,25 vrij. |
| 4 | Te los, houdt pose niet | **Ja, klein werk** | Pro heeft al wrijvingsribbels. In 1.1 één schakelaar "Holds pose (friction ribs)" voor de hele figuur, standaard aan. Dit is de klacht die het vaakst terugkomt na het printen. |
| 5 | Materiaal | **Ja, klein** | Bij export een korte regel: "Print joint parts in PETG for friction; PLA may sag." Kost niets, scheelt een mislukte print. |
| 6 | Boolean-rommel | **Al opgelost** | Click Joints maakt gesloten, waterdichte delen. Zet het op de winkelpagina: "watertight parts, no boolean cleanup". |
| 7 | Kogel breekt bij inklikken | **Misschien** | De wanddikte in mm staat al in de passingkleur. Een sleufje in de kom (zodat hij veert) is een GOK; alleen doen als het in 1.1 past, anders 1.2. |
| 8 | Steunmateriaal | **Nee, niet in 1.1** | Buiten bereik. Hooguit later: per deel de platte kant naar beneden. |
| 9 | Bereik pas na printen zien | **Ja, dit is ons beeld** | Bereik uit de rig en de bogen met graden per gewricht. Waar een pantserstuk het bereik inperkt, eerlijk `blocked` tonen (doet 1.1 al bij de heup). Dit is het schermafbeeldingsmoment. |
| 10 | Naden en lijnen | **Nee** | Printerwerk, niet ons terrein. |

Samengevat: 1.1 raakt 1, 2, 6 en 9 al, en met drie kleine dingen (4 ribbels aan voor de hele figuur, 3 waarschuwing onder 0,2 mm, 5 materiaalregel) ook de klachten na het printen. Dat maakt het verschil tussen "mooie knop" en "mijn figuur werkt echt".

## (3) Wat in reviews van top-add-ons "het waard" maakt

1.322 vijfsterrenreviews op Superhive (14 goedverkopers), geteld met zoekwoorden (GEZIEN, een review kan in meer groepen vallen):

| Groep | Aantal 5-sterrenreviews | Aandeel |
|---|---|---|
| Makkelijk, intuïtief, één klik | 242 | 18% |
| Onmisbaar, elke dag in mijn werk | 230 | 17% |
| Maker antwoordt snel, helpt, lost op | 196 | 15% |
| Kwaliteit van het resultaat | 152 | 11% |
| Uitleg: video, documentatie | 144 | 11% |
| Bespaart uren | 123 | 9% |
| Updates | 118 | 9% |
| Uitdrukkelijk "worth every penny / worth it" | 86 | 7% |

In de 78 reviews die letterlijk "worth it / worth every penny / worth the money" zeggen, staat daarnaast het vaakst: uitleg en video (17), makkelijk (15), onmisbaar (15), snelle hulp van de maker (13), kwaliteit (13), updates (12), tijd (11).

**De drie dingen:**
1. **Ook zonder voorkennis binnen minuten resultaat.** Auto-Rig Pro: "I've zero experience with rigging. This gave me exactly what I needed after 10 minutes ... well worth the money." Voor ons: een maker zonder rigkennis moet met een preset of een Mixamo-figuur in vijf minuten een printbare figuur hebben.
2. **Goede uitleg en een video.** "read the documentation, it's a good amount to process" en tutorials komen het vaakst mee in "het waard"-reviews. Voor ons: een filmpje van 60 seconden (figuur in, één knop, bogen in beeld, delen eruit) en een korte pagina "first figure in 5 minutes" met het speling-kaartje.
3. **Een maker die snel helpt en blijft bijwerken.** "contacted the developer with a test file. He responded professionally ... released a fix right away"; "the developer fixed it within a few hours. Definitely worth the money." Voor ons: elke vraag of review binnen een dag beantwoorden, en de belofte "12 maanden updates" zichtbaar waarmaken met een changelog.

## Voorstel voor deze week
**Ruben zet in 1.1 de schakelaar "Holds pose" (wrijvingsribbels voor de hele figuur, standaard aan) en de oranje waarschuwing onder 0,2 mm erbij, en maakt het testkaartje stap 0 in het paneel.** Waarom: "te los" en "speling raden" zijn de klachten na het printen; zonder die twee werkt een mooi gerigde figuur in het echt niet, en dan komt de eerste review daarover. Kost GOK één tot twee runs. Daarnaast (Chris, na 1.1): het filmpje van 60 seconden en de "first figure in 5 minutes"-pagina, want dat is wat in "het waard"-reviews het vaakst meekomt.

## Open, volgt vóór wo 18 nov 09:00
- Printables-reacties onder de populairste flexi- en actiefiguren (wat mislukt bij printers?) en YouTube-reacties onder 2 of 3 "how to make articulated figure in Blender"-filmpjes.
- Negatieve reviews (76 met 1 of 2 sterren) van de toppers: wat kost sterren.
