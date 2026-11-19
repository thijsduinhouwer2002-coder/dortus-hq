# Keuring opzet marketingtak Roep, 19 nov 2026, keurder (losse Claude)
Wat ik keurde: `marketing/REGELS.md`, `marketing/wachtrij/LEESMIJ.md`, `marketing/dagrapport.md`, `organisatie/sjablonen/taak-roep-maker.md`, `organisatie/sjablonen/taak-roep-keurder.md`, `marketing/VOORSTEL-hoofdchat.md`, stand van main op 19 nov ±11:25 NL.
Akkoord: **nee** (de veiligheid is goed geregeld; 7 moet-punten, allemaal kleine tekstwijzigingen in de sjablonen, REGELS of het voorstel, behalve moet 1 dat ook een stukje meetcode vraagt of een andere keuze van adressen)

Getoetst aan: CLAUDE.md (hoofdzaak, regels 2, 4, 5, 7), `platformen/ideeen/marketing-tak-2026-11-19/KEURING.md` (moet 1 tot 6), `organisatie/hoofdchat-ronde.md`, `commercie/geplaatst.md`, `organisatie/regels/thijs.md`, besluiten 19 nov 01:30, 01:35 en 11:00. Ik bouw niets.

## Zelf nagelopen (19 nov ±11:20 NL, met curl)
| # | Wat | Uitslag | Bron |
|---|---|---|---|
| 1 | @dortusstudio is persoonlijk | `commerceUser: false`, `uniqueId: dortusstudio`, 1 volger, 2 video's | GEZIEN, tiktok.com/@dortusstudio (curl, 200) |
| 2 | YouTube-RSS van het kanaal werkt met het kanaal-id uit REGELS | Ja, naam "Dortus", nieuwste video sgcC965GVps | GEZIEN, youtube.com/feeds/videos.xml?channel_id=UCTspMNCOwnBkGT2LZ7tB2dg |
| 3 | `dortus.com/click-joints/?ref=yt` werkt | 200; de pagina linkt naar Gumroad Pro **zonder** de ref door te geven | GEZIEN, dortus.com |
| 4 | Het scorebord telt bezoeken met `?ref=` | **Nee.** `scorebord_amami.py` vraagt alleen `type=path` op; in `organisatie/scorebord.md` staat nergens ref | GEZIEN, `organisatie/controle/scorebord_amami.py` regel 101 |
| 5 | Materiaal voor de Maker: `-geluid.mp4` van Click Joints in de releases | Drie: filmpje 2 (gaat vandaag 16:00 uit), 5 (vr 20 nov 16:00 ingepland), 7 (al eerder geplaatst); plus `click-joints-pro-uitleg-1-geluid.mp4` (release youtube-pro-1, kreeg nee van Daan) | GEZIEN, GitHub releases-API |
| 6 | Geluid van de filmpjes is niet door AI gemaakt | Met code gemaakt (`filmpjes-geluid.yml`, "zelf gemaakt geluid (met code)") | GEZIEN, workflow |
| 7 | ffmpeg in een cloudomgeving | Aanwezig in deze omgeving | GEZIEN, `which ffmpeg` |
| 8 | Curl-zin letterlijk in beide opdrachten | Ja, in beide (zonder opmaak, zelfde woorden als CLAUDE.md regel 3) | GEZIEN |
| 9 | Verboden koppelingen in beide opdrachten genoemd | Ja, alle acht; Keurder ook Metricool uit | GEZIEN |

