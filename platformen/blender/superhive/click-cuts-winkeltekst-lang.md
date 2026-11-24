# Click Cuts: tweede winkeltekst, lange versie (CONCEPT, 24 nov 2026)

**Leidend is de tekst van Chris in `click-cuts-winkeltekst.md`** (titel, varianten en bundel met eigen curl-metingen en de Gumroad-hulp). Dit bestand schreef een agent van de hoofdchat tegelijk, omdat de opdracht stil leek te staan. Het is een aanvulling: Chris neemt over wat hij wil (vooral de volledige beschrijving met "Where to find it", "Good to know", de regel "Tested in Blender 4.2 and 5.3 on every change", de kruisverwijzing naar Click Joints Pro en het blok Keywords). Waar de twee verschillen, geldt na de keuring de tekst van Chris.

Geschreven door een agent van de hoofdchat, in plaats van Chris (opdracht hoofdchat kwartier 24 nov ±04:25, aanvullingen 06:25 bundel en 06:34 printtitels, `berichten/chris.md` r. 1082 tot 1107). Skill `update-tekst`. Status: **CONCEPT tot de keuring**. Plakken: Thijs, in dezelfde ronde als de uitgave (week van ma 30 nov). Prijzen zet Thijs zelf; dit is geen geld uitgeven.

Gaat over **versie 1.0.0** (kandidaat, `producten/blender-splitser/CHANGELOG.md`). Elke zin in de Engelse tekst is nagekeken tegen de code in `producten/blender-splitser/split_joints/` (tabel onderaan).

## Waarom zo

