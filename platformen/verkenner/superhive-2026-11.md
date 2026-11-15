# Superhive: wat verkoopt er echt aan add-ons (opdracht hoofdchat 15 nov 20:20)

Vera, verkenner. Uiterlijk wo 18 nov 18:00. **Stand: tweede tussenstand, run 15 nov 21:31.** De meting in GitHub Actions (run 43753540741) loopt nog: om 21:23 (Amsterdam) 820 van ±2.589 add-ons binnen, klaar rond 23:00. De top 5 en het prijsadvies hieronder zijn voorlopig, op de meting van 9 nov plus de eerste 820; de volgende run na 23:00 rekent ze na met de volle CSV en laat een controleur kijken.

## Hoe gemeten
- Workflow `.github/workflows/verkenner-superhive.yml` draait `data/superhive-6mnd-script.py`: de lijst van alle add-ons op datum (nieuwste eerst), daarna elke productpagina. Rustig: 1 pagina per 2 seconden, alleen openbare pagina's, niet ingelogd. Per add-on: naam, maker, prijs, verkoopblok, ratings, categorie, "Published ... ago", Blender-versie, korte beschrijving. Stopt na 40 add-ons op rij die 7 maanden of ouder zijn.
- De CSV komt op de tak `verkenner-data` (`superhive/addons-6mnd.csv`), tussentijds elke 15 minuten. De volgende run zet hem ook hier als `data/superhive-addons-6mnd-2026-11-15.csv`.
- Analyse: `data/superhive-6mnd-analyse.py` (verdeling 0 tot 10, 10 tot 100, 100+ en 1000+, per leeftijd, mediane prijs, per soort en per Superhive-categorie, prijsklassen, makers, 3D-printen).
- Let op bij het lezen: Superhive toont het verkoopblok pas vanaf 10 verkopen ("10+", "100+", "2600+"). Geen blok betekent 0 tot 9. Het blok is een ondergrens, dus omzet die we eruit rekenen is ook een ondergrens. "Published" is grof (in maanden), dus leeftijd is ±een halve maand.

## Voorproef uit de meting van 9 nov (GEZIEN, `data/superhive-nieuwe-addons-2026-11-09.jsonl`, wordt vervangen)
Dezelfde analyse op de 2.955 add-ons van de meting van 9 nov, alles van 0 tot 6 maanden oud (2.154 betaald, 829 makers):
- Betaald: **79,5% onder 10 verkopen**, 17,5% 10 tot 99, 2,9% 100 tot 999, 0,2% 1000+ (4 add-ons).
- Na 2 tot 6 maanden is het iets beter: 57 tot 77% onder 10, 3 tot 6% 100+.
- Mediane prijs $12 (kwartielen $8 en $20). Duurder verkoopt niet slechter: $15 tot $30 haalt 37 tot 41% 10+ en 9 tot 10% 100+, onder $10 maar 20 tot 23% en 0,5%.
- Scheef: de top 10 makers hebben ±56% van alle verkopen (ondergrens in dollars). Milad Kambari alleen al 12%.
- 3D-printen is klein maar loopt het best per add-on: van 31 betaalde add-ons van 2 tot 6 maanden haalt 16% 100+ (gemiddeld 4 tot 5%).

## 3D-printen: Cleave naast Click Joints Pro (GEZIEN, productpagina 15 nov)
- **Cleave** (V4SS3UR, enige product van deze maker): $23, of $28 als steunversie. Sales 100+, 3 ratings, ±2 maanden oud. Het is vooral een **splitser**: grote STL's in printbare delen knippen langs natuurlijke naden, met per naad een pen (4 profielen, ook zwaluwstaart), deuvel, staafkanaal, magneetgaten of, sinds versie 1.6, een **kogelgewricht** (één kant of dubbel, passing Resin, FDM of eigen, met een "ghost" die laat zien waar het deel heen zwaait). Verder: 120+ printers ingebouwd met "past of past niet" per deel, platen inpakken, 3MF per plaat, Exploded View en Reassemble, reparatie van AI-modellen (Meshy, Tripo). Sterk en breed product.
- **Wat Cleave niet heeft (gelezen op de pagina):** geen bereik in graden, geen scharnier met eindstop, geen testkaartje voor de speling per printer. Precies de punten van Click Joints Pro.
- Andere print-add-ons van de laatste 6 maanden (meting 9 nov): Dovetail Key $18 800+ (Milad Kambari), CatPin $27 400+ (nu met korting $21,60; ook Business-licentie $90), Split-3DPrint $28 400+, JointLab $65 20+, Cut Flex $34,99 10+, SPLIT IT! $12 10+, Oryx CAD $14,99 10+, en een golf van één maker (Hanru Croucamp, 6 nieuwe add-ons van $3 tot $17 in twee dagen). Splitsen met verbinders is de print-klus die verkoopt; gewrichten alleen (JointLab $65) verkoopt veel minder.

