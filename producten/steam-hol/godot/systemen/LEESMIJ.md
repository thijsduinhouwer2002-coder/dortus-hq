# systemen (Bram)
Helden, bewoners, vallen, kroniek, voortgang terwijl je weg bent. Zie de afspraak in `platformen/steam/taken.md`.

- `held.gd`: de held. De kern pakt hem vanzelf (in plaats van `kern/standin_held.gd`). Daans lijf + hoed + wapen,
  karakter (hebzuchtig of schijterig), wrok bepaalt het doel (vijand eerst), kans per verdediging uit `balans.md`
  (slijm 30%, put 22%, +10 tegen zijn eigen vijand), schat aanraken = niets kwijt + Hoard-Toucher, `info.moet_vallen`
  voor de eerste held van een nieuw spel. Boos teken boven het hoofd op weg naar zijn vijand, gouden ster bij 3 keer gevlucht.
- `slijm.gd`: bewoner Gloop met Daans plaatje. Gaat nooit dood: verliest hij, dan is hij 60 s plat (`plat()`, `kan_vechten()`)
  en telt hij zijn happen (`gegeten`). Nog niet gebruikt door `strook.gd` (die zet de stand-in neer).
- `kroniek.gd`, `voortgang.gd`: kroniek met wrok en bijnamen; voortgang terwijl je weg bent (alleen winst, plafond 12 uur, zelfde kansen als held.gd). `Voortgang.verhaal(uitkomst, kroniek.helden, ["Gloop the Slime", "the Spike Pit"], zaad)` geeft 2 tot 3 regels met namen (wie terug was, welke wrok, aartsvijand), elk hooguit 42 tekens.
- Balans: `../../sim/sim.py`, uitkomst in `../../sim/UITKOMST.md`.

Toetsen (Godot 4.3, moeten 0 FOUT geven):
```
godot --headless --path producten/steam-hol/godot --import
godot --headless --path producten/steam-hol/godot -s systemen/toetsen/toets_systemen.gd
godot --headless --path producten/steam-hol/godot -s systemen/toetsen/toets_held.gd
```
