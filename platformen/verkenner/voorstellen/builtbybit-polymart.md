# Voorstel: BuiltByBit en Polymart (betaalde Minecraft-serverplugins)

Onderzocht door Vera, 7 nov 2026, run 09:31 UTC.

## Nagekeken
Controleur akkoord (7 nov), 7 correcties verwerkt. Alle cijfers nagerekend, 8 producten live nagekeken: kloppen exact.

## Kort
Advies: **nee**, cijfer **2**. Polymart (heet nu voxel.shop) is zelf gemeten en daar verdient een nieuwe betaalde plugin bijna niets: van 131 betaalde producten uit mei tot aug 2026 is de mediaan 0 downloads en heeft geen enkele er 50 (GEZIEN). BuiltByBit, de grootste winkel, is niet te lezen met curl (403, Cloudflare) en de API vraagt een sleutel. Daar is het geld dus niet gemeten. Op SpigotMC premium mat een hulpagent eerder mediaan 3 aankopen. Daarbovenop verbiedt de Minecraft-EULA letterlijk het verkopen van "mods", en plugins vallen daaronder. Drie winkels, hetzelfde beeld: geld bij een paar gevestigde makers.

## Cijfers

### Polymart / voxel.shop (eigen meting, GEZIEN)
- Bron: de open API `api.polymart.org/v1/getResourceInfo` per product, ids uit de sitemap (6.643 producten in totaal). Gemeten: alle 903 producten met id 8800 en hoger (aangemaakt vanaf 8 nov 2025 tot okt 2026; de 32 producten van 1 tot 8 nov 2025, waarvan 27 betaald, vallen erbuiten, controleur haalde ze live op). Data in `data/polymart-producten-sinds-nov2025-2026-11-07.jsonl`, scripts `data/polymart-haal-script.py` en `data/polymart-analyse-script.py`.
- Maat: "downloads". Bij een betaald product kan alleen een koper downloaden, dus downloads ≈ kopers (GOK: dubbel downloaden of downloads door de maker zelf zijn niet uit te sluiten, dus eerder te hoog dan te laag). Wel kan het te laag zijn als een maker ook buiten Polymart verkoopt (eigen Tebex of Discord), en downloads × prijs gebruikt de huidige prijs, zonder kortingen (GOK).
- **Betaald, 2 tot 6 maanden oud (mei tot aug 2026, n=131):** mediaan 0 downloads, 31% heeft er 1 of meer, 2% 10 of meer, 0% 50 of meer. Mediaanprijs $5. Bruto omzet (downloads × prijs): mediaan $0, beste 10% boven $28, beste product $277, alle 131 samen $1.494.
- **Betaald, 6 tot 12 maanden oud (nov 2025 tot apr 2026, n=458):** mediaan 1 download, 50% 1+, 5% 10+, 1 van de 458 met 50+. Beste product $623 bruto in ±10 maanden (VeloFlame PRO, 52 × $11,98). Alle 458 samen $6.965.
- Beste maker over het hele jaar: ±$1.260 bruto, verdeeld over meerdere producten (owner 66076). 249 verschillende makers zetten betaalde producten neer.
- **Gratis** ter vergelijking (nov 2025 tot apr 2026, n=230): mediaan 5 downloads, 7% 100+. Ook het bereik is dus klein.
- **Drukte:** ±110 tot 140 nieuwe producten per maand van nov 2025 tot mrt 2026, daarna 14 tot 83 per maand (GEZIEN). Mogelijk deels door producten die wachten op goedkeuring en niet in de sitemap staan (GOK). De controleur vond 7 van 12 ontbrekende ids op "waiting for review", ook uit nov 2025 (bijvoorbeeld 8911): wachten duurt soms bijna een jaar. Verwijderde producten zijn waarschijnlijk vooral flops, dus de cijfers zijn eerder te gunstig.
- Afdracht 2% (of vrijwillig 4% of 8%) plus betaalkosten, uitbetaling via Stripe of PayPal, verkoper regelt zelf btw (DERDEN, voxel.shop/merchant-agreement, door hulpagent gezien).
- Bestverkochte betaalde producten op de hele site: Nexo 4.366 downloads bij $22,99, ItemsAdder 2.649 (DERDEN, voxel.shop voorpagina, door hulpagent gezien). Dat zijn oude namen.

