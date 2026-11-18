# Keuring onderzoek distributie en marketing (A tot en met J), 18 nov 2026, onafhankelijke keurder
Wat ik keurde: `BRIEF.md` en de verslagen `A-winkel.md` tot en met `J-publiek-doorverwijzen.md` in deze map (niet gecommit, stand 18 nov ±20:51). Alle bronnen hieronder zelf met curl gelezen op 18 nov ±21:00 tot 21:30 NL.
Akkoord: **ja, als bron voor het eindplan**, mits het eindplan de vier moet-punten onderaan volgt. Geen enkele zware bewering bleek verzonnen; wel zijn er drie overdrijvingen en een paar verouderde aannames.

## Deel A: doet het wat beloofd is?

### 1. Steekproef van 12 zware beweringen (elk zelf bij de bron nagekeken)

| # | Bewering (verslag) | Oordeel | Wat ik zag (bron) | Zekerheid |
|---|---|---|---|---|
| a | JetBrains raadt bij `.y` GoYacc en Bison Language Support aan, Bison & Flex niet (A) | **KLOPT** | `plugins.jetbrains.com/feature/getImplementations?featureType=com.intellij.fileTypeFactory&implementationName=*.y` geeft precies `idea.goyacc` en `info.fluffos.idea_bison`. Ook `*.l` leeg, `*.yy` alleen GameMaker Tools, `*.ll` LLVM en NPCoding: alles zoals A schrijft. | hoog |
| b | Upload zet een plugin bovenaan "New plugins" (B) tegenover "±1 uur in New and Updated" (A) | **KLOPT DEELS** (beide) | Docs `plugins-ranking.html`: "New plugins: Plugins are ranked by the date when the last plugin update was uploaded", dus B citeert goed. Maar de plek duurt kort: API `searchPlugins?orderBy=update date` gaf om ±19:50 UTC nummer 1 van 19:45, nummer 10 van 19:00, nummer 100 van 08:59. De eerste 9 zijn dus ±45 minuten oud: A's "±1 uur" klopt. Extra vondst: de datum is de **uploaddatum**, niet de goedkeurdatum. Onze 2026.1.1 heeft datum 8 nov 18:31 UTC maar werd pas 17 nov openbaar. Als een update 1 tot 4 werkdagen op keuring wacht (A), kan hij de lijst al "oud" binnenkomen en de top nooit halen (vermoeden, niet getest). B's advies "elke 2 tot 3 weken uploaden om bovenaan te staan" rust dus op een effect van hooguit een uur, en misschien nul. | hoog (lijst), midden (keuringseffect) |
| c | Betaalde Marketplace-plugins krijgen gratis marketinghulp (G) | **KLOPT DEELS** | De vier citaten van G staan letterlijk op `benefits-of-jetbrains-marketplace.html` (pagina gedateerd 30 July 2026). Maar het zijn mogelijkheden ("can review", "Prioritized access to ... opportunities", "Possibility for additional promotion ... subject to availability, the quality of the plugin"). G's "waar een betaalde plugin recht op heeft" en "hun eigen pagina belooft dat" gaan te ver. Vragen kost niets; rekenen op een plek in blog of nieuwsbrief niet. | hoog |
| d | Metricool: goedkeurfunctie alleen in Advanced, Free 20 posts per maand (C, E) | **KLOPT** | `metricool.com/pricing/`: Free "Schedule up to 20 posts per month", "Metricool MCP"; "Post approval system" en "Metricool API" staan pas bij Advanced (vanaf € 43 per maand jaarlijks, € 54 maandelijks). Hulpartikel: alleen geplaatste posts tellen, "Duplicate posts count once for each social network". Niet te controleren zonder iets aan te maken: of de MCP-functie `createScheduledPostForReview` op Free echt weigert (C zegt zelf GOK). | hoog (prijzen), laag (gedrag MCP) |
| e | YouTube weigert `<` en `>` in beschrijvingen (C) | **KLOPT** | `developers.google.com/youtube/v3/docs/videos` (wordt doorgestuurd naar de REST-referentie): `snippet.description` "may contain all valid UTF-8 characters except < and >", ook voor de titel. Dat dit de oorzaak is van de mislukte post bij filmpje 2 is een sterk vermoeden, geen GEZIEN zoals C schrijft (Metricool gaf de foutreden niet in het verslag). | hoog (regel), midden (oorzaak) |
| f | Gumroad: mailen pas na $100 omzet en een uitbetaling (J) | **KLOPT** | Letterlijk op beide hulppagina's (169 en 131): "You cannot send emails until you've earned $100 after fees and received a payout." | hoog |
| g | Blender extensions-API kan een versie met token uploaden (E) | **KLOPT** | `developer.blender.org/docs/features/extensions/ci_cd/`: `POST https://extensions.blender.org/api/v1/extensions/$EXTENSION/versions/upload/` met `Authorization:bearer $BLENDER_EXTENSIONS_TOKEN`, `version_file` en `release_notes`. Alleen voor een bestaande extensie. | hoog |
| h | Steam heeft geen API voor aankondigingen (D, E) | **KLOPT** (in de documentatie) | `partner.steamgames.com/doc/marketing/event_tools` noemt alleen de editor, HTML-import, concepten, stagen en de RSS-feed. De Web API-lijst (`/doc/webapi`) heeft `ISteamNews` met alleen `GetNewsForApp` en `GetNewsForAppAuthed` (lezen). Geen gedocumenteerde manier om te plaatsen. D's absolute "geen API" moet zijn "geen gedocumenteerde API". | hoog |
| i | r/incremental_games eist een blok "AI Disclosure" (B) | **KLOPT** | Arctic Shift, post `1tublm5` van moderator Equinoxdawg, 2 jun 2026, 877 punten: "Posts made by publishers or developers will need to explicitly include a section labelled "AI Disclosure" ... otherwise the post will be removed". Ook gebruik bij debuggen moet gemeld. Zelfde post: eigen werk 1 keer per 30 dagen en iets speelbaars verplicht. Kanttekening: "We'll be trialling this for a month or so"; of het nu nog zo geldt, vóór een post opnieuw kijken. | hoog (juni), midden (nu) |
| j | Kit gratis tot 10.000 adressen (D, J) | **KLOPT** | Kit-hulp "The Kit Newsletter Plan" (23 sep 2026): "Manage up to 10,000 subscribers in Kit, for free", met "1 basic visual automation with 1 email sequence" en Recommendations aan. D gebruikte een blog van derden, J de bron zelf. API v4: `send_at: null` bewaart een concept (GEZIEN, developers.kit.com). | hoog |
| k | BlenderNation plaatste Click Joints op 18 nov (B, G) | **KLOPT** | De link geeft 200, titel "Click Joints: free add-on that cuts printable ball joints and shows how far they bend", `article:published_time` 2026-11-18T08:35:39Z, auteur "Community Reporter" (dus door ons ingestuurd). Downloads op de listing nu 233, zoals B en G zeggen. | hoog |
| l | Pose to Print op Superhive, $24 (A) | **KLOPT** | `superhivemarket.com/products/pose-to-print`: "Pose to Print: Turn Rigged Characters Into Print-Ready Miniatures and Figures" van Meshwright, $24, "Published 16 days ago", Blender Extension Compatible. A's titel is ingekort, de rest klopt. Aantal verkopen niet te zien zonder lijstweergave; niet gecontroleerd. | hoog |

