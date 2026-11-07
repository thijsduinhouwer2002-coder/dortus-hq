# Blender proef: architectuur

Doel: bewijzen dat we een add-on in de echte Blender kunnen laden, testen en schermafbeeldingen van de interface kunnen maken op GitHub Actions. Dit is geen product; het eerste echte product neemt deze opbouw over.

- `dortus_proef/`: de add-on als extensie (Blender 4.2+), met `blender_manifest.toml`, een paneel in de zijbalk (tab Dortus) en één knop.
- `e2e/maak_zip.sh`: pakt de add-on in als extensie-zip.
- `e2e/test_achtergrond.py`: `blender -b`, installeert de zip als extensie, controleert aan, operator, paneel en knop. Exit 1 bij een fout.
- `e2e/schermen.py`: start de echte interface onder Xvfb, opent het paneel, maakt schermafbeeldingen voor en na de klik, sluit af.
- `.github/workflows/blender-proef-e2e.yml`: draait beide op Blender 4.2 LTS en 5.2, zet de plaatjes op de tak `schermen` in `blender-proef/<tak>/<versie>/`.
