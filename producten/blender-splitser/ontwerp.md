# Split Joints (werknaam): ontwerp kern v0.1

Akkoord: nee (eerst de ontwerper, zie `merk/` zodra die er is)

Bouwer: agent van de hoofdchat, ma 23 nov 2026. Verder bouwen: de vaste Productbouwer.
Besluit: Thijs 23 nov ±16:25 NL, tweede product is een splitser met verbinders, beter dan CatPin en Cleave (`organisatie/besluiten.md`, onderaan).

## 1. Begrijpen
Een Blender-add-on die een model dat te groot is voor de printer in stukken snijdt die elk op het bed passen, met zo weinig mogelijk stukken, met pennen en gaten met gemeten speling op elk snijvlak, en een nummer in elk snijvlak zodat je weet wat waar hoort. Voor wie figuren, beelden en props print (dezelfde kopers als Click Joints).

Af voor deze kern (toetsbaar, in echte Blender 4.2 en 5.3 in CI):
- elk stuk past op het gekozen bed (A1 mini in de test) en is waterdicht;
- elke pen past in zijn twee gaten met de ingestelde speling (0,2 mm, gemeten met stralen in het stuk) en is niet langer dan de twee gaten samen;
- elk stuk heeft een verdiept nummer op elk snijvlak;
- export naar STL en 3MF werkt (bestand teruggelezen: maat gelijk, millimeter);
- een snijvlak dat je verschuift, verschuift de stukken mee;
- een vlak dat te klein is voor een pen geeft een duidelijke melding.

## 2. Wat er al was (hergebruikt uit Click Joints)
- `producten/blender-gewrichten/click_joints/gewricht.py` r. 29-73: keuze Manifold of Exact en de Boolean-modifier. Overgenomen in `splitsen.py`.
- `click_joints/gesloten.py`: telling van slechte randen, volume, Maak gesloten (voxel). Overgenomen in `gesloten.py`.
- `click_joints/drie_mf.py`: eigen 3MF-schrijver. Letterlijk overgenomen (alleen de naam in de metadata).
- `click_joints/exporteer.py` en `uit_elkaar.py`: export in mm met de echte plek, opengewerkt beeld met delta_location.
- `.github/workflows/blender-gewrichten-e2e.yml`: Blender ophalen met spiegels, zip valideren, tak schermen.

## 3. Open vragen, zelf beantwoord
- **Rechte assen of schuin snijden?** Eerst langs de wereldassen: voorspelbaar, snel, en een stuk ligt plat op een snijvlak. Draaien om Z om stukken te sparen komt later (zie 6).
- **Wanneer past een stuk?** Als zijn maat in een van de zes standen (90 graden draaien) binnen het bed valt, min de marge (standaard 2 mm, GOK). Wie print, draait een stuk toch in de slicer.
- **Hoeveel stukken?** We proberen alle roosters (nx, ny, nz) waarin elke cel past, en nemen het rooster met de minste cellen waar echt iets van het model in zit (een L-vorm spaart zo de lege hoek). Bij gelijkspel: de kleinste snijvlakken samen, dan liggende sneden.
- **Speling: per kant of in totaal?** Per kant, net als Click Joints: gat = pen + 2 x speling in doorsnede. De gatwand bestaat uit platte vlakken op precies de gatstraal (de punten liggen iets verder), de pen heeft zijn punten op de penstraal. De kleinste opening is dus precies de speling.
- **Pen te groot voor een vlak?** Eerst kleiner (5, 4, 3 mm). Past ook 3 mm niet, dan geen pen en een melding met de breedte van het vlak en wat een pen nodig heeft: "Glue this joint".
- **Nummer?** "3-5" op stuk 3 waar het aan stuk 5 vastzit, en "5-3" op stuk 5. Het eerste getal is altijd het stuk zelf. 0,6 mm diep, 2,5 tot 8 mm hoog, waar het vlak de meeste ruimte heeft, weg van de gaten.
- **Model niet waterdicht?** Splitsen weigert met een melding en de knop Make watertight (voxel) staat ernaast.
- **Wat bij rood?** Het stuk wordt wel gemaakt, maar rood gekleurd met de reden in het paneel (te groot, niet waterdicht, wand onder 0,8 mm).

