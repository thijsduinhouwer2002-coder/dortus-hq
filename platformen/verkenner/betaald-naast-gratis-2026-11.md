# Wat maakt mensen betalen naast gratis? (Vera, 16 nov 2026)

Opdracht: `berichten/vera.md`, hoofdchat 16 nov 15:40. Aanleiding: Thijs (15:12) "je moet wel een duidelijke waarde hebben in de betaalde, dat mist bij ons soms."
Gemeten 16 nov 2026 tussen 15:40 en 16:30 UTC, alle pagina's met `curl`. Labels: GEZIEN (zelf gelezen of geteld), DERDEN (bron van een ander), GOK (mijn oordeel).
Ruwe lijst: `data/betaald-naast-gratis-superhive-2026-11-16.csv`.

## Kort
1. **Bij de toppers is een gratis versie zeldzaam.** Van de 150 best verkopende add-ons op Superhive (lijst van 8 nov, opnieuw gelezen op 16 nov) hebben er maar 15 iets gratis ernaast (precies de gevraagde 15), en daarvan zijn er 3 alleen een proefbestand of kijkversie zonder werkende add-on (GEZIEN). De rest verkoopt zonder gratis versie. Gratis naast betaald is dus geen voorwaarde om te verkopen; het is een manier om gevonden te worden.
2. **Het patroon bij wie het wel doet: gratis is een compleet, klein gereedschap; betaald is de hele klus, voor wie er werk mee maakt.** Wat achter betalen zit, in volgorde van hoe vaak ik het zag:
   - **meer inhoud** (meer lenzen, presets, assets, riggen): Lens Sim, Easy Fog 2, BagaPie, Urbaniac, RBC (5 van de 12 toppers met een echte gratis versie);
   - **de hele werkwijze, niet één stap** (zelf maken in plaats van alleen plaatsen, bulk, fabriek): KIT OPS, RBC (2 van de 12; Audio Trigger, buiten de top 150, doet het ook).
   Eerlijk: "meer inhoud" en "alleen steunen" komen even vaak voor (elk 5). Bijna de helft van de toppers met een gratis versie geeft dus alles weg en leeft van steun en gemak; FLIP Fluids (demo) valt in geen groep. Het patroon "betaald = de hele klus" geldt voor de makers die wel iets achterhouden;
   - **niets extra, alleen steunen of gemak** (open bron, betaald is hetzelfde of alleen een label weg): Gaffer, PowerSave, Serpens, Anti-Seam, Poly Haven (5);
   - **licentie voor werk dat geld oplevert of voor een team**: bijna allemaal, als tweede trap (Easy Fog 2 $29,99 tegen $59,99 commercieel, AutoCam $29 tegen $129 voor 5 plaatsen).
3. **Voor ons:** Click Joints Pro op $12 met alleen het scharnier is dun naast Cleave ($23 tot $28, knippen met pennen, magneten en kogels volgens de hoofdchat (GEZIEN 15 nov), zoekt zelf knippunten; 100+ verkopen in 2 maanden). $12 is te verdedigen als instapprijs, niet als eindprijs. Met 1.1 "Rig to Figure" (hele figuur in één keer, bereik uit de rig, spelingsproef) is $19 te verdedigen (GOK). Ebb op $4,99 is te duur voor wat de gratis apps al doen; de echte reden om te betalen is de voortgang over weken, en die moet bovenaan. Bison & Flex volgt al het patroon dat op JetBrains werkt (alles in één bestand gratis, over bestanden heen betaald).

## 1. Superhive: toppers met een gratis versie

Hoe gemeten: de 190 best verkopende add-ons uit `data/superhive-bestsellers-addons-2026-11-08.jsonl`; van de eerste 150 de productpagina opnieuw gelezen op 16 nov (GEZIEN). Gezocht naar een variant van $0, een gratis demo, een gratis versie op GitHub of extensions.blender.org, of een woord als "free version", "trial" of "demo". Daarnaast de namen van alle 1.662 add-ons op extensions.blender.org (open API) gezocht op "Lite", "Free" en "Demo", en daarvan de Superhive-pagina gelezen (AutoCam, Audio Trigger, UVgami). Plaats = plek in de verkooplijst.

