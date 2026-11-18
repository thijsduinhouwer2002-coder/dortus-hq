# Uitgaven Het Hol naar Steam

Elke build die echt naar Steam gaat (tak `intern`, nooit openbaar) krijgt hier eerst een regel. De workflow `.github/workflows/steam-uitbrengen.yml` leest deze tabel.

Zo breng je een versie uit:
1. Zet `application/product_version` en `application/file_version` in `producten/steam-hol/godot/export_presets.cfg` (beide presets) op de nieuwe versie, bijvoorbeeld `0.2.0.0`. Push naar main en wacht tot `steam-hol.yml` groen is.
2. Daan keurt de build (skill `keuren`), zijn oordeel staat in `ontwerp/steam/keuring-daan/`. Olaf zet daarna hier de regel met `ja` en het pad van dat bestand.
3. Tag pushen op die commit (of een latere waarin `producten/steam-hol` gelijk is): `git tag hats-steam-v0.2.0 && git push origin hats-steam-v0.2.0`.
   Om te testen: `hats-steam-v0.2.0-proef1` doet alle controles en bouwt, maar uploadt niet (akkoord Daan is dan alleen een waarschuwing).
4. De build staat daarna op de tak `intern` in Steamworks. Live zetten doet alleen Thijs.

Echt uploaden kan pas na de goedkeuring van Valve en de sleutels uit `organisatie/toegang.md`.

| versie | akkoord Daan | keuringsbestand | commit | run | wanneer |
|---|---|---|---|---|---|