## Deel A: doet het wat beloofd is?
(getoetst aan de keuring van 19 nov, het voorstel daarin, en de vijf vragen van de opdracht)
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | **Moet 1 tot 6 van de vorige keuring zijn verwerkt:** nulmeting 305 staat in de stopregel, één eigenaar van Metricool (de Maker), 3 rondes per dag, "Automatically approve" verplicht in beide sjablonen, geen AI-beeld/stem/persoon en schrijven als Dortus (vraag 9 en 10), en het eerlijke verwachtingszinnetje staat bovenaan REGELS en in het voorstel. | feit | hoog | |
| A2 | **Veiligheid in de opdrachten is goed:** de Maker plant alleen `groen` met een keurder die niet hij is; oranje gaat alleen via de hoofdchat naar groen; de Keurder heeft geen Metricool en mag niets maken of plaatsen; geen reageren, geen geld, niets onder de naam van Thijs; waarschuwing over het mailadres uit `getBrandSettings`; `isAigc` en `isAiGeneratedContent` blijven `false`, wat klopt omdat beeld en geluid echt zijn (bevinding 6 hierboven). Reddit en mail kunnen niet: geen koppeling, en de kanalen staan vast op TikTok en YouTube. | feit | hoog | |
| A3 | **Feiten van vandaag kloppen in REGELS en de Keurder-opdracht:** TikTok persoonlijk (geen bio-link, geen eerste reactie, verwijzing naar een klikbare link = rood, `dortus.com/click-joints` om over te typen = goed), kanaallink "Click Joints Pro ($12)" bovenaan YouTube, lange YouTube-video als enige klikbare verkoopweg, Metricool Free 20 per maand met de Maker als enige plaatser, alleen `-geluid.mp4` met geluid_check GOED, geen `<` of `>`. | feit | hoog | |
| A4 | **De meetlat bestaat niet.** REGELS, het dagrapport en Maker-stap 5 laten de Maker "bezoeken met ?ref=tt en ?ref=yt uit organisatie/scorebord.md" overnemen, maar het scorebord telt alleen paden (bevinding 4). En TikTok kan nooit `?ref=tt` opleveren: wie `dortus.com/click-joints` overtypt, typt geen ref. Gevolg: de Maker schrijft elke ronde een cijfer dat er niet is (of verzint het), en de geld-stopregel ("14 dagen zonder één bezoek met ?ref=") kan niet werken. Ook Gumroad krijgt de ref niet mee (bevinding 3), dus een verkoop is alleen aan een kanaal te koppelen via de dag. | feit | hoog | een regel met ref of per-kanaal-pad in `organisatie/scorebord.md` |
| A5 | **Gumroad-link in YouTube-teksten:** REGELS en de opdrachten laten "de Gumroad-link of dortus.com/click-joints/?ref=yt" toe. De Gumroad-link gaat langs de meting heen (geen ref, geen bezoek op dortus.com) en het subdomein van de winkel bevat een deel van de accountnaam van Thijs, terwijl vraag 6 en REGELS zeggen "nooit de naam van Thijs in een post". Alleen `https://dortus.com/click-joints/?ref=yt` is meetbaar en neutraal. | feit (meting), vermoeden (naam) | hoog / midden | |
| A6 | **Lege rondes vol tekst:** de Maker schrijft elke ronde, ook als er niets gebeurde, een blok in het dagrapport en een regel in `commercie/geplaatst.md` (REGELS "Ook een Maker-ronde zonder plaatsing is één regel", stap 5 zonder uitzondering), en bij STOP ook nog een regel. Dat is 6 schrijfacties en 3 commits per dag zonder inhoud. De Keurder doet het goed ("Geen open concepten: niets vastleggen"). | feit | hoog | dagrapport na 3 dagen zonder posts |
| A7 | **Maken zonder rem en zonder materiaal:** bij minder dan 3 dagen voorraad maakt de Maker elke ronde 2 concepten (tot 6 per dag). Vers materiaal is er nauwelijks (bevinding 5: de drie Click Joints-filmpjes met geluid zijn al uit of ingepland; vraag 8 blokkeert hergebruik binnen 14 dagen), en de opdracht noemt alleen "bijvoorbeeld uit de releases", niet waar echte schermbeelden staan of hoe die een openbare URL krijgen. Wordt alles rood, dan maakt hij elke ronde een nieuwe versie (`-v2`, `-v3`) en vraagt hij Chris elke ronde opnieuw om een lange video. Er staat nergens wat hij moet doen als er niets te maken valt. | feit | hoog | wachtrij na 2 dagen |
| A8 | **Shorts:** REGELS zegt dat een Short alleen na een oranje-besluit van de hoofdchat uit de reserve mag, maar de Keurder-opdracht maakt een Short alleen oranje als er een URL in staat. Een Short zonder URL wordt dus groen en de Maker plant hem in (stap 4 kent `type "short"`) uit een quotum dat niet bestaat. | feit | hoog | eerste yt-short-concept |
| A9 | **Stopregel staat niet in de Maker-opdracht.** REGELS heeft de stopregel van 1 dec en de geldregel van 14 dagen, maar stap 3 en 5 noemen ze niet; in een zelfstandige run is "staat in REGELS" zwakker dan een stap. Wie op 1 dec controleert en ophoudt met TikToks inplannen staat nergens. | feit | midden | ronde van 1 dec |
| A10 | **Volgorde van het voorstel draait rond:** "doorvoeren zodra Thijs de taak heeft aangemaakt", maar het punt op de lijst van Thijs om die taak aan te maken staat zelf in het voorstel (deel 4). Bovendien leest de Maker in zijn eerste ronde CLAUDE.md regel 4 "Agents plaatsen nooit zelf; de hoofdchat doet het" (vorige keuring B6). Dat moet eerder veranderd zijn dan de eerste run. | feit | hoog | |
| A11 | **Botsingen Maker, Keurder, Chris, hoofdchat-ronde:** 30 minuten tussen Maker en Keurder, elk ±15 tot 20 minuten, één eigenaar van Metricool, Chris levert alleen in de wachtrij aan, de hoofdchat beslist alleen oranje en plaatst niet meer zelf (na het voorstel). Werkt, mits A10 goed gaat. Kleine botsing: LEESMIJ zegt dat `status:` van de Keurder is, maar de Maker zet `ingepland`, `geplaatst`, `mislukt` en rood na 24 uur. | feit | midden | |
| A12 | **Teruglezen kan vals "mislukt" geven:** TKPO03 komt uit de Metricool-statistiek, die voor een nieuwe video kan achterlopen. Geen adres = mislukt en "dat soort post gaat terug naar oranje", dus één vertraging zet het hele TikTok-kanaal op oranje. Het openbare profiel met curl werkt wel (bevinding 1) en kan als tweede bron. | vermoeden | midden | eerste ronde na 20 nov 16:00 |
| A13 | **Quotum november:** filmpje 5 is twee keer opnieuw aangemaakt (08:22 en 10:35, `commercie/geplaatst.md`). Telt Metricool aangemaakte posts in plaats van bestaande, dan is er minder over dan 12, en `getScheduledPosts` laat verwijderde posts niet zien. Schrappen gaat goed (TikTok eerst), maar de lange YouTube-video komt pas laat in de maand en kan dan op een vol quotum stuiten. | vermoeden | laag | Metricool weigert een post vóór de 30e |
| A14 | **Geld:** de weg is eerlijk beschreven. Lange YouTube-video met link is de enige klikbare weg; daarvan is er nu nul goedgekeurd (Pro 1 kreeg nee van Daan), dus in november hangt het geld aan de volgende run van Chris. TikTok werkt alleen via overtypen of "search Click Joints" (dat leidt naar de gratis versie, die niet naar Pro mag wijzen). "Tientallen dollars" (GOK) blijft een redelijke verwachting. | feit | midden | eerste verkoop op een dag met een YouTube-post |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Geen persoonsgegevens in de zes bestanden; de repo-eigenaar in de opdracht staat al overal in de repo. Waarschuwing over het mailadres uit `getBrandSettings` staat in REGELS en in de Maker-opdracht. | feit | hoog | 2 |
| B2 | Regel 4: de tak plaatst alleen op Dortus-kanalen na keuring door een andere Claude; schrijven als Dortus; niets onder de naam van Thijs. Maar zolang CLAUDE.md regel 4 niet is aangepast, overtreedt de Maker de regel (zie A10). De nieuwe tekst zegt "alleen wat de Keurder van Roep groen keurde" en vergeet groen door de hoofdchat na oranje. | feit | hoog | 4 |
| B3 | Cijfers in de bestanden hebben GEZIEN, DERDEN of GOK (2.200 tekens is netjes GOK). De ref-cijfers zijn het zwakke punt (A4). | feit | hoog | 5 |
| B4 | Verboden koppelingen in beide opdrachten letterlijk uitgezet; de Maker alleen Metricool, de Keurder niets. | feit | hoog | 7 |
| B5 | De taaknamen beginnen niet met "Dortus". `organisatie/regels/thijs.md` zegt "Dortus-taken heten Stijn, Hans, Vera, Olaf, Jet (of beginnen met Dortus)"; een hoofdchat-ronde die met `list_triggers` meekijkt, kan "Roep: ..." als vreemde taak laten liggen. | vermoeden | midden | thijs.md, gedeeld account |
| B6 | Geen gedachtestreepjes gevonden; Nederlands, gewone woorden. | feit | hoog | 8 |

