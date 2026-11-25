# Keuring Hats: geluid klinkt echt (keurissue #51, commit 19f40c5), 25 nov 2026 ±07:00 NL, Daan
Wat ik keurde: `kern/geluid.gd`, de haken in `kern/afloop.gd`, `kern/kaartje.gd`, `kern/venster.gd`, `toets_klap.gd`, de wav's in `godot/geluid/`.
Akkoord: ja op deel A en B, onder voorwaarde dat Windows-run 45556235322 groen eindigt (liep nog bij deze keuring).

## Deel A: code
| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| 1 | Vier spelers, -6 dB, munt hooguit één per 0,12 s; vangst geeft plof of hap en 0,18 s later de munt; koop bij een aankoop, lied als een bard vlucht. Klopt met de belofte. | Feit, code gelezen | hoog |
| 2 | `t` loopt alleen als er iets wacht (`set_process` uit als het stil is). De muntgrens rekent met `t`; dat werkt omdat de munt alleen via `vangst()` komt, die de klok aanzet. Roept iemand later `speel("munt")` direct aan, dan staat `t` stil en wordt elke volgende munt geweigerd. | Feit (nu geen fout), vermoeden voor later | midden |
| 3 | Als alle vier bezet zijn, neemt het altijd speler 0, niet de oudste. Klein. | Feit | hoog |
| 4 | Toets dekt plof, munt, twee happen tegelijk geeft één munt, koop, -6 dB. | Feit | hoog |

## Deel B: zacht genoeg naast werk, munten ratelen niet
Ik kan het niet beluisteren; ik heb de wav's gemeten (GEZIEN): piek -9 dBFS, gemiddeld (rms) -19 tot -25 dBFS, kort (0,14 tot 0,89 s), mono 22 kHz. Met -6 dB in Godot wordt dat piek ±-15 dBFS: zacht, onder een gewone melding van Windows (GOK). Munt hooguit één per 0,12 s, dus geen geratel. Uit via Sound dempt bus 0. Naast Rusty's Retirement (dat ook zacht geluid heeft en "playable without timed input" is) stoort dit niet. Cijfer 8.

## Kan
1. Ook plof en hap een kleine grens geven (bijv. 0,08 s): twee vangsten in hetzelfde beeld klinken nu dubbel zo hard.
2. `t` altijd laten lopen of `Time.get_ticks_msec()` gebruiken, zodat punt A2 nooit kan bijten.
3. LEESMIJ noemt een bus "Hol"; de code speelt op de hoofdbus. En de muziek (piek -14 dB) is nu luider dan de geluidjes (±-15), terwijl de LEESMIJ zegt "zachter". Tekst of getal gelijk trekken.
