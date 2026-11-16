# CPU in het gewone spel: waarom is de graver zuiniger? (Bram, 16 nov 2026 ±21:35 UTC)

Vraag Iris (keuring 9, `platformen/steam/keuring/2026-11-16-21.md` punt 3): gewoon spel 0,84 tot 1,23 CPU-s per 10 s, de graver (`koper=1`) maar 0,59.

## Wat ik deed
1. De vier Windows-duurtests van 16 nov (tak `schermen`, `steam-hol-duur/main-1920x1080`, `main-koper-1-1920x1080`, `main-koper-2-1920x1080`, `main-1920x1080-exe`) naast elkaar gelegd: `cpu-per-10s.txt` tegen de regels `HOL meting t= beelden= helden= hol_vast=` uit `hol.log`. Script `cpu_per_beeld.py` en `cpu_plat.py`, uitkomst `uitkomst.txt`.
2. Hetzelfde spel (main, `zaad=4242`, 250 s, 1920 breed, strook 120) op Linux gedraaid met Godot 4.3 onder xvfb (opengl3, software), gewoon en `koper=1`. Script `meet_linux.sh`, uitkomst in `linux/`.

## Wat de cijfers zeggen (GEZIEN)
- **Op Windows kost een beeld bij de graver een derde:** gewoon 16,7 ms CPU per getekend beeld, koper=2 (koopt, graaft niet) 15,3, de .exe 14,1, **koper=1 (koopt en graaft) 5,6**. De graver tekent juist meer beelden (105 per 10 s tegen 67 tot 73), dus het ligt niet aan minder tekenen.
- CPU volgt het aantal beelden (correlatie 0,57 tot 0,69): zonder held in beeld tekent het spel ±1 beeld per s en kost het bijna niets, met een held 10 tot 20 per s. Daarom het patroon hoog, hoog, laag in het ritme van de helden.
- **Niet Gloop plat:** binnen een run is de CPU met en zonder plat ongeveer gelijk (gewoon 1,41 tegen 1,27 met held; koper-2 1,03 tegen 1,10).
- **Niet het vaste hol opnieuw tekenen:** de graver tekent het vaste hol het vaakst (1,4 keer per 10 s tegen 0,25) en is toch het zuinigst.
- **Op Linux is er geen verschil per beeld:** gewoon 9,7 ms, koper=1 10,2 ms per beeld; daar kost de graver juist meer (meer beelden). Het voordeel van de graver bestaat dus alleen op Windows.

## Lezing (GOK, nog niet bewezen)
Het verschil zit in iets dat alleen op Windows telt en dat graven verandert, niet kopen (koper=2 koopt ook en blijft duur). Graven doet op Windows één ding extra: na elk nieuw vast beeld meet `hol_vast.gd` de bovenrand opnieuw en zet `strook.gd` `rand_veranderd()` het muisvlak opnieuw (`DisplayServer.window_set_mouse_passthrough`). Op Windows is dat een vensterregio: buiten het vlak tekent het venster niets. Mogelijk is het vlak dat bij de start één keer gezet wordt (vóór de bovenrand gemeten is, of met de volle hoogte) groter of anders dan nodig, en kost elk beeld daardoor meer om op het scherm te zetten; de graver zet het vlak steeds opnieuw.

## Proef die het beslist (Windows, voor Olaf)
Duurtest gewoon spel met één regel erbij die het muisvlak elke 30 s opnieuw zet (`_muis_vlak(vlak_paneel)` in `_process`, alleen met een startargument). Zakt de CPU naar ±0,6, dan is het het vlak: dan het vlak na de eerste meting van de bovenrand nog één keer zetten. Blijft hij hoog: dan zit het in iets anders dat graven verandert (bijvoorbeeld de helden die bij een gegraven hol korter over het gras lopen), en meet ik dat met een logregel per held boven of in de gang.

## Proef gestart (16 nov ±21:35 UTC, Bram)
Tak `claude/steam-hol-vlak-proef` (7808f65): startargument `vlak_elke=<s>` zet het muisvlak elke s seconden opnieuw, alleen met het argument (2 regels in `kern/strook.gd`, 1 in `kern/proef.gd`; toets_systemen en toets_held lokaal 0 FOUT). Twee duurtests tegelijk op die tak, 20 min, 1920x1080, `zaad=1794860558` (zelfde helden als Olafs gewone run 43948989836): met `vlak_elke=30` (run 43961482697) en zonder (run 43961487906). Uitkomst op tak `schermen` → `steam-hol-duur/claude-steam-hol-vlak-proef-zaad-1794860558-vlak-elke-30-1920x1080/` en `.../claude-steam-hol-vlak-proef-zaad-1794860558-1920x1080/`. Lezing: proef duidelijk lager dan zonder (±0,6 tegen ±1,2) = muisvlak; gelijk = GOK fout, dan meet ik de helden boven en in de gang. De tak gaat niet naar main; Olaf beslist wat er van komt.
