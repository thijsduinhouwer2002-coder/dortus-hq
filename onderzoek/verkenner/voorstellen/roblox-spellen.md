# Voorstel: Roblox-spellen (experiences)

Vera, 9 nov 2026, run 12:31 (Amsterdam). Controleur akkoord met correcties (9, verwerkt; geld van 8 naar 7). Opdracht van Thijs (berichten/vera.md, 9 nov 12:00). Eerder mat ik op Roblox de Creator Store (plugins, cijfer 4) en UGC (avatar-items, cijfer 3); dit is de eerste meting van de spellen zelf.

## Kort
**Advies: nog niet klaar, maar serieus. Cijfer 5.**
Geld: het grootste en best aangetoonde geld van alles wat ik tot nu toe mat. Nieuw werk breekt echt door: 96 van de 98 spellen in Up-and-Coming zijn na 11 aug gemaakt, en 13 staan op een persoonlijk account (geen groep), waarvan 8 zonder spel van voor 2026, met 287 tot 17.911 spelers tegelijk. Of dat echt kleine makers zijn, is niet te bewijzen. Maar onder die top is het een loterij: in een willekeurige steekproef van 9.897 nieuwe universes van juni en juli (bijna allemaal lege plaatsen, 17 ooit bezocht) had na 4 tot 5 maanden niet één nog een speler. En het past slecht bij ons: we kunnen bouwen, publiceren en code testen zonder Roblox Studio, maar we kunnen niet zelf spelen en voelen of het leuk is, en publiceren voor kinderen vraagt een ID-controle, een borg van 1.000 Robux en 250 echte spelers van 16+. Een kleine proef kan, als Thijs dat wil.

## Hoe gemeten
- Ontdekpagina van Roblox, open API zonder inlog: `apis.roblox.com/explore-api/v1/get-sorts` en `get-sort-content` (Up-and-Coming, Top Trending, Top Playing Now, elk ±100 spellen). Daarna per spel `games.roblox.com/v1/games` (aanmaakdatum, bezoeken, spelers nu, maker), per groep `groups.roblox.com/v1/groups/<id>` (leden, eigenaar) en de groepen van die eigenaar, en per spel de game passes via `apis.roblox.com/game-passes/v1/universes/<id>/game-passes`.
- Willekeurige steekproef: 10.000 willekeurige universe-ID's tussen 10.300.000.000 en 10.500.000.000 (aangemaakt 10 juni tot 14 juli 2026, dus nu 4 tot 5 maanden oud), 9.897 bestonden.
- Zoeken: 25 gewone zoekwoorden (obby, tycoon, brainrot, horror, rng, enz.), 8 pagina's elk, via `apis.roblox.com/search-api/omni-search`: 4.617 spellen. Dit is scheef naar populaire spellen (zoeken toont eerst wat gespeeld wordt), dus alleen als aanvulling.
- Alles rustig gelezen (0,3 tot 0,5 s tussen verzoeken), alleen lezen.
- Bronnen van derden en regels: één onderzoeker, met links, zie onder.
- Scripts en data: `data/roblox-spellen-*-script.py` en `data/roblox-spellen-*-2026-11-09.json`.

## Cijfers

### Drukte (hoeveel nieuwe spellen)
- GEZIEN: universe-ID's lopen op met ±5,9 miljoen per dag (10,3 miljard op 10 juni, 10,5 miljard op 14 juli, 10,7 miljard op 14 aug 2026). Bijna allemaal zijn het lege plaatsen die Roblox automatisch maakt ("naam's Place").
- GEZIEN: van de 9.897 willekeurige universes uit juni en juli hadden er 17 ooit een bezoek, 2 meer dan 100 bezoeken (hoogste 527), en **0 hadden nu een speler**.
- GOK (doorgerekend uit die steekproef, grote marge): per dag ±10.000 nieuwe universes met minstens één bezoek en ruwweg 200 tot 4.000 met 100+ bezoeken. Het echte aantal "serieuze" nieuwe spellen per dag kan ik zo niet scherp meten; daarvoor is een steekproef van een paar honderdduizend ID's nodig (kan, kost ±2 uur rustig lezen).