## 4. Drie aanpakken
1. **Snel: bmesh bisect plus gaten vullen.** Snel en zonder Booleans, maar het vullen van een doorsnede met gaten erin (vaas, ring) is in Blender onbetrouwbaar en geeft open stukken. Nee.
2. **Netjes: eigen mesh-snijder in numpy.** Volledige controle, maar weken werk en elk randgeval zelf oplossen. Nee.
3. **Middenweg (gekozen): Boolean per cel plus een eigen plan in numpy.** Elk stuk is model doorsnede doos (Intersect), daarna gaten en nummers eraf (Difference). Dezelfde solvers die in Click Joints al bewezen waterdicht werken (Manifold op 4.5+, Exact op 4.2). Het plannen (welke sneden, waar de pennen, waar het nummer) doen we zelf op een raster van de doorsnede, los van Blender, dus snel te testen zonder Blender (`e2e/test_logica.py`).

## 5. Wat de kern doet (v0.1)
1. **Printer**: keuze uit 9 printers (maten uit de profielen van OrcaSlicer, DERDEN: `split_joints/printers.py`) of een eigen maat, en een marge.
2. **Plan cuts**: snijvlakken als platte objecten in de collectie "Split Joints cuts". Je schuift er een met G langs zijn as (de andere assen staan op slot) of typt de plek in het paneel; erbij en weg kan ook. Het paneel toont live hoeveel cellen op het bed passen.
3. **Split**: per cel een stuk, genummerd van onder naar boven. Op elk gedeeld vlak 1 tot 4 pennen per eiland (een los deel van het vlak, zoals twee benen), verspreid zodat de stukken niet draaien, minstens gatstraal plus 1,2 mm wand van de rand (3 mm meer waar het kan), en in 3D getoetst: genoeg diepte aan beide kanten, wand rond het hele gat, niet tegen een gat van een ander vlak.
4. **Controle per stuk**: past (groen) of niet (rood), waterdicht, kleinste wand rond de gaten. Kleur als materiaal en objectkleur.
5. **Export**: per stuk een STL of 3MF in mm, plus per pendikte een plaatje met alle pennen staand (een print).

## 6. Later (volgorde naar wat kopers het eerst merken, GOK)
1. Klikverbinders (snap) en zwaluwstaart naast pennen; pen vast aan een kant (geen losse pennen).
2. Draaien van het model om Z (en een vrije snijhoek) om stukken te sparen; sneden die naar een smalle plek schuiven.
3. Live voorbeeld van stukken en pennen voor je splitst, met kleuren op de snijvlakken.
4. Stukken plat op het bed leggen bij export (beste kant naar onder) en alles in één 3MF met platen.
5. Holle stukken (wanddikte instellen) voor grote beelden: minder plastic.
6. Testkaart voor de speling (zoals de Fit test strip van Click Joints Pro).
7. Uiterlijk en namen volgens de ontwerper (`merk/`), winkelplaatjes, README.

## 7. Wat getest wordt
Zie `architectuur.md`, deel Testen.

