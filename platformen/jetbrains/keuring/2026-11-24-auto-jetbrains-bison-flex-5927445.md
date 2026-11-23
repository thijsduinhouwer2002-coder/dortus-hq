# Keuring Bison & Flex winkeltekst met link naar gratis licenties, 24-11-2026, automatische keurder
Wat ik keurde: commit 5927445ec, bestand `producten/jetbrains-bison-flex/src/main/resources/META-INF/plugin.xml`
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De beschrijving krijgt een derde link "Free licenses" naar `https://plugins.jetbrains.com/plugin/35901-bison--flex/pricing`. | Feit dat de link erin staat. Vermoeden dat hij werkt en op de juiste pagina uitkomt. | midden | `curl` op de link, of een kijkje op de Marketplace na de uitgave. Het pluginnummer 35901 komt wel in het ontwerp voor. |
| 2 | De zin zegt nu dat studenten, docenten en open-bronprojecten Pro gratis kunnen krijgen via JetBrains. Dat is een belofte aan kopers die niet in het ontwerp staat. | Vermoeden dat het klopt. In de tekst staat geen bron en geen GEZIEN of DERDEN. | laag | De officiële JetBrains-pagina over gratis licenties voor Marketplace-plugins, of een bevestiging dat dit voor onze plugin aan staat en voor wie. |
| 3 | De rest van de belofte (wat, voor wie, gratis en Pro) is niet aangeraakt. | Feit, uit de diff. | hoog | n.v.t. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De winkeltekst is veranderd na het akkoord van Daan van 23 nov. Dat akkoord geldt voor 2e46f5e2, en Daan wilde nieuw zichtbaar werk eerst nakijken. In `ontwerp.md` staat nog geen nieuw akkoord. | Feit. | hoog | Jet dient pas in na `Akkoord: ja` voor de huidige versie. De belofte moet overal precies gelijk zijn. |
| 2 | De claim over gratis Pro heeft geen label GEZIEN, DERDEN of GOK. | Feit. | hoog | Claims en cijfers met GEZIEN/DERDEN/GOK. |
| 3 | `CHANGELOG.md` en `architectuur.md` zijn niet bijgewerkt. Dat is niet nodig voor een tekstwijziging in de beschrijving. | Vermoeden. | midden | Andere plekken die de winkeltekst herhalen (`indienen.md`, manual, poster) kan ik niet zien. Die moeten dezelfde zin houden. |
| 4 | De commit noemt "keuring e2e Olaf", maar die keuring zit niet in deze wijziging. | Feit dat ze ontbreekt. Ik kan niet zien of ze elders staat. | midden | Het keuringsbestand onder `platformen/jetbrains/keuring/`. |
| 5 | Het is één klein bestand, zonder persoonsgegevens of sleutels. Er zijn geen tests aangepast. | Feit. | hoog | n.v.t. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Studenten en open-bronmakers vinden hun weg naar gratis Pro nu sneller, met een link in de linkrij. | Zet in de zin of op de pricing-pagina kort uit wie er recht op heeft. | klein |
| 2 | De zin "free features are enough for most courses" is eerlijk en maakt de plugin laagdrempelig. Hij is wel lang geworden. | Splits hem in twee korte zinnen. | klein |
| 3 | Ik kan niet zien hoe de beschrijving in het pluginvenster van de IDE eruitziet met drie links in één regel. | Kijk na in licht en donker. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Onderbouw de claim "students, teachers and open source projects can get Pro free through JetBrains" met een bron (DERDEN) of schrap hem. Als het niet klopt, is het een foute belofte op de winkelpagina.
2. Daan moet de nieuwe winkeltekst nakijken en `Akkoord: ja` zetten in `ontwerp.md` voor deze versie, voor die wordt uitgebracht.

**Kan**
- Test of de pricing-link werkt en op de goede pagina uitkomt.
- Controleer of de zin ook in `indienen.md`, de manual en de plaatjes gelijk is.
- Splits de lange zin in twee.
- Zet het keuringsbestand van Olaf erbij of verwijs ernaar.

---
Automatische keurder, model `claude-sonnet-5-5`, 18352 tokens in, 3243 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
