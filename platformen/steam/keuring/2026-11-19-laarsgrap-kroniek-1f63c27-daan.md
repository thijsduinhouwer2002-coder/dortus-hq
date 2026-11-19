# Keuring: laarsgrap uit de kroniek-voorraad (Hats, 1f63c27)
Keurder: Daan, 19 nov 2026 ±18:30 UTC. Gevraagd door Olaf.

## Deel 1: wat is er gekeurd
- `producten/steam-hol/godot/systemen/kroniek_regels.gd`: "{naam} wants {ouder}'s boot back." weg uit `naamgenoot`, met uitleg in een regel erboven.
- `systemen/toetsen/toets_namen.gd`: toets dat de kroniek-lijst `naamgenoot` geen "boot" meer bevat.
- Windows-run 44575656543 op 1f63c27: success (GEZIEN, GitHub Actions).

## Deel 2: uitslag
**Akkoord: ja.**
- Klopt: de kroniek (`kroniek.gd` regel 62 tot 64) kiest `naamgenoot` voor elke naamgenoot, zonder te weten of de ouder een laars liet. Daar mag de laarsgrap dus niet staan. De gewone binnenkomst (`kern/binnenkomst.gd` regel 87) kiest `naamgenoot_laars` alleen als `laars_namen` de ouder bevat. Beide paden zijn nu eerlijk.
- Nagekeken: `naamgenoot_hoed` ("wants {ouder}'s hat back") heeft dezelfde vorm, maar wordt alleen gekozen als de ouder door een bewoner is opgegeten (`gevallen_door`), en dan klopt de hoed. Geen fout.
- De twee overgebleven regels in `naamgenoot` zijn gelijk aan die in `kern/regels.gd`; geen gat in de voorraad (twee regels is genoeg naast de herhaalregel).
- Kan (niet nodig voor het bevriezen): de toets leest de lijst met `load()` in plaats van via een preload-constante zoals RT; werkt, maar een preload bovenaan maakt hem gelijk aan de rest.