## 8. Stand ma 23 nov 2026 ±17:45 NL (bouwer van de kern)
- e2e groen in echte Blender 4.2.23 (Exact) en 5.3.0 (Manifold): run [45216254964](https://github.com/thijsduinhouwer2002-coder/dortus-hq/actions/runs/45216254964), 913 toetsen per versie, 0 fout (GEZIEN).
- Suzanne 330 mm: 8 stukken, 40 pennen; vaas 600 mm: 16 stukken, 32 pennen, maar **op 16 van de 28 naden past geen pen** (op minstens een deel van het vlak; de glaswand is daar 5 tot 6 mm, een pen van 3 mm vraagt 5,8 mm) en krijgt de koper de melding "too small for a pin ... Glue this joint". Op 320 mm hoogte (de eerste testmaat) paste op geen enkele naad een pen. Holle beelden en vazen krijgen dus bijna geen pennen: een kleinere verbinder of een blokje binnenin is werk voor later. Schedel 300 mm: 8 stukken, 44 pennen.
- Schermafbeeldingen (Workbench en het echte paneel): release [splitser-kern-1](https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/tag/splitser-kern-1). Zelf bekeken: stukken groen, gaten en "1-2" zichtbaar in het snijvlak, paneel leesbaar in de standaardbreedte van de zijbalk.
- Lessen: de "4" van het ingebouwde lettertype gaf in 4.2 (Exact) steeds 4 open randen, daarom een eigen pixelletter; tekst nooit van een al gesneden stuk aftrekken maar eerst van de doos; de wandmeting moet het eigen snijvlak overslaan.
- Nog niet gekeurd door een aparte keurder (skill `keuren`): dat is de eerste stap voor de Productbouwer.

## 9. Herstel na de keuring (ma 23 nov ±18:30 NL, `keuring/2026-11-23-kern.md`, akkoord nee)
- **M1, model in mm in een scene in meters:** schaalcheck uit Click Joints (`schaal.py`, onder 10 of boven 3000 mm) met de knop Convert to mm in het paneel; Plan cuts en Split weigeren dan met een melding, Make watertight weigert boven 3000 voxels. Rem op 200 cellen in het plan (`plan.MAX_CELLEN`, zoekt niet verder dan dat) en in Split. De telling in het paneel wordt bewaard tot sneden, bed of model veranderen en maakt boven 200 geen cellen meer; het paneel toont hooguit 20 sneden.
- **M2, plan telde hoekpunten:** het plan bemonstert nu de huid (elke driehoek, punten dichter dan 1/8 van de kleinste bedmaat) en telt ook een cel waarvan het midden binnen het model ligt. Kale doos 500 x 150 x 120: 3 stukken (was 2), plaat 600 x 600 x 30: 16 (was 4), volle kubus 500: 27. De 2.000 aangevulde punten in `test_logica.py` zijn weg.
- **M3:** de test eist op elk snijvlak met een buur een nummer (buren gemeten op de meshes) en leest de 3MF terug met de maat binnen 0,01 mm.
- **M4:** zin over de vaas hierboven eerlijk gemaakt (16 van de 28 naden zonder pen).
- Erbij (kan-punten): melding bij meer gekozen objecten, e2e met een kale doos zonder voxel (3 stukken, alle toetsen) en een open Suzanne zonder voxel (Split weigert), e2e in een scene in meters (zelfde doos als STL in mm: weigeren, omzetten, splitsen; Suzanne van 0,33 m: alle toetsen in mm).
- e2e groen in 4.2.23 en 5.3.0: run [45220594138](https://github.com/thijsduinhouwer2002-coder/dortus-hq/actions/runs/45220594138), 1323 toetsen per versie, 0 fout (GEZIEN).

## 10. Passingproef (Productbouwer, ma 23 nov 2026 ±19:30 NL, must have 1 uit `concurrentie.md`)
- **Wat:** in stap 3 een vak "Fit test: print this first". Kies je materiaal, klik Make fit test: een blok van ±68 x 18 x 8 mm (pen 5 mm, lengte 12) met 4 gaten voor je eigen pen (zelfde diameter en diepte als bij Split), de speling gegraveerd voor elk gat, plus 4 pennen. Export fit test schrijft het blok en de pennen als STL of 3MF. Na het printen klik je de speling die past; die wordt de speling van de scene en wordt bewaard in de voorkeuren van de add-on per printer en materiaal. Kies je later (ook in een ander bestand) dezelfde printer of hetzelfde materiaal, dan komt die speling vanzelf terug.
- **Keuzes:** 4 spelingen rond de ingestelde in stappen van 0,05 mm (0,20 geeft 0,15 / 0,20 / 0,25 / 0,30; zelfde bereik als de Fit test strip van Click Joints Pro). Eén blok met losse pennen in plaats van twee blokken: minder plastic, en de pen moet toch in elk gat los getoetst worden. Gaten staan rechtop (opening boven), net als een gat in een stuk dat met het snijvlak op het bed ligt. De proef gebruikt de hoofddiameter; kleinere pennen op kleine vlakken (Auto) zitten niet in de proef (GOK: zelfde speling werkt voor 3 tot 5 mm, nog niet gemeten op een printer).
- **Niet gedaan:** een echte print. Of 0,05 mm stappen fijn genoeg zijn is een GOK; CatPin raadt een proef aan zonder knop ([FAQ](https://superhivemarket.com/products/catpin/faq), DERDEN via `concurrentie.md`).
- **Getest:** `e2e/toetsen_passing.py` en 12 toetsen in `test_logica.py`. Lokaal in Blender 4.2.23: 97 toetsen groen (GEZIEN). Beelden: `passing-1.png` en `passing-2.png` in de release `splitser-kern-1`.
- **Herstel na de keuring** (`keuring/2026-11-23-passingproef.md`, akkoord nee): M1 het model blijft actief na Make fit test en Plan cuts en Split slaan het proefblok altijd over; M2 bij een nieuw of geopend bestand krijgt elke scene zonder zelf getypte speling de bewaarde speling (handler bij openen), plus een knop "Use saved" als ze afwijken; M3 de vier spelingen gaan nooit boven 1,0 mm (0,85 tot 1,00), dus elke knop bewaart wat erop staat. Toetsen erbij in `toetsen_passing.py` en `test_logica.py`; lokaal in 4.2.23 105 toetsen groen (GEZIEN). CI van de eerste versie (ccf3800): groen in 4.2.23 en 5.3.0, run [45228604028](https://github.com/thijsduinhouwer2002-coder/dortus-hq/actions/runs/45228604028) (GEZIEN).

## 12. Vrije snede: draaibaar snijvlak dat maar een deel raakt (Productbouwer, di 24 nov 2026 ±00:45 NL)
- **Wat en voor wie:** na Split kies je een stuk, klik **Add free cut** en zet het vlak met G, R en S waar je wilt (een arm bij de schouder, schuin). **Cut piece** snijdt alleen wat binnen de rechthoek ligt, aan de kant waar de pijl (lokale Z) heen wijst, met pennen en nummers zoals bij de gewone sneden. Dit is het verschil met de gratis slicer, die altijd door het hele model snijdt. Af = de e2e-toets `e2e/toetsen_vrij.py` slaagt in 4.2 en 5.3.
- **Drie aanpakken:** A) vrije snede op één stuk na Split (klein, raakt plan en rooster niet); B) vrije sneden vóór het rooster, daarna een rooster per deel (minste stukken, maar plan, nummering en pennen moeten allemaal om); C) het hele rooster om Z draaien (raakt nog steeds het hele model, dus niet wat gevraagd is). **Gekozen: A**, omdat het binnen een run werkt, niets van de gekeurde kern breekt en alles erna (kleur, controle, uit elkaar, export) gewoon meedoet. B kan later als kopers vragen om minder stukken.
- **Hoe:** het stuk wordt in rekenen gedraaid zodat het vlak plat op z = 0 ligt; dan plant dezelfde `verbind_3d.plan_alles` pennen en nummer als voor twee cellen boven elkaar, en worden gaten en nummers terug gedraaid. Nieuw stuk = stuk maal een doos over de rechthoek (tot voorbij het stuk); rest = stuk min die doos. Nieuwe gaten bewaren hun richting als `n`; `controle.py` meet de wand nu ook langs een schuine as.
- **Weigeren in plaats van gokken:** raakt de doos het stuk met een zijwand (rechthoek te klein, of er zit meer van het stuk aan die kant), dan weigeren we met "scale the plane up". Ook geweigerd: een vlak dat het stuk mist, en een vlak door of te dicht bij een bestaand pengat (binnen de minimale wand).
- **Kleur:** de twee helften houden hun rooster-cel, maar zijn buren van elkaar (`sj_vrij_buren`), dus nooit dezelfde kleur.
- **Niet gedaan:** een vrije snede op het model vóór Split (aanpak B); pen-kant kiezen op printrichting; meer dan één vrije snede tegelijk (wel na elkaar). Het nummer staat in het overzichtsbeeld op zijn kant als de snede rechtop staat; van voren gezien leest het goed.
- **Getest:** lokaal in Blender 4.2.23 alle 25 toetsen van `toetsen_vrij.py` groen (GEZIEN): figuur met arm, snede 90 graden plus 15 graden om Z, 2 stukken waterdicht en groen, armeinde 47,9 tot 80,0 mm, volumes tellen op (79.357 voor, 79.058 na, gaten 289 mm3), elk nieuw gat 6,30 mm diep langs de normaal aan beide kanten, nummers 1-2 en 2-1, verschillende kleuren, 1 pen; geweigerd: rechthoek te klein, vlak naast het stuk, vlak door een pengat. `test_logica.py` groen. Beelden `vrij-1-stukken.png` en `vrij-2-snijvlak-1-2.png` (zelf bekeken: schuin snijvlak met gat en "1-2"); CI zet ze in release `splitser-kern-1`.

## 13. Split to fit: één knop (Productbouwer, di 24 nov 2026, opdracht hoofdchat 23 nov 23:35 en 24 nov 01:25)
- Bovenaan het paneel: printer, de knop **Split to fit** (de enige blauw opgelichte knop), één uitslagregel ("3 parts, all fit the bed" plus "8 pins, 0.20 mm clearance") en een kleinere knop Export parts. De vier genummerde stappen staan onder het inklapbare vak More settings.
- Wat de knop doet (`in_een_klik.py`): kiest het model (het actieve mesh als dat geen stuk, pen, snede of proefblok is, anders het model van de sneden), maakt een open model eerst dicht, dan Plan cuts, Split met pennen, gaten en nummers, en de controle. Printer en speling komen uit het paneel; de bewaarde speling uit de passingproef zit daar al in.
- Fout: één rode regel met wat je moet doen ("Wrong unit? Open More settings and use Convert to mm"). Convert to mm wist die regel.
- Bewijs in de e2e (`e2e/toetsen_klik.py`): één klik geeft dezelfde stukken, pennen en volumes als Plan cuts plus Split; een tweede model in dezelfde scene wordt het nieuwe model; meters weigeren binnen 5 seconden en snijden na Convert to mm wel.
