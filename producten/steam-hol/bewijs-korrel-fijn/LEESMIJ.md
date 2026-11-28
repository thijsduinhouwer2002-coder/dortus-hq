# Fijne korrel in kamer en gangwand op 160 px en hoger (Mila, 28 nov)

Waarom: Iris #334 punt 1 (keuring e70eab3 op 200 px): "grove vierkante vlekken in de gegraven kamers en de gangwand ... blokken van 5 x 5 schermpixels naast gladde 3D. Twee soorten beeld door elkaar: dat is wat cheap zegt." De hoofdmanager zette de header (#30) stil tot het spelbeeld zelf beter is (#333); dit is mijn stuk daarvan.

Wat er veranderde (alleen vanaf schaal 4, dus 160, 200 en 240 px; op 96 en 120 px is elke regel hetzelfde als eerst):
- `godot/hol/kamerwand.gd`: korrel in de kamerbuis tekent op schermpixels. Spikkels ±2 x 2 schermpx op een vaste plek in hun spelpixel; bovenrand 2 tot 3 schermpx met een doorlopende zachte schaduw eronder (was blokjes van 5 px die per kolom verschilden); happen als smalle druppels; steentjes met 1 schermpx lucht en een glimlijntje; barstjes als dunne lijn; laagjes dunner. Welke spelpixels iets krijgen blijft precies hetzelfde (`pixels()`, de toets ziet geen verschil).
- `godot/hol/metsel.gd`: voegen ±3 schermpx, lichte bovenkant, schaduwrand en zijkant ±2, vlekjes en barstjes als stipjes, afgebrokkelde bovenkant ondieper met treden van 1 schermpx.
- `godot/hol/achterwand.gd`: de vochtige laag onder het plafond van de kamer is een glad verloop in plaats van 6 treden van 5 schermpx.

Bewijs (GEZIEN, eigen films Godot 4.3 Linux onder Xvfb, `--write-movie --fixed-fps 5`, `hoogte=200 vers=1 zaad=12 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 palet=zacht`, dezelfde args als Iris in #334):
- `min10-200-zacht-voor-na-2x.png` en `...-2x-midden.png`: boven main (beeld van Iris, e70eab3), onder deze versie, minuut 10, 2x.
- `min10-200-zacht-voor-na-1x.png`: hele strook op ware grootte, boven voor, onder na.
- `scherm-zd-min10-200-zacht-korrelfijn-ware-maat.png`: dezelfde strook op het bureaublad van Iris (voor de blinde test).
- 0 SCRIPT ERROR in films op 160 en 200 px (20 s) en 200 px (600 s). Alle 11 toetsen 0 FOUT.

Bekeken met Read op 1x en 2x. Wat ik zie: de kamers lezen nu als aarde met fijne korrel in de stijl van de 3D-figuren, geen dambord van blokjes meer; de stenen in de gang hebben dunne voegen en een fijne rand. Nog grof: de bovenste voeg tussen aarde en gangwand (1 spelpx, met opzet, dat is de rand van de muur).
