# Keuring blender-gewrichten, notitie "Pro zet gratis uit" (#114), 26-11-2026, automatische keurder
Wat ik keurde: commit 8b0c378ce, alleen `producten/blender-gewrichten/KAART.md` (één alinea erbij)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is alleen een statusnotitie. De code van #114 zit niet in deze diff (tak `claude/blender-114`), dus ik kan niet keuren of Pro de gratis versie echt uitzet. | Feit | hoog | De diff van 46f8667 op de tak, of de e2e-log van run 45760022687. |
| 2 | De notitie belooft de regel "Free Click Joints was turned off; Pro includes everything in it.", zonder dat iets wordt verwijderd. Dat past bij het doel van #114. | Vermoeden | midden | Een schermbeeld van het Pro-paneel met de regel, of een e2e-toets die de regel leest. |
| 3 | De notitie noemt samenvoegen op maandag 30 nov. Die datum is een maandag en de volgorde is logisch: eerst de sale, daarna samenvoegen, daarna de zin uit de Superhive Docs-tab halen. | Feit | hoog | Niet nodig. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen tests aangepast, geen persoonsgegevens, geen sleutels, één bestand met een paar regels erbij. | Feit | hoog | Tests, persoonsgegevens, bestandsgrootte |
| 2 | Run-uitslagen staan met GEZIEN en commit-nummers erbij. Ik kan de runs zelf niet openen. | Feit dat het zo is gelabeld, vermoeden dat de runs kloppen | midden | Cijfers met GEZIEN/DERDEN/GOK |
| 3 | De notitie zegt dat ontwerp en architectuur zijn bijgewerkt (in 46f8667). De `architectuur.md` die ik zie noemt de nieuwe regel nog niet. Dat kan kloppen, want die update staat op de tak. | Vermoeden | midden | architectuur.md bijgewerkt: na het samenvoegen controleren. |
| 4 | De nieuwe alinea staat zonder lege regel direct onder de vorige. Dat kan in Markdown tot één blok versmelten. | Vermoeden | laag | Opmaak, klein |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Alleen tekst in een interne kaart. Er is voor een klant niets te zien of te spelen, dus de beeldtest en de cijfers 1 tot 10 zijn niet van toepassing. | Niet van toepassing. | klein |
| 2 | Een gebruiker die van gratis naar Pro gaat, hoeft niets meer zelf uit te zetten. Dat lijkt een echte verbetering. Of de regel in het paneel duidelijk leest, kan ik zo niet zien. | Een schermbeeld van de regel op 600 px erbij zetten. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Voor het samenvoegen op 30 nov: het ontwerp- en architectuurbestand op main nalopen op de nieuwe regel.
2. Een lege regel voor de nieuwe alinea in KAART.md zetten.
3. Bovenaan `ontwerp.md` ontbreekt het "Akkoord: ja" voor 1.2.9 (#103 en #138). Zet het erbij als Daan het gaf.
4. In de notitie staat "Daan ja (#138, 8)". Het getal 8 wordt niet uitgelegd.

---
Automatische keurder, model `claude-sonnet-5-5`, 18604 tokens in, 2555 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
