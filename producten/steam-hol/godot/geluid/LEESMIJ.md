# Geluid Het Hol (Mila, 10 nov)

Zelf gemaakt in code door `ontwerp/steam/mila/bron/geluid.py` (geen licentie van anderen nodig). Pas de wav's niet met de hand aan: pas het script aan en draai het opnieuw.

Klank: zacht en rond (sinus en driehoek), kort, piek -9 dB, geen tik aan begin of eind. Standaard uit (Olaf 01:40), aan via het rechtsklikmenu.

| bestand | wanneer | lengte |
|---|---|---|
| `hap.wav` | Gloop slokt een held op (twee blubs en een boertje) | 0,33 s |
| `munt.wav` | munt komt op de schat (B5 dan E6, "pling") | 0,21 s |
| `val.wav` | held valt in de stekelput (glijfluitje omlaag, plof) | 0,48 s |
| `poef.wav` | het boze wolkje van een wrok knapt (`poef.png`) | 0,14 s |
| `koop.wav` | je koopt een upgrade (C6 E6 G6) | 0,34 s |
| `lied.wav` | de bard ontsnapt en zingt (vijf getokkelde noten) | 0,89 s |

Regels voor het afspelen (voorstel Mila): bij veel munten tegelijk hooguit één `munt` per 0,12 s, anders wordt het geratel. Volume in Godot op -6 dB onder de rest van de computer (AudioServer bus "Hol"). Golfvormen: `ontwerp/steam/mila/geluid-golven.png`.
