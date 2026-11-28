# Les opnieuw voor oude saves (Sanne, 28 nov, #368)

Thijs (28 nov 10:36): "ik snap echt niet wat ik moet doen". Zijn save van 24 nov liep door, dus hij kreeg nooit een les.

Wat veranderde (`kern/eerste_minuut.gd`, `kern/opslag.gd`, `kern/strook.gd`):
- Een save zonder `uitleg_v` 2 krijgt de les één keer opnieuw: welkom met het doel (4 s), dan meteen graven en val zetten (geen kijkstap, er lopen al helden). Daarna nooit meer.
- Het welkom zegt nu het doel: "Heroes want your gold. Trap them first!" (concept tot Thijs hem schrijft; was "Hats of the Fallen. Your taskbar has a basement.").
- Kan een stap nergens (alles gegraven of overal een put), dan gaat hij na 1 s door: de les loopt nooit vast.
- Altijd hooguit één aanwijzing tegelijk (zo was het al; nagekeken in beide films).

Bewijs (GEZIEN, Linux Xvfb, main 1c8dfc5 plus deze wijziging, hoogte 240, 10 fps, 0 SCRIPT ERROR):
- `eerste-30s-nieuw.jpg` en `eerste-30s-oud.jpg`: momenten na 1, 3, 6, 10, 20 en 30 s. Logs: `*-uitleg.log`.
- Oude save: welkom op 0 s, "Click the dirt to dig." op 4,1 s (was: nooit). Nieuwe save: welkom 0 s, graven op 9,1 s.
- Blinde lezer (aparte Claude zonder uitleg, alleen de beelden): snapt bij beide het doel ("helden komen voor je goud, vang ze") en klikt als eerste op het gouden vak; 1 aanwijzing per moment; zekerheid nieuw 6, oud 7 van 10. Nog onduidelijk voor hem: of één vak graven genoeg is, wat de "1" linksboven is.
- Toetsen: alle 12 groen (0 FOUT), 5 nieuwe in toets_systemen.