## Moet (blokkeert akkoord)
1. **Meetlat echt maken (A4).** Kies één: (a) `scorebord_amami.py` vraagt ook de query op (Umami-metric `type=query`) en zet bezoeken met `ref=tt` en `ref=yt` per dag in het scorebord; of (b) gebruik aparte paden die het scorebord nu al telt, bijvoorbeeld een kort over te typen adres alleen voor TikTok en een apart adres alleen voor YouTube, die doorsturen naar de Click Joints-pagina. Voor TikTok is (b) de enige manier om iets te meten. Tot dat er is: de Maker schrijft "niet gemeten" in plaats van een ref-cijfer, en de geld-stopregel leunt alleen op Gumroad-verkopen.
2. **In posts alleen `https://dortus.com/click-joints/?ref=yt`, geen Gumroad-link (A5).** Aanpassen in REGELS (YouTube lang), LEESMIJ (doel, Tekst), Maker-stap 4 en 6 en Keurder-stap 5. Meetbaar, en geen naam van Thijs in een post.
3. **Voorstel in de goede volgorde (A10, B2).** De hoofdchat voert regel 4, `hoofdchat-ronde.md` en `regels/thijs.md` door **tegelijk** met het punt op de lijst van Thijs, met een overgangszin in de hoofdchat-ronde: "Staat er nog geen Maker-blok in `marketing/dagrapport.md`, dan plaatst de ronde nog zoals vroeger." Nieuwe regel 4: "alleen wat groen is (Keurder van Roep, of de hoofdchat na oranje)".
4. **Geen lege rondes (A6).** Maker: bij STOP niets schrijven en stoppen; is er sinds de vorige ronde niets teruggelezen, ingepland of gemaakt, dan geen dagrapport-blok en geen commit, alleen het eindantwoord. Het volledige dagrapport-blok één keer per dag (ronde van 20:13), of als er iets uitging of misging. REGELS "Ook een Maker-ronde zonder plaatsing is één regel" schrappen.
5. **Rem op maken, en wat te doen zonder materiaal (A7).** In stap 6: hoogstens 2 nieuwe concepten **per dag**; noem de bronnen (release `filmpjes-week-1` en volgende releases met `-geluid.mp4`, echte schermbeelden in `commercie/blender-click-joints/` en `ontwerp/click-joints/`, openbare URL via raw.githubusercontent.com van deze repo); na 2 keer rood achter elkaar of als er geen bruikbaar materiaal is: één bericht aan de hoofdchat en niets maken. Chris alleen vragen als er geen open vraag van de laatste 48 uur onderaan `berichten/chris.md` staat.
6. **Elke Short oranje (A8).** In de Keurder-opdracht stap 5 en 6, en in het keurformulier van REGELS: "kanaal yt-short = altijd oranje (alleen uit de reserve na besluit van de hoofdchat)". De zin "Shorts zitten niet in het quotum" vervangen door "Shorts gaan alleen uit de reserve".
7. **Stopregel als stap in de Maker-opdracht (A9).** In stap 3 of 5: "Vanaf di 1 dec: staat er geen TikTok met meer dan 1.000 weergaven en meer dan 5 seconden gemiddelde kijktijd, plan dan geen TikTok meer in en meld het de hoofdchat. 14 dagen posts zonder één verkoop van Pro: meld het in het dagrapport en aan de hoofdchat."

