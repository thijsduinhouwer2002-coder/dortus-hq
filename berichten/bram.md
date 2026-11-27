# Berichten voor bram

Oudere berichten staan in `berichten/archief/bram-t-m-2026-11-24.md` en `berichten/archief/bram-25-t-m-26-nov-2026.md` (zoek met grep). Hieronder alleen de recente; de nieuwste staat onderaan.

- 27 nov ±05:00 NL (van Daan): #246 YouTube-beschrijvingen ja (8), klaar om te plakken. Kan (geen nakeuring): in de saleversie van de Shorts de tweede regel "Type dortus.com/yt" weg; in 65JiRlDupNc de saleregel direct na de eerste zin.

## 28 nov 2026 ±00:10 NL, van de automatische keurder: blender-gewrichten akkoord nee
Keuring van 7de51b8..086354d: `platformen/blender/keuring/2026-11-28-auto-blender-gewrichten-086354d.md`. Moet en kan: **Moet** 1. Laat een groene e2e-run zien met `toetsen_tenen.py` erin, op 4.2.23 en 5.x, plus de bestaande Pro-toetsen (army_man, Rigify, Meshy-knight). Zonder dat is niet bewezen dat de teenfout weg is en dat `buiten == 0` Pro niet raakt (A2, A3, B1). 2. Maak duidelijk welke workflow `toetsen_tenen.py` start en hoe het Human Base Meshes-bestand binnenkomt. Als dat niet gebeurt, draait de test nooit (B1). **Kan** 1. Zet in de test een logregel waaruit blijkt dat bij Exact het samensmelten van de ogen echt voorkomt, om de versoepeling te onderbouwen (B2). 2. `h_pogingen` heeft nu 5 in plaats van Los elk moet-punt op en push opnieuw; de keurder kijkt dan weer. Hij leest alleen tekst, dus beeld en speelplezier blijven bij Daan en Iris.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 28 nov 2026 ±00:15 NL, van de automatische keurder: blender-gewrichten akkoord ja
Keuring van 086354d..f893c68: `platformen/blender/keuring/2026-11-28-auto-blender-gewrichten-f893c68.md`. Moet en kan: **Moet:** geen. **Kan:** - Zet het gemeten verlies uit de eerste groene run in de commit of in `ontwerp.md`. Dan is de grens van 6% onderbouwd (A2). - Controleer in het log dat `lid` bestaat en dat `vol0` klopt. Laat de toets anders vooraf een waarschuwing geven als het figuur open randen heeft (A3, B5). Hij leest alleen tekst, dus beeld en speelplezier blijven bij Daan en Iris.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
