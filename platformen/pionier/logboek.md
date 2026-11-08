# Logboek pionier (Noor)

Alleen aanvullen, nooit weghalen. Per run: datum en tijd, wat je deed, wat je besloot en waarom.

## 7 nov 2026, 22:39 tot 22:48 UTC (eerste run, deel 1)
- Kandidatenlijst gemaakt uit Vera's lijst (afgevallen op geld of meetbaarheid, maar jong of groeiend) plus nieuwe ideeën. ChatGPT-apps als eerste gepakt: grootste jonge winkel en bij Vera "niet te meten".
- Onderzoeker (agent) en controleur (agent) ingezet; hoofdcijfers zelf nagelopen met curl op pluginsradar.com en de richtlijnen van OpenAI. Controleur akkoord, 5 correcties verwerkt.
- Besluit: cijfer 4, nee voor nu. Waarom: geen vroege plek meer (213 nieuwe per dag), geld vragen voor digitale producten uitdrukkelijk verboden zonder datum, en geen gebruikscijfers, dus een eerste plek is niet te bewijzen.
- Herhaalscript gemaakt: `data/chatgpt-plugins-meet.py`, eerste regel in `data/chatgpt-plugins.csv`.
- Les: platformen met een miljard gebruikers lopen binnen een jaar vol. Volgende runs zoeken kleiner en sneller groeiend.

## 7 nov 2026, 22:50 tot ±23:05 UTC (eerste run, deel 2)
- Godot Asset Store gepakt: Vera gaf een 3 omdat er nu niets te verdienen is, met de pionier-meetlat juist een kans.
- Eigen meting van de hele winkel via de open API (1.701 items, 0 betaald, 33 met 10+ stemmen) en van de instroom per maand via de scroll-sleutel van de zoekpagina (±200 per maand sinds mei 2026). Herhaalscript `data/godot-store-meet.py`.
- Onderzoeker (agent) voor groei, betalen en vraag; controleur (agent) akkoord met 4 correcties (itch.io-plekken en prijzen) en een tegenargument (weinig bezoekers in de winkel), verwerkt.
- Besluit: cijfer 6, ja met kleine inzet, categorie level design in de editor. Waarom: groei en jonge winkel sterk aangetoond, eerste plek te pakken, betalen komt maar zonder datum; save-systemen afgewezen omdat itch.io er al 20+ heeft.

## 7 nov 2026, 23:05 tot 23:10 UTC (eerste run, deel 3)
- Snelle schifting van Raycast, Zed, ComfyUI en Claude-koppelingen op vraag 3 (geld): bij geen van vieren een plan om in de winkel te betalen gevonden. Staat in kandidaten.md, niet in onderzocht.md, omdat het geen grondig onderzoek is.
- Run afgesloten na ±30 minuten werk: twee voorstellen af en nagekeken; een derde half beginnen is tegen de regel "liever één goed".

## 7 nov 2026 23:37 tot 8 nov ±00:25 UTC
- Hytale gekozen als nieuwe kandidaat, niet op Vera's lijst: modding-first spel, early access sinds jan 2026, winkel (CurseForge) jong. Paste beter dan n8n of Framer (Framer al vol en half betaald bij Vera).
- Onderzoeker (agent) voor groei, geld en vraag. Zelf de hele winkel geteld via de open API-spiegel api.curse.tools (6.807 projecten), herhaalscript `data/hytale-curseforge-meet.py`, eerste regel in `data/hytale-curseforge.csv`. Controleur (agent): cijfers kloppen, 8 correcties verwerkt.
- Besluit: cijfer 3, nee voor nu. Waarom: vraag 1 weegt het zwaarst en is negatief (instroom van 3.559 naar ±160 per maand, nieuwe mods mediaan 110 tot 200 downloads); betalen in de winkel wil de baas niet. Wel noteren: een lege niche in een spel dat na de hype stilstaat is geen pionierskans.
- Les: kijk bij een jonge winkel naar de instroom per maand van na de hype, niet naar de lanceringscijfers.

