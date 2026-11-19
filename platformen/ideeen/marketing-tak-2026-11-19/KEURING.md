# Keuring marketing-tak (nachtonderzoek A en B), 19 nov 2026, keurder (losse Claude)
Wat ik keurde: `BRIEF.md`, `A-voorbeelden.md` (ronde 1 tot 6, tot run ±06:20 UTC) en `B-ontwerp.md` (run 1 tot 7, tot 07:00 UTC) in deze map, stand van main op 19 nov ±07:15 UTC.
Akkoord: **nee** (de kern is goed en kan morgen starten, maar met de 6 moet-punten hieronder rechtgezet; het voorstel onderaan doet dat al)

Hoe ik keurde: 22 claims zelf nagelopen met `curl` (19 nov ±07:15 UTC) plus twee leesacties in Metricool (`getBrandSettings`, `getScheduledPosts` voor november, niets aangemaakt of gewijzigd). Ik bouw niets.

## Zelf nagelopen claims
| # | Claim (waar) | Uitslag | Bron |
|---|---|---|---|
| 1 | Eigen TikTok-app plaatst alleen privé tot audit (B punt 3) | Klopt: "All content posted by unaudited clients will be restricted to private viewing mode" | GEZIEN, developers.tiktok.com content-posting-api-get-started |
| 2 | `auto_add_music` alleen bij direct plaatsen (A 16) | Klopt: "Only works for post_mode = DIRECT POST" | GEZIEN, developers.tiktok.com photo-post |
| 3 | Hacker News verbiedt gegenereerde tekst en automatisch plaatsen (B tabel) | Klopt: "please don't put generated text in HN posts ... please don't automate" | GEZIEN, news.ycombinator.com/newsguidelines.html |
| 4 | Metricool Free: 20 posts per maand, geen X (B run 2) | Klopt: "Up to 20 posts per month in the planner", "Free does not include LinkedIn, X/Twitter" | GEZIEN, help.metricool.com verschillen Free en betaald |
| 5 | Metricool-API alleen Advanced, de koppeling (MCP) ook op Free, met dezelfde 20 (B run 4) | Klopt: "Metricool MCP is available on any plan, including Free"; "Free accounts cannot schedule more than 20 posts per month" | GEZIEN, help.metricool.com plans-add-ons en mcp-limits |
| 6 | Eerste reactie op TikTok alleen bij zakelijk account (B run 7) | Klopt: "TikTok Professional pages only 150" | GEZIEN, help.metricool.com first comment |
| 7 | Short aan lange video koppelen en reacties vastpinnen kan niet via de API (B run 7) | Klopt, letterlijk in de lijst "Link or tag a video/Short as 'similar'..." en "Pin comments" | GEZIEN, help.metricool.com api-limitations |
| 8 | Blender verbiedt reclame voor Pro in de gratis add-on (B run 6) | Klopt: artikel 6.1 tot 6.3 letterlijk zo | GEZIEN, extensions.blender.org/terms-of-service |
| 9 | X-API: $0,015 per post, $0,20 met link (B tabel) | Klopt | GEZIEN, docs.x.com pricing |
| 10 | Bluesky 5.000 punten per uur, post kost 3 (B tabel) | Klopt | GEZIEN, bsky-docs rate-limits.md |
| 11 | Zakelijk TikTok-account krijgt meteen een klikbare bio-link (B run 4) | Staat zo bij Stan, maar dat is één bron die zelf link-in-bio verkoopt | DERDEN, stan.store; zekerheid midden |
| 12 | @dortusstudio is persoonlijk en heeft geen link (B run 6) | Klopt nog: `commerceUser: false`, geen bioLink, 1 volger, 2 video's | GEZIEN, tiktok.com/@dortusstudio, 07:18 UTC |
| 13 | Metricool plaatst op @dortusstudio (B correctie run 5) | Klopt: beide gepubliceerde TikToks geven `uniqueId: dortusstudio` | GEZIEN, de twee videopagina's |
| 14 | "Op TikTok kwam alleen Ebb uit" (B run 5 punt 3) | **Fout.** De Click Joints-TikTok van 17 nov 16:00 staat in Metricool op PUBLISHED en heeft **305 weergaven, 5 likes** (Ebb: 127) | GEZIEN, Metricool `getScheduledPosts` en videopagina 7709157242309774625 |
| 15 | X haalde 42.000 reageer-bots weg (A 6) | Klopt: "removal of 42,000 accounts caught automating replies with chatbots" | DERDEN, startupfortune.com, gelezen |
| 16 | NerdSip: 350.000 weergaven in twee weken (A 18) | Klopt volgens hun eigen blog. Let op: met **AI-gemaakte beelden** (Nano Banana) | DERDEN, nerdsip.pages.dev |
| 17 | dev.to eist AI-melding en verbiedt reclame voor eigen werk (B run 2) | Klopt | GEZIEN, dev.to guidelines-for-ai-assisted-articles |
| 18 | YouTube-spambeleid over massaal gelijke AI-inhoud (B tabel) | Klopt: "Using automated tools or AI to churn out high volumes of similar content with minimal changes" | GEZIEN, support.google.com/youtube/answer/2801973 |
| 19 | AI-label alleen bij realistisch AI-beeld of -geluid (B run 3) | Klopt volgens Kapwing ("realistic", "could pass as real") | DERDEN, kapwing.com |
| 20 | Reddit: geen nieuwe API sinds 31 okt, RSS dicht 13 nov, rest maart 2027 (B punt 1) | Klopt | DERDEN, winbuzzer.com |
| 21 | 244 downloads gratis Click Joints, dortus.com/click-joints/ linkt naar Gumroad Pro (B run 6 en 7) | Klopt | GEZIEN, extensions.blender.org en dortus.com |
| 22 | Quotum november ±14 over (B run 3) | Was juist om 03:00; nu staan er **8** posts in november (2 erbij om 03:54), dus **±12 over** als de ERROR meetelt | GEZIEN, Metricool `getScheduledPosts` |

