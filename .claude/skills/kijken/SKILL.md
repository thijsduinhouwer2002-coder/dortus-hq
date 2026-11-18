---
name: kijken
description: Gebruik dit na elke wijziging die je kunt zien (spel, add-on, winkelbeeld, site, README, filmpje) voordat je "klaar" meldt. Kijken met eigen ogen, niet de code lezen.
---

# Kijken voordat je klaar meldt

Afgekeken bij OpenStatus (skill `screenshot`: verplicht na elke zichtbare wijziging, desktop en mobiel) en PostHog ("zichtwerk bevestig je niet door de code te lezen").

1. **Maak het beeld** waar de gebruiker het ziet:
   - Hats: de keurfilm of losse beelden uit de Windows- of Linux-build in Actions (`steam-hol*.yml`), op het echte formaat (strook van 160 px en ingezoomd).
   - Blender: de render uit de e2e-workflow; Garmin: de simulatorbeelden; JetBrains: de schermen uit de IDE-test.
   - Site of README: de pagina zoals hij live staat (`curl` voor de tekst; voor het beeld de schermen op de tak `schermen` of een render).
2. **Bekijk het echt met de Read-tool.** Klein formaat én groot. Vergelijk met het vorige beeld of met de toppers als die er zijn.
3. **Schrijf op wat je zag**, met het pad van het beeld: wat goed is, wat raar is (overlap, afgesneden, onleesbaar, verkeerde prijs of tekst).
4. Klopt iets niet: eerst herstellen, dan opnieuw kijken. Pas dan "klaar", met het beeld als bewijs in je logboek.

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