## Kan (mag later)
- Teruglezen TikTok: als TKPO03 nog leeg is, het openbare profiel `tiktok.com/@dortusstudio` met curl lezen; "mislukt" alleen bij ERROR of na 24 uur zonder adres (A12).
- Quotum: in elke maand de lange YouTube-video's eerst een plek geven; weigert Metricool een post om het quotum, dan niet opnieuw proberen maar melden (A13).
- Maker controleert met `git log` op het concept dat de commit met `uitkomst: groen` een Keurder-commit was (vaste commitkop "Roep-Keurder:"), als tweede slot op "nooit eigen werk keuren".
- LEESMIJ: in de tabel "wie schrijft wat" zetten dat de Maker `status:` mag zetten op ingepland, geplaatst, mislukt en rood na 24 uur (A11).
- Beide taken eerst kort laten kijken of er werk is (`grep -l "status: open"`, geplande posts) voor ze alles lezen; scheelt capaciteit bij lege rondes.
- Taaknamen "Dortus Roep: maken en plaatsen" en "Dortus Roep: keuren", of Roep toevoegen aan de lijst in `regels/thijs.md` (B5).
- Gumroad-verkopen per verkoop met verwijzer uit de Gumroad-API (`/sales`) in het scorebord, zodat een verkoop aan dortus.com of YouTube te koppelen is.
- Nagaan of Metricool `firstCommentText` voor YouTube echt plaatst (niet zelf gezien).
- Profieltekst TikTok "Made by Thijs, NL": keuze van Thijs (stond al in de vorige keuring).

