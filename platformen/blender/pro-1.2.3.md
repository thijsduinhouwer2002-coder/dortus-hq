# Click Joints Pro 1.2.3: Figure from rig betrouwbaar (Bram, 24 nov 2026)

**Waarom (geld):** saleweek begint do 26 nov. Een koper die bij Figure from rig de ene keer 8 en de andere keer 9 gewrichten krijgt, of een overgeslagen heup zonder uitleg, denkt dat Pro kapot is. Effect op verkoop: GOK, klein; vooral minder klachten en terugbetalingen.

**Wat erin zit:** tak `claude/betrouwbaar-rig` van de agent Betrouwbaarheid (alleen `betaald/`, gratis zip gelijk). Uitslag: `producten/blender-gewrichten/proeven/betrouwbaar-rig-2026-11-23/uitslag.md` op die tak.

## Stand (24 nov ±10:00 NL, Bram)
1. Keuring A (herkeuring op 37de78bce) en B: akkoord ja. Automatische keurder: ja. Daan: Engelse teksten ja na M1 en M2.
2. Op main als één commit (de tak heeft geen gedeelde geschiedenis met main meer, dus geen merge mogelijk): alleen de bestanden van Betrouwbaarheid (`betaald/` omhulsel, herstel, redenen, rig, scharnier, terugval, `__init__`; `e2e/meet_*`, `toetsen_mens.py`; uitslag; `architectuur.md`; workflow `betrouwbaar-rig.yml`; stap `CJ_HERKANS=3` in de e2e). Nieuwere bestanden van main (gratis zip 0.1.2, keuringen, regisseur-workflows) bleven van main. Gratis deel ongemoeid.
3. PRO_VERSIE 1.2.3 in `blender-gewrichten-e2e.yml` en `betrouwbaar-rig.yml`; uitgave-workflow op tag `click-joints-pro-v1.2.3`; tak uit de trigger van de e2e. K2 van Daan (puntkomma na "here") in `redenen.py`.
4. Volgende: e2e op main helemaal groen (ook 4.2.23), dan uitgave-run en run-id plus artefactnaam naar de hoofdchat.

## Cijfers die in de tekst mogen (GEZIEN door Betrouwbaarheid, nageteld door keurder A)
- 5.2.3 en 5.3.0: testset van 7 figuren, elke figuur 5 keer: 60 van 60 in elke herhaling (was 53 tot 55, wisselend).
- 4.2.23: op dezelfde zes figuren 28 naar 44 van 51. Niet "51 van 60" gebruiken. 4.2 is op lichte figuren 2 tot 3,6 keer trager.
- 4.5 is niet gemeten: niets over 4.5 beloven.

## Releasenote 1.2.3 (Engels, gekeurd door Daan na M1, M2 en K1; Gumroad en Superhive)
```
Click Joints Pro 1.2.3
- Figure from rig is more reliable on figures with arms or legs close to the body. On our test figures in Blender 5.2 and 5.3 it placed every joint, and the same mesh gave the same joints every time we ran it.
- When Figure from rig skips a joint, the list now says why and what you can do.
- Blender 4.2 also skips fewer joints, but can still skip some joints and is slower on light figures. Blender 5.2 and 5.3 cut best.
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```
"Some joints" dekt ook de linkerschouder en linkerheup op de robot (wens hoofdchat en keurder H8). Plaatsen pas na groene e2e op main in alle drie versies.
