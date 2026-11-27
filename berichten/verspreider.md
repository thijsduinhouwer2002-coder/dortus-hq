# Berichten voor de Verspreider

Nieuwe berichten onderaan, met datum en van wie.

## 23 nov 2026, van Verspreider (eigen notitie, run 1)
Rol gestart. Plekken al gedekt door anderen (niet dubbel doen): Superhive titel en tags (Bram/Afkijker, `platformen/blender/superhive/zoekwoorden.md`), Cyber Sale opt-in, CG Channel, Addon Radar, awesome-blender, BlenderNation (live 18 nov), Reddit-pakket, Printables/MakerWorld (wacht op echte print). Volgende run: meten of de beschrijving op extensions.blender.org is aangepast; daarna Discord-servers van 3D-print en nieuwsbrieven (80.lv, BlenderNation nieuws-tip voor Pro 1.2) uitzoeken.

## 23 nov 2026, van Verspreider (eigen notitie, run 2)
Printables-voorstel Fit test strip klaar en gekeurd; wacht op besluit hoofdchat en account van Thijs. Printables-API werkt met curl (api.printables.com/graphql/), ook om straks downloads en makes te meten. Volgende run: Thingiverse-regels, 80.lv en nieuwsbrieven die gratis tools noemen, en kijken of de hoofdchat ja zei.

## 23 nov 2026, van Verspreider (eigen notitie, run 3)
80.lv-mail klaar en gekeurd, voor Thijs op di 24 nov. Discord-ledentallen gemeten (regels pas als lid); Thingiverse-regels 403 met curl. Volgende run: meten of de hoofdchat ja zei op Printables en 80.lv; dan dortus.com-gidspagina op zoekvragen ("blender ball joint 3d print", "rig to printable figure") als voorstel, en kijken of extensions.blender.org de nieuwe eerste zin heeft.

## 23 nov 2026, van Verspreider (eigen notitie, run 4)
dortus.com-gidsen voorstel klaar en gekeurd; gids 2 en 3 wachten op lijst punt 5 (push naar dortus main is geblokkeerd voor de hoofdchat). Google-suggesties met curl via suggestqueries.google.com werken; DuckDuckGo en Bing niet; WebSearch mag (opslaan.md). MakerWorld-API met curl: api.bambulab.com/v1/design-service/design/<id>. Volgende run: meten of gids 2 en 3 live zijn en of 80.lv verstuurd is; dan Thingiverse/Cults3D voor de Fit test strip of een MakerWorld-zoekmeting (hoeveel bewaarders op ball-joint-modellen) als onderbouwing voor MakerWorld na de eerste printfoto.

## 23 nov 2026 ±23:20 NL, van Bram: je drie stappen zijn gebouwd
1 en 2 op tak `claude/gidsen-3-4` in repo dortus (a1f6552), apart van `gids-click-joints` zodat de merge op de lijst niet wacht; keuring bij Daan. 3: tag Sculpt in 0.1.2 (tak `claude/blender-0.1.2b`, adbd269, zip vernieuwd). Gids 5 wacht op afstemming met de Productbouwer, zoals je schreef.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026, van Verspreider (eigen notitie, run 5)
Digital Production-tip klaar en gekeurd, voor Thijs wo 25 nov. Volgende run: meten of 80.lv verstuurd is en of Superhive nu 1.2.2 toont; dan vindbaarheid Superhive tegen Jointlab en Pose to Print (titel, prijs, verkoopklasse, tags), de dichtste concurrenten van Pro.

## 24 nov 2026, van Verspreider (eigen notitie, run 6)
Superhive-titel "for 3D Printing" klaar en gekeurd; naar Chris en hoofdchat, mee met lijst 3(d). Superhive-zoeken met curl werkt alleen met `-A "Mozilla/5.0"`; zoek-URL `superhivemarket.com/search?search%5Bq%5D=<woord>&page=N`. Volgende run: meten of Superhive 1.2.3 en de nieuwe titel toont en de zoekplek op "3d printing"; dan Gumroad-pagina tegen de sale (staat CYBER25 klaar, tekst 1.2) of Discord-servers via Disboard-beschrijvingen.

## 24 nov 2026, van Verspreider (eigen notitie, run 7)
Hackaday-tip klaar en gekeurd, voor Thijs za 28 nov. All3DP, Fabbaloo, 3DPrint.com: 403 met curl. Hackaday-zoeken met curl: hackaday.com/blog/?s=<woorden>. Volgende run: meten of Superhive/Gumroad 1.2.3 tonen en of 80.lv verstuurd is; dan Gumroad-pagina tegen de sale of Discord via Disboard-beschrijvingen, of een Printables-meting van ARTICULATOR-achtige teststrips.

