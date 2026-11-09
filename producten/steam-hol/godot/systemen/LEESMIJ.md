# systemen (Bram)
Helden, bewoners, vallen, kroniek, voortgang terwijl je weg bent. Zie de afspraak in `platformen/steam/taken.md`.
Zolang `held.gd` hier niet staat, gebruikt de kern de stand-in `kern/standin_held.gd` (Olaf). Zet je eigen `held.gd` hier
(extends Node2D, met `func start(hol, info: Dictionary)` en signaal `klaar(held, uitkomst: String, info: Dictionary)`),
dan pakt de kern hem vanzelf.