### Bereik (komen nieuwe spellen en kleine makers boven)
- GEZIEN: van de 98 spellen in Up-and-Coming ("gepubliceerd in de laatste 28 dagen, gesorteerd op groei", tekst op de pagina zelf) zijn er 96 aangemaakt na 11 aug 2026; mediaan aangemaakt 17 okt. Spelers nu: mediaan 4.713, kwartielen ±1.780 en 9.310, laagste 287, hoogste 51.663.
- GEZIEN: van Top Playing Now (99 spellen, mediaan 19.313 spelers) zijn er 40 jonger dan 90 dagen; van Top Trending 78 van 97. De top ververst dus snel. DERDEN (IBTimes en Dexerto over RDC 2026, links onder): 28% van de top 100 en 33% van de top 1.000 op speeluren was in aug 2026 jonger dan 90 dagen.
- GEZIEN, wie de makers zijn: 85 van de 98 Up-and-Coming spellen staan op naam van een groep, 13 op een persoonlijk account. Groepen hebben mediaan 157.485 leden (kwartielen 34.541 en 479.356), maar dat zijn bijna altijd verse groepen per spel (spelers worden lid voor beloningen), dus dat zegt weinig over de maker.
- GEZIEN: bij 89 van de 98 is het oudste openbare spel van die groep of dat account van 2026; 81 hebben geen eerder spel met meer dan 1 miljoen bezoeken. Maar: bij 18 van de 85 groepen bezit de eigenaar nog een andere groep met 100.000+ leden en bij 23 bezit de eigenaar 5 of meer groepen. Studio's met eerdere hits zitten er dus zeker tussen, en een studio kan een nieuwe groep op een nieuw account zetten; "geen eerder spel" bewijst niet dat de maker klein is.
- GEZIEN, het sterkste signaal voor kleine makers: 13 spellen in Up-and-Coming staan op een persoonlijk account; 5 daarvan hebben al spellen van 2018 tot 2024 (onder meer Tiny Skies, 18 spellen sinds 2018, en Krillion, 28 spellen sinds 2019), 8 hebben geen spel van voor 2026 (onder meer "Net a Fish!" 17.911 spelers, "Flying Tesla Roadster" 5.470, "Tiny Skies" 4.476, "Ragdoll" 4.057, "Wacky Games" 3.247, "Zoo Builder" 1.666, "Krillion" 311).
- GEZIEN (zoekmeting, scheef naar populair): van 617 gevonden spellen van 3 tot 6 maanden oud hebben er nu 61 nul spelers, mediaan 34 spelers, 229 hebben 100+ en 69 hebben 1.000+. Dit zijn de spellen die zoeken nog laat zien, niet een gemiddeld nieuw spel.
- Conclusie bereik: wie de top haalt, haalt meteen duizenden spelers tegelijk; een gewoon nieuw spel haalt bijna niets. De mediaan na 4 tot 5 maanden van een gemiddelde nieuwe universe is 0 spelers. Het percentage dat 100+ bezoeken haalt is in de willekeurige steekproef 2 van 9.897, maar die steekproef zit vol lege plaatsen en zegt dus weinig over een spel dat echt gelanceerd wordt. Dat cijfer ontbreekt nog.

