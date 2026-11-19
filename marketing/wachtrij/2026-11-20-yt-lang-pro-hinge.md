# Click Joints Pro: de click hinge die stopt (lange YouTube-video 1)

- status: open
- kanaal: yt-lang
- soort: video
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/youtube-pro-1/click-joints-pro-uitleg-2-geluid.mp4
- geluid_check: volgt uit run 44519478563 (workflow `youtube-pro-1.yml`, stap "In elkaar zetten met geluid"); proef op nepbeelden 19 nov 11:49 UTC: GOED (gemiddeld -16,6 dB, piek -1,3 dB, -14,3 LUFS)
- lengte: ±2:00 tot 2:07 (GOK; de echte staat na de run in `metingen.json` in de release), liggend 1920x1080
- tijd: 2026-11-20T17:00:00+01:00
- doel: https://dortus.com/yt/
- gemaakt_door: Chris
- vorige: (eerste versie in het oude formaat: `commercie/wachtrij/youtube-pro-1.md`)

Let op voor de Keurder: keur alleen `click-joints-pro-uitleg-2-geluid.mp4`. Geeft die URL nog geen 200, dan draait de opname nog (klaar ±12:45 UTC 19 nov). `uitleg-1` is de versie die Daan afkeurde. Daan keurt alleen zijn drie moet-punten na; zijn akkoord komt onder Bronnen.

## Titel
Blender hinge for 3D printing that stops at 115° | Click Joints Pro

## Tekst
```
https://dortus.com/yt/

We make Click Joints, a Blender add-on that cuts a part into print-ready joints. This video shows the hinge from Click Joints Pro: pick an end stop of 90°, 115° or 135°, click Place hinge, and drag Bend to see how far it goes. Push past the stop and the arc turns red and shows how far you went, so you see the limit before you print.

Measured in Blender, not printed yet. Recorded in Blender 5.3 with the add-on itself; the colours and the arc come from the add-on.

[HOOFDSTUKKEN uit hoofdstukken.txt in de release youtube-pro-1]

Also in Pro: ball joints with the green fit band, Exploded view, export as STL or 3MF.
There is a free version with ball joints on extensions.blender.org (search "Click Joints").

#blender #3dprinting #b3d
```
Let op: de regel met HOOFDSTUKKEN is een plek om in te vullen, geen tekst voor YouTube. Chris of de Maker vervangt hem door de inhoud van `hoofdstukken.txt` voor het inplannen.

## Eerste reactie
```
Get Click Joints Pro, with the hinge that stops at 90°, 115° or 135°: https://dortus.com/yt/
```

## Bronnen
- Standen 90, 115 en 135 en de rode boog voorbij de stop: gemeten door de add-on in de opname (`metingen.json`, run 44493861163: 89,96 / 114,96 / 135,04 graden, rood 7 vlakken voorbij elke stop, 0 na terug), GEZIEN.
- "the arc turns red and shows how far you went": keuring Daan moet 1 (alleen de boog wordt rood in beeld, niet de vlakken).
- Ball joints, fit band, Exploded view, STL en 3MF in Pro: `producten/blender-gewrichten/` en dortus.com/yt/ (GEZIEN 19 nov 11:50 UTC, geeft 200).
- Gratis versie op extensions.blender.org: winkelpagina Click Joints (eerdere metingen in `commercie/blender-click-joints/`).
- Keuring Daan versie 1: `platformen/blender/keuring/2026-11-19-youtube-pro-1-daan.md`, akkoord nee, 3 moet. Verwerkt in commit ac0dbb7: (1) zin over rood in video en tekst aangepast, (2) "Back inside the range" pas vanaf 2,1 s in dat deel (na de beweging terug, het rood is dan gemeten weg), (3) geen stilstaande titel meer: de video opent met de buig naar de stop met titel en "90° · 115° · 135°" erover, het stilstaande been van 9 naar 3 s. Kan 3 ook: geluid naar -14 LUFS.
- Herkeuring Daan versie 2: (volgt)

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