### BuiltByBit (niet zelf te meten)
- builtbybit.com geeft 403 met curl; de API (api.builtbybit.com) vraagt een sleutel van een account (GEZIEN: "Authorization header was not present").
- Afdracht 9,9% plus betaalkosten, uitbetaling via Tebex Wallet, minimumprijs $1,99 tot $5,99 (DERDEN, github.com/HytaleModding/site, publishing/builtbybit.mdx, en mclicense.org/blog/spigotmc-vs-polymart-vs-builtbybit).
- 730.000+ leden, 35.000+ producten, "$5,8 miljoen totale verkoop" (DERDEN, maar zwak: grokipedia.com/page/BuiltByBit, niet op BuiltByBit zelf gezien, datum onbekend). $5,8 miljoen over de hele looptijd (sinds MC-Market) is weinig per product.
- Makersverhalen met bedrag: Doomwen 3.000+ verkopen van $10 tot $20 (DERDEN, mclicense.org, reclame van een licentiedienst, startjaar onbekend). Draadtitels "Made $1,000+ in 2 Months" (een nagemaakte server-setup) en "Only 2 sales so far" (DERDEN, alleen de titel gezien). Geen enkele maker gevonden die na 2024 begon en een maandbedrag boven $300 deelt.
- Hoe meten als het moet: Thijs maakt een BuiltByBit-account en een API-sleutel, dan kan een run per product de aankopen lezen. Niet gevraagd, want de andere twee winkels en de EULA maken een ja onwaarschijnlijk.

### SpigotMC premium
- Eerder (7 nov run 08:31, hulpagent via de Spiget-API): 742 premium plugins uit de laatste twee jaar, mediaan 3 downloads, 17 met 100+. Niet door mij nagerekend.
- Geen afdracht, maximaal $19,99, licentiesystemen verboden (DERDEN, mclicense.org).

### Markt
- ±194.000 servers met bStats-plugins online op 7 nov 2026, 75% op Paper (DERDEN, bstats.org/global/bukkit, door hulpagent via de API opgehaald). Licht groeiend sinds 2025. Het publiek is er dus, maar het koopt weinig nieuws.

## Voor en tegen
Voor:
- Betalen in de winkel, lage afdracht (2% tot 9,9%).
- Groot publiek van servers, een plugin bouwen in Java kunnen we in 1 tot 2 weken.

Tegen:
- Een nieuwe betaalde plugin verkoopt bijna niets: mediaan 0 op Polymart, mediaan 3 op SpigotMC (GEZIEN en hulpagent).
- Het geld zit bij gevestigde namen (Nexo, ItemsAdder, MMOItems-uitbreidingen).
- **Juridisch:** de Minecraft-EULA (minecraft.net/en-us/eula) zegt over zelfgemaakte mods "as long as you don't sell them for money", en noemt plugins als mods (GEZIEN door de controleur, letterlijk op de pagina). Plugins worden al tien jaar openlijk verkocht zonder bekende handhaving, maar het blijft een risico voor de naam van Dortus.
- Bij elke Minecraft-versie bijwerken (nu 26.x).
- De grootste winkel (BuiltByBit) is zonder account niet te meten.

## Eerste idee (als het ooit toch zou gaan)
Een betaalde uitbreiding op een groot gratis plugin (zoals de MMOItems-uitbreidingen), met een gratis lite-versie op Modrinth of Hangar voor bereik. Maar ook die uitbreidingen halen hier maar 15 tot 35 kopers per jaar.

## Oordeel
Cijfer 2, nee. Bereik voor betaalde producten is bijna nul (mediaan 0 tot 1 koper), geld voor een kleine nieuwe maker is niet aangetoond (beste nieuwe product $623 bruto in 10 maanden), en de EULA maakt verkopen juridisch grijs.

Wat het oordeel zou veranderen: een eigen meting op BuiltByBit (met sleutel) waarin nieuwe betaalde plugins mediaan 10+ aankopen halen, of 2 makers die na 2024 begonnen en daar boven $300 per maand verdienen.