Ook gezien: Kit heeft **0 abonnees** en Gumroad Pro **0 verkopen** (GEZIEN, `organisatie/scorebord.md` 18 nov 23:49). Het TikTok-profiel zegt "Made by Thijs, NL" (GEZIEN).

## Deel A: doet het wat beloofd is?
(getoetst aan BRIEF.md, de wens van Thijs 01:32 "zelfstandig plaatsen, reageren, verzinnen, 24/7" en de hoofdzaak geld)
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | A doet wat de nadruk van Thijs vroeg: 38 voorbeelden van makers met opzet, cijfers, wat misging, en eerlijk over verkooppraat. Het belangrijkste patroon (maken levert geld, reageren op vreemden levert bans en $0) wordt door de bronnen gedragen. | feit | hoog | |
| A2 | B geeft per kanaal wat kan, met de regels erbij, en een eindontwerp (run 6 punt 5, run 7) dat op wat we al hebben draait: Metricool-koppeling, geplande sessies, scorebord. €0 per maand. Bruikbaar als basis. | feit | hoog | |
| A3 | **Weg van post naar verkoop:** B ziet het goed: nu kan geen enkele geplande post iets verkopen (Short-links dood, TikTok zonder bio-link). De enige echte uitgangen zijn TikTok-bio na zakelijk maken en lange YouTube-video's met link. Zonder lijst punt 1 van Thijs levert de hele tak alleen bereik op. | feit | hoog | bio-link staat erin en `?ref=tt` geeft bezoekers in het scorebord |
| A4 | **Hoeveel geld, hoe snel:** geen enkel voorbeeld in A gaat over desktopsoftware (A patroon 12), en B's eigen rekensom geeft 0,1 verkoop per 1.000 weergaven. Bij $12 per Pro is de verwachting voor de eerste weken tientallen dollars, geen honderden. Het onderzoek zegt dat wel, maar de samenvatting "distributie is de motor achter geld" belooft meer dan de bronnen dragen. | vermoeden | midden | Gumroad-verkopen per dag naast posts na 14 dagen |
| A5 | **Reageren 24/7 kan bijna nergens:** TikTok-reacties niet (geen inbox in de koppeling), YouTube-reacties niet zonder sleutel (captcha), Discord van Hats heeft 1 lid, Kit 0 abonnees. B schrijft het per stuk op, maar zegt nergens in één zin tegen Thijs dat "zelfstandig reageren" in week 1 neerkomt op niets. Dat moet eerlijk gezegd worden. | feit | hoog | |
| A6 | **Fout in B run 5 punt 3:** "op TikTok alleen Ebb" klopt niet; de Click Joints-TikTok van 17 nov ging live en is met 305 weergaven onze beste post. Gevolg: de nulmeting voor de stopregel (1.000 weergaven vóór 1 dec) en de les "niemand merkte iets" zijn deels verkeerd. Run 3 had het wel goed. | feit | hoog | videopagina 7709157242309774625 |
| A7 | **24/7 en zelfstandig:** het ontwerp is zelfstandig zodra Thijs de twee taken aanmaakt. Maar een geplande run stopt bij elke handeling die toestemming vraagt (beschrijving van `create_trigger`: "a run stops whenever an action needs approval"). Zonder "Automatically approve" in de taakinstellingen blijft elke Metricool-plaatsing hangen. B noemt dit alleen als bijzin. | feit | hoog | eerste run van de taak plant wel of niet in |
| A8 | **Ritme te zwaar:** twee sessies elk uur (48 per dag) om hoogstens 1 post per dag te maken, met ±12 posts over in november en 20 in december. Dat kost capaciteit van het abonnement die de bouwers nodig hebben, voor geen extra geld. | vermoeden | midden | aantal posts per sessie na een week |
| A9 | **Twee plaatsers op één quotum:** de hoofdchat-ronde plaatst ook via Metricool (`organisatie/hoofdchat-ronde.md` stap 2). Het ontwerp zegt niet wie het quotum van 20 bezit. Kans op dubbel plaatsen of een leeg quotum halverwege de maand. | feit | hoog | |
| A10 | Draft en "laatste tik door een mens" (A patroon 16) is bij ons niet nodig gebleken: beide TikToks via de API kregen weergaven uit "Voor jou" (127 en 305, GEZIEN). B kiest terecht voor `autoPublish: true` met noodrem. | feit | midden | een post die onder de 50 blijft |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Cijfers hebben vrijwel overal GEZIEN, DERDEN of GOK, en verkoperbronnen zijn als zodanig gemarkeerd. Goed. | feit | hoog | regel 5 |
| B2 | Geen persoonsgegevens gevonden; `check.py` zegt OK. Let op: Metricool `getBrandSettings` geeft het mailadres van Thijs terug; de tak mag dat nooit in een rapport zetten. | feit | hoog | regel 2 |
| B3 | **A raadt het NerdSip-recept aan met "één beeldmodel"** (A run 3 voorstel). NerdSip gebruikt realistische AI-beelden; die vragen op TikTok een label (DERDEN, Kapwing). Dat botst met "nergens een AI-melding". B lost het goed op ("geen AI-beeld, geen AI-stem, geen AI-persoon"); dat moet de regel van de tak zijn, niet A's voorstel. | feit | hoog | besluit 19 nov 01:30 |
| B4 | **Stem van Thijs op een Dortus-kanaal:** de Pro-post van vrijdag begint met "I made a Blender add-on" en het profiel zegt "Made by Thijs, NL". Een agent die in de ik-vorm als Thijs praat, schuift richting "onder de naam van Thijs" (regel 4), en bij reageren op mensen wordt het een agent die zich voordoet als mens. Het ontwerp zegt hier niets over. | vermoeden | midden | regel 4 |
| B5 | Geen nepaccounts, nepreviews of gekochte volgers in het ontwerp; het model met veel accounts (Studley, Alex) wordt terecht afgewezen. Reddit, HN, fora, pers en makers blijven bij Thijs. | feit | hoog | brief, regel 4 |
| B6 | Het ontwerp vraagt een wijziging van CLAUDE.md regel 4 ("agents plaatsen nooit zelf"). Dat is door Thijs al besloten (19 nov 01:35), maar de wijziging is nog niet gedaan; zonder die wijziging overtreedt de tak de regel. | feit | hoog | regel 4 |
| B7 | B schrijft zelf `marketing/REGELS.md` en taakteksten voor, maar zet ze terecht niet zelf neer (alleen als tekst om te plakken). Binnen de eigen map gebleven. | feit | hoog | regel 6 |
| B8 | Geen gedachtestreepjes gevonden in A of B. | feit | hoog | regel 8 |

