# Robot-actiefiguur van Dortus: herkomst en gebruik

- **Wat:** `robot-dortus.glb` is een kijkmodel van de robot uit `../figuur_robot.py` (alle losse vormen met hun
  kleuren, 220 mm hoog, in meters opgeslagen zoals glTF dat wil). GitHub toont het bestand als draaibaar 3D-model.
- **Herkomst:** eigen werk van Dortus, 23 nov 2026, helemaal gemaakt met het script `figuur_robot.py` (afgeronde
  dozen, buizen en bollen uit Blender zelf). Geen download van buiten, geen AI-model, geen merk of bekend personage.
- **Gebruik:** vrij voor de eigen filmpjes, winkelbeelden en posts van Dortus. Wie anders er wat mee mag, beslist
  Thijs (er is bewust geen open licentie op gezet).
- **Laden in de studio:** niet dit bestand, maar `figuur_laden.laad_figuur("robot")`. Die bouwt de robot opnieuw uit
  het script, maakt er met Make watertight één gesloten mesh van en hangt de rig eraan (Mixamo-namen). Dat geeft
  precies het figuur dat in CI getest is. Dit glb-bestand heeft geen rig en bestaat uit losse, overlappende vormen.
