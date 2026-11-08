# Blender proef: architectuur

Doel: bewijzen dat we een add-on in de echte Blender kunnen laden, testen en schermafbeeldingen van de interface kunnen maken op GitHub Actions. Dit is geen product; het eerste echte product neemt deze opbouw over.

- `dortus_proef/`: de add-on als extensie (Blender 4.2+), met `blender_manifest.toml`, een paneel in de zijbalk (tab Dortus) en één knop.
- `e2e/maak_zip.sh`: pakt de add-on in als extensie-zip.
- `e2e/test_achtergrond.py`: `blender -b`, installeert de zip als extensie, controleert aan, operator, paneel en knop. Exit 1 bij een fout.
- `e2e/schermen.py`: start de echte interface onder Xvfb, opent het paneel, maakt schermafbeeldingen voor en na de klik, sluit af.
- `.github/workflows/blender-proef-e2e.yml`: draait beide op Blender 4.2 LTS en 5.2, zet de plaatjes op de tak `schermen` in `blender-proef/<tak>/<versie>/`.

Gecontroleerd 8 nov 2026 (controleur, akkoord met kleine punten, verwerkt): de zip wordt gevalideerd met `blender --command extension validate`; de schermen-stap wordt rood als het tabblad Dortus niet actief werd of de plaatjes ontbreken. De harde poort blijft `test_achtergrond.py`.

Overnemen voor een echt product: kopieer deze map en de workflow en vervang overal `blender-proef`, `dortus_proef`, `DORTUS_PT_paneel`, `dortus.hallo` en `DOEL = "Dortus"` (tabblad). Tabblad kiezen gaat met xdotool Ctrl+muiswiel boven de zijbalk, want `active_panel_category` is alleen-lezen. Quick Setup blijft weg doordat de workflow vooraf voorkeuren opslaat in een eigen map (`BLENDER_USER_RESOURCES`).