### Geld
- DERDEN (Roblox zelf, create.roblox.com/docs/production/monetization/developer-exchange): DevEx $0,0038 per verdiende Robux sinds 5 sep 2025, drempel 30.000 Robux (= $114), minimaal 13 jaar, geverifieerd e-mailadres, belastingformulier W-8 of W-9.
- DERDEN (Roblox, about.roblox.com/newsroom/2026/04/...increases-qualifying-devex-rate-42): sinds 8 juni 2026 $0,0054 per Robux voor aankopen van Amerikaanse spelers van 18+ met gecontroleerde leeftijd in "novel games".
- DERDEN (Roblox, create.roblox.com/docs/monetize-experiences): de maker houdt 70% van de Robux van een eigen game pass of developer product. Een pass van 179 Robux (de mediaan die ik mat) levert de maker dus ±125 Robux = ±$0,48 op.
- DERDEN (Roblox, create.roblox.com/docs/creator-rewards): Premium Payouts zijn sinds 24 juli 2025 vervangen door Creator Rewards (5 Robux per dag per "Active Spender" die 10+ minuten speelt; 35% van de eerste $100 van nieuwe of teruggekeerde spelers die jij naar Roblox brengt; eis: 60 dagen gemiddeld 100+ dagelijkse spelers).
- DERDEN (Roblox, nieuwspagina hierboven): in 2025 meer dan $1,5 miljard DevEx uitbetaald. DERDEN (IBTimes en Dexerto over RDC 2026, niet op een eigen Roblox-pagina gevonden): ±$1,7 miljard in de 12 maanden tot 30 juni 2026; ruim 42.000 makers kregen DevEx, mediaan ±$1.500 per jaar; top 1.000 gemiddeld $1,4 miljoen; top 10 samen bijna 40%.
- DERDEN (Roblox, corp.roblox.com/newsroom/2025/09/roblox-annual-economic-impact-report): over 2024 top 1.000 gemiddeld $820.000.
- GEZIEN: 90 van de 98 Up-and-Coming spellen verkopen game passes, mediaan 6,5 per spel, prijzen mediaan 179 Robux (kwartielen ±94 en 299).
- GOK: een spel met ±1.000 spelers tegelijk verdient een paar duizend dollar per maand; de bedragen uit de TikTok-reacties ($5.000 tot $10.000 voor "een spel van een dag") passen bij een spel dat de Up-and-Coming haalt, niet bij een gewoon nieuw spel. Niet te controleren.
- Conclusie geld: aantoonbaar groot, maar voor de meeste makers klein (mediaan ±$1.500 per jaar, en de 42.000 makers komen alleen uit de pers). Het grote geld zit bij weinigen.

### Vindbaarheid en advertenties
- DERDEN (Roblox, create.roblox.com/docs/discovery): een algoritme kiest per speler ±100 spellen voor de Home-pagina. Zwaarst telt: hoeveel mensen doorklikken en spelen, hoeveel er binnen 60 of 180 seconden weggaan (telt negatief), terugkomen op dag 1, 2 tot 7 en 8 tot 28, en speeltijd. Spelers via advertenties tellen niet mee voor de rangorde, maar brengen een spel wel in beeld. Een nieuw spel hoeft niet te wachten: de eerste signalen tellen meteen.
- GEZIEN: Up-and-Coming is volgens de pagina zelf "experiences published within the last 28 days sorted by user growth". De eerste weken zijn dus de kans.
- DERDEN (Roblox, create.roblox.com/docs/production/promotion/ads-manager): advertenties betaal je met een creditcard (18+) of met ad credits gekocht met Robux, met dag- of totaalbudget en een prijs per keer spelen (CPP).
- Niet gevonden: wat een keer spelen of 1.000 vertoningen nu kost. Dat ziet alleen wie in Ads Manager zit. Blogs noemen bedragen, maar niet betrouwbaar.

