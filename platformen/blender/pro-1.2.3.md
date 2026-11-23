# Click Joints Pro 1.2.3: Figure from rig betrouwbaar (Bram, 24 nov 2026)

**Waarom (geld):** saleweek begint do 26 nov. Een koper die bij Figure from rig de ene keer 8 en de andere keer 9 gewrichten krijgt, of een overgeslagen heup zonder uitleg, denkt dat Pro kapot is. Effect op verkoop: GOK, klein; vooral minder klachten en terugbetalingen.

**Wat erin zit:** tak `claude/betrouwbaar-rig` van de agent Betrouwbaarheid (alleen `betaald/`, gratis zip gelijk). Uitslag: `producten/blender-gewrichten/proeven/betrouwbaar-rig-2026-11-23/uitslag.md` op die tak.

## Stand (24 nov 00:15 NL)
1. Keuring B akkoord ja (5aa27a88d). Keuring A akkoord nee: M1 verlies bij kogelsneden meten (op de tak in 1945f46), M2 cijfers 4.2 rechtzetten (nog niet in de uitslag op 1945f46: daar staat nog "51 van 60"). Wacht op herkeuring A.
2. Automatische keurder op 1945f46: akkoord ja, alleen kan-punten.
3. Na ja van A: tak als één commit op main, PRO_VERSIE 1.2.3 in `blender-gewrichten-e2e.yml` (en de uitgave-workflow op tag `click-joints-pro-v1.2.3`), beide kanten van `berichten/hoofdchat.md` houden, e2e op main groen, uitgave-run, hoofdchat melden.

## Cijfers die in de tekst mogen (GEZIEN door Betrouwbaarheid, nageteld door keurder A)
- 5.2.3 en 5.3.0: testset van 7 figuren, elke figuur 5 keer: 60 van 60 in elke herhaling (was 53 tot 55, wisselend).
- 4.2.23: op dezelfde zes figuren 28 naar 44 van 51. Niet "51 van 60" gebruiken. 4.2 is op lichte figuren 2 tot 3,6 keer trager.
- 4.5 is niet gemeten: niets over 4.5 beloven.

## Concept releasenote 1.2.3 (Engels, Gumroad en Superhive; nog niet gekeurd, bij Daan)
```
Click Joints Pro 1.2.3
- Figure from rig is more reliable on figures with arms or legs close to the body. On our test figures in Blender 5.2 and 5.3 it placed every joint, and the same mesh now always gives the same joints.
- When Figure from rig skips a joint, the list now says why and what you can do.
- Blender 4.2 also skips fewer joints, but can still skip a knee and is slower on light figures. Blender 5.2 or newer cuts best.
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```
Waarom zo: het voorstel van Betrouwbaarheid noemde "Blender 4.5+", maar 4.5 is niet gemeten (keuring A). "Every joint" geldt alleen voor onze testset, daarom "on our test figures".
