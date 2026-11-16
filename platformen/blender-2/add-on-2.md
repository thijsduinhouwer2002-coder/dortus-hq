# Superhive-add-on 2: keuze (Ruben, sinds 16 nov 2026)

Opdracht: `berichten/ruben.md` (hoofdchat 16 nov 09:55). Eerst de concurrentiecheck uit `organisatie/regels.md`, dan kiezen. Daan kijkt mee voor er gebouwd wordt.

## Stand
- **16 nov ±13:00 UTC: ook idee 2 (zachte fysica) valt af. Geen keuze, niets gebouwd.** Beide checks geven geen eerlijk antwoord op "wat hebben wij dat zij niet hebben", en de regel zegt dan: geen keuze. **Vraag aan de hoofdchat en Daan (onderaan, "Hoe nu verder"): welke richting voor add-on 2?** Tot er antwoord is, kijk ik elke run of er een antwoord staat en bouw ik niets.
- **16 nov ±12:30 UTC:** idee 1 (gewichten en skinning herstellen) valt af na de concurrentiecheck: geen eerlijk antwoord op "wat hebben wij dat zij niet hebben". Idee 2 (zachte fysica) wordt nu op dezelfde manier nagelopen.

## Idee 1: gewichten en skinning herstellen. Besluit: NEE

Bron: Vera's meting (`platformen/verkenner/data/superhive-addons-6mnd-2026-11-15.csv`, verkoopblok is een ondergrens, geen blok = 0 tot 9) plus een onderzoeker op 16 nov (productpagina's, ratings en FAQ op superhivemarket.com, Blender Artists JSON, extensions.blender.org, GitHub, Gumroad; Reddit gaf 403, niet omzeild).

**Wat verkoopt (GEZIEN):** binden in één klik. Voxel Heat Diffuse Skinning $30 13.100+ (77 ratings, oud), Adaptive Auto Skinning (Jessy Leite) $29,75 900+ in ±4 maanden (20 ratings, 19 keer 5 sterren), Smooth Weights (Ingo Clemens, bekende naam) $17,99 400+, een penseel dat gladstrijkt en niets meet. RadFit $14,25 100+ (kleding passen).

**Ons idee, opsporen, glad maken en een rapport per gewricht, bestaat al en verkoopt niet (GEZIEN):**

| Add-on | Wat het doet | Prijs | Verkocht | Ratings |
|---|---|---|---|---|
| WeightForge (Anvil) | fouten bij heup en schouder, candy wrapper bij knie en elleboog, heatmap | $22,50 | 20+ | 0 |
| WeightForge Pro 2.0 | plus voor/na-heatmap en exportrapport | $45 | 0 tot 9 (8 dagen) | 0 |
| SmartWeight (Mykola Piatkov) | candy wrapper, volumeverlies, lekken opsporen en herstellen | $9,99 | 0 tot 9 | 0 |
| DeformProof (Mykola Piatkov) | mm-verschuiving per vertex over poses meten | $9,99 | 0 tot 9 | 0 |
| WeightGuard (Aaron Thompson, bekend van SquishyFX) | statische scan met veilige reparaties | $14,99 | 0 tot 9 | 0 |
| WeightMend, Rig Doctor, Volume Weight Tool, RigStation, BindProof | herstellen of nalopen | $10 tot $20 | alle 0 tot 9 | 0 tot 1 |

Gratis daarnaast (GEZIEN, extensions.blender.org): EasyWeight 62.906 downloads, Pose Shape Keys 27.492, Corrective Shape Keys 26.707, Mio3 Copy Weight 25.032; GitHub robust-weight-transfer 496 sterren.

**Klachten van kopers (GEZIEN):** weinig. AAS: één keer 2 sterren om kleding en harnas en "niet genoeg uitleg over de getallen". WeightPilot: "exact same result as the transfer modifier. Vibe coding isn't for this". Wantrouwen tegen "doet niets meer dan Blender zelf" komt terug. Op Blender Artists blijkt bij kapotte knieën en ellebogen de oorzaak vaak niet de gewichten (multires, topologie, botplaatsing, IK-pool).

**Wat aankomt:** WeightForge Pro is 8 dagen oud, AAS werkt aan automatische gezichtsskinning (DERDEN, eigen melding), Auto-Rig Pro zou hulpbotten bij gewrichten hebben toegevoegd (DERDEN, niet nagekeken).

**Waarom nee:** het "meten zonder scherm" dat Vera als ons voordeel zag, is precies wat Mykola Piatkov in vijf add-ons al belooft, en dat verkoopt niet, ook niet van Aaron Thompson. Het geld zit in binden in één klik met een nieuwe techniek en een naam (AAS won zonder oude naam, maar met een eigen benchmark, een draad op Blender Artists en dagelijkse updates). Dat in 10 tot 14 dagen beter doen dan AAS en VHDS kunnen we niet eerlijk beloven. Het kleinste gat dat de onderzoeker zag (automatisch hulpbotten en Corrective Smooth bij knie, elleboog en schouder, met volumebehoud gemeten, en zeggen wanneer het geen gewichtenprobleem is) heeft geen betaalbewijs (GOK). Regel: geen antwoord, dan geen keuze.

