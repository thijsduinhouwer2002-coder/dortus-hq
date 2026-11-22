# Voorstel: Autodesk Design and Make Marketplace (vroeger Autodesk App Store)

**Advies (bijgewerkt 9 nov run 03:31): nee voor nu.** Cijfer 3 (was 4, nog niet klaar). Reden: de reviews zijn nu wel gemeten (alle 18.159, via de winkel-API) en laten zien dat er in deze winkel heel weinig gebeurt, zeker bij betaalde apps van nieuwe makers. Zie het blok "Vervolg 9 nov" hieronder. Onderzocht 7 nov 2026 run 15:32, eigen meting van alle 5.055 apps uit de openbare sitemap (marketplace.autodesk.com, robots.txt staat dat toe) plus een onderzoeker voor het geld. Controleur: eerst niet akkoord (betaald-telling en prijzen fout), na 7 correcties akkoord bij herkeuring.

Kort: de voorwaarden zijn de beste die we tot nu toe zagen (0% afdracht, kopers zijn bedrijven, 41% van de apps vraagt in de winkel geld), maar bereik en verkoop zijn van buitenaf niet te zien, en ik vond geen enkele kleine maker die aantoonbaar via deze winkel verdient.

## Vervolg 9 nov 2026 (run 03:31): reviews gemeten
Thijs noemt het lezen van de winkel-API van Autodesk nu in zijn vaste toestemming. Rustig gelezen, alleen lezen.

**Bron (GEZIEN):** de winkel haalt zijn cijfers uit `developer.api.autodesk.com/ngappapi/public/`, zonder inlog. Gevonden door de netwerkverzoeken van een app-pagina in Playwright te bekijken. Gebruikt: `apps/comments/batch-rating-summary?appIds=...` (50 per verzoek, 102 verzoeken voor alle 5.058 apps uit de meting van 7 nov) en `apps/<id>/comments?limit=50&offset=...` (per review: sterren, datum, "geverifieerde download"). Downloads of verkopen geeft de API niet.

**Uitkomst (GEZIEN, eigen meting, alle apps):**
- In totaal 18.159 reviews op 5.058 apps; 45% van de apps heeft er minstens 1. Na ontdubbelen (dezelfde app staat soms per product of taal apart met dezelfde reviews) 14.588 reviews op 4.833 apps.
- **Hele winkel samen ±2.000 tot 2.300 reviews per jaar** (2021 tot 2025), ±150 tot 220 per maand. Daarvan op betaalde apps maar ±270 tot 410 per jaar (2023 tot 2025: 360 tot 410), ±30 tot 40 per maand, verdeeld over ±2.000 betaalde apps. Deze jaar- en maandtellingen zijn niet ontdubbeld; ontdubbeld ligt het ±20% lager.
- **Rond de overstap naar de nieuwe winkel stonden reviews stil:** van 7 mei tot 20 juli 2026 staat er geen enkele review in de data, ook live in de API niet (de app met 808 reviews springt van 3 mei naar 3 aug; controleur). Waarschijnlijk kon niemand reviewen tijdens de overstap (GOK). Mei (108, waarvan 78 op 3 mei) en juli (69, in 11 dagen) zeggen daarom weinig. Daarna: aug 133, sep 137, okt 272. Okt is opgeblazen door één maker (Trisita Engineering, 4 Revit-apps die eind sep en begin okt verschenen): 138 reviews op 29 en 30 okt, allemaal 5 sterren (plus één van 1 ster op 8 nov). Zonder Trisita okt 134. **Aug tot okt ±135 per maand tegen ±200 in 2025:** de nieuwe winkel heeft het oude niveau nog niet terug.
- **Best beoordeelde betaalde app ooit: 55 reviews** (TracianCAD, Fusion, $39,99 per jaar, sinds 2020). Ter vergelijking: de top gratis app heeft 808.
- **Nieuwe apps (reviews per app, ontdubbeld, 1+ = minstens één review):**

| Leeftijd (eerste uitgave) | Soort | Aantal | Mediaan | 1+ | 5+ | 10+ |
|---|---|---|---|---|---|---|
| 3 tot 6 maanden | betaald, kleine maker (max 3 apps) | 29 | 0 | 10% | 0% | 0% |
| 3 tot 6 maanden | betaald, maker met 4+ apps | 76 | 0 | 7% | 0% | 0% |
| 3 tot 6 maanden | gratis of alleen proef | 137 | 0 | 16% | 4% | 1% |
| 6 tot 12 maanden | betaald, kleine maker | 31 | 0 | 29% | 6% | 0% |
| 12 tot 18 maanden | betaald, kleine maker | 28 | 0,5 | 50% | 14% | 7% |
| 12 tot 18 maanden | betaald, maker met 4+ apps | 112 | 0 | 21% | 0% | 0% |

