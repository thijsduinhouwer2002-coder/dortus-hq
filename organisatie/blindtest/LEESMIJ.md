# Blinde test door Gemini en ChatGPT (besluit Thijs 24 nov 2026 20:19)

Waarom: Claude die Claude keurt ziet dezelfde dingen niet. Twee andere modellen beoordelen ons beeld **blind**: tussen 3 concurrenten, zonder namen, in wisselende volgorde, met de vraag welke ze als klant het eerst zouden kopen. "Is dit mooi?" vragen we nooit: daar zegt elk model ja op.

**Regel:** een nieuw hoofdbeeld, omslag of thumbnail gaat pas live als het bij beide rechters gemiddeld op plek 2 of beter staat. Niet geslaagd: terug naar de maker met de zinnen "Over ons" en "Beter maken" uit de uitslag.

**Hoe:**
1. Maak of kopieer een set in `sets/<naam>.json`: `titel`, `rol` (wie de klant is, in het Engels), `ons` (een of meer kandidaten met openbare url) en precies 3 `concurrenten` (hun hoofdbeeld, openbare url; de beste in die winkel, zie `organisatie/lat/`).
2. Push: de workflow `blindtest.yml` draait vanzelf voor gewijzigde sets. Of start hem met de setnaam (skill `actions`).
3. Uitslag in `uitslag/<set>-<datum>.md` en in de samenvatting van de run.

Kosten: een paar cent per run (GOK). Sleutels staan als GitHub-geheimen, nooit in de repo. Agents draaien deze test zelf; Thijs kijkt alleen naar wat geslaagd is.