## Herkeuring, 19 nov 2026 ±11:50 NL, zelfde keurder
Wat ik keurde: commit 7967cb8c (dortus-hq; REGELS, LEESMIJ, dagrapport, beide sjablonen, VOORSTEL) en de pagina's `dortus.com/tt` en `dortus.com/yt/` (site-commit 17b64d0e), stand van main ±11:45 NL.
Akkoord: **ja** (alle 7 moet-punten zijn weg; niets nieuws onveiligs gevonden; twee kleine kan-punten hieronder)

### Moet-punten
| # | Was | Nu | Weg? |
|---|---|---|---|
| 1 | Meetlat bestaat niet | Eigen meetadressen `dortus.com/tt` (TikTok, over te typen) en `https://dortus.com/yt/` (lange YouTube). Tot het scorebord ze apart telt schrijft de Maker "niet gemeten" en leunt de geld-stopregel alleen op Gumroad (REGELS, Maker-stap 2 en 4, dagrapport). De voorgestelde regel voor `PAGINAS` werkt met `pagina_van` zoals die nu is (GEZIEN, regel 64 tot 72): `/tt` en `/tt/` vallen er allebei onder. | ja (de scorebord-regel voert de hoofdchat door) |
| 2 | Gumroad-link in posts | Overal vervangen door de meetadressen; een `gumroad.com`-adres in titel, tekst of eerste reactie is rood bij de Keurder (stap 5) en in vraag 6, en de Maker toetst het nog eens (stap 3). Geen `?ref=` meer in de zes bestanden (GEZIEN met grep). | ja |
| 3 | Volgorde voorstel | "Doorvoeren tegelijk met het lijstpunt, vóór de eerste run van de Maker", overgangszin in stap 2 van de ronde, regel 4 met "of groen door de hoofdchat na oranje", ook in de besluitregel. | ja (doorvoeren doet de hoofdchat) |
| 4 | Lege rondes | Maker-stap 0: bij STOP of zonder werk niets schrijven en niets vastleggen; dagrapport één blok per dag (20:13), anders alleen een regel als iets uitging of misging; geen regel meer in `geplaatst.md` voor rondes zonder plaatsing. Keurder kijkt eerst met grep of er iets open staat. | ja |
| 5 | Maken zonder rem | Hoogstens 2 per dag (geteld op `gemaakt_door`), materiaal met paden en openbare URL genoemd, stoppen na 2 keer rood of zonder materiaal met één bericht, Chris alleen als er 48 uur geen open vraag staat. | ja |
| 6 | Shorts | Elke Short oranje in REGELS, LEESMIJ, Keurder-stap 5 en 6; Maker plant een Short alleen na groen van de hoofdchat uit de reserve. | ja |
| 7 | Stopregel niet in de opdracht | Maker-stap 2 "Quotum en stopregel" met beide regels, en de stand van de stopregel in het dagrapport. | ja |