- **Zoekwoorden in de titel vanaf dag 1.** Op Superhive staan vier van de vijf best verkopende buren met "3D Print" of "for 3D Printing" in de titel, en op "3d printing" staan Lattice Generator (#1) en Cleave (#3) bovenaan; Click Joints Pro, zonder die woorden in de titel, staat niet in de eerste 144 (GEZIEN door de Verspreider, curl 24 nov ±02:55 UTC, `commercie/verspreiden/2026-11-24-superhive-titel-3d-printing.md`). Titels van de buren (zelfde bron en `ideeen-kwartier.md` 04:25): Cleave "Smart Model Split & Cut for 3D Printing With Connectors (Pegs, Dowel, Rod Channel, Magnets, Ball Joints)", SnapSplit "Cuts & Custom connector builds for 3D printing", JointLab "... for 3D Printing". De woorden die buren gebruiken: **split, cut, 3D printing, connectors, pegs/pins**. Niemand heeft **printer bed** of **fit** in de titel, terwijl dat precies is wat wij beter doen.
- **Zelf met curl getoetst: lukte niet.** Op 24 nov gaf elke aanvraag naar superhivemarket.com (en gumroad.com) vanuit deze sessie "CONNECT tunnel failed, response 403" van de proxy (GEZIEN). De zoekwoorden hierboven komen dus uit de metingen van de Verspreider en de hoofdchat van vannacht. Wie later kan curlen: meet de plek van Click Cuts op "split", "3d printing", "printer bed" en "connectors" in de eerste week na live.
- **Titel over de print, niet over Blender** (Afkijker 06:34: titels over het printresultaat halen het meest, GEZIEN bij Painted4Combat). Daarom staat "Blender" niet in de titel; Superhive is al een Blender-winkel.
- **Eerste zin met wat geen concurrent zegt:** printer kiezen, één knop, elk deel past op je bed, en een passingproef met je eigen pen. CatPin laat de printermaat aan de koper ("user remains responsible ... printer volume"), Dovetail Key heeft geen past-op-bed, en geen van de grote vier heeft een passingproef in de splitser (GEZIEN 23 nov door de concurrentie-analist, `producten/blender-splitser/concurrentie.md` tabel 2a). Cleave heeft wel printerkeuze; wat Cleave niet heeft is de passingproef. Kopers bij naam, zoals Cleave doet: busts, statues, cosplay props, terrain, large figures.
- **Geen concurrent bij naam in de tekst** (`concurrentie.md`: nooit afkraken).
- **Wat 1.0.0 niet doet, staat er eerlijk in** (geen klikverbinders, geen magneten, geen zwaluwstaart, delen niet vanzelf plat op het bed, holle dunne wanden krijgen vaak geen pen). Zo koopt niemand iets wat er niet in zit, en vraagt niemand zijn geld terug.

## 1. Titel

```
Click Cuts: Split Big Models for 3D Printing to Fit Your Printer Bed, with Pin Connectors
```
89 tekens (Cleave heeft ±110, dus de lengte kan). Reserve als een veld korter blijkt (64 tekens):
```
Click Cuts: Split Models for 3D Printing to Fit Your Printer Bed
```

## 2. Excerpt (korte regel onder de titel)

```
Pick your printer, press one button, and every part of your model fits the bed, with pins, holes and a number on each cut face. Print the fit test first to find the clearance that fits your printer.
```

## 3. Beschrijving (Superhive en Gumroad gelijk)

```
**Too big for your printer? Pick the printer, press one button, every part fits the bed.**

Click Cuts splits big models for 3D printing (busts, statues, cosplay props, terrain, large figures) into watertight parts that each fit your printer bed, with pins, pin holes and a number on every cut face. A fit test print with your own pin tells you which clearance fits your printer before you print the big parts.

What you get:
- **Split to fit.** Choose your printer and press Split to fit. Click Cuts plans the cuts with as few parts as it can, cuts the model, places the pins and holes, and engraves the numbers. One line tells you the result, for example "3 parts, all fit the bed".
- **Printer list.** Bambu Lab A1 mini, A1, X1 / P1 series and H2D, Prusa MK4, Core One and MINI, Creality Ender 3 and K1, or your own bed size. A margin keeps room free on every side of the bed.
- **Fit test: print this first.** One button makes a small block with four holes for your own pin, at four clearances, with each clearance engraved next to its hole, plus four pins. Print it, click the clearance that fits, and Click Cuts keeps it for that printer and material (PLA, PETG, ABS/ASA, TPU, resin or other), also in your next file.
- **Pins that line up.** 1 to 4 pins per cut face, spread out so the parts do not turn. Pins are separate, with chamfered ends, and are exported standing up, one plate per pin size. Where a 5 mm pin does not fit, Click Cuts uses a smaller one, down to 3 mm.
- **Numbers on the hidden faces.** "3-5" on part 3 where it meets part 5, engraved into the cut face, so you know what goes where.
- **Check before you print.** Every part is green (fits the bed, watertight, enough wall around the holes), orange (fits, but thin wall around a hole) or red, with the reason.
- **Free cut.** After splitting, add an extra cut at any angle through one part, for example an arm at the shoulder, with pins and numbers like the other cuts.
- **Colour per part** in an exploded view, neighbours never the same colour.
- **Export** all parts and pins as STL or 3MF, in millimetres.

Where to find it: the sidebar in the 3D viewport (press N), tab Click Cuts. Printer and Split to fit are at the top; every step is under More settings.

Good to know:
- Clearance is 0.20 mm per side by default. Print the fit test first; every printer and material is different.
- Open meshes are made watertight first with a voxel remesh on a copy; your original is kept.
- A model in millimetres in a scene in metres is caught at once, with a Convert to mm button.
- Hollow models with thin walls (a vase, a thin shell) often have no room for a pin. Click Cuts then tells you the joint is too small for a pin and to glue it.
- Version 1.0 has round pins only: no snap connectors, magnets or dovetails yet. Cuts follow the X, Y and Z axes, plus the free cut. Parts are not laid flat on the bed for you; do that in your slicer.
- Blender 4.2 and newer. Tested in Blender 4.2 and 5.3 on every change.
- Pure Python, no other add-ons needed.

**Make it move: Click Joints Pro.** Splitting makes it fit on the bed. Click Joints Pro makes it move: open a part, put the 3D cursor on the knee or elbow, and it cuts a hinge with an end stop or a ball joint right there, with the range in degrees.

**Figure Print Kit: Click Joints Pro + Click Cuts.** Split your figure to fit the bed, then make it move. Both add-ons together for less in the Figure Print Kit.

Keywords: split model for 3D printing Blender, cut model into parts for 3D printing, fit model to printer bed, too big for print bed, split STL into parts Blender, 3D print connectors Blender, pin connectors 3D print, dowel pins split model, split bust for 3D printing, split cosplay prop for 3D printing, split statue for 3D printing, print large model in parts, printer bed size Blender addon, numbered parts 3D print, clearance fit test 3D print, STL and 3MF export Blender
```

## 4. Varianten (Thijs zet de prijzen)

| Variant | Prijs | Wat |
|---|---|---|
| Standard | **$19 tot en met zo 14 dec**, daarna **$24** | de add-on, alle updates |
| Supporter | **$29** | dezelfde add-on en updates; de rest helpt de volgende updates betalen |

Tekst bij Supporter (Engels): `Same add-on and updates as Standard. The extra helps fund the next updates.`

Onderbouwing: de best verkopende buren zitten op $18 tot $24 en hebben bijna allemaal een duurdere steunvariant met dezelfde functies: Cleave $23 en Support $28, CatPin $24 en Supporter $36, Split 3D Print $22 en Support $28, Dovetail Key $18 (GEZIEN 23 nov door de concurrentie-analist, links in `concurrentie.md` 2a). Startprijs $19 tot 14 dec uit `concurrentie.md` punt 5. Supporter $29 (niet $34 zoals in `concurrentie.md`) volgt de opdracht van de hoofdchat (04:25), dicht bij Cleave. Hoeveel kopers Supporter nemen: GOK ±1 op 10 (`ideeen-kwartier.md` 04:25). Studio en een gratis variant: niet nu (gratis kost op Superhive een betaald makersabonnement, DERDEN via `README.md` in deze map, artikelen 281 en 302).

## 5. Bundel "Figure Print Kit: Click Joints Pro + Click Cuts"

**Zin voor op beide pagina's** (Engels, staat al in de beschrijving hierboven; op de pagina van Click Joints Pro onderaan erbij):
```
Figure Print Kit: Click Joints Pro + Click Cuts. Split your figure to fit the bed, then make it move. Both add-ons together for less in the Figure Print Kit.
```

**Bundeltekst** (eigen productpagina van de bundel):
```
Title: Figure Print Kit: Click Joints Pro + Click Cuts (Split and Articulate Figures for 3D Printing)

Too big for your printer, and you want it to move? Click Cuts splits your model so every part fits your printer bed, with pins, holes and numbers. Click Joints Pro reads your rig and cuts hinges with an end stop and ball joints, with every range in degrees before you print. Print the fit test of each add-on first to find the clearance that fits your printer.
```
De Pro-zin volgt de gekeurde titeltekst (`titel-2026-11-24.md`, ja van Daan na M1): "reads your rig", "hinges and ball joints", bereik in graden. Bewust zonder "end stop from your rig" (Daan M1: alleen als de rig grenzen heeft). "Fit test of each add-on" alleen plakken als de Pro-zip op Superhive 1.2 of hoger is (de Fit test strip zit pas in Pro 1.2; op 24 nov stond Superhive op 1.1.0, GEZIEN door Daan ±04:30); anders die zin weglaten.

**Prijs:** voorstel **$34** (hoofdchat 06:25). Let op de rekensom, want de korting hangt af van de losse prijzen:
- Gumroad na 14 dec: los $19 (Pro, GEZIEN door de hoofdchat 06:20) + $24 = $43, bundel $34 scheelt $9 (21%).
- Gumroad tot 14 dec: los $19 + $19 = $38, bundel $34 scheelt maar $4. Voorstel: in de startweken bundel **$31** (±20% van $38), na 14 dec $34.
- **Superhive nu:** Pro staat daar op $12 (GEZIEN door de hoofdchat 06:20, "nog $12 tot na de Cyber Sale"), dus los $12 + $19 = $31, **goedkoper dan de bundel van $34**. Zet de bundel op Superhive pas aan als Pro daar naar $19 gaat, of reken hem op dat moment opnieuw uit (±20% onder de som van de losse prijzen).

**Kan een bundel van één maker, en hoe:**
- Superhive: bundels bestaan en krijgen een eigen blok op de voorpagina ("Top Selling Bundles This Week", "Brand New Bundles"), en bundels van één maker staan er (TrueDepth + Cinepack van Lewis Martin, $35, 40+ verkopen); bij bundels van meer makers staat "Multiple Creators" (GEZIEN door de Afkijker 22 nov, https://superhivemarket.com/products/truedepth--cinepack-bundle en de voorpagina, `platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-22-truedepth-bundels.md`). Hoe je hem instelt: niet gevonden; zoeken op "bundle" in support.superhivemarket.com gaf op 22 nov geen artikel (GEZIEN door de Afkijker, zelfde bestand). Vandaag kon ik niet curlen (proxy 403). Thijs ziet het in zijn makerdashboard bij een nieuw product (GOK).
- Gumroad: er staat een bundel van één maker op Gumroad (3D Print Suite van Sonneblom Digitaal, 18 add-ons, $139, GEZIEN door een eerdere agent, `platformen/succes/verhalen-groei.md` r. 706). Dat Gumroad een producttype "Bundle" heeft waarin je eigen producten kiest: GOK, niet nagelezen in de hulp (curl naar gumroad.com gaf vandaag 403). Eerste stap voor wie wel kan curlen: de Gumroad-hulp lezen op "bundle" en de link hier zetten.
- Dus: Gumroad zeker als het producttype er is; Superhive zodra Pro daar $19 kost.

## 6. Korte post (CONCEPT voor de Maker van Roep, keuring door de Keurder van Roep, plaatsen alleen via de vaste weg)

Printtitel, zonder "Blender" en zonder productnaam in de titel (Afkijker 06:34):
```
Titel: Print a statue bigger than your printer bed
Every part fits the bed, with pins and a number on each cut face. Print the small fit test first, pick the clearance that fits, then print the big parts.
```
Beeld: het splitsbeeld uit release `splitser-merk-1` of een echte print zodra die er is. Naam en Blender alleen in beeld en beschrijving.

## 7. Nagekeken tegen de code (versie 1.0.0)

| Zin in de tekst | Klopt omdat |
|---|---|
| Split to fit, één knop, "3 parts, all fit the bed" | `in_een_klik.py` (bl_label "Split to fit"), `ontwerp.md` deel 13 |
| as few parts as it can | `ontwerp.md` deel 3: rooster met de minste cellen waar model in zit |
| printerlijst, 9 printers plus eigen maat, marge | `printers.py` r. 8 tot 16, `eigenschappen.py` (Margin, standaard 2 mm) |
| fit test: 4 gaten, 4 spelingen gegraveerd, 4 pennen, bewaard per printer en materiaal, ook in een volgend bestand | `passingproef.py`, `passing.py` (MATERIALEN r. 17 tot 24), `ontwerp.md` deel 10 en herstel M2 |
| 1 tot 4 pennen per vlak, verspreid tegen draaien | `verbinders.py` (MAX_PENNEN 4, doel_aantal) |
| losse pennen met afgeschuinde uiteinden, staand geëxporteerd, één plaat per pendikte | `vormen.py` (AFSCHUINING_MM 0.4, "standing pin"), `exporteer.py` (pins_..mm), `ontwerp.md` deel 5 |
| kleinere pen tot 3 mm | `eigenschappen.py` pen_auto: "down to 3 mm" |
| nummer "3-5" gegraveerd | `ontwerp.md` deel 3, `eigenschappen.py` r. 56 |
| groen, oranje, rood met reden | `controle.py` r. 1 tot 21; oranje is sinds 36912d5 echt oranje (keuring Daan 13:30 opgelost) |
| free cut, elke hoek, één deel | `vrije_snede.py` (Add free cut, Cut piece), `ontwerp.md` deel 12 |
| buren nooit dezelfde kleur, pennen goud | `eigenschappen.py` r. 74 ("neighbors never the same. Pins in gold") |
| STL of 3MF in mm | `exporteer.py` r. 1 |
| N-paneel, tab Click Cuts, More settings | `paneel.py` r. 1 en 23 |
| 0,20 mm per kant standaard | `eigenschappen.py` speling_mm default 0.2; `ontwerp.md` deel 3 "per kant" |
| open mesh dicht met voxel op een kopie, origineel bewaard | `gesloten.py` r. 47 |
| mm in meters gevangen, Convert to mm | `schaal.py` r. 38, CHANGELOG |
| holle dunne wanden geen pen, "Glue this joint" | `verbinders.py` r. 99, `ontwerp.md` deel 8 (vaas: 16 van 28 naden zonder pen, GEZIEN door de bouwer) |
| alleen ronde pennen, assen plus vrije snede, niet plat gelegd | `ontwerp.md` deel 6 (klik, zwaluwstaart, plat leggen staan op "later"); geen magneet in de code (`grep magnet` leeg) |
| Tested in Blender 4.2 and 5.3 on every change | `.github/workflows/blender-splitser-e2e.yml`: start bij elke push op `producten/blender-splitser/**`, matrix 4.2.23 en 5.3.0 |
| Click Joints Pro: 3D cursor, scharnier met eindstop of kogel, bereik in graden | gekeurde Pro-tekst in `README.md` van deze map ("Split with anything. Make it move.") |

Bewust niet: "AI models" (niet getest op AI-modellen in deze versie), "lays parts flat", "snap", "magnets", "click" als belofte over de print, "first time right".