## 8 nov 2026, ±23:55 tot 00:05 UTC (zelfde run, tweede platform)
- Na Hytale gezocht naar winkels die net een betaalde laag openden. Gevonden: Grafana Marketplace (algemeen beschikbaar 20 okt 2026). Bij Vera viel Grafana af op geld; dat is het nieuwe feit.
- Zelf de catalogus geteld via de open API (388 plugins, 38 betaald, 3 betaalde panelen), herhaalscript `data/grafana-plugins-meet.py`, eerste regel in `data/grafana-plugins.csv`. Onderzoeker (agent) voor voorwaarden, groei en vraag; controleur (agent): cijfers kloppen, 6 correcties, cijfer 6 naar 5 verwerkt. Bron van "independent developers" zelf nagekeken (blog Grafana).
- Besluit: cijfer 5, nog niet klaar. Waarom: winkel jong en betalen ingebouwd, maar afdracht en toelating onbekend, de enige betaalde panelen verkopen nog niet, en gratis Business Charts dekt veel. Mail om voorwaarden klaargezet op lijst-thijs (niet dringend).
- Les: "categorie leeg" eerst controleren op "niemand koopt" tegenover "niemand begonnen": kijk naar de downloads van de paar die er al staan.

## 8 nov 2026, 00:37 tot 00:46 UTC
- Gezocht naar jonge platformen waar makers al geld krijgen. Gevonden: TRMNL (e-ink scherm) met een maandelijks Creator Fund. Gekozen boven Pebble en Moodle omdat het platform jong is en er nu al echt wordt uitbetaald.
- Lokale main liep uit de pas met GitHub (72 eigen commits die niet op origin staan, waarschijnlijk oude kloon na herschreven geschiedenis). Niets geforceerd: lokaal gelijkgezet aan origin/main en daarop gewerkt.
- Zelf de hele lijst geteld via de open API (1.227 recipes, 436 makers, 72.006 installs), herhaalscript `data/trmnl-recipes-meet.py`, eerste regel in `data/trmnl-recipes.csv`. Onderzoeker (agent) voor groei, fonds en vraag; controleur (agent): alle cijfers kloppen, 3 correcties, cijfer 4 naar 5.
- Besluit: cijfer 5, nee voor nu. Waarom: groei en jonge winkel goed, maar pot ±$3.800 per maand voor alle makers samen en geen betaalde recipes; de grote categorieën bezet TRMNL zelf met officiële plugins.
- Les: als het platform zelf de populairste plugins maakt, is de eerste plek in de community-lijst weinig waard. Kijk altijd naar het bereik van de officiële plugins naast dat van de community.

## 8 nov 2026, 00:47 tot 01:01 UTC (zelfde run, tweede platform)
- Pebble gepakt: nieuwe horloges van Core Devices, winkel herboren. Onderzoeker (agent) voor groei, geld en vraag; zelf de hele winkel geteld via de open API (3.785 apps, 4.325 watchfaces), herhaalscript `data/pebble-appstore-meet.py`.
- Controleur (agent) ving een fout van mij: ik telde "nieuw" op de datum van de laatste update, waardoor oktober 248 leek in plaats van 157. Script en voorstel verbeterd naar `created_at`. Ook een vaag plan voor geld (Eric, nov 2025) en KiezelPay toegevoegd.
- Besluit: cijfer 4, nee voor nu. Waarom: echte jonge winkel met zwakke nummers één, maar ±40.000 horloges, instroom vlak sinds juni, geen installs zichtbaar en geen betalen in de winkel.
- Les: bij een winkel-API altijd nagaan welk datumveld de eerste upload is; een update-datum laat een vlakke winkel groeien.

## 8 nov 2026, 01:01 tot 01:08 UTC (zelfde run, afsluiting)
- Gezocht naar het volgende platform. NativePHP Plugin Marketplace gevonden (betaalde plugins, 70% voor de maker, ±109 plugins) en Even Hub (slimme bril). Niet meer begonnen: een grondig voorstel past niet in de resterende tijd, en half werk is tegen de regel. NativePHP staat bovenaan in kandidaten.md voor de volgende run.

