# Staande opnames Click Joints (Bram, 15 nov 2026 22:35 UTC)

Voor de korte filmpjes van Chris (TikTok, Shorts, Reels; opdracht hoofdchat 15 nov 23:00). Echte Blender 5.3.0 met de betaalde zip 1.0.1, zelfde verloop als demofilm v3, maar op een scherm van 1080 x 1920, zonder zijbalk en met de camera dichter op het gewricht. Lokaal opgenomen (491 beelden), alle vijf delen "FILM OK".

Elk bestand: 1080 x 1920, 30 fps, H.264 (`-preset veryfast`, crf 18), geen geluid, **geen tekst** (onderschriften zet Chris er zelf op). Onder het gewricht is ±40% van het beeld leeg verloop, daar passen de onderschriften en de knoppen van de apps.

| Bestand | Duur | Wat je ziet | Gratis of Pro |
|---|---|---|---|
| `click-joints-staand-1-knie-buigt.mp4` | 2,0 s | knie buigt van 0 naar 115° met de gradenboog (haak) | Pro (scharnier) |
| `click-joints-staand-2-plaatsen.mp4` | 3,3 s | het hele been draait, dan Place hinge: twee delen met groen | Pro |
| `click-joints-staand-3-buigen.mp4` | 4,5 s | de buig van 0 naar 115° en 1 s stil op de stop | Pro |
| `click-joints-staand-4-rood.mp4` | 3,2 s | camera op de stop, 9,5° voorbij: rood en "+9° past limit" | Pro |
| `click-joints-staand-5-kogel.mp4` | 3,3 s | kogel en kom uit elkaar met de groene pasband | gratis (zit ook in Pro) |
| `click-joints-staand-6-proefje-spelingen.mp4` | 13,0 s | voor tip 9 (16 nov): drie staafjes van 10 mm, kogel 5 mm, speling 0,1 / 0,2 / 0,3 mm (gemeten 0,0998 / 0,1996 / 0,2995), uit elkaar, alle drie Good fit. 0 tot 3,0 s alle drie; 3,0 tot 5,5 s links (0,1); 5,5 tot 8,0 s midden (0,2); 8,0 tot 10,5 s rechts (0,3); 10,5 tot 13,0 s terug naar alle drie | gratis 0.1.1 |

`staand-beelden.jpg`: het middelste beeld van elk deel naast elkaar, GEZIEN door mij met Read (rood past nu helemaal in beeld, kogel groot).

Let op: delen 1 tot 4 tonen het scharnier, dat alleen in Pro zit. Zolang Pro niet live is, eerlijk zeggen dat het Pro is ("coming to Superhive") of alleen deel 5 gebruiken voor de gratis versie. De opnames zijn 2 tot 4,5 s; voor een filmpje van 10 tot 20 s zet je er twee of drie achter elkaar (1, 3, 4 is de buig met het rood).

Opnieuw maken of langer: `FILM_STAAND=1` bij `e2e/film_pro.py` op een X-scherm van 1080x1920 en daarna `bash e2e/maak_staand.sh <map> <uit>`; of op GitHub de workflow `click-joints-pro-film.yml` met de keuze "staand" aan. Camera bijstellen kan met `FILM_AFSTAND` (68), `FILM_MIDDEN` (-4,0,14), `FILM_ROOD_AFSTAND` (46) en `FILM_KOGEL_AFSTAND` (45). Wil Chris een ander moment of een langere opname, dan maak ik die.

**Opname 6 (Bram, 16 nov ±05:30 UTC):** `e2e/film_proefje.py` met de gratis zip 0.1.1, lokaal in Blender 5.3.0 op een X-scherm van 1080 x 1920. Geen gradenboog (`toon_bereik` uit), want het gaat om de speling. Eerlijk: het verschil tussen 0,1 en 0,3 mm zie je op dit formaat niet; zet de speling als tekst bij elk staafje (links 0.1, midden 0.2, rechts 0.3 mm). Het hele staafje is groen omdat de add-on bij Good fit het hele deel kleurt. Beelden op 3,0 / 4,2 / 6,7 / 9,2 / 12,3 s: `staand-6-beelden.jpg`, GEZIEN met Read.
