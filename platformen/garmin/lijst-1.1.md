# Ebb: lijst voor versie 1.1

Besluit Thijs 12 nov 22:20: wat geen crash, veiligheid of onwaarheid in de winkel is, komt hier en niet meer in 1.0.

- **Orka groter en met meer wit** (flankvlek, witte buik boven water bij inademen). Wens van drie keurders in run 73. Hij is nu te zien (meting run 74: 68 tot 95), maar klein en bij inademen in de nacht geen duidelijke orka. Wijziging aan de tekening, dus eerst Mila.
- **Maanvis bij dag op AMOLED:** het lila lijf (AAAAFF) lijkt op de lila lucht erachter bij inademen (meting run 74: 43 op de fenix 8). Hij heeft een witte rand en valt niet weg. Kleinste stap: een eigen luchtband, zoals de dolfijn en het zeepaardje.
- **Narwal bij dag:** de witte buik valt samen met het lichte zand (FR255) en het schuim. De zwarte omtrek houdt hem leesbaar.
- **Meetscript `meet_dieren_beeld.py`:** de achtergrond uit een beeld zonder dier halen in plaats van uit de rand van het venster (nu meet hij te laag bij golfrand, schuim en zand). Ook de venu 3s en uitademen meenemen.
- **Bouwstraat:** `plaatjes-openbaar` schrijft voor elke proeftak naar dezelfde map op de tak `schermen`. Bij vijf proeftakken tegelijk verloor één run (43315475655) na vijf pogingen, en de job bleef toch groen. Per tak een eigen map, en rood worden als het schrijven niet lukt.
- Uit de taken van run 73: aparte toets voor het eindscherm; `_proefTimer` opruimen; sea complete en "Sit or lie down" op de oude achtergrond.
