# Keuring winkeltekst Click Cuts, 24 nov 2026, keurder (agent van de hoofdchat)
Wat ik keurde: `platformen/blender/superhive/click-cuts-winkeltekst.md` (commit f63f4ba, Chris). Opdracht: `berichten/chris.md`, hoofdchat kwartier 24 nov ±04:25 en ±06:25.
Akkoord: nee (één moet-punt, klein: de bundel botst met de Cyber-korting op Pro; de tekst voor de koper zelf is goed)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Elke regel in "Wat het doet" klopt met de code van 1.0.0: knop "Split to fit" (`in_een_klik.py`: dichtmaken alleen als nodig, sneden plannen, splitsen, controle), 9 printers plus "Custom size" (`printers.py`), passingproef met 4 spelingen die per printer en materiaal bewaard wordt (`passing.py` `spelingen()`, `passingproef.py`), controle groen/oranje/rood met reden en wand rond de gaten (`controle.py`), vrije snede (`vrije_snede.py`), Make watertight op een kopie met grens 3000 voxels (`gesloten.py`), export STL of 3MF in mm (`exporteer.py`), Convert to mm (`schaal.py`), Blender 4.2 en nieuwer (`blender_manifest.toml`). Niets beloofd wat er niet is; alleen pennen. | feit | hoog | |
| 2 | "a number on every cut face" klopt: "Engrave numbers" staat standaard aan (`eigenschappen.py`, default=True). | feit | hoog | |
| 3 | De waarschuwing in de tekst ("orange" is nog geel in `controle.py`) is verouderd: de bouwer heeft het al opgelost, KLEUREN["oranje"] = (1.0, 0.26, 0.0) (commit 36912d5, Productbouwer run 8). "orange" mag dus in de tekst blijven. | feit | hoog | |
| 4 | Zoekonderbouwing titel klopt in de kern (curl zelf, 24 nov, eerste 12): "split model" #1 Cleave, #2 Bed Fit Splitter, #4 PrintSplitter, #5 CatPin, #7 FigureCut; "split 3d printing" #1 Cleave, #2 SnapSplit, #4 Oryx CAD, #8 FigureCut, #9 PrintSplitter; "printer bed" #1 Bed Fit Splitter, #2 CatPin, daarna geen splitters; "3d print connectors" #1 Cleave, #2 Split It, #3 CatPin. Bed Fit Splitter $19, nu $14.25 (GEZIEN). Kleine onjuistheid: "Wie bovenaan staat heeft 'Split Models' in de titel" klopt niet voor #1: Cleave heeft "Model Split", niet "Split Models". | feit | hoog | |
| 5 | Titel is 85 tekens, niet 84 (`wc -c`). Geen gevolg, wel een verkeerd cijfer. | feit | hoog | |
| 6 | Prijzen kloppen met `concurrentie.md` punt 5 en tabel 2a: Cleave $23 en $28, CatPin $24 en $36, Split $22 en $28, startprijs $19 tot 14 dec, daarna $24. Maar de CatPin-prijzen staan in `concurrentie.md` als DERDEN (keuring 23 nov), niet GEZIEN. En "Supporter met dezelfde functies doen Cleave en CatPin ook" staat nergens onderbouwd. | feit | midden | De pagina's van Cleave en CatPin met curl: wat krijgt een Supporter extra? |
| 7 | Bundelbron Gumroad klopt (curl, help-artikel 339): type "Bundle", eigen producten, eigen prijs, losse waarde doorgestreept, één variant per product, geen bundel in een bundel. Extra uit dezelfde pagina wat de tekst mist: de doorgestreepte waarde is "fixed by the product variants you picked when you built the bundle". | feit | hoog | |
| 8 | Bundelbron Superhive klopt: pagina bestaat, "Products: 7", "Sales: 20+" (curl 24 nov). Wel was die bundel een actie van 4 dagen ("Available from May 20 to May 23"). | feit | hoog | |
| 9 | Click Joints Pro kost op Superhive $12 Personal en $45 Studio (GEZIEN curl 24 nov) en op Gumroad $19 (price_cents 1900, GEZIEN json). Klopt met de tekst. | feit | hoog | |
| 10 | **Bundel botst met de Cyber-korting.** `commercie/blender-click-joints/black-friday.md` punt 1: code CYBER25, 25% op Click Joints Pro op Gumroad tot di 1 dec 23:59, automatisch toegepast. Click Cuts gaat live in de week van ma 30 nov. Op 30 nov en 1 dec is los dan $14,25 + $19 = $33,25, goedkoper dan de bundel van $34. De doorgestreepte waarde ($38 bij de startprijs) wekt dan een verkeerde indruk. De tekst noemt alleen het verschil met $19 tot 14 dec, niet deze botsing. | feit | hoog | Datum van uitgave van Click Cuts, en of CYBER25 ook op de bundel komt. |
| 11 | Rekenfout in een interne zin: "bundel op $29 zetten (21% onder $36)". $29 is 19% onder $36 (21% zou $28,44 zijn). Staat niet in de tekst voor de koper. | feit | hoog | |
| 12 | Engels is goed en vrij van AI-zinnen (geen "unleash", "seamless", "elevate", geen opsomming van bijvoeglijke naamwoorden). Kort, concreet, werkwoorden vooraan. Klein: "Click Cuts cuts" leest iets stroef; Britse spelling ("millimetres", changelog "Colour") terwijl de add-on zelf "millimeters" en "color" zegt (`exporteer.py`, `controle.py`), dus kies één. | feit | midden | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen persoonsgegevens van Thijs (geen account- of partnernummer, geen adres). | feit | hoog | harde regel 2 |
| 2 | Geen concurrentnaam in de titel; titel neemt de titel van Bed Fit Splitter niet letterlijk over. | feit | hoog | opdracht |
| 3 | Geen gedachtestreepjes in de Nederlandse tekst (grep op lange en halve streepjes en op een los streepje tussen spaties: niets). | feit | hoog | harde regel 8 |
| 4 | Bijna alle cijfers hebben GEZIEN/DERDEN. Uitzonderingen: CatPin-prijzen GEZIEN genoemd waar de bron DERDEN zegt (A6); "Sales 20+", "$14,25", "$12/$45" goed gelabeld. Bundelprijs en $9/21% zijn eigen rekensom, mag zonder label. | feit | hoog | harde regel 5 |
| 5 | Status CONCEPT en "plakken doet Thijs", geen prijsbesluit genomen (prijs bij Thijs). Geen geld uitgegeven. | feit | hoog | harde regel 1 en 4 |

