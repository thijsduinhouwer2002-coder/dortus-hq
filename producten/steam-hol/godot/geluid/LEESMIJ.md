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

## Muziek: `muziek_hol.ogg` ("Gloop's Lullaby", Mila 10 nov)
Getokkelde luit (een geplukte snaar nagebootst in code, zuiver gestemd, nagemeten op 0 cent), zachte bas en een eenvoudige melodie. A klein, 72 slagen per minuut, 24 maten, precies 80 s, loopt naadloos rond (de naklank van het eind zit al in het begin, ook de kamer en het filter lopen rond). Piek -14 dB, dus zachter dan de geluidjes. Opbouw: 4 maten alleen luit, dan melodie A, melodie A met variatie, een lichter deel in C, A terug, en 4 maten alleen luit, zodat de naad stil en zacht is.
In Godot: importeer met Loop aan (Import, Loop: On), speel af op een eigen bus, standaard uit, aan in het rechtsklikmenu ("Music"), los van de geluidjes. Bron `ontwerp/steam/mila/bron/muziek.py`, golf en naad `ontwerp/steam/mila/muziek-golf.png`.