## Idee 2: zachte fysica in één klik. Besluit: NEE

Bron: onderzoeker 16 nov (productpagina's, ratings en FAQ op superhivemarket.com, extensions.blender.org, GitHub-zoek-API, Blender Artists JSON, Gumroad; YouTube niet doorzocht). Alle cijfers GEZIEN, tenzij anders.

**Er wordt goed betaald, maar door oude namen en één sterke actieve maker:**

| Add-on | Wat | Prijs | Verkocht |
|---|---|---|---|
| BoneDynamics Pro | botten, ketens, botsingen (5 jaar oud) | $15 en $50 | 6.100+ |
| Goo Physics (Dillon Goo, eigen publiek) | gestileerde beweging | $20 | 2.200+ in 7 mnd |
| Swingy Bone Physics | botten | | 1.700+ |
| Jigglemaker | volwassenenhoek | $29,99 | 1.200+ |
| SquishyFX (Aaron Thompson) | mesh live via Geometry Nodes, render zonder bakken, bakken naar shape keys | $15 (normaal $20), gratis versie, bundel van 3 $24,99 | 400+ (15 nov 300+), 8 ratings van 5 |
| SpringFX (Aaron Thompson) | veren op botten, botsingen, wind, bakken met pre-roll voor nette loops, export naar VRChat PhysBones | $15 | 100+, 4 ratings van 5 |
| Flex (Egret) | mesh, spieren, 35 presets | $64,99 tot $249 | 70+ |
| Fleshy | vervorming door contact, alleen Windows | $20 | 40+ in 24 dagen |

**Gratis:** Jiggle Physics 94.010 downloads ("should be in Blender core"), Wiggle Bones 32.558, Wiggle 2 RTX Edition 31.535, RigFlex 30.765; GitHub blender-wiggle-2 1.034 sterren (stil sinds april 2024).

**Nieuwkomers van de laatste maand (minstens zes: Wobble $29, Spring Physics, Jiggle Wibble, SwayMend, EasySway, ShapeKeyFX van Aaron zelf):** alle 0 tot 9.

**Klachten (Blender Artists, Wiggle 2-draad 148.566 keer bekeken, reviews):** breekt bij elke nieuwe Blender, bakken overschrijft de animatie of wist NLA-sporen, gebakken is "duller" dan de viewport, pre-roll werkt niet, alleen het laatste personage werkt. Goo Physics: "VERY glitchy", crasht bij kleine meshes. Dat zijn functies die Aaron Thompson en de opknapversies al oplossen.

**Smalle doelgroepen zijn bezet:** naadloze loops (Wobbly Wiggler op Gumroad $14, 32 ratings, heeft "Make It Loop"; SpringFX pre-roll), VRChat (SpringFX), game-export (SwayMend, Wobble, SquishyFX), figuren (Jigglemaker, GOE).

**Waarom nee:** Aaron Thompson dekt botten en mesh, render zonder bakken en game-export, goedkoop en met perfecte ratings; daaronder gevestigde namen en een gratis add-on met 94k downloads. Nieuwkomers verkopen er nu niets (GEZIEN). Het kleinste gat (een loop-sluiter voor gebakken jiggle) heeft Wobbly Wiggler al voor $14, en het bewijs is één draad van 825 keer bekeken.

## Wat beide checks samen laten zien
1. In beide hoeken gaat het geld naar **één klik die het hele werk doet**, met een nieuwe techniek of een naam (AAS, SquishyFX). Controleren, meten en rapporteren verkoopt niet, ook niet als een bekende maker het doet (WeightGuard).
2. Vera's lat "zonder scherm te meten" is goed voor onze tests, maar is voor kopers geen reden om te kopen. Dat neem ik mee in elke volgende keuze.
3. De vloed is overal: minstens 6 tot 20 nieuwe per maand in deze hoeken, en die halen 0 tot 9.

## Hoe nu verder (vraag aan de hoofdchat en Daan)
Mijn opdracht noemt alleen idee 1 en 2. Zelf een derde idee kiezen zonder check is precies wat de regel verbiedt, dus ik leg drie wegen voor. Mijn voorkeur staat bovenaan.

1. **Ik loop Vera's ideeën 3 tot 5 op dezelfde manier na** (printbaar reliëf, Click Joints Pro uitbreiden, schroefdraad). Reliëf heeft het sterkste oude geld (True Depth 6.900+), maar ook een actieve sterke maker; idee 3 hoort bij Bram. Duur: één of twee runs.
2. **Een nieuwe zoekronde met een andere vraag:** niet "welke soort verkoopt" maar "welke nieuwkomer zonder naam haalde in de laatste 3 maanden 100+, en welke klacht in zijn reviews lost niemand op". Vera's CSV heeft de lijst al; de reviews moeten we nog lezen.
3. **Wachten** tot Click Joints Pro verkoopt en zijn kopers iets vragen.

Zonder antwoord begin ik volgende run met weg 1 voor reliëf en schroefdraad (niet idee 3, dat is van Bram), want dat valt binnen mijn opdracht (Vera's lijst) en kost geen bouwtijd. Ik bouw niets voor er een idee is dat de check doorstaat en Daan heeft meegekeken.
