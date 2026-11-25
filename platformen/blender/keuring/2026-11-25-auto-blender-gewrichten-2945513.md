# Keuring blender-gewrichten sale-regel in KAART.md, 25-11-2026, automatische keurder
Wat ik keurde: commit 294551368 (bereik 64c6d6b..2945513), alleen `producten/blender-gewrichten/KAART.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is één regel in de kaart. Die zegt dat CYBER25 bestaat en ingepland staat ("inactive"). Dat is passend vóór de start op 27 nov. | Vermoeden (de tekst zegt "GEZIEN", maar ik zie de curl-uitvoer niet) | midden | Een `curl` op de Gumroad-API of de productpagina op 27 nov ochtend: status "active", korting zichtbaar. |
| 2 | De commit noemt saleregels, salelink en controle, maar meegestuurd is alleen KAART.md. `platformen/blender/pro-sale-27nov.md` en `sale-controle.sh` staan niet in deze wijziging. Ze kunnen uit een eerdere commit komen. | Vermoeden | midden | `git ls-files platformen/blender/` toont beide bestanden, en `bash platformen/blender/sale-controle.sh` draait zonder fout. |
| 3 | De salelink `…/l/click-joints-pro/CYBER25` zet de kortingscode in het pad. Dat is een bekende Gumroad-vorm. | Vermoeden | midden | Openen op 27 nov: de korting staat al in het winkelmandje. |
| 4 | De regel zegt "voor alle kanalen", maar Superhive heeft een eigen sale (35%, t/m 2 dec). Gumroad stopt al op 1 dec. Het is onduidelijk of de link ook naar Superhive-kopers gaat. | Vermoeden | laag | De tekst in `pro-sale-27nov.md`: welke link waar, en wat er op 2 dec gebeurt. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Alleen een Markdown-regel, geen code en geen tests aangepast. architectuur.md hoeft niet mee. | Feit | hoog | Tests niet aangepast om te slagen, architectuur.md |
| 2 | KAART.md blijft ver onder 400 regels. | Feit | hoog | Bestanden onder ±400 regels |
| 3 | Geen sleutels, wachtwoorden of persoonsgegevens. Er staat een openbare winkel-URL van de verkoper, geen geheim. | Feit | hoog | Geen persoonsgegevens |
| 4 | "Curl: inactive, GEZIEN" is wel gelabeld. Ik kan het niet nagaan, en de status verandert op 27 nov. | Vermoeden | midden | Cijfers met GEZIEN/DERDEN/GOK |
| 5 | Eerlijk gemeld dat de keuring van Daan op de saleregels nog openstaat. | Feit | hoog | Keuring door een agent |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Er is niets te zien of te spelen en geen beeld voor een klant, dus de blinde test en de cijfers 1 tot 10 zijn hier niet van toepassing. Dit oordeel gaat alleen over de tekst op de kaart.
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Voor de koper telt dat de link de korting meteen toont. Dat is nu onbewezen. | Een vaste proef op 27 nov: de link openen in een privévenster en het bedrag in het mandje noteren. | klein |
| 2 | Verschillende einddata (1 dec Gumroad, 2 dec Superhive) kunnen verwarren. | Eén zin op de saleplek over wat er geldt tot wanneer. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Bevestig dat `pro-sale-27nov.md` en `sale-controle.sh` echt in de repo staan (deel A, rij 2).
- Maak duidelijk of de Gumroad-link ook voor Superhive-kopers bedoeld is (deel A, rij 4).
- Laat `sale-controle.sh` op 27 nov ochtend ook de salelink zelf openen en de korting in het mandje controleren (deel A, rij 3).
- Daan keurt de saleregels nog zelf, zoals de kaart al zegt.

---
Automatische keurder, model `claude-sonnet-5-5`, 18299 tokens in, 3030 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
