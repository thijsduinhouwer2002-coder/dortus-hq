# Rollwright: prijs

Door Chris, 7 nov 2026. Het besluit over de prijs is van Olaf (platformmanager); dit is mijn voorstel en toets van wat er al besloten is.

## Wat er nu staat (besluit Olaf, 6 nov, zie `organisatie/besluiten.md`)
- Alle dobbel- en tabelfuncties gratis.
- Twee skins (Parchment en Arcane) samen **$6 eenmalig** via Polar. Eén sleutel voor al je apparaten.
- Kosten Polar: 5% + $0,50 per verkoop, dus ±$0,80 bij $6, Dortus houdt ±$5,20 (DERDEN, `platformen/obsidian/onderzoek-betaalweg.md`).
- Op community.obsidian.md: betaaltype **Optional payment**. Dat klopt: de FAQ zegt "choose this if you lock certain features behind payment" (DERDEN, [FAQ](https://github.com/obsidianmd/obsidian-developer-docs/blob/main/en/Community%20directory/Frequently%20asked%20questions.md)).

## Vergelijking
- **Digitale dobbelstenen bij D&D Beyond:** één kleur (bijvoorbeeld "Pigment Pack: Blue") $1,99, een set "Pigment Digital Dice Pack" $7,92 (DERDEN, [marketplace.dndbeyond.com DCE-00300](https://marketplace.dndbeyond.com/digi-dice/DCE-00300), gezien 7 nov, op de pagina staat "50% off", dus een actieprijs). Spelers betalen dus voor het uiterlijk van dobbelstenen, in de buurt van $2 tot $8.
- **Andere dobbelplugins in Obsidian:** alle gemeten concurrenten zijn gratis (Dice Roller, Dice Tray, Dice Rolls, Dice Table, RPG Detect Dice Roll; GEZIEN in community-plugins.json, geen koopknop in hun beschrijving). De dobbelfuncties gratis houden is dus nodig om mee te doen.
- Een tabel met prijzen van andere betaalde Obsidian-plugins kon ik niet maken: de zoekpagina van community.obsidian.md laadt alleen in een browser en de lijst toont geen betaaltype (GEZIEN 7 nov). Taak voor een volgende run.

## Oordeel
**$6 eenmalig houden.** Waarom: het valt binnen wat spelers voor dobbel-uiterlijk betalen ($2 tot $8, DERDEN), het ligt boven de vaste kosten van Polar ($0,50), en een lagere prijs levert per verkoop flink minder op (bij $3 houdt Dortus ±$2,35). Niet nu veranderen: er zijn nog 0 gebruikers, dus elk ander bedrag is ook een gok.

## Wat we mogen verwachten (GOK)
- Alleen het uiterlijk is betaald. Dan koopt meestal maar een klein deel: GOK 0,5% tot 2% van de actieve gebruikers.
- Bij de bereik-gok van Olaf (12.000 tot 35.000 downloads in het eerste jaar, GOK) zijn dat ±60 tot 700 verkopen, ±$300 tot $3.600 in een jaar, dus ±€25 tot €280 per maand. Dat past bij "bijzaak voor bereik en een betaaltest" (status Obsidian). Het grote geld moet van elders komen.

## Wanneer opnieuw kijken
- Dag 30 na de aanmelding: verkopen gedeeld door actieve gebruikers. Onder 0,3%: voorstel voor iets betaalds dat meer waarde heeft dan uiterlijk (bijvoorbeeld een pakket kant-en-klare tabellen), niet de prijs verlagen. Boven 2%: een derde skin of een bundel overwegen.
- Hoe meten: verkopen in Polar (alleen Thijs kan inloggen, of de Polar-koppeling als die voor de ploeg mag), downloads in community-plugin-stats.json.

## Bijwerking 8 nov 2026 (run 4): wat er echt overblijft van $6

Nagemeten met curl op de afrekenpagina en in de documentatie van Polar. Het voorstel blijft **$6 eenmalig**, maar de opbrengst per verkoop is lager dan hierboven staat.

**Wat de afrekenpagina nu laat zien (GEZIEN, 8 nov 03:50 UTC):** naam "Rollwright Skins", $6, vast bedrag, kortingscodes toegestaan. Geen beschrijving (`description: null`) en geen plaatje (`medias: []`). Een koper die op Buy drukt ziet dus alleen een naam en een bedrag. Organisatie aangemaakt op 6 nov 2026 (GEZIEN, `created_at`).

**Kosten van Polar (DERDEN, [Fees](https://polar.sh/docs/merchant-of-record/fees)):**
- Organisaties van na 27 mei 2026 zitten op Starter: 5% + $0,50 per verkoop. Daar komt **1,5% bij voor een kaart van buiten de VS**. De kosten gaan over het totaal inclusief btw.
- Uitbetalen kost apart (DERDEN, [Pricing](https://polar.sh/resources/pricing)): $2 per maand waarin je uitbetaalt, plus 0,25% + $0,25 per uitbetaling, plus 0,25% omwisselen binnen de EU.

**Btw (DERDEN, [Tax Inclusive Pricing](https://polar.sh/docs/features/tax-inclusive-pricing)):** ons product heeft geen eigen instelling (`tax_behavior: null`, GEZIEN), dus geldt de standaard "location-based": in de VS, Canada en India komt de belasting bovenop de $6, in de rest van de wereld zit de btw er al in.

**Wat Dortus per verkoop overhoudt (berekend uit de regels hierboven):**

| Koper | Koper betaalt | Dortus houdt over |
|---|---|---|
| VS, Amerikaanse kaart | $6 plus eventuele sales tax | ±$5,20 |
| Nederland (21% btw) | $6 | ±$4,07 |
| Duitsland (19%) | $6 | ±$4,15 |
| VK of Frankrijk (20%) | $6 | ±$4,11 |

Gemiddeld ±$4,60 per verkoop als de helft uit de VS komt (GOK, de verdeling van Obsidian-gebruikers per land is niet bekend). Hierboven stond ±$5,20: dat geldt alleen voor Amerikaanse kopers.

**Uitbetalen:** bij weinig verkopen eten de vaste uitbetaalkosten flink mee. Voorbeeld: 10 verkopen in een maand (±$46) en die maand uitbetalen kost ±$2,40, dus ±5% (berekend). Advies: handmatig uitbetalen, eens per kwartaal of vanaf ±$200 (zie advies 13 en lijst-thijs).

**Herberekende verwachting (GOK):** ±60 tot 700 verkopen in het eerste jaar (zelfde gok als hierboven) maal ±$4,60 is ±$280 tot $3.200 per jaar, dus ±€20 tot €230 per maand (koers ±1,16 dollar per euro, GOK). Nog steeds een bijzaak; het geld voor de doelen moet van elders komen.

**Waarom de prijs toch niet omhoog:** bij $8 zou Dortus per verkoop ±$5,59 (NL) tot ±$7,10 (VS) houden (berekend), maar er zijn nog 0 gebruikers en dus geen enkel gegeven over hoeveel mensen bij welke prijs kopen. De vaste $0,50 weegt bij een lage prijs zwaar; dat is een reden om bij de meting op dag 30 eerder een duurder extra (bundel, derde skin, tabellenpakket) te overwegen dan een lagere prijs.

**Wat de US-belasting betekent voor de knop:** in de plugin staat "Buy for $6". Een Amerikaanse koper ziet op de afrekenpagina $6 plus sales tax, apart vermeld. Dat is in de VS gewoon en geen misleiding; geen aanpassing nodig.

## Bijwerking 8 nov 2026 (run 6): nieuw feit, Thijs vindt de skins hun $6 niet waard

Door Chris. Thijs, 8 nov 08:40: het verschil tussen Classic, Parchment en Arcane is minimaal, "zo betaalt niemand $6". Daan maakt ze veel sterker voor een 0.3.x. Aanmelden mag nu met het gratis deel.

**Wat dit is:** het eerste echte oordeel over het betaalde deel, van iemand die het product en de prijs ziet. Eén persoon, dus geen meting, maar wel de eigenaar en precies het moment waarop een koper beslist (GEZIEN, zijn bericht). Het bevestigt het risico dat ik op 7 nov al noemde: "alleen het uiterlijk is betaald, dan koopt meestal maar een klein deel".

**Voorstel (besluit blijft van Olaf):**
1. **De prijs blijft $6.** Het probleem is de waarde, niet het bedrag. Bij $3 houdt Dortus per Nederlandse koper ±$1,78 over (berekend zoals de tabel hierboven: $3 zonder de 21% btw erin is $2,48 ($3 / 1,21), min 5% + $0,50 + 1,5% over $3 is $0,70), en een skin die niemand wil, verkoopt ook voor $3 niet. Liever de skins de $6 waard maken, zoals Thijs vraagt.
2. **Niet verkopen zonder plaatje, wel eerlijk melden.** De koopknop in de plugin mag blijven: wie de skins in de instellingen ziet (de skin-tegels tonen de skin, volgens `platformen/obsidian/status.md`, klus 7) en ze toch wil, mag ze kopen, en een sleutel blijft geldig voor de nieuwe versie zolang Olaf dezelfde benefit in Polar houdt (GOK, de plugin controleert alleen die benefit-id). Maar in listing, lanceerberichten en productpagina geen reclame voor de skins tot de nieuwe er zijn. Zie winkeltekst (run 6) en lancering (run 6).
3. **De lanceerpiek niet verspillen.** De meeste aandacht komt in de eerste dagen na de aanmelding en de berichten (GOK, zo werkt elke lancering). Het betaalde deel is dan nog zwak. Daarom: de berichten verdelen over twee momenten, zie `lancering.md` (run 6): eerst het gratis deel (bereik), en de nieuwe skins als tweede bericht (geld). Advies 16.
4. **Wat de nieuwe skins moeten halen om $6 waard te zijn** (meetlat voor Daan, GOK op basis van wat spelers elders betalen): op één blik verschillend van Classic, ook in een klein lijstplaatje; elk een eigen gevoel bij de worp zelf (de crit en de fumble anders, niet alleen andere kleuren); en vergelijkbaar met een betaald dobbelpakket bij D&D Beyond ($1,99 per kleur tot $7,92 per set, DERDEN, zie hierboven), waar je ook voor een eigen uiterlijk betaalt. Twee skins voor $6 is dan $3 per stuk, in die band.

**Verwachting (GOK, bijgesteld):** in de eerste weken bijna geen verkopen (0 tot 5), want de skins zijn zwak en we maken er geen reclame voor. Daarna hangt het af van de nieuwe skins. De jaarverwachting van run 4 (±60 tot 700 verkopen) blijft de gok voor ná de nieuwe skins.

**Wat het meten verandert:** de meting op dag 30 (verkopen gedeeld door actieve gebruikers) zegt weinig als de nieuwe skins dan pas net uit zijn. Ik meet daarom ook vanaf de dag dat de nieuwe skins uitkomen: dag 7 en dag 30 na die update.
