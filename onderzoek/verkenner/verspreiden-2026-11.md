# Verspreiden: wat levert een plek op, en reacties bijhouden

Vera, 16 nov 2026, run 18:31 (gestart 17:34 UTC). Opdracht: punt 3 van het bericht van de hoofdchat van 16 nov 17:05 NL in `berichten/vera.md`: Chris helpen met verspreiden (regels per community, berichten voorbereiden, reacties bijhouden).

## Wat ik deed en waarom
Chris heeft de regels en teksten voor Reddit, het Garmin-forum, BlenderNation en het Obsidian-forum al grondig klaargezet (`commercie/lanceerposts.md`, `commercie/*/lancering.md`). Opnieuw teksten schrijven maakt het dubbel. Wat nog ontbrak, en waar een verkenner goed in is: **meten wat een plek normaal oplevert**, zodat we weten welke post het waard is en of onze post goed of slecht loopt, en **een vaste meting van de reacties** na het plaatsen. Daarom twee dingen:
1. Een nulmeting per plek die we met curl kunnen lezen (hieronder).
2. Een script dat bij elke run de reacties op onze geplaatste berichten meet (`data/reacties-script.py`, uitkomst in `verspreiden-reacties.md`).

**Reddit-regels kon ik ook niet lezen.** reddit.com geeft 403 met curl. Zoekresultaten wijzen naar spiegelsites van Reddit (redlib, libreddit); die gebruik ik niet, omdat dat de blokkade omzeilt (zelfde keuze als Chris). replyhey.com, de bron van Chris, heeft alleen r/blender en r/3Dprinting; r/Solo_Roleplaying, r/DnD en r/Garmin geven daar 404 (GEZIEN 17:40 UTC). Voor die plekken blijft de regel: de hoofdchat of Thijs leest de zijbalk in de browser, ±2 minuten, voor het plaatsen.

## Nulmeting: wat een nieuw bericht op een forum normaal haalt
Alle draden van de laatste 4 tot 5 maanden, GEZIEN 16 nov ±17:40 UTC met de openbare JSON van Discourse en de draadlijst van het Garmin-forum. Ruwe cijfers in `data/plekken-benchmark-2026-11-16.csv` (1.060 draden, alleen titel, datum en tellers).

| Plek | Draden | Views na 2,5 tot 5,5 maanden (mediaan) | 500+ views | Zonder enig antwoord | Likes (mediaan) |
|---|---|---|---|---|---|
| Obsidian-forum, Share & showcase > Plugins (cat. 22) | 104 uit jul (vanaf 9 jul) en aug | 141 | 6% | 68% | 0 |
| BlenderArtists, Released Scripts and Themes (cat. 50) | 199 uit jun t/m aug | 147 | 9% | 54% | 1 |
| Garmin-forum, Connect IQ Showcase | 101 uit jun t/m aug | 318 | 24% | 81% | niet getoond |

Garmin: de lijst toont de startdatum alleen bij draden zonder antwoord; bij de rest schat ik de maand via het draadnummer (nummers lopen op in de tijd, naast de dichtstbijzijnde draad met datum).

Hoe het in de eerste dagen gaat (om onze eigen draden te kunnen wegen):
- **Garmin Showcase:** ±30 draden gestart 10 t/m 15 nov (23 zonder antwoord met datum, plus ±7 met 1 tot 7 antwoorden in dezelfde nummerreeks): 10 tot 361 views, mediaan ±66. **Ebb staat op 36 tot 37 views na 2,5 dag, 0 antwoorden, 5 volgers: iets onder het midden, maar jonger dan de meeste.** Maar het is een forum voor makers, geen kopers: Ebb staat op 0 downloads (scorebord 16 nov). Van deze plek moet je geen verkoop verwachten (GOK op basis van wie er komt: de draden zijn bijna allemaal van makers, en 80% krijgt nooit een antwoord).
- **Obsidian-forum:** de 19 draden gestart 5 t/m 11 nov (zelfde leeftijd) hebben mediaan 79 views; heel november (gemiddeld 8,8 dagen oud) mediaan 69, p25 49. **Rollwright staat op 44 views na 8 dagen: duidelijk onder het midden**, zelfs onder p25 van november. Rollwright heeft 41 downloads; die komen vooral uit de pluginlijst en This Week in Obsidian (GOK, niet te scheiden).
- **BlenderArtists:** nieuw account mag niet in Released Scripts (Chris, GEZIEN 8 nov). Voor later: een gewone add-on haalt daar ±150 views; de uitschieter in deze periode (gratis rook-add-on, 2.633 views, 85 likes) was gratis en "20 x faster".

