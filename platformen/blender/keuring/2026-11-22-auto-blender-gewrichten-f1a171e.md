# Keuring blender-gewrichten architectuur rig.py (elleboog gedraaid), 22-11-2026, automatische keurder
Wat ik keurde: commit f1a171e0c (26c7aca..f1a171e), alleen `producten/blender-gewrichten/architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is één alinea in architectuur.md over `betaald/rig.py` (Pro 1.1, elleboog 90 graden gedraaid na een weigering). De add-on en de goedgekeurde versies (gratis 0.1.1, Pro 1.0.2) veranderen niet. | Feit | Hoog | De bestandenlijst bevat alleen dit ene bestand. |
| 2 | Of de alinea klopt met `rig.py` kan ik niet toetsen: de code zit niet in dit bereik. | Vermoeden | Midden | Een diff van `rig.py` en de toets die het gedraaide scharnier controleert. |
| 3 | Het commitbericht noemt ook een "logboek monsterproef", maar dat bestand staat niet in de wijziging. | Vermoeden | Midden | Een logboekbestand in dezelfde commit, of de melding dat het elders staat. |
| 4 | De alinea is eerlijk over wat nog niet werkt: knie en enkel worden overgeslagen en de Ninja lukt nog niet. Zo staat er geen belofte die de code niet waarmaakt. | Feit | Hoog | Niet van toepassing. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | architectuur.md is bijgewerkt voor de nieuwe werking van `rig.py`. | Feit | Hoog | architectuur.md bijgewerkt |
| 2 | Er zijn geen testbestanden gewijzigd, dus er is niets aangepast om te slagen. De alinea noemt echter geen toets voor het gedraaide scharnier. | Feit | Hoog | Tests niet aangepast om te slagen |
| 3 | "Yeti, Orc en Alien van 2 naar 4 of 6 gewrichten" staat als GEZIEN, maar zonder runnummer of bron. | Feit | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | De lengte van het bestand kan ik niet zien, want het is afgekapt. De alinea is wel erg lang, met regels van duizenden tekens. | Vermoeden | Laag | Bestanden onder ±400 regels |
| 5 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. Quaternius is een bronnaam. | Feit | Hoog | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Dit is alleen documentatie, ik kon niets zien of spelen. Deze punten zijn daarom vermoedens op basis van de tekst.
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Bij een rig worden knie en enkel stil of "eerlijk" overgeslagen. De gebruiker kan denken dat de knop faalde. | Een duidelijke melding in het paneel met welke gewrichten zijn overgeslagen en waarom. | Klein |
| 2 | Een rig in T-houding laat de elleboog eerst verkeerd buigen. De gebruiker merkt dat pas na een weigering. | Controleer de buigrichting vooraf en toon dat in het paneel. | Midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet runnummer of bron bij het GEZIEN over Yeti, Orc en Alien.
- Noem de toets die het gedraaide scharnier controleert, of voeg er een toe.
- Controleer of het logboek van de monsterproef echt is meegecommit.
- Splits architectuur.md of kort de zeer lange alinea's in, voor leesbaarheid en de regel van ±400 regels.
- Deze keuring dekt alleen de tekst. Pro 1.1 en de code van `rig.py` hebben nog geen akkoord in ontwerp.md.

---
Automatische keurder, model `claude-sonnet-5-5`, 21261 tokens in, 2527 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