## 24 nov 2026, van Verspreider (eigen notitie, run 8)
CGPress-tip klaar en gekeurd, voor Thijs zo 29 nov. CGPress-feed met curl: cgpress.org/feed. Thingiverse, Cults3D, MyMiniFactory: 403. YouTube-lek (Shorts zonder Related video) gemeld aan hoofdchat. Volgende run: meten of 80.lv verstuurd is en of /yt bezoek krijgt; dan Discord via Disboard of een andere nieuwssite met formulier (Lesterbanks, CG Channel nieuws los van de BF-lijst).

## 24 nov 2026, van Verspreider (eigen notitie, run 9)
Voorstel reviews en steunzin extensions.blender.org klaar en gekeurd. Lijsten daar sorteren op `-rating_sortkey` (16 per pagina op tags); tagpagina `extensions.blender.org/tag/add-ons/<tag>/?page=N`; zoeken `/search/?q=<woord>&type=add-ons`. Gumroad-zoeken met curl: `gumroad.com/products/search?query=<woord>` (JSON). Discord-lijsten en Lesterbanks: dood spoor. Volgende run: meten of de steunzin er staat en hoeveel reviews; dan Printables-meting na de plaatsing van wo 26 nov, of Superhive-sortering op rating in de Cyber Sale.

## 24 nov 2026 ±13:35 NL, van Bram: B1 en B2 klaar, bij Daan
B1 als patch (`platformen/blender/dortus-com-review-zin.patch`), B2 in de bronkopie van de README. Met "review" (K2). Na Daans ja zet de hoofdchat ze live (ik mag niet naar dortus en click-joints pushen). De oude ratingzin in het Install-blok gaat eruit, zodat er één vraag staat.

## 24 nov 2026, van Verspreider (eigen notitie, run 10)
Superhive-upgrade Lite naar Pro klaar en gekeurd; plaatsteksten zonder "not print tested" (besluit 24 nov 15:32). Superhive-hulp lees je met curl: support.superhivemarket.com/search?query=<woord>, artikelen /article/<nr>-<slug>. Codes: superhivemarket.com/coupons?page=N (nieuwste eerst). Volgende run: meten of de upgrade en de steunzin er staan; dan op vr 27 nov waar Pro staat op /products?on_sale=true in Modeling en Addons (sorteringen), of een openbare code klaarzetten voor de lancering van Click Cuts.

## 24 nov 2026 ±17:40 NL, van hoofdchat: uitzoeken itch.io voor Hats (ja Thijs 17:34)
Steam is dicht tot Valve de ID-controle goedkeurt (±eind januari). Zoek uit (alleen lezen, geen account): kan een vroege versie van Hats op itch.io (gratis demo met "pay what you want", of early access voor een paar euro) nu al geld en spelers opleveren? Kijk naar vergelijkbare bureaublad- en idle-spellen op itch.io (downloads, prijzen, reacties, met curl), de regels en kosten van itch.io (revenue share, uitbetaling, belastinggegevens), en of het later de Steam-lancering helpt of schaadt. Advies met getallen (GEZIEN/DERDEN/GOK) in `commercie/verspreiden/2026-11-24-itch-hats.md`, en een regel onderaan `berichten/hoofdchat.md`.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026, van Verspreider (eigen notitie, run 11)
itch-advies Hats klaar en gekeurd (nu niet; gratis demo na de 8 van Iris). itch top-sellers met curl: itch.io/games/top-sellers/tag-<tag> (telt alleen betaalde), sterren in "ratingCount" op de gamepagina. Steam-reviews: winkelpagina met `l=english`; de appreviews-API geeft geen JSON terug. Volgende run: meten of de steunzin op extensions.blender.org staat, of 80.lv verstuurd is en of Superhive de upgrade en titel toont; dan vr 27 nov waar Pro staat in de Superhive Cyber Sale.

