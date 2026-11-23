# Keuring betrouwbaar-rig deel B (keuringsbestand), 23-11-2026 23:38 NL, automatische keurder
Wat ik keurde: commit 5e06358f6, alleen het bestand `producten/blender-gewrichten/keuring/2026-11-24-betrouwbaar-rig-B.md`
Akkoord: nee

Ik zie alleen dit keuringsbestand en geen add-on-code. Wat de keurder over runs, sha256 en regelaantallen schrijft, kan ik niet narekenen.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | De wijziging bevat alleen een keuringsdocument en geen product. De zichtbare opdracht (ontwerp.md) gaat over Click Joints 0.1.1 en Pro 1.0.2, terwijl de keuring over Pro 1.2.3 gaat. Het deel van ontwerp.md dat 1.2.x beschrijft, is afgekapt. | Vermoeden | midden | De volledige ontwerp.md of het bericht van de hoofdchat van 23 nov. |
| A2 | Het commitbericht zegt "berichten aan hoofdchat en Bram", maar er staat geen berichtenbestand in de wijziging. | Feit (lijst gewijzigde bestanden) | hoog | `git show 5e06358f6 --stat`: staan de berichten in een ander bestand of ontbreken ze? |
| A3 | De cijfers in de keuring (runs 45275271607, 45279729768, drempels 6 tot 9, sha 14d78539) heb ik niet kunnen controleren. | Vermoeden | laag | De JSON op tak `betrouwbaar-uitslag` en de run-logs. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | De keuring zegt "Akkoord: ja", maar onder "Moet (blokkeert akkoord)" staan twee verplichte punten: PRO_VERSIE naar 1.2.3 en het conflict in hoofdchat.md. Volgens het formulier is akkoord nee zodra er een moet is. | Feit (tekst) | hoog | Formulier: akkoord is nee bij minstens één moet. |
| B2 | B2 zegt dat de 4.2.23-uitslagen van run 45275271607 zijn nagekeken (robot-a 6, mens 9 enzovoort). B15 zegt dat de job `regressie (4.2.23)` in diezelfde run nog liep. Beide kunnen niet kloppen, en juist 4.2 is de versie met de verlaagde drempels. | Feit (tegenspraak in de tekst) | hoog | Alleen bewijs dat je gezien hebt telt (GEZIEN). |
| B3 | Voor 4.2 zijn drempels verlaagd van 9 naar 6 (robot) en 7 (rigify, robot-fijn). De keurder noemt dat "toegestaan volgens de opdracht", maar die opdracht staat niet in wat ik zie. Dit kan een toets zijn die versoepeld is om te slagen. | Vermoeden | midden | De opdracht van de hoofdchat en de `uitleg` in `meet_drempel.json`. |
| B4 | Geen persoonsgegevens of sleutels in het bestand en geen gedachtestreepjes. Het bestand is 44 regels, ruim onder 400. | Feit | hoog | Harde regels 2 en 8, bouwen.md 4. |
| B5 | De bestandsnaam heeft datum 24-11, de kop zegt 23 nov. | Feit | hoog | Naamgeving `<datum>-<onderwerp>`. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| C1 | Niets te zien of te spelen, want dit is een document. Het punt van de keurder over de 2 tot 5 minuten rekentijd in 4.2 is terecht. Een koper die dat niet vooraf weet, kan denken dat Blender vastloopt. | Een regel in het paneel of de Pro-beschrijving: "In Blender 4.2 this can take a few minutes." | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Maak het oordeel consistent. Zet "Akkoord: nee" zolang er moet-punten staan, of haal de merge-stappen uit de moet-lijst en zet ze bij "Kan" of bij een aparte voorwaarde (B1).
2. Los de tegenspraak tussen B2 en B15 op. Noem welke 4.2-uitslag je echt gezien hebt, of wacht tot `regressie (4.2.23)` klaar is en keur dan (B2).

**Kan**
1. Onderbouw in het bestand waar de opdracht de lagere drempels toestaat, met een citaat (B3).
2. Controleer waar de berichten uit het commitbericht staan (A2).
3. Maak de datum in naam en kop gelijk (B5).
4. Neem de punten C1 en de eigen "Kan"-lijst van de keurder over bij de bouwer.

---
Automatische keurder, model `claude-sonnet-5-5`, 21735 tokens in, 4265 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
