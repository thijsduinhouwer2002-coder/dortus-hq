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