### Past het bij ons
- Bouwen zonder Studio kan, GEZIEN in de README van Roblox zelf (github.com/Roblox/place-ci-cd-demo): een spel als bestanden met Rojo, met `rojo build` een .rbxl maken, uploaden met de Open Cloud API en tests draaien met de Luau Execution API op de servers van Roblox, alles vanuit GitHub Actions. Rojo werkt met gewone bestanden en Git (README rojo-rbx/rojo). Lune draait Luau los op Linux. Dat past bij hoe we nu testen (regels: echte app via Actions).
- DERDEN (Roblox, create.roblox.com/docs/cloud/guides/usage-place-publishing): publiceren met een API-sleutel werkt alleen voor een place die al bestaat; één keer aanmaken gaat via Studio of de Creator Hub (Thijs, op Windows of Mac). Sommige onderdelen (onder meer SurfaceAppearance en PartOperation) gaan niet mee via de API.
- Wat we niet kunnen: zelf spelen. De Luau Execution API toetst code, geen gevoel, beeld of speelplezier. Bij een spel is dat het halve werk (de regel "opvallen, speciaal, mooi"), en het algoritme straft precies dat af (wie binnen 60 seconden weggaat, telt negatief). Daan kan schermafbeeldingen beoordelen als we een manier vinden om die te maken (bijvoorbeeld een speler die Thijs laat spelen); dat is nog niet uitgezocht.
- 3D-modellen en geluid: met gratis spullen uit de Creator Store of eenvoudige vormen; dat maakt "speciaal en mooi" lastig.
- Drempels om te publiceren, DERDEN (Roblox, create.roblox.com/docs/production/publishing/kids-and-select): voor spelers van 16+ een account van 2 dagen plus een leeftijdscontrole (gezicht of ID). Voor spelers onder 16 (en dat is het grootste deel) ook een ID-verificatie (maker 18+), tweestapsverificatie, de vragenlijst over inhoud, en 1.000 Robux borg (komt terug; bron: create.roblox.com/docs/production/publishing/publish-games-and-places#optional-fees) of 2 maanden Premium. Daarnaast eerst 250 keer spelen door actieve, geverifieerde spelers van 16+ binnen 60 dagen. Dat is allemaal werk van Thijs (ID, betalen) en dus voor `lijst-thijs.md`.

### Kinderen en eerlijk geld vragen
- DERDEN (Roblox, create.roblox.com/docs/production/monetization/paid-random-items): bij betaalde willekeurige items (eieren, prijswielen) moeten alle uitkomsten en exacte kansen vooraf zichtbaar zijn. Ouders kunnen uitgavenlimieten zetten (about.roblox.com/parental-controls).
- Ons voorstel als we het doen: alleen gewone game passes met een vaste, duidelijke prijs (bijvoorbeeld een extra werktuig of cosmetica), geen eieren of loterijen, geen "koop nu, alleen vandaag", geen betaalmuur die het spel onspeelbaar maakt. Het spel moet zonder betalen helemaal leuk zijn. Dat is eerlijker en past ook bij wat het algoritme beloont (terugkomen, niet afhaken).
- Een aparte nieuwe regel uit 2025 tegen misleidende betaalmuren vond de onderzoeker niet; nog na te lezen in de Community Standards voor we bouwen.

## Voordelen
- Het grootste aantoonbare geld van alle platformen die ik mat (meer dan $1,5 miljard per jaar aan makers volgens Roblox; 42.000 makers betaald volgens de pers).
- De top ververst snel: 40 van de 99 meest gespeelde spellen zijn jonger dan 90 dagen, 96 van de 98 in Up-and-Coming zijn na 11 aug gemaakt, en 13 staan op een persoonlijk account.
- Bouwen, publiceren en code testen kan zonder Studio, op Linux, met Roblox' eigen voorbeeld.
- Geld komt binnen in de winkel van Roblox zelf; geen eigen betaalsysteem nodig.

## Nadelen
- Een loterij: in de willekeurige steekproef had niet één nieuw spel van juni of juli nu nog een speler. Er komen per dag honderden tot duizenden nieuwe spellen bij (gok).
- We kunnen niet zelf spelen of voelen of het leuk is; een spel is nog meer dan een plugin een kwestie van gevoel.
- Veel stappen alleen voor Thijs (account, leeftijds- of ID-controle, tweestap, 1.000 Robux borg, belastingformulier, creditcard voor advertenties).
- Groeiende concurrentie van studio's en investeerders die spellen opkopen (DERDEN, Bloomberg via thestar.com.my, juli 2025).
- Het publiek is vooral kinderen; dat vraagt zorg bij elke betaalknop.
- Advertentieprijzen niet te meten van buitenaf.

## Eerste idee wat we zouden bouwen
Een klein, eerlijk spel in een genre dat nu groeit en dat met eenvoudige vormen kan (bijvoorbeeld een rustig verzamel- of bouwspel, zoals de spellen van een persoonlijk account "Net a Fish!", "Zoo Builder" of "Tiny Skies" in Up-and-Coming), met een duidelijke eigen draai, gratis helemaal speelbaar, 3 tot 6 game passes van 49 tot 299 Robux met een vaste inhoud. Gebouwd als Rojo-project in dortus-hq, getest met de Luau Execution API in Actions, gepubliceerd met Open Cloud. Eerste doel: de 250 geverifieerde spelers halen en zien of het in Up-and-Coming komt.

## Cijfer en advies
- Bereik: 5 (de top is open en ververst snel, ook voor solo makers, maar een gewoon nieuw spel haalt niets).
- Geld: 7 (groot en aantoonbaar, maar scheef verdeeld; voor ons hangt het geld van bereik af, en de cijfers over kleine makers komen alleen van derden).
- Past bij ons: 3 (bouwen en testen kan, spelen en mooi maken niet zonder Thijs, veel ID- en betaalstappen).
- **Totaal 5: nog niet klaar.** Wat er nog gemeten moet worden voor een ja:
  1. Hoeveel echt gelanceerde nieuwe spellen (met een eigen naam en minstens 100 bezoeken in de eerste week) na 3 maanden nog 10+ spelers hebben. Kan met een veel grotere steekproef (±300.000 ID's) of door Up-and-Coming een paar weken lang elke dag op te slaan en te volgen.
  2. Wat een keer spelen via Ads Manager kost (alleen te zien met een account, dus via Thijs).
  3. Of we het speelplezier kunnen laten toetsen (bijvoorbeeld Thijs speelt 10 minuten per versie, of een vriend).
- Als Hans het toch wil proberen: één klein spel als proef, met de stappen voor Thijs op zijn lijst. Kosten vooraf (1.000 Robux borg, die terugkomt) zijn geen reden om af te schieten.

## Shopify en YouTube (ook in de TikTok-reacties)
- Shopify: al grondig gemeten op 6 en 7 nov (`voorstellen/shopify.md`, cijfer 6, nog niet klaar; Thijs' gevoel dat bereik heel moeilijk is klopt). De reacties noemen Shopify-winkels (een eigen webwinkel met producten), niet Shopify-apps; dat is handel, geen app-platform. Niets nieuws.
- YouTube-kanalen: geen app-platform en geen plek voor een product van ons; de reacties zelf zeggen dat het weinig opleverde ("youtube was on the low end so I quit"). Niet gemeten.
- Handelsbots: overgeslagen, zoals Thijs vroeg.
- GEZIEN in de reacties (687 regels): 26 noemen Roblox, 6 Shopify, 10 YouTube.

## Bronnen
- Roblox docs: developer-exchange, monetize-experiences, creator-rewards, discovery, discovery-faq, ads-manager, usage-place-publishing, luau-execution, kids-and-select, paid-random-items (allemaal onder create.roblox.com/docs/).
- https://about.roblox.com/newsroom/2026/04/roblox-fuels-high-fidelity-games-over-18-players-increases-qualifying-devex-rate-42
- https://corp.roblox.com/newsroom/2025/09/roblox-annual-economic-impact-report
- https://www.ibtimes.co.uk/roblox-top-creators-devex-payouts-2026-1819403
- https://www.dexerto.com/roblox/robloxs-top-creators-average-65-7-million-a-year-but-most-make-far-less-3408675/
- https://www.thestar.com.my/tech/tech-news/2025/07/14/roblox-game-buying-frenzy-is-turning-teens-into-millionaires
- https://github.com/Roblox/place-ci-cd-demo (README), https://github.com/rojo-rbx/rojo (README), https://github.com/lune-org/lune (README)
