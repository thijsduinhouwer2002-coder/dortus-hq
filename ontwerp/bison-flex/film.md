# Bison & Flex: filmpje (Daan, 9 nov 2026)

Opdracht Thijs (8 nov 23:15): meer tijd en moeite in GIF's en video's, ook voor Bison & Flex. Dit is het draaiboek. Jet neemt de beelden op in de echte IDE (zoals de winkelschermen, in de IDE-test op GitHub Actions); ik zet ze in elkaar, keur ze beeld voor beeld en zet de film daarna voor de projectchat klaar.

Waar het voor is: rechts in de hero van dortus.com/bison-flex/ (zoals bij Rollwright), als GIF bovenaan de README, en als video bij de lancering (Reddit r/Jetbrains of r/ProgrammingLanguages, met link). In de winkel van JetBrains kan een video alleen als YouTube-link; dat zet ik later op de lijst van Thijs, niet nu.

## Waarom dit opvalt
De enige concurrent voor Bison/Yacc in C en C++ die nog in de winkel staat (Bison Language Support) kent alleen `.y` en kreeg sinds september 2023 geen update (DERDEN, zie "Waarom wij" bovenaan `producten/jetbrains-bison-flex/ontwerp.md`); zijn winkelpagina toont geen film (GOK, niet nagekeken deze run). Niemand laat zien wat het echte probleem van iemand met een `.l` en `.y` is: twee bestanden die over dezelfde tokens gaan en elkaar niet kennen. Ons filmpje laat in vijftien seconden zien dat een token van het ene bestand naar het andere springt, en dat hernoemen in beide tegelijk gebeurt. Eén zin: **je ziet NUM reizen.**

## Gezicht
Zelfde als de poster (`winkel-1-poster.png`): donkere achtergrond met de oranje gloed rechtsboven en blauw linksonder, Inter voor koppen, oranje voor grammatica (Y), blauw voor scanner (L), de boog van L naar Y uit het icoon. De IDE-vensters zweven als kaarten op die achtergrond, met afgeronde hoeken en een zachte schaduw. Geen geluid nodig; alles is zonder geluid te snappen.

## Draaiboek (±15 s, 1920 x 1080, 30 beelden per seconde)
| # | Tijd | Wat je ziet | Kop | Bron |
|---|------|-------------|-----|------|
| 1 | 0,0 tot 1,5 | **Haak.** Dichtbij `return NUM;` in calc.l. NUM krijgt het oranje kader, een gloeiende boog schiet omhoog naar `%token NUM` in calc.y, dat kader licht op. | (geen, eerst beweging) | lagen van mij over echte schermen |
| 2 | 1,5 tot 3,5 | Camera trekt terug: beide vensters naast elkaar op de achtergrond. | **Your grammar and scanner, finally connected.** | lagen |
| 3 | 3,5 tot 6,0 | calc.y in het donkere thema: kleuren, Structure-paneel klapt open, een tikfout geeft een rode golflijn met melding. | Free: colors, structure and syntax errors | echte reeks |
| 4 | 6,0 tot 9,0 | Ctrl ingedrukt boven NUM in calc.l: onderstreept. Klik: het tabblad wisselt en de cursor staat op `%token NUM` in calc.y. Toetsen Ctrl + Click en het PRO-label in beeld. | Ctrl + Click: jump to the %token. PRO | echte reeks |
| 5 | 9,0 tot 12,5 | Shift+F6 op NUM: het hernoemvenster van de IDE, je typt NUMBER (één beeld per letter), Enter. Daarna calc.l en calc.y naast elkaar met overal NUMBER; het kort oplichten van die plekken is een laag van mij, geen IDE-gedrag. | Rename once. Both files follow. PRO | echte reeks |
| 6 | 12,5 tot 13,5 | Een ongebruikte regel krijgt een waarschuwing, Alt+Enter, weg. | Unused rules, caught. PRO | echte reeks |
| 7 | 13,5 tot 15,5 | Eindkaart: icoon, "Bison & Flex for JetBrains IDEs", eronder de vaste regel en het adres. | Free: colors, structure and syntax errors · Pro: jump, rename and unused-code warnings across grammar and scanner | lagen |

Gratis en Pro precies zoals op de poster en in `plugin.xml` (regel Thijs 8 nov). Wat niet in de plugin zit, komt niet in beeld.

## Wat ik van Jet vraag (opname in de echte IDE)
1. Eén IDE-test `FilmOpname` naast de winkelschermen, op een eigen tak, IntelliJ IDEA Community in het donkere thema (New UI, Dark), venster 1920 x 1080, lettergrootte editor **18** (op een video moet je de code kunnen lezen), presentatiemodus of alle gereedschapsvensters dicht behalve waar de scène ze nodig heeft, geen statusbalk-meldingen, muiswijzer mag weg (ik teken de klik).
2. **Beeld voor beeld**, niet realtime: per stap een schermafbeelding, met korte pauzes zodat het beeld klaar is. Ongeveer: scène 3 tien beelden (openklappen Structure in stappen, typen van de tikfout), scène 4 zes beelden (zonder Ctrl, met Ctrl en onderstreping, na de klik), scène 5 één beeld per letter van NUMBER plus het eindbeeld (in gesplitst venster, calc.l links en calc.y rechts), scène 6 drie beelden. Namen `scene3/0001.png` enzovoort.
3. **Log per beeld de schermplek** van NUM in beide bestanden (x, y, breedte, hoogte in pixels). Daarmee teken ik het kader, de boog en de klik precies op de goede plek.
4. Zet de mappen op de tak `schermen` in `jetbrains-bison-flex/film/<taknaam>/`, met RUN.txt. Gebruik het voorbeeld calc.l en calc.y uit de winkelschermen, zodat het overal hetzelfde voorbeeld is.
5. Schrijf onderaan `producten/jetbrains-bison-flex/ontwerp.md` dat het klaar staat. Ik maak de film (lagen, overgangen, koppen) en keur hem.

Niet dringend: het live product en de moderatie gaan voor. Wel graag binnen een dag, zodat de film er is als de winkel ja zegt.

## Bijgesteld na de controleur (9 nov 02:50 UTC)
- **Eigen map voor de film met alleen calc.l en calc.y** (geen calc.yy en calc.ll, anders geeft Ctrl+Click een keuzelijst in plaats van een sprong).
- **Pro aan** zoals in `Winkelschermen.kt` (stand GELDIG via MeldingenDiagnose).
- **Scène 4 is nog nooit met Pro in de echte IDE getoetst** (de test kijkt alleen dat er zonder licentie niet gesprongen wordt). Log daarom na de klik: cursor staat op `%token NUM` in calc.y, en het aantal onderstrepingen bij Ctrl-zweven (`ctrlZweven`). Springt hij niet: eerst repareren, dan pas de film.
- **Donker thema is nieuw werk** (de winkelschermen zijn licht).
- Scène 6: neem de zweeftekst of het Alt+Enter-menu in beeld, want een WEAK WARNING zie je in donker op video nauwelijks.
- GIF voor de README: 960 breed, 15 beelden per seconde.

## Klaar als (ik toets dit)
1. 14 tot 16 s, 1920 x 1080, H.264, onder 6 MB; GIF-versie onder 8 MB voor de README.
2. Beeld 1 haakt zonder geluid: beweging en licht in de eerste halve seconde.
3. Code op 1280 breed nog leesbaar.
4. Gratis en Pro overal gelijk aan poster en `plugin.xml`.
5. Alles wat in een IDE-venster gebeurt, is een echte opname.
