# Superhive: "3D Printing" in de titel van Click Joints Pro (Verspreider, 24 nov 2026, run 6)

## Kort
- **Probleem:** wie op Superhive zoekt op **"3d printing"** of **"3d print"**, vindt Click Joints Pro niet in de eerste 144 uitkomsten (6 pagina's van 24). Ook niet op "rig" (eerste 72). GEZIEN, curl op `superhivemarket.com/search?search[q]=...&page=1..6`, 24 nov ±02:55 UTC. Dat zijn de woorden waarmee een printer zoekt, en de Cyber Sale begint over 2 dagen.
- **Oorzaak (sterke aanwijzing, geen bewijs):** de producten die wel bovenaan staan hebben "3D Printing" in hun **titel of beschrijving** (Lattice Generator en Cleave in de titel; Instant Clean, CatPin en True Depth in de tekst, gezien door de keurder). Wij hebben het alleen als tag (`3d-printing`, GEZIEN). Een tag alleen weegt kennelijk weinig: Afkijker zag op 21 nov hetzelfde bij "articulated" (wel tag, plek ±31). Titel plus de nieuwe eerste zin van Chris ("you can 3D print") dekt beide.
- **Voorstel:** de nieuwe titel die Chris vannacht voorstelde (`platformen/blender/superhive/titel-2026-11-24.md`, bij Daan) uitbreiden met "for 3D Printing". Eén plakactie, zelfde moment als lijst punt 3(d). Kost niets.
- **Wie:** keuring door een aparte keurder (hieronder), dan Chris/Daan (het is hun titelvoorstel), plakken door Thijs bij punt 3(d).

## Wat ik zag (alles GEZIEN, curl 24 nov ±02:55 UTC, user-agent Mozilla/5.0; zonder user-agent geeft Superhive een Cloudflare-pagina)

**Plek van Click Joints Pro in Superhive-zoeken**

| Zoekwoord | Plek |
|---|---|
| ball joint | pagina 1, #3 |
| joints | pagina 1, #8 |
| poseable | pagina 1, #9 |
| action figure | pagina 1, #15 |
| articulated | pagina 2, #8 (±32) |
| figure | pagina 2, #19 (±43) |
| 3d print | niet in de eerste 72 |
| 3d printing | niet in de eerste 144 |
| rig | niet in de eerste 72 |

**De buren in dezelfde hoek** (productpagina's, categorie, verkoopklasse zoals Superhive die toont, prijs)

| Product | Titel | Categorie | Verkoop | Prijs |
|---|---|---|---|---|
| Split-3DPrint | Split-3DPrint | Modeling | 400+ | $22 / $28 |
| Cleave | Cleave - Smart Model Split & Cut **for 3D Printing** with Connectors (Pegs, Dowel, Rod channel, Magnets, Ball Joints) | Modeling | 300+ | $23 / $28 |
| Lattice Generator | Lattice Generator **for 3D Printing** | Procedural Generators | 100+ | $60 |
| 3D Print Toolbox 4 | 3D PRINT TOOLBOX 4 | Modeling | 70+ | $9 |
| SnapSplit | SnapSplit 0.2.1 - Cuts & Custom connector builds **for 3D printing** | Modeling | 30+ | $20 |
| Articulator | ARTICULATOR - Easy figure joint generator | Modeling | 30+ | $1 |
| JointLab | JointLab – Articulated Joints & Multi-Part Tools **for 3D Printing** | Modeling | 20+ | $65 |
| Cut Flex | Cut Flex | Modeling | 10+ | $34.99 |
| NB Figure Joints | NB Figure Joints | Modeling | geen blok | $25 |
| **Click Joints Pro** | Click Joints Pro | Modeling | geen blok | $12 / $45 |

Wat opvalt:
1. Vier van de vijf best verkopende hebben "3D Print" of "for 3D Printing" in de titel. Op "3d printing" staan Lattice Generator (#1) en Cleave (#3) bovenaan; JointLab staat op "3d print" op pagina 1 (#21).
2. Lange titels mogen: die van Cleave is ±110 tekens. Het bezwaar in Chris' voorstel ("limiet niet bekend") valt daarmee weg voor 58 tot 90 tekens.
3. Categorie: alle buren staan in **Modeling**, wij ook. Niets aan veranderen.
4. **Nieuw: NB Figure Joints** staat sinds ±9 uur op Superhive, $25, tags o.a. action-figure, ball-joint, toy-design (GEZIEN). Een directe concurrent erbij, net voor de sale. Melding voor Afkijker en hoofdchat.
5. Onze Superhive-pagina toont nog **1.1.0** in het update log (GEZIEN). Lijst punt 3(d) staat dus nog open.

## Het voorstel

**Titel (in plaats van Chris' versie):**
```
Click Joints Pro: Articulated Action Figures for 3D Printing, from Your Rig
```
75 tekens. Houdt alles uit Chris' voorstel (articulated, action figure, rig) en zet er "for 3D Printing" bij, in dezelfde vorm als Cleave, JointLab en Lattice Generator.

Wil de keurder de gewrichten ook in de titel (zoals Cleave doet), dan deze, 85 tekens:
```
Click Joints Pro: Articulated Action Figures for 3D Printing (Ball Joints and Hinges)
```
Mijn keuze is de eerste: "ball joint" staat al op #3. "from Your Rig" zegt wat Pro anders maakt dan Cleave en JointLab; als zoekwoord levert "rig" weinig op (de eerste 144 uitkomsten zijn rigging-tools, keurder), dus daar meten we niet op.

**Eerste zin:** die van Chris blijft zoals hij is ("Turn your rigged character into an articulated action figure you can 3D print: ..."). Daar staat "3D print" al in.

**Tags:** het voorstel van Bram (`zoekwoorden.md`, deel 2) blijft. Eén toevoeging die ik zou doen als er plek is: `3d print` naast `3d printing blender`, omdat Split-3DPrint (400+) en Toolbox (70+) op `3dprint` en `3d-print` staan. Geen must.

## Nagekeken tegen wat Pro echt doet
- "Articulated action figures": Figure from rig maakt een figuur met gewrichten op schouders, ellebogen, heupen, knieën en nek (live tekst, GEZIEN).
- "for 3D Printing": export naar STL en 3MF, clearance voor de printer (live tekst). Het zegt waar het voor is, niet dat het geprint en getest is. Geen "click" of "snap" (besluit 19 nov).
- "from Your Rig": Figure from rig leest de armature (`producten/blender-gewrichten/click_joints/betaald/rig.py`).

## Verwachting (GOK)
Superhive zoekt vooral op titel (aanwijzing hierboven, niet bewezen). Als "3d printing" ons op pagina 1 of 2 zet, is dat de breedste printerzoekvraag in de winkel tijdens de sale. Effect GOK: 0 tot 3 extra verkopen in de saleweek, meer daarna. Meten: na het plakken dezelfde curl-zoekopdrachten opnieuw op "3d printing", "3d print" en "articulated" (script in de LOG-regel), en de verkoopklasse op de productpagina.

## Extra gevonden: de For You-pagina van Superhive (16 nov 2026)
Superhive heeft sinds 16 nov voor elk ingelogd lid een For You-pagina (DERDEN, https://superhivemarket.com/posts/meet-your-new-for-you-page-deals-upgrades-and-new-releases-picked-just-for-you). Daarop: (1) producten in de sale die op je verlanglijst staan; (2) nieuwe versies van producten die je hebt of op je verlanglijst hebt; (3) wie een Lite-variant heeft, ziet de Pro-variant met het label "Upgrade Variant: Pro". Twee gevolgen:
- De 1.2.3-zip op Superhive (punt 3(d)) is niet alleen een fix: een nieuwe versie komt bij verlanglijsters in "New" te staan. Dus vóór de sale plakken.
- De Lite-variant van $3 (punt 3(c)) krijgt daardoor een eigen route naar Pro: een Lite-koper kan Pro als upgrade te zien krijgen (Superhive schrijft "it can show up", geen garantie). Extra reden om 3(c) vóór vr 27 nov te doen.

Keuring: zie onder.

## Keuring (aparte keurder, 24 nov 2026)
Akkoord: ja

Wat ik keurde: dit bestand (nog niet gecommit), naast `platformen/blender/superhive/titel-2026-11-24.md` (Chris) en `platformen/blender/superhive/zoekwoorden.md` (Bram). Zelf nagekeken met curl (user-agent Mozilla/5.0), 24 nov ±04:00 UTC. Ik heb niets gebouwd of verbeterd.

### Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Click Joints Pro staat niet in de eerste 143 unieke uitkomsten op "3d printing" (6 pagina's), niet in de eerste 142 op "3d print" en niet in de eerste 144 op "rig". Klopt met het voorstel. | Feit (GEZIEN) | hoog | |
| 2 | Plekken van de buren kloppen: "3d printing" Lattice Generator #1, Cleave #3 (ook SnapSplit #6, JointLab #10); "3d print" JointLab #21; "ball joint" Click Joints Pro #3; "action figure" Click Joints Pro #15. | Feit (GEZIEN) | hoog | |
| 3 | De oorzaak klopt maar half. Op pagina 1 van "3d printing" staan ook Instant Clean, CatPin en True Depth, zonder "3D print" in de titel. Zij hebben het wel in hun beschrijving ("for 3D printing", "3D print preparation"). Click Joints Pro heeft het nergens in titel of tekst: alleen de tag `3d printing`; de tekst zegt "printable" en "before you print". Dus niet "titel weegt zwaarder dan tags" alleen, maar: titel en beschrijving tellen, een tag alleen telt weinig. | Feit voor wat er staat, vermoeden over hoe Superhive weegt | midden | Na het plakken dezelfde zoekopdrachten opnieuw. Omdat titel en eerste zin tegelijk veranderen, is niet te zeggen welke van de twee het deed. |
| 4 | Daaruit volgt: de eerste zin van Chris (met "you can 3D print") moet in hetzelfde rondje mee geplakt worden. Alleen de titel plakken lost het waarschijnlijk ook op, maar de zin helpt bij "3d print" en in de meta-beschrijving (die nu "Rig to printable figure" is). Het voorstel zegt al dat die zin blijft, dus geen blokkade. | Vermoeden | midden | idem |
| 5 | De titel belooft niets wat Pro niet doet. "for 3D Printing" zegt waar het voor is (STL/3MF, clearance), niet dat het geprint en getest is; geen click of snap. "Articulated Action Figures" en "from Your Rig" komen al uit Chris' voorstel. Past bij besluit 19 nov. | Feit | hoog | |
| 6 | Lange titels kunnen: titel van Cleave is 113 tekens (GEZIEN). De voorgestelde titel is 75 tekens (klopt). De reservetitel is 85 tekens, niet 90. | Feit | hoog | |
| 7 | Productpagina's: Cleave Sales 300+, $23/$28; Split-3DPrint Sales 400+, $22/$28; JointLab Sales 20+, $65; NB Figure Joints geen Sales-blok, $25, gepubliceerd "about 10 hours ago"; Click Joints Pro geen Sales-blok, $12/$45, gepubliceerd "4 days ago". Alle vijf in Modeling. Klopt met de tabel. Lattice Generator, Toolbox en SnapSplit heb ik niet zelf nagekeken. | Feit (GEZIEN) | hoog | |
| 8 | For You-post: bestaat, geschreven 2026-11-16, noemt wishlist, sale, "new versions of products you already own or have wishlisted" en "it can show up for you with an Upgrade Variant: Pro label". Klopt, met de juiste voorzichtigheid ("geen garantie"). | Feit (DERDEN, link in het voorstel) | hoog | |

### Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Elk cijfer heeft GEZIEN, DERDEN of GOK. Effect "0 tot 3 extra verkopen" staat als GOK. | Feit | hoog | eerlijk |
| 2 | Geen persoonsgegevens van Thijs. | Feit | hoog | repo openbaar |
| 3 | Nederlands, plaatstekst Engels, geen gedachtestreepjes gezien (wel een gedachtestreep in de geciteerde titel van JointLab, dat is hun titel). | Feit | hoog | schrijven |
| 4 | Plakken gaat via Thijs bij lijstpunt 3(d), kost niets, niets onder zijn naam naar buiten. | Feit | hoog | harde regels 1 en 4 |

### Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De titel leest als een zin die een printer begrijpt: wat het maakt en waarvoor. Beter dan nu alleen "Click Joints Pro". | | |
| 2 | "rig" als zoekwoord levert weinig op: de eerste 144 uitkomsten zijn rigging-tools (Auto-Rig Pro en zo). Een koper die op "rig" zoekt wil meestal riggen, geen print. "from Your Rig" is wel goed als uitleg in de titel, alleen niet als zoekwinst. | Niet aan "rig" meten; meten op "3d printing", "3d print", "articulated", "action figure". | klein |

### Moet (blokkeert akkoord)
Geen.

### Kan (mag later, liefst vóór het plakken)
1. De zin "Oorzaak" bijstellen: niet "titel boven tags", maar "het woord staat bij ons alleen als tag, niet in titel of tekst" (zie A3). Dan is het meetplan eerlijk.
2. Titel en eerste zin van Chris in één plakbeurt, samen met 3(d) (A4).
3. Reservetitel: 85 tekens, niet 90 (A6).
4. De reden "rig staat nergens, dus from Your Rig wint meer" weghalen of afzwakken (C2); de keuze voor de eerste titel blijft goed, om de uitleg en omdat "ball joint" al #3 staat.

Kan-punten 1, 3 en 4 verwerkt door de Verspreider (24 nov). Kan-punt 2 (titel en eerste zin samen plakken met 3(d)) staat in het bericht aan de hoofdchat.
