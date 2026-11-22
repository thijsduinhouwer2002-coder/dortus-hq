# Uniform van Dortus (Mila)

Versie 1, 10 nov 2026 ±01:00 NL. Opdracht Thijs 10 nov 00:16: overal hetzelfde, "echt mooi en vertrouwd en spectaculair". Mila maakt de beelden, Abel zet ze per account klaar, Daan keurt.

## Het idee in één zin
**De D van Dortus is een deur die op een kier staat, met warm licht erachter.** Achter elke deur van Dortus zit iets: een spel, een tool, een dobbelsteen. Je wilt weten wat.

- **Vertrouwd:** het oude logo (paarse D met twee bolletjes op de rechte kant) zit er nog in. De twee bolletjes zijn nu de **scharnieren** van de deur. Wie het oude logo kent, herkent het nieuwe meteen; het lijkt alsof het altijd al een deur was.
- **Stoppen met scrollen:** goud licht in een donker vlak is het eerste waar een oog naartoe gaat, in elke lijst op Steam en GitHub.
- **Haak en grap:** op de grote beelden rollen er spullen uit de deur het licht in: een **kroontje** (een hoed uit Het Hol), een **dobbelsteen** (Rollwright) en **accolades** (de tools voor programmeurs). Eerlijk: dat zijn echt onze producten. Komt er een product bij, dan rolt dat er ook uit.
- **Werkt klein:** op 32 en 16 px blijft een lila D met een gouden hart over (GEZIEN in `toets-klein.png`). Geen figuur, geen tekst in het beeldmerk.
- **Maker, geen spelfiguur** (eis Abel): geen Gloop in het merk. De kroon op de vloer is een knipoog, niet het logo.

## Kleuren (overal deze, niets anders)
| Naam | Hex | Waar |
|---|---|---|
| Nacht | `#1d1426` | achtergrond, altijd donker (zelfde als de aarde van Het Hol) |
| Pruim | `#3f2846` | het deurblad |
| Lila donker | `#6f55d9` | binnenkant van de deurpost |
| Lila licht | `#c9b9ff` | buitenrand van de D |
| Lila | `#a58cff` | de D en de onderregel (familie van het oude `#9b8cf2`) |
| Goud | `#ffd25c` | licht, scharnieren, deurknop (zelfde als de schat van Het Hol) |
| Oranje | `#ff9a3c` | rand van het licht |
| Crème | `#fff4e0` | het woord "ortus" en tekst |

Letter: **Inter Display ExtraBold** voor het woord, **Inter Medium** voor regels eronder. Het woordmerk is altijd de deur-D plus "ortus" in kleine letters: zo lees je "Dortus".

## Bestanden (alles in deze map, gemaakt door `bron/maak_uniform.py`)
| Bestand | Maat | Voor |
|---|---|---|
| `avatar-1024.png` | 1024 | bron, Steam laat zelf schalen |
| `avatar-512.png` | 512 | GitHub, Polar, Blender ID, JetBrains, Obsidian-forum |
| `avatar-184.png` | 184 | Steam profiel, groep en ontwikkelaarspagina |
| `avatar-32.png`, `avatar-16.png` | 32, 16 | eigen kleine tekening (grotere D, deur verder open, geen scharnieren) |
| `merkteken.svg` | vector | favicon dortus.com en alles wat scherp moet blijven (`merkteken-klein.svg` voor 16 en 32 px, beter als favicon) |
| `steam-logo-1200x460.png` | 1200 x 460, doorzichtig | logo bovenaan de ontwikkelaarspagina (v1; v2 hieronder staat in het midden) |
| ~~`steam-kop-1500x220.png`~~ | 1500 x 220 | **niet gebruiken** (deur valt op 1024 px weg). Gebruik `steam-kop-1500x220-v1b.png` (akkoord Daan) of v2 na keuring |
| `steam-achtergrond-1920.png` | 1920 x 1200 | achtergrond ontwikkelaarspagina, met de spullen in het licht |
| `og-1200x630.png` | 1200 x 630 | deelplaatje dortus.com |
| `social-1280x640.png` | 1280 x 640 | GitHub social preview (algemeen) |
| `toets-klein.png` | | toets: avatar rond en vierkant op 184, 64, 32, 20 en 16, op Steam-donker en GitHub-wit, naast het oude logo |

Alle avatars zijn rond te knippen: de D valt binnen de middelste 70% (GEZIEN in `toets-klein.png`). De avatar heeft een eigen donkere achtergrond, dus werkt op licht en donker.

## Regels voor wie het gebruikt
1. Niets aan de D veranderen (kleur, vorm, deur). Alleen schalen.
2. Achtergrond altijd Nacht of donkerder. Nooit de D op wit zonder het donkere vlak eromheen. Het Steam-logo (doorzichtig, "ortus" in crème) alleen op Nacht of Steam-donker.
3. Per product mag in het licht van de deur iets van dat product liggen (social preview per repo): dat volgt in v2, Abel zegt welke repo's eerst.
4. Producten houden hun eigen icoon (Bison & Flex, Click Joints, Rollwright, Het Hol). Het uniform zit in de avatar, de kop en de deelplaatjes.

## Eerlijk oordeel en wat nog kan (v2)
- Sterk: leest klein, warm, en het oude logo leeft voort. Naast de standaard GitHub-blokjes en het oude lichte vierkantje is dit een echt merk.
- Diepte (nog in v1 toegevoegd): lichte buitenrand en een donkere binnenkant van de deurpost, zodat de D een echte deurpost is en niet een plat letterteken. Op 32 en 16 px weggelaten, daar telt alleen de vorm.
- De spullen op de vloer zijn nu simpel getekend; in v2 met wat meer licht en schaduw, en een stofwolkje van de rollende dobbelsteen.
- Steam-achtergrond: de grote D staat rechts; controleer in de v2-editor of de inhoud van de pagina er niet overheen valt (Abel).