## Aanzet ideeën (nog niet gewogen, uit de printmeting van 8 nov, `platformen/blender-2/data/superhive-print-2026-11-08.jsonl`, GEZIEN)
- **Wat verkoopt in de printhoek, ook oud:** reliëf en dieptekaart (True Depth $25 6.900+ in ±2 jaar, AI Depth Modeller $25 600+, Bildeform $19,60 500+, ZForm $8 1.100+), meshreparatie (InstantClean $13 5.000+), splitsen met verbinders (zie boven), schroefdraad en tandwielen (Precision Gears $24 500+, Precision Bolts $24 200+, beide ±4 jaar oud).
- **Wat net nieuw is en (nog) niet verkoopt:** een golf kleine printtools van oktober en november, $7 tot $19, allemaal onder 10: holle modellen met afvoergaten voor resin, lithofaan, sleutelhanger, koekjesvorm, gridfinity, miniatuurvoet, passingtest, bedmaat-splitser. Drukte in kleine printklusjes is dus hoog, met nog geen bewijs van verkoop.
- **Groot signaal buiten printen:** Image to 3D van Milad Kambari ($18) 900+ in 9 dagen (meting 9 nov), op 15 nov 1.200+ in 16 dagen met 22 ratings (GEZIEN, productpagina). Nog na te gaan: gebruikt het een betaalde AI-dienst van buiten. Zijn reeks (Smart Remesh, Auto Unwrap, Smart Segmention, Dovetail Key) zijn allemaal "één klik doet een vervelende klus".

## Eerste 820 van de nieuwe meting (GEZIEN, tussentijdse CSV op tak verkenner-data, 15 nov 21:23)
- De eerste 820 rijen gaan maar tot ±1 maand oud: **744 betaalde add-ons in de laatste maand**, tegen 160 tot 350 per maand in mei tot september (meting 9 nov). De vloed van nieuwe add-ons gaat dus door en is nog groter dan op 9 nov.
- Van die 744 jonge betaalde add-ons: 93,3% onder 10 verkopen, 5,9% 10 tot 99, 0,7% 100+, één 1000+ (Image to 3D, Milad Kambari, nu 1.200+). Dat is hetzelfde beeld als de jongste maand op 9 nov (93,1%).
- Milad Kambari heeft 42% van alle verkopen (ondergrens in dollars) in deze jongste groep. Wie geen naam heeft, begint bijna altijd onder 10.
- 3D-printen in deze maand: 36 nieuwe add-ons, waarvan 24 van één maker (Hanru Croucamp, $1 tot $139, ook bundels). Alleen Cut Flex ($34,99) haalt 10+. Alle andere, ook vier nieuwe splitsers (FigureCut, Mesh Split, Ninja Cut, Easy Slice), staan onder 10.

## Voorlopige top 5 ideeën voor de volgende add-on (run 21:31, nog na te rekenen)
Lat: een duidelijke klus die snel gaat, te testen in Blender zonder scherm (geometrie meten in onze toetsen), bewijs dat zoiets verkoopt, en een reden waarom wij het beter kunnen. Bewijs uit de meting van 9 nov (`data/superhive-nieuwe-addons-2026-11-09.jsonl`) en de printmeting van 8 nov (`platformen/blender-2/data/superhive-print-2026-11-08.jsonl`), GEZIEN tenzij anders vermeld.

