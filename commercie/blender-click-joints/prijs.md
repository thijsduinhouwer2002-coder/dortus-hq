# Click Joints (Blender): prijs

Door Chris, 8 nov 2026. Het besluit over de prijs is van Bram (platformmanager); dit is mijn voorstel en een toets van wat er al besloten is. Vroeg gemaakt, terwijl het product nog gebouwd wordt, omdat de verdeling gratis en betaald nu in de code komt.

## Wat er nu staat (besluit Bram, 8 nov, `organisatie/besluiten.md`)
- Gratis op extensions.blender.org: kogel en pen, speling in mm, één gewricht tegelijk, passingkleur, waterdichte uitvoer.
- Betaald op Superhive: **$12, lanceerprijs $9 (GOK)**. Scharnier met eindstop, printerprofielen met testkaartje, alle ledematen in één keer, magneetgaten en wrijvingsribbels.
- Kosten Superhive: maker houdt 70% op het gratis plan, plus $0,49 per verkoop (DERDEN, `platformen/blender/status.md`). Bij $12 houdt Dortus ±$7,91 over, bij $15 ±$10,01, bij $9 ±$5,81 (eigen rekensom op die afdracht).

## Wat de markt vraagt (alles GEZIEN 8 nov 2026 met curl, `https://superhivemarket.com/products/<slug>`, tenzij anders)
23 splitters en gewrichtentools op Superhive, normale prijs voor één licentie:
- **Mediaan $15**, middelste helft $8 tot $24, spreiding $1 tot $65.
- Alleen de tools met een teller van 30+ verkopen: mediaan ±$21 (Articulator $1, Dovetail Key $18, SnapSplit $20, Cleave $23, Split-3DPrint $28, CatPin $30).

| Product | Prijs nu (normaal) | Verkocht | Beweegbare gewrichten? |
|---|---|---|---|
| CatPin | $24 ($30) | 400+ | nee, zegt zelf "Articulated, rotating and movable joints are not currently supported" |
| Split-3DPrint | $22 ($28) | 400+ (telt $0-variant mee) | nee |
| Dovetail Key | $18 | 800+ | nee |
| Cleave | $23 | 90+ | kogel ja, scharnier nee |
| Cut Flex | $34,99 | 10+ (18 dagen) | ja, 15 vormen, plus beweegproef "Check Pose" |
| JointLab | $65 (early access) | 20+ | ja |
| Articulator | $1 | 30+ | kogel en scharnier, geen eindstop |
| SnapSplit | $20 | 30+ | nee |
| FigureCut | $10 | geen teller (7 dagen) | pen en gat |
| Pose to Print | $18 ($24) | geen teller (5 dagen) | nee, versmelt alles tot één dicht geheel |
| Fit & Tolerance Test Generator | $7 | geen teller | alleen een testkaartje |
| LayerMechanic | $25 | geen teller (26 dagen) | beweegproef met PASS/FAIL |

Let op: de teller op Superhive telt ook $0- en $1-varianten mee (GEZIEN bij Split-3DPrint en Articulator).

## Gratis naast betaald: werkt dat? (GEZIEN, downloads op extensions.blender.org, tellers op Superhive)
| Product | Gratis versie | Betaald | Verschil |
|---|---|---|---|
| AutoCam | 37.181 downloads | $29, 900+ (telt $1-variant mee) | Pro heeft extra functies |
| Retro Console | Lite, 1.756 | $20, 70+ | 21 presets, paletten, dithering alleen betaald |
| Audio Trigger | Lite, 654 | $29, 50+ | audiobestanden alleen betaald |
| Driver Espresso | Lite, 193 | $25 of $45, 10+ | 18 tegen 135 of 230 recepten |
| SnapSplit | 1.237 | $20, 30+ | zelfde product |
| Easy-Print | 6.973 | $5 (nu $2,75), ±10 | zelfde product, betalen is steun |

**Wat opvalt (GOK op GEZIEN):** ruwweg 1 tot 5% van de gratis downloads koopt. Wie gratis en betaald hetzelfde aanbiedt, verkoopt bijna niets (Easy-Print ±0,15%). Het werkt als de gratis versie echt werkt maar duidelijk minder kan (Retro Console, Driver Espresso, Audio Trigger tot ±8%). Het plan van Bram past bij dat patroon: één gewricht tegelijk, geen scharnier, geen profielen.

Rekenvoorbeeld (GOK): een nieuwe gratis print-add-on haalt op extensions.blender.org ±1.200 tot 7.000 downloads in een paar maanden (SnapSplit 1.237, EasySlice Print 5.792, Easy-Print 6.973, GEZIEN). Bij 1 tot 5% kopers zijn dat 12 tot 350 verkopen, het midden past bij de verwachting van de controleur van Bram (20 tot 60 in 6 maanden).