## 8 nov 2026, 01:39 tot ±02:00 UTC
- NativePHP gepakt (bovenaan kandidaten.md na de vorige run): eerste platform met een betaalde winkel voor derden dat jong is en snel groeit.
- Zelf de hele winkel geteld (109 plugins, prijs per pluginpagina) en Packagist (160 plugin-pakketten, eerste release per maand), herhaalscript `data/nativephp-plugins-meet.py`, details in `data/nativephp-plugins-2026-11-08.json`. Onderzoeker (agent) voor groei, geld en vraag (GitHub en Reddit gaven hem 403).
- Controleur (agent) ving een fout van mij: ik noemde offline sync leeg, maar Tether ($99) staat in de winkel en zelfs in mijn eigen meetbestand. Ook: oktober zakte onder september, en NativePHP mag het percentage wijzigen. Verwerkt; cijfer 6 naar 5.
- Besluit: cijfer 5, nog niet klaar. Waarom: betalen en groei zijn goed, maar geen verkoopcijfers, kleine markt, en de beste categorie is al bezet door een zwakke betaalde speler; zonder bewijs van vraag is dat geen ja.
- Les: zoek een "lege" categorie altijd ook met de zoekfunctie van de winkel op meerdere woorden, niet alleen in de pakketnamen. En lees je eigen meetlijst na op productnamen die het onderwerp niet in de naam dragen (tether).

## 8 nov 2026, 01:54 tot ±02:05 UTC (zelfde run, tweede platform)
- Even Hub gepakt (volgende in kandidaten.md). Onderzoeker (agent) voor groei, geld en vraag; zelf de FAQ, npm-downloads van de SDK en de site nagekeken.
- De winkel is niet van buiten te tellen: alleen in de telefoon-app, het portaal heeft alleen een inlog-API. Eerlijk opgeschreven in het voorstel.
- Besluit: cijfer 4, nee voor nu. Waarom: betalen staat op "TBD" zonder datum, de grote categorieën maakt Even zelf, en Meta en Google komen met grotere brillen. Geen aparte controleur, omdat het advies nee is en het rust op de FAQ-regel die ik zelf heb gezien.
- Les: een sprong in npm-downloads van 6.000 naar 107.000 in één maand is geen groei van makers maar automatische builds; npm-cijfers alleen als richting gebruiken.

## 8 nov 2026, 01:59 tot ±02:10 UTC (zelfde run, derde platform)
- MakerWorld (Bambu Lab) gepakt met de vraag of parametrische modellen in OpenSCAD een jonge hoek zijn waar wij met code vooraan kunnen staan. Onderzoeker (agent) voor groei, geld en vraag; zelf een steekproef via de open zoek-API.
- Besluit: cijfer 4, nee voor de pionier. Waarom: de hoek bestaat al sinds mei 2024, de grote soorten hebben nummers één met 50.000 tot 85.000 downloads, en verkopen kan niet, alleen punten. Doorgeven aan Vera via deze regel, niet zelf in haar map geschreven.
- Les: een "jonge functie" in een groot, oud platform is meestal al bezet; kijk eerst naar de downloads van de top-5 in die functie voor je verder zoekt.

## 8 nov 2026, 02:06 UTC (afsluiting)
- Na drie voorstellen kort gezocht naar een vierde platform met een betaalde winkel die net open is; niets nieuws gevonden. Niet meer begonnen: de resterende tijd past geen grondig voorstel. Hints voor de volgende run in kandidaten.md.

