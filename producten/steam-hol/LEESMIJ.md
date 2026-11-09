# Het Hol (werknaam), Steam-bureaublad-spel

Jij bent de kerker. Onderaan je scherm, net boven de taakbalk, ligt jouw hol. Helden klimmen erin om je schat te stelen; je graaft gangen, zet vallen en laat je slijm het werk doen. Wie ontsnapt, komt terug met een litteken, een wrok en een bijnaam.

- Besluit Thijs 9 nov 2026 19:20: richting Het Hol, meteen het spel bouwen. Niets betalen of publiceren tot Thijs het prototype goedkeurde.
- Wie waar schrijft: `platformen/steam/taken.md`. Kern (`godot/kern/`, `godot/hol/`): Olaf. Systemen (`godot/systemen/`, `sim/`): Bram. Kunst (`godot/kunst/`): Daan.
- Test: `.github/workflows/steam-hol.yml` start het spel op een Windows-runner met Kladblok erachter, maakt schermafbeeldingen op 96, 120 en 160 px, meet de CPU en maakt een GIF van een minuut spelen (Godot Movie Maker). Uitkomst op de tak `schermen`, map `steam-hol/<tak>`.
- Argumenten na `--`: `hoogte=96..160` (standaard 120), `duur=<s>`, `log=<pad>`, `demo=1` (vaste helden en graven voor de film), `film=1`, `vers=1` (zonder opslag).

Stand 9 nov 18:30 UTC: eerste kern met blokjes (nog geen kunst), stand-in held en slijm van Olaf tot Bram zijn systemen levert.
