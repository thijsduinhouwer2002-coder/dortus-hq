# Rand en schaduw om elke held (Olaf, 27 nov 2026, issue #242)

Thijs zei dat helden niet opvallen; Iris (#239) zag een held in het fakkellicht links bijna verdwijnen tegen de gele stenen. Keuze Sanne (27 nov ±04:00): voorstel 1 met een schaduwvlek, geen extra loopwip.

**Wat de speler nu ziet:**
- Om elke held een donkere rand van 1 spelpx, warm bijna zwart (#1a1008, dekking 0,85), om lijf en hoed samen. Niet om het teken, de nootjes of de klap. Ook als de held vlucht (gespiegeld) en als hij in de put zakt.
- Onder de voeten een zachte ovale schaduwvlek van 10 x 3 spelpx (dekking 0,35). Bij een sprong blijft hij op de vloer, half zo donker en 70 procent breed; bij een val is hij na 0,2 s weg.
- Het lijf is niet helderder gemaakt: met de rand stond de held in het fakkellicht al los van de stenen (zie de beelden), dus die stap van Sanne was niet nodig.

**Hoe:** `systemen/held_rand.gd`. De rand is het 3D-blad als wit silhouet (één keer per blad gemaakt, 8 tot 10 ms), 4 keer 1 spelpx verschoven getekend in de randkleur, vóór lijf en hoed. De bladen hebben een zachte waas van bijna doorzichtige punten om het lijf; die telt niet mee (alfa onder 96 geen rand, 96 tot 160 zacht oplopend), anders werd de rand een donkere wolk (gezien in de eerste proef). Uit voor vergelijken: `uit3d=rand`. De witte flits staat sinds nu ook in dit bestand, zodat `held_beeld.gd` onder de 400 regels blijft (394).

**Beelden (GEZIEN, Godot 4.3 Linux onder Xvfb, `--write-movie --fixed-fps 5`, `hoogte=120 vers=1 zaad=7 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=640`; voor = zelfde build met `uit3d=rand`). De twee runs lopen niet gelijk, dus het zijn andere helden op bijna dezelfde plek:**
- `links-fakkel-voor-boven-na-onder-1x.png` en `-2x.png`: drie helden in het fakkellicht links, boven zonder, onder met rand.
- `midden-voor-boven-na-onder-1x.png` en `-2x.png`: drie helden in het midden voor de blauwgrijze stenen.
- `held-6x-voor-links-na-rechts.png`: één held van dichtbij.
- `vlucht-gespiegeld-8-beelden-1x.png`: een vluchtende held (gespiegeld) met rand om lijf en tonhoed.
- `held-rand-35s-ware-maat.mp4`: 35 s ware maat met geluid (speltijd 355 tot 390 s), een held loopt door het fakkellicht naar rechts.

**Blinde lezers (GEZIEN, twee aparte lezers, elk 3 beelden op 1x van 1440 x 120, zonder te weten wat er veranderde):**
| | helden in beeld | gevonden | gemiddeld "hoe snel gezien" (1 zoeken, 5 springt eruit) |
|---|---|---|---|
| met rand (`blind-na-*`) | 6 | 6 | 4,0 |
| zonder rand (`blind-voor-*`) | 6 | 6 | 4,2 |

Beide lezers vonden alle helden. Een verschil in hoe snel ze die zagen is hiermee niet te zien: het lage cijfer bij "met rand" (2) is een held die op dat moment in de put valt, naast een "!" en de stekels. Beide lezers noemen een bruine tonhoed die op de bruine wand lijkt (met en zonder rand). Mijn eigen oordeel naast elkaar op 1x en 2x: met rand staat de held in het fakkellicht duidelijk los van de gele stenen, zonder rand loopt het lijf er in over (GOK tot Daan en Iris keken).

**Toetsen (GEZIEN, Linux):** `toets_rand.gd` 0 FOUT (randkleur en maten, silhouet voor alle 9 heldenbladen en 2 hoedenbladen even groot, wit, vol waar het lijf vol is en leeg in de waas, één keer gemaakt; schaduw weg na 0,2 s vallen, kleiner bij een sprong; vlek ovaal met zachte rand). Alle andere toetsen 0 FOUT (held, systemen, tekens, klap, aanloop, licht, namen, vleermuis, berg-wand, opslag). `toets_rand` staat erbij in de Windows-run (`steam-hol.yml`).

**CPU (GEZIEN, eis hooguit +5 procent):** vier runs van 300 s tegelijk op 2 kernen, onder Xvfb, echte tijd, `hoogte=120 vers=1 zaad=5 uitleg_klik=6 koper=1 koper_wacht=8 balk=0`, CPU-tijd van Godot plus Xvfb (user + sys):
| run | met rand | zonder (`uit3d=rand`) |
|---|---|---|
| 1 | 44,18 s | 43,02 s |
| 2 | 44,26 s | 42,76 s |
Gemiddeld **+3,1 procent** (44,22 tegen 42,89). Binnen de eis; per held per beeld 8 extra tekenbeurten met hetzelfde silhouet en 1 voor de vlek.

**Nog open voor "Klaar als":** keuring Daan, en Iris geeft "helden vallen op" een 8.
