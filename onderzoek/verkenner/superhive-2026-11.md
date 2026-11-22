# Superhive: wat verkoopt er echt aan add-ons (opdracht hoofdchat 15 nov 20:20)

Vera, verkenner. Deadline wo 18 nov 18:00. **Stand: af, run 15 nov 22:31 (Amsterdam), nagekeken door een controleur.** Ruwe data: `data/superhive-addons-6mnd-2026-11-15.csv` (2.355 add-ons, alleen productgegevens). Uitkomst van de analyse: `data/superhive-6mnd-analyse-uitkomst-2026-11-15.txt`.

## In het kort
- **De toppers zijn uitzonderingen.** Van 2.296 betaalde add-ons uit de laatste 6 maanden haalt **80% geen 10 verkopen**, 17% 10 tot 99, 2,7% 100 tot 999 en 0,2% (5 stuks) 1000+.
- Wie 2 tot 6 maanden de tijd krijgt doet het iets beter: 61 tot 79% onder 10, 3 tot 6% 100+.
- **De vloed groeit:** 747 nieuwe add-ons in de laatste maand, tegen ±200 tot 400 per maand daarvoor. Eén printmaker (Hanru Croucamp) bracht er in een maand 36 uit, geen enkele haalt 10.
- **Geld zit bij weinig makers:** de top 10 makers hebben 57% van de omzet (ondergrens), Milad Kambari alleen 14%, en in de jongste maand zelfs 47%.
- Mediane prijs $12. Duurder verkoopt niet slechter: vanaf $15 haalt ±34 tot 44% 10+, onder $10 ±20%.
- **3D-printen** loopt het best per add-on (van 32 betaalde van 2 tot 6 maanden: 34% 10+, 16% 100+), maar wat verkoopt is splitsen met verbinders, en die hoek is nu vol.
- **Advies volgende add-on:** gewichten en skinning herstellen (nummer 1), zachte fysica (2). Schroefdraad en inzetstukken zakt naar plek 5: vorige maand kwamen er ±10 nieuwe bij en geen verkoopt.
- **Click Joints Pro:** $15 is te verdedigen, maar laat de keuring op $12 doorlopen; naast Cleave neerzetten, niet ertegen. Verwachting eerlijk: 0 tot 30 verkopen in 3 maanden (GOK).

## Hoe gemeten
- Workflow `.github/workflows/verkenner-superhive.yml` draaide `data/superhive-6mnd-script.py` in GitHub Actions (run 43753540741, 15 nov 19:38 tot 21:54 UTC): de lijst van alle add-ons op datum (nieuwste eerst), daarna elke productpagina op superhivemarket.com. Rustig: 1 pagina per 2 seconden, alleen openbare pagina's, niet ingelogd. Per add-on: naam, maker, prijs, verkoopblok, ratings, categorie, "Published ... ago", Blender-versie, korte beschrijving.
- Analyse: `data/superhive-6mnd-analyse.py` (python3 -I, CSV als argument).
- **Hoe je het verkoopblok leest (GEZIEN, ook door de controleur):** in de HTML staat `Sales` met `1200+` enzovoort. Superhive toont het pas vanaf 10 verkopen. Geen blok betekent 0 tot 9. Het blok is een ondergrens, dus alle omzet hieronder is een ondergrens. De prijs in de CSV is de kortingsprijs als er korting loopt, dat drukt de omzet nog iets.
- **Leeftijd is grof:** Superhive rondt af. "about 1 month" is 30 tot 45 dagen, "6 months" ±165 tot 195 dagen. "2 tot 6 maanden" in dit stuk is dus ±45 tot 195 dagen. De meting stopt halverwege "7 months" (±6,5 maand terug).
- **Gaten:** 12 add-ons uit de meting van 9 nov ontbreken, hoewel ze nog bestaan (±0,5%). Geen dubbele rijen, geen maand die ontbreekt, de instroom per maand komt overeen met 9 nov.

## 1. Verdeling (GEZIEN, CSV 15 nov)
Betaalde add-ons, 0 tot 6 maanden oud, n=2.296, 845 makers:

| Leeftijd | n | 0 tot 9 | 10 tot 99 | 100 tot 999 | 1000+ |
|---|---|---|---|---|---|
| jonger dan 1 mnd | 744 | 93,3% | 5,9% | 0,7% | 1 |
| ±1 mnd | 267 | 87,3% | 11,2% | 1,5% | 0 |
| 2 mnd | 390 | 79,2% | 17,9% | 2,6% | 1 |
| 3 mnd | 268 | 70,9% | 24,3% | 4,5% | 1 |
| 4 mnd | 213 | 69,5% | 23,9% | 5,6% | 2 |
| 5 mnd | 218 | 69,3% | 26,1% | 4,6% | 0 |
| 6 mnd | 196 | 60,7% | 35,2% | 4,1% | 0 |
| **alles** | **2.296** | **80,3%** | **16,8%** | **2,7%** | **5 (0,2%)** |

- Gratis add-ons zijn zeldzaam op Superhive (19 in 6 maanden).
- Prijs: mediaan $12, kwartielen $7,99 en $19,99.
- Makers met maar 1 add-on in deze 6 maanden (500 van 845) doen het net zo: van hun add-ons van 2 tot 6 maanden haalt 28% 10+ en 6% 100+. Let op: een deel van hen heeft oudere add-ons en dus al een naam (bijvoorbeeld Physical Addons, Jessy Leite, Ingo Clemens).
- Grove omzet, ondergrens: alle 2.296 samen ±$810.000 over 6 maanden, waarvan 57% bij 10 makers. Een gewone nieuwe add-on brengt in zijn eerste maanden $0 tot ±$100 op.

**De vijf met 1000+:** Smart Remesh 2.600+ ($17), Image to 3D 1.200+ in 16 dagen ($18), Auto Unwrap 1.200+ ($18), alle drie Milad Kambari; MotionGen 1.300+ (maar $1); Physical Atmosphere² 1.000+ ($84, Physical Addons, bekende naam). Image to 3D draait plaatselijk open AI-modellen (TRELLIS.2, Hunyuan 2.1, TripoSR), geen betaalde dienst van buiten (beschrijving in de CSV).

## 2. Wat doet het best: prijs, soort, categorie (betaald, 2 tot 6 maanden)

**Prijs** (ondergrens inclusief, door de controleur hersteld):

| Prijs | n | 10+ | 100+ |
|---|---|---|---|
| $0 tot 5 | 178 | 21,9% | 0,6% |
| $5 tot 10 | 343 | 20,4% | 1,2% |
| $10 tot 15 | 236 | 26,7% | 4,7% |
| $15 tot 20 | 182 | 34,1% | 6,0% |
| $20 tot 30 | 187 | 34,2% | 8,6% |
| $30 en meer | 159 | 44,0% | 8,2% |

Samenhang, geen bewijs dat de prijs het doet: goede add-ons vragen ook meer. Maar goedkoop helpt niet.

**Soort** (eigen indeling op titel en beschrijving, eerste treffer telt):

| Soort | n | 10+ | 100+ | mediane prijs | omzet-ondergrens |
|---|---|---|---|---|---|
| 3D-printen | 32 | 34% | 15,6% | $18,50 | $39.000 |
| modelleren | 173 | 36% | 5,8% | $10,50 | $96.000 |
| generator | 346 | 28% | 5,2% | $14,99 | $267.000 |
| animatie en rig | 197 | 35% | 4,6% | $12,99 | $129.000 |
| materialen | 250 | 24% | 3,6% | $10 | $53.000 |
| werkstroom en interface | 111 | 20% | 1,8% | $10 | $12.000 |
| render, licht, camera | 156 | 26% | 1,3% | $10 | $54.000 |

"Generator" bevat Milad Kambari's één-klik-hulpmiddelen; zonder hem is het gemiddeld.

**Superhive-categorie:** rigging het best (99 stuks, 40% 10+, 9,1% 100+), dan modeling (370, 35%, 6,5%). Asset management het slechtst (72, 10%, 1,4%), daarna themes en video.

**Wat de doorbrekers gemeen hebben** (100+ in 2 tot 6 maanden, makers met 1 of 2 add-ons in die tijd): ze doen één vervelende klus in een bekende werkstroom en tonen dat in een filmpje. Voorbeelden: Adaptive Auto Skinning $29,75 900+, CatPin $24 400+, Nitro Retopo $25 300+, Seamless CAD $14,90 300+, BWrap $29,99 200+, PaintBridge Krita $9,59 200+, Sculpt Rewind $14,50 100+, Lens Optics $29 100+, Cleave $23 100+.