## Keuring Daan
**Akkoord: ja 10 nov 2026 (Daan, 00:30 UTC)** voor v1, **Steam-kop alleen v1b** (v1 valt op 1024 px half weg), Steam-achtergrond pas na moet-punt 1 (D niet achter de middenkolom van de pagina). Volledige keuring met kan-punten voor v2: `ontwerp/keuring-abel.md`, keuring 2.

## Versie 2 (Mila, 10 nov ±02:20 NL): wacht op keuring Daan
Alle punten van Daan (keuring 2) en Abel (`voor-mila.md`) verwerkt. Nieuwe bestanden hebben `-v2` in de naam; de v1-bestanden blijven staan tot Daan v2 keurt. Avatars en merkteken veranderen niet.

| Bestand | Wat er anders is | Punt |
|---|---|---|
| `steam-kop-1500x220-v2.png` | **Geen tweede D meer.** Het licht valt vanaf links over de vloer naar rechts, alsof het uit de deur in de avatar komt, en daarin rollen kroon, dobbelsteen en accolades. Op 1024, 1280 en 1920 breed staat het licht steeds net rechts van de avatar (GEZIEN in `proef/steam-pagina-v2-op-steam-*.png`); de spullen staan op kop-x 600 tot 1080, op 1024 buiten het grijze verloop, en boven y 200 zodat de tabs ze niet afknippen. | Daan 6, Abel punt 1 |
| `steam-achtergrond-1920-v2.png` | Abels v1b overgenomen (geen tweede D, het licht valt uit de D van het paginalogo), nu precies onder de lichte opening van het logo v2, en **alle drie de spullen terug** in de kantlijn, elk in een eigen gloed: kroon en dobbelsteen links, accolades rechts. Hoger gezet, want de achtergrond begint pas onder de tabs. | Daan 1, Abel punt 2 |
| `steam-logo-1200x460-v2.png` | Woordmerk precies in het midden (gemeten, niet geschat). | Daan 8 |
| `og-1200x630-v2.png`, `social-1280x640-v2.png` | Lichtbundel en spullen nieuw (zie hieronder). | Daan 2 en 4 |

Wat overal nieuw is:
- **Het licht komt uit de kier.** De bundel begint smal onder de lichte opening (tussen deurblad en boog) en wordt daarna breder, met een fellere kern. Je leest nu "het licht valt door de deur naar buiten".
- **De spullen hebben diepte:** de kroon ligt iets scheef, met een band, glans en drie steentjes; de dobbelsteen is een echte kubus met lichte bovenkant en een stofwolkje erachter (hij rolt nog); de accolades hebben een donkere rand en een schaduwkant.
- Eén nadeel, eerlijk: op een venster van 1024 breed schaalt Steam het paginalogo, de achtergrond niet, dus daar sluit de bundel op de achtergrond niet aan op de D (de kop wel). Op 1280 en breder klopt het.
- Nog niet gedaan (Daan 3): social per repo met het productbeeld groot in het licht. Volgt als Abel zegt welke repo's eerst.

## Versie 3 achtergrond (Mila, 10 nov ±02:55 NL): wacht op keuring Daan
Alleen `steam-achtergrond-1920-v3.png` is nieuw (keuring 3 van Daan: achtergrond nee). De rest van v2 is akkoord en verandert niet.
- **Moet 1, niets half op 1280:** spullen staan nu helemaal links van x 300 (munten, x 108 tot 284) of rechts van x 1600 (sleutel, x 1620 tot 1845), nagemeten in de png. Op 1280 breed zijn ze dus helemaal weg, op 1920 helemaal te zien.
- **Moet 2, geen herhaling uit de kop:** kroon, dobbelsteen en accolades staan alleen nog in de kop. In de kantlijn liggen andere dingen: links drie gouden munten (de schat van Het Hol, eentje nog op zijn kant), rechts de gouden **sleutel van de deur**. Waarom de sleutel: het hele uniform is een deur op een kier; wie op brede schermen de sleutel ernaast ziet liggen, snapt het grapje (de deur staat open, de sleutel ligt er nog).
- **Moet 3, rand op 2560:** de buitenste 160 px links, rechts en onder lopen uit in vlak Nacht (`#1d1426`, gemeten in de hoeken en randen: overal 29, 20, 38). De bundel is smaller en raakt de rand niet meer. Abel: zet als paginakleur naast het plaatje ook `#1d1426` als Steam dat toelaat; proef op 2560 graag nog in je mock.

## Voorstel avatar v2 (Mila, 10 nov ±03:05 NL): wacht op keuring Daan
Abel (run 3) en Daan (kan 7) zagen op 24 px rond de scharnieren als gele spikkels naast de D. Ik zie het ook: `proef/avatar-v1-v2-klein-rond.png` (boven v1, onder v2, op 24, 32 en 45 px rond, verkleind zoals Steam, Polar en GitHub dat zelf doen).
- `avatar-1024-v2.png`, `avatar-512-v2.png`, `avatar-184-v2.png` (bron `avatar-v2.svg`, `python3 bron/maak_uniform.py avatar-v2`): de D is 13% groter, zodat hij meer van de cirkel vult, en de scharnieren zitten half in de D in plaats van ernaast. Klein worden het inkepingen in de rand van de letter, geen losse spikkels meer; groot blijven het duidelijk de twee bolletjes van het oude logo.
- De kleine tekening voor 32 en 16 px (favicon) verandert niet. v1 blijft staan; Abel gebruikt v2 pas na Daans ja.
