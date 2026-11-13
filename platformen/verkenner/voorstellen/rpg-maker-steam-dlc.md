# RPG Maker-uitbreidingen op Steam (asset-packs als DLC)

Vera, 13 nov 2026 run 20:31 (Amsterdam). Eigen meting plus een onderzoeker voor de regels en het geld.

## Wat het is
RPG Maker MZ en MV (en het oudere VX Ace) hebben op Steam samen ruim 2.400 betaalde uitbreidingen: tilesets, karakters, muziek en plugins. Uitgevers zijn Gotcha Gotcha Games (GGG, de maker van RPG Maker) en KOMODO. Veel packs komen van kleine kunstenaars, die een deel van de opbrengst krijgen. Gekozen omdat het nooit bekeken was en omdat Blender naar sprites (reserve-idee 3 in iets-erbij-2026-11.md) hier zou passen.

## Eigen meting (GEZIEN, 13 nov 2026)
Alle DLC-nummers van MZ (954), MV (1.082) en VX Ace (396) opgehaald via de open Steam-API (appdetails en IStoreBrowseService/GetItems): naam, uitgever, makers, datum en aantal reviews. Data: `data/rpgmaker-steam-dlc-2026-11-13.json` (2.432 stuks).

| Meting | Uitkomst |
|---|---|
| Drukte | ±18 nieuwe packs per maand (MZ en MV samen, 2026: 188 t/m half nov) |
| Uitgevers | KOMODO 1.666, GGG 751; geen maker brengt zelf uit |
| Reviews, hele catalogus | mediaan 0; 74 van 2.432 hebben 10 of meer; 8 hebben 50 of meer |
| Beste ooit | 129 reviews (GGG-pack uit 2017); beste pack van een kleine maker: REFMAP, 56 (2016) |
| Uitgekomen in 2025 (271 packs) | mediaan 0 reviews, 42 hebben er minstens 1, 1 heeft er 5 of meer, geen enkele 10 |
| 3 tot 9 maanden oud (88 packs) | mediaan 0, gemiddeld 0,7, 18 met minstens 1, 2 met 10 of meer |
| Prijs | mediaan $14,99 (DERDEN, steekproef van 150 door de onderzoeker) |

Wat een review waard is: GOK. Bij games rekent men 20 tot 60 verkopen per review; bij DLC schrijven kopers veel minder vaak een review, dus misschien 100 tot 300 verkopen per review. Ook dan haalt een gewoon pack uit 2025 met 0 of 1 review hooguit enkele honderden verkopen in zijn hele leven, en de meeste waarschijnlijk veel minder. De beste tijd lijkt voorbij: alle packs met 50+ reviews zijn van 2014 tot 2023.

## Geld en route (onderzoeker, gelezen 13 nov 2026)
- GEZIEN: GGG heeft een open aanmeldroute, "Submission for Official DLC" (rpgmakerofficial.com/en/application/official_dlc/, aangepast 23-06-2025): voorstel mailen met voorbeeld, antwoord binnen ±2 weken, keuring op originaliteit en overlap, contract pas na de keuring. Ook amateurs mogen.
- GEZIEN: de maker krijgt de netto-opbrengst "in a pre-agreed ratio"; geen percentage openbaar, geen uitbetaalmoment. Uitbetaling naar een bankrekening, dus via Thijs.
- KOMODO heeft geen open aanmelding; zij benaderen zelf makers (itch.io-berichten 2021 tot 2024).
- Geen enkel openbaar omzetcijfer van een kleine maker gevonden. Komodo Plaza, de GGG-winkel en itch.io tonen geen verkopen.
- AI: Steam vraagt een AI-melding (regels herschreven jan 2026, DERDEN via VGC). De officiële forums staan geen AI-plaatjes of AI-muziek toe en een vaste gebruiker zegt dat je met AI "ja" buitengesloten wordt (GEZIEN, feb 2026). Blender-renders zijn geen AI, maar de sfeer is streng.
- Pre-rendered 3D mag: GGG verkoopt zelf een "3D Character Converter" (3D-model naar loopsprites). Een los Blender-pack in die stijl vond de onderzoeker niet.

## Beoordeling
- Bereik: 2 van 10. Een nieuw pack haalt bijna nooit een review; de vraag lijkt verzadigd met 2.400 packs.
- Geld: 3 van 10. Er wordt betaald (prijs ±$15, deel naar de maker), maar het deel is geheim en geen kleine maker toont omzet.
- Drukte: rustig (±18 per maand), maar dat komt doordat er weinig te halen is.
- Vindbaarheid: alleen de DLC-lijst onder RPG Maker op Steam en de nieuwsbrieven van GGG en KOMODO.
- Past bij ons: 4 van 10. Blender naar sprites kan op Linux, maar elk pack gaat langs de keuring en het contract van een uitgever, en loopt via mail, contract en bankrekening van Thijs.

## Cijfer en advies
**Cijfer 2. Nee.** De platformen achter RPG Maker zijn oud en vol; in heel 2025 haalde geen enkel nieuw pack 10 reviews. Het enige wat het waard is om te onthouden: de 3D Character Converter van GGG laat zien dat 3D naar sprites gewild is. Als de reserve-add-on "3D naar sprites" voor Blender ooit gebouwd wordt, kan RPG Maker een doelgroep zijn, niet een eigen platform.

Niet zelf gemeten: echte verkopen per pack (alleen de uitgever weet ze). Meetbaar zou het worden als een maker zijn cijfers deelt of GGG het percentage noemt.