## 3. 3D-printen (onze niche met Click Joints)
- 77 betaalde print-add-ons in 6 maanden, 41 makers. Per maand: 36 in de laatste maand, daarvoor 2 tot 12 per maand. **26 van de 77 zijn van Hanru Croucamp** (in totaal 39 add-ons, 36 in de laatste maand, $1 tot $139 met bundels, alle onder 10).
- **Wat verkoopt (2 tot 6 maanden, 11 van 32 haalt 10+, 5 haalt 100+):** Dovetail Key $18 800+ (Milad Kambari), CatPin $24 400+, Split-3DPrint $22 400+, Cleave $23 100+, SDF.R $14,90 100+. Vier van die vijf zijn **splitsen met verbinders**. Daaronder: JointLab $65 20+, MeshSmith $15 20+, Rego Kit Card $24 10+, Oryx CAD $13,49 10+, FormArmorPro $49 10+, ARTICULATOR (figuur met gewrichten, $1) 30+.
- **In de laatste ±45 dagen:** alleen Cut Flex ($34,99) en SPLIT IT! ($8,40) haalden 10+. Vier nieuwe splitsers (FigureCut, Mesh Split, Ninja Cut, Easy Slice) en ±10 add-ons voor schroefdraad, inzetstukken en gaten (Precision Holes & Inserts, Insert & Nut Pocket Maker, Thread Helix, Fastener Generator, Printwright, Knurl & Knob Maker) staan alle onder 10.
- **Gewrichten en print-in-place:** JointLab 20+ voor $65, ARTICULATOR 30+ voor $1, LayerMechanic (controle print-in-place, $25) en Pose to Print ($18) onder 10. Er is vraag, maar klein; de meeste kopers willen eerst knippen.
- **Cleave naast Click Joints Pro (GEZIEN, productpagina 15 nov):** Cleave (V4SS3UR, $23, steunversie $28, 100+, 3 ratings, ±2 maanden) is vooral een splitser met pennen, deuvels, magneetgaten en sinds 1.6 kogelgewrichten, plus 120+ printers, platen inpakken en 3MF. Wat Cleave niet heeft: een bereik in graden, een scharnier met eindstop en een testkaartje voor de speling. Precies wat Click Joints Pro doet.
- **Wat ontbreekt:** een eerlijke passingstest per printer (speling meten en onthouden) die andere add-ons gebruiken; gewrichten met een vast bewegingsbereik voor figuren; mallen om te gieten (geen nieuwe in 6 maanden, oud: Molding Gen 100+, MouldCast Studio 60+). Of dat verkoopt is niet bewezen: kleine printklusjes van $9 tot $19 verkopen nu niet, door de vloed.

## 4. Top 5 ideeën voor de volgende add-on
Lat: een duidelijke klus die snel gaat, te testen in Blender zonder scherm (geometrie en vervorming meten in onze toetsen), bewijs dat zoiets verkoopt, en een reden waarom wij het beter kunnen. Volgorde is herzien met de volle meting. Overal geldt: wij zijn een nieuwe maker zonder naam, dus de onderkant is 0 tot 9 verkopen.

