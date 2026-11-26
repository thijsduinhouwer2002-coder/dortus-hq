# Stap 4 tot 6 per soort (#145, Olaf 26 nov 2026)

GEZIEN, Godot 4.3 Linux onder xvfb, `--write-movie --fixed-fps 4`, scherm 1024, `hoogte=120 vers=1 zaad=3 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=900`. Log: `log-zaad3.txt`.

- `sticky-en-sharp-1x.png`, van boven naar onder: 526,0 s, 526,6 s en 527,5 s (kaartje "Sticky Gloop, Bought.", Undo +75; Gloop wipt met het bestaande koopmoment en houdt het Royal-beeld), 821,8 s (bord "Sharp Spikes ready: click the pit", munt boven de put), 822,6 s (kaartje "Sharp Spikes, Bought.", Undo +85; de put houdt het Trick Lid-beeld).
- `stap4-koop-500-560s.mp4` en `stap4-put-795-835s.mp4`: de twee kopen in beweging (4 beelden per s, zonder geluid).

In deze run kocht de proefspeler in 900 s 8 dingen (was 6), de laatste op 822 s.

## Na Daan #154 (kan K1 tot K3), Olaf 26 nov ±10:20 NL

- K1: elke stap 4 tot 6 zegt nu "Heroes drop 2 more gold." (geen "+2 gold" meer).
- K2: geen belofte van meer vangst: Sharp Spikes "Shiny. Heroes drop 2 more gold.", Doom Pit "Heroes drop 2 more gold. For doom.", Sticky Gloop "15 s nap. Heroes drop 2 more gold.", Endless Pit "Endless. Heroes drop 2 more gold."; kroniek "The spikes got shiny." in plaats van "sharper". Alles 34 tekens of minder (toets).
- K3: elke gekochte stap 4 tot 6 geeft bij een vangst één muntje extra in de regen naar de schat (`kern/afloop.gd`). Na Sticky en Sharp vliegen er dus 2 meer (in deze vangst 8 in plaats van 6).
- GEZIEN, zelfde opzet als hierboven, duur 900: `muntjes-voor-671-679s.mp4` (vangst op 674,7 s, voor stap 4), `muntjes-stap4-704-714s.mp4` (vangst op 710,2 s, na Sticky Gloop), `muntjes-voor-na-1x.png` (boven 674,8 tot 675,6 s, onder 807,9 tot 808,7 s na Sticky en Sharp). Log: `log-zaad3-muntjes.txt`.
- Minuut 0 tot 11 verandert niet: de extra muntjes komen pas na stap 4 en zijn alleen beeld.
