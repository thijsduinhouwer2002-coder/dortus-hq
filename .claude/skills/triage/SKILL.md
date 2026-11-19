---
name: triage
description: Gebruik dit als er meldingen, reviews of vragen van gebruikers binnenkomen (issues in een loket-repo zoals bison-flex of click-joints, winkelreviews, Discord, mail via de hoofdchat). Sorteren, antwoorden klaarzetten, en de juiste eigenaar aan het werk zetten.
---

# Meldingen sorteren

Afgekeken bij GitLens (`triage`, `prioritize`) en meanmail.dev (reactietijd openbaar in de README: snel antwoorden is marketing).

1. **Verzamelen:** nieuwe issues in de loket-repo's (GitHub-zoek-API of `git clone`), reviews in de winkels (winkel-API's), en wat de hoofdchat doorgeeft.
2. **Per melding één regel** in `platformen/<platform>/meldingen.md`: datum, bron, link, soort (bug, wens, vraag, lof), ernst (blokkeert, hindert, klein), en of we het kunnen nadoen.
3. **Bug die blokkeert:** bericht onderaan in `berichten/<eigenaar>.md` met de stappen om het na te doen; dit gaat voor ander werk.
4. **Antwoord klaarzetten:** kort, vriendelijk, menselijk, in de taal van de melder, met wat we doen en wanneer. Antwoorden plaatsen doet de hoofdchat (harde regel 4); Roep reageert niet op mensen, en op TikTok en YouTube plaatst alleen de Maker van Roep.
5. **Doel: binnen 24 uur een eerste antwoord.** Meet de reactietijd per week in `organisatie/scorebord.md`.

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