## Moet (blokkeert akkoord)
1. **B run 5 punt 3 rechtzetten:** de Click Joints-TikTok van 17 nov staat live met 305 weergaven (GEZIEN). Nulmeting voor de stopregel daarop zetten. (A6)
2. **Eén eigenaar van het Metricool-quotum:** zodra de taak "Roep: maken en plaatsen" draait, plaatst alleen die nog via Metricool; de hoofdchat-ronde besluit alleen nog over oranje. Verdeling van het quotum vastleggen. (A9)
3. **Ritme omlaag** naar 3 rondes per dag per agent; elk uur levert niets op bij ±1 post per dag. (A8)
4. **"Automatically approve" verplicht** in de instructie aan Thijs, anders stokt de tak bij de eerste plaatsing. (A7)
5. **Regels van de tak:** geen AI-beeld, geen AI-stem, geen AI-persoon (B's regel, niet A's NerdSip-voorstel), en de tak schrijft als Dortus ("we", "Click Joints"), nooit in de ik-vorm als Thijs. Antwoorden op mensen pas als die regel staat. (B3, B4)
6. **Eerlijk tegen Thijs:** in week 1 plaatst en verzint de tak zelfstandig, maar reageert hij nergens zelf (geen inbox, geen sleutel, geen publiek). En verwacht geld: tientallen dollars in de eerste weken, niet meer, tenzij één post groot gaat (GOK). (A4, A5)

