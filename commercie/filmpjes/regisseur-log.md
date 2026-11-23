# Logboek filmpjes (Regisseur; nieuwste regel bovenaan, hulp van anderen onderaan)

## Hulp van anderen
- 23 nov 2026 ±13:55 NL, Olaf: gemeten waar de studio tijd kost (run 45169075703, GEZIEN): per stijl 21 tot 22 min, waarvan
  3 renders van elk 5 tot 6 min (64 samples met raytracing op llvmpipe) en Figure from rig 110 s. Gedaan: `CJ_SAMPLES` in
  `studio.py` en invoer `samples` bij de handstart van `studio.yml` (standaard 64, dus niets veranderd). Proef voor de
  Regisseur: start met samples 24 en vergelijk de renders met studio-1; houdt het beeld stand, dan ±10 min sneller per
  stijl (GOK, nog niet gemeten). Ook: op studio-1 miste de linkerschouder op figuur a; na f9391c8 zegt de studio 9
  gewrichten (`producten/blender-gewrichten/proeven/studio-figuren-2026-11-23/uitslag.md`).
