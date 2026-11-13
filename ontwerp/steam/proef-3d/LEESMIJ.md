# Proef: Gloop als 3D-model in Blender (hoofdchat, 13 nov 2026)

Aanleiding: Thijs koos beelden uit eigen werk (route C) en vroeg om proactief te zoeken naar gratis gereedschap. Gevonden route zonder AI en zonder kosten: **figuren modelleren in Blender met code (bpy) en renderen**. Bekende techniek, onder meer gebruikt voor Dead Cells (3D-modellen gerenderd tot sprites). Blender draait al in onze GitHub Actions (Click Joints) en als Python-pakket in de werkomgeving (`pip install bpy`, versie 5.2.4).

- `gloop.py`: het model (metaballen voor het lijf, één oog, scheve grijns met één tand, helm, puntmuts en kroon), licht (warme fakkel, koel tegenlicht) en een orthografische camera. Eén render van 900x900 duurt ±45 s op de CPU.
- `groot2.png`: de render. `pixel40.png`: dezelfde render simpel verkleind tot 40 px hoog. `gloop-proef-3d.png`: naast de huidige Gloop.

Eerste oordeel (hoofdchat, Thijs beslist): de 3D-render is de sterkste kandidaat voor de **winkelafbeelding** (daar staan we het zwakst). Simpel verkleinen naar pixelart werkt niet: het wordt modder. Voor de figuren in het spel blijft de getekende pixelart beter, tenzij we een echte 3D-naar-pixel-stap bouwen (vaste kleuren, rand, geen zachte schaduw).

Ook bekeken (13 nov): gratis AI-pixelgenerators en MCP-servers (PixelLab, Retro Diffusion, Hugging Face, Gemini). Die vragen een sleutel van Thijs en een **openbare AI-melding op de Steam-pagina** (Valve, regels jan 2026: ook winkelbeelden tellen). Blender-renders vallen daar niet onder.
