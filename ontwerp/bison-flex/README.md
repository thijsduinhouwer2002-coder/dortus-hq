# Bison & Flex: poster en icoon (Daan)

- `winkel-1-poster.png`: eerste winkelplaatje, 2400 bij 1520 (1200 bij 760 op factor 2, de maat die de JetBrains-winkel aanraadt). Gemaakt van de echte schermen uit IDE-run 42429131027 (main c0562da): `donker-calc-l.png` en `donker-calc-y-structuur.png`, alleen bijgesneden.
- `pluginIcon.svg`: voorstel nieuw pluginicoon, 40 bij 40. Blauwe L (scanner) linksonder wijst met een boog naar de oranje Y (grammatica) rechtsboven. Werkt op licht en donker (`icoon-vergelijking.png`: links nieuw, rechts oud). Jet: kopieer naar `src/main/resources/META-INF/pluginIcon.svg` en `pluginIcon_dark.svg` (zelfde bestand mag voor beide).
- `proIcon13.svg`: 13 bij 13 voor de Pro-balloon, zelfde opbouw zonder letters.
- `bron/`: opnieuw maken met `node bron/render.mjs bron/poster.html uit.png donker 2` (vanuit `bron/`, Playwright nodig).
