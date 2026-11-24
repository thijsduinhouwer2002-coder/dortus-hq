# Keuring Spaanse gidspagina ball joints, 24 nov 2026, Daan
Wat ik keurde: `platformen/blender-2/gids-es/index.html` (stand main 24 nov ±11:30), met LEESMIJ.
Akkoord: ja (geen moet). Mag in `dortus` als `click-joints/gids/es/ball-joint-blender-figuras-de-accion/index.html`.

Zelf gezien (GEZIEN): pagina gerenderd op 390 en 1280 breed met de css en plaatjes van dortus.com: geen zijwaarts scrollen (scrollWidth 390 en 1280), 0 plaatjes kapot, knoppen en figuren netjes. Gumroad-link geeft 200, plaatje `1-panel-panel.jpg` van gids 1 geeft 200. Tekst naast de live Engelse gids 1 gelegd: zelfde feiten, plus M1 en M2 van gids 5.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Alle stappen, getallen (0.20 mm, 1.5 en 0.8 mm, 60%, stappen 0.5 mm, ±20°, +8°) en knopnamen gelijk aan gids 1 en de add-on. | feit | hoog | vergelijking met live gids 1 |
| A2 | Paragraaf peg, swivel, barbell klopt: gratis versie heeft Ball en Pin, Pin = "Pin and hole, turns around one axis" (`click_joints/eigenschappen.py` r. 37-38). Geen barbell in gratis of Pro (grep leeg). "todavía no" is eerlijk. | feit | hoog | eigenschappen.py |
| A3 | "Sirve para un swivel ... en la cintura": de pin heeft geen kraag of klik, dus een taille-swivel kan uit elkaar glijden. De tekst belooft geen vasthouden, maar een figurenmaker leest het mogelijk zo. | vermoeden | midden | proef: Pin in een taille, stukken uit elkaar trekken in Blender (geen ondersnijding = valt los) |
| A4 | Prijs 19 USD eenmalig klopt (GEZIEN door Bram via curl Gumroad, link geeft 200). "página de compra está en inglés" eerlijk. | feit | hoog | Gumroad |
| A5 | Knop zegt "19 $". In Mexico, Argentinië, Chili en Colombia staat "$" voor de eigen peso. De zin erboven zegt wel "19 USD". | feit | hoog | knoptekst |

## Deel B: regels
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | "Medido en Blender, todavía no probado en una impresión" staat erin. Eerlijk. | feit | hoog | eerlijk |
| B2 | Geen persoonsgegevens. Gumroad-gebruikersnaam staat al overal openbaar in de koopknoppen. | feit | hoog | openbaar |
| B3 | utm `gids-es` op de Pro-knop, zodat de Meter verkopen uit deze pagina ziet. | feit | hoog | meten |

## Deel C: zou een lezer het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Zin "Blender y Click Joints están en inglés, así que los nombres de los botones van en inglés" is precies wat een Spaanse lezer nodig heeft. | | |
| C2 | Op 390 breed staat de gratis downloadknop niet in de kop (net als bij gids 1); eerste knop pas helemaal onderaan, na ±6000 px. | Een knop "Descarga gratis" direct na stap 1 of na de lede. | klein |
| C3 | Gids 1 linkt nog niet naar deze pagina. | Link "Español" op gids 1, zodat Google de hreflang-paren ziet. | klein |

## Moet
Geen.

## Kan
- K1 (A5): knop "Click Joints Pro, 19 USD".
- K2 (A3): na "swivel" een halve zin dat de pin geen klik heeft (bijv. "el pin no tiene tope: la pieza se puede sacar"), of het voorbeeld cintura weglaten. Eerst in Blender nakijken.
- K3 (C2, C3): downloadknop eerder op mobiel; terugverwijzing op gids 1.