1. **Schroefdraad, inzetstukken en passende gaten voor printen, met speling per printer.** Klus: "dit deel moet vast met een M3-schroef of een inzetmoer" in één klik, met gaten en draad die echt passen. Bewijs: Precision Gears $24 500+ en Precision Bolts $24 200+ (beide ±4 jaar oud, zelfde maker), Quick Screws 100+ (±4 jaar). Nieuwkomers Thread Helix en Precision Holes & Inserts (Hanru) staan nog onder 10. Waarom wij: de leiders zijn oud; onze toetsen meten maten al tot op de tiende millimeter (Click Joints), en het testkaartje voor de speling is precies wat hier ontbreekt. Past bij Click Joints Pro als tweede printtool. GOK 10 tot 100 verkopen in 6 maanden.
2. **Zachte fysica in één klik voor animatie** (wiebelen, inveren, botten die nazwaaien). Bewijs: SquishyFX $20 300+ in 3 maanden, SpringFX $20 100+, GanzoFX 100+ (alle drie Aaron Thompson), Flex $65 70+, Jiggle Studio 40+. Fysica en rigging scoren het best van alle soorten: Superhive-categorie rigging 43% 10+ en 8,1% 100+ na 2 tot 6 maanden (alle betaalde samen 30% en 4,5%). Waarom wij: past bij ons simulatorgereedschap, uitkomst is te meten (beweging per frame). Nadeel: Aaron Thompson is actief en goed.
3. **Gewichten en skinning opknappen** (gladde gewichten, kapotte vervormingen bij knieën en ellebogen herstellen). Bewijs: Adaptive Auto Skinning $35 800+ in 4 maanden, Smooth Weights $17,99 400+, WeightForge $30 20+. Waarom wij: vervorming is in Blender zonder scherm te meten (hoek en volume per gewricht), en het sluit aan op wat we leerden over gewrichten. Nadeel: technisch zwaarder, 2 weken is krap.
4. **Reliëf en naambordjes om te printen uit een afbeelding of tekst.** Bewijs: True Depth $25 6.900+ in ±2 jaar, zForm 1.100+, AI Depth Modeller 600+, Bildeform $19,60 500+, Bas-Relief Sculpt 300+. Nieuwe pogingen (DepthCraft AI 10+, Milad's Depth Map 20+, Lithophane Maker onder 10) komen niet ver. Gat: de leiders maken reliëf voor beeld, niet een dicht printbaar stuk met muurdikte, maximale hoogte en bedmaat. Nadeel: True Depth is sterk en Lewis Martin brengt nieuwe dingen uit (PocketCam 100+ in 26 dagen). Volgens de harde regel twijfelgeval.
5. **Mallen maken om te gieten** (tweedelige mal met gietkanaal en luchtgaten uit elk model). Bewijs klein maar echt: Molding Gen 100+ (±3 jaar), MouldCast Studio 60+ in 8 maanden. Waarom wij: zelfde soort geometrie als splitsen en pennen (Click Joints), goed te toetsen. Nadeel: kleine markt, GOK onder 50 verkopen per jaar.

Wat ik bewust niet voorstel: nog een splitser met pennen (in 3 tot 4 maanden 4 winnaars van 400 tot 800, daarna 10 nieuwe die onder 10 blijven, en Cleave dekt bijna alles), "één klik"-hulpmiddelen voor modelleren en UV (Milad Kambari heeft dat in handen), kleine printklusjes van $9 tot $15 (Hanru Croucamp maakt er tientallen, geen enkele verkoopt), meerkleuren-3MF (4 add-ons, alle onder 10).

## Voorlopig prijsadvies Click Joints Pro naast Cleave
- **Advies: $15 in plaats van $12.** Waarom: in de meting van 9 nov haalt $10 tot $15 na 2 tot 6 maanden 28% 10+ en 4,3% 100+, $15 tot $20 41% en 8,7% (GEZIEN). Dat is samenhang, geen bewijs dat de prijs het doet (betere add-ons vragen ook meer), maar onder $15 verkoopt niet beter. $15 blijft duidelijk onder Cleave ($23 en $28) en ver onder JointLab ($65, 20+).
- **Niet als concurrent van Cleave neerzetten, maar ernaast:** Cleave knipt en verbindt, Click Joints Pro maakt een deel beweegbaar met een bereik in graden, een scharnier met eindstop en een testkaartje voor de speling. Die drie heeft Cleave niet (pagina 15 nov). Zin voor de pagina: "Works on parts from any splitter, including Cleave." Alleen schrijven als het getoetst is op een STL die met een splitser is geknipt.
- Eerlijk: Click Joints Pro valt in de groep die het meest voorkomt, een nieuwe maker zonder naam in een volle hoek. Verwachting (GOK): 0 tot 30 verkopen in de eerste 3 maanden. De gratis Click Joints (138 downloads op 15 nov) is de beste weg naar kopers; zet in de gratis versie een duidelijke verwijzing naar Pro.
- Beslissing over de prijs ligt bij Hans en Bram; dit is advies.

## Nog te doen (volgende run)
1. Volledige CSV binnenhalen en in de repo zetten, analyse draaien, cijfers hierboven vervangen.
2. 3D-printen: lijst compleet maken met de nieuwe data (wie, prijs, verkopen per maand, wat ontbreekt).
3. Top 5 en prijsadvies hierboven narekenen met de volle CSV (per soort na 2 tot 6 maanden, prijsklassen, de genoemde add-ons), en definitief maken.
4. Controleur (agent) laat 10 rijen live nakijken en de analyse herrekenen.
