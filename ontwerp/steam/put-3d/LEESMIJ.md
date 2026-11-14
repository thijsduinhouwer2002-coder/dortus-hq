# Stekelput in 3D per gekochte stap (Daan, 14 nov 2026)

Voorstel voor Olafs kan "stap 1 en 2 van de put zien er nog uit als stap 0" (`hol_3d.gd` zoekt al naar `put_1` en `put_2`).

- `put_stappen.py`: draait Mila's `hol.py` ongewijzigd (zonder de laatste render-regel) en past daarna alleen de put aan. `STAP=0/1/2`.
- `put-stappen-voorstel-4x.png` en `put-stappen-ware-grootte.png`: kolom 3 tot 6 van de gang, 720 x 120, 16 samples. GEZIEN met Read.

Ontwerp:
- **1 Rusty Spikes:** grijs staal met donkere roestbanden, een derde van de stekels helemaal roestbruin, iets scheef. Eerst egaal oranje geprobeerd: frisse kijker "leest als koper of vuur", dus nu staal met roest.
- **2 Deep Pit:** langere, dunnere stalen stekels met roestige voet, en een zwarte, bredere opening op vloerhoogte. Een dieper gat alleen zie je niet (camera 15 graden van boven, onder de vloer is maar 2,6 spelpixel beeld), dus het verschil zit boven de vloer.
- **3 Trick Lid:** blijft zoals Olaf het heeft (dicht is gewone vloer, dat is de grap).

Frisse kijker op ronde b: 6 op ware grootte ("1 springt eruit, 2 lijkt op 0"); ronde c verwerkt beide punten. Volgende stap: Mila neemt de stukken over in `hol.py` (of leest dit script in) en de pijplijn knipt `put_1` en `put_2` uit, zoals `put`. Daarna wil ik een keurstrook op 120 en 160 zien.

Ronde d (±13:50 UTC): frisse kijker op ronde c gaf 6,5 ("1 leest nu als oud roestig staal, goed; silhouet verdwijnt tegen de put; zwart van 2 heeft geen contrast"). Verwerkt: lichte stalen punt op elke roestige stekel, zwarte opening breder (1,72). Een lichte stenen lip voor de opening geprobeerd en weer uit: op 4x een streep dwars door de stekels, leest als een hekje. Besluit: dit is het voorstel; het echte oordeel volgt op de keurstrook in het spel.