Bijvangst, ook nagekeken: J's bewering dat dortus.com een formulier naar Kit tegenhoudt **klopt** (meta-CSP met `form-action 'self'` en `connect-src 'self' https://analytics.amami.dev`). En `dortus.com/hats/` en `dortus.com/hats-of-the-fallen/` geven allebei 404.

**Uitslag steekproef:** 9 KLOPT, 3 KLOPT DEELS, 0 KLOPT NIET. De onderzoekers lazen hun bronnen echt; de fouten zitten in wat ze eruit afleiden.

### 2. Tegenspraak tussen de verslagen

| # | Onderwerp | Wie zegt wat | Mijn oordeel | Zekerheid |
|---|---|---|---|---|
| T1 | **Itch-demo voor Hats** | D actie 2: wel, als Thijs het AI-label op itch accepteert (Gamblers Table, Survival Idle). F deel 5: niet, "no one played it" (Herald), en Olaf raadde het al af. | Geen echte botsing in feiten: beide hebben voorbeelden, en D noemt zelf Idlewood Outpost als mislukking. Het verschil is de inschatting. Doorslag: D's eigen voorwaarden (een spel dat in 10 seconden in de browser leuk is, de webexport van Godot 4.3 met de strook is GOK) zijn niet bewezen voor Hats. Eindplan: itch is een **keuze voor Thijs met één vraag**, niet een actie. Let op: dezelfde AI-meldvraag geldt voor itch (D), r/incremental_games (B) en 80 Level (G). Leg die als één vraag voor. | midden |
| T2 | **Maillijst: Gumroad of Kit** | E stap 6: Gumroad-volgers en `/v2/emails`. J: Kit, want Gumroad mailt pas na $100 plus uitbetaling. D: Kit. | J heeft gelijk (f klopt). E stap 6 werkt nu niet. Gumroad $0+ mag als winkel en adressenbak blijven, maar de lijst waar we naar mailen is Kit. Kit vraagt wel een postadres in elke mail (J, keuze van Thijs, nooit in de repo) en een CSP-aanpassing of een Kit-landingspagina. | hoog |
| T3 | **Wat een update oplevert** | A: in Blender niets (geen sortering op bijgewerkt, uit de broncode), Garmin geen downloads, JetBrains ±1 uur; alleen Superhive (For You) en Steam (bezitters en verlanglijsten) bereiken mensen. B: "elke 2 tot 3 weken uploaden" en in de automatiseertabel "Elke versie: winkel en New-lijst" ook voor Blender Extensions. F: elke 2 tot 4 weken een versie met een post. G: TWIO gaf ±x1,34, door de update. | A is het sterkst onderbouwd (broncode en eigen meting, zie b). B's Blender-deel spreekt A tegen zonder bron. Wat F en G laten zien, is dat de **post of het bericht bij een versie** iets doet, niet de versie in de winkel. Eindplan: uitbrengen alleen voor een echte verbetering, en dan met een post; nooit voor de plek. | hoog |
| T4 | **Clips voor Hats vóór de Steampagina** | C actie 1: pas vanaf de paginadag (±8 dec), tot dan 15 clips renderen en niet plaatsen. D: kleine clips nu, met een bestemming (`dortus.com/hats` met aanmeldvak); de haak blijft voor de paginadag. | D bouwt op een nieuwer feit: de pagina komt misschien pas ±eind januari (ID-controle, plus Valve tot 12 werkdagen achter). C rekent nog met 8 dec. Tien weken niets plaatsen past niet bij het doel van 1 dec. D's richting wint, maar D's eigen doel (100 aanmeldingen op 2 dec, ±40.000 weergaven) is een rekdoel bij 1 TikTok-volger. | midden |
| T5 | **Datum van de paginadag** | C en delen van B en H gaan uit van ±8 dec. D en G: hangt aan Valve, mogelijk vr 22 jan 2027 (D's rekensom, GOK op feestdagen). | Het eindplan moet met beslisdata werken (D: 14 dec, 4 jan, 10 jan), niet met 8 dec als vast punt. | hoog |
| T6 | **Adres van de Hats-pagina** | D en J: `dortus.com/hats`. H: `dortus.com/hats-of-the-fallen/`. | Klein maar echt: Hat Tower (J), de TikTok-bio en de Kit-links moeten één adres hebben. Kies er één. | hoog |
| T7 | **Hoe vaak Reddit voor Hats** | B: r/incremental_games op de demodag plus 30 dagen later, r/CozyGamers, r/cozygames. F: hooguit één aankondiging per moment (pagina, demo, uitgave), Void Miner werd verbannen. | Passen samen als het per subreddit één post per moment blijft binnen hun regels (30 dagen, woensdag). Thijs plaatst zelf. | midden |
| T8 | **BlenderNation opnieuw** | B en F: bij de volgende gratis versie die het melden waard is weer insturen. G: niet nog een keer gratis over hetzelfde product. I: betaalde vermelding ($20 per week) niet doen. | Komt op hetzelfde neer: alleen bij echt nieuws, en Pro is commercieel (€ 25). Alle drie raden nu geen betaald bericht aan. | hoog |
| T9 | **Goedkeuren in Metricool** | BRIEF noemt `createScheduledPostForReview` als voorbeeld. C en E: dat zit in Advanced (€ 43 tot 54). E: gebruik `draft: true` of `autoPublish: false`, plus een eigen wachtrij in `goedkeuren.md`. | E's route volgen; geen Advanced kopen voor de knop. | hoog (prijs), laag (of de MCP-knop op Free echt faalt) |

Geen tegenspraak, wel bevestiging: B, C, F en H willen alle vier één YouTube-uitleg voor Flex en Bison, en hun weergavecijfers (120.448, 68.865, 33.780) zijn gelijk. A, G en J willen allemaal dat JetBrains Bison & Flex bij `.y`/`.l` aanbiedt; dat past in één mail aan marketplace@jetbrains.com (na ja van Thijs op de tekst).

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| R1 | Cijfers hebben bijna overal GEZIEN, DERDEN of GOK, met link. | feit | hoog | harde regel 5 |
| R2 | C noemt de oorzaak van de YouTube-fout GEZIEN; het is een afleiding (sterk, maar geen gezien foutbericht). | feit | midden | regel 5 (label) |
| R3 | G noemt de JetBrains-hulp "recht op" en "belooft"; de bron zegt "can" en "possibility". | feit | hoog | regel 5 (niets mooier maken) |
| R4 | Geen enkel verslag stelt voor dat een agent zelf plaatst; alles gaat als concept naar Thijs of de hoofdchat. Reddit doet Thijs. | feit | hoog | harde regel 4 |
| R5 | Geld alleen als voorstel met bedrag en opbrengst: I ($75 Reddit, verlies $50 tot 70 verwacht, met stopregel), E en C (Metricool Starter € 16 tot 20), G en B (BlenderNation € 25). | feit | hoog | harde regel 1 |
| R6 | Geen persoonsgegevens gezien; het postadres voor Kit staat als "keuze van Thijs, nooit in de repo". | feit (grep op de tien bestanden, niets gevonden) | midden | harde regel 2 |
| R7 | B stelt voor "elke 2 tot 3 weken een kleine versie" te uploaden. Elke versie kost een handkeuring bij JetBrains en, volgens ons uitbrengbeleid, een keuring bij ons. Uitbrengen voor de plek botst met A's advies en met de les dat bewegen zonder reden niets oplevert. | vermoeden | midden | `organisatie/regels/uitbrengen.md` (niet herlezen) |

## Wat staat stevig, wat niet, en wat het eindplan mag zeggen

**Stevig (mag als feit in het eindplan):**
- Bison & Flex staat niet in JetBrains' aanraadlijst voor `.y` en `.l`; bij `.l` is er niemand. Dit is de grootste gratis knop voor deze plugin (A, gemeten).
- Gumroad kan nog niet mailen; Kit kan het gratis tot 10.000 adressen, met een postadres en een CSP-aanpassing op dortus.com.
- Metricool Free: 20 geplaatste posts per maand, een post op twee netwerken telt twee keer; goedkeurknop en REST-API pas in Advanced.
- YouTube-teksten nooit met `<` of `>`.
- Blender-updates kunnen met een token vanuit de workflow; Steam-aankondigingen niet (geen gedocumenteerde API), wel als concept klaarzetten.
- r/incremental_games vraagt een AI-blok (stand juni 2026), 1 post per 30 dagen en iets speelbaars.
- BlenderNation plaatste Click Joints Free op 18 nov 08:35 UTC; effect nog niet gemeten (G: 20 nov opnieuw kijken).
- Steam verkoopt geen advertenties; betaalde verlanglijsten via Reddit kosten in alle gevonden proeven $0,50 tot $2 (DERDEN), meer dan wat een verlanglijst van Hats waard is (I's rekensom, GOK op de koopkans).

**Niet stevig (alleen met GOK of als vraag):**
- Wat een update in een winkel oplevert: in JetBrains hooguit ±1 uur zichtbaar en misschien niets door de keuringstijd; in Blender niets.
- Dat JetBrains ons marketing geeft: alleen "we kunnen het vragen".
- Elk verwacht aantal aanmeldingen, verlanglijsten of verkopen (D 100 aanmeldingen, J 100 tot 300, I 20 tot 60 verlanglijsten): rekensommen op cijfers van anderen.
- Of een itch-demo van Hats aanslaat (T1).
- Of `createScheduledPostForReview` op ons plan werkt.
- Alle data rond de Steampagina.

**Het eindplan mag NIET zeggen:**
- "Een upload zet ons bovenaan" of "elke 2 tot 3 weken uploaden voor de lijst".
- "JetBrains belooft of geeft betaalde plugins gratis marketing".
- "We mailen via Gumroad".
- "Paginadag 8 dec" als vaststaand.
- "Steam heeft geen API" zonder "gedocumenteerde".

## Moet (blokkeert akkoord) / Kan (mag later)

**Moet (voor het eindplan, niet voor de verslagen zelf):**
1. B's Bison & Flex-actie 1 ("elke 2 tot 3 weken uploaden") niet overnemen; A's regel volgen: alleen uitbrengen voor een echte verbetering, met een post erbij (T3, b).
2. Maillijst = Kit, niet Gumroad; met de twee voorwaarden (postadres gekozen door Thijs, CSP of Kit-landingspagina) als punten voor Thijs en de site-agent (T2).
3. G's JetBrains-punt herschrijven als "vragen of er ruimte is", zonder "recht op" (c).
4. Plan met beslisdata in plaats van "paginadag 8 dec"; één adres voor de Hats-pagina kiezen (T5, T6).

**Kan:**
- De AI-meldvraag voor itch, r/incremental_games en 80 Level als één vraag aan Thijs voorleggen (T1).
- Vóór een post op r/incremental_games nakijken of de AI-regel van juni nog geldt (i).
- Na de volgende JetBrains-update de uploaddatum en het moment van openbaar worden naast elkaar zetten, om te zien of een update de top van "New and Updated" ooit haalt (b).
- C's label voor de oorzaak van de YouTube-fout aanpassen naar vermoeden (R2).
