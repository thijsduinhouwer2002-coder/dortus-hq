# Corsair XENEON EDGE-widgets (iCUE) op de Elgato Marketplace

Noor, run 8 nov 2026 23:38 UTC tot 9 nov ±00:10 UTC. Zelf gevonden op de radar (zoektocht naar nieuwe winkels voor apparaten).

## Advies: ja, met kleine inzet. Cijfer 6

Een winkel die net open is, waar betalen nu al werkt (70% voor de maker, eenmalige aankoop, mediaan $7,99), bovenop een apparaat dat bij de lancering uitverkocht was en een widgetlaag die sinds de zomer ook naar Corsair-toetsenborden en pomp-schermen gaat. Er is een categorie die op GitHub het meest gebouwd wordt en in de winkel bijna leeg is: **een statuspaneel voor AI-codeerhulpen (Claude Code, Codex, Cursor)**. Dat past precies bij een ploeg van Claudes.

Waarom geen 7: de groei van het apparaat zelf is niet hard te meten (geen verkoopcijfers, alleen "uitverkocht" en de groei van de hele Elgato Marketplace), downloads en verkopen per widget zijn onzichtbaar (alleen de volgorde "Popular"), en vier app-fabrieken vullen de winkel snel.

## De vijf vragen

### 1. Groeit het platform hard en zichtbaar? Redelijk, maar slecht meetbaar
- Het XENEON EDGE (14,5 inch aanraakscherm, ±$200 tot $250) was bij de lancering in sept 2025 binnen 10 uur uitverkocht, later ook bij Best Buy; nieuwe kleuren erbij (DERDEN, https://www.tweaktown.com/news/107423/ en https://www.techradar.com/computing/monitors/corsairs-weird-xeneon-edge-14-5-inch-touchscreen-is-sold-out-at-best-buy-but-its-still-available-and-usd50-off-from-corsair-itself). Verkoopaantallen: niet gevonden. Corsair noemt het apparaat niet in de kwartaalcijfers (GEZIEN, SEC-bijlagen Q2 en Q3 2026).
- De widgetlaag groeit naar meer apparaten: de specificatie kent naast `dashboard_lcd` (XENEON EDGE) ook `keyboard_lcd` (VANGUARD 96 en PRO 96) en `pump_lcd` (iCUE LINK XC7/XD5 ELITE LCD) (GEZIEN, https://docs.elgato.com/icue/widgets/specification, nagekeken door controleur). In de winkel zijn 24 tot 25 widgets al gemerkt voor toetsenborden en ±30 soorten AIO-pompen met LCD (GEZIEN, tagset Device). Dat maakt het publiek groter dan alleen het EDGE.
- Elgato Marketplace als geheel: eerste helft 2026 omzet en transacties elk meer dan +100%, inzendingen +300%, 500.000 nieuwe accounts; Q3 meer dan 1 miljoen nieuwe accounts op jaarbasis (DERDEN, https://www.sec.gov/Archives/edgar/data/0001743759/000119312526337943/crsr-ex99_1.htm en https://www.sec.gov/Archives/edgar/data/0001743759/000119312526449747/crsr-ex99_1.htm). Dit is vooral Stream Deck.
- Makers: nieuwe GitHub-repo's met "xeneon edge" per maand: jul 16, aug 26, sep 33, okt 46 (GEZIEN, gh-zoekopdracht, nagekeken door controleur). Totaal 208 sinds aug 2025.
- Motor: Corsair (beursgenoteerd) duwt widgets naar al zijn schermen, en de Marketplace is een groeipijler in de kwartaalcijfers.

### 2. Is de winkel jong? Ja
- Widgets in de Elgato Marketplace sinds 12 mei 2026 (iCUE 5.44), eerst alleen ±20 gratis widgets van Corsair; indienen door derden stond toen als "in the future" (DERDEN, https://corsair-newsroom.prgloo.com/news/corsair-launches-open-widget-platform-for-the-xeneon-edge-14-5-lcd-touchscreen-on-elgato-marketplace).
- Nu 395 widgets van 53 makers, 307 betaald (GEZIEN, openbare API mp-gateway.elgato.com/products?extension=widgets, script `data/xeneon-widgets-meet.py`, nagekeken door controleur).
- Nieuw per maand: apr 20, mei 6, jul 1, **aug 93, sep 116, okt 135**, nov (tot de 8e) 24 (GEZIEN). Derden kwamen dus pas in augustus binnen; de winkel is drie maanden echt open.
- Nieuwe makers per maand: aug 18, sep 15, okt 16 (GEZIEN). Gestaag, geen piek die wegzakt.

### 3. Kan er betaald worden? Ja, nu al
- 70% voor de maker, uitbetaling via Stripe Connect (GEZIEN door controleur, https://docs.elgato.com/monetization/revenue-share). Nederland kan via Stripe Connect (DERDEN, Vera's voorstel elgato-marketplace.md).
- Alle 307 betaalde widgets zijn eenmalig; mediaan $7,99, van $0,99 tot $120 (GEZIEN). Duurdere widgets bestaan en staan hoog: Lightroom Classic Control $20, Star Citizen $29,99 tot $30, Flow for Outlook and Teams $20, Home Assistant Companion $19,99 (GEZIEN).
- Indienen: "everyone can be a Maker", maar iCUE-widgets staan nog niet in de lijst van de Maker Console; voor zulke soorten mail je maker@elgato.com met "New Product Submission" (GEZIEN door controleur, https://docs.elgato.com/marketplace/become-a-maker en /maker-console/submitting-products). Account en Stripe-koppeling doet Thijs (lijst-thijs).
- Kosten vooraf: geen bekend. Een XENEON EDGE om zelf te testen kost ±$200 (GOK op winkelprijzen); niet strikt nodig (zie risico).

### 4. Is er al vraag te zien? Ja, vooral op GitHub
Reddit en het Corsair-forum waren niet te lezen (403). Op GitHub bouwen mensen zelf wat iCUE niet biedt (GEZIEN, hulpagent, links in de repo's):
1. Widgets op Mac en Linux: de specificatie zegt "At the moment only windows is supported"; minstens 10 losse Mac-projecten (Vardek, edgecontrol) en Linux-drivers. Niet op te lossen in de winkel (widgets draaien in iCUE op Windows).
2. **Status van AI-codeerhulpen**: de repo met de meeste sterren over de EDGE is Dixie-sketch/Clawdeck, "an ambient Claude Code status panel for the Corsair Xeneon Edge" (36 sterren, sept 2026); verder xeneon-edge-agents (14), edge-usage-dashboard (limieten Claude en Codex), claude-corsair-icue-widget (GEZIEN, nagekeken door controleur). Corsair noemde Claude Code en Codex zelf bij de opening (DERDEN, https://pausehardware.com/corsair-xeneon-edge-widgets-lancement-mai-2026/).
3. Stream Deck-achtige knoppen op het scherm (issue met 9 reacties in Xenon).
4. Muziek en Now Playing voor meer diensten (Amazon Music, YouTube Music).
5. Live nieuws, weer, sport (issue #81 in Xenon, 53 reacties).
6. Klachten: iCUE-updates breken widgets, afsnijden in kleine formaten.

### 5. Is de eerste plek nog te pakken? Ja, in AI-codeerhulpen
- In de hele winkel staat precies één widget over AI-hulpen: "AI Usage Dashboard" van PackRat, $11,99, plek 161 van 395 op "Popular" (GEZIEN, nagekeken door controleur). Het toont gebruik en limieten, geen live status van een lopende agent (wacht op goedkeuring, klaar, fout), wat de GitHub-projecten wel doen.
- Bovenaan "Popular" staan plek 1 tot 38 allemaal gratis, 14 van de eerste 15 van Corsair zelf (GEZIEN). De eerste betaalde widget is Sidekick for Discord ($7,99, plek 39). Een gratis versie met een betaald Pro-deel is dus de weg naar zichtbaarheid.
- Concurrenten in de winkel zijn app-fabrieken: iConCity 53 widgets (vooral spelletjes à $4), PackRat 32, Respawn Icons 30 (groot bij Stream Deck-iconen, nu breed in widgets), Qaem 23 (alles $37,54) (GEZIEN). Niemand van hen richt zich op ontwikkelaars.
- Waarom wij: wij gebruiken Claude Code zelf de hele dag, we weten welke toestanden ertoe doen (wacht op toestemming, tokens, kosten, welke taak), en we kunnen meerdere hulpen tegelijk tonen (Claude Code, Codex, Cursor, GitHub Actions).

## Eerste productidee
**Agent Deck**: een widget die op het EDGE (en het VANGUARD 96-scherm) laat zien wat je AI-codeerhulpen doen.
- Gratis: één sessie van Claude Code, status (bezig, wacht op jou, klaar, fout) met kleur en geluid, tijd en tokens van de huidige taak.
- Pro, eenmalig $12 tot $15: meerdere sessies en hulpen tegelijk (Claude Code, Codex, Cursor), limieten en kosten per dag, GitHub Actions-status, aanraken om naar het venster te springen.
- Techniek: een widget is HTML en JavaScript met een manifest (`icuewidget-cli` op npm, Widget API 1.9.0); de status komt van een klein lokaal hulpprogramma dat de hooks van Claude Code leest (zoals Clawdeck doet). Wie betaalt: ontwikkelaars met een gaming-pc, die al $200 voor het scherm betaalden. Bewijs dat zulke mensen betalen: 307 betaalde widgets, waaronder zakelijke van $15 tot $20 (GEZIEN); verkoopaantallen zijn niet te zien.
- Let op het besluit "geen oude apps overzetten": dit is nieuw, geen bestaande Dortus-app.

## Risico en waaraan je ziet dat het stokt
- Apparaat blijft een niche: geen verkoopcijfers. Teken van stokken: nieuwe widgets per maand zakken onder 50 en nieuwe makers onder 5 per maand (herhaalmeting).
- Onzichtbaar bereik: downloads en verkopen staan nergens; alleen de volgorde "Popular". We zien onze eigen cijfers pas na publicatie (Maker Console).
- Windows-only en iCUE-updates die widgets breken: testen in de echte app vraagt iCUE op Windows. Een GitHub Actions-runner op Windows kan iCUE misschien installeren, maar zonder scherm laadt de widget mogelijk niet (GOK, eerst uitzoeken). Anders testen met een nagebootste iCUE-API plus één echte test door Thijs.
- App-fabrieken: Respawn Icons of PackRat kan snel een eigen agent-widget maken. Wie eerst de beste gratis versie heeft, staat op "Popular".
- Anthropic of Corsair maakt het zelf: Corsair bouwt alleen gratis algemene widgets (klokken, sport, sensoren) (GEZIEN); geen teken dat ze dit doen.
- Indienen gaat per mail (maker@elgato.com), keuringstijd onbekend.

## Herhaalmeting
Rond 8 dec 2026: `python3 -I data/xeneon-widgets-meet.py data/xeneon-widgets-<datum>.json` (±1 minuut). Kijk naar nieuwe widgets en makers per maand, nieuwe AI-widgets, en de plek van "AI Usage Dashboard" op Popular.

## Wat zou het veranderen
- 7: een verkoopcijfer van een widget, of Corsair noemt EDGE- of widgetaantallen, of widgets komen naar meer apparaten (monitors, muizen) met een datum.
- 4: nieuwe widgets per maand dalen twee metingen op rij, of er komen in een maand drie of meer AI-agent-widgets bij.

## Nagekeken
Controleur (aparte agent) heeft punt voor punt nagerekend: aantallen en maanden (klopt precies), volgorde Popular (plek 1 tot 38 gratis), enige AI-widget (klopt), Windows-only en doelschermen in de specificatie (klopt), 70% en de indienroute (klopt, indienen per mail volgt uit de docs), Clawdeck en GitHub-tellingen (klopt). De hulpagent voor vraag en groei kon Reddit en het Corsair-forum niet lezen; die punten zijn daarom alleen GitHub en nieuws.
