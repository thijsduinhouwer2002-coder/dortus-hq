# Figure from rig betrouwbaar: oorzaak, nulmeting en eindmeting (Betrouwbaarheid, 23 nov 2026)

Opdracht hoofdchat 23 nov ±20:50 NL: op een vaste testset van figuren elk gewricht, in Blender 4.2, 5.2 en 5.3.
Tak `claude/betrouwbaar-rig`. Alle cijfers hieronder zijn GEZIEN in de JSON-uitslagen op de tak `betrouwbaar-uitslag`
(map `<run>/<versie>/<figuur>.json`, tabel met `python3 producten/blender-gewrichten/e2e/meet_tabel.py <map>`).

## Testset (`e2e/meet_rig.py`, workflow `betrouwbaar-rig.yml`)
Zeven figuren, alle eigen werk of vrije licentie, niets gedownload: de robot van de studio (eigen werk) in beide
kleurstellingen en met voxel 0,35 mm, het aangeklede MakeHuman-figuur van studio-1 (CC0 1.0, `makehuman-base-LICENTIE.md`),
de kale MakeHuman-mens van `toetsen_mens.py`, de Rigify-metarig van Blender met buizen, de buizenfiguur met armen.
Haalbaar per figuur: robot en mensen 9, Rigify 7 (schouders: "no room on this 29 mm bone for a ball joint next to the
elbow", in elke versie en voor en na, de bovenarm is te kort), buizenfiguur 8 (de rig heeft geen nek). Samen 60 per
versie.

## Nulmeting en eindmeting
Cel: gewrichten / slechte sneden onderweg (open, leeg of overlappend, ook als een latere plek het redde) / tijd van de knop.

Nulmeting, main zoals uitgebracht als Pro 1.2.2 (run 45253697551):

| Figuur | 4.2.23 | 5.2.3 | 5.3.0 |
|---|---|---|---|
| robot-a | 5 / 5 / 156 s | 9 / 1 / 139 s | 9 / 1 / 138 s |
| robot-b | 5 / 5 / 171 s | 9 / 1 / 139 s | 9 / 1 / 95 s |
| robot-fijn | 5 / 8 / 315 s | 9 / 0 / 140 s | 9 / 0 / 112 s |
| kleding | 6 / 30 / 1813 s | 8 / 14 / 611 s | 8 / 14 / 469 s |
| mens | 3 / 36 / 340 s | 9 / 0 / 14 s | 9 / 0 / 17 s |
| rigify | 5 / 15 / 164 s | 7 / 0 / 16 s | 7 / 0 / 28 s |
| armen | 6 / 7 / 40 s | 8 / 0 / 12 s | 8 / 0 / 13 s |
| **samen** | **35 van 60** | **59 van 60** | **59 van 60** |

Eindmeting, eindstand van de add-on op de tak (commit 6dc00b2). 5.2.3 en 5.3.0 uit run 45267268513. Kolom 4.2.23 uit run
45264302449 (commit 7ea796e): de 4.2-jobs voor robot en rigify van 45267268513 werden door GitHub afgebroken (exit 143,
SIGTERM van de runner), en de weg in 4.2 (Exact) is in beide commits dezelfde; kleding, mens en armen gaven in 45267268513
hetzelfde aantal (8, 9, 8).

| Figuur | 4.2.23 | 5.2.3 | 5.3.0 |
|---|---|---|---|
| robot-a | 7 / 1 / 136 s | 9 / 0 / 66 s | 9 / 0 / 75 s |
| robot-b | 7 / 1 / 171 s | 9 / 0 / 93 s | 9 / 0 / 95 s |
| robot-fijn | 9 / 4 / 239 s | 9 / 0 / 244 s | 9 / 0 / 202 s |
| kleding | 8 / 6 / 205 s | 9 / 0 / 69 s | 9 / 0 / 59 s |
| mens | 9 / 0 / 153 s | 9 / 0 / 19 s | 9 / 0 / 20 s |
| rigify | 7 / 4 / 291 s | 7 / 0 / 30 s | 7 / 0 / 21 s |
| armen | 8 / 0 / 43 s | 8 / 0 / 24 s | 8 / 0 / 24 s |
| **samen** | **55 van 60** | **60 van 60** | **60 van 60** |

In 5.2 en 5.3 nu elk haalbaar gewricht en geen enkele slechte snede meer onderweg (was 16 per versie). Het aangeklede
figuur (de filmpjes) ging van 8 naar 9 en van ±8 naar ±1 minuut. In 5.x komt de voxelvorm alleen nog waar de oude vereniging mislukte (19 keer in run 45267268513), dus lichte figuren zijn even snel als eerst (kale mens 19 s).

## Herhaald: 5 keer per figuur per versie, en waarom dezelfde mesh wisselend uitkwam (run 45273407326)
Opdracht hoofdchat 23 nov ±23:00 (robot van studio-3: in 6 CI-jobs 5 keer 9 en 1 keer 8). Elke figuur 5 keer per versie
in een eigen Blender, voor de nulstand (Pro 1.2.2, `NUL_COMMIT` e8769d2, zelfde figuren) en voor deze tak (commit 0eb3510).
Let op: vanaf hier is de robot die van studio-3 (dikker, vuisten met vingers); de tabellen hierboven hadden die van studio-2.
Cel: gewrichten per herhaling / slechte sneden opgeteld / mediane tijd / aantal verschillende uitkomsten (vingerafdruk:
regels met bereik plus punten per deel).

Nulstand (Pro 1.2.2):

| Figuur | 4.2.23 | 5.2.3 | 5.3.0 |
|---|---|---|---|
| robot-a | 4,4,4,4,4 | **9,8,8,9,9** | **8,9,9,8,9** |
| robot-b | 4,4,4,4,4 | **9,9,8,9,8** | **8,9,9,9,9** |
| robot-fijn | (afgebroken) | 5,5,5,5,5 | 5,5,5,5,5 |
| kleding | 6,6,6,6,6 | 8,8,8,8,8 | 8,8,8,8,8 |
| mens | 3,3,3,3,3 | 9,9,9,9,9 | 9,9,9,9,9 |
| rigify | 5,5,5,5,5 | 7,7,7,7,7 | 7,7,7,7,7 |
| armen | 6,6,6,6,6 | 8,8,8,8,8 | 8,8,8,8,8 |

Deze tak. 5.2.3 en 5.3.0 uit run 45273407326 (commit 0eb3510); 4.2.23 uit run 45275271607 (commit 183fae2, met
`herstel.opschonen`; zonder die stap gaf de robot van studio-3 in 4.2 maar 2,2,2,2,2):

| Figuur | 4.2.23 | 5.2.3 | 5.3.0 |
|---|---|---|---|
| robot-a | 6,6,6,6,6 | 9,9,9,9,9 | 9,9,9,9,9 |
| robot-b | 6,6,6,6,6 | 9,9,9,9,9 | 9,9,9,9,9 |
| robot-fijn | 7,7,7,7,7 | 9,9,9,9,9 | 9,9,9,9,9 |
| kleding | 8,8,8,8,8 | 9,9,9,9,9 | 9,9,9,9,9 |
| mens | 9,9,9,9,9 | 9,9,9,9,9 | 9,9,9,9,9 |
| rigify | 7,7,7,7 | 7,7,7,7,7 | 7,7,7,7,7 |
| armen | 8,8,8,8,8 | 8,8,8,8,8 | 8,8,8,8,8 |
| **samen (elke herhaling)** | **51 van 60** | **60 van 60** | **60 van 60** |

Nulstand samen: 4.2.23 28 van 51 (zonder robot-fijn, die jobs werden afgebroken), 5.2.3 en 5.3.0 53 tot 55 van 60, wisselend per run.
**Eerlijke vergelijking 4.2 (keuring A, M2):** op dezelfde zes figuren (zonder robot-fijn) gaat 4.2 van **28 naar 44 van 51**; de 51 van 60 in de tabel is met robot-fijn erbij, die in de nulstand niet afliep.

Op deze tak zijn de gewrichten en hun bereik in elke herhaling precies gelijk, op elke figuur en in elke versie (21 van 21
groepen één set regels, GEZIEN). Alleen het aantal punten van een paar delen verschilt (enkele tientallen tot ±180).

**Bron van het wisselen (GEZIEN):** in de nulstand gaven 194 van de 567 kogelsneden in 5.x een H "los" (alle 5 herhalingen geteld, telling keurder A), en precies die 194
waren slecht (open of overlappend); geen enkele andere snede was slecht. Op dezelfde mesh en dezelfde plek gaf de
Exact-vereniging van omhulsel en lid (`een_lid._samen`) de ene keer "samen" en de andere keer "los" (robot-a, rechterschouder:
herhaling 1, 4, 5 "samen" en ±30°, herhaling 3 "los", 9181 paren overlap, "blocked"). Ook op hetzelfde processortype (AMD
EPYC 7763) verschilde het, dus het is niet alleen de processor: de vereniging werkt op een vorm die zichzelf snijdt, en de
uitkomst daarvan hangt af van de volgorde waarin het parallelle rekenwerk klaar is (GOK voor dat laatste stapje; dat het
precies de "los"-sneden zijn is GEZIEN). In 4.2 waren de gewrichten in de nulstand en op de tak in elke herhaling gelijk; op snede-niveau niet altijd (run 45279729768: mens-3 had één slechte linkerschoudersnede die de andere herhalingen niet hadden, de volgende plek redde het; robot-fijn had twee vingerafdrukken). De Meshy knight wisselt in 4.2 ook (1 of 2 gewrichten), al op main.
Op deze tak: 0 van 440 kogelsneden "los" (93 keer werd een mislukte vereniging een voxelvorm), 0 slechte sneden. Bij scharnieren gaf een "los"-H in de nulstand 20 keer wel een goede snede; het verband geldt voor kogels. Het kleine
verschil in punten komt doordat de keuze "samen" of "voxel" per run nog kan wisselen; de gewrichten en het bereik niet.

## Verlies bij kogelsneden (keuring A, moet 1; run 45282711505, commit 1945f46)
Het vangnet "the cut lost part of the model" (`rig.verloren_stuk`, grens 6%) gold alleen voor scharnieren, terwijl de
voxelvorm juist bij kogelsneden zit. Nu:
- **In de add-on:** `rig.py` past het vangnet ook toe op elke kogelsnede (`VERLOREN_MAX` 0,06): meer verlies, dan
  terugdraaien en de volgende plek. Toets in de e2e: `CJ_HERKANS=3` in `e2e/toetsen_mens.py` (eerste
  linkerschoudersnede verliest zogenaamd 50%; de knop moet een volgende plek nemen en de schouder toch plaatsen). Groen in
  de rig-toetsen van run 45282711505 voor 5.2.3 en 5.3.0 (GEZIEN: "na een kogelsnede die te veel verliest neemt de knop
  een volgende plek"), en in de gewone e2e (run 45282711688, stap Figuurpresets met `CJ_HERKANS=3`) groen in 4.2.23, 5.2.3 en 5.3.0.
- **Gemeten:** bij elke geslaagde kogelsnede hetzelfde `verloren_stuk` (bol van 15 mm rond de cursor overgeslagen), in
  nulstand (2 herhalingen) en tak (5 herhalingen), drie versies. Cel: grootste verlies / kogelsneden boven 6%.

| Figuur | 4.2.23 nul | 4.2.23 tak | 5.2.3 nul | 5.2.3 tak | 5.3.0 nul | 5.3.0 tak |
|---|---|---|---|---|---|---|
| robot-a | 5,0% / 0 | 0,0% / 0 | 0,3% / 0 | 0,0% / 0 | 0,0% / 0 | 0,3% / 0 |
| robot-b | 5,0% / 0 | 0,0% / 0 | 0,0% / 0 | 0,3% / 0 | 0,0% / 0 | 0,3% / 0 |
| robot-fijn | afgebroken | 0,0% / 0 | 0,0% / 0 | 0,0% / 0 | 0,0% / 0 | 0,0% / 0 |
| kleding | 0,0% / 0 | 0,0% / 0 | 0,5% / 0 | 0,0% / 0 | 0,5% / 0 | 0,0% / 0 |
| mens | 0,0% / 0 | 0,0% / 0 | 0,0% / 0 | 0,0% / 0 | 0,0% / 0 | 0,0% / 0 |
| rigify | 0,2% / 0 | 0,2% / 0 | 0,2% / 0 | 0,2% / 0 | 0,2% / 0 | 0,2% / 0 |
| armen | 0,0% / 0 | 0,0% / 0 | 0,9% / 0 | 0,9% / 0 | 0,9% / 0 | 0,9% / 0 |

  Nergens boven 6%, nergens slechter dan de nulstand (grootste verlies tak 0,9%, nul 5,0%). De kogelsneden met voxelvorm
  (125 in 4.2, 37 en 35 in 5.2.3 en 5.3.0) verloren elk 0,0%. Het vangnet heeft op de testset dus niets geweigerd; het
  aantal gewrichten is gelijk aan run 45273407326 en 45275271607, en per figuur in elke herhaling dezelfde gewrichten met
  hetzelfde bereik (21 van 21 groepen). De 7 tot 11% van de knight in 4.2 was een scharniersnede (rechterknie), waar het
  vangnet al gold en doorschoof.
- Afgebroken door GitHub (exit 143, SIGTERM van de runner): 4.2 robot-fijn nulstand (beide) en 4.2 rigify tak (2 van 5).

## Oorzaak (met bewijs)
Figure from rig snijdt een lid los met een omhulsel H (`een_lid`): een convex omhulsel rond het snijvlak plus het lid
zelf, elk punt `m` (0,2 tot 0,6 mm) langs zijn normaal naar buiten, samengevoegd met een Exact-vereniging.
1. **H snijdt zichzelf.** Op een voxelfiguur vouwt de naar buiten geschoven huid in elke holte om: de meetregels tellen
   100 tot 300 paren driehoeken van H die elkaar snijden (`h_zelf_overlap`). Lukt de Exact-vereniging niet (controle
   op volume en kader), dan valt H terug op twee losse schillen door elkaar (`h_soort` "los"): 4263 paren op de heup van
   de robot, 470 tot 780 op de schouders van het aangeklede figuur.
2. **Een boolean met zo'n H is niet bepaald.** Elke slechte snede in 5.2 en 5.3 in de nulmeting had H "los" (16 van 16).
   Robot, linkerheup: delen gesloten maar in rust 9271 paren overlap tussen A en B, daarna "blocked". Aangekleed figuur,
   linkerschouder: 8 plekken achter elkaar met H "los", 2745 tot 3960 paren overlap, schouder overgeslagen. In 4.2
   (Exact zonder Self Intersection) gaf dezelfde soort H open randen (100 tot 290) of een leeg deel B (0 punten).
3. **Daarom CI 8 en lokaal 9.** Manifold rekent met afronding die per processor net verschilt (Olaf zag op Intel met
   AVX-512 een gave heup, in CI op AMD een kapotte, runs 45206324187 en 45208410893). Bij een geldige vorm maakt dat niets
   uit; bij een vorm die zichzelf snijdt kantelt de uitkomst. Verklaring: GOK, maar hij past bij elke meting hier.
4. **Wat het niet is.** Het snijvlak een fractie verschuiven (0,05 mm) of draaien (0,3 en 1,0 graad) gaf op elke slechte
   snede in 5.x dezelfde fout (overlap 9171 tot 9326 op de heup); Exact in plaats van Manifold ook (397 en 811 open
   randen). De figuren zelf snijden zichzelf niet (`bron_zelf_overlap` 0). De 0,3 mm-plek van 1.2.2 redde de robot alleen
   omdat H daar toevallig wel samen ging.
5. **4.2 heeft daarnaast een eigen fout.** Na een Exact-snede heeft een deel soms één rand met 4 vlakken, 27 tot 93 mm
   van het gewricht (twee stukken huid die in een lijn raken); en een scharniersnede geeft soms delen die in rust
   overlappen of een onderbeen van 717 punten (robotknie). Dat zit in de Exact-solver van 4.2, ook zonder H.

## Oplossing (allemaal Pro, het gratis deel blijft gelijk)
- `betaald/omhulsel.py`: H wordt één schone, gesloten vorm door een voxel-remesh van omhulsel en lid samen, met een
  controle dat het lid erin ligt; lukt dat niet, dan de oude weg. Dit is de echte oplossing: nul slechte sneden in 5.x,
  zonder geluk (zelfde uitkomst op AMD- en Intel-runners in CI, runs 45256924126 tot 45267268513).
  Bijstelling na run 45264302449 (GEZIEN): met Manifold alleen nog bij een mislukte vereniging ("los"); met voxel-H
  altijd verloor de rechterknie van de Meshy-knight 8,2 tot 9,2% van de punten (vangnet 6%) in plaats van 5,3 tot 5,6%,
  want de voxelvorm vult holtes en neemt wat stof naast het lid mee. In 4.2 (Exact) altijd voxel.
- `betaald/herstel.py`: in 4.2 een paar randen met 4 vlakken splitsen als het deel daarna gesloten is (geen punt verschuift).
- `rig.py`: na "overlap before they move" (scharnier in 4.2) de volgende plek, zoals al bij "no watertight parts".
- `betaald/redenen.py`: bij een overgeslagen gewricht door een mislukte snede zegt de lijst wat de koper kan doen
  ("place it by hand a few mm along the bone", in 4.2 ook "or use a newer Blender such as 5.2, which cuts more reliably"; 4.5 is niet gemeten, dus niet genoemd; niet bij "blocked"; "The cut failed" heeft een eigen zin).
- Geprobeerd en niet gehouden: scharnieren in 4.2 met het diepe omhulsel (`DIEP_EXACT`, run 45261862637): geen gewricht
  erbij. Scharniersnede in 4.2 met Self Intersection aan (run 45266243590): nooit gesloten; 0,05 mm verschoven: 2 van 6
  keer gesloten, dus geluk en niet gebouwd.

## Wat nog niet lukt (eerlijk)
- **Blender 4.2: 51 van 60 met de robot van studio-3 (op de zes figuren van de nulstand 28 naar 44 van 51)** (55 van 60 met die van studio-2, tabel boven). Robot: linkerschouder
  en linkerheup ("no room ... next to the elbow/knee": in 4.2 reikt het linkerscharnier verder, zijn snede is niet goed,
  bereik 0 tot 150 in plaats van 120) en linkerknie (delen overlappen in rust); robot-fijn: linkerschouder en linkerheup;
  aangekleed: rechterknie. Alle 5 herhalingen gelijk. De koper krijgt een zin met wat hij kan doen. Een echte 4.2-oplossing
  (de scharniersnede zelf in Exact) is een eigen spoor, niet vóór woensdag.
- **Tijd in 4.2:** daar is H altijd een voxelvorm, en Exact is traag. Mediaan nulstand tegen tak (runs 45273407326 en 45275271607): lichte figuren zijn **2 tot 3,6 keer trager** (rigify 64 naar 230 s, mens 84 naar 165 s, robot 125 naar 184 s); kleding werd sneller (761 naar 202 s), armen ook (49 naar 34 s). In 5.x is de tak even snel of sneller (kleding 166 naar 89 s, robot-fijn 397 naar 205 s).
- **Meshy knight (alleen in de gewone e2e, licentie niet zelf nagelezen, niet in de testset):** de rechterknie zit op de
  grens van het vangnet "lost part of the model" (6%): 5,3 tot 5,6% verloren, net als op main (zes metingen in run
  45267268513). Een grensgeval dat al bestond; met voxel-H altijd was het 8 tot 9% (daarom de bijstelling).
- **Keuring:** door de automatische keurder per commit (ja op fc5b58f, nee op 7ea796e om de drempel voor 4.2, opgelost in
  f804f10); een aparte keurder volgens
  `.claude/skills/keuren/SKILL.md` kon ik niet inzetten (geen Agent-tool). Keuring: nog niet gedaan.