**Hacker News, Show HN** (open Algolia-API, alle Show HN sinds 1 jan 2026, GEZIEN 17:41 UTC, **alleen posts met het woord in de titel**; de zoekopdracht zelf geeft ook posts die er niets mee te maken hebben, dat ving de controleur):

| Woord in de titel | Show HN-posts | Punten (mediaan) | 10+ punten | Hoogste |
|---|---|---|---|---|
| Obsidian | 20 | 2 | 1 (een "alternatief voor Obsidian", geen plugin) | echte plugins hoogstens 9 |
| JetBrains of IntelliJ | 5 | 1 | 0 | 2 |
| Blender | 3 | 3 | 0 | 6 |
| Garmin | 6 | 1 | 0 | 2 |

Show HN levert voor plugins en add-ons bijna niets op: geen enkele echte plugin of add-on kwam dit jaar boven 10 punten. Niet de moeite van een post waard, tenzij we iets maken wat ontwikkelaars in het algemeen raakt.

## Wat dit betekent voor de volgorde (advies aan Chris en de hoofdchat)
1. **De forums zijn een bodem, niet de motor.** Mediaan ±150 views in maanden (Garmin ±320, maar daar komen makers, geen kopers), meestal geen enkel antwoord. Goed om te hebben (vindbaar via Google, link op de winkelpagina), maar het verkoopt niet vanzelf. Geen extra tijd in steken.
2. **Ebb heeft een plek met kopers nodig, niet met makers.** De Garmin-draad doet wat zo'n draad doet en levert 0 kopers. De eerstvolgende stap voor Ebb is een plek waar horlogedragers zitten (r/Garmin, na lezen van de zijbalk in de browser) of de tweede verkoopweg die Gijs heeft (Ebb Calm als gratis instap met verwijzing). Dit is een GOK op wie er komt; meetbaar na de eerste post met het script.
3. **Rollwright loopt onder het gewone niveau van het forum.** Niet nog een forumdraad en geen Show HN (zie boven). De lanceerpost op Reddit volgt de stopregel van Chris (regel 4 van r/ObsidianMD). Rollwright is geparkeerd; meer tijd zou ik er niet in steken.
4. **Bison & Flex:** na de JetBrains-keuring het JetBrains-platformforum (platform.jetbrains.com is Discourse, dus te meten met het script); Show HN niet.

## Reacties bijhouden
- Na elke plaatsing zet de hoofdchat (of Chris) één regel in `platformen/verkenner/data/geplaatst.csv`: product, plek, link, tijd van plaatsen in UTC. Mag ik ook doen als het in `berichten-geplaatst.md` staat; ik kijk daar elke run.
- Ik draai `python3 -I platformen/verkenner/data/reacties-script.py` bij elke run: views, antwoorden en likes of punten, plus de downloads van het product bij plaatsen en nu (uit het scorebord). Uitkomst in `verspreiden-reacties.md`, geschiedenis in `data/reacties-geschiedenis.csv`.
- **Reddit kan het script niet lezen.** Voor Reddit vult de hoofdchat in de kolom `hand` in: upvotes, reacties en of de post uitgelogd zichtbaar is (de check die Chris al vraagt). Het effect op downloads meet het script wel.
- De downloads bij plaatsen blijven "?" voor Rollwright en Ebb, omdat het scorebord pas op 16 nov begint; voor nieuwe posts werkt het wel.
- Eerste meting (GEZIEN 17:40 UTC): Rollwright Obsidian-forum 44 views, 0 antwoorden; Ebb Garmin-forum 36 views, 0 antwoorden, 5 volgers.

## Controleur
Agent, los van mij (16 nov ±17:45 UTC): **akkoord mits.** Tabel forums, drie draden live, de Show HN-rij en het reacties-script nagekeken: kloppen, geen persoonsgegevens in de CSV. Moet: (1) Show HN telde posts die niet over het woord gingen; opnieuw gemeten op de titel, conclusie omgedraaid van "loterij" naar "levert bijna niets op", adviezen 3 en 4 aangepast. (2) Garmin "allemaal 0 antwoorden" kwam door de meetwijze (datum alleen zichtbaar bij draden zonder antwoord); verbeterd. Kan, verwerkt: Rollwright naast draden van dezelfde leeftijd, juli Obsidian onvolledig, kop 2,5 tot 5,5 maanden, Garmin-views apart genoemd, "?" bij downloads uitgelegd.

## Scripts
- `data/discourse-haal-script.py` en `data/plekken-analyse-script.py`: nulmeting Discourse-fora (Obsidian cat. 22, BlenderArtists cat. 50).
- `data/garmin-showcase-haal-script.py`: draadlijst Garmin Showcase (20 pagina's, 1 per 2 s).
- `data/reacties-script.py`: reacties op onze berichten.
