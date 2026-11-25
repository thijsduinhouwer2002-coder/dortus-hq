# Echt spel, 10 min, een speler die koopt (Mila, 25 nov ±17:20 NL, issue #62, voor Iris #7 en Daan #84)

Iris (keuring 77d657f) zag de Gloop-les nog in geen echt spel en vroeg een film van 10 min van deze build waarin de speler koopt zodra het kan, met geluid. Dit is die film.

**Film:** `koper-10min-1920-ware-grootte.mp4`, 605 s, 1920 x 120 (ware grootte op een 1080p-scherm), 10 beelden per s, met geluid (gemiddeld -45,8 dB, piek -12,4 dB, gemeten met ffmpeg). Main 2da580e (spel gelijk aan 77d657f plus de les van 58824bb). Godot 4.3 Linux onder Xvfb, `--write-movie --fixed-fps 10`, `hoogte=120 vers=1 zaad=2 uitleg_klik=6 koper=1 koper_wacht=8 balk=0`. Log: `koper.log`.

**De proefspeler:** doet wat de les zegt (na 6 s), en koopt elk ding als het al 8 s kan (`koper_wacht=8`, nieuw, alleen voor films). Zonder die bedenktijd kocht de oude koper binnen een tel, nog voor ring en les in beeld kwamen; geen mens doet dat.

**Wat je ziet (GEZIEN, log en strips):**
- 188,4 s: 50 goud, ring met munt gaat aan om Gloop, en tegelijk één keer de les "Click Gloop to grow him." met pijl op zijn kruin. Op het bord geen regel, alleen het verhaaltje.
- 194,5 s: de speler klikt op Gloop, het kaartje "Big Gloop, Bigger mouth. More heroes fall. Buy 45" gaat open, de les is weg (na 6,1 s).
- 197,3 s: gekocht. Ring uit, Gloop staat zichtbaar groter in het hol.
- 509,6 s: tweede koop, de Spike Pit.
- Strips: `koper-ring-les-strip-1920-ware-grootte.png` (hele strook) en `koper-ring-les-strip-rechts-2x.png` (rechterhelft 2x), op 186, 188,8, 191, 194,8, 197,8 en 199 s.

**Eerlijk, voor Sanne en Iris (tempo-regel 4):** een speler die koopt zodra het kan, koopt in 10 min maar 2 dingen (197 s en 510 s, zaad 2, GEZIEN). Tussen 197 en 510 s, ruim 5 min, is er niets te kopen en staat de ring dus niet aan. Dat is tempo, niet beeld; issue #76 (elke aankoop zichtbaar) hangt eraan.

**Code (alleen proef):** `kern/ritme.gd` `tik_koper` (bedenktijd per soort, koopt in een kaartje dat al openstaat), `kern/proef.gd` (startargument `koper_wacht`). Zonder `koper_wacht` werkt de koper als voorheen. Toetsen 7 x 0 FOUT op Linux.
