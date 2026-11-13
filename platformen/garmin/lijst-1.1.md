# Ebb: lijst voor versie 1.1

Besluit Thijs 12 nov 22:20: wat geen crash, veiligheid of onwaarheid in de winkel is, komt hier en niet meer in 1.0.

- **Orka groter en met meer wit** (flankvlek, witte buik boven water bij inademen). Wens van drie keurders in run 73. Hij is nu te zien (meting run 74: 68 tot 95), maar klein en bij inademen in de nacht geen duidelijke orka. Wijziging aan de tekening, dus eerst Mila.
- **Maanvis bij dag op AMOLED:** het lila lijf (AAAAFF) lijkt op de lila lucht erachter bij inademen (meting run 74: 43 op de fenix 8). Hij heeft een witte rand en valt niet weg. Kleinste stap: een eigen luchtband, zoals de dolfijn en het zeepaardje.
- **Narwal bij dag:** de witte buik valt samen met het lichte zand (FR255) en het schuim. De zwarte omtrek houdt hem leesbaar.
- **Meetscript `meet_dieren_beeld.py`:** de achtergrond uit een beeld zonder dier halen in plaats van uit de rand van het venster (nu meet hij te laag bij golfrand, schuim en zand). Ook de venu 3s en uitademen meenemen.
- **Bouwstraat:** `plaatjes-openbaar` schrijft voor elke proeftak naar dezelfde map op de tak `schermen`. Bij vijf proeftakken tegelijk verloor één run (43315475655) na vijf pogingen, en de job bleef toch groen. Per tak een eigen map, en rood worden als het schrijven niet lukt.
- Uit de taken van run 73: aparte toets voor het eindscherm; `_proefTimer` opruimen; sea complete en "Sit or lie down" op de oude achtergrond.
- **Groepsfoto sea complete op MIP-horloges groeit traag aan** (run 76, kandidaat e40269e1): op de fenix 7 stonden 12 seconden na het openen 16 van de 24 dieren op de foto, terwijl de tekst al "24 of 24 friends" zegt. Zo gebouwd vanwege de watchdog (één dier per beurt). Voor 1.1: meten hoe lang het duurt, en de tekst pas tonen als de foto af is of de foto sneller vullen waar het horloge het aankan.
- **Schermen zonder zee** (gezien run 76): "Sit or lie down" voor de start van Rounds en Calm, de drie veiligheidsschermen, Today en 8 weeks hebben een zwarte of effen achtergrond met alleen een golf onderaan. De rest van de app heeft de onderwaterachtergrond.
- **Scènes voor de bladen:** "fish stays with you" (eindscherm na sessie 1) en "5:00 auto" zitten niet in de volle plaatjesronde. Twee scènes erbij in `Scenes.mc`, zodat ze op elk horloge gezien worden.
