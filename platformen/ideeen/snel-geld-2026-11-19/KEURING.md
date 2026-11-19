# Keuring snel-geld-onderzoek, do 19 nov 2026, keurder (losse Claude, niet de maker)
Wat ik keurde: `platformen/ideeen/snel-geld-2026-11-19/` (BRIEF.md, A-wat-we-hebben.md, B-nieuwe-routes.md, C-bewijs.md, H-hackathons.md), stand op main van 19 nov ochtend.
Akkoord: **ja**, met correcties. De bronnen kloppen bijna overal (14 van 14 nagelopen bronnen bestaan en zeggen in hoofdzaak wat er staat). Wat niet klopt, zit in de schattingen: B rekent de hackathons te hoog, C rekent de kans op een "lumabar" te hoog, en voor geld binnen 12 weken telt een deel van de hackathonprijzen niet mee. Gebruik daarom de rangorde onderaan, niet de losse bedragen van B en C. Geen van de fouten is een verzonnen cijfer.

Alles hieronder zelf nagelezen met curl op 19 nov 2026 (±08:00 tot 09:00 NL). GEZIEN = ik zag het zelf op de bron.

## Nagelopen claims (14)

| # | Claim (bestand) | Wat ik zag | Oordeel |
|---|---|---|---|
| 1 | lumabar $16.746, okt $1.228, nov $15.518, 7 dagen $10.432, 15 en 16 nov $3.919 en $3.227, 171 volgers op X (C) | Precies zo op `trustmrr.com/startup/lumabar.md`, bron Polar (API-sleutel), gesynct 19 nov 00:01 UTC | klopt |
| 2 | "lumabar maakte 47% van alle omzet in twee dagen ($7.146 van $16.746)" (C) | $7.146 klopt, maar dat is **43%**, niet 47% | kleine rekenfout |
| 3 | Superhive Cyber Sale 2024: $713.399 omzet, $540.903 voor makers, 15.254 bestellingen, 33.691 producten, 80% van een maand van $881k, gemiddeld $375 per maker (A, C) | Alles letterlijk zo in de recap (`$713,399.73`, `Total orders (excluding free): 15,254`, `Average Earnings per Creator: $375.11`, 1.442 betaalde makers) | klopt |
| 4 | Click Joints Pro staat nog niet op Superhive (A) | `superhivemarket.com/creators/dortus`: "No products found". Pagina `2026-cyber-sale` bestaat, zonder datum of inhoud. Opt-in via Sitewide Sale Settings (artikel 300) klopt | klopt |
| 5 | Devpost: 45 open online hackathons met dollarprijs, samen $530.630, 10 van $10.000+ (B) | Alle 7 pagina's van de API opgeteld: **$530.630 en 10 boven $10.000 kloppen**, maar dat geld zit in **25** hackathons; 48 staan in dollars, waarvan 23 met $0 (nu 53 open in totaal) | bedrag klopt, aantal niet |
| 6 | Reddit Game of the Day: $15.000 beste dagspel, $6.000 beste overgezette dagspel, 10x $1.000, eigen IP vereist, deadline di 8 dec 18:00 PST, bedrijven mogen, NL niet uitgesloten, bestaand spel mag mits flink bijgewerkt, één prijs per project (B, H) | Alles letterlijk zo in de rules en op de overzichtspagina ("Note you must own the original app/IP", "Organizations ... organized or incorporated", uitgesloten o.a. Brazil, Quebec, Russia, OFAC; "A project can only win one (1) prize") | klopt |
| 7 | Reddit: AI mag en hoeft niet gemeld (H) | Rules zeggen niets over AI; overzicht: "Did you use AI? Fantastic! But it shouldn't be obvious ... ask your agentic assistant to help hide their involvement!" | klopt; past bij besluit 19 nov 01:30 |
| 8 | Reddit: filmpje optioneel (H) | Klopt formeel, maar de rules zeggen ook: **"Judges are not required to test the Project and may choose to judge based solely on the text description, images, and video"**. Dat staat niet in H | aanvulling: filmpje is in de praktijk verplicht |
| 9 | Vorige Reddit Daily Games 525 inzendingen; Codegeist 2024 143; Cloud9 2025 179 (B, H) | Galerijen nageteld: 21x24+21 = 525, 5x24+23 = 143, 7x24+11 = 179 | klopt |
| 10 | Codegeist 2026: $120.000, 4 bonusprijzen van $1.500 elk 6x, geen AI-melding; uitslag ±15 feb 2027 (B, H) | Klopt; nu 4.248 aanmeldingen. Uitslag "on or around Monday, February 15, 2027" valt **na week 12** (12 weken na 19 nov = do 11 feb). B schrijft "toegezegd binnen 12 weken": dat klopt niet | B fout op timing |
| 11 | Cloud9: JetBrains-tool verplicht, repo openbaar met open-sourcelicentie; PICO eist AI-melding (H) | Letterlijk zo ("using at least one JetBrains tool (... AI Coding Agent Junie)"; PICO: "the text description must list the AI tools and models used"). PICO is bovendien een XR-app voor de PICO-bril die op het apparaat moet draaien, niet een gewone Android-app | klopt, PICO valt dubbel af |
| 12 | Blendkit: maker 75%, "plus 4% en $0,50 per verkoop", Blendkit betaalt 15% korting, fair share voor gratis add-ons (A) | 75%, 15% op kosten van Blendkit en fair share kloppen. De 4% en $0,50 zijn **kosten die eraf gaan** (merchant fee en transaction fee), niet iets wat de maker erbij krijgt | woordkeus misleidend |
| 13 | Superpower for AI $16.835 sinds dec 2025, $2.080 in 30 dagen (B) | Klopt (opgericht 11 dec 2025, 0 volgers op X). Ook ScaleReach $10.744, Prospo drie betalingen van $4.800/$4.800/$4.990, ClaudeKit $315, TrustMRR $418k (nu $418.312) kloppen (C) | klopt |
| 14 | Bison & Flex `approve: false` terwijl versies goedgekeurd zijn (A) | API 35901: `approve: False`; 2026.1.1 en 2026.1.0 `approve: True, listed: True`. Downloads nu **12** (A zei 6) | klopt; cijfer verouderd |