## Deel C: zou een koper het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Titel en eerste zin zijn sterk: printer kiezen, één knop, past op het bed, passingproef. Dat laatste heeft geen concurrent; een koper die ooit een te strakke pen printte klikt hierop. | | |
| 2 | Op Superhive staat Cleave er direct naast met "Pegs, Dowel, Rod Channel, Magnets, Ball Joints". Een koper ziet bij ons alleen "pins" en vraagt zich af of dat genoeg is. | Zeg het zelf eerlijk en positief in één regel in de lijst, bijvoorbeeld "Round pins with matching holes, sized from your fit test", zonder toekomstbeloftes. | klein |
| 3 | Er staat geen regel over wat er niet in zit in het Engels; sectie 6 is alleen intern. Kopers van CatPin klagen in reviews over verrassingen. | Een korte FAQ voor de pagina (Does it work on AI or sculpted meshes? Which connectors? Does it lay parts flat? Blender versions?), met de antwoorden uit sectie 6. | klein |
| 4 | Geen plan voor beelden: Cleave verkoopt met een uit elkaar geschoven figuur in felle kleuren plus echte geprinte delen. | Hoofdbeeld: model uit elkaar in kleur per deel (zit in 1.0.0) plus de geprinte passingproef. Hoort bij Daan/Sanne, wel noemen bij de uitgave. | midden |
| 5 | Geen tags of zoekwoorden voor het tagveld van Superhive ("terrain", "cosplay", "bust", "connectors", "printer bed"). | Tags-lijst toevoegen. | klein |
| 6 | De supporter-variant zegt niet wat de koper ervoor terugkrijgt. | Eén regel: "Same features, for people who want to support updates" plus wat updates inhouden (bijv. alle 1.x-updates). | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
- M1 (A10): Bundel en Cyber-korting. Zet in sectie 5 dat de bundel op Gumroad pas na di 1 dec live gaat (of dat CYBER25 ook op de bundel komt), anders is los kopen op 30 nov en 1 dec goedkoper dan de bundel ($33,25 tegen $34).

