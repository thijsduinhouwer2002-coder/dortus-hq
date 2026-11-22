# Productkans Blender: verlaten bestsellers na Blender 5

Vera, 8 nov 2026 run 19:31 (Amsterdam). **Uitkomst: geen sterke kans. Cijfer 2. Advies: nee.** Dit bestand staat er vooral zodat niemand deze route opnieuw loopt.

## Het idee
Blender 5.0 (nov 2025) haalde twee dingen weg waar oude add-ons op leunen: de tekenmodule BGL en `scene.node_tree` voor de compositor (GEZIEN, https://developer.blender.org/docs/release_notes/5.0/python_api/). Een betaalde add-on die veel verkocht maar niet meer werkt op 5.x, zonder opvolger, is precies het soort gat uit de proef van Thijs: bewezen betalen, zwakke of afwezige nummer één.

## Hoe gemeten
- De 190 best verkochte add-ons van Superhive (`/categories/addons/browse?sort_sales=desc`, pagina 1 tot 8), met per product de verkoopteller en de tag "Blender Version" (GEZIEN, 8 nov). Laagste teller in de lijst: 1.300+. Data: `data/superhive-bestsellers-addons-2026-11-08.jsonl`, script `data/superhive-bestsellers-script.py`.
- Tag hoogste versie: 5.2 bij 139, 5.1 bij 16, 5.0 bij 20, **lager dan 5.0 bij 15** (GEZIEN).
- Die 15 (zonder Pie Menu Editor, dat Bram al onderzocht in `platformen/blender/kandidaten-2026-11-07.md`) door een onderzoeker nagelopen: changelog, 2 tot 4 pagina's reviews, opvolgers op Superhive en extensions.blender.org. Vier punten zelf nagekeken met curl (drag-n-drop-import, Lens Sim, Launch Control, Easy Fog 2): kloppen.

## Wat eruit kwam (GEZIEN, links per product op superhivemarket.com/products/<naam>)
| Add-on | Verkocht | Waarom het gat dicht is |
|---|---|---|
| Easy Fog (alt-tab-easy-fog) | 5.800+ | zelfde maker heeft Easy Fog 2, 4.700+, tag tot 5.2 |
| BQR Boolean Quad Ready | 4.800+ | maker actief (antwoord 5 maanden geleden), set modifiers, werkt waarschijnlijk nog (GOK) |
| SurfaceFlow | 4.000+ | maker actief, versie 2.1.0, tag verouderd |
| Tesselator, DynRemesh 2 | 3.700+, 3.100+ | verlaten met klachten, maar Smart Remesh (2.500+, tot 5.2), SoftWrap (3.700+), QRemeshify vullen het |
| Mask Tools | 2.500+ | gratis Ucupaint (320.082 downloads, vorige week bijgewerkt) |
| Pro Lens 2 | 2.400+ | Lens Sim (7.500+, $40, tot 5.2) |
| Turbo Tools v3 | 2.400+ | pagina verwijst zelf naar de nieuwe Turbo Tools voor Blender 5 |
| Drag-n-Drop Import | 2.300+ | pagina: "no longer maintained, as the functionality was added in Blender natively" (Blender 4.1 en 4.2) |
| Car Rig Pro | 2.000+ | Launch Control (3.400+, $59, tot 5.2), RIGICAR |
| Erintools | 1.300+ | nodegroepen, werken meestal nog, veel gratis (GOK) |
| Pixel (alttab-pixel) | 1.400+ | **onduidelijk**: geen klachten, maker actief, opvolgers voor 5.x verkopen maar 10+ tot 100+ |
| Angle Tool | 1.300+ | **onduidelijk**: laatste fix nov 2023 (BGL), geen directe opvolger, niet getest of het kapot is |

## Het gat in één zin
Er is geen echt gat: bijna elke verlaten bestseller heeft binnen een jaar een opvolger die 5.x steunt, vaak van dezelfde maker, of Blender bouwde het zelf in.

## Waarom cijfer 2
- De top van Superhive wordt goed onderhouden: 175 van de 190 bestsellers steunen 5.x al volgens de tag, en van de 15 andere zijn er 13 dicht.
- De twee onduidelijke (Pixel, Angle Tool) zijn klein (samen ±2.700 verkopen in jaren, $10) en niet bewezen kapot. Pixel kan morgen een nieuwe tag krijgen; die maker werkt Easy Fog 2 wel bij.
- Les voor de ploeg (GEZIEN): op Blender wint een gat door een nieuwe Blender-versie niet vanzelf; makers en concurrenten springen er snel in. Dat past bij wat Bram vond bij Pie Menu Editor (PieMaster kwam binnen maanden).

## Wat het oordeel kan veranderen
- Pixel of Angle Tool blijkt in een test op Blender 5.2 echt kapot en de maker reageert niet: dan Pixel opnieuw wegen (kleine niche, ±$500 tot $1.000 per maand als je de oude verkoop haalt, GOK).
- Een betere volgende zoektocht (advies onderzoeker): bestsellers die de compositor via Python aansturen of BGL-tekencode gebruiken, ook buiten de top 190.

Geen bericht naar Bram of Olaf: er is geen kans die ze kunnen oppakken.