Extra nagelopen: Dovetail Key op Superhive 800+ verkopen, $18, 5 maanden oud (A): klopt.

## Deel A: doet het wat beloofd is?
(toets tegen `BRIEF.md`: drie hoeken, elke route met euro's in 4 en 12 weken, kosten, wat Thijs doet, rangorde)

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Alle drie hoeken plus de controle H zijn er, elk met rangorde, kosten en eerste stap. C levert 11 voorbeelden (vraag was 8 tot 12), waarvan 4 met omzet uit een betaalsysteem. | feit | hoog | |
| A2 | **B schat de hackathons op €2.000 tot €6.000 met ±50% kans. Dat is te hoog.** H telde de echte prijsverdeling en kwam op ±€1.300 tot €2.000 verwacht. Ik kom nog iets lager (zie A3 tot A5). B's bedrag niet aan Thijs noemen. | feit (rekensom), bedragen GOK | hoog | Uitslag Reddit 17 dec |
| A3 | Reddit, categorie ported: H geeft 10 tot 20% kans. Ik vind 5 tot 12% eerlijker: de prijs gaat naar de **beste** port, ook bestaande Reddit-makers met eigen spellen mogen een port insturen, en de winnaars vorige keer waren gepolijste puzzels en woordspellen. Een 30-secondenspel van één knop moet echt een dagspel worden (H zegt dat ook). Verwacht ±$400 tot $950, **±€350 tot €800** (GOK). | vermoeden | midden | Aantal ports in de galerij na 9 dec |
| A4 | **Codegeist levert binnen 12 weken €0 op, ook niet toegezegd**: uitslag ±15 feb, geld maart tot april. Cloud9: uitslag ±8 feb (net binnen week 12), geld daarna. Binnen 12 weken kan alleen Reddit echt geld op de rekening zetten, en ook dat pas eind dec tot half feb. | feit (data uit de rules) | hoog | |
| A5 | H mist dat Reddit-jury's alleen op tekst, beelden en filmpje mogen oordelen. Een filmpje van onder 1 minuut is dus het belangrijkste stuk van de inzending, geen bijzaak. | feit | hoog | |
| A6 | **C geeft "±10 tot 20% kans op €10.000 per poging" voor een klein Windows-programma (lumabar-patroon). Dat is overlevingsbias**: lumabar is gevonden omdat het de snelste stijger op TrustMRR is. C noemt zelf geen enkele mislukte poging. Ik schat 1 tot 5% per poging. Daarbij: een Windows-programma testen en zien (skill `kijken`) kan in onze Linux-cloud alleen via Windows-runs in Actions, en de motor (één Reddit-bericht) kan geen agent en geen hoofdchat plaatsen. | vermoeden | midden | Drie pogingen, tel de treffers |
| A7 | C stelt Click Joints Pro in de Cyber Sale op €100 tot €600, A op €50 tot €300. A is beter onderbouwd: C rekent met 1 tot 5% van de 240 gratis gebruikers, maar de gratis add-on mag in Blender niet naar Pro wijzen (besluit 17 nov 18:35), dus die kopers komen er niet vanzelf. | feit (botsing), bedragen GOK | hoog | Verkopen in de sale |
| A8 | B route 3 schrijft "Kai bouwt nu een andere Chrome-extensie" en "$5 staat al op de lijst van Thijs". Beide verouderd: Kai is geparkeerd en de agenda-extensie afgewezen (besluit 17 nov 10:50, bord), en de $5 staat niet op de huidige lijst. Superpower for AI deed er 11 maanden over om $16.835 te halen; €100 tot €1.000 in 12 weken vanaf nul is te hoog, ik schat €0 tot €300. | feit | hoog | |
| A9 | B route 4 (Poki en CrazyGames, €0 tot €1.000): er is geen enkel cijfer per spel (B zegt dat zelf). Poki kiest zelf; een Reddit-dagspel met Redis-ranglijst draait niet zonder ombouw los in de browser. Ik schat €0 tot €100 in 12 weken. | vermoeden | midden | Eén maand op CrazyGames |
| A10 | B noemt "45 hackathons met een prijs in dollars"; het zijn er 25 met echt prijzengeld (zie claim 5). Het totaal van $530.630 klopt wel. | feit | hoog | |
| A11 | C "47%" moet 43% zijn (claim 2); A noemt 6 downloads voor Bison & Flex, nu 12. Klein. | feit | hoog | |
| A12 | Twee koersen naast elkaar: A rekent met €0,90 per dollar, H met €0,86. Geeft ±5% verschil; geen invloed op de rangorde. | feit | hoog | |
| A13 | Eindconclusie van A en C klopt: met wat we hebben komt er in 12 weken geen €10.000. Ook met alle hackathons samen niet, tenzij een hoofdprijs valt (±1 tot 3%). Eerlijk verwacht voor alles samen: **±€1.000 tot €2.500 toegezegd in 12 weken, waarvan minder dan €1.000 echt binnen** (GOK, som van de rangorde). | vermoeden | midden | Stand op 11 feb 2027 |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Geld uitgeven staat overal met "ja van Thijs": Chrome $5, certificaat voor Windows, printer of printdienst, rekenkosten van een video-SaaS. Geen route koopt iets stilletjes. Let op bij Cloud9: de gratis JetBrains-codes gelden "while supplies last"; zijn ze op, dan kost Junie geld en is een ja nodig. | feit | hoog | harde regel 1 |
| B2 | **Bijvangst, geen fout van het onderzoek maar wel belangrijk voor route Superhive:** de makersbio van Dortus op Superhive zegt nu letterlijk "How we work: the code is written with AI agents and tested in real Blender". Dat is een AI-melding, in strijd met besluit 19 nov 01:30 ("nergens een AI-melding"). Hetzelfde soort zin staat in de gekozen FAQ (`berichten/hoofdchat.md` regel 188). De hoofdchat moet die zin weghalen vóór de Cyber Sale. | feit | hoog | besluit 19 nov 01:30 |
| B3 | Hackathons: H heeft per hackathon de AI-regels nagelezen. Reddit en Codegeist vragen geen melding. PICO eist er een en valt terecht af. Cloud9 vraagt aantoonbaar gebruik van een JetBrains-tool; eerlijk kan dat alleen met Junie, en "gebouwd met Junie" is een AI-vermelding. H legt dat terecht bij Thijs. Een JetBrains-IDE noemen die we niet echt gebruikten zou misleiding zijn: niet doen. Of de inzendformulieren op Devpost een AI-vraag hebben is ONBEKEND; zo ja, dan geen onware "nee" (besluit 01:30). | feit | hoog | besluit 19 nov 01:30, "niets nep" (9 nov 22:56) |
| B4 | Niets onder de naam van Thijs zonder ja: H zet zijn ja op elke inzendtekst, mail aan flexi-ontwerpers (A 1e) staat op zijn ja. **C route 2 zegt "de hoofdchat regelt een Reddit-account van Dortus": dat kan niet.** Een account maken en Reddit openen kan alleen Thijs (lijst-thijs: "Reddit kan de hoofdchat niet openen"), en Reddit staat niet bij de kanalen waar Dortus zonder zijn ja mag posten (regel 4: YouTube, TikTok, Discord van Hats). De testpost in een subreddit voor de Reddit-hackathon hoort dus in zijn ja op de inzending. | feit | hoog | harde regel 4 |
| B5 | Grijs gebied en fraude: B schiet nepstreams, nepwerk als mens, airdrop-farmen, data schrapen en grijze sleutels terecht af. "Hide AI involvement" bij Reddit is een uitnodiging van de organisator zelf, geen fraude. Bug bounty buiten de scope is strafbaar; B zet dat er eerlijk bij. | feit | hoog | brief (grijs mag, illegaal niet) |
| B6 | Besluit 18 nov 18:40 ("geen nieuwe producten tot 9 dec") botst met de hackathons, het Windows-programma en de figuren. Alle verslagen zeggen dat en leggen het bij de hoofdchat. Het nieuwe feit is het besluit van Thijs van 19 nov 01:21 (hoofdzaak geld). Terugkomen mag dus, maar moet als nieuw besluit onderaan `besluiten.md`. | feit | hoog | besluiten: terugkomen alleen met nieuw feit |
| B7 | Cijferlabels: bijna alles heeft GEZIEN, DERDEN of GOK met reden. Twee zwakke plekken: B's ±50% en C's 10 tot 20% zijn GOK zonder basiscijfer (hoeveel pogingen mislukken). | feit | hoog | harde regel 5 |
| B8 | Geen persoonsgegevens van Thijs in de vijf bestanden gevonden; H schrijft bij het verkopersaccount "staat bij Thijs". Dat Dortus een eenmanszaak is, stond al in de besluiten. | feit | hoog | harde regel 2 |
| B9 | Cloud9 eist een openbare repo met open-sourcelicentie. Dan wordt de code van Hat Tower open. Beelden van Hats kunnen onder een aparte licentie buiten de code blijven; dat moet de bouwer regelen. Botst niet met "productcode privé" (18 nov 17:04), want Hat Tower is een gratis spel, maar wel opletten. | vermoeden | midden | besluit 18 nov 17:04 |
| B10 | Geen tijd-voor-geld: hackathonprijzen zijn geen klantwerk; B schiet GitHub-bounties terecht af als klussen. Bug bounty zit op de grens (betaald werk voor andermans product), maar per vondst en zonder klant. | vermoeden | midden | besluit 17 nov 16:40 |

## Moet (blokkeert akkoord) / Kan (mag later)

**Moet** (blokkeert het onderzoek niet, wel een verkeerde samenvatting aan Thijs):
1. Noem Thijs niet de €2.000 tot €6.000 van B, maar de rangorde hieronder: hackathons samen verwacht ±€750 tot €1.500, met ±15 tot 30% kans op minstens één prijs; Codegeist telt voor de 12 weken als €0.
2. Haal de AI-zin uit de makersbio van Dortus op Superhive (en uit de FAQ als die live staat) vóór de Cyber Sale (besluit 19 nov 01:30).
3. Maak het filmpje bij de Reddit-inzending verplicht in de opdracht van de bouwer (jury mag alleen op tekst en filmpje oordelen).

**Kan:**
- C: 47% wordt 43%; kans per Windows-poging naar 1 tot 5%; "hoofdchat regelt Reddit-account" wordt "Thijs maakt het, en elke Reddit-post vraagt zijn ja".
- B: "45 hackathons" wordt 25; Kai en de $5 rechtzetten; Chrome en Poki lager schatten.
- A: Blendkit-zin: 4% en $0,50 gaan eraf; Bison & Flex staat nu op 12 downloads.

## Samengevoegde rangorde (A, B, C en H)

Euro's zijn verwacht (gemiddelde) of een bandbreedte, in 12 weken tot do 11 feb 2027, GOK van mij, gerekend met ±€0,86 per dollar. "Toegezegd" = gewonnen of verkocht, geld kan later komen. Kans = kans op meer dan €0.

| # | Route | € in 12 weken (GOK) | Kans | Kosten | Wat Thijs moet doen | Deadline | Mijn oordeel in één zin |
|---|---|---|---|---|---|---|---|
| 1 | **Reddit Game of the Day**, Hat Tower als echt dagspel, categorie ported (B1, H1) | verwacht ±€350 tot €800 toegezegd; uitkomst €0, €860, €5.200 of €12.900 | ±10 tot 20% | €0 | Devpost "Join" en Reddit-account voor Dortus plus `devvit login --copy-paste` (±25 min, vóór ma 23 nov); ja op tekst en testpost (vóór ma 7 dec); bij winst W-8BEN | di 8 dec 18:00 PST (wo 9 dec 03:00 NL) | Doen, nu: het beste geld per uur werk van alle routes en het enige prijzengeld dat binnen 12 weken kan binnenkomen, maar reken op nul en zie een prijs als meevaller. |
| 2 | **Click Joints Pro door de Superhive-keuring en in de Cyber Sale**, met $0-variant, titel en tags, daarna $19 (A 1a, 1b, 1c; C1) | €50 tot €300 | middel (keuring moet vóór ±27 nov klaar) | €0 | niets, of 2 min voor het sale-vinkje | Black Friday vr 27 nov | Doen, bijna gratis werk; klein geld, wel echte verkopen in de drukste week van het jaar. Eerst de AI-zin uit de bio. |
| 3 | **Cloud9 x JetBrains, Event Mini Game** met dezelfde toren (B1, H3) | verwacht ±€400 tot €750, toegezegd ±8 feb, geld maart tot april | ±10 tot 20% | €0 (zolang de gratis codes er zijn) | ja of nee op "gebouwd met Junie"; JetBrains-codes inwisselen, Junie-sleutel als secret (±20 min, vóór ma 14 dec); ja op tekst | di 12 jan 2027 | Goede tweede inzet omdat het spel al bestaat, maar alleen met de ja van Thijs op Junie en een open repo. |
| 4 | **Klein Windows-programma, lumabar-patroon** (C2) | €0 tot €15.000; verwacht ±€200 tot €600 per poging | ±1 tot 5% op €10.000, ±20% op een paar honderd | €0; certificaat €100 tot €400 per jaar met ja | Reddit-account en de lanceringspost onder zijn ja; ja op loslaten besluit 18 nov 18:40 | geen; hoe eerder hoe beter (piek in kerstvakantie) | Het enige plafond boven €10.000, maar een loterij; alleen als één poging van maximaal een week, met vooraf geregeld wie op Reddit plaatst. |
| 5 | **Codegeist 2026**, één app voor een bonusprijs (B1, H2) | €0 in 12 weken; ±€300 tot €400 verwacht in maart tot april | ±8 tot 12% | €0 | Atlassian-ontwikkelaarsaccount, site en sleutel (±20 min, vóór ma 30 nov); ±1 uur filmen in Jira; ja op tekst | di 22 dec 21:00 NL | Pas doen als er na Reddit een agent vrij is; telt niet voor de 12 weken en we spelen tegen Jira-bedrijven. |
| 6 | Studio-licentie gratis aan 10 flexi-ontwerpers (A 1e) | €0 tot €150 | laag tot middel | €0 | ja op de mailtekst, mail onder zijn naam | geen | Goedkoop en de enige motor buiten de pagina voor Pro; verwacht weinig binnen 12 weken. |
| 7 | Uitlegvideo als zoekvraag op de Dortus-kanalen (A 1f) | €0 tot €140 | middel | €0 | niets | loopt al (Chris, vr 12:00) | Doen, helpt routes 2 en 6; los weinig geld. |
| 8 | Pro en Free op Blendkit (A 1d) | €0 tot €90 | onbekend | €0 | account en uitbetaalgegevens | geen | Mag mee in dezelfde vraag aan Thijs, geen haast. |
| 9 | Chrome-extensie voor AI-chats met Pro (B3) | €0 tot €300 | laag | $5 met ja | ja op $5 en op terugkomen op besluit 17 nov 10:50 | geen | Niet nu: bouwers van de chatdiensten maken deze functies zelf, en groei via de winkel duurt maanden. |
| 10 | Zelfde HTML5-spel op Poki en CrazyGames (B4) | €0 tot €100 | laag | €0 | ontwikkelaarsaccounts met betaalgegevens | na 8 dec | Pas na de Reddit-uitslag, als het spel goed bleek. |
| 11 | Bug bounty met een Claude-hackbot (B2) | €0 tot €500 | ±10% | €0 | account met ID, ja per melding onder zijn naam | geen | Niet doen: elke melding gaat onder zijn naam, onze proxy beperkt testen, en de markt verzuipt in AI-meldingen. |
| 12 | Printbare beweegbare figuren met eigen tool (A 8) | €0 tot €450 (plafond op een jaar hoger) | laag op 12 weken | printer of printdienst met ja | ja op geld en op loslaten besluit 18 nov | geen | Later; kan niet zonder echte print (besluit 17 nov 13:40). |
| 13 | Hats supporter pack op itch of Gumroad (A 6) | €0 tot €180 | laag | €0 | niets, maar itch vraagt een AI-melding | geen | Niet doen: botst met "nergens AI-melding" en kost de eerste indruk van de lancering. |
| 14 | AI-knipper als abonnement (C4) | €0 tot €2.000 | laag | rekenkosten €50 tot €500 per maand met ja | ja op maandkosten | geen | Niet doen zonder een gat dat de drie knippers missen; kost elke maand geld. |
| 15 | Bison & Flex, Rollwright, Garmin (A 3 tot 5) | €0 tot €80 samen | laag | €0 | niets | | Laten lopen, geen extra werk. |
| 16 | Hats op Steam (A 6, C3) | €0 in 12 weken | nul voor 11 feb | €0 | Valve afwachten | demo 4 jan, fest 14 jan | Blijft het grote geld op een jaar, maar levert binnen 12 weken niets. |
| 17 | PICO Space Program (H4) | €0 | | | | 1 feb | Niet doen: verplichte AI-melding en het moet op een PICO-bril draaien. |
| 18 | Kit met onze werkwijze, skills of prompts, dataverslag (B5, C10) | ±€0 | heel laag | €0 | niets | | Niet doen: bewezen $0 tot $315 bij anderen, en onze repo is gratis te lezen. |

**Samen (GOK):** routes 1 tot 3 plus 6 tot 8 geven verwacht ±€1.000 tot €2.500 toegezegd in 12 weken, waarvan minder dan €1.000 echt op de rekening voor 11 feb. €10.000 komt alleen binnen bereik met een hackathon-hoofdprijs (±1 tot 3%) of een treffer met route 4 (±1 tot 5% per poging). Wie €10.000 in drie maanden echt wil, moet dus meerdere goedkope pogingen achter elkaar doen (routes 1, 3 en een of twee keer route 4), niet één grote.