**Kan**
- K1 (A3): haal de verouderde "Let op: nu geel"-regel weg; oranje is al opgelost (36912d5).
- K2 (A5, A4, A11): titel is 85 tekens; Cleave heeft "Model Split" niet "Split Models"; $29 is 19% onder $36.
- K3 (A6, B4): CatPin-prijzen DERDEN noemen; zin over Supporter van Cleave en CatPin onderbouwen of weghalen.
- K4 (A7): noteer dat de doorgestreepte waarde op Gumroad vastligt op het moment van bouwen; na 14 dec de bundel opnieuw opslaan of nakijken dat $43 getoond wordt.
- K5 (C2, C3, C5, C6): regel over pennen, korte Engelse FAQ, tags, wat Supporter is.
- K6 (A12): één spelling kiezen, Brits of Amerikaans, en die ook in de changelog aanhouden.

## Herkeuring, 24 nov 2026 (commit 478962d)
Akkoord: ja

| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| 1 | M1 opgelost: sectie 5 punt 0 zet de bundel op Gumroad pas op wo 2 dec live, na het einde van CYBER25 (di 1 dec), met de rekensom $33,25 tegen $34. Click Cuts zelf mag in de week van 30 nov. | feit | hoog |
| 2 | Pennenregel waar: pennen zijn rond (cilinder met afschuining, `vormen.py`), de speling komt uit de instelling of de passingproef, en de pennen zijn een losse pennenplaat die apart wordt geëxporteerd (`exporteer.py`, "every piece and every pin plate"). | feit | hoog |
| 3 | FAQ waar voor 1.0.0: alleen pennen; Make watertight is een voxelkopie die bij een te groot model weigert (`gesloten.py`, grens 3000 voxels), dus "may need to be cleaned first" is eerlijk; delen worden niet vanzelf plat gelegd; Blender 4.2 en nieuwer, getest in 4.2 en 5.3 (CHANGELOG). | feit | hoog |
| 4 | Supporter-zin klopt met de varianten (zelfde add-on). De GOK over Supporter bij Cleave en CatPin staat nu als GOK. | feit | hoog |
| 5 | K1, K2, K3, K6 verwerkt (oranje, 85 tekens, "Model Split", 19%, CatPin DERDEN, Amerikaanse spelling). | feit | hoog |

**Kan (blokkeert niet):**
- K7: "yet" in de FAQ ("No dovetails, magnets or snap keys yet", "Not automatically yet") en "fund faster updates" klinken als een belofte voor later. Liever zonder "yet" en "Pick Supporter if you want to support updates", tenzij het plan er echt is.

## Tweede keuring, 24 nov 2026 ±07:00 NL, keurder winkeltekst (los van de keurder hierboven)
Wat ik keurde: `click-cuts-winkeltekst.md` op 28c002e (na M1 en K7) en de aanvulling `click-cuts-winkeltekst-lang.md` (4e0c396), tegen de code in `producten/blender-splitser/split_joints/` en de opdracht in `berichten/chris.md` (04:25, 06:25 bundel, 06:34 printtitels). Ik kon zelf niet curlen naar superhivemarket.com en gumroad.com (proxy 403, GEZIEN 24 nov ±06:50 NL); zoekuitslagen en winkelprijzen toets ik dus op samenhang met de repo, niet bij de bron.
Akkoord: **nee** (twee moet-punten, allebei klein). Dit staat tegenover de herkeuring hierboven; de reden staat bij A3 en A6.

### Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Titel heeft de vier zoekwoorden (split, for 3D Printing, Printer Bed, Connectors), geen "Blender", geen concurrentnaam. Goed. | feit | hoog | plek op die zoekwoorden in de eerste week na live |
| A2 | Lijst "Wat het doet" en de FAQ kloppen met de code: Split to fit (`in_een_klik.py`), 9 printers plus Custom en marge 2 mm (`printers.py`, `eigenschappen.py`), passingproef 4 spelingen per 0,05 mm, bewaard per printer en materiaal (`passing.py`, `passingproef.py`), groen/oranje/rood met reden, oranje echt oranje sinds 36912d5 (`controle.py`), vrije snede met pennen en nummers (`vrije_snede.py`), dichtmaken op een kopie, grens 3000 voxels (`gesloten.py`), STL/3MF in mm, Convert to mm, Blender 4.2+ (`blender_manifest.toml`), e2e op 4.2.23 en 5.3.0 bij elke push (laatste afgeronde runs dea21a9 en 174ff08 groen, GEZIEN via de GitHub-API). | feit | hoog | |
| A3 | **"with pins, pin holes and a number on every cut face"** (eerste zin) belooft te veel. Een vlak dat te klein of te dun is krijgt geen pen: de add-on meldt dan "too small for a pin ... Glue this joint" (`verbinders.py` r. 97 tot 99, `verbind_3d.py` r. 152; bij de vaas 16 van 28 naden zonder pen, `ontwerp.md` deel 8). Een vlak zonder ruimte krijgt geen nummer ("no room for the number on a part of this face", `verbind_3d.py` r. 168). Punt A2 van de eerste keuring keek alleen naar de standaardwaarde van "Engrave numbers", niet naar deze paden. De FAQ noemt dunne of holle wanden niet. De lange versie wel ("Good to know"). | feit | hoog | een holle vaas splitsen en de meldingen lezen |
| A4 | "fits your bed": een stuk past als het in een van de standen per 90 graden in het bed past (`printers.past`); plat leggen doet de koper. De FAQ zegt dat nu. Goed. | feit | hoog | |
| A5 | Varianten kloppen met de opdracht: Standard $19 tot en met 14 dec, daarna $24; Supporter $29, zelfde add-on. | feit | hoog | |
| A6 | **Bundel op Superhive is nog niet besloten en de som mist de startweken.** Pro kost op Superhive $12 (GEZIEN door Chris en de eerste keurder). Los daar is dan $12 + $19 = **$31** tot en met 14 dec (de bundel van $34 is dan **duurder dan los**) en $12 + $24 = $36 daarna (de bundel scheelt dan $2). De tekst noemt alleen $36 en laat de keuze open ("Keuze bij de hoofdchat"), terwijl de zin "for $34" bedoeld is "voor op beide pagina's". Wie plakt, zet hem dan ook op Superhive. | feit (rekensom) | hoog | prijs van Pro op Superhive op de dag van instellen |
| A7 | Bundel op Gumroad is zinvol en goed geregeld: live op wo 2 dec na CYBER25, $38 tegen $34 tot 14 dec, $43 tegen $34 daarna (21%). Rekent op Pro $19 op Gumroad (GEZIEN door de eerste keurder, json); niet door mij gezien. | feit | midden | |
| A8 | Lange versie, extra beloften: 1 tot 4 pennen per eiland, kleinere pen tot 3 mm, losse pennen met afschuining, één exportbestand per pendikte, "3-5"-nummer, buren nooit dezelfde kleur, N-paneel tab Click Cuts. Klopt. Maar ook hier "a number on every cut face" en "every part of your model fits the bed, with pins ... on each cut face" (excerpt), zelfde punt als A3. "also in your next file" klopt alleen als Blender de voorkeuren bewaart (`passingproef.schrijf_json` zet `is_dirty`; standaard aan). | feit | hoog | |
| A9 | Printtitels (06:34): de korte post in de lange versie volgt het, als CONCEPT voor de Maker van Roep. Goed. | feit | hoog | |

### Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Tijden kloppen niet: "±14:45 NL" en "curl ... ±14:30 NL" bij Chris, "±15:20" in zijn bericht, "±15:00" in de lange versie, terwijl commit f63f4ba van 06:44 NL is en het nu ±07:00 NL is. Een GEZIEN met een tijd die nog niet geweest is, is niet na te gaan. Vermoedelijk een klokfout, geen verzinsel. | feit | hoog | eerlijk (GEZIEN herleidbaar) |
| B2 | Geen persoonsgegevens, geen concurrentnaam in de Engelse tekst, geen gedachtestreepjes, CONCEPT en prijs bij Thijs. | feit | hoog | regels 1, 2, 5, 8 |

### Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | De leidende tekst zegt niet waar de knop staat. | "Where to find it: sidebar (N), tab Click Cuts" uit de lange versie | klein |
| C2 | Op Superhive ziet een koper alleen korting als de basisprijs $24 is met een sale naar $19 (doorgestreept). Een vaste $19 die later $24 wordt, toont geen korting. | basis $24, lanceerkorting naar $19 tot en met 14 dec | klein |
| C3 | De titel lijkt sterk op die van Bed Fit Splitter ("Split Models ... to Fit Your Printer Bed"). Kan als kloon lezen. | alleen aanpassen als de zoekwoorden blijven | klein |
| C4 | "Keywords: ..." als blok in de lange versie leest als zoekwoordvulling. | in de tags zetten, niet in de tekst | klein |

### Moet (blokkeert akkoord)
- **M1 (A6):** zet één besluit voor Superhive in de tekst: **geen bundel op Superhive bij de uitgave** zolang Pro daar $12 kost; de zin "for $34" alleen op de Gumroad-pagina's. Wil je toch een Superhive-bundel, dan pas na 14 dec en onder de losse som (bijvoorbeeld $29). Plus: wie de bundel instelt, kijkt die dag de prijs van Pro in beide winkels na. Waarom geld: een bundel die duurder is dan los verkoopt niets en kost vertrouwen.
- **M2 (A3, A8):** niet "a number on every cut face" beloven; bijvoorbeeld "with pins, pin holes and part numbers on the cut faces". En één FAQ-regel: "*Thin or hollow models?* Some joints have no room for a pin; Click Cuts tells you which ones to glue." Zelfde in het excerpt van de lange versie als die gebruikt wordt.

### Kan (mag later)
- K1 (B1): juiste tijden bij de GEZIEN-metingen en in de berichten.
- K2 (C1 tot C4): Where to find it, $24 met lanceerkorting, titel minder als Bed Fit Splitter, Keywords als tags.
- K3 (A8): "also in your next file" alleen met "as long as Blender saves your preferences", of weglaten.
- K4: wie de eerste week kan curlen, meet de plek op "split model", "3d printing", "printer bed", "connectors".

## Derde keuring, 24 nov 2026, 09:46 NL, keurder winkeltekst (los, herkeuring van M1 en M2 uit de tweede keuring)
Wat ik keurde: `platformen/blender/superhive/click-cuts-winkeltekst.md` op 579eae5 (diff tegen 28c002e), tegen de tweede keuring hierboven, `producten/blender-splitser/ontwerp.md` deel 14, `ontwerp/keuringen/2026-11-24-click-cuts-snelheid-daan.md`, en de code in `split_joints/` (`paneel.py`, `verbinders.py`, `verbind_3d.py`, `splitsen.py`, `in_een_klik.py`). Geen curl nodig: alle nieuwe zinnen gaan over onze eigen code en metingen.
Akkoord: **ja** voor `click-cuts-winkeltekst.md` (geen moet-punten meer). Let op: de lange versie `click-cuts-winkeltekst-lang.md` is hiermee **niet** goedgekeurd om te plakken (zie A6).

### Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | **M1 opgelost.** Deel 5 zegt "Alleen op Gumroad", de zin "for $34" staat er als "alleen voor de Gumroad-pagina's (niet op Superhive)", punt 2 zegt "Geen bundel op Superhive bij de uitgave" met de som $12 + $19 = $31, en punt 3 zegt dat wie de bundel instelt die dag de prijs van Pro in beide winkels nakijkt. Precies wat M1 vroeg. | feit | hoog | |
| A2 | **M2 opgelost.** Eerste zin nu "with pins, pin holes and part numbers on the cut faces": belooft niet meer elk vlak. FAQ-regel "*Thin or hollow models?* Some joints have no room for a pin; Click Cuts tells you which ones to glue." staat er letterlijk. | feit | hoog | |
| A3 | **FAQ dunne vlakken klopt met de code.** Geen pen past: `verbinders.py` r. 97 tot 99 geeft "too small for a pin ... Glue this joint"; te dun stuk: `verbind_3d.py` r. 151 tot 153 "piece only ... mm thick here ... Glue this joint". Elke melding begint met de naam van de snede (`{naam}:`), komt via `splitsen.py` r. 331 in `inst.meldingen` en staat in het paneel (`paneel.py` r. 144 tot 147); de knop meldt "N notes in the panel" (`splitsen.py` r. 343). Twee kleine randjes: het paneel toont **hoogstens 8** meldingen (`[:8]`), en ze staan onder het ingeklapte "More settings". Bij de vaas uit `ontwerp.md` deel 8 (16 van 28 naden zonder pen) ziet de koper dus maar 8 namen. Geen moet voor de tekst: de zin is waar voor de meeste modellen; het is een punt voor de bouwer (K1). | feit | hoog | een holle vaas splitsen en de meldingen in het paneel tellen |
| A4 | **Snelheidszin klopt met de meting.** "Tested on a 1 million face scan in Blender 5.3: about 40 seconds (2-core test machine)": deel 14 meet 1,01M vlakken, Blender 5.3.0, 2 kernen, 42,3 s na de versnelling, 8 stukken groen (GEZIEN door de bouwer). "about 40" is eerlijk afgerond. Het model is de ScatteringSkull-scan, met voxel remesh op 1M gebracht: "scan" mag. Daan M1 (versie noemen) is gedaan. | feit | hoog | |
| A5 | **"Big models show a note under Split to fit"** klopt: `in_een_klik.zwaar_tekst` vanaf 1M vlakken, getekend direct onder de knop in `paneel.py` als er nog geen uitslag is. Wel zegt die regel "can take a few minutes", terwijl de FAQ 40 seconden noemt (Daan B3 en K2). Niet fout (te ruim, niet te krap), wel twee verhalen. | feit | hoog | |
| A6 | **"Where to find it: press N in the 3D viewport and open the Click Cuts tab"** klopt: `paneel.py` r. 20 tot 24, `bl_space_type = "VIEW_3D"`, `bl_region_type = "UI"` (de zijbalk onder N), `bl_category = "Click Cuts"`, geen `poll` die het paneel verbergt. | feit | hoog | |
| A7 | **De lange versie heeft M2 nog niet.** `click-cuts-winkeltekst-lang.md` r. 31 ("a number on each cut face"), r. 39 ("a number on every cut face") en r. 111 ("a number on each cut face") beloven nog elk vlak. Die regels staan niet in 579eae5 en Chris is niet de schrijver; de lange versie zegt zelf dat de tekst van Chris leidend is. Dus geen blokkade voor deze keuring, wel: niets uit de lange versie plakken voor die drie regels zijn aangepast (K2). | feit | hoog | |
| A8 | Nieuwe FAQ "*Does it work with Click Joints Pro?* Yes, side by side." Beide add-ons hebben een eigen tab en eigen namen (`split_joints` tegenover Pro); niet zelf samen geïnstalleerd getest. | vermoeden | midden | beide add-ons tegelijk aanzetten in 4.2 en 5.3 |
| A9 | Prijs nu "basisprijs $24, lanceerkorting naar $19 tot en met 14 dec": de kan-punt C2 uit de tweede keuring is verwerkt. De bundelsom op Gumroad ($19 + $24 = $43, $9 minder) klopt. | feit | hoog | |

### Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | **De GOK "In Blender 4.2 it takes about twice as long" mag in de winkel blijven.** Reden: het is geen los verzonnen getal. Daan zag in de CI-logs op hetzelfde soort werk (Suzanne, 0,5M vlakken) 4.2 21,1 s tegen 5.3 11,5 s, dus 1,8 keer (GEZIEN, Daan B1). Alleen de 1M-maat in 4.2 is afgeleid. Bovendien is het een waarschuwing in ons nadeel: de koper verwacht eerder te traag dan te snel. Daan vroeg deze zin zelf (zijn M1). Voorwaarde: de bronregel onder de FAQ noemt het nu "nog GOK"; schrijf daar bij dat het rust op de gemeten 1,8 keer bij 0,5M (Daan B1), zodat het herleidbaar is. Komt de 1M-meting in 4.2 (Daan K1) voor het plakken, dan het getal daaraan aanpassen. Komt die op meer dan 2,5 keer uit, dan de zin aanpassen voor het plakken. | feit + oordeel | hoog | eerlijk (GEZIEN, DERDEN, GOK) |
| B2 | Andere cijfers: 9 printers, 4.2 en 5.3, $24, $19, $29, $34, $43, $12, $31, $36 hebben allemaal een bron in de tekst of de vorige keuringen. De tijden bovenaan zijn rechtgezet (K1 tweede keuring). | feit | hoog | eerlijk |
| B3 | Geen persoonsgegevens, geen concurrentnaam in de Engelse tekst, geen gedachtestreepjes, CONCEPT, prijs bij Thijs. | feit | hoog | regels 1, 2, 5, 8 |

### Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | "Where to find it" staat nu tussen twee lijstjes, tussen "Blender 4.2 and newer" en "Connectors in 1.0.0 are pins". Leest als losse regel midden in de lijst. | "Where to find it" onder de lijst zetten, na de pennenregel | klein |
| C2 | "Tested in Blender 4.2 and 5.3 on every change" staat twee keer (lijst en FAQ). | in de FAQ alleen "4.2 and newer" | klein |
| C3 | Een koper met een holle vaas leest "tells you which ones to glue" en ziet 8 namen van de 16. | in de code "and N more" of alle meldingen; tekst kan blijven | klein |

### Moet (blokkeert akkoord)
Geen.

### Kan (mag later)
- K1 (A3, C3, voor de bouwer): het paneel toont nu hoogstens 8 meldingen en verbergt ze onder More settings; laat "and N more" zien of toon de lijm-meldingen ook bij de uitslag bovenaan.
- K2 (A7): in `click-cuts-winkeltekst-lang.md` r. 31, 39 en 111 dezelfde fix als M2 ("part numbers on the cut faces") voordat iets uit die versie geplakt wordt.
- K3 (B1): bronregel onder de FAQ aanvullen met "rust op 1,8 keer gemeten bij 0,5M (Daan B1)"; na Daan K1 het 4.2-getal vervangen door de meting.
- K4 (A5): paneelregel "can take a few minutes" laten passen bij de FAQ, bijvoorbeeld "can take a minute or more" vanaf 1M (Daan K2).
- K5 (A8): één keer Click Cuts en Click Joints Pro samen aanzetten in 4.2 en 5.3 voor de FAQ-regel "side by side" GEZIEN is.
- K6: kleine opruiming in deel 5: "Twee dingen om op te letten" telt nu vier punten (0 tot 3), en de regel "Kan het daar niet, dan alleen Gumroad" is overbodig nu het besluit al "alleen Gumroad" is. C1 en C2 hierboven.
