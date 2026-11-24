# Keuring Split to fit, naam Click Cuts, snedeplek en vrije snede, 24 nov 2026, keurder klik
Wat ik keurde: commit c651793 (en 27951bb voor de vrije snede) in `producten/blender-splitser/`, opdrachten van de hoofdchat van 23 nov 23:35 en 24 nov 01:25 onderaan `berichten/productbouwer.md`, ontwerp.md deel 12.
Akkoord: nee (twee moet-punten, beide klein)

Hoe gemeten: zip gemaakt met `e2e/maak_zip.sh`, in Blender 5.3.0 lokaal `e2e/toetsen_klik.py` en `e2e/toetsen_vrij.py` gedraaid (beide `KLAAR 0 FOUT []`, GEZIEN), plus een eigen meetscript buiten de repo dat de add-on aanroept en de meshes meet (cilinder met Array-modifier, tweede model in dezelfde scene, andere printer en speling, vrije sneden op andere plekken). CI-run 45305657263 op c651793: 4.2.23 groen (GEZIEN), 5.3.0 liep nog bij het afsluiten van deze keuring. Paneelbeeld `blender-4.2.23-paneel-x.png` uit release `splitser-kern-1` (01:33 UTC) zelf bekeken.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Vrije snede werkt: 2 stukken, waterdicht en groen, gaten 6,30 mm diep langs de schuine normaal, nummers 1-2 en 2-1, 1 pen (log toetsen_vrij in 5.3.0). Na elkaar snijden werkt ook: een tweede vrije snede op stuk 2 bij x=70 en op stuk 1 bij x=30 gaf 3 en 4 stukken. | feit | hoog | eigen meetscript |
| A2 | **De toets "snede door een pengat geweigerd" bewijst het niet.** Stuk 2 staat na de snede in het uit-elkaar-beeld op wereld-x 56,35 tot 88,48 (gemeten); het vlak op x=52 mist het stuk dus helemaal en wordt geweigerd met "does not go through Piece 02". De toets kijkt alleen naar CANCELLED, niet naar de reden. | feit | hoog | log toetsen_vrij en eigen meting van de hoekpunten |
| A3 | De pengat-weigering zelf werkt wel: stuk 2 bij x=60 en stuk 1 bij x=46 en x=40 geweigerd met "goes through a pin hole of Piece 0x (to piece y). Move it at least 1.2 mm away"; daarbuiten (x=70, x=30) snijdt hij. | feit | hoog | eigen meetscript |
| A4 | Naam Click Cuts: manifest id `click_cuts` en name, tabblad en paneel "Click Cuts", collecties "Click Cuts cut planes", "Click Cuts pieces", "Click Cuts fit test", materialen "Click Cuts piece 01..", "Click Cuts pins", "Click Cuts green", 3MF-metadata "Click Cuts", exportmap `//click_cuts/`. Geen zichtbare "Split Joints" meer over (grep), alleen interne klassenamen. | feit | hoog | grep, lijst van collecties en materialen na een klik, paneelbeeld |
| A5 | Split to fit geeft dezelfde stukken als Plan cuts plus Split, ook op een eigen model dat anders is dan de testmodellen: cilinder 180 x 420 mm met Array-modifier (2x) en 20 graden gedraaid, speling 0,30: 18 stukken, 138 pennen, zelfde maten, gaten per stuk en status, beide wegen `GELIJK True`. Gat-straal 2,80 mm volgt de speling. | feit | hoog | eigen meetscript |
| A6 | Andere printer en speling volgen: na K1 en 0,15 mm gaf een nieuwe klik 8 stukken (180 x 127 x 210 mm), uitslag "8 parts, all fit the bed / 30 pins, 0.15 mm clearance". | feit | hoog | eigen meetscript |
| A7 | **Split to fit op een tweede model snijdt het oude model opnieuw.** Na een klik op de cilinder een bol gemaakt, alleen de bol geselecteerd en actief, Split to fit: `bron` bleef "Cyl", de cilinder werd opnieuw in 18 stukken gesneden, de bol bleef heel. De knop zegt "Cut the selected model". Oorzaak: `snedes.model()` neemt eerst `scene.split_joints.bron`. Een koper die een tweede model in hetzelfde bestand laadt, ziet zijn eerste model weer gesneden en niets aan zijn nieuwe. | feit | hoog | eigen meetscript, regel 100 van `snedes.py` |
| A8 | Eén uitslagregel klopt met de stukken ("3 parts, all fit the bed", "8 pins, 0.20 mm clearance"), meters weigeren direct met "Wrong unit? Open More settings and use Convert to mm", open Suzanne krijgt eerst een dichte kopie. Vier stappen staan onder een inklapbaar "More settings" (paneelbeeld). | feit | hoog | log toetsen_klik, paneelbeeld 4.2 |
| A9 | Snedeplek: `Object.sj_plek_mm` heeft precisie 1 (0,1 mm), stap 0,1 mm, en leest en zet goed in een mm- en een meter-scene (12,3 mm wordt 0,0123 m). In het paneelbeeld staat More settings dicht, dus de afgeronde weergave heb ik niet met eigen ogen gezien. | feit (beeld: vermoeden) | hoog / midden | RNA-precisie en toets; beeld met More settings open |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Bestaande tests niet verzwakt: alleen namen aangepast, de kleurtoets is strenger geworden (exacte materiaalnamen). | feit | hoog | tests niet aangepast om te slagen |
| B2 | Alle bestanden onder 400 regels (grootste `vrije_snede.py` 364). | feit | hoog | ±400 regels |
| B3 | `architectuur.md` bijgewerkt met `in_een_klik.py`, `sj_plek_mm`, paneel en beide toetsen. `ontwerp.md` heeft nog geen deel voor Split to fit. | feit | hoog | architectuur bijgewerkt |
| B4 | Geen persoonsgegevens in de diff gevonden. | feit | midden | openbare repo |
| B5 | Toets A2 claimt in de docstring en in ontwerp deel 12 "geweigerd: vlak door een pengat" als bewezen, terwijl het om een andere reden weigert. | feit | hoog | eerlijk, werk pas af als de tests het bewijzen |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Het paneel is nu kort en duidelijk: printer, Split to fit, één vak met vinkje, Export. Dat is de 60-secondenbelofte. | (goed zo) | |
| C2 | De knop Split to fit is grijs, net als Export; in de schets is hij goud en springt hij eruit. | knop met `depress` of een opvallender icoon, of Export kleiner zodat Split to fit de enige grote knop is | klein |
| C3 | De rij Connectors (Pins, Click, None) uit de schets ontbreekt. | later toevoegen als Click-verbinders er zijn; nu niet nodig | midden |
| C4 | De printerkeuze staat twee keer (bovenaan en in stap 1). | in stap 1 alleen marge en eigen maten | klein |
| C5 | Na een geweigerde klik blijft de rode regel "Wrong unit?" staan, ook na Convert to mm, tot de volgende klik. | Convert to mm wist de regel | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
- M1 (A7): Split to fit moet het geselecteerde model snijden. Is het actieve object een ander mesh dan `bron` (en geen stuk, pen, snede of proefblok), dan wordt dat het nieuwe model en worden de oude sneden en stukken niet hergebruikt. Toets erbij in `toetsen_klik.py`: tweede model in dezelfde scene, klik, de stukken komen van het tweede model.
- M2 (A2, B5): de toets "snede door een pengat geweigerd" moet het pengat raken en op de reden toetsen (melding bevat "pin hole"), bijvoorbeeld vlak op het echte gat van stuk 2 in het uit-elkaar-beeld of uit-elkaar eerst uit. Plus een toets dat een vlak net buiten het gat wel snijdt.

