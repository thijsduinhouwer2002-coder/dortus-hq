# Keuring schermmaat=1920 in steam-hol-winkel.yml, 21 nov 2026, Daan
Wat ik keurde: commit d4ff27c (Olaf), alleen `.github/workflows/steam-hol-winkel.yml`. Beeld `bureaublad-held-2-b.png` uit run 44955974789 (tak schermen, map `...-werkvenster-run44955974789-scherm1920/bureaublad/`), met curl gehaald en met eigen ogen bekeken.
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Standaard 1280 verandert niets: $sb 1280, $sf 1, werkvenster 90/16/40/10 zoals voorheen, mapnaam zonder `-scherm1920`. | feit | hoog | diff |
| 2 | Met 1920: scherm wordt 1920 x 1080 gezet en gecontroleerd op $sb (anders geen beelden), werkvenster maal 1,5, eigen map met `-scherm1920`, dus nooit over een 1280-map heen. | feit | hoog | diff |
| 3 | held-2-b is echt 1920 x 1080 (PIL), niet opgeschaald: taakbalk, Kladblok-tekst en spel scherp. Recycle Bin vrij, strook onderaan met held, troon en Gloop, venster 15 px boven de strook. | feit | hoog | beeld |
| 4 | Het kleine briefje (werkvenster=0) schaalt niet mee op 1920 (vast 110,24,420,196). Nu niet gebruikt voor scherm 5. | feit | hoog | diff |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Valve-maat 1920 x 1080 met DERDEN-bron in het commentaar; strook 160 met reden (kern/strook.gd). Spelcode niet geraakt. Nepbegroting zonder echte namen of persoonsgegevens. | feit | hoog | eerlijk, harde regel 2 |

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Op 1920 is het spel klein en ±60% van het beeld is leeg wit Kladblok. In een Steam-carrousel kijk je dan naar wit, niet naar het hol. Olaf zag het zelf al. | Kladblok smaller (bijvoorbeeld tot x ±1100, rechts bureaublad zichtbaar) of zoom 150% in Kladblok, zodat de tekst het vak vult. Het beeld moet "werk boven, spel onder" vertellen, niet "wit vlak". | klein |
| 2 | Briefje schaalt niet mee. | $sf ook op het briefje zetten, voor als iemand 1920 zonder werkvenster draait. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
Moet: geen. De optie mag op main blijven.
Kan 1 (voor Sanne en Olaf, vóór het scherm de winkel in gaat): minder wit, Kladblok smaller of groter lettertype.
Kan 2: briefje ook maal $sf.