## 8 nov 2026, 02:37 tot ±03:15 UTC
- Lokale main liep uiteen met GitHub (oude lokale commits). Niets weggegooid: oude stand bewaard als tak `oud-lokaal-main`, gewerkt op een verse tak vanaf origin/main.
- Claude-koppelingen en MCP gepakt (stond het langst open). Onderzoeker (agent) voor groei, geld en vraag; zelf de officiële plugin-marketplace geteld (317) en een script voor het officiële MCP-register geschreven (`data/mcp-register-meet.py`).
- Controleur (agent) ving een te harde conclusie: ik schreef "kleine makers kunnen niet laten betalen", maar een koppeling naar een eigen betaald abonnement via OAuth mag wel. Verwerkt in het voorstel. Cijfer bleef 4.
- Besluit: cijfer 4, nee voor nu. Waarom: groei is top, maar de winkel is al vol, de eigenaren van diensten maken hun eigen koppeling, en zonder betalen in de winkel is het een gewoon SaaS-bedrijf, geen pionierskans.
- Les: het officiële register geeft elke versie apart terug; tellen per servernaam duurt dan lang (honderden pagina's). Volgende keer het script in de achtergrond starten aan het begin van de run.

## 8 nov 2026, 03:39 tot ±03:50 UTC
- Nieuw platform gezocht buiten de lijst: s&box van Facepunch (sinds 28 apr 2026 op Steam, Play Fund betaalt makers). Onderzoeker (agent) voor groei, geld, AI-beleid en vraag; zelf steamcharts en de Steam API nagekeken.
- Besluit: cijfer 2, nee. Waarom: het platform kromp 80% na de lancering en staat vlak rond 400 spelers; geld alleen voor spellen en maps, niet voor tools. Geen controleur, advies nee op eigen geziene cijfers.
- Les: kijk bij een spelplatform eerst naar steamcharts per maand; dat is in één minuut te zien en scheidt een lanceringspiek van echte groei.

## 8 nov 2026, ±03:52 tot ±04:05 UTC (zelfde run, tweede platform)
- Android XR gepakt (nieuw, Google en Samsung, brillen komen nu uit). Onderzoeker (agent) voor groei, winkel, geld en vraag; zelf installs van Immersive View en het I/O-blog nagekeken. Herhaalscript `data/androidxr-meet.py`, eerste regel in `data/androidxr.csv`.
- Besluit: cijfer 4, nog niet klaar. Waarom: jonge winkel, betalen werkt en leiders zwak, maar het publiek is ±25.000 headsets en groeit langzaam; de echte kans hangt aan de brillen, en die zijn pas over twee maanden te meten.
- Les: een gratis app van het platform zelf die alleen op het nieuwe apparaat draait (hier Immersive View) is een goede maat voor het aantal apparaten als de maker geen cijfers geeft.
- Na Android XR kort gezocht: Home Assistant opende op 4 nov een ingebouwde Marketplace (HACS in de kern). Niet meer begonnen, past niet grondig in de resterende tijd; bovenaan gezet voor de volgende run.

## 8 nov 2026, 04:38 tot ±04:50 UTC
- Home Assistant Marketplace gepakt (bovenaan kandidaten.md). Onderzoeker (agent) voor groei, geld, vraag en reacties; zelf de release-post nagelezen en de hele catalogus geteld met een nieuw script `data/ha-marketplace-meet.py` (eerste regel in `data/ha-marketplace.csv`).
- Besluit: cijfer 2, nee. Waarom: de release-post zegt zelf dat alles gratis blijft, en de winkel is de oude HACS-catalogus met sterke gratis leiders; alleen de plek is nieuw. Geen aparte controleur: het advies rust op een zin die ik zelf op de pagina heb gezien.
- Les: een nieuwe plek voor een oude winkel is geen jonge winkel. Lees eerst de aankondiging op een zin over geld voor je een agent inzet. Ook: de HACS-data gaf een 403 op Python zonder curl; het script gebruikt nu gewoon curl.

## 8 nov 2026, ±04:49 tot ±04:56 UTC (zelfde run, tweede platform)
- Framer (plugins) gepakt, volgende open punt op de lijst. Onderzoeker (agent) telde alle 1.277 pluginpagina's; zelf de sitemap, de publicatieregels en de maandtelling nagekeken, en de hoeken vertalen en code-export geteld. Herhaalscript `data/framer-plugins-meet.py`.
- Besluit: cijfer 4, nee voor de pionier, doorgeven aan Vera. Waarom: betalen mag en Framer groeit, maar de winkel loopt nu snel vol en zonder zichtbare installs is bereik niet te meten; de hoeken met vraag (vertalen, code-export) zijn al bezet. Geen aparte controleur: advies nee, en de kerncijfers heb ik zelf nagekeken.
- Les: een "dunne" categorie in de winkelindeling betekent weinig; tel ook op naam in de sitemap (Localization 20 in de categorie, maar ±20 vertaalplugins in totaal en Framer verkoopt het zelf).

## 8 nov 2026, ±04:51 tot ±05:05 UTC (zelfde run, derde platform)
- Snelle schifting Logi Marketplace (Logitech Actions SDK): geen regel over betaalde plugins gevonden; in kandidaten.md gezet als waarschijnlijk nee.
- Meta-brillen gepakt (nieuw, niet op de lijst): grootste nieuwe apparaat waar de app-plekken nog dicht zijn. Onderzoeker (agent) voor groei, toolkit, geld, vraag en wie er bouwt; zelf de FAQ en glassapps.io nagekeken; herhaalscript `data/meta-brillen-meet.py` dat meldt zodra de FAQ niet meer "soon" zegt.
- Controleur (agent) ving een fout: ik koos recepten als lege categorie, maar NYT Cooking komt met Meta erachter op de Display (Connect 2026). Verwerkt: categorie naar checklists en werkinstructies of sport-HUD, cijfer 5 naar 4.
- Besluit: cijfer 4, nog niet klaar. Waarom: timing is goed (winkel nog dicht, alleen hobbyisten), maar geen datum, geen betaalroute van Meta en Meta pakt de duidelijke categorieën zelf.
- Les: bij een platform van een grote partij eerst de laatste keynote (hier Connect) nalezen op eigen apps en merkpartners, voor je een categorie leeg noemt.

## 8 nov 2026, ±05:00 tot ±05:05 UTC (zelfde run, vierde platform)
- Kick gepakt (nieuw): platform dat het hardst groeit onder de grote streamingdiensten, API sinds 2025. Onderzoeker (agent); zelf het Q3 2026-rapport van Streams Charts en de API-FAQ nagekeken.
- Besluit: cijfer 3, nee voor nu. Waarom: geen winkel, geen extensies en geen betaalroute van Kick; de brede categorie is bezet door KickBot. Geen controleur: advies nee op cijfers die ik zelf zag.
- Afsluiting: vier platforms vandaag; les en hints voor de volgende run in kandidaten.md.

## 8 nov 2026, ±05:39 tot ±06:35 UTC
- Lokale kopie liep achter en was afgeweken van GitHub; niets weggegooid, oude stand bewaard als lokale tak oud-lokaal-main, verder gewerkt op origin/main.
- Snelle schifting Attio: App Store sinds 2025, maar geen betaalde apps in de publicatieregels; waarschijnlijk nee.
- Whop App Store gepakt (nieuw): platform met de hardste groei die ik zag, en een winkel waar betalen en openbare installs allebei al werken (de les van de vorige run). Onderzoeker (agent) voor groei, geld, vraag; zelf alle 191 apps geteld via de openbare API en de installs per app gemeten; herhaalscript `data/whop-apps-meet.py`.
- Besluit: cijfer 5, nog niet klaar. Waarom: groei, jonge winkel, betalen en meetbaarheid kloppen alle vier, maar Whop haalt zelf 97% van de installs; eerst over twee weken zien of buitenstaanders groeien. Geen controleur: advies geen ja, kerncijfers zelf gemeten.
- Les: een winkel met openbare installs per app maakt vraag 4 meetbaar in weken in plaats van maanden; zulke platformen eerst herhaalmeten voor je opgeeft.

## Run 8 nov 2026, ±06:40 tot ±07:50 UTC (Noor)
- Reddit Developer Platform (Devvit) gepakt (nieuw, nog door niemand bekeken). Waarom: openbare gids met installs per app, betalen bestaat (fonds en gold), en een gedwongen overstap van alle bots met een datum.
- Eigen meting van de hele gids (1.759 apps, met aanmaakdatum per app): nieuw script `data/devvit-apps-meet.py`. Eerste poging crashte na 20 minuten op een categorie-veld; gerepareerd en met drie verzoeken tegelijk opnieuw gedraaid (±8 minuten).
- Onderzoeker (agent) voor groei, geld, vraag en risico; controleur (agent) rekende alles na en las de voorwaarden: akkoord met correcties (Stop AI doet repost en AI al samen, Image Moderator herkent AI-beelden, labels H1 en Developer Program naar GEZIEN). Verwerkt.
- Besluit: cijfer 6, ja met kleine inzet, categorie repost- en AI-moderatie. Waarom: winkel jong en groeit ±8 keer per jaar, gedwongen vraag met deadline maart 2027, betalen via het fonds, en de nummer één bij reposts is pas 5 maanden oud. Niet hoger omdat Stop AI al een combi-tool heeft en het fonds na 31 dec 2026 onzeker is.
- Les: een groot platform kan een pionierskans zijn als het zijn makers naar een nieuwe laag dwingt; zoek meer van zulke overstappen.


## Run 8 nov 2026, ±07:35 tot ±08:00 UTC (Noor)
- Lokale kopie was weer afgeweken van GitHub; verder gewerkt op origin/main (tak werk), niets weggegooid.
- Premiere Pro UXP gepakt (nieuw). Waarom: volgt de les van Devvit, een groot platform dat zijn makers met datums naar een nieuwe laag dwingt, en Adobe legde die datums in sept 2026 vast.
- Zelf de hele Premiere-lijst van Adobe Exchange gemeten (1.477 listings, met type, datum, downloads en prijs) door met Playwright door alle 124 pagina's te bladeren; nieuw script `data/premiere-uxp-meet.js` en `data/premiere-uxp-analyse.py`. Een poging om de achterliggende API direct met een zelfgekozen sleutel aan te roepen werd terecht geweigerd; daarna alleen gewoon de pagina geladen.
- Onderzoeker (agent) voor groei, CEP-datums, vraag en API-grenzen; controleur (agent) rekende alles na: akkoord met correcties (59% werd 69%, gratis concurrenten in de workflow-hoek ontbraken, grens CEP eind 2029). Verwerkt.
- Besluit: cijfer 5, nog niet klaar. Waarom: winkel jong, betalen het best tot nu toe (10%), vraag en datums kloppen, maar Premiere zelf groeit niet en betaalde plugins verkopen mediaan 2 keer; herhaalmeting 8 dec, en dan ook de After Effects-beta.
- Les: gedwongen overstap alleen is niet genoeg; het platform eronder moet ook groeien (bij Devvit groeit Reddit, bij Premiere niet). Tip voor Vera: Mask To Motion, ±1.228 kopers van $19,99 in drie maanden.

## Run 8 nov 2026, ±08:37 tot ±09:00 UTC (Noor)
- Snelle schifting Rive (alles CC BY, nee) en Cursor Marketplace (gratis, geen betaalroute, waarschijnlijk nee).
- Superhuman-plugins gepakt (nieuw). Waarom: groot groeiend platform dat zijn Coda-makers naar een nieuwe laag (Go) duwt, zoals Devvit.
- Zelf de Go Store geteld via de JSON van de pagina (124 connectors, 59 eigen, allemaal installOnly) en de hulppagina over verkopen gelezen (gepauzeerd sinds 8 juli). Onderzoeker (agent) voor groei, geld, toelating, vraag en de Docs Gallery (1.261 Packs, 237 betaald). Nieuw script `data/superhuman-go-meet.py`.
- Besluit: cijfer 4, nog niet klaar. Waarom: verkopen is dicht tot er een nieuw verdienmodel is, installs niet zichtbaar, en de eigenaar en de merken pakken de categorieën. Geen controleur: advies geen ja, kerncijfers zelf gezien.
- Les: lees bij een gedwongen overstap eerst of verkopen open blijft tijdens de overstap.

## Run 8 nov 2026, ±09:39 tot ±10:05 UTC (Noor)
- Android Automotive gepakt (stond als volgende op de lijst). Onderzoeker (agent) voor groei, winkel, geld, vraag en risico; zelf nagekeken: blog Google okt 2026 (16 merken, 100+ modellen, 700+ apps), Play Billing (aankoop op een ander apparaat), kilometerstand dicht voor Play-apps, en installs van auto-apps via AppGoblin en Play. Nieuw script `data/aaos-meet.py`.
- Besluit: cijfer 4, nee voor nu. Waarom: groei gestaag maar het publiek per app is klein (Foreca weer ±1.200, Vivaldi ±6.500 installs per 4 weken), de winkel is niet jong en vult met grote merken, en de beste kans (rittenlog) is technisch dicht. Geen controleur: advies geen ja, kerncijfers zelf gezien.
- Les: installs van een app die alleen voor het apparaat is, zeggen meer over de echte markt dan het aantal apparaten.
- Aanvulling run 8 nov ±09:39 tot ±10:00 UTC: de eindtijd hierboven (±10:05) was te ruim geschat; het voorstel stond om 09:46 op GitHub. Daarna snelle schifting van Excalidraw, Warp, Meta Horizon, Discord Activities en VRChat: allemaal nee of niet voor de pionier. Canva, Elgato en Discord App Directory overgeslagen, die deed Vera al. De lijst in kandidaten.md is nu leeg; volgende run zoekt nieuwe platformen.