| Plaats | Add-on | Prijs | Verkocht | Gratis | Alleen betaald | Soort |
|---|---|---|---|---|---|---|
| 6 | FLIP Fluids | $269 | 18.900+ | "Try our free FLIP Fluids Demo addon" | volledige vloeistofsimulatie | proefversie (inhoud demo niet kunnen lezen: GitHub-wiki geblokkeerd vanaf hier) |
| 7 | Poly Haven Asset Browser | $49 | 18.800+ | alle assets gratis (CC0) op polyhaven.com; Poly Haven Lite op extensions.blender.org | "faster access to them directly inside of Blender", en je steunt het maken van nieuwe assets; ook $5 via Patreon | gemak plus steunen |
| 8 | Simply Cloth | $36 | 18.800+ | alleen een gratis .blend met voorbeelden ("Free Gift") | de add-on zelf (Lite $9, hoger tot $36) | proefbestand, geen gratis add-on |
| 31 | Lens Sim | $40 | 7.500+ | Demo $0 = Lite met watermerk in de render | Lite $15 (basis, beperkt aantal lenzen), Full $40 (80+ lenzen, alles) | meer inhoud, watermerk |
| 53 | Alt Tab Easy Fog 2 | $29,99 | 4.700+ | $0: "a few procedural volume presets, explosions, clouds and smoke" | alle presets en VDB's ($29,99), commercieel $59,99 | meer inhoud plus licentie |
| 54 | Gaffer | $19 | 4.700+ | volledige versie, geen tijdslimiet | niets: "The only difference ... is a small 'Trial version' text" | steunen |
| 64 | PowerSave | $1 | 3.100+ | gratis op GitHub | hetzelfde | steunen |
| 68 | BagaPie | $93 (Full) | 3.600+ | BagaPie Modifier $0 (het gereedschap zelf) | 250 assets ($39), 750 assets plus biomen en presets ($93) | meer inhoud |
| 87 | Flared 2 | $59,90 | 2.900+ | alleen een testscène "does not include the addon interface" | de add-on | proefbestand |
| 88 | Urbaniac City Asset Pack | $49,99 | 2.900+ | 14 gratis assets | het hele pakket | meer inhoud |
| 89 | Serpens 3 | $20 | 2.900+ | "You can already download Serpens for free" (GitHub, v4 wordt open bron) | de Superhive-versie, steun | steunen |
| 94 | KIT OPS 4 | $35 | 2.600+ | zelfde add-on: plaatsen, boolean-snijden, eenvoudige INSERTs maken | INSERTs maken die snijden, de hele INSERT FACTORY, favorieten, vervangen, bibliotheek omzetten, PNG naar decal, BATCH, extra hulpmiddelen | hele werkwijze |
| 96 | RBC (auto's riggen) | $59 | 2.600+ | 1 rig, alleen auto, beperkte instellingen | alle soorten voertuigen, geavanceerde instellingen, FX-paneel | meer inhoud plus hele werkwijze |
| 119 | Anti-Seam | $1 | 2.100+ | "if you can't afford to buy it, you can download it for free here" | hetzelfde | steunen |
| 139 | 3D Hair Brush v3 | $85 | 1.900+ | "Free viewer" $0: alleen bekijken en renderen, niets aanpassen | de add-on | kijkversie |
| buiten 150 | AutoCam | $29 | 900+ | "The complete free version ... free everywhere else" ($1 op Superhive omdat het moet) | "the full Pro feature set", studio $129 voor 5 | meer functies plus licentie |
| buiten 150 | Audio Trigger | $29 | 60+ | Lite op extensions.blender.org (723 downloads): elk veld laten bewegen op een BPM-raster, bakken | echte geluidsbestanden: slagen vinden, laag/midden/hoog, golfvorm, BPM vanzelf | hele werkwijze |

Alles GEZIEN op de Superhive-pagina's (16 nov), Lite-downloads op extensions.blender.org GEZIEN. UVgami (gratis Lite op extensions.blender.org, $1 op Superhive) heeft nog geen verkoopteller en telt niet mee.

**Eerlijk over de lijst:** de opdracht vroeg de 15 best verkopende mét gratis versie. In de top 150 zijn het er 15, waarvan 3 alleen een proefbestand of kijkversie (Simply Cloth, Flared, 3D Hair Brush); ik zette er twee kleinere bij (AutoCam, Audio Trigger) omdat ze precies ons model zijn (gratis op extensions.blender.org, betaald op Superhive). De top 3 van Superhive (Auto-Rig Pro 71.000+, Hard Ops 48.400+, MACHIN3tools 36.400+) heeft geen gratis versie; Auto-Rig Pro heeft wel een goedkopere "Lite" van $25 (GEZIEN).

**Wat niet te meten was:** hoeveel mensen van gratis naar betaald gaan. Superhive toont naast "Sales" ook "Downloads", maar dat getal staat ook bij add-ons zonder gratis variant (Auto-Rig Pro 93.900+), dus het telt niet alleen gratis downloads (GEZIEN). Geen omzetting uit af te leiden.

### Het patroon in vier regels (GOK, uit de tabel)
1. **Gratis moet op zichzelf af zijn.** KIT OPS, BagaPie, AutoCam en Audio Trigger geven een gereedschap dat één ding helemaal doet. Niemand geeft een kapotte versie weg; wel soms een beperkte (Lens Sim met watermerk, RBC met 1 rig).
2. **Betaald = de klus van begin tot eind of de grote voorraad.** De vraag is steeds: wie hier werk mee maakt, wil dit sneller of groter. Eén extra functie ernaast (zoals bij ons het scharnier) zie ik bij geen enkele topper als hele reden.
3. **Het verschil staat letterlijk op de pagina, als twee varianten met elk één zin** ("Free: 1 Rig, Type: Car, Limited..."; "Everything in Lite, plus real tracks"). Superhive toont varianten als knoppen met prijs; de koper ziet het verschil zonder te zoeken.
4. **Een tweede trap voor werk en teams** (commercieel, studio 5 plaatsen) brengt extra geld zonder extra bouwen. Wij hebben die al (Studio $45).

## 2. Click Joints gratis en Pro naast het patroon

Bron: `platformen/blender/superhive-pagina.md` (winkeltekst Pro 1.0.1 en 1.0.2), `producten/blender-gewrichten/ontwerp.md`, `platformen/blender-2/rig-to-figure.md` (Ruben, concurrentiecheck 16 nov).

| | Gratis Click Joints (extensions.blender.org) | Click Joints Pro 1.0.2 ($12, Superhive en Gumroad) |
|---|---|---|
| Kogel- en pengewricht, passingkleur, bereik in ±graden | ja | ja |
| Delen splitsen, waterdicht, STL en 3MF in mm | ja | ja |
| Scharnier met eindstop (0 tot 115°) voor knie en elleboog | nee | ja |
| Houdingschuif per scharnier, rood voorbij de stop | nee | ja |
| Afstandscontrole tussen gewrichten | nee | ja |
| Printerprofielen met testkaartje, alle ledematen in één keer, magneetgaten | nee | **nog niet gebouwd** (stond in het ontwerp als Pro) |

**Naast de concurrenten (GEZIEN door Ruben, 16 nov, en de hoofdchat, 15 nov):** Cleave $23 tot $28 (volgens de hoofdchat knippen met pennen, magneten en kogels; volgens Ruben als bewegend gewricht alleen een kogel sinds 1.6, geen eindstop; zoekt zelf knippunten bij nek, schouders, knieën; 100+ in 2 maanden), Cut Flex $34,99 (gewricht per lichaamsdeel, 10+ in 26 dagen, alleen Windows), JointLab $65 (20+).

**Is $12 nu te verdedigen? Als instap ja, als blijvende prijs nee (GOK).**
- Voor: onder Cleave en Cut Flex, en het scharnier met eindstop en bereik in graden heeft niemand anders (Ruben). Wie knieën print die niet achterover mogen klappen, krijgt iets wat nergens te koop is.
- Tegen: volgens het patroon hierboven is één extra gewrichtsoort geen "hele klus". De gratis versie doet al het meeste (kogel, pen, kleur, graden, export). Een koper die Cleave ernaast ziet, ziet bij Cleave meer soorten verbinders plus zelf knippunten zoeken, en bij ons één extra gewricht. Dat is precies wat Thijs voelt.

**Wat moet er in 1.1 om $15 tot $19 te vragen (in volgorde, GOK op basis van het patroon en Rubens plan):**
1. **Hele figuur in één keer** (figuurpresets: heup en schouder kogel, knie en elleboog scharnier, enkel, nek, elk met bereik). Dat is het "hele werkwijze"-patroon van KIT OPS en RBC, en de vraag van de Dovetail Key-koper. Zonder dit geen prijsverhoging.
2. **Rig lezen** (bereik uit Limit Rotation per bot). Uniek, niemand doet het; maakt de belofte "van figuur naar printbaar speelgoed" af.
3. **Spelingsproef in één klik** (drie spelingen naast elkaar als één printje). Klein werk (Bram mat de spelingen al), en het lost de grootste angst op: "klikt het op mijn printer?" Cleave heeft vaste keuzes, wij dan een meting.
- Pas met 1 en 2 erin: $19 (onder Cleave $23, boven de huidige $12). Met alleen 1: $15. Studio mee omhoog naar $59 (zoals Split-3DPrint, GOK).
- Gratis blijft zoals hij is. Niets uit gratis halen: dat kost vertrouwen en de regels van extensions.blender.org staan geen verwijzing naar betaald toe.

**Waarom betalen (één zin, voor de winkelpagina, na 1.1):**
"Free Click Joints makes one joint at a time; Pro turns your whole figure, or your rig, into printable hinges and ball joints that stop where the bones stop."
Tot 1.1 live is (eerlijk, alleen wat er nu is): "Free Click Joints does ball and pin joints; Pro adds the knee and elbow hinge that clicks and stops at 115°, so legs never bend backwards."

**Tabel voor de winkelpagina (Engels, alleen wat er na 1.1 echt in zit; regels met 1.1 pas tonen als ze getest zijn):**

| | Free | Pro |
|---|---|---|
| Ball and pin joints with fit colour | ✓ | ✓ |
| Bend range in degrees | ✓ | ✓ |
| Split, watertight, export STL / 3MF in mm | ✓ | ✓ |
| Knee and elbow hinge that stops at 115° | | ✓ |
| Pose slider, red where parts collide | | ✓ |
| Whole figure in one click (hips, shoulders, knees, elbows, ankles, neck) | | ✓ (1.1) |
| Read your rig: joint ranges from your bones | | ✓ (1.1) |
| Clearance test print (0.1 / 0.2 / 0.3 mm) | | ✓ (1.1) |
| Studio licence (up to 5 people) | | ✓ (alleen tonen in een winkel waar Studio te koop is; nu alleen Superhive) |

## 3. Ebb ($4,99) naast de gratis ademapps

Bron: `platformen/succes/verhalen-groei.md` verhaal 14 (Joris, 16 nov) en `platformen/garmin/concurrenten-2026-11-13.md`.

**Wat de markt zegt (DERDEN uit verhaal 14, door Joris GEZIEN):** van 33 nieuwe ademhalingsapps (16 aug tot 16 nov) haalden 7 de 100+, en 6 van die 7 zijn gratis. De enige betaalde met 100+ kost $1,99 (Vagal). Ebb en Vytera Breath op $4,99 stonden na 3 en 24 dagen op 0. De gratis leider voor inhouden is WHM breathing; Garmin heeft zelf een ademtimer.

| | Gratis apps (WHM breathing, Breathe Free, Garmin zelf) | Ebb Calm (gratis, wacht op keuring) | Ebb ($4,99) |
|---|---|---|---|
| Rustig ademen met een patroon | ja | alleen 4-7-8 | box, 4-7-8, rustig, eigen patroon |
| Rondes met adem inhouden | ja (WHM) | nee | ja |
| Trilling per fase, ogen dicht | deels (GOK, niet bij elke app nagekeken) | ja | ja |
| Inhouden als duik, dieren die je verzamelt | nee | één dier | 24 dieren, logboek |
| Eindscherm met rondes, 8 weken met gemiddelde en sessies per week | nee (GOK: niet gezien bij de nieuwe gratis apps) | nee | ja |

**Eerlijk:** de kern (rondes met een inhoudtimer) zit al gratis in WHM breathing. Wat alleen Ebb heeft is **zien dat je blijft oefenen** (eindscherm met je rondes, 8 weken met gemiddelde en sessies per week) en de beleving (duik, 24 dieren die je verdient door terug te komen). Let op: langer inhouden wordt bewust niet beloond (besluiten 10 en 12 nov, Garmin-regel); dus geen record en geen groeiende inhoudtijd beloven. Dat is het patroon "betaald = de hele klus", maar alleen als de koper het in een paar seconden ziet. Op de huidige winkelpagina komt "mooi" eerst ("Breathe. Make sea friends.") en voortgang later.
- **$4,99 is nu niet te verdedigen naast gratis** (GOK, steunt op de 6 van 7 gratis winnaars). Advies blijft wat Joris schreef: tijdelijk $2,99 tot de eerste 5 reviews, en Ebb Calm openbaar als gratis ingang. Daarna terug naar $4,99 kan als de reviews de voortgang noemen.
- Geen medische beloftes in de zin of de tabel.

**Waarom betalen (één zin):** "Ebb Calm helps you breathe; Ebb turns your practice into a habit: breath hold rounds as a calm dive, 24 sea animals you meet by coming back, and 8 weeks that show how often you practised."

**Tabel voor de winkelpagina (Engels):**

| | Ebb Calm (free) | Ebb |
|---|---|---|
| Calm breathing 4-7-8 with the rising sea | ✓ | ✓ |
| Vibration for every phase, eyes closed | ✓ | ✓ |
| Slow breathing and your own pattern | | ✓ |
| Breath hold rounds: each hold is a dive | | ✓ |
| Summary of your rounds after every session | | ✓ |
| 8 weeks: average per session and sessions per week | | ✓ |
| 24 sea animals to meet and keep in your log | 1 | 24 |

(Box 4-4-4-4 is op 11 nov uit de winkeltekst gehaald; pas weer tonen als Gijs het vast in de winkeltekst zet. Gijs kijkt na of "summary of your rounds" precies is wat het eindscherm nu toont.)

## 4. Bison & Flex Pro ($19 per jaar, $49 voor bedrijven) naast het patroon op JetBrains

Bron: `producten/jetbrains-bison-flex/ontwerp.md`, `platformen/jetbrains/status.md` (9 nov: nog in keuring, verborgen). Vergelijking: de vijf meest gedownloade freemium-plugins op JetBrains Marketplace via de open API (`api/searchPlugins?pricingModels=FREEMIUM`, 413 freemium-plugins, GEZIEN 16 nov).

| Plugin | Downloads | Gratis | Betaald |
|---|---|---|---|
| GitToolBox | 10,8 mln | alles lokaal: telling, blame op de regel, takken opruimen | alles wat over grenzen gaat: links naar de remote, pull request erbij, uitgebreide blame |
| Symfony Plugin | 8,7 mln | bijna alles ("All features which are inside GitHub are free") | oude versies, gemarkeerd met [paid]; 15 min alles open bij het openen van een project |
| Better Highlights | 1,0 mln | commentaar kleuren, verwijzingen | eigen markeringen, RegExp, instellingen voor zware gebruikers |
| Shopware | 0,1 mln | basis | navigatie, aanvullen en inspecties; "all day on Friday" gratis |

**Bison & Flex past al in het patroon van GitToolBox:** binnen één bestand gratis, over grammatica en scanner heen betaald, plus meldingen. Dat is een duidelijke grens die een gebruiker snapt (GOK). Zwakker punt: de belangrijkste dagelijkse hulp (aanvullen van namen) komt pas in 1.1, en $19 per jaar is een abonnement voor een kleine niche. Advies: aanvullen in Pro bij 1.1, en de 30 dagen proef plus "één melding per sessie" houden. Prijs laten tot er gebruikers zijn: zonder één download valt er niets te meten.

**Waarom betalen (één zin):** "Free Bison & Flex understands each file; Pro connects them: jump, find and rename tokens between grammar and scanner, and see undefined or unused names before Bison does."

**Tabel voor de pluginpagina (Engels):**

| | Free | Pro |
|---|---|---|
| Bison/Yacc and Flex/Lex file types, colours, folding, structure view | ✓ | ✓ |
| Syntax errors in grammar and scanner | ✓ | ✓ |
| Go to declaration and rename within one file | ✓ | ✓ |
| Jump, find usages and rename across grammar and scanner | | ✓ |
| Undefined and unused names, with a quick fix | | ✓ |
| Completion of rule and token names | | ✓ (1.1) |
| 30-day free trial | | ✓ |

## Nakijken
Controleur (agent, 16 nov ±16:40 UTC): Superhive-steekproef 7 van 7 klopt (KIT OPS, Lens Sim, RBC, BagaPie, Gaffer, AutoCam, Anti-Seam: prijs, verkoopblok en gratis/betaald). Zes moet-correcties verwerkt: Ebb-zin en -tabel zonder record en groeiende inhoudtijd (botste met de besluiten van 10 en 12 nov), box-regel eruit, Cleave met bron, patroon eerlijker (steunen even vaak als meer inhoud, Audio Trigger niet als topper), Bison find usages eruit tot de code het bevestigt, Studio alleen waar te koop. Ook: het bewijs dat $4,99 te duur is, is dun (7 apps met 100+, Ebb pas 3 dagen in de winkel).

## Wat ik niet weet
- Hoeveel gebruikers van een gratis versie later kopen (Superhive geeft het niet, zie boven).
- Wat er precies in de FLIP Fluids Demo zit (GitHub is vanaf hier niet te lezen).
- Of de prijs $19 voor Click Joints Pro 1.1 echt meer oplevert dan $12: dat is een GOK; meten kan pas na de lancering (verkopen per week voor en na).

## Doorgegeven
- Ruben en Bram (Click Joints): dit stuk, vooral de volgorde in 1.1 en de zin. Chris: de tabellen voor de winkelpagina's. Gijs: de Ebb-zin en -tabel. Jet: de Bison & Flex-tabel. Via mijn logboek; de hoofdchat beslist over prijzen.
