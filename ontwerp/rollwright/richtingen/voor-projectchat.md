# Voor de projectchat: drie richtingen voor de betaalde skins (Daan, 9 nov 2026)

Opdracht: bericht Thijs 8 nov 22:58. Eerst naar de projectchat (poortwachter), daarna op de lijst van Thijs.

Alle plaatjes zijn 16:9 (1400 x 788) uit de echte Obsidian met de echte Rollwright 0.3.2 en echte worpen (run 42542400186, tak `ontwerp/rollwright-richtingen`, spec `e2e/ontwerp/richtingen.e2e.mjs`). De skins zelf zijn nog prototype-CSS (`e2e/ontwerp/richtingen/maak.py`), dus dit is een ontwerp, nog geen gebouwde skin. Zelfde notitie in alle drie, zodat je eerlijk kunt vergelijken: initiatief, de wolf (NAT 20), de val (NAT 1), schade en Perception.

| Richting | Bovenaan | Iets lager (wolf en val) |
|---|---|---|
| A. De Taverne: eikenhout, messing munt, kaarslicht | [taverne-1.png](https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/main/ontwerp/rollwright/richtingen/taverne-1.png) | [taverne-2.png](https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/main/ontwerp/rollwright/richtingen/taverne-2.png) |
| B. De Kerker: steen, gebeitelde Uncial-letters, sintels | [kerker-1.png](https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/main/ontwerp/rollwright/richtingen/kerker-1.png) | [kerker-2.png](https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/main/ontwerp/rollwright/richtingen/kerker-2.png) |
| C. De Hofcodex: velijn, fraktur, lapis, vermiljoen, bladgoud | [codex-1.png](https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/main/ontwerp/rollwright/richtingen/codex-1.png) | [codex-2.png](https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/main/ontwerp/rollwright/richtingen/codex-2.png) |

Wat per richting anders is: achtergrond, letter, kleuren, vorm van het token, NAT 20 en NAT 1, Roll log en de kleur van de wolf en de val. Uitleg en tabel: `producten/obsidian-rollwright/ontwerp-skins-richtingen.md`.

**Beeld bij de worp** is een optie die de gebruiker zelf kiest (`|icon(wolf)` of een lijstje woord naar icoon), niet geraden. Iconen van game-icons.net (CC BY 3.0). In de plaatjes: klein in het token, groot in de callout.

**Mijn keuze:** C zeker (de enige lichte wereld, het meest eigen). Voor de tweede twijfel ik tussen A en B; de controleur vindt A het braafst en raadt B aan, en ik neig daar ook naar. Thijs kiest.

**Eerlijk:** de achtergrond van de notitie hoort bij de skin alleen als de gebruiker dat aanzet (schakelaar of `cssclasses`), want een plugin verft niet ongevraagd je notities. Zonder schakelaar: token, Roll log en iconen in de wereld van de skin.

Controleur (agent): eerst nee met vijf kleine moet-punten (fraktur te klein, tab, barst door de tekst, twee beweringen die niet te zien waren); alles verwerkt en opnieuw bekeken.
