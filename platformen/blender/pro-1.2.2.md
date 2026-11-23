# Click Joints Pro 1.2.2: minder mislukte sneden (Bram, 23 nov 2026)

**Waarom (geld):** een Pro-koper die "no watertight parts" krijgt, of bij Figure from rig een gewricht minder dan een ander, denkt dat de add-on kapot is. Dat kost reviews en terugbetalingen in de saleweek. Effect op verkoop: GOK, klein, vooral minder klachten.

**Wat erin zit (allemaal Pro, het gratis deel blijft gelijk aan 014172e):**
1. Terugval naar Exact (`betaald/terugval.py`, deze tak `claude/blender-solver-terugval`): geeft de Manifold-snede een open deel, dan één keer opnieuw met Exact.
2. Figure from rig zoekt verder na "no watertight parts" (Olaf, `rig.py`, op main sinds 80417b8, toets `CJ_HERKANS`; automatische keurder akkoord ja).
3. Figure from rig: na een geweigerde kogelsnede nog één plek 0,3 mm verder het lid in (Olaf, `rig.py`, main 6dcadc8; robot linkerheup op CI 8 naar 9 gewrichten, runs 45206324187 en 45208410893, GEZIEN door Olaf; automatische keurder akkoord ja). Olaf (17:45): toets `CJ_HERKANS=2` laat zien dat de 0,3 mm-plek op andere leden net zo vaak kapot is; erin laten (schaadt niets), maar het is geen vangnet. Echte oplossing (A4) staat als kandidaat 5 in `pro-1.3-kandidaten.md`. Releasenotes zeggen daarom niets over processors.

## Stand
1. Keurder (auto, 542c4be) akkoord nee met 2 moet. Opgelost: `terugval.py` omhult ook `markeer` zodat `cj_solver` na de terugval EXACT is; de toets `solver_terugval` toetst weer 0, 1 en 2 keer open (2: ook de Exact-snede open, operator weigert, figuur heel, geen hulpresten) en controleert `cj_solver`. `architectuur.md` bijgewerkt. Main (met de fix van Olaf) in de tak gevoegd.
2. e2e op 019170f (run 45206694580) groen in alle drie versies (GEZIEN). 23 nov ±17:20 NL: main met 6dcadc8 (heupfix Olaf) in de tak gevoegd; e2e 45213981354 op a3f5e85 groen in 4.2.23, 5.2.3 en 5.3.0 (GEZIEN).
3. Daan akkoord (keuring `keuring/2026-11-23-pro-1.2.2-daan.md`, ook releasenotes). 23 nov ±18:10 NL (Bram): tak op main gevoegd met PRO_VERSIE 1.2.2. e2e 45225138956 groen; uitgave-run 45230763628 groen, artefact tot 26 nov 17:44 UTC. Uploaden op Gumroad en Superhive: Thijs (via de hoofdchat).

## Releasenotes 1.2.2 (Engels, Gumroad en Superhive; akkoord Daan)
```
Click Joints Pro 1.2.2
- Fewer failed cuts: if a cut with the fast solver leaves a part that is not watertight, Click Joints Pro cuts once more with the Exact solver before giving up.
- Figure from rig: when a cut fails at one spot, it now tries the next spot on that bone instead of skipping the joint.
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```
