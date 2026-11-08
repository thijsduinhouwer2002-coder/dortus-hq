# Bison & Flex: poster en icoon (Daan)

- `winkel-1-poster.png`: eerste winkelplaatje, 2400 bij 1520 (1200 bij 760 op factor 2, de maat die de JetBrains-winkel aanraadt). Gemaakt van de echte schermen uit IDE-run 42429131027 (main c0562da): `donker-calc-l.png` en `donker-calc-y-structuur.png`, alleen bijgesneden.
- `pluginIcon.svg`: voorstel nieuw pluginicoon, 40 bij 40. Blauwe L (scanner) linksonder wijst met een boog naar de oranje Y (grammatica) rechtsboven. Werkt op licht en donker (`icoon-vergelijking.png`: links nieuw, rechts oud). Jet: kopieer naar `src/main/resources/META-INF/pluginIcon.svg` en `pluginIcon_dark.svg` (zelfde bestand mag voor beide).
- `proIcon16.svg`: 16 bij 16 voor de Pro-balloon, twee vakjes met de pijl ertussen (`proIcon16-voorbeeld.png`, licht en donker). Een eerste 13px-versie zonder pijl was op ware grootte niet te lezen (controleur), daarom 16 met pijlpunt.
- `bron/`: opnieuw maken met `node bron/render.mjs bron/poster.html uit.png donker 2` (vanuit `bron/`, Playwright nodig).
- `winkel-2-grammatica.png` en `winkel-3-scanner.png` (8 nov 06:35): tweede en derde winkelplaatje, zelfde maat en stijl als de poster, van de echte schermen uit IDE-run 42453419735 (`licht-calc-y-structuur`, `donker-calc-l`, alleen bijgesneden). Opnieuw maken vanuit `bron/`: `node kaart.mjs kaarten.json 2 ../winkel-2-grammatica.png` (kop, tekst en snede staan in `kaarten.json`). Plaatje 4 en 5 volgen zodra Jet de schermen met Pro heeft (beoordeling 12).
- Volgorde in de winkel: 1 poster, 2 grammatica, 3 scanner, 4 hernoemen (PRO), 5 melding met snelle oplossing (PRO).
