# Hats: klap-ster en witte flits in het spel (issue #25, Olaf 25 nov 2026)

Opgenomen met de Movie Maker van Godot 4.3 (30 fps, strook 160 px, nieuw spel, demo), op Linux met Xvfb (GEZIEN). Windows-run en duurtest staan in issue #25.

- `val-klap-sprong-20s-160px.mp4`: 20 s op ware grootte (seconde 10 tot 30): Kees valt in de put (flits, klap-ster, "+6"), later springt Anouk over de put.
- `flits-strip-2x.png`: de val om de 2 beelden: de held wordt 0,12 s wit, dan 0,06 s half, dan zakt hij weg.
- `klapster-strip-2x.png`: de klap-ster van Mila (4 beelden, 8 per seconde, 0,5 s) met "+6" en de muntjes.
- `val-klap-2x.gif`: de hele val op 2x, elk beeld.
- `sprong-teken-onder-gras-2x.png`: het teken in de sprong blijft nu helemaal in de aarde, onder het gras (kan 2 van Daan, #46).

Code: `kern/klap.gd` (ster uit `kunst/klapster.png`), `systemen/held_beeld.gd` (flits met een eigen ShaderMaterial, alleen tijdens de flits), splitsing `held_val.gd` en `held_noot.gd` (held.gd 337, held_beeld.gd 392 regels).
