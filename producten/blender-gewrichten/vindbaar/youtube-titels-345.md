# Klaar om te plakken: twee YouTube-titels Pro (#345)

Bram, za 28 nov 2026 ±06:20 NL. Titels gekeurd door Daan in #335 (eerste zoals voorgesteld, tweede met zijn M1). Alleen de titel wijzigt; beschrijvingen blijven zoals in #244.

Waar: YouTube Studio, kanaal Dortus, Inhoud, video openen, Details, Titel, Opslaan.

| Video | Nu (RSS 28 nov 06:10, GEZIEN) | Wordt (plakken) |
|---|---|---|
| 4-3l3MZZWPc | Blender rig to 3D printable figure: one button, hinges and ball joints \| Click Joints Pro | `Ball Joints for 3D Printed Action Figures in Blender: One Button from Your Rig \| Click Joints Pro` |
| m3sNvDOJYQ0 | Blender hinge for 3D printing that stops at 115° \| Click Joints Pro | `Hinges for Poseable 3D Printed Figures in Blender: Stops at 115° \| Click Joints Pro` |

Lengte 97 en 83 tekens (grens YouTube 100, GEZIEN met Python). Het teken in de tweede titel is een gradenteken (°).

Bij 4-3l3MZZWPc in dezelfde keer de miniatuur van de Beeldmaker wisselen (#346, Daan ja #349, blinde test GESLAAGD): `ontwerp/pro-yt-miniatuur/beelden/yt-pro-r2-1280x720.jpg`.

## Nulmeting (28 nov ±06:15 NL, `organisatie/lat/vindbaar/meet.py`, GEZIEN)
- "ball joint blender addon": 4-3l3MZZWPc op plek 15 van 15; m3sNvDOJYQ0 niet in de lijst (de Afkijker zag 14 en 16 van 16 om 00:40).
- "action figure blender": geen van beide in de eerste 16.

## Na het plakken
1. RSS van het kanaal moet beide nieuwe titels geven: `curl -s "https://www.youtube.com/feeds/videos.xml?channel_id=UCTspMNCOwnBkGT2LZ7tB2dg" | grep -o "<title>[^<]*"`.
2. Drie dagen later dezelfde meting, uitslag als reactie in #345.
