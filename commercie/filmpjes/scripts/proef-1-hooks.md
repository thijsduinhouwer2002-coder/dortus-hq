# Stem-proef 1: twee hook-versies (Sanne, 23 nov 2026)

Opdracht hoofdchat 23 nov ±12:45 NL (recept v3): de proef-Short met stem begint nog zonder echte hook; maak twee versies met een andere hook. Voor de Regisseur en de stem-agent.

## Klaar om te draaien
- `proef-1-hook-a.json` en `proef-1-hook-b.json`: kopie van `commercie/filmpjes/stem/proef-1.json`. Alleen `naam`, `titel` en scène 1 zijn anders; scène 2 tot het eindbeeld zijn byte voor byte gelijk (GEZIEN, diff).
- Draaien: in `.github/workflows/stem-proef.yml` twee regels `montage.py` erbij met deze json's (alleen staand is nodig). Dat bestand is van de stem-agent; ik heb het niet aangeraakt.

## De twee hooks
| | A: probleem | B: oude manier |
|---|---|---|
| gesproken | "Do your printed knees bend too far?" | "Still finding knee problems after printing?" |
| grote tekst (kop) | Knees bend too far? | Knee problems after printing? |
| pil | TOO FAR? (rood) | AFTER THE PRINT? (rood) |
| beeld | knie voorbij de stop met rode boog en "+12° past limit" (deel `knie_rood`, beeld 6 tot 97, met het Bend-kaartje) | zelfde beeld |
| titel | Do your printed knees bend too far? Check in Blender first 🦵 \| Blender | Knee problems after printing? Catch them in Blender first 🦵 \| Blender |

- **Zelfde beeld met opzet:** zo verschilt alleen de zin, en zegt de meting na 48 uur iets over de woorden en niet over het plaatje.
- **Lengte:** 6 woorden, ±1,8 tot 2,2 s bij snelheid 0,95 (GOK, Kokoro haalt ±2,7 woorden per seconde; de workflow meet het echt). Korter dan de oude openingszin (12 woorden), dus de Short blijft onder 60 s. Gaat de hook toch over 1,5 s heen: de grote tekst staat er vanaf beeld 1, dus de vraag is binnen 1,5 s te lezen.
- **Nooit de productnaam vooraan:** klopt, Click Joints Pro valt pas in scène 2.

## Klopt het (tegen de bronnen)
- A: de rode boog voorbij de stop staat in beeld (keuring stem-proef 1: schuif op 132, "+12° past limit", GEZIEN door de Keurder). "Bend too far" is wat het beeld laat zien.
- B: `platformen/blender-2/gumroad-1.1.md`: "What you only find out after the print is that the knee bends backwards ... Click Joints shows all three before you print." Scène 11 ("So you find the problem in Blender, before you print") sluit erop aan.
- Geen belofte over printen: de zin "Measured in Blender, not print tested by us yet. Print a test joint first." blijft staan.

## Meten
Plaatsen met minstens twee dagen ertussen (of A en B op dezelfde dag op TikTok en YouTube, als de Maker dat kan). Na 48 uur in YouTube Studio: weergaven en "bleef kijken" (percentage na de eerste seconden). Uitslag in `commercie/filmpjes/regisseur-log.md`.