## Kan (mag later)
- Tweede bron zoeken voor "zakelijk account = meteen bio-link" in de EU (nu alleen Stan, DERDEN). Als de link na omzetten niet verschijnt: lange YouTube-video's worden de enige uitgang.
- `YOUTUBE_API_KEY` erbij als Thijs de YouTube-OAuth regelt, voor reacties lezen.
- Bluesky en Mastodon pas als TikTok de drempel haalt (0 volgers, agent heeft geen publiek: A patroon 6).
- De benader-agent voor makers (A ronde 6) is voor Hats sterk, maar Hats kan nog niet op Steam (KYC tot ±eind januari) en versturen valt onder regel 4: pas in december klaarzetten.
- Profieltekst TikTok: "Made by Thijs, NL" zegt Thijs zelf; laten staan of niet is zijn keus.

## Voorstel: de tak "Roep" vanaf vr 20 nov
**Doel:** Click Joints Pro verkopen ($12 Gumroad, later Superhive met Cyber Sale). Het enige product dat nu via eigen kanalen geld kan opleveren. Meetlat: Gumroad-verkopen en bezoeken `dortus.com/click-joints/?ref=tt|yt` per dag naast de posts (scorebord bestaat al).

**Agents: 2, beide geplande sessies, geen Actions nodig.**
1. **Maker** (schrijft, plant in, leest terug). Per ronde, in deze volgorde: `marketing/STOP` lezen; groen gekeurde concepten inplannen via Metricool (`autoPublish: true`, hoogstens 1 TikTok per dag, quotum bijhouden); adres en weergaven van wat gisteren uitging teruglezen (Metricool `TKPO03` plus de openbare TikTok-pagina, YouTube-RSS) en ERROR melden; dagrapport `marketing/dagrapport.md`; bij minder dan 3 dagen voorraad hoogstens 2 nieuwe concepten uit echte schermbeelden (diashow met `autoAddMusic`, of clip met eigen geluid en `geluid_check.py` GOED), één idee per post, één zin per dia, 5 tot 7 hashtags, haak in de eerste seconde, winnaars binnen een dag in varianten opnieuw.
2. **Keurder** (andere Claude): elk open concept met het formulier van 8 vragen en de techniek-check uit B run 5 punt 4, aangevuld met B run 6 punt 4 en run 7 punt 2, plus de twee regels uit moet 5. Bekijkt elk beeld zelf. Groen, oranje (prijs, korting, Cyber Sale, Hats, klacht) of rood (naam van Thijs, regel geschonden).