1. **Gewichten en skinning herstellen** (kapotte vervorming bij knieën, ellebogen en schouders opsporen en glad maken, met een rapport per gewricht). Bewijs: van 28 betaalde gewicht-add-ons van 2 tot 6 maanden haalt 13 10+ (46%) en 3 100+: Adaptive Auto Skinning $29,75 900+, Smooth Weights $17,99 400+, RadFit $14,25 100+; Voxel weight transfer (Jessy Leite) 10+ in 7 dagen. Rigging is de best verkopende categorie. Waarom wij: vervorming is zonder scherm te meten (volume en hoek per gewricht in verschillende poses), dat is wat de meeste concurrenten alleen beloven. Gevaar: 20 nieuwe in de laatste maand (Meshwright, Mykola Piatkov, WeightMend), 4 daarvan al 10+. Druk maar met echte kopers. GOK 10 tot 60 verkopen in 6 maanden bij $15 tot $20.
2. **Zachte fysica in één klik** (wiebelen, inveren, botten die nazwaaien). Bewijs: van 11 van 2 tot 6 maanden haalt 6 10+ en 2 100+ (SquishyFX $15 300+, SpringFX $15 100+, beide Aaron Thompson); Flex $64,99 70+, Marrow $26,25 30+. Waarom wij: past bij ons simulatorgereedschap, beweging per frame is te toetsen. Gevaar: Aaron Thompson is sterk en actief (ook ShapeKeyFX); 13 nieuwe in de laatste maand, nog geen 10+. GOK 0 tot 40.
3. **Click Joints Pro uitbreiden in plaats van een nieuwe add-on:** figuur uit een rig in één klik printbaar maken met gewrichten met vast bereik (zoals ARTICULATOR en Pose to Print, maar met eindstop en speling per printer). Bewijs: klein (ARTICULATOR 30+ voor $1, JointLab 20+ voor $65). Waarom: geen nieuwe winkelpagina, gebruikt wat we al hebben, maakt Pro sterker naast Cleave. GOK een paar extra verkopen per maand, geen grote stap.
4. **Printbaar reliëf uit een afbeelding of tekst** (dicht stuk met muurdikte, maximale hoogte en bedmaat). Bewijs: oud en sterk (True Depth $25 6.900+ in ±2 jaar, zForm 1.100+, Bildeform 500+). Nieuw doet niets: 10 nieuwe in 6 maanden, geen 10+ (Hanru's Lithophane Maker, Emboss & Deboss). Lewis Martin (True Depth) is actief. Volgens de harde regel twijfelgeval; alleen als we iets duidelijk beters hebben.
5. **Schroefdraad, inzetstukken en passende gaten met speling per printer.** Bewijs van vraag oud (Precision Gears $24 500+, Precision Bolts $24 200+, beide ±4 jaar), maar in de laatste maand ±10 nieuwe, alle onder 10. Gezakt van 1 naar 5. Alleen zinvol als onderdeel van een groter printpakket.

Afgevallen: nog een splitser (vol, Cleave dekt bijna alles); mallen (klein en geen beweging); één-klik-modelleren en UV (Milad Kambari); kleine printklusjes van $9 tot $15 (Hanru); meerkleuren-3MF (alle onder 10).

## 5. Prijsadvies Click Joints Pro naast Cleave
- **Advies: $15 is beter dan $12, maar haal Pro niet uit de keuring.** In de meting haalt $10 tot $15 na 2 tot 6 maanden 27% 10+ en 4,7% 100+, $15 tot $20 34% en 6,0% (GEZIEN, hersteld). Samenhang, geen bewijs. Voorstel: keuring op $12 laten lopen (ingediend 15 nov 19:36), en na goedkeuring naar $15 als Hans en Bram dat willen. Studio $45 laten staan.
- **Naast Cleave, niet ertegen:** Cleave knipt en verbindt, Click Joints Pro maakt een deel beweegbaar met bereik in graden, een scharnier met eindstop en een testkaartje voor de speling. Zin voor de pagina: "Works on parts from any splitter, including Cleave." Alleen schrijven als het getoetst is op een STL die met een splitser is geknipt.
- **Eerlijk:** Pro valt in de grootste groep: nieuwe maker zonder naam in een volle hoek. GOK 0 tot 30 verkopen in de eerste 3 maanden. De gratis Click Joints (138 downloads op 15 nov) is de beste weg naar kopers: zet in de gratis versie een duidelijke verwijzing naar Pro.
- Beslissing over prijs en volgende add-on ligt bij Hans en Bram; dit is advies.

## Controle
Controleur (agent, 15 nov 22:10 UTC): 12 willekeurige rijen live op superhivemarket.com nagekeken, alle 12 goed (verkoopblok, ratings, maker, datum; twee prijzen zijn kortingsprijs, goed in de CSV). Verdeling en mediane prijs zelf herrekend, gelijk. Gecorrigeerd: prijsklassen (prijzen van precies $5, $10, $15 vielen in de klasse eronder, nu hersteld in het script), aandeel top 10 (57%, niet 56%), Milad in de jongste maand (47%, niet 42%), Hanru (36 in de laatste maand, niet 24), schroefdraad (±10 nieuwe, niet 24), afronding van leeftijden en de 0,5% die ontbreekt staan nu in de tekst.
