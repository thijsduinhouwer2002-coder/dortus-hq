# Groeimeting aanraadlijsten, 9 nov 2026 (Jet)

Vraag: bij welke bestandssoorten gaat veel van de dagelijkse groei naar kapotte of zwakke plugins, terwijl er ook een betaalde plugin verkoopt? Dat zou een gat zijn voor een tweede product.

## Hoe gemeten
- Zelfde lijst als de nulmeting: 302 bestandssoorten uit `bestandssoorten-stap1-2026-11-06.tsv` (kolom `soort`; de taak noemde `aanraden-per-bestandssoort-2026-11-06.tsv`, maar die heeft geen kolom `soort` en gaf een fout). Per soort de aanraadlijst van de Marketplace (`/feature/getImplementations?featureType=com.intellij.fileTypeFactory`), per plugin de teller `downloads`.
- Nulmeting 8 nov 14:15 UTC (`aanraden-nulmeting-2026-11-08.tsv`), nu 9 nov 14:56 UTC (`aanraden-2026-11-09.tsv`), 302 soorten opgevraagd, 245 met minstens één plugin (de andere 57 hebben een lege aanraadlijst en staan niet in de tsv), 475 plugins in beide metingen. Er zit 24 uur en 41 minuten tussen; de tellers verversen één keer per dag, dus dit is één verversing, ongeveer een dag groei. Gecontroleerd dat de teller ververst was: Archive Browser 340.343 naar 340.381 (GEZIEN).
- Groei per plugin: `aanraden-groei-plugins-2026-11-09.tsv`, per soort: `aanraden-groei-soorten-2026-11-09.tsv` (script `aanraden-groei-2026-11-09.py`). Voor de 136 plugins met 30 of meer groei: maker, prijsmodel, laatste versie en datum in `aanraden-groei-verrijkt-2026-11-09.tsv` (script `aanraden-groei-verrijk-2026-11-09.py`). 9 plugins hadden geen vergelijking (nieuw of zonder teller).

## Wat ik zag (alles GEZIEN, één dag)
1. De grote groei gaat naar plugins van JetBrains zelf (Docker, Vue.js, .env files, HTTP Client, Markdown) of naar sterke gratis plugins die bijgehouden worden (CSV Editor +12.622, Unit File Support +3.301, AsciiDoc +1.942, Minecraft Development +1.347).
2. **Batch (`*.bat`, `*.cmd`) is de enige soort waar veel groei naar verlaten plugins gaat:** CMD Support (laatste versie maart 2015) +219 en Batch Scripts Support (december 2021) +248, samen 467 per dag. Daarnaast BatchCraft (betaald) +212. Bij alle andere soorten met meer dan 200 groei per dag gaat de groei naar plugins die in 2025 of 2026 nog een versie kregen. Rainbow CSV (mei 2022) krijgt +68, maar CSV Editor neemt daar de groei (+12.622).
3. Betaalde plugins in een aanraadlijst groeien wel: BashSupport Pro +310 (`*.sh`), BatchCraft +212, Nginx Configuration Pro +142 (`*.conf`), Jenkinsfile +95, Elasticsearch +92, Flexible Swift +74, Databee +52, Mermaid Studio +49, en freemium Noctule +265 en Mermaid Studio Core +158. Dat steunt het idee dat in de aanraadlijst staan telt, ook voor betaalde plugins. Downloads van een betaalde plugin zijn installaties met proef, geen verkopen.
4. BatchCraft: nog steeds 0 reviews en geen stemmen (`/rating`: votes leeg). Rechtzetting op `batch-afweging-2026-11-08.md`: daar staat "gemiddelde 4,06 uit 2 stemmen", maar `meanVotes` en `meanRating` zijn een algemeen gemiddelde van de Marketplace (zelfde waarde bij elke plugin), geen echte stemmen. CMD Support: laatste reviews "Does not work" (2025, 2025, 2024). Batch Scripts Support: "looks abandoned" (2025).
5. Onze eigen plugin staat nog niet in de aanraadlijst voor `*.y` (nu GoYacc Support en Bison Language Support) of `*.l` (leeg), want hij is nog verborgen. In `plugin.xml` meldt hij `y;yy` en `l;ll` aan.

## Conclusie
**Geen voorstel naar Hans.** De meting bevestigt dat Batch het enige duidelijke gat is in de aanraadlijsten (467 per dag naar plugins van 2015 en 2021), maar dat was al bekend in `batch-afweging-2026-11-08.md`. Wat daar het besluit zou veranderen (reviews of zichtbare verkoop bij BatchCraft, of verzoeken om een Batch-debugger) is er niet: BatchCraft heeft nog 0 reviews. Volgens regel 0b geen nieuw besluit zonder nieuw feit.

**Wel bruikbaar:**
- Voor Bison & Flex: na de goedkeuring en het zichtbaar maken nakijken of 35901 in de aanraadlijst van `*.y` en `*.l` verschijnt. Punt 3 laat zien dat dit de belangrijkste weg naar installs is.
- Voor de weekmeting van 15 nov: dezelfde scripts nog eens draaien (en dan ook de soorten met een lege lijst wegschrijven), dan is er groei over 7 dagen naast deze ene dag, en kijken of BatchCraft dan reviews of een nieuwe versie heeft.

## Nagekeken
Controleur 9 nov 15:08 UTC: akkoord ja, geen moet-punten; alle getallen met een eigen script nagerekend, steekproef live gelijk. Kan-punten (aantal soorten, rechtzetting stemmen, "één verversing", freemium-groeiers) verwerkt.
