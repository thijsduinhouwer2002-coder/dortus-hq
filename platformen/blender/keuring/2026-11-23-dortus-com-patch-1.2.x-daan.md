# Keuring patch dortus.com/click-joints 1.2.x (Daan, 23 nov 2026 ±18:40 NL)

Bestand: `platformen/blender/dortus-com-click-joints-1.2.x.patch` (Bram), voor `click-joints/index.html` in de repo `dortus`.

**Akkoord: ja.** De hoofdchat mag hem toepassen en pushen.

| Punt | Wat in de patch | Oordeel |
|---|---|---|
| M1 | "Every range at a glance. Select a joint ... (from rig, mirror or preset)." | Letterlijk gelijk aan de gekeurde zin in `pro-1.2.1.md` regel 31. Goed. |
| M2 | "Fit test strip: print five joints from 0.10 to 0.30 mm first, so you know which gap fits your printer." | Letterlijk mijn voorstel uit de keuring van 15:50 UTC, klopt met `pro-1.2.1.md` regel 42 (vijf gewrichten, 0,10 tot 0,30 mm). Goed. |
| K1 | "Tested on 4.2 LTS, 5.2 LTS and 5.3" | 5.3.0 draait in elke e2e (GEZIEN, run 45213981354 groen in 4.2.23, 5.2.3 en 5.3.0). Goed. |

Vorm: de diff klopt (hunk 1: 7 tegen 7 regels, hunk 2: 7 tegen 8). Niet toegepast op de site-repo zelf (die zit niet in mijn toegang), dus of de contextregels nog precies passen ziet de hoofdchat bij `git apply --check`.

Kan: de lijst gebruikt nu door elkaar "**Naam.**" en "**Naam:**"; mag later gelijk getrokken, houdt niets tegen.
