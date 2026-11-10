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
- `kroniek_regels.gd`: de ene voorraad kroniekregels (Sanne, `platformen/steam/kroniek-regels.md`), ook met de soorten die `kern/strook.gd` gebruikt (terug_bewoner, terug_val, val, val_bewoner, plat, op, hoed_klein). `kies(soort, v, achter)`: achter een tekst (" +7") wordt erachter geplakt; achter een getal houdt zoveel tekens vrij en geeft nooit leeg (zoals Olafs oude `kern/regels.gd`). Per soort de laatste 4 overgeslagen en over alle soorten heen niets uit de laatste 10 (Sanne toets 5). Naamgenoot: `{naam}` is "Kees II", `{oud}` is "Kees".
- `held.gd`: `info.snelheid` (factor, standaard 1.0) voor de demo; `WAND_ER := false`: zolang de wand niet te zien is gaat ook de hoed van een aartsvijand op de bewoner die hem at (Sanne 22:55).
- `held_beeld.gd` (10 nov): het tekenen van de held (lijf, littekens, hoed, wapen, teken, de val met poef), los van `held.gd`. `held.gd` roept in `_draw()` alleen `HELD_BEELD.teken(self)` aan. `HOED_TOP` blijft in `held.gd`.
- `held.gd` (10 nov): `naar_dict()` en `herstel(hol, d)` om een held die nog loopt te bewaren en terug te zetten (na `add_child`).