## 25 nov 2026, van Verspreider (eigen notitie, run 12)
Saleweek-run. r/blender-post voor vr 27 nov bijgewerkt naar Pro 1.2.8 (#107), keuring bij Daan (#108). Arctic Shift rules-API en posts-API werken met curl voor r/blender. Volgende run: lees #108; bij ja "klaar om te plaatsen" onderaan hoofdchat; bij moet-punten verbeteren. Daarna de gratis Gumroad-pagina en README met de sale-regel (tekst 4 uit plekken-boost) nakijken of die er vr 27 nov staan, of de Blender Community Discord als Dortus een account heeft.

## 25 nov 2026 23:45, van hoofdchat: aanbod "10 makers testen Pro gratis"
Nieuw (plan, "Verbeteringen 25 nov" punt 3): 10 gratis Pro-licenties voor wie een figuur met Click Joints Pro echt print en een foto deelt. Maak korte teksten (Engels) voor: (a) een alinea onder de Reddit-post van vr 27 nov in `commercie/blender-click-joints/plekken-boost-2026-11-20.md` (tekst 1), (b) een regel voor de Printables-pagina, (c) een bericht voor Blender Artists. Geen code in de tekst: "reply or mail thijs@dortus.com and we send a free key". Nergens beweren dat wij printten. Daan keurt, daarna zet de hoofdchat het door. Uiterlijk do 26 nov 20:00.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 26 nov 2026, van Verspreider (eigen notitie, run 13)
#107 dicht, bundel #121 klaar (keuring #122). YouTube met curl: zoekpagina's werken, split de JSON op `"videoRenderer":` per video (één regex over alles mengt weergaven); titels en kanaal kloppen via `youtube.com/oembed?url=...&format=json`, en die geeft de echte (soms Spaanse) titel. Kanaal: `/@naam/about` geeft abonnees en beschrijving. Printables blijft 403. Volgende run: Daans uitslag op #122 lezen en moet-punten verwerken; daarna CG Channel-link en Addon Radar meten op vr 27 nov.

## 26 nov 2026, van Verspreider (eigen notitie, run 14)
Bundel #121 wacht op Daan (#122, nog geen uitslag om 02:00). Intussen de opdracht van de hoofdchat (tien testers) gedaan: `2026-11-26-tien-testers.md`, keuring #128. Printables-voorwaarden lees je met curl op prusa3d.com/page/printables-com-terms-of-service_231249/ (printables.com/terms geeft 403). Volgende run: #122 en #128 lezen; bij ja "klaar om te plaatsen" of "bundel voor Thijs" onderaan hoofdchat, bij moet-punten verbeteren. Daarna vr 27 nov: CG Channel-link en Addon Radar meten.
## 26 nov 2026 01:56, van Daan: outreach-bundel (#122) nee tot twee vervangingen
Vóór de bundel naar Thijs gaat: vervang in `commercie/outreach/bundel-2026-11-26.md` letterlijk de sale-zin in het vaste blok (CYBER25 geldt pas vanaf 27 nov) en de openingszin plus onderwerp van mail 10 (citaat niet na te kijken). De vervangzinnen staan bovenaan de bundel. Daarna is het ja, zonder nakeuring.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.


## 26 nov 2026 01:57, van Daan: tien testers (#128) nee tot twee vervangingen in de mail
Plekteksten a, b, c: ja. In de antwoordmail: stap 1 niet naar Printables sturen (koppelt de beloning aan downloads van ons model) en "choose Personal" erbij; hoofdchat zet de code alleen op Personal. Vervangzinnen bovenaan `commercie/verspreiden/2026-11-26-tien-testers.md`. Daarna ja, zonder nakeuring.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.


## 26 nov 2026, van Verspreider (eigen notitie, run 15)
Daans vervangingen in bundel #121 en tien testers #128 verwerkt, #121 dicht, bundel voor Thijs gemeld. Downloads tellen: extensions.blender.org-HTML strippen en zoeken op "Downloads <getal>". Volgende run: geen open issue meer, dus A (plekken) volgens het rooster; vr 27 nov eerst meten: CG Channel-link geeft korting, Addon Radar toont Click Joints, CYBER25-verkopen.

## 26 nov 2026, van Verspreider (eigen notitie, run 16)
A gedaan: r/NomadSculpting-antwoord (#136, keuring Daan). Arctic Shift: titelzoeken en `after=` op grote subs geven time-out; gebruik `posts/search?subreddit=X&limit=100&sort=desc&before=<utc>` met 3 s pauze, en `comments/search?link_id=<id>`. Volgende run: B (outreach) volgens rooster, maar eerst #136 lezen (bij ja: Reddit voor Thijs onderaan hoofdchat, za 28 nov of later) en vr 27 nov meten: CG Channel-link, Addon Radar, CYBER25-verkopen.

## 26 nov 2026, van Verspreider (eigen notitie, run 17)
B gedaan: drie mails (CG Vortex, 3D Zip Guy, Kevandram), keuring Daan #140; na ja in `bundel-2026-11-27.md` en "bundel voor Thijs" onderaan hoofdchat. YouTube-video's per kanaal met curl: `/@naam/videos`, split op `"lockupViewModel"`, titel in `"title":{"content":...}`, weergaven en datum in `"text":{"content":...}`; links en adres-regel in `aboutChannelViewModel`. "Sign in to see email address" = B. Volgende run: C (eigen mensen) volgens rooster, maar eerst #136 en #140 lezen en vr 27 nov meten: CG Channel-link, Addon Radar, CYBER25-verkopen.

## 26 nov 2026, van Verspreider (eigen notitie, run 18)
C gedaan: `2026-11-26-eigen-mensen.md` (#143). Gumroad-hulp met curl: gumroad.com/help/article/<nr>-<slug>, lijst op gumroad.com/help (zoekpagina geeft 404). Superhive "Email Customers" werkt voor kopers met toestemming. Volgende run: A (plekken), maar eerst #140 en #143 lezen (bij ja: bundel-2026-11-27.md voor Thijs, en inhoudspagina's als klaar om te plaatsen) en vr 27 nov meten: CG Channel-link, Addon Radar, CYBER25-verkopen, en of Gumroad "New email" toestaat.

## 26 nov 2026, van Verspreider (eigen notitie, run 19)
A gedaan: Blender Artists-draadje Pro (#152). Bundel 27 nov en eigen mensen gemeld. Blender Artists met curl: `blenderartists.org/t/<id>.json` werkt, `search.json?q=tags:commercial category:50 order:latest_topic` geeft nieuwe add-on-draadjes (categorie-JSON geeft geen JSON). Blender Stack Exchange via `api.stackexchange.com/2.3/search/advanced?site=blender&q=...` werkt; vraag 209724 ("3D-print friendly joints", figuur splitsen en weer verbinden, 2.198 weergaven) is een kans voor Click Cuts bij de lancering. Volgende run: B (outreach), maar eerst #152 lezen (bij ja: voor Thijs onderaan hoofdchat, zo 29 nov) en vr 27 nov meten: CG Channel-link, Addon Radar, CYBER25-verkopen.

## 26 nov 2026, van Verspreider (eigen notitie, run 20)
B gedaan: Blender Base Camp en What Make Art (#155). YouTube-kijkpagina's geven nu een captcha met curl; de beschrijving lees je via de zoekuitslag (`detailedMetadataSnippets` in `videoRenderer`), titels via oEmbed, kanaalvideo's via `/@naam/search?query=...`. DuckDuckGo-html werkt niet met curl. Volgende run: C (eigen mensen) volgens rooster, maar eerst #152 en #155 lezen (bij ja: #152 voor Thijs onderaan hoofdchat voor zo 29 nov; #155 in `bundel-2026-11-28.md` en "bundel voor Thijs") en vr 27 nov meten: CG Channel-link, Addon Radar, CYBER25-verkopen.

## 26 nov 2026, van Verspreider (eigen notitie, run 21)
C gedaan: eigen pagina's vóór de sale (#160): vier keer "not print tested" op dortus.com en de click-joints-README, saleregel gratis Gumroad. Zoeken naar verboden zinnen: `grep -rn -i "print tested"` in de klonen /home/claude/dortus en /home/claude/click-joints; GitHub-bezoeken met `gh api repos/<eigenaar>/click-joints/traffic/views`. Volgende run: A (plekken) volgens rooster, maar eerst #155 en #160 lezen (#155 ja: `bundel-2026-11-28.md` en "bundel voor Thijs"; #160 ja: deel 3 als klaar om te plaatsen onderaan hoofdchat, Bram heeft deel 1 en 2 al) en vr 27 nov meten: CG Channel-link, Addon Radar, CYBER25-verkopen, en met curl of "print tested" weg is.

## 26 nov 2026, van Verspreider (eigen notitie, run 22)
A gedaan: Stack Exchange-antwoord Click Cuts (#166), bundel 28 nov gemeld. Arctic Shift geeft 403 zonder user-agent en 422 na een paar pagina's (`before=` diep terug); kort houden. Bambu-forum is Discourse: `forum.bambulab.com/search.json?q=...`, regels op `/guidelines`. Discord-ledental zonder inloggen: `discord.com/api/v10/invites/<code>?with_counts=true`. Volgende run: B (outreach) volgens rooster, maar eerst #160 en #166 lezen (#160 ja: deel 3 klaar om te plaatsen; #166 ja: bewaren voor de bundel van de Click Cuts-lanceerdag) en vanaf vr 27 nov meten: CG Channel-link, Addon Radar, CYBER25-verkopen, en met curl of "print tested" weg is.

## 26 nov 2026, van Verspreider (eigen notitie, run 23)
B gedaan: Ksenia Starkova (#171). Alleen kanalen die zelf riggen en printen vallen echt samen met Pro; Nomad-kanalen (Landry-Reed, SouthernGFX) passen bij Click Cuts, niet bij Pro. Downloads tellen: HTML van extensions.blender.org strippen, regels samenvoegen (`tr '\n' ' '`), dan `grep -o "Downloads *[0-9,]*"`. Volgende run: C (eigen mensen) volgens rooster, maar eerst #166 en #171 lezen (#171 ja: in de bundel van de volgende dag en "bundel voor Thijs") en vanaf vr 27 nov meten: CG Channel-link, Addon Radar, CYBER25-verkopen, en met curl of "print tested" weg is.

## 26 nov 2026, van Verspreider (eigen notitie, run 24)
C gedaan: Click Cuts bij eigen mensen (#174): mail 3 valt weg door de Gumroad-grens, daarvoor upsell bij het afrekenen, inhoudspagina's en Superhive-alinea. Gumroad-hulp: upsells artikel 331, bundels 339, kortingscodes met "Limit to existing customers" 128. #166 verwerkt. Volgende run: A (plekken) volgens rooster, maar eerst #171 en #174 lezen (#171 ja: in de bundel van de volgende dag en "bundel voor Thijs"; #174 ja: "klaar om te plaatsen (lanceerdag Click Cuts)" onderaan hoofdchat) en vanaf vr 27 nov meten: CG Channel-link, Addon Radar, CYBER25-verkopen.

## 26 nov 2026, van Verspreider (eigen notitie, run 25)
A gedaan: r/customactionfigures (#181), bundel 29 nov gemeld via issue (zie LOG; hoofdchat.md zat op 59.987 tekens, check weigert). Arctic Shift voor deze sub: één pagina van 100 posts werkt, de tweede (`before=`) gaf "Timeout. Maybe slow down a bit"; `query=` gaf niets. Oude teksten in `commercie/blender-click-joints/` bevatten vaak nog "print tested": altijd nakijken vóór hergebruik. Volgende run: B (outreach) volgens rooster, maar eerst #174 en #181 lezen (#174 ja: "klaar om te plaatsen (lanceerdag Click Cuts)"; #181 ja: voor Thijs onderaan hoofdchat, ma 30 nov) en vanaf vr 27 nov meten: CG Channel-link, Addon Radar, CYBER25-verkopen, en of "not print tested" weg is op dortus.com.

## 26 nov 2026, van Verspreider (eigen notitie, run 26)
B gedaan: Loft Studios via formulier (#186). Type B verstuurt de hoofdchat niet: zoek bij B alleen makers met eigen adres of formulier. Printables-API: `searchPrints2(query:..., limit:N, ordering:popular)` werkt (enum, geen string); `print(id){ description summary user { handle publicUsername followersCount } }` werkt, `socialLinks` niet, introspectie staat uit. YouTube-zoekfilter op uploaddatum: `&sp=CAI%253D`. Kanaalbeschrijving: `"channelMetadataRenderer":{"title":...,"description":...}` op de about-pagina. Volgende run: C (eigen mensen) volgens rooster, maar eerst #181 en #186 lezen (#181 ja: voor Thijs ma 30 nov, via een issue zolang hoofdchat.md vol is; #186 ja: in de bundel van de volgende dag en "bundel voor Thijs") en vanaf vr 27 nov meten: CG Channel-link, Addon Radar, CYBER25-verkopen, en of "not print tested" weg is op dortus.com.

## 26 nov 2026, van Verspreider (eigen notitie, run 27)
C gedaan: Printables-strip niet vindbaar (#192); #181 verwerkt en voor Thijs gemeld op #182. Printables-API: `print(id){ datePublished firstPublish displayCount category{path{name}} tags{name} downloadCount likesCount makesCount }` werkt; een veld voor het AI-label heb ik niet gevonden. Help-pagina's van Prusa laden pas in de browser (curl geeft lege opmaak); het Prusa-forum wel met `curl -sL` (met slash aan het eind). C is bijna op: reviewvraag, testers, inhoudspagina's, upsell en eigen pagina's liggen er al; link naar Pro in de gratis add-on mag niet (Extensions 6.1 tot 6.3). Volgende run: A (plekken) volgens rooster, maar eerst #186 en #192 lezen (#186 ja: in de bundel van de volgende dag en "bundel voor Thijs"; #192 ja: "klaar om te plaatsen" bij de hoofdchat, via #182 zolang hoofdchat.md vol is) en vanaf vr 27 nov meten: CG Channel-link, Addon Radar, CYBER25-verkopen, Printables-downloads en of de strip in `searchPrints2` verschijnt.

## 26 nov 2026, van Verspreider (eigen notitie, run 28)
A gedaan zonder nieuwe plek: A is op tot de lancering van Click Cuts (zie LOG). Printables-groepen zoeken: `searchGroups2(query:"..."){ items { id name slug membersCount } }`; `group(id)` heeft geen description. Arctic Shift geeft 422 na een paar vragen: hooguit 3 vragen per run, 5 s pauze. Volgende run: B (outreach) volgens rooster, maar eerst #192 lezen (ja: "klaar om te plaatsen" bij de hoofdchat) en vanaf vr 27 nov meten: CG Channel-link, Addon Radar, CYBER25-verkopen, Printables-downloads. Volgende A: plekken voor Click Cuts zodra die live staat (r/3Dprinting-vragen over te groot voor het bed, Blender Artists-draadje vanaf ±6 dec).

## 26 nov 2026 16:30 NL, van Bram: deel 1 gedaan, deel 2a bij de hoofdchat
Deel 1 (dortus.com, drie plekken) live in dortus 9e3d0d4 (curl 16:2x, 0 keer "print tested", GEZIEN). Deel 2a staat in `producten/blender-gewrichten/repo-click-joints/README.md`; de hoofdchat pusht naar click-joints (buiten mijn toegang). 2b liet ik weg: extra weghaalklus op 2 dec voor weinig bereik.

## 26 nov 2026, van Verspreider (eigen notitie, run 29)
B gedaan: Katsby voor Click Cuts (#202). Pro-outreach is op bij deze lat: YouTube en Printables zijn in run 17 tot 29 afgezocht; nieuwe B-runs richten zich op Click Cuts (3D Printer Academy en Milad Kambari staan als B bewaard). Hulpje kanaal: `/@naam/about` geeft abonnees in `"content":"... subscribers"` en links in `"link":{"content":...}`. Volgende run: C (eigen mensen) volgens rooster, maar eerst #202 lezen (ja: in de bundel van de lanceerdag van Click Cuts en "bundel voor Thijs") en vanaf vr 27 nov meten: CG Channel-link, Addon Radar, CYBER25-verkopen, Printables-downloads.

## 26 nov 2026, van Verspreider (eigen notitie, run 30)
C gedaan: antwoord aan makers met de code (#206). Eigen-mensen deel 1 tot 3 (reviewherinnering, inhoudspagina's) staan sinds 26 nov als klaar om te plaatsen maar nog niet in geplaatst.md; gemeld bij de hoofdchat. Volgende run: A (plekken) volgens rooster, maar eerst #202 en #206 lezen (#206 ja: in de bundel van de volgende dag en "bundel voor Thijs", MetalBricks met voorrang) en vr 27 nov meten: CYBER25-verkopen, CG Channel-link, Addon Radar, Printables-downloads, gebruik makerscodes.

## 26 nov 2026, van Verspreider (eigen notitie, run 31)
A gedaan: Stack Exchange-antwoord kogelgewricht, gratis Click Joints (#211); #202 M1 en M2 verwerkt in Katsby. Zoeken op Stack Exchange: `search/advanced?site=blender&q=...&sort=creation` met zoekwoorden ball joint print, articulated print, hinge print; alleen 209724 en 109488 passen, Stack Exchange is daarmee op tot er nieuwe vragen komen. Arctic Shift: `posts/search?subreddit=X&title=print&after=...` werkt, `query=` geeft Timeout. Volgende run: B (outreach) volgens rooster, maar eerst #206 en #211 lezen (#206 ja: in de bundel van de volgende dag en "bundel voor Thijs", MetalBricks met voorrang; #211 ja: in de bundel voor Thijs, plaatsen ma 30 nov of later) en vr 27 nov meten: CYBER25-verkopen, CG Channel-link, Addon Radar, Printables-downloads, gebruik makerscodes.

## 26 nov 2026, van Verspreider (eigen notitie, run 32)
B gedaan: 3D Jesus voor Click Cuts (#216); #206 verwerkt in bundel 27 nov deel 2 (MetalBricks met voorrang). Click Cuts-outreach op YouTube is nu ook bijna op: alleen 3D Jesus en Katsby hebben adres, passend onderwerp en de goede grootte; AbeLeal3D en AquaCatz bewaard als B. Hulpje: zoeken met `&sp=CAI%253D` (nieuwste eerst) en dan `/@naam/about` voor abonnees en de beschrijving (adres maskeren voor je het opschrijft). Volgende run: C (eigen mensen) volgens rooster, maar eerst #211 en #216 lezen (#211 ja: in de bundel voor Thijs, plaatsen ma 30 nov of later; #216 ja: bij Katsby in de bundel van de lanceerdag Click Cuts) en vr 27 nov meten: CYBER25-verkopen, CG Channel-link, Addon Radar, Printables-downloads, gebruik makerscodes.

## 26 nov 2026, van Verspreider (eigen notitie, run 33)
C gedaan zonder nieuwe tekst: C is op; #211 en #216 verwerkt en samen in `bundel-2026-11-30.md` (lanceerdag). Downloads tellen: HTML-tags weghalen met `sed 's/<[^>]*>/ /g'` vóór `grep -o "Downloads [0-9,]*"` (anders leeg). Volgende run: A (plekken) volgens rooster; A is op tot Click Cuts live staat, dus vr 27 nov vooral meten: CYBER25-verkopen, CG Channel-link, Addon Radar, Printables-downloads, gebruik makerscodes. Het SE-antwoord Click Cuts (#166) pas een paar dagen na het kogelgewricht-antwoord, in een latere bundel.

## 26 nov 2026, van Verspreider (eigen notitie, run 34)
A gedaan: voorstel betaald BlenderNation-bericht Pro (#225). BlenderNation-formulier: "Commercial promotions require a 'Commercial Blender User' membership on our Patreon ... one-off post EUR 25"; feed `blendernation.com/feed/` werkt met curl en een browser-user-agent, zoeken (`?s=` en wp-json) geeft Cloudflare. Volgende run: B (outreach) volgens rooster, maar eerst #225 lezen (ja: onderaan hoofdchat "voor Thijs (geld): EUR 25 BlenderNation, tekst klaar", insturen vr 27 nov) en vr 27 nov meten: CYBER25-verkopen, CG Channel-link, Addon Radar, Printables-downloads, gebruik makerscodes.

## 26 nov 2026, van Verspreider (eigen notitie, run 35)
B gedaan zonder nieuwe mail: zes kanalen en twee blogs gewogen, niemand met passend onderwerp, goede grootte én zakelijk adres (zie LOG). YouTube-zoekpagina parsen: niet met één grote regex (hangt), maar splitsen op `"videoRenderer":{` en per stuk zoeken. Volgende run: C (eigen mensen) volgens rooster, maar C is op; vr 27 nov is de eerste saledag, dus vooral meten: CYBER25-verkopen, CG Channel-link, Addon Radar, Printables-downloads, gebruik makerscodes, en of Thijs ja zei op EUR 25 BlenderNation (#225 ja, K2 verwerkt, gemeld bij de hoofdchat).

## 27 nov 2026, van Verspreider (eigen notitie, run 37)
A gedaan als meting: CG Channel-lijst en Addon Radar bevestigd (zie LOG). Hulpjes: CG Channel-feed is oud (2024), lees de homepage en zoek `href="/2026/11/black-friday...`; Addon Radar: `addonradar.com/sitemap.xml`, pagina's onder `/addon/<slug>/` (niet `/addons/`); Gumroad Discover: `gumroad.com/products/search?query=...&from=N` met header `accept: application/json`. Volgende run: B (outreach) volgens rooster; Pro-outreach is op, dus alleen als er een echte print of foto van een koper is, anders meten (Superhive on_sale, Addon Radar Black Friday-pagina, downloads, antwoorden 80.lv en Digital Production in de outreach-map).

## 27 nov 2026, van Verspreider (eigen notitie, run 38)
B gedaan zonder nieuwe mail (zie LOG). Zoeken via curl op duckduckgo, bing en brave werkt niet vanuit deze omgeving (000 of lege uitkomst); WebSearch werkt wel. YouTube-zoeken met `&sp=CAI%253D` blijft het beste hulpje. Volgende run: C (eigen mensen) volgens rooster; C is op, dus meten: Superhive on_sale, downloads, Printables-strip, en of de hoofdchat "Automatically apply" voor CYBER25 aanzette. Volgende echte B pas bij een foto van een koper of de lancering van Click Cuts (zo 29 nov).

## 27 nov 2026, van Verspreider (eigen notitie, run 39)
C gedaan: salelink op eigen pagina's (#241). Hulpje: `bash platformen/blender/sale-controle.sh` meet in één keer Gumroad-code, Superhive-prijs, After you buy en dortus.com. Eigen pagina's nalopen op salelink: curl en `grep -oi 'cyber25\|gumroad.com/l/click-joints-pro[^"< )]*'`. Volgende run: A (plekken) volgens rooster; A is op tot Click Cuts live staat (zo 29 nov), dus eerst #241 lezen (ja: "klaar om te plakken" onderaan hoofdchat, deel 1 Bram, deel 2 hoofdchat) en meten.

## 27 nov 2026, van Verspreider (eigen notitie, run 40)
A gedaan als controle zonder nieuwe tekst (zie LOG). Blender Artists: `search.json?q=<woorden>%20after:2026-11-20`; Stack Exchange: `fromdate=<unix>`. Arctic Shift gaf om ±03:57 alleen Timeout, ook op één verzoek. Volgende run: B (outreach) volgens rooster; Pro-outreach is op, dus alleen bij een foto van een koper, anders eerst #241 lezen (ja: "klaar om te plakken" onderaan hoofdchat) en meten. Zo 29 nov (Click Cuts live) gaan A en B weer open.

## 27 nov 2026, van Verspreider (eigen notitie, run 41)
B gedaan zonder nieuwe mail (zie LOG). blender-addons.org: formulieren op `/contact/` (Airtable), feed `/feed/` laat zien of ze nog plaatsen; pas zinvol als daar weer nieuwe add-ons verschijnen. Downloads: `sed 's/<[^>]*>/ /g' | tr -s ' \n' ' ' | grep -o "Downloads [0-9,]*"` (zonder `tr` leeg). Volgende run: C (eigen mensen) volgens rooster; C is op, dus meten. Zo 29 nov (Click Cuts live) gaan A en B weer open.

## 27 nov 2026, van Verspreider (eigen notitie, run 42)
C gedaan als meting zonder nieuwe tekst (zie LOG). A, B en C zijn alle drie op tot zo 29 nov (Click Cuts live) of een foto van een koper. Volgende run: A (plekken) volgens rooster; tot zondag alleen meten met `bash platformen/blender/sale-controle.sh` en de downloadregel, en kijken of er een nieuw issue met label verspreider is.

## 27 nov 2026, van Verspreider (eigen notitie, run 43)
A gedaan als controle zonder nieuwe tekst (zie LOG). Gratis Gumroad-pagina lezen: `data-page` uit de HTML halen en met `html.unescape` plus `json.loads` openen; tags staan onder `props.sections[0].search_results.tags_data`. Volgende run: B volgens rooster; tot zo 29 nov (Click Cuts live) alleen meten, tenzij er een issue met label verspreider of een foto van een koper is.

## 27 nov 2026, van Verspreider (eigen notitie, run 44)
B gedaan als controle zonder nieuwe mail (zie LOG). De Printables-strip staat na 4 dagen op 0 downloads: niet meer elke run meten. Volgende run: C volgens rooster; tot zo 29 nov (Click Cuts live) alleen meten, tenzij er een issue met label verspreider of een foto van een koper is.

## 27 nov 2026, van Verspreider (eigen notitie, run 45)
C gedaan als meting zonder nieuwe tekst (zie LOG). Volgende run: A volgens rooster; tot zo 29 nov (Click Cuts live) alleen meten, tenzij er een issue met label verspreider of een foto van een koper is.

## 27 nov 2026, van Verspreider (eigen notitie, run 46)
A gedaan als meting plus links in de bundels (wens Thijs 27 nov 09:50, zie LOG). Vanaf nu in elke nieuwe bundel en elk bericht voor Thijs bovenaan een blok "Links" met de GitHub-link van het bestand en de directe link naar elke plek. Volgende run: B volgens rooster; tot zo 29 nov (Click Cuts live) alleen meten, tenzij er een issue met label verspreider of een foto van een koper is.

## 27 nov 2026, van Verspreider (eigen notitie, run 47)
B gedaan als controle zonder nieuwe mail (zie LOG). Click Cuts staat nog niet op Gumroad; de lanceerbundel wacht op de echte link. Volgende run: C volgens rooster; tot zo 29 nov (Click Cuts live) alleen meten, tenzij er een issue met label verspreider of een foto van een koper is.

## 27 nov 2026, van Verspreider (eigen notitie, run 48)
C gedaan als meting zonder nieuwe tekst (zie LOG). Volgende run: A volgens rooster; tot zo 29 nov (Click Cuts live) alleen meten, tenzij er een issue met label verspreider of een foto van een koper is.

## 27 nov 2026, van Verspreider (eigen notitie, run 49)
A gedaan als meting zonder nieuwe tekst (zie LOG). Volgende run: B volgens rooster; tot zo 29 nov (Click Cuts live) alleen meten, tenzij er een issue met label verspreider of een foto van een koper is.

## 27 nov 2026, van Verspreider (eigen notitie, run 50)
B gedaan als meting zonder nieuwe mail (zie LOG). Volgende run: C volgens rooster; tot zo 29 nov (Click Cuts live) alleen meten, tenzij er een issue met label verspreider of een foto van een koper is.

## 27 nov 2026, van Verspreider (eigen notitie, run 51)
C gedaan als meting zonder nieuwe tekst (zie LOG). Printables kreeg om ±14:00 gerenderde beelden en Engelse STL-namen (#257, commit 4329a3a): zodra die live staan kan A (Printables, MakerWorld) weer open. Volgende run: A volgens rooster; tot zo 29 nov (Click Cuts live) alleen meten, tenzij er een issue met label verspreider, een foto van een koper of de nieuwe Printables-pagina live is.
