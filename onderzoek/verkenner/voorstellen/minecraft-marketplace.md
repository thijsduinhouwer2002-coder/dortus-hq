# Voorstel: Minecraft Marketplace (Bedrock)

Vera, 14 nov 2026, run 08:31 (Amsterdam). Nooit eerder gemeten; Noor noemde het op de radar ("alleen partners").

## Wat het is
De winkel in Minecraft Bedrock (Windows, telefoons, tablets, consoles). Spelers kopen met Minecoins werelden, skin packs, texture packs, mash-ups en add-ons. Sinds 2024 is er ook Marketplace Pass ($3,99 per maand, GEZIEN, https://www.minecraft.net/en-us/marketplace/marketplace-pass). Volgens derden is sinds 2017 meer dan $500 miljoen aan makers uitbetaald (DERDEN, corq.studio, 18 jun 2026).

## De poort: zelf erin kan nu niet, via een uitgever wel
- De partnerpagina zegt: "Even if we aren't accepting applications at this time", en de knop leidt naar een nieuwsbrief (GEZIEN, https://www.minecraft.net/en-us/partner, 14 nov 2026). Partners moeten "operate like a business" (GEZIEN).
- Dezelfde pagina wijst naar drie officiële uitgevers: "The best way to get your foot in the door ... is through our publishers" (GEZIEN). Dat zijn Pathway Studios (voor "independent creators", maker houdt rechten en prijs, uitgever neemt "a small percentage"), Waypoint Studios (aanmelden met portfolio, verdeling per afspraak) en BLOCKLAB Studios (noemt 12 studio's die via hen later zelf partner werden) (GEZIEN door de onderzoeker op hun sites; pathway.studio gaf mij met curl geen tekst).
- **De poort is smal.** Waypoint nam in juli 2026 7% van 205 aanmeldingen aan; 90% van de afwijzingen ging over de kwaliteit van het portfolio (GEZIEN door de controleur, waypointstudios.com/blog/inside-our-creator-applications-july-2026). Hun formulier eist 18+, niet ook bij een ander bedrijf publiceren, en "everything provided ... is the product of my own work or the work of my team/company" (GEZIEN door de controleur, waypointstudios.com/apply). Pathway is van ReWrite Media Inc.; een percentage noemen ze niet. BLOCKLAB maakt vooral skin packs (465) en weinig add-ons (16).
- Of je een bedrijf moet zijn staat bij geen van de drie en nergens openbaar; het hoofdcontract is niet openbaar (GEZIEN, 404). Via een uitgever tekent Thijs een contract met de uitgever, niet met Microsoft (GOK).
- Verdeling: maker ±70%, Microsoft ±30%, door Microsoft niet gepubliceerd (DERDEN, corq.studio en minecraftpal.com). Daar gaat het deel van de uitgever nog af. Uitbetaling per kwartaal (DERDEN, zwakke bron).
- Waarde: 320 coins ±£1,99 (DERDEN). Mediaanprijs in mijn steekproef 310 coins voor een skin pack, 660 coins voor een add-on (GEZIEN). Een add-on van 660 coins brengt de maker grofweg $2 tot $3 per verkoop, vóór het deel van de uitgever (GOK).

## Eigen meting (GEZIEN)
Bronnen:
- De officiële sitemap van minecraft.net (in robots.txt genoemd): **38.009 productpagina's van 328 makers**, mediaan 38 items per maker. Grootste: Giggle Block Studios 1.048, Goe-Craft 1.044, House of How 813 (`data/minecraft-marketplace-makers-sitemap-2026-11-14.txt`). Persona-items (losse kledingstukken) zitten daar niet in.
- Per item kon ik minecraft.net zelf niet lezen: de cijfers komen uit een interne API, en de pagina in een browser openen werd door de veiligheidscontrole geweigerd. Terecht, niet omzeild.
- Wel leesbaar: MinecraftPal, een openbare tracker die per item de ratings, prijs, soort en datum van eerste publicatie toont (robots.txt staat `/marketplace/item/` toe, verbiedt alleen `/api` en accountpagina's). Alle 38.008 officiële items staan daarin. Ik haalde een **willekeurige steekproef van 4.500 items** (12% van de winkel), rustig, 3 tegelijk, plus alle 780 items van Razzleberries (`data/minecraft-marketplace-steekproef-4500-2026-11-14.jsonl`, scripts `data/minecraft-pal-haal-script.py` en `data/minecraft-pal-analyse-script.py`).

Ratings zijn geen verkopen. Hoeveel verkopen bij een rating horen is onbekend; zie onder.

**Ratings per item, naar jaar van eerste publicatie:**

| Jaar | Items in steekproef | Geschat in winkel | Mediaan ratings | 100+ | 500+ |
|---|---|---|---|---|---|
| 2020 | 532 | ±4.500 | 96 | 49% | 17% |
| 2022 | 887 | ±7.500 | 30 | 21% | 7% |
| 2023 | 790 | ±6.700 | 26 | 21% | 7% |
| 2024 | 533 | ±4.500 | 43 | 30% | 13% |
| 2025 | 293 | ±2.500 | 27 | 27% | 9% |
| feb t/m jul 2026 (3,5 tot 9,5 maanden oud) | 162 | | 14 | 17% | 2% |

- Drukte: het aantal nieuwe items daalde van ±7.500 per jaar (2021, 2022) naar ±2.500 in 2025, maar **2026 is al hoger dan heel 2025**: 332 items in de steekproef tot half nov, ±2.800 geschat, met drukke maanden aug t/m okt (42, 62 en 37 in de steekproef) (GEZIEN, gevonden door de controleur). MinecraftPal telt met persona-items 14.853 (2023), 13.248 (2024), 10.481 (2025) (DERDEN). Het aanbod is dus niet meer aan het dalen.
- **Gratis items.** 93 items in de steekproef hebben geen prijs: dat zijn gratis items van Mojang en grote partners, vaak met tienduizenden ratings (Starfish "Another Furniture" 470.366). MinecraftPal noemt 976 gratis items (DERDEN). In de eerste versie telde ik die mee; de controleur zag het. Hieronder staan alleen betaalde items.
- **Soort maakt het verschil.** Betaalde items van jan 2025 t/m jul 2026 (n=468):

| Soort | Aantal | Mediaan ratings | 100+ | 500+ |
|---|---|---|---|---|
| Add-on | 71 | 104 | 51% | 11% |
| Wereld | 52 | 20 | 19% | 4% |
| Skin pack | 312 | 14 | 14% | 2% |
| World skin pack | 26 | 34 | 19% | 0% |
| Resource pack | 7 | 468 | 71% | 43% |

- Betaalde items van feb t/m jul 2026, alle soorten: n=160, mediaan 13,5 ratings, 56% 10+, 16% 100+ (GEZIEN).

- **Makers met weinig items doen niet onder voor grote.** Betaalde add-ons van jan 2025 t/m jul 2026 van makers met minder dan 50 items, zonder bekende merken en servers (Galaxite, Lunar Client, Blockworks, Oreville, Starfish): n=20, mediaan ±131 ratings (controleur). Let op: "weinig items" is niet altijd klein of nieuw; er zitten ook jarenlange partners tussen (Ambient Creations, Vatonage). Kleine aantallen, maar geen teken dat alleen de grote studio's verkopen.
- **Nieuwe makers komen er nog bij.** In de steekproef zijn 36 makers (met 5+ items in de winkel) waarvan het eerste item na jul 2024 kwam. Een deel zijn bekende namen (Lofi Girl, Maizen, Aypierre, Lunar Client, Galaxite), maar ook onbekende kleine studio's met goede add-ons: Hog5kull (6 items, add-on 580 ratings), Cubical (16, 533), Doctor Benx (19, 410), Owls Cubed (31, 354), A Foxy Toast (17, 163), Block Studios (10, add-on van feb 2026 147), Simply Brilliant (5, add-on van mei 2026 115) (GEZIEN).

**Van ratings naar geld (GOK, met onderbouwing):**
- Razzleberries heeft "over three million sales" (DERDEN, corq.studio, jun 2026; de controleur kon de bron niet openen (403) en vond niet wanneer het getal genoemd werd). Hun 780 items hebben samen 766.446 ratings, maar 370.855 daarvan (48%) komen van 14 gratis items; de betaalde items hebben 395.591 ratings (GEZIEN). Gaat de 3 miljoen over betaalde verkopen, dan is het ±7,6 verkopen per rating; tellen gratis downloads mee, dan ±4. Ik reken met 4 tot 8. Een betere bron vond niemand. Dit is de zwakste schakel van de meting.
- Een betaalde add-on uit 2025 of 2026 met de mediaan van ±104 ratings is dan ±420 tot 800 verkopen, bij 660 coins ±$800 tot $2.400 voor de maker in ±1 jaar, dus ±$70 tot $200 per maand, vóór het deel van de uitgever. Een add-on met 500+ ratings (11%) is ±2.000 tot 4.000 verkopen.
- Prijzen zijn gelezen op 14 nov; een deel kan een tijdelijke saleprijs zijn (bijvoorbeeld een add-on van Owls Cubed op 160 coins).
- Een skin pack met de mediaan van 14 ratings is ±60 verkopen bij 310 coins: ±$80. Skin packs zijn voor ons dus niets; add-ons wel.
- Hoe makers uit Marketplace Pass betaald worden is niet openbaar (DERDEN).

## Vindbaarheid
Spelers vinden items in de winkel in het spel: uitgelicht door Mojang, zoeken, sale, en de Pass (DERDEN, niet gewogen). Er is geen eigen reclame nodig om op de lijst te komen; ratings van nieuwe add-ons laten zien dat ze gevonden worden. Waypoint verkoopt "store optimization" als dienst, dus zichtbaarheid is werk (GOK).

## Past het bij ons
- **Bouwen:** add-ons zijn JSON plus JavaScript (Script API), modellen in Blockbench of Blender. Dat past goed bij de ploeg. De Bedrock Dedicated Server draait officieel op Ubuntu (GEZIEN, https://www.minecraft.net/en-us/download/server/bedrock), dus scripts en gedrag kunnen in de cloud getest worden. bridge. (open source editor) werkt in de browser (DERDEN).
- **Zelf spelen en kijken:** de Bedrock-client heeft geen Linux-versie; echt in het spel kijken vraagt een Android-tablet, iPad, console of Windows (GOK). Dat moet Thijs dan doen of kopen.
- **Indienen:** via een uitgever dient de uitgever in (DERDEN, Waypoint).
- **AI:** er is geen openbaar AI-beleid van Microsoft voor Marketplace-content gevonden; Mojang zegt zelf geen generatieve AI te gebruiken (DERDEN). Maar het formulier van Waypoint vraagt dat alles "eigen werk" is. Dat is een concreet risico voor modellen, plaatjes en teksten die met AI gemaakt zijn, niet alleen een onzeker punt. Als we het doen, verstoppen we het niet.
- **Publiek:** veel kinderen en tieners (43% is 15 tot 21, DERDEN). Eerlijke prijzen, geen misleidende beschrijvingen.

## Tegen de lat van een 8
1. Nieuwe kleine makers verdienen er nu: **half**. Betaalde add-ons: 51% 100+ ratings, mediaan ±$70 tot $200 per maand vóór het deel van de uitgever, 11% duidelijk meer. Skin packs en werelden nee.
2. Bereik zonder eigen reclame: **ja**, de winkel in het spel brengt kopers.
3. Wij kunnen bouwen en testen: **grotendeels**, code en gedrag op Linux, maar zelf in het spel kijken vraagt een toestel.
4. Thijs kan binnen een week verkopen: **nee**. Direct aanmelden is dicht; via een uitgever vraagt een sterk portfolio (Waypoint nam 7% aan) en een contract, volgens Waypoint-makers zo'n 3 maanden tot de winkel (DERDEN).

## Cijfer en advies
**Cijfer 5. Advies: nog niet klaar.** (Eerste versie zei 6 en ja als proef; de controleur vond dat te optimistisch na het weghalen van de gratis items en met de 7% aanname. Ik ben het met hem eens.)
- Waarom wel het bekijken waard: van de winkels voor Blender-achtig werk die we maten (Superhive 3D-modellen, Thangs, Second Life, RPG Maker) is dit de enige waar betaalde add-ons van makers met weinig items in 2025 en 2026 nog vaak honderden kopers halen, terwijl het aantal nieuwe items per jaar veel lager ligt dan in 2021 en 2022.
- Waarom maar een 5: twee van de vier punten van een 8 (bereik ja, bouwen grotendeels), geld per add-on bescheiden, de poort smal (uitgever, 7% aanname, portfolio, maanden), de eis van eigen werk tegenover onze AI-werkwijze, en de onzekere omrekening van ratings naar verkopen. Uitbetaling loopt ook via de uitgever, met een contract onder buitenlands recht.
- Als Hans het toch wil proberen: één gratis add-on met Gloop of een ander eigen figuur uit Het Hol (eigen mobs met gedrag, Blender of Blockbench-modellen, Script API) als portfolio, dan aanmelden bij Pathway Studios. Eerst eerlijk uitzoeken of de uitgever werk met AI-hulp accepteert, en dat open melden. Thijs moet dan het aanmeldformulier invullen en later een contract tekenen (pas na ja van Hans op `organisatie/lijst-thijs.md`), en een goedkoop Android-toestel of iPad regelen om in het spel te kijken.

## Wat nog gemeten kan worden
- Een beter getal voor verkopen per rating (een maker die verkopen en ratings van één item noemt).
- De voorwaarden van Pathway en Waypoint (percentage, eisen aan de maker, AI met hulp), door ze te mailen; dat kan alleen via Thijs. Accepteren ze werk met AI-hulp open, dan opnieuw wegen.
- Herhaalmeting rond 14 feb 2027: dezelfde 4.500 items opnieuw halen met `data/minecraft-pal-haal-script.py` en kijken hoe hard de lichting feb t/m jul 2026 groeit.
