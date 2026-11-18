# Uitgaven Het Hol naar Steam

Elke build die echt naar Steam gaat (tak `intern`, nooit openbaar) krijgt hier eerst een regel. De workflow `.github/workflows/steam-uitbrengen.yml` leest deze tabel.

Zo breng je een versie uit:
1. Zet `application/product_version` en `application/file_version` in `producten/steam-hol/godot/export_presets.cfg` (beide presets) op de nieuwe versie, bijvoorbeeld `0.2.0.0`. Push naar main en wacht tot `steam-hol.yml` groen is.
2. Daan keurt de build (skill `keuren`), zijn oordeel staat in `ontwerp/steam/keuring-daan/`. Olaf zet daarna hier de regel met `ja` en het pad van dat bestand.
3. Op die commit (of een latere waarin `producten/steam-hol` gelijk is) de uitgavetak pushen: `git push origin HEAD:refs/heads/uitgave/hats-steam-v0.2.0`.
   Een tag `hats-steam-v0.2.0` werkt ook, maar een tag pushen geeft vanuit onze sessies 403 (GEZIEN 18 nov); Thijs kan het wel.
   Om te testen: `uitgave/hats-steam-v0.2.0-proef1` doet alle controles en bouwt, maar uploadt niet (akkoord Daan is dan alleen een waarschuwing).
   Een uitgavetak blijft staan: de workflow kijkt daaraan welke versies al uit zijn.
4. De build staat daarna op de tak `intern` in Steamworks. Live zetten doet alleen Thijs.

Echt uploaden kan pas na de goedkeuring van Valve en de sleutels uit `organisatie/toegang.md`.

| versie | akkoord Daan | keuringsbestand | commit | run | wanneer |
|---|---|---|---|---|---|
