# Uitlegfilm Hats voor Thijs (Sanne, 28 nov, #370)

Film: `hats-uitlegfilm.mp4` (55 s, 1920 x 1080, geen geluid). Direct: https://github.com/thijsduinhouwer2002-coder/dortus-hq/raw/main/producten/steam-hol/uitlegfilm/hats-uitlegfilm.mp4

- Bron: echte opname van het spel, workflow `steam-hol-uitlegfilm.yml` run 46131690893 (main 46c6c4d, 1920 x 240, nieuw spel, `uitleg_klik=3 koper=1 zaad=7`), 0 SCRIPT ERROR (GEZIEN, `opname-film.log`).
- Opbouw per stap: bovenaan titel, in het midden de hele strook op ware maat (wit kader = welk stuk uitvergroot is), daaronder 2x uitvergroot met een gouden ring op wat je aanklikt, onderaan een Nederlandse ondertitel.
- 8 stappen: jij bent het hol; waar helden binnenkomen; graven; val zetten; kopen (muntje); Gloop (ring); bordje hol-niveau; rechtsklikmenu.
- Eerlijk: alleen het rechtsklikmenu is nagetekend (het Windows-menu komt niet in een opname) en staat zo in beeld. Stap 3 is één stilstaand beeld: in de opname stond "Click the dirt to dig." maar 0,1 s in beeld omdat de proefspeler meteen groef.
- Opnieuw maken: `python3 maak_film.py ruw.mp4 scenes.json uit.mp4` (ruw.mp4 uit het artifact van de run). Tien beelden om te kijken in `beelden/`.
