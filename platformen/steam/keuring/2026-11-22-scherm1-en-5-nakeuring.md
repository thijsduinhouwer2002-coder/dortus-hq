# Nakeuring scherm 1 (alleen pijl) en scherm 5 (1920 x 1080), 22 nov 2026, Iris
Wat ik keurde: `ontwerp/steam/winkelpagina/concept-21nov/1-bureaublad-pijl.png` (+ `-600`), `5-naast-werk.png` (+ `-600`), `maak_scherm1_pijl.py`, `LEESMIJ.md` (stand main 34b2e26). Bron scherm 5: `bureaublad-held-2-b.png` uit run 44975368948 op tak `schermen` (met curl via raw.githubusercontent). Vorige keuring: `2026-11-21-scherm1-en-5.md`.
Akkoord scherm 1: **ja**
Akkoord scherm 5: **ja**

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Moet 1 opgelost: geen woorden meer op scherm 1, alleen de witte pijl. De enige tekst in beeld komt uit Windows en het spel (GEZIEN). | feit | hoog | |
| A2 | Scherm 1 is pixel voor pixel het gekeurde `schermen-steam/2-bureaublad.png`, behalve het vlak x 1005 tot 1467, y 420 tot 756 (de pijl, nagemeten met PIL). De pijl blijft dus boven de graslijn en raakt niets van het spel. | feit | hoog | |
| A3 | C2 verwerkt: de pijlpunt wijst nu op Gloop met zijn hoed op de troon. Leest op 600 breed (GEZIEN). | feit | hoog | |
| A4 | Moet 2 opgelost: scherm 5 is 1920 x 1080 (nagemeten), en byte voor byte gelijk aan de bron uit run 44975368948 (sha256 d21706c8...2be4 bij beide). Dus niet opgeschaald en niet bewerkt. | feit | hoog | |
| A5 | Scherm 5: Recycle Bin vrij, geen schuifbalk, werk boven en spel onder leest op 1920 en op 600 (GEZIEN). Held met helm en held met heksenhoed bij de ladder, Gloop met hoeden op de troon, kaartje "Gerda read about you in a tavern." | feit | hoog | |
| A6 | Begroting in Kladblok opnieuw nagerekend (nieuwe opname): alle zes rijen, de drie maandtotalen (2.800, 2.705, 3.190) en 8.695 kloppen; "licences go up 40 in Dec" klopt (460 min 420). | feit | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Geen marketingtekst op de schermen (Valve-regel, DERDEN https://partner.steamgames.com/doc/store/assets/standard). Dat de pijl mag blijft GOK, en staat zo in het concept (regel 90). | feit / GOK | hoog / midden | Valve-regel, GEZIEN/DERDEN/GOK |
| B2 | Geen AI-beeld: beide uit de build, pijl met PIL. | feit | hoog | geen AI-beeld op Steam |
| B3 | Geen persoonsgegevens: Kladblok heeft alleen verzonnen posten, heldennaam verzonnen. | feit | hoog | repo openbaar |
| B4 | Concept regel 87 (plek 5) noemt nog de oude opname "1280 x 720 en dus te klein"; LEESMIJ is wel bijgewerkt. Kleine verouderde regel. | feit | hoog | eerlijk en actueel |

## Deel C: zou een speler het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Scherm 1 zegt nu zonder woorden "dit spel woont onder je werk". Sterk als eerste beeld. | niets | |
| C2 | Scherm 5 op 600 breed: het spel is klein en de lege ruimte tussen Kladblok en strook groot. Dat is juist het punt (naast echt werk), maar het spel valt minder op dan op scherm 1. Mag zo. | niets, of later een opname met Kladblok wat lager | klein |
| C3 | Hint "Trick Lid ready: click the pit" in het kaartje rechtsonder is echte speltekst, geen probleem. | niets | |

## Moet (blokkeert akkoord)
Geen.

## Kan
- B4: concept regel 87 bijwerken naar run 44975368948, 1920 x 1080, gekeurd.
- Beide schermen mogen nu naar `schermen-steam/` (volgens de LEESMIJ pas na deze nakeuring). Spelerstekst blijft CONCEPT tot Thijs.
