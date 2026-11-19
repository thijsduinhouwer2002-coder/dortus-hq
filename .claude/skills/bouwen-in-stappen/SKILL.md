---
name: bouwen-in-stappen
description: Gebruik dit bij elke nieuwe functie of elk nieuw product dat meer dan een paar regels code raakt (spel, add-on, horloge-app, site). Zeven stappen van begrijpen tot keuren, zodat het in één keer goed is.
---

# Bouwen in zeven stappen

Doel: geen half werk en geen "deels verwerkt". Elke stap levert iets op dat je kunt laten zien.

1. **Begrijpen.** Schrijf in twee zinnen wat er gebouwd wordt en voor wie. Wat is "af"? Maak het toetsbaar (bijvoorbeeld: "de held valt binnen 40 s", "de test X slaagt").
2. **Code verkennen.** Lees eerst hoe het nu werkt: de bestanden die je gaat raken, één vergelijkbare functie die er al is, de tests. Noem de 3 tot 5 belangrijkste bestanden met regelnummers. Bouw verder op wat er is, niet ernaast.
3. **Open vragen.** Schrijf op wat onduidelijk is (randgevallen, wat bij een fout, wat het niet doet). Beantwoord ze zelf met een reden uit `organisatie/besluiten.md`, de kennisbank of je rolinstructie. Alleen geld gaat naar Thijs.
4. **Ontwerp met keuze.** Schets 2 of 3 aanpakken (klein en snel, netjes, of een middenweg), met voor- en nadeel. Kies er één en schrijf waarom in `producten/<naam>/ontwerp.md`. De keurder (skill `keuren`) kijkt mee vóór je bouwt.
5. **Bouwen.** Volg het ontwerp en de stijl van de bestaande code. Kleine stappen, na elke stap testen.
6. **Keuren door een ander.** Laat een aparte agent (die het werk niet maakte) kijken naar: fouten, wat breekt bij rare invoer, en of het past bij het ontwerp en de eisen van stap 1. Hij geeft per punt hoe zeker hij is (hoog, midden, laag). Los alles met "hoog" op. Bij spelwerk keurt Iris daarna op plezier en beeld.
7. **Samenvatten.** In je logboek: wat er gebouwd is, welke keuzes, wat getest is en hoe, wat nog open staat. Met bewijs (testuitslag, schermafbeelding, meting), niet "zou moeten werken".

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