## Voorstel
1. **Normale prijs $15 in plaats van $12.** Waarom: geen enkele concurrent heeft scharnier met eindstop plus testkaartje plus passingkleur samen, en per verkoop houdt Dortus ±$10,01 over in plaats van ±$7,91, 27% meer.
   **Tegenargument (controleur):** Bram stelde als eis "een duidelijk lagere prijs dan het veld" (`platformen/blender/kandidaten-2026-11-07.md` sectie 18), en $15 is precies de mediaan van alle 23 splitters. Ook het doel van een bewijsproduct (de hele weg leren) en de stopregel (10 verkopen in 6 weken) pleiten voor een lage drempel. **Mijn antwoord:** het veld waar wij mee vergeleken worden is niet "alle splitters" maar de tools met beweegbare gewrichten: Cleave $23, Cut Flex $34,99, JointLab $65. Daar is $15 nog steeds 35% onder de goedkoopste (Cleave), dus de eis van Bram blijft overeind. Dat goedkoop hier niet beter verkoopt, kan ik niet hard maken: de nieuwkomers onder $12 (FigureCut $10, Fit & Tolerance $7) hebben nog geen teller maar zijn ook pas 7 en 14 dagen oud. Kiest Bram voor de lage drempel, dan is $12 verdedigbaar; dit is een afweging, geen fout.
2. **Geen eigen lanceerprijs van $9 in de week van Black Friday.** Superhive houdt elk jaar van Black Friday tot Cyber Monday een sitebrede uitverkoop van 5 dagen, meestal 25% korting, en noemt het de drukste week van het jaar: in 2024 $713k omzet in 5 dagen, 80% van een gewone maand (DERDEN, [cyber sale recap 2024](https://superhivemarket.com/posts/blender-market-2024-cyber-sale-recap), [2025 Cyber Sale](https://superhivemarket.com/page/2025-cyber-sale), die pagina laadt alleen met JavaScript en is niet nagelezen). Een eigen korting werkt niet tijdens zo'n sitebrede uitverkoop (DERDEN, [creator sale campaigns](https://support.superhivemarket.com/article/315-creator-sale-campaigns)). Black Friday 2026 is 27 nov. Dus: staat Click Joints vóór die week live, dan meedoen met de sitebrede uitverkoop (vinkje "Opt-in to all sitewide sales", [artikel 300](https://support.superhivemarket.com/article/300-participating-in-site-wide-sales)); $15 min 25% is $11,25, Dortus houdt dan ±$7,39 over, iets minder dan bij een normale $12; de week is het waard om de drukte, niet om de marge. Het vinkje geldt voor alle toekomstige sitebrede uitverkopen; liever per campagne aanzetten. Staat hij er pas later, dan een eigen lanceerprijs van $12 (20% korting) in de eerste twee weken. **Niet haasten om die week te halen** (besluit Thijs 6 nov): eerst Daan akkoord en een groene test.
3. **Verdeling gratis en betaald zo laten**, met één waarschuwing: de gratis versie moet echt werken (regel 3.3 van extensions.blender.org) maar duidelijk minder kunnen dan de betaalde, anders koopt niemand (zie Easy-Print). Eén gewricht tegelijk tegen alle ledematen in één keer is een goede, harde grens. Het testkaartje blijft betaald: de controleur van Bram opperde het als lokmiddel in de gratis versie, maar een los testkaartje kost bij de concurrent al $7, dus het heeft waarde.
4. **Geen sleutel, geen proefversie op Superhive.** De gratis versie op extensions.blender.org is de proef. Dat past bij wat Superhive levert (zip zonder sleutelsysteem, `producten/blender-gewrichten/ontwerp.md`).

## Wat dit voorstel zou veranderen
- Na 6 weken onder de 10 verkopen geldt de stopregel van Bram. Mijn suggestie (zijn besluit, niet het mijne): kijk dan ook naar bezoekers tegen kopers op de Superhive-pagina, zodat we weten of het aan de prijs of aan de vraag lag.
- CatPin of Split-3DPrint gaat beweegbare gewrichten maken (CatPin zegt "not currently supported"): dan zijn wij niet meer de enige naast de dure tools.
- Cut Flex of Cleave gaat onder $15 zakken of voegt een passingkleur plus testkaartje toe: dan opnieuw naar de prijs kijken.
- Superhive kondigt voor 2026 geen Cyber Sale aan of een andere opzet: punt 2 opnieuw bekijken.