- Betaalde apps met een review in de laatste 12 maanden: 167 (van ±2.000). Zonder Trisita heeft de beste er 11 (TracianCAD). Kleine makers sinds 2024 met 5+ reviews op een betaalde app: 9 makers, de beste WiseBIM (18, $49 per maand), Mohamed Eissa (11, $20 per maand), Almaz (10, Civil 3D, $10 per maand).
- "Geverifieerde download" betekent dat de schrijver de app downloadde, ook een proef of gratis versie; het is geen bewijs van aankoop (GOK op basis van de naam, niet nagegaan).

**Wat dit zegt (GOK):** hoeveel kopers bij één review horen weten we niet; de onderzoeker vond geen maker die downloads en reviews naast elkaar zet. Neem willekeurig aan dat één op de 50 kopers een review schrijft: dan zijn ±30 tot 40 reviews per maand op alle betaalde apps samen ±1.500 tot 2.000 verkopen per maand voor de hele winkel (bij één op de 200: 6.000 tot 8.000), verdeeld over 2.000 betaalde apps. Bij een mediaan van $25 eenmalig of $60 per jaar blijft daar voor een nieuwkomer weinig van over. Dat past bij wat de onderzoeker vond: geen enkele kleine maker deelt een bedrag (Indie Hackers, TrustMRR, Reddit, blogs; forums.autodesk.com en aps.autodesk.com niet leesbaar, 403 en 406), en een R&D-lead op r/Revit zegt dat betaalde plugins vooral van bedrijven komen (DERDEN, https://redlib.reallyaweso.me/r/Revit/comments/1ibnyql/question_for_developers/m9mvrkz/).

**Data en scripts:** `data/autodesk-reviews-script.py` (samenvattingen, ±2 minuten), `data/autodesk-comments-script.py` (alle reviews, 4 tegelijk, ±8 minuten; limit mag maximaal 50), `data/autodesk-reviews-analyse-script.py` en `data/autodesk-reviews-tijd-script.py`. Ruwe data: `data/autodesk-ratings-2026-11-09.json` en `data/autodesk-reviews-2026-11-09.jsonl` (zonder namen).

**Controleur:** akkoord na 5 correcties (stilstand mei tot juli in plaats van inzakking, betaald per jaar 270 tot 410, tellingen niet ontdubbeld, Trisita 138 plus 1, rekensom met 1 op 200). Alle andere getallen en de tabel zelf nagerekend.

**Wat het advies nog kan veranderen:** komt het aantal reviews in de nieuwe winkel boven het oude niveau (meer dan ±250 per maand zonder uitschieters van één maker, 3 maanden op rij), bijvoorbeeld door de zoekfunctie van Autodesk Assistant, dan opnieuw wegen. Herhaalmeting begin feb 2027 met dezelfde scripts.

## Wat is het
De winkel voor uitbreidingen op AutoCAD, Revit, Fusion, Civil 3D, Inventor en meer. In april 2026 vervangen door de Design and Make Marketplace; apps.autodesk.com stuurt door (DERDEN, https://blog.autodesk.io/design-make-marketplace/).

## Cijfers

### Drukte (GEZIEN, eigen meting)
- 5.055 apps in de sitemap (3 pagina's gaven een fout). Eerste uitgave per jaar: 2023 458, 2024 513, 2025 651, 2026 tot nu 979.
- Nieuwe apps per maand: 2025 ±40 tot 90, 2026 eerste helft 55 tot 90, daarna 130 (aug), 139 (sep), 158 (okt); nov tot nu 50 (een week). Snelle groei sinds de nieuwe winkel en, denk ik, AI-hulp bij bouwen (GOK).
- Van aug tot nu: 477 nieuwe apps van 251 makers, 185 makers met precies 1 app. Veel makers met 1 app. Maar ook bedrijven met reeksen (Todor Latev 52 sinds nov 2025, Piping Content 25, ProtoTech 24).
- Producten bij nieuwe apps sinds nov 2025 (n=1.070): Revit 435, Fusion 205, Civil 3D 159, Plant 3D 151, AutoCAD 133.
- Nieuw: 10 apps van de soort "MCP" sinds aug (GEZIEN).
- Let op: de sitemap toont alleen apps die nu online staan. Weggehaalde apps tellen niet mee, dus oude jaren lijken kleiner (GOK).

### Geld
- **Afdracht 0%** (Publisher Agreement, bijgewerkt 3 mei 2026: "has set a commission rate of 0.0%", mag Autodesk wijzigen; GEZIEN door de controleur, https://apps.autodesk.com/Content/pdf/Publisher.pdf). De commissie geldt op de "net fee", dus na de kosten van de betaaldienst die Autodesk aanwijst; die kosten betaalt de maker. Volgens de makerspagina's is dat PayPal (DERDEN, https://aps.autodesk.com/marketplace/publisher-center). Btw en terugbetalingen doet de maker zelf (artikel 3 en 20.10).
- **Prijsvormen (GEZIEN, alle apps):** 2.054 van 5.055 apps (41%) zijn echt te koop in de winkel (eenmalig, maand- of jaarabonnement, of een bedrag boven 0). Plannen: gratis 1.836, eenmalig 1.308, onbeperkte proef 1.159, jaarabonnement 736, proef 30 dagen 581, maandabonnement 552, Autodesk-abonnement 76. Een app met alleen "onbeperkte proef" toont alleen "Start free trial" zonder prijs: de licentie loopt buiten de winkel (GEZIEN door de controleur). Nieuwe apps sinds nov 2025: 449 van 1.070 (42%) echt betaald, 211 alleen proef. Mediaanprijs bij nieuwe apps (USD, boven 0): eenmalig $25 (n=311), per maand $8 (n=111), per jaar $60 (n=135).
- **Verkoop: niet te zien.** Geen downloads, geen gebruikers, geen verkopen op de pagina's. Reviews worden pas in de browser geladen via een interne API; die heb ik niet gebruikt (de veiligheidscontrole hier weigerde dat, terecht).
- **Kleine makers met cijfers: niet gevonden** (onderzoeker). Een R&D-lead op r/Revit (jan 2025): "Most for sale plugins are developed by third party app developers (companies), not individuals" (DERDEN, via een Reddit-spiegel). Twee Indie Hackers-titels die mogelijk over AutoCAD-plugins gaan ("$150k/yr product", "10k all time revenue") konden niet gelezen worden (botcheck), dus tellen niet.
- Revit-tools verkopen wel bij bedrijven: DiRootsOne Premium €100 per gebruiker per jaar (DERDEN, https://diroots.com/revit-plugins/dirootsone/), maar dat is een bedrijf.

### Bereik
- Niet te meten. Er is geen sortering op populariteit in de winkel (gebruiker op r/Fusion360, mei 2026, DERDEN). Totaalcijfer alleen oud: 3 miljoen downloads in dec 2017 (DERDEN, https://blog.autodesk.io/autodesk-app-store-surpasses-3-million-downloads/).

### Vindbaarheid (DERDEN en GOK)
- Sinds 27 aug 2026 zoekt Autodesk Assistant in de winkel in gewone taal en vergelijkt apps op prijs en reviews (DERDEN, https://aps.autodesk.com/node/4051). Dat kan een nieuwe, eerlijke ingang zijn voor nieuwe apps (GOK).
- Kopers zijn vaak BIM-managers bij bureaus die meerdere licenties kopen (GOK).

### Past het bij ons
- Revit- en AutoCAD-plugins zijn C# (.NET) op Windows; testen in de echte app kan niet op GitHub Actions zonder Autodesk-licentie (GOK, niet nagegaan). Dat is een groot verschil met Obsidian en JetBrains.
- Fusion-add-ins kunnen in Python of C++. Een web-app of MCP-server kan zonder desktop.
- Een gewone desktop-plugin heeft geen kosten voor Autodesk Platform Services (DERDEN, getting-started).

## Voor- en nadelen
Voor: 0% afdracht; kopers zijn bedrijven met budget; betalen, proef en abonnement zitten in de winkel (41% van de apps gebruikt dat); nieuwe AI-zoekfunctie.
Tegen: verkoop en bereik niet te zien; 185 makers met 1 app sinds aug is vooral drukte; geen bewijs dat kleine makers verdienen; drukte verdubbelt in een paar maanden; bouwen en testen vraagt Windows en een dure licentie (Revit ±$3.000 per jaar, GOK).

## Eerste idee (GOK)
Een Revit-hulpmiddel voor BIM-managers (bijvoorbeeld controle van naamgeving en parameters met een rapport), of een MCP-server die Revit-gegevens leesbaar maakt voor AI, met 30 dagen proef en een jaarabonnement.

## Wat er nog moet gebeuren voor een ja
1. Reviews per app tellen (de enige zichtbare maat voor gebruik): kan met de browser van Thijs, of als Thijs toestemming geeft om de openbare API achter de winkel te lezen. Dan een steekproef van nieuwe apps sinds 2025.
2. Twee kleine makers vinden die een bedrag delen (Indie Hackers met browser, LinkedIn).
3. Nagaan of testen zonder betaalde Revit kan (een proeflicentie of de Revit-API in een test).

## Herhaalmeting
`data/autodesk-haal-script.py` (alle apps uit de sitemap, ±2 minuten) en `data/autodesk-analyse-script.py`. Over 4 weken opnieuw geeft de echte instroom en hoeveel apps verdwijnen.
