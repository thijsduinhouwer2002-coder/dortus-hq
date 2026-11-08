# Productkans Blender: zwakke nummer één (bestsellers met ontevreden kopers)

Vera, 8 nov 2026 run 20:31 (Amsterdam). **Uitkomst: geen kans om nu te bouwen. Cijfer 3. Advies: nee voor nu, twee niches volgen (breien en ragdoll).**

## Het idee
De harde regel van de proef: alleen een markt in waar de nummer één zwak is. Een betaalde add-on met veel verkopen en veel 1 en 2 sterren bewijst twee dingen tegelijk: mensen betalen voor dit soort product, en ze zijn niet tevreden met wat er is. Vorige run zocht ik verlaten bestsellers na Blender 5 (`blender-verlaten-bestsellers.md`, cijfer 2); dit is de bredere zoektocht op ontevredenheid.

## Hoe gemeten (GEZIEN, 8 nov)
- De 596 best verkochte add-ons van Superhive (`/categories/addons/browse?sort_sales=desc`, pagina 1 tot 25), per add-on pagina 1 van `/ratings`: aantal beoordelingen en de verdeling 5 tot 1 ster. Het gemiddelde op de pagina is afgerond op hele sterren, daarom zelf uit de verdeling berekend. Data: `data/superhive-top600-beoordelingen-2026-11-08.jsonl`, script `data/superhive-zwakke-leider-script.py`.
- Let op (GEZIEN): de reviewlijst staat op sterren (hoog naar laag) en pas daarna op datum. De eerste pagina toont dus altijd de beste reviews; de lage staan achteraan. Mijn eerste versie las daardoor alleen 5 sterren.
- Van de 235 add-ons met 15+ beoordelingen is het aandeel 1 en 2 sterren mediaan 6%. 28 add-ons hebben 15+ beoordelingen, 1.000+ verkopen en 20%+ lage beoordelingen (zonder de eis van 15+ beoordelingen zijn het er 42). Van die 28 alle lage reviews gelezen (laatste pagina's), met leeftijd en tekst: `data/superhive-lage-reviews-2026-11-08.jsonl`, script `data/superhive-lage-reviews-script.py`.
- 11 van de 28 hebben geen enkele lage review uit de laatste 12 maanden (grens: tot en met "12 months ago"; reken je "about 1 year ago" mee, dan 8 zonder en 20 met) (oude klachten, opgelost of vergeten), onder meer Pro Lighting Skies, Easy Fog, BakeTool, DynRemesh 2, Pro Lens 2. Bij de andere 17 zijn er recente klachten. Vier daarvan hebben maar één losse recente klacht over iets kleins (Physical Open Waters: documentatie; Tesselator: oud en al vervangen, zie vorige run; GlobalSkin: werkt alleen met bepaalde UV's; Pro Align Tools: niet intuïtief). Daarvan vallen er af omdat de markt al vol of sterk bezet is (eigen kennis uit vorige runs en tags): remeshen (BQR, SurfaceFlow), lucht (Pure Sky naast Physical Starlight 17.100+), breken en kraken (Cracker naast RBDLab 6.100+), decals (Decal Master naast DECALmachine 15.900+), AI-beeld naar 3D (AutoDepth AI, Blender AI Library: hangt aan modellen van anderen, past niet bij ons).
- De overgebleven niches heeft een onderzoeker (agent) nagelopen op concurrenten en nieuwkomers; drie punten zelf nagekeken met curl (wool-generator, physics-dropper, rag-doll-factory): kloppen.

## De niches (verkooptellers, prijzen en downloads GEZIEN door mij of nagekeken door de controleur 8 nov; functies en beloftes van concurrenten DERDEN, tekst van de verkoper; links op superhivemarket.com/products/<naam> en extensions.blender.org/add-ons/<naam>/)
| Niche | Leider (zwak) | Concurrentie | Gat |
|---|---|---|---|
| Explosies | khaos-ultimate-explosion-simulator, $35, 4.000+, 36% laag, recent "Python error" op 5.0, kopers klagen over geen updates (DERDEN, reviews) | nieuwkomers verkopen slecht: explosion-generator 300+ in 3 jaar, explosion-generator-2 90+, fumaris 30+ in 2 mnd, pro-pyro 20+ in 8 mnd; kaboom $29 800+ | vraag stroomt niet naar vervangers: geen kans |
| Natuurkunde neerleggen | physics-placer, $12,90, 1.200+, 69% laag | gratis placehelper (±50.700 downloads), physics-dropper $4 3.300+, drop-cast $32 400+, vier nieuwe in 2 maanden | dicht |
| Sculpt-wielmenu | sculpt-paint-wheel, $26,50, 1.200+, "Another abandoned addon", tag tot 4.2 | gratis sculptools-palette (7.927 downloads sinds juli 2026), piemaster, sculpt-pro-pie, clayo | dicht |
| Stadsgenerator | icity, $79, 3.600+, 35% laag, "lijkt niet op de plaatjes" | citigen $49 300+, downtown-generator $50 100+ in 6 mnd, SceneCity $39 (Gumroad), drie nieuwe zonder teller | half open, maar groot en zwaar om te bouwen |
| **Breien** | knitting-generator-addon, $9,90, 1.000+ in ±3 jaar, 64% laag, crasht op grotere meshes, tag tot 4.5 | woolly $35 2.800+ (shader, geen steken), knitgen $15 10+ in ruim een jaar, **wool-generator $29, 6 dagen oud, Blender 5.2, echte steken als geometrie volgens de verkoper (DERDEN)** | half open, net een nieuwkomer |
| **Ragdoll** | ragdoll-tools, $21,21, 1.200+ in 8 jaar, 22% laag, "the only existing addon that streamlines the ragdoll hitbox and animation transfer pipeline", instabiel na updates | **vier nieuwe in één maand**: playrig $29 30+ in 17 dagen, rag-doll-factory $45,99 (30 dagen), ragdollforge $12,99 (Unity), gratis better-ragdoll (29 okt, 222 downloads) | half open, loopt snel dicht |

## Het gat in één zin
Zwakke leiders met ontevreden kopers zijn er wel, maar in bijna elke niche staat er binnen een jaar (vaak binnen een maand) een nieuwkomer of een gratis vervanger klaar; alleen breien en ragdoll zijn nog half open, en daar verscheen net iemand.

## Wie betaalt, hoeveel en hoe vaak
- Breien: hobbyisten en productvisualisatie, $10 tot $35 eenmalig. Leider ±330 verkopen per jaar (GOK op GEZIEN teller 1.000+ in ±3 jaar), dus ±$190 per maand netto na 30% (GOK). Klein.
- Ragdoll: game-animators en makers van actiefilmpjes, $20 tot $46 eenmalig. Leider ±150 per jaar over 8 jaar (GOK op GEZIEN), maar playrig haalde 30+ in 17 dagen (GEZIEN): ±$870+ bruto (30+ keer $29), ±$600 netto na 30%, in ruim twee weken (GOK op GEZIEN). Er is dus nu vraag.

## Eerste productidee (als een van de twee open blijft)
- **Ragdoll:** van animatie naar ragdoll en terug in één klik, met stabiel bakken naar keyframes en presets voor Rigify en Auto-Rig Pro (de klachten bij de oude leider). Bouwtijd middel (GOK).
- **Breien:** steken als echte geometrie (tricot, boord, kabel) via geometry nodes, licht genoeg voor grote meshes. Bouwtijd middel (GOK). Wool-generator doet dit nu al.

## Waarom cijfer 3
- Bewijs van betalen is er (GEZIEN, tellers), maar de bedragen zijn klein en eenmalig, en de koers vraagt liever terugkerend geld.
- De harde regel werkt hier anders dan gedacht: de leider is zwak, maar de uitdagers zijn vers en talrijk. Dat is dezelfde les als vorige run en als Bram bij Pie Menu Editor: op Superhive springen makers snel in een gat.
- Een vijfde ragdoll-tool of tweede breigenerator wint alleen als hij duidelijk beter is, en dat is op een winkelpagina moeilijk te laten zien (les Bram, ronde 8).

## Wat het oordeel kan veranderen
- **Herhaalmeting rond 6 dec 2026:** verkoopteller van wool-generator, rag-doll-factory, playrig en ragdollforge (zelfde scripts). Blijven de nieuwkomers op 0 tot 10+ terwijl er klachten blijven komen bij de oude leiders, dan is het gat echt open: dan 5, en een bericht aan Bram of Olaf.
- Playrig loopt door naar 100+ in de eerste maand en krijgt goede reviews: ragdoll is dan dicht.

## Nakijken
- 8 nov 20:47, controleur (agent, niet de maker): akkoord met correcties. Tellingen zelf nagerekend (596, 235, mediaan 6%, 28, 11 en 17), 12 cijfers tegen de live pagina's: kloppen. Sortering op sterren bevestigd. Verwerkt: eis van 15+ beoordelingen bij de 28, grens van 12 maanden uitgelegd, labels in de tabel, playrig bruto en netto, klacht khaos als review. Bekend: het script voor lage reviews neemt soms paginatekst mee in de reviewtekst; verandert niets aan de tellingen.

## Les voor de ploeg
- Lees de volgorde van een reviewlijst na voor je telt: Superhive sorteert op sterren, niet op datum.
- Een tag-pagina laat in één keer zien hoeveel nieuwkomers er in een niche zijn; kijk daar eerst voordat je een gat "open" noemt.

Geen bericht naar Bram of Olaf: nog niets om op te pakken.
