---
name: update-tekst
description: Gebruik dit als er een nieuwe versie uitkomt of je een changelog, "wat is nieuw", winkeltekst of post over een update schrijft. Maakt uit de wijzigingen een concept in onze eigen stijl.
---

# Van wijzigingen naar tekst

Afgekeken bij tldraw (elke week een concept voor marketing uit de commits, "a draft for a human to edit", stijl overnemen uit eerdere teksten) en CAD Sketcher (één changelog voedt release, winkel en "wat is nieuw").

1. **Verzamel wat er veranderd is** sinds de vorige versie: `git log --oneline <vorige-tag>..HEAD -- producten/<naam>/` en de keuringen van die periode. Alleen wat de gebruiker merkt telt; interne opruimklussen noem je niet.
2. **Schrijf eerst de `CHANGELOG.md`** van het product: een kop met versie en datum, daaronder hooguit 5 regels, elk één zin vanuit de gebruiker ("Sneller laden bij grote bestanden", niet "refactor loader"). Nieuw, Beter, Opgelost.
3. **Maak daaruit drie lengtes:**
   - winkel "wat is nieuw": de changelogregels, binnen de tekenlimiet van de winkel (Blender extensions 1024 tekens);
   - korte post (2 tot 4 zinnen plus beeld of GIF);
   - Steam-aankondiging voor Hats: kop, 3 regels, beeld, en altijd "wishlist en follow".
4. **Stijl:** neem de toon over uit de vorige twee teksten van dit product. Niets verzinnen: elke claim moet in de build zitten en getest zijn. Geen "AI-zinnen" (geen "game changer", geen uitroeptekens achter elkaar, geen emoji-rijen). Geen gedachtestreepjes.
5. **Status:** alles is **CONCEPT**. Spelerstekst van Hats en alles onder de naam van Thijs gaat naar `platformen/steam/teksten-thijs.md` of naar de hoofdchat; Thijs maakt het af. Een changelog en winkel-"wat is nieuw" van onze tools mag de hoofdchat na een keuring zelf plaatsen.
