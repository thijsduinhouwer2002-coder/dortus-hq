# Voorstel: YouTube Playables (webspellen in YouTube)

Vera, 14 nov 2026, run 07:31 (Amsterdam). Nooit eerder bekeken, ook niet door Noor of Lotte.

## Wat het is
Playables zijn kleine webspellen (HTML5) die in de YouTube-app en op youtube.com draaien, zonder installeren. Gestart in mei 2024 in 7 landen, sinds eind september 2026 in meer dan 50 landen, ook de hele EU (DERDEN: https://shattered.io/youtube-playables-50-markets-zero-iap-2026/, die PocketGamer.biz en MobileGamer.biz aanhaalt). Geld komt alleen uit reclame (voorfilmpje, tussendoor, beloningsreclame). Kopen in het spel bestaat nog niet; Google wil dat in 2027 proeven (DERDEN, zelfde bron).

## De poort: zelf erin kan niet, via een uitgever wel
- **Zelf aanmelden kan niet.** Het Developer Portal is "Private Preview", "Participation is by invitation only" (GEZIEN, https://developers.google.com/youtube/gaming/playables/developer_portal, gelezen 14 nov 2026).
- **Geld voor makers is een proef met een paar makers.** "we are piloting revenue sharing with a select number of Playable creators" (GEZIEN, https://developers.google.com/youtube/gaming/playables/reference/monetization).
- **Maar uitgevers met toegang nemen spellen van kleine makers op.** Playgama ("Publish your game on YouTube Playables", "Monetization is live") en Mediacube (MC Play, "apply your games") doen dat zonder kosten vooraf en zonder exclusiviteit (GEZIEN, https://playgama.com/publish-your-game-on-youtube-playables/ en https://mediacube.io/en/blog/youtube-playables-monetization, bijgewerkt 11 nov 2026).
- **Wat de maker krijgt bij Playgama voor YouTube Playables:** 75% van de netto-opbrengst, Playgama houdt 25% (GEZIEN, "You keep 75%, we take 25%", https://playgama.com/publish-your-game-on-youtube-playables/). De trappen van 70, 80 en 90% op https://playgama.com/developers gelden voor hun eigen portalen, niet voor YouTube (controleur, voorwaarden developer.playgama.com/terms). Netto betekent na aftrek van kosten, en daar horen volgens de voorwaarden ook marketing, hosting en valutakosten bij (DERDEN, controleur). Uitbetalen via PayPal, Wise, crypto of bank, pas vanaf $100 (GEZIEN en controleur). Een gewone volwassen persoon mag meedoen, geen KvK nodig; de maker regelt zelf zijn belasting (controleur, voorwaarden, definitie "Developer").

## Eigen meting (GEZIEN)
Bron: de pagina https://www.youtube.com/playables (robots.txt staat die toe; `/youtubei/` is verboden, dus geen verder scrollen). De pagina geeft 60 spellen in de volgorde A tot Z (titels met een cijfer, A en het begin van B, tot "Ball Run"; chips "A to Z", "All" en "New", nagekeken door de controleur), elk met aantal plays, maker (Developer), uitgever (Publisher) en publicatiedatum. Omdat de volgorde alfabetisch is en niet op populariteit, is dit een redelijke steekproef van de ±2.500 spellen (dat totaal komt van Playgama, DERDEN). Ruwe data: `platformen/verkenner/data/youtube-playables-a-z-2026-11-14.json`, script `data/youtube-playables-haal.py`. Twaalf landen geprobeerd: steeds dezelfde 60.

Plays tot nu toe (plays zijn geen unieke spelers; één speler die tien keer speelt telt tien keer):

| Gepubliceerd | Aantal | Mediaan plays | Laagste | 100.000+ | 1 miljoen+ |
|---|---|---|---|---|---|
| 2023 t/m 2025 | 15 | 10.000.000 | 2.300.000 | 15 | 15 |
| 2026 jan t/m jun | 18 | 1.850.000 | 255.000 | 18 | 12 |
| 2026 jul t/m aug | 14 | 589.500 | 120.000 | 14 | 1 |
| 2026 sep t/m 14 nov | 13 | 574.000 | 16.000 | 10 | 6 |

- **Kleine makers via een uitgever (de route voor ons):** 21 van de 60 spellen hebben een andere uitgever dan maker. Playgama en Mediacube hebben samen 16 spellen (8 en 8); 10 daarvan zijn van een andere maker, 6 van de uitgever zelf (waaronder de grootste van Mediacube: 5,4, 3,3 en 2,8 miljoen). Makers via die twee: Bravestars (1,3 miljoen, sep), John Hany (8,8 miljoen, mrt 2026), Square Dino (2,1 miljoen mei; 406.000 okt), DudaGames (710.000, aug), Nulla Games (872.000, aug), Lory Games (576.000, aug), LISIK GAMES (284.000, aug), Izyplay (141.000, 11 okt). Laagste nieuwkomer in de hele steekproef: 16.000 plays na ±3 weken.
- **Wie er verder zit:** grote namen (Voodoo, Homa, CrazyLabs, Rovio, Miniclip, Supercent, FRVR) naast kleine studio's en eenmanszaken (Lütfi Altin, 5,2 miljoen met 2048 Cubes; 2D Hunter, 1,1 miljoen). Playgama en Mediacube zijn de grootste uitgevers in de steekproef (elk 8 van 60).
- **Vergelijking:** CrazyGames (Lotte, 9 nov) gaf mediaan 93.143 plays voor Full Launch-spellen; Playables geeft voor spellen van de laatste maanden ±575.000. Het bereik per nieuw spel is hier dus ongeveer zes keer zo groot, maar het is niet dezelfde soort meting: wat YouTube een play noemt is niet gedefinieerd, CrazyGames telt sessies, en daar ging het om een bijna volledige telling (301 spellen), hier om een steekproef van 27 nieuwe spellen op een platform waar je alleen via een uitgever in komt.

**Kanttekeningen bij de meting:**
1. Overlevers: spellen die YouTube verborg of weghaalde staan er niet in. Hoeveel dat er zijn, is van buiten niet te zien.
2. Alleen de eerste 60 van A tot Z. Meer kan alleen via `/youtubei/`, en dat verbiedt robots.txt. Niet omzeild.
3. 60 titels van A tot "Bal" past slecht bij 2.500 spellen (dan verwacht je er eerder 500 tot 900 tot die letters). Mogelijk is de A tot Z-lijst maar een deel van het aanbod, bijvoorbeeld wat in dit land te spelen is (GOK, controleur).
4. Hoeveel nieuwe spellen er per maand bijkomen, kon ik niet tellen. De steekproef heeft er 27 van jul t/m nov op 60 (45%), dus de stroom is groot en groeit (GOK op basis van die verhouding).

## Geld
- Betalen kan (reclame, via de uitgever), en de verdeling bij Playgama is openbaar (GEZIEN, zie boven).
- **Bewijs dat kleine makers verdienen is zwak en komt van belanghebbenden:**
  - Playgama zegt dat zijn spellen in de gesloten proef (vanaf maart 2026) gemiddeld ±$3.100 per maand verdienden (DERDEN, via shattered.io; cijfer van Playgama zelf, niet van YouTube).
  - Playgama noemt 200+ spellen op YouTube met samen 125 miljoen+ plays per maand, en 650 miljoen+ plays per maand "across all games" (DERDEN, Playgama; onduidelijk of dat alleen YouTube is).
  - Een maker op de Playgama-pagina meldt "revenue exceeding $5,000" (DERDEN, getuigenis op playgama.com/developers, niet alleen YouTube).
  - Mediacube: de eerste inkomsten komen binnen een paar dagen na livegang, door het voorfilmpje; reclame wordt nog niet bij elke play getoond (DERDEN).
- **Opbrengst per 1.000 plays is nergens gepubliceerd.** Als $3.100 per maand gemiddeld klopt met 125 miljoen plays over ±200 spellen, is dat ±$5 per 1.000 plays (GOK, rekensom op cijfers van Playgama zelf, waarschijnlijk te hoog). Voor CrazyGames is het enige echte cijfer €1,20 per 1.000 plays (Kees, 9 nov). Ik reken met $1 tot $3 per 1.000 plays voor de maker na afdracht (GOK).
- Wat dat betekent voor één nieuw spel als de mediaan van jul t/m nov (±575.000 plays in 1 tot 4 maanden): ±$600 tot $1.700 totaal, ±$150 tot $600 per maand (GOK). Een uitschieter met miljoenen plays geeft het tienvoudige.

## Vindbaarheid
In de Playables-hoek van YouTube (lijsten, genres, nieuw), aanbevolen tussen video's, en sinds sept 2025 via livestreams (Playables on Live: een streamer speelt, kijkers spelen mee) (DERDEN, shattered.io). Playgama zegt ook betaalde YouTube-reclame in te zetten bij een lancering (DERDEN). Spellen die op elkaar lijken mogen niet: YouTube weigert "duplicate uploads or builds substantially identical" (DERDEN, https://portalready.world/portals/youtube-playables/, nagelezen door die site op 30 sep 2026).

## Past het bij ons
- **Bouwen:** een gewoon HTML5-spel (Phaser, PixiJS, Defold, Godot web). Eerste download onder 30 MiB (15 aangeraden), elk bestand onder 30 MiB, geheugen onder 512 MB, SDK-aanroepen voor laden, opslaan, geluid en pauze (DERDEN, portalready.world, die de officiële eisen samenvat). Dat kunnen we op Linux bouwen en in headless Chrome testen. YouTube levert een eigen test suite.
- **Onze troeven:** Gloop en de Blender-renders uit Het Hol als plaatjes; het Garmin-arcadespel uit `iets-erbij-2026-11.md` zou in een webversie hetzelfde idee kunnen zijn. Eén spel kan via de Bridge SDK van Playgama ook naar andere portalen (MSN Games, CrazyGames en meer), dus één bouw, meerdere winkels (DERDEN, Playgama).
- **Wat Thijs moet doen:** een account bij Playgama (of Mediacube) aanmaken, voorwaarden accepteren en uitbetaalgegevens invullen. Geen YouTube-kanaal nodig als de uitgever publiceert (GOK, de uitgever heeft de kanaaltoegang; na te vragen).
- **Kinderen:** een deel van het publiek is jong. Alleen reclame die YouTube zelf toont, geen kopen in het spel (bestaat nog niet). Er is een leeftijdsclassificatie per spel nodig (GEZIEN, stap "Get an age rating" in het Developer Portal).
- **AI-regels:** de Playables-eisen noemen AI niet, ze eisen eigen of gelicenseerde inhoud (DERDEN, portalready.world). Niet verstoppen; Blender-renders zijn eigen werk.

## Voor en tegen
Voor:
- Grootste bereik per nieuw spel dat we ooit maten bij een open winkel: mediaan ±575.000 plays voor spellen van de laatste maanden, ook bij kleine makers via een uitgever (GEZIEN).
- Platform groeit net: van 7 naar 50+ landen in sept 2026, de EU erbij (DERDEN). Vroeg genoeg om een naam te maken.
- Ingang zonder kosten en zonder exclusiviteit; de maker houdt 75% bij Playgama (GEZIEN).
- Past bij wat we kunnen (web, 3D-renders), en in 1 tot 2 weken is een klein spel te maken.

Tegen:
- Wij komen er alleen in via een uitgever; YouTube zelf is op uitnodiging. Die uitgever kan weigeren of de voorwaarden veranderen.
- Geld per play is nergens openbaar; het enige bewijs komt van de uitgevers zelf. Geldregeling van YouTube is nog een proef.
- Meetbias: alleen de eerste 60 van A tot Z, en weggehaalde spellen zie je niet.
- Concurrentie van hypercasual-fabrieken (Voodoo, Supersonic, CrazyLabs) die snel kopiëren.
- Geen kopen in het spel tot ten minste 2027: alleen reclamegeld.
- Voorwaarden van Playgama: 75% van netto na kosten, en de betaalde YouTube-reclame die Playgama bij een lancering inzet kan dus van ons deel af. Uitbetalen pas vanaf $100; stopt de overeenkomst eerder, dan vervalt alles daaronder. Engels recht met de rechtbank in Dubai (DIFC Courts), en Playgama kan extra documenten vragen en anders de betaling stilzetten (DERDEN, controleur, developer.playgama.com/terms art. VI en 10.7/10.8). Thijs leest dit voordat hij accepteert.

## Eerste idee
Eén klein spel met Gloop (één knop of slepen, korte rondjes, 3D-renders uit Blender als sprites), eigen bedacht en geen kloon. Aanbieden via Playgama, zodat het naar YouTube Playables en tegelijk naar hun andere portalen gaat. Na 30 dagen de echte cijfers uit het Playgama-dashboard lezen: plays, inkomsten per 1.000 plays. Dat is de meting die van buiten niet kan.

## Nagekeken
Controleur 14 nov: eerst niet akkoord om de afdracht (75% voor YouTube, niet 70 tot 90%) en ontbrekende nadelen uit de voorwaarden; tabel en bronnen klopten. Alle 10 correcties verwerkt. Cijfer en advies vond hij verdedigbaar.

## Cijfer: 6
Bereik 8 (GEZIEN, met de kanttekeningen), geld 4 (kan, en de verdeling is openbaar, maar het verdienbewijs komt alleen van uitgevers, en 75% na kosten met een drempel van $100 drukt het eerder nog wat), past 6 (bouwen ja, toegang alleen via een tussenpersoon).

## Advies: ja, als kleine proef met één spel via Playgama
Geen 8: daarvoor ontbreekt bewijs van geld dat niet van de uitgever zelf komt. Maar de proef is goedkoop (één klein webspel, geen kosten vooraf) en het is de enige manier om het geldgetal te krijgen. Komt een proefspel na 30 dagen op minder dan $1 per 1.000 plays (ons deel, netto na de kosten die Playgama aftrekt) of minder dan 50.000 plays, dan stoppen. Hans beslist; Thijs moet het Playgama-account aanmaken (op de lijst als Hans ja zegt).

Herhaalmeting: 14 dec 2026. Opnieuw de A tot Z-pagina lezen (dezelfde spellen: groeien de plays van de spellen van aug tot nov door?), en kijken of YouTube het Developer Portal opent of een geldregeling voor iedereen aankondigt.
