# Worm en mot in het echte spel (Olaf, 26 nov 2026, issue #190)

Bladen en model van Mila (#179, Daan #180 ja met een 8). Code: `godot/systemen/leven_beest.gd` (nieuw, 160 regels) en een paar regels in `godot/systemen/leven.gd`. Worm en mot zijn weer twee van de vijf soorten klein leven; de gaten van 5 tot 15 s blijven gelijk, er is nooit meer dan één ding tegelijk per hol (dus ook hooguit één worm per verdieping, kan Daan #180).

- **Worm:** steekt zijn kop uit een hoopje aarde op de gangvloer, volgorde van Mila: piek, op, links, op, rechts, op, piek (4,2 s), zacht in en uit. Alleen op een vrije gangtegel: niet bij schacht, val (en de tegel ernaast), vloerding, stut, de laatste 3 tegels voor de schat, en niet onder de hoedenberg van Gloop; geen held binnen 48 spelpixels als hij begint. In het korte hol van de eerste minuut is er geen plek, dus de worm komt pas als je gegraven hebt (in de film vanaf 70 s).
- **Mot:** fladdert een lusje net onder de fakkelvlam, vleugels om en om open en dicht, nooit door het plafond.

## Beelden (GEZIEN, Godot 4.3 Linux onder xvfb, strook 120, `vers=1 zaad=7 koper=1`, echt spel zonder proef)
- `worm-strook-1x.png` en `worm-uitsnede-2x.png`: worm op de gangvloer op 70 s.
- `mot-strook-1x.png` en `mot-uitsnede-2x.png`: mot bij de fakkel op 12 s.
- `film-eerste-80s-1x.mp4`: de eerste 80 s op ware grootte (zonder geluid, xvfb heeft geen geluidskaart); mot rond 6 tot 10 s, worm rond 64 tot 69 s.
- In 8 min echt spel (zelfde run): 11 worm, 7 mot, 9 goudstof, 4 stofje, 2 vleermuis (GEZIEN, `HOL leven` in hol.log).

## CPU
1. **Tekenbeurten (GEZIEN, toets `toets_licht.gd`):** 30 min klein leven met en zonder de bladen: 3726 tekenbeurten met worm en mot, 3760 zonder (-0,9 procent). Worm en mot komen in de plaats van een ander ding, en tekenen niet vaker: de worm tekent ±14 keer per keer (een stofje 54), de mot 54 zoals een stofje.
2. **Binnen één run** (zoals #162; `wissel=leven` zet worm en mot om de 20 s aan en uit, `wissel=nep` laat ze aan als placebo; Linux xvfb, `vers=1 zaad=5 koper=1`, 12 min, drie runs tegelijk op 2 kernen; alle seconden, want met een koper is er bijna altijd een held). Script `platformen/steam/data/cpu-duur/cpu_stenen.py` (leest nu ook `wissel leven`), ruwe meting in `platformen/steam/data/cpu-duur/leven/`.

| run | aan | uit | verschil | buurparen |
|---|---|---|---|---|
| echt (worm en mot aan of uit) | 1,574 | 1,429 CPU-s per 10 s | +10,1 % | +12,0 ± 3,5 |
| placebo (altijd aan) | 1,571 | 1,463 | +7,4 % | +10,4 ± 4,3 |
| zwaar: elke 2 s een worm, tegen niets | 1,629 | 1,391 | +17,1 % | +19,2 ± 4,2 |

De placebo laat zien dat de aan-blokken in deze runs vanzelf ±7 tot 10 procent duurder zijn (zelfde zaad, de helden komen in alle drie op dezelfde tijd). Echt min placebo: **+2,7 procent (buurparen +1,7), met een ruis van ±5**: niet te onderscheiden van nul, maar ook niet hard binnen +1. Zwaar min placebo +9,7 procent voor een worm die 68 procent van de tijd in beeld is; in echt spel is een worm ±6 procent van de tijd in beeld (GOK uit de telling hierboven), dan is dat ±0,9 procent tegen niets, en hij vervangt een stofje dat meer tekent.
Beelden per 10 s (`beelden_leven.py`): echt +7,0, placebo +5,3, zwaar +11,4 procent.

**Mijn oordeel:** binnen +1 volgens de telling van tekenbeurten (punt 1, GEZIEN) en de afleiding uit de zware run; de directe meting is te ruw om dat zelf te bewijzen. Een rustige meting zonder helden in een gegraven hol kan als Daan dat wil.

## Toetsen
Alle acht 0 FOUT op Linux (Godot 4.3). In `toets_licht.gd` nieuw: worm en mot terug (kruimels niet), bladen laden, worm alleen op vrije gangtegels, volgorde van de worm, zuinig tekenen, mot onder het plafond, alle vijf soorten komen in 10 min minstens 3 keer, tekenbeurten met en zonder.

Startargumenten om te keuren: `leven_proef=worm` of `leven_proef=mot` (alleen dat ding, om de 2 s; de worm heeft wel een gegraven gang nodig, dus samen met `koper=1`).