**Kan**
- K1 (A9): schermafbeelding met More settings open, zodat "Cut X (mm) 101.5" met eigen ogen te zien is.
- K2: CI 5.3.0 op c651793 groen zien voor de kandidaat van do 27 nov.
- K3: deel in `ontwerp.md` voor Split to fit.
- K4: C2, C4, C5 hierboven.

## Herkeuring M1, M2 en kan-punten (ea51a74, 817d650), 24 nov 2026
Wat ik keurde: commit ea51a74 (M1 `in_een_klik.kies_model`, M2 toets in `e2e/toetsen_vrij.py`, printer één keer) en 817d650 (knop opgelicht, Export kleiner, Convert to mm wist de rode regel, paneelbeeld met More settings open, ontwerp.md deel 13), nu op main.
Akkoord: ja

Hoe gemeten: zip gemaakt met `e2e/maak_zip.sh`, in Blender 5.3.0 lokaal `toetsen_klik.py` en `toetsen_vrij.py` gedraaid: beide `KLAAR 0 FOUT []` (GEZIEN). Daarnaast drie eigen meetscripts buiten de repo (scratchmap) die de add-on aanroepen en de stukken meten. CI-run 45319700708 op 817d650: 5.3.0 en 4.2.23 beide groen, uitslag success (GEZIEN). Beelden `blender-5.3.0-paneel-x.png` en `blender-5.3.0-paneel-meer.png` uit release `splitser-kern-1` (03:30 UTC, uit die run) zelf bekeken.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| H1 | **M1 opgelost.** Cilinder (r 90, 420 mm) geklikt: 12 stukken rond x 0. Daarna een bol (r 150) op x 800 gemaakt, alleen die geselecteerd en actief, Split to fit: bron "Bol", 8 stukken op x 631 tot 969, de stukken van de cilinder zijn weg, de cilinder zelf bestaat nog (verborgen). | feit | hoog | eigen meetscript |
| H2 | Met een stuk, een penplaatje, een snedevlak, het proefblok of de proefpennen actief geeft een klik steeds weer de bol (bron "Bol", 8 stukken, zelfde plek). Cilinder weer zichtbaar en gekozen: die wordt weer het model (12 stukken). Niets actief: het laatste model. Alle objecten van de add-on dragen een van de vlaggen die `kies_model` overslaat (`sj_stuk`, `sj_pennen`, `sj_as`, `sj_passing`, `sj_vrij`), dus er is geen object dat per ongeluk als model telt. | feit | hoog | eigen meetscript, lijst van objecten met hun vlaggen |
| H3 | De nieuwe toets in `toetsen_klik.py` (tweede doos "Second", gekozen, klik) toetst op bron, aantal en maat van de stukken: OK in mijn run. | feit | hoog | log toetsen_klik |
| H4 | **M2 opgelost.** De toets zet het vlak nu op het echte gat van stuk 2 (punt van het gat plus halve diepte langs de normaal plus de uit-elkaar-verschuiving `delta_location`) en toetst op "pin hole" in de melding; log: "goes through a pin hole of Piece 02 (to piece 1)". De tweede toets (3 mm voorbij de bodem van het gat) snijdt: 3 stukken. | feit | hoog | log toetsen_vrij |
| H5 | Zelf de grens gemeten met hetzelfde vlak op verschillende diepten (gat 6,30 mm diep): 0,3, 3,15, 6,0, 6,8 en 7,3 mm geweigerd met "pin hole"; 7,8 mm snijdt. Dat klopt met "Move it at least 1.2 mm away". -0,5 mm (buiten het stuk) geeft terecht "does not go through Piece 02". | feit | hoog | eigen meetscript |
| H6 | Split to fit is in het beeld de enige blauw opgelichte knop, Export parts (STL) eronder is duidelijk kleiner. | feit | hoog | paneel-x.png 5.3.0 |
| H7 | Tweede beeld met More settings open: stap 1 heeft nu alleen Margin en "Usable: 176 x 176 x 178 mm" (printer niet meer dubbel), snedelijst "Cut X (mm) 5.0, Cut Y (mm) -2.8, Cut Z (mm) 116.9" met één decimaal, telling "8 cells, 8 fit the bed". | feit | hoog | paneel-meer.png 5.3.0 |
| H8 | Convert to mm wist de rode regel en daarna snijdt de klik wel (toetsen "Convert to mm wist de rode regel" en "na Convert to mm snijdt hij wel": OK, 3 stukken). De code wist alleen een regel die met "Wrong unit" begint, andere foutregels blijven staan. | feit | hoog | log toetsen_klik, `schaal.py` |
| H9 | ontwerp.md deel 13 beschrijft de knop, de keuze van het model, de foutregel en wat de e2e bewijst; klopt met wat ik mat. | feit | hoog | ontwerp.md |
| H10 | Regels: bestaande toetsen niet verzwakt (de oude pengat-toets is strenger geworden), bestanden onder 400 regels (toetsen 167 en 185), architectuur.md bijgewerkt voor `kies_model` en `depress`, geen persoonsgegevens in de diff. | feit | hoog (persoonsgegevens: midden) | git diff, wc |

