# Voorstel: Foundry VTT (modules)

## Update 7 nov 2026 run 15:32: route (c), alleen buiten de officiële lijst

**Advies voor route (c): nee.** Cijfer 3. Het geld en bijna al het bereik lopen via de officiële lijst. Buiten de lijst vond ik geen maker die aantoonbaar meer dan een paar honderd dollar per maand haalt, en gratis modules buiten de lijst halen op de Forge minder bereik dan modules in de lijst (met weinig modules, dus niet hard), terwijl de Forge juist de plek is waar ze even goed te vinden zijn. Nagekeken door de controleur, akkoord, 7 correcties verwerkt. Thijs koos (c) na de AI-regels (bericht 7 nov 15:25). Hieronder de drie vragen.

### 1. Staan de twee grote makers in de officiële lijst? Ja, allebei.
- Alle 8 gecontroleerde modules van GlitchSmith (Cinematic Cut-ins, Landing Page Maker, Visual Novel Maker, Smartphone Widget, Stylish Action HUD, Stylish Shop, Unboxing the Mystery, GlitchSmith Library) en alle 8 van Wand & Widgets (MapForge, Exalted Scenes, Heavy Lore, Narrator's Jukebox, SessionFlow, The Stockpile, Mortal Needs, Your Flavor) geven 200 op foundryvtt.com/packages/<id> (GEZIEN, 16 van 16, ook 2 gratis modules van W&W).
- De pagina's staan als "Purchase: Publisher" en leggen uit hoe je installeert: "Link Patreon to your Foundry account, install MapForge from Add-on Modules" (GEZIEN, https://foundryvtt.com/packages/mapforge) en "a premium module available through GlitchSmith's Patreon" (GEZIEN, https://foundryvtt.com/packages/landing-page-maker). Bij Wand & Widgets is het dus de Patreon-koppeling van Foundry (GEZIEN). GlitchSmith verwijst voor installeren naar een eigen gids op Patreon; of dat de koppeling is, staat er niet (GOK), maar ook hij verkoopt als "Publisher" in de officiële lijst (GEZIEN). Hun geld loopt dus via de lijst.
- Ook de grootste verdieners theripper93 ($43.233), Moulinette ($8.337), MrPrimate en Baileywiki staan in de lijst (GEZIEN door de onderzoeker).

### 2. Makers alleen buiten de lijst die aantoonbaar verdienen? Bijna geen.
Gevonden door de onderzoeker (graphtreon, itch.io, Forge Bazaar):
- Loremaster (AI-spelleider, Jerry Chan): $90 per maand, 9 leden, sinds 17 dec 2025 (GEZIEN, https://graphtreon.com/creator/loremastervtt). Niet in de lijst (404, GEZIEN; stond er waarschijnlijk eerder in, GOK). Installeren met een GitHub-manifestlink. 19 Forge-gebruikers (GEZIEN).
- Mad Wizard (elizeuangelo): betaalde codemodules op de Forge Bazaar en itch.io (NPC Generator $7,99, Hero Points $3,99, Computers $7,99), niet in de lijst. NPC Generator: 294 Forge-gebruikers sinds mei 2024 (GEZIEN). Omzet onbekend, ruwe schatting honderden dollars per jaar (GOK). Let op: dezelfde maker heeft oudere gratis modules met duizenden gebruikers (Narrator Tools 2.656, Combat Music Master 1.215), dus hij had al publiek.
- Shattered Codex: $346 per maand, 92 leden, sinds okt 2025 (GEZIEN, https://graphtreon.com/creator/shatteredcodex). Betaalde modules via een eigen Download Hub met manifestlink, en zegt openlijk met AI te werken (GEZIEN, https://shattered-codex-wiki.pages.dev/ai-policy). Maar zijn gratis modules staan wel in de lijst (5 van 6 in de Forge-data geven 200, GEZIEN), dus geen zuiver geval van buiten de lijst.
- Blyghtmare (itch.io, $9,99, "AI Assisted, Code"): verkoopcijfers niet te zien.
- **Conclusie (GEZIEN, met beperking):** geen maker gevonden die alleen buiten de lijst zit en boven ±$300 per maand komt. Itch.io en Ko-fi tonen geen omzet, dus er kunnen er zijn die we niet zien.

**Eigen meting bereik (GEZIEN):** alle 3.038 modules uit de Forge-data met een eerste publicatie tussen mei 2025 en aug 2026 nagekeken op foundryvtt.com/packages/<id>: 2.422 in de lijst, 615 niet (404), 1 doorverwijzing. Forge-gebruikers (1 = 0,00136%):

| Groep | n | mediaan | 100+ |
|---|---|---|---|
| Gratis code (GitHub/GitLab), mei tot aug 2026, in lijst | 446 | 15 | 6% |
| idem, NIET in lijst | 23 | 9 | 4% |
| Gratis code, mei 2025 tot apr 2026, in lijst | 823 | 35 | 23% |
| idem, NIET in lijst | 63 | 18 | 10% |
| Betaald (Patreon of winkel-link), mei 2025 tot apr 2026, NIET in lijst | 236 | 1 | 0% (hoogste 12) |

- **Correctie controleur (belangrijk):** de tabel telt een 404 als "niet in lijst". Van de 86 gratis code-modules met 404 staan er 46 toch in de lijst onder een ander id (zelfde GitHub-repo, bijvoorbeeld deltagreen-ui als delta-green-player-ui, segue als foundry-vtt-segue; GEZIEN door de controleur, lijst in `data/foundry-404-ander-id-2026-11-07.tsv`). Echt buiten de lijst: 40. Daarvan mei tot aug 2026: n=6, mediaan 10,5, niemand 100+. Mei 2025 tot apr 2026: n=34, mediaan 14,5, 9% 100+ (GEZIEN, tegen 35 en 23% in de lijst). Ook de rij "ander" (kaarten, pakketten) wijst dezelfde kant op: niet in lijst n=208, mediaan 1, 1% 100+ (GEZIEN).
- Op de Forge zijn modules buiten de lijst even goed te vinden (de Bazaar toont ze gewoon), en toch halen ze minder. Met 6 en 34 modules is het verschil niet hard te maken, de richting wel. Dat er zo weinig echt buiten de lijst zitten (40 van ±900 gratis code-modules in anderhalf jaar) zegt zelf ook iets: bijna iedereen kiest de lijst (GEZIEN). Bij de ±85 tot 90% van de gebruikers die niet op de Forge zitten is het gat veel groter: het zoekscherm "Install Module" in Foundry toont alleen modules uit de officiële lijst, daarbuiten moet de gebruiker zelf een manifestlink plakken (DERDEN, https://foundryvtt.com/article/modules/: "a list of all available modules hosted on or approved to be part of the official Foundry VTT repository", anders "use the Manifest URL box"). Mijn schatting: buiten de Forge haalt een module buiten de lijst een fractie van het bereik (GOK, niet te meten zonder downloadtellers van GitHub, die hier 403 geven).
- Beperking: de groep "niet in lijst" is klein (23 en 63) en kan modules bevatten die er eerder in stonden en zijn weggehaald, of die minder goed zijn. De hoogste: art-for-daggerheart 464, phils-day-night-cycle 314 (GEZIEN).
- Betaald buiten de lijst op de Forge Bazaar: vrijwel niets, mediaan 1 gebruiker (vaak de maker zelf, GOK). Wel moet gezegd: betaalde modules via Patreon worden ook in de lijst op de Forge bijna niet geteld (98% nul), dus deze rij zegt vooral iets over Bazaar-verkoop.

### 3. Hoe reageert de gemeenschap op AI-modules?
- Zelf niet goed te meten: Reddit geeft vanuit deze omgeving 403, dus geen draadjes of scores (GEZIEN, onderzoeker).
- Foundry zelf koos de strengste regel van alle platformen die we bekeken: geen AI-tekst, beeld of "vibe coding" in de lijst, met permanente ban bij misleiden (GEZIEN, https://foundryvtt.com/article/ai-policy/). De Forge keurt sinds april 2023 geen AI-beelden meer goed voor verkoop; over AI-code zegt hij niets (GEZIEN, https://blog.forge-vtt.com/ai-and-the-forge/).
- Breder in de modwereld: oude makers noemen vibe-coded mods een "bullshit trend" (DERDEN, Eurogamer 4 okt 2026, via https://news.tyber.io/en/ai-models/vibe-coded-game-mods-go-viral-and-veteran-modders-are-fed-up/).
- Wie het openlijk doet, blijft klein: Shattered Codex ($346), Loremaster ($90), itch-items met "AI Assisted" (GEZIEN). Of dat door AI komt of door iets anders, weet ik niet.
- Als we het zouden doen, zetten we het open op de pagina (zoals Thijs vraagt). Dan verwacht ik dat een deel van de gebruikers, en mogelijk de Discord en Reddit, ons links laat liggen (GOK).

### Nog iets wat meetelt
- Artikel 1.2 geeft licentiehouders het recht om zelf te verspreiden ("As a Foundry VTT license holder, you retain the right..."), buiten de "official listing and marketplace", dus ook buiten de officiële winkel. Zelf uitgegeven werk moet wel aan de Foundry VTT Limited License for Package Development voldoen (GEZIEN, AI-regels). Een licentie kost $50 eenmalig (DERDEN); om te testen hebben we er toch een nodig.
- Op de Forge Bazaar verkopen kan zonder de officiële lijst: Creator worden per mail met bestaand werk, alleen eenmalige aankopen, 25% afdracht vanaf $3 (GEZIEN onderzoeker, https://forums.forge-vtt.com/t/getting-started-as-a-bazaar-creator/13205). Of AI-code daar mag, staat nergens.

### Cijfer route (c): 3, advies nee
- Geld: het bewijs van 7 nov (GlitchSmith, Wand & Widgets) gaat niet op voor route (c), want die makers verkopen via de officiële Patreon-koppeling. Buiten de lijst hoogstens een paar honderd dollar per maand.
- Bereik: bijna al het bereik loopt via de lijst. Het zoekscherm in Foundry toont alleen de lijst, bijna alle makers kiezen de lijst, en zelfs op de Forge halen modules buiten de lijst minder (kleine groep).
- Daarbij een gemeenschap die AI-werk wantrouwt. Dat maakt een open "met AI gemaakt" product nog zwaarder.
- Wat dit zou veranderen: een maker die aantoonbaar alleen buiten de lijst boven $300 per maand verdient (zoeken via itch.io-makers met graphtreon), of Foundry dat zijn AI-regels versoepelt. Tot dan Foundry op nee.

### Herhaalmeting
`data/foundry-lijst-analyse-script.py` met `data/foundry-forge-modules-2026-11-07.json` en `data/foundry-in-lijst-2026-11-07.txt` (per module de HTTP-code van foundryvtt.com/packages/<id>). Let op: vergelijk bij een herhaling op GitHub-repo, niet op id (zie `data/foundry-404-ander-id-2026-11-07.tsv`).

## Eerste meting 7 nov run 11:31 (route via de officiële lijst)

**Advies: nog niet klaar.** Cijfer 6. Onderzocht 7 nov 2026 run 11:31, eigen meting via de open API van de Forge Bazaar (9.360 modules) en graphtreon (23 Patreon-makers). Controleur akkoord, 7 correcties verwerkt.

Kort: het beste geldbewijs voor kleine makers van code tot nu toe, redelijk bereik, maar de AI-regels van Foundry botsen met hoe Dortus werkt. Of dat op te lossen is, kan alleen Thijs zeggen (zie lijst Thijs).

## Wat is het
Foundry Virtual Tabletop is software om rollenspellen (D&D, Pathfinder) online te spelen. Een licentie kost eenmalig $50 (DERDEN). Modules zijn JavaScript-uitbreidingen. Gratis modules staan in de officiële lijst op foundryvtt.com/packages. Betaald kan via de Patreon-koppeling van Foundry zelf: een maker zet modules in een Patreon-tier, de gebruiker koppelt Patreon aan zijn Foundry-account en installeert ze direct.

## Cijfers

### Geld
- **Makers van code-modules met een Patreon-pagina gestart in 2025 of 2026** (alle Patreon-makers die op de Forge Bazaar een module met een Patreon-link hebben en daar pas sinds 2025 staan, n=23, waarvan 10 met code-modules; cijfers GEZIEN via graphtreon.com, dat de cijfers van Patreon zelf toont):
  - GlitchSmith: $6.724 per maand, 1.046 betalende leden, pagina sinds okt 2025 (Cinematic Cut-ins, Landing Page Maker, Visual Novel Maker)
  - Gambit's Lounge: $4.163 per maand, 759 leden, sinds apr 2025 (FXMaster+, Gambit's Games). **Geen nieuwe kleine maker** (controleur): hij beheert FXMaster (±33.000 Forge-gebruikers, nummer 7 van alle modules) en had al Gambit's Premades sinds jan 2024. Telt hieronder niet mee.
  - Wand & Widgets: $3.465 per maand, 634 leden, sinds dec 2025 (MapForge, Exalted Scenes, Heavy Lore)
  - Origin Studios (reslinfvtt): $476 tot $2.000 per maand (schatting graphtreon), 272 leden, sinds jan 2026 (Dungeon Weave, The Bindery)
  - Designed by Nox: $308 per maand, 41 leden, sinds mrt 2025 (Crafting System, Advanced Item Recharge). Krap en dalend (-$20). Waarschijnlijk dezelfde persoon als ZeroXNoxus, kleine modules sinds 2023 (GOK op naam).
  - Lobowerewolf: $286 tot $2.000 (schatting), 207 leden, sinds mrt 2025 (Simple Bank, Backpack)
  - 3 Death Saves: $173 tot $1.000 (schatting), 125 leden, sinds feb 2026
  - Shadowdrake Creations: $74 tot $336 (schatting), 42 leden, sinds jul 2025
  - xvorob: $124, 37 leden, sinds mrt 2025
  - RNK (ragnaroks): $36, 16 leden, sinds okt 2025
  - Daarbuiten vond de hulpagent nog Shattered Codex: $346 per maand, 92 leden, sinds okt 2025 (GEZIEN graphtreon).
- **Samen: zonder Gambit zitten 4 van de 9 nieuwe code-makers boven ±$300 per maand (1 krap), 2 misschien. Twee daarvan (GlitchSmith, Wand & Widgets) zitten boven $3.000 en lijken echt nieuw: hun eerste module verscheen tegelijk met of na hun Patreon (nagekeken door de controleur, een eerdere naam kon niet worden uitgesloten).** De eis van Hans ("2 kleine makers gestart na 2024 boven $300 per maand") wordt gehaald, met makers van code, niet van kunst.
- **Let op, scheefheid (GOK):** dit zijn makers die het tot een Patreon-pagina én een Forge-vermelding brachten. Makers die een Patreon begonnen en niemand vonden staan er minder vaak in. Het echte aandeel is dus lager dan de helft. Ook kan "pagina sinds 2025" een maker zijn die al eerder gratis modules had (Wasp, DFreds, Gambit).
- **Afdracht (DERDEN):** Patreon houdt ±8 tot 12% plus betaalkosten. Foundry rekent via de Premium Content Agreement een "small fee", hoogte niet openbaar (https://foundryvtt.com/article/publisher-handbook/). Forge Bazaar: 25% bij producten vanaf $3 (https://forums.forge-vtt.com/t/bazaar-creator-faq/13711). Officiële winkel foundryvtt.store sinds feb 2025, afdracht niet gevonden.
- **Hoe groot is betaald (DERDEN, Foundry jaaroverzicht 2026, https://foundryvtt.com/article/year-in-review-2026/):** 2.138 van de 5.338 goedgekeurde modules zijn premium. De doorsnee gebruiker heeft 19 modules en geen premium inhoud, de gemiddelde gebruiker 2,47 stuks premium. Gebruik van de Patreon-koppeling +106% in een jaar (jaaroverzicht 2024). In de top 10 van Patreon-makers staan dit jaar twee nieuwe namen, GlitchSmith (5) en Gambit (10).
- **Concentratie (GEZIEN graphtreon):** theripper93 (Levels, 3D Canvas) haalt $43.233 per maand, veel bekende makers van gratis modules zitten onder $300 (Monk's $275, Kandashi $2). Geld komt bij een duidelijk betaald product, niet bij een donatieknop (GOK op GEZIEN).

### Bereik (GEZIEN, eigen meting)
- De Forge Bazaar (forge-vtt.com, een grote hostingpartij) geeft per module "installs": het percentage Forge-gebruikers dat hem heeft. De kleinste stap is 0,00136%, dus 1 gebruiker = 0,00136% en de noemer is ±73.500 Forge-gebruikers (GOK op GEZIEN: elke waarde is een veelvoud van die stap; de controleur rekende op alle 1.197 verschillende waarden 0,0013575%, noemer ±73.700).
- **Gratis code-modules (link naar GitHub; de controleur bekeek er 12, 11 waren echte code-modules, 1 een vertaling) uit mei tot aug 2026, 3 tot 6 maanden oud, n=462:** mediaan 14 Forge-gebruikers, p75 32, p90 68. 65% haalt 10+, 16% 50+, 5% 100+, 4% nul.
- Alle modules uit die maanden (n=858, ook kaartpakketten en premium): mediaan 5. Premium-modules tonen op de Forge vrijwel nul (87%), waarschijnlijk omdat ze via Patreon geïnstalleerd worden en de Forge ze niet telt (GOK).
- **Van Forge naar alle gebruikers (GOK):** 15,77% van alle Foundry-gebruikers host bij een partner, de Forge is daar één van (DERDEN, jaaroverzicht 2026). De Forge is dus hooguit ±10 tot 15% van alle gebruikers. Forge-gebruikers installeren meer modules dan gemiddeld: libWrapper staat op de Forge op 80,9%, bij alle gebruikers op 68,9%, FXMaster 45,4 tegen 29,1% (DERDEN, jaaroverzicht, via de controleur). Met factor 5 tot 10 komt de mediaan van een gratis code-module op **±70 tot 140 gebruikers** na 3 tot 6 maanden, **40 tot 65% haalt 100+** (dat is 10 tot 20 Forge-gebruikers: 65% haalt 10+, 40% haalt 20+), en de top 5% op 500 tot 1.000+ (alles GOK op GEZIEN). Vergelijk: Obsidian 213 tot 364, JetBrains 111.
- Grote nieuwe uitschieters bestaan: lib-item-select-dialog (jul 2025) ±4.000 Forge-gebruikers, seasons-and-stars (jun 2025) ±1.800, tabletop-rpg-music-filter (aug 2026) ±2.100 (GEZIEN).
- Niet gelukt: downloadtellers van GitHub-releases (geeft in deze omgeving 403 voor repo's buiten Dortus). Daarmee zou het totaal over alle gebruikers te meten zijn. Kan via de GitHub-API met een eigen sleutel.

### Drukte (GEZIEN)
- ±200 tot 240 nieuwe modules per maand op de Forge in 2026, was ±130 tot 160 in mid 2025. Officiële lijst: 5.338 modules, +38% in een jaar (DERDEN).

### Vindbaarheid (DERDEN en GOK)
- In Foundry zelf zoek je modules in een lijst bij het installeren; daarnaast de officiële pakketlijst, de Forge Bazaar, de Foundry-Discord (110.000+ leden), Reddit r/FoundryVTT en YouTube. Patreon-makers groeien vooral via video's en Discord (GOK).

### Past het bij ons
- Bouwen: JavaScript in de browser, vergelijkbaar met Obsidian. Een eerste module in 1 tot 2 weken kan (GOK).
- **AI-regels (GEZIEN, https://foundryvtt.com/article/ai-policy/, herzien 18 mrt 2026):** geldt voor de officiële lijst en de officiële winkel.
  - Alle vooraf geschreven tekst die de gebruiker ziet moet door een mens geschreven zijn, ook **UI-labels**, beschrijvingen en de marketingtekst. AI mag alleen helpen met proeflezen en opmaak.
  - Code mag met AI, maar de maker moet elk deel "understand, explain, modify, and maintain" en dat bij indienen verklaren. "Vibe coding" is verboden. Bij twijfel kan Foundry vragen het uit te leggen.
  - Ook beelden en geluid moeten door mensen gemaakt zijn. Vertalen met AI mag als een spreker van die taal het nakijkt.
  - De verklaring geldt bij indienen én bij elke update.
  - Niet naleven: de module wordt gearchiveerd of verwijderd. Misleiden over AI-gebruik: permanent van de lijst, herhaald te kwader trouw: levenslange ban.
  - De Patreon-koppeling valt onder de officiële kanalen: Patreon-premium staat op foundryvtt.com/creators (GEZIEN door de controleur, pagina Gambit's Lounge). Buiten de officiële kanalen mag je zelf uitgeven (manifest-link, of alleen de Forge Bazaar), maar dan is het bereik veel kleiner (GOK, niet gemeten).
- Voor Dortus betekent dit: Thijs zou de maker zijn die alle tekst in de module en op de pagina zelf schrijft, en die de code moet kunnen uitleggen, bij elke update opnieuw. Dat is werk voor Thijs en een risico voor zijn account. Daarom staat het op de lijst voor Thijs.
- Onderhoud: elke grote versie (V13, V14) breekt modules; een maand na V13 ondersteunde maar 16% die versie (DERDEN, jaaroverzicht 2025).
- Spelsystemen hebben eigen licenties (OGL, Paizo). Een module zonder systeemgebonden inhoud ontwijkt dat.

## Voor- en nadelen
Voor:
- Aantoonbaar geld bij nieuwe makers van code: 2 echt nieuwe makers sinds eind 2025 boven $3.000 per maand, 4 van 9 boven $300 (1 krap).
- Gebruikers zijn gewend te betalen via Patreon (2,47 premium per gemiddelde gebruiker), en de koppeling zit in Foundry zelf.
- Bereik van gratis modules redelijk (GOK ±70 tot 140), meetbaar via een open API.
- Techniek past bij wat we voor Obsidian al doen.

Tegen:
- De AI-regels vragen menselijke tekst en een maker die de code begrijpt. Dat is de kern van hoe Dortus werkt.
- Patreon is een abonnement: makers moeten blijven leveren, anders zeggen leden op (GOK).
- Elke grote Foundry-versie vraagt onderhoud.
- Geld zit bij een kleine groep; meer dan de helft van de nieuwe Patreon-makers uit de meting zit onder $300, en de meting is scheef naar makers die het al een beetje redden.

## Eerste idee (GOK)
Een systeemloze module voor de spelleider, in de lijn van wat nu verkoopt (scènes, sfeer, presentatie): bijvoorbeeld een "scène-regisseur" die muziek, licht, kaart en tekstvenster per scène in één klik wisselt. Gratis basis in de officiële lijst voor bereik, extra's via een Patreon-tier van $3 tot $5. Alle tekst in de module en op de pagina door Thijs.

## Wat er nog moet gebeuren voor een ja
1. Thijs zegt of hij de maker wil zijn volgens de AI-regels: alle tekst voor de gebruiker zelf schrijven (UI-labels, beschrijving, Patreon-pagina) en de code kunnen uitleggen, bij elke update. Ja, dan advies ja met cijfer 6 (7 als hij die rol echt op zich neemt en het tempo houdt). Nee, dan nee (cijfer 3), tenzij zelf uitgeven buiten de officiële lijst genoeg bereik blijkt te geven.
2. De weg buiten de officiële lijst (manifest-link, Forge Bazaar) meten.
3. Liefst: van GlitchSmith en Wand & Widgets nagaan of ze onder een andere naam al publiek hadden (GitHub-profielen gaven 403).

## Herhaalmeting
`data/foundry-haal-script.py` en `data/foundry-analyse-script.py` (Forge Bazaar), `data/foundry-patreon-graphtreon-2026-11-07.json` (makers).
