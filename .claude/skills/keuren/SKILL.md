---
name: keuren
description: Gebruik dit als je werk van een ander keurt of een aparte keurder inzet (code, ontwerp, winkeltekst, onderzoek, beelden). Vast formulier in twee delen, de keurder bouwt zelf niets.
---

# Keuren met een vast formulier

Afgekeken bij Formbricks (twee keurders: één op de opdracht, één op de regels), Ghostty (de keurder schrijft geen code) en de solo-maker van Excalidraw voor Obsidian (feit los van vermoeden, met zekerheid).

## Regels voor de keurder
- Je **bouwt en verbetert niets**. Je schrijft alleen een oordeel. Ook geen "kleine fix even zelf".
- Je hebt het werk niet zelf gemaakt. Zet de bouwer zichzelf in als keurder, dan telt het niet.
- Bekijk wat je ziet echt: beelden en schermen met de Read-tool, uitslagen van tests in het log, cijfers bij de bron (met `curl`). Code lezen is geen bewijs dat iets er goed uitziet.
- Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## Het formulier
Schrijf je keuring in het bestand dat de opdracht noemt (anders `platformen/<platform>/keuring/<datum>-<onderwerp>.md`):

```
# Keuring <onderwerp>, <datum>, <keurder>
Wat ik keurde: <commit, bestand of link>
Akkoord: ja | nee

## Deel A: doet het wat beloofd is?
(toets tegen de opdracht: producten/<naam>/ontwerp.md, het bericht met de opdracht, of de belofte op de winkelpagina)
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |

## Deel B: houdt het zich aan onze regels?
(tests niet aangepast om te slagen, bestanden onder ±400 regels, architectuur.md bijgewerkt, geen persoonsgegevens,
cijfers met GEZIEN/DERDEN/GOK, spelerstekst van Hats alleen als CONCEPT, geen AI-beeld of -geluid op Steam)
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |

## Deel C: zou een gebruiker het leuk en fijn vinden? (alles wat je kunt zien of spelen)
(kijk als de speler of koper, niet als programmeur: wat is na 30 seconden saai, herhalend of voorspelbaar,
bijv. steeds dezelfde kant, dezelfde held, dezelfde reactie of klank; wat voelt stroef of goedkoop; wat mist er
dat het leuker of duidelijker maakt. Noem het ook als niemand erom vroeg. Thijs, 19 nov: "dit soort dingen uit jezelf doen".)
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |

## Deel C: is het goed genoeg? (verplicht bij alles wat een klant ziet: beeld, video, winkeltekst, spel, site)
(Thijs 24 nov 19:20: "de kwaliteit is niet goed bij veel dingen". Lat: "echt een mooi stuk techniek moeten mensen gelijk denken".)
| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeleken (link naar het beste voorbeeld van een concurrent) |
| Ziet het er top uit, op het niveau van de beste in de winkel? | | |
| Zou ik het zelf kopen of bekijken op basis van dit? | | |
| Zou Thijs er trots op zijn? | | |
Elk cijfer onder 8 = **Akkoord: nee**, ook als alles in deel A en B klopt. Leg het naast het beste voorbeeld van een concurrent (beeld met Read naast elkaar) voor je een cijfer geeft.

## Moet (blokkeert akkoord) / Kan (mag later)
```

## Automatische keurder
Bij elke push naar Click Joints, Bison & Flex of Rollwright, en elke avond om 21:00 voor Hats, vult een losse Claude dit formulier vanzelf in (`.github/workflows/keurder.yml`). Je krijgt het oordeel onderaan je berichtenbestand en een groen of rood vinkje op de commit. Rood = niet uitbrengen tot de moet-punten weg zijn. Hij leest alleen tekst: beeld en speelplezier keuren Daan en Iris nog steeds, en bij live zetten blijft een keuring door een agent nodig.

## Na de keuring
- Alles met **hoog** en "moet" lost de bouwer op; daarna keur je opnieuw alleen die punten.
- Bij spelwerk keurt Iris daarna op plezier en beeld; bij uiterlijk Daan (`Akkoord: ja` bovenaan `ontwerp.md`).
- Bij werk dat zwaar weegt (geld, live zetten, besluit van Thijs) zet je twee keurders tegelijk in: één voor deel A, één voor deel B.