Ook verwerkt uit "Kan": profiel als tweede bron bij teruglezen en "mislukt" pas na 24 uur, lange YouTube eerst in het quotum, niet opnieuw proberen bij een vol quotum, commitkop "Roep-Keurder:" als tweede slot, LEESMIJ zegt wie welke status zet, taaknamen "Dortus Roep: ...".

### Zelf gezien op de site (curl, ±11:45 NL)
- `https://dortus.com/tt`, `/tt/`, `http://dortus.com/tt`, `/yt` en `/yt/`: alle 200 (zonder schuine streep of via http één of twee keer doorgestuurd naar `https://dortus.com/<tt|yt>/`). GEZIEN.
- Beide pagina's zijn gelijk: titel "Click Joints Pro for Blender: hinges that click and stop", `$12` en `115°` zoals op `dortus.com/click-joints/`, knop naar Gumroad Pro, "Try the free version first", "Click Joints is made by Dortus", Blender-merkzin. Amami-script met hetzelfde website-id als de Click Joints-pagina, `noindex, follow`, niet in `sitemap.xml`. Geen persoonsgegevens in de tekst, geen AI-zinnen, geen ik-vorm. GEZIEN.

### Nieuw gevonden (geen moet)
| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| H1 | De overgangszin "zolang er geen Maker-blok in `marketing/dagrapport.md` staat, plaatst de ronde nog zoals vroeger" botst licht met moet 4: de Maker schrijft zijn blok pas om 20:13. Plant hij om 08:13 al iets in, dan kan de hoofdchat-ronde tot de avond ook nog plaatsen, en kan er die dag één post boven het dagplafond uitgaan. Geen regelbreuk (beide alleen gekeurd werk, quotum telt Metricool mee), wel slordig. | feit | midden |
| H2 | Meekijken in de ronde (stap 2b van het voorstel) zoekt "een nieuw blok, commit van vandaag"; door "geen lege rondes" laat een Maker-ronde zonder werk geen spoor. Het avondblok blijft het dagelijkse teken van leven. | feit | midden |

### Kan
- Overgangszin in REGELS en het voorstel: "zolang er geen commit met kop `Roep-Maker:` op main staat" in plaats van "geen Maker-blok in het dagrapport" (H1).
- Hoofdchat-ronde: of de Maker en de Keurder draaien lezen met `last_run` uit list_triggers of het avondblok, niet met elke ronde een blok (H2).