## Deel C (herkeuring): zou een gebruiker het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| HC1 | Na een klik op een tweede model verdwijnen de stukken van het eerste model en blijft het eerste model verborgen. Een koper die twee modellen in één bestand heeft, ziet zijn eerste model niet meer terug en moet het in de Outliner zichtbaar maken om het weer te snijden. | het oude model weer zichtbaar maken als een ander model gesneden wordt, of één regel "Previous model hidden: Cyl" | klein |
| HC2 | Direct na een klik staat in het uitslagvak ook "Move a cut in More settings, then Split". Na een eerste klik is dat een derde regel die de koper niet nodig heeft, en "then Split" zegt niet welke knop (Split to fit of Split in stap 3). | regel alleen tonen als een snede verschoven is, of "then Split to fit" | klein |
| HC3 | Is een ander mesh geselecteerd maar een stuk actief, dan snijdt de klik het oude model. Dat is de gewone Blender-regel (actief telt), dus geen fout. | (goed zo) | |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen. M1 en M2 zijn opgelost en zelf gemeten.

**Kan**
- K5 (HC1): het vorige model weer zichtbaar maken of melden als een ander model gesneden wordt.
- K6 (HC2): de regel "Move a cut in More settings, then Split" alleen na een verschoven snede, en de knop bij naam noemen.
- K7: de toets "net voorbij het gat" op 1,5 mm in plaats van 3 mm zetten, dan bewaakt hij de grens van 1,2 mm echt (zelf gemeten: grens ligt tussen 7,3 en 7,8 mm).
- K8: architectuur.md noemt bij `passingproef.py` nog de oude collectienaam "Split Joints fit test".
