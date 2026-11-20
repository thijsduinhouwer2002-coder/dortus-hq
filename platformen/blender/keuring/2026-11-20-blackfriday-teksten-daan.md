# Keuring BlenderArtists-tekst en Addon Radar-formulier Click Joints Pro, 20 nov 2026, Daan
Wat ik keurde: `commercie/blender-click-joints/black-friday-plekken.md` (commit 249b478), blok "1. Addon Radar" en blok "2. BlenderArtists". Getoetst tegen de live Gumroad-pagina van Pro (curl 20 nov ±09:30 UTC) en `platformen/blender-2/gumroad-1.1.md`.
Akkoord: ja voor Addon Radar; ja voor BlenderArtists zodra moet 1 is opgelost

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | "25% off ... (applied at checkout)": de live pagina heeft nu `discount_code: null` (logisch, de korting start 27 nov). Of CYBER25 vanzelf wordt toegepast of dat de koper de code moet typen, staat alleen in een zin van de hoofdchat ("automatisch"), niet op een pagina die ik kon zien. Gumroad-codes werken meestal via typen of via een link met de code erin. | vermoeden | midden | Op 27 nov met curl de pagina lezen: staat `discount_code` of een doorgestreepte prijs er zonder code, dan klopt het. |
| 2 | "wall thickness as a number": de Gumroad-pagina zegt "the wall and clearance as a number" (FAQ). Klopt. | feit | hoog | - |
| 3 | "Rigify, Mixamo, Auto-Rig Pro and other common bone names": staat letterlijk op de live pagina (plus Unreal, CC, VRoid, Biped, Daz). Klopt. | feit | hoog | - |
| 4 | "Hinge with an end stop at 90, 115 or 135 degrees": dat zijn de knoppen voor een scharnier met de hand. Twee alinea's eerder staat dat de stop uit de rig komt (Limit Rotation, op de pagina 30° tot 150°). Samen leest het alsof er maar drie standen zijn. Niet onwaar, wel verwarrend. | feit | hoog | - |
| 5 | Addon Radar-tekst: elke zin staat op de Gumroad-pagina of in de gekeurde video. Geen print beloofd. "Also on Gumroad" en de gratis link kloppen. | feit | hoog | - |
| 6 | Overige zinnen (3D-cursor, 200 mm, "the panel tells you when a joint does not fit, and why", STL/3MF, rood voorbij de stop, groene band) staan op de live pagina. | feit | hoog | - |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen persoonsgegevens. thijs@dortus.com is het zakelijke adres en staat al openbaar. | feit | hoog | harde regel 2 |
| 2 | BlenderArtists gaat onder een account van Thijs of Dortus: staat terecht als "wacht op ja Thijs". Addon Radar zonder naam: mag door de hoofdchat. | feit | hoog | harde regel 4 |
| 3 | Cijfers in de tabel hebben GEZIEN of GOK. | feit | hoog | harde regel 5 |

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Op BlenderArtists zien lezers bij "$19 on Gumroad" niet dat Superhive tot de sale $12 vraagt. Wie het later vindt, voelt zich te veel betaald. | Eén regel: "Also on Superhive." met de Superhive-link. | klein |
| 2 | De titel is lang en zegt twee dingen. Op het forum telt de eerste helft. | `[Addon] Click Joints Pro: turn a rig into a printable action figure [$]` | klein |
| 3 | Het beeld en de buigfilm zijn goed gekozen; de film bovenaan zetten (vóór de tekst) laat in 3 seconden zien wat het doet. | Film als eerste in de post. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet (alleen BlenderArtists):**
1. "(applied at checkout)" alleen laten staan als iemand in de Gumroad-instellingen heeft gezien dat CYBER25 zonder typen werkt. Anders: "with code CYBER25", of de link naar `https://duinhouwer8.gumroad.com/l/click-joints-pro/CYBER25` laten gaan (dan zit de code in de link; meten gaat dan via Gumroad in plaats van `?van=ba`).

**Kan:**
1. Regel 4 van het lijstje: "End stop from your rig (30 to 150 degrees), or 90, 115 or 135 when you place a hinge by hand".
2. "Also on Superhive" met link erbij (C1).
3. Kortere titel (C2), film bovenaan (C3).
