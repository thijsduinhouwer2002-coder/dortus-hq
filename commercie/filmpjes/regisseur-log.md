# Logboek filmpjes (Regisseur; nieuwste regel bovenaan, hulp van anderen onderaan)

- 23 nov 2026 ±14:00 tot 14:50 NL, Regisseur run 1: nieuwe workflow `regisseur-1.yml` en map `regisseur-1/`: echte opname in Blender 5.3.0 met Pro 1.2.0 en voor het eerst het aangeklede studio-figuur in de opname (niet alleen in stilstaande beelden), plus een nieuw deel met de Fit test strip (echte klik op "Fit test: ball" en "Fit test: hinge"). Daarop de stem-machine met twee hooks: `fit-hook-a` ("Not sure which gap your printer needs?") en `fit-hook-b` ("Still guessing your joint clearance?"), concepten 2026-11-26 en 2026-11-28 in de wachtrij. Onderwerp nieuw: geen Short van de laatste 14 dagen over de Fit test strip.
  Geleerd uit de keuring van de stem-Short (23 nov): getallen in beeld als "0.10 to 0.30 mm" en uitgeschreven alleen in `uitspraak` (A7); niet weer een knie-Short (B3, derde in 4 dagen); hook-kop korter dan de gesproken vraag zodat hij niet twee keer letterlijk staat (C1). Cijfers RSS 23 nov ±14:00 (GEZIEN): "One click: rig to 10 printable parts" 553, "Make your rigged character poseable" 392, "How far can this knee bend" 321, "printable parts with joints" 69 (pas 3 uur oud). De titels met een belofte over het eigen figuur lopen het best; te weinig om een hook-soort te kiezen.
  Gezien in studio-1: in beide renders staat een losse schoen op het podium. In mijn renders gaan losse meshes die niet bij figuur of strip horen uit beeld; oorzaak nog niet gezocht (melding aan hoofdchat).
  Bewust niet gebruikt: de Knight-opname van youtube-shorts-5 (grijs, laag-poly, zwarte renders: niet mooi genoeg voor de lat van Thijs).

## Hulp van anderen
- 23 nov 2026 ±13:55 NL, Olaf: gemeten waar de studio tijd kost (run 45169075703, GEZIEN): per stijl 21 tot 22 min, waarvan
  3 renders van elk 5 tot 6 min (64 samples met raytracing op llvmpipe) en Figure from rig 110 s. Gedaan: `CJ_SAMPLES` in
  `studio.py` en invoer `samples` bij de handstart van `studio.yml` (standaard 64, dus niets veranderd). Proef voor de
  Regisseur: start met samples 24 en vergelijk de renders met studio-1; houdt het beeld stand, dan ±10 min sneller per
  stijl (GOK, nog niet gemeten). Ook: op studio-1 miste de linkerschouder op figuur a; na f9391c8 zegt de studio 9
  gewrichten (`producten/blender-gewrichten/proeven/studio-figuren-2026-11-23/uitslag.md`).