**Ritme:** Maker 3 keer per dag (08:13, 14:13, 20:13 NL), Keurder 30 minuten later (08:43, 14:43, 20:43). Een concept staat zo binnen ±6 uur ingepland. Oranje beslist de hoofdchat-ronde (4 keer per dag).

**Kanalen eerst:** (1) TikTok @dortusstudio via Metricool, pas zodra het zakelijk is met bio-link naar `dortus.com/click-joints/?ref=tt`; (2) lange YouTube-video's (2 tot 4 minuten, liggend) via Metricool met de link in beschrijving en `firstCommentText` (`?ref=yt`). Geen Shorts met links, geen Bluesky, Mastodon, X, Reddit of mail in week 1.

**Quotum (Metricool Free 20 per maand):** november nog ±12: 8 TikTok, 2 lange YouTube, 2 reserve. December: 14 TikTok, 4 lange YouTube, 2 reserve.

**Wat de hoofdchat vóór de start doet:** regel 4 in CLAUDE.md aanpassen ("de taak Roep plaatst wat een andere Claude groen keurde, alleen op de kanalen van Dortus") met een besluitregel; een bouwer laat `marketing/REGELS.md` (B run 5 punt 4 plus moet 5), `marketing/wachtrij/` en `marketing/dagrapport.md` aanmaken; stap 2 van `organisatie/hoofdchat-ronde.md` wordt "Metricool is van Roep, ik beslis alleen oranje".

**Wat Thijs eenmalig doet (±10 minuten):**
1. @dortusstudio in de TikTok-app zakelijk maken en de link `dortus.com/click-joints/?ref=tt` in de bio (staat al als lijst punt 1).
2. Twee geplande taken aanmaken, tekst uit B run 4 punt 6 met het ritme hierboven: **"Roep: maken en plaatsen"** en **"Roep: keuren"**, en bij beide in de taakinstellingen **"Automatically approve"** aanzetten.
3. Liefst: een kanaallink naar `dortus.com/click-joints/?ref=yt` bovenaan @Dortusapps in YouTube Studio.

**Wat week 1 (20 tot 27 nov) moet opleveren:**
- 5 of meer TikToks en 1 tot 2 lange YouTube-video's live, elk met adres-bewijs in het dagrapport, en geen ERROR die langer dan één ronde onopgemerkt blijft.
- Per post in het dagrapport: weergaven, gemiddelde kijktijd, bezoeken met `?ref=` en Gumroad-verkopen van die dag.
- Minstens 1 post boven 1.000 weergaven (lat staat nu op 305, GEZIEN).
- De eerste verkoop van Pro die aan een kanaal te koppelen is (doel, GOK of het lukt).
- Stopregel blijft: vóór 1 dec geen video boven 1.000 weergaven en 5 seconden kijktijd, dan stopt de TikTok-reeks voor Click Joints en kiest de tak een andere vorm.
