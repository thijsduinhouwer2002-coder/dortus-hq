# Keuring betrouwbaar-rig (keuringsbestand deel B), 23-11-2026, automatische keurder
Wat ik keurde: commit 58e05a361, alleen het bestand `producten/blender-gewrichten/keuring/2026-11-23-betrouwbaar-rig-deel-B.md`. De tak `claude/betrouwbaar-rig` en zijn code zitten niet in deze wijziging en heb ik dus niet beoordeeld.
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | De wijziging voegt alleen een keuringsbestand toe. De add-on, het ontwerp en de beloofde functies (Click Joints 0.1.1 en Pro 1.0.2) veranderen niet. | feit | hoog | De lijst met gewijzigde bestanden bevat één markdown-bestand. |
| A2 | Het bestand volgt het formulier: kop, "Wat ik keurde", "Akkoord: nee" voor de tak, daarna deel A, B, C en de moet/kan-lijst. De drie moet-punten komen overeen met de bevindingen B1 tot B6. | feit | hoog | Het bestand zelf. |
| A3 | De inhoud van de bevindingen (runnummers, 2 gewrichten in 4.2 op de nieuwe robot, de kloppende splitsing in `herstel.py`) kan ik uit deze tekst niet nagaan. Ik neem ze over als de claim van de andere keurder. | vermoeden | midden | Run 45266165562 in het GitHub-log en de JSON's op de tak `betrouwbaar-uitslag` zouden ze bevestigen of weerleggen. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Er is geen test aangepast of weggehaald, want er is alleen een nieuw bestand. | feit | hoog | tests niet aangepast om te slagen |
| B2 | Het bestand is 43 regels, ruim onder ±400. | feit | hoog | bestandsgrootte |
| B3 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in. Het noemt alleen `github.token` van Actions als naam, zonder waarde. | feit | hoog | geen persoonsgegevens |
| B4 | De cijfers in het bestand hebben runnummers, en onzekere punten zijn als vermoeden gemarkeerd (B11, B17). Het bestand is eerlijk over wat niet gezien is, zoals B13 (4.5 niet gemeten). | feit | hoog | GEZIEN/DERDEN/GOK |
| B5 | `architectuur.md` hoort bij code en niet bij een keuringsbestand, dus niets bij te werken. Wel noemt de keuring zelf een afwijking in `architectuur.md` van de tak (B12). | feit | hoog | architectuur.md bijgewerkt |
| B6 | Het keuringsbestand is een momentopname: sommige runs "liepen nog toen ik keek" (B5 van het bestand). Dat is geen fout, maar het oordeel op die punten kan inmiddels verouderd zijn. | feit | midden | eerlijk, verzin niets |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| C1 | Er is niets te zien of te spelen in deze wijziging. De keuring noemt zelf de zeven bijna gelijke "Skipped"-zinnen op de robot in 4.2. Dat is een goede opmerking voor de koper. | Eén korte zin bovenaan en per gewricht alleen de plek, zoals de keuring voorstelt. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Dit akkoord geldt alleen voor het keuringsbestand en niet voor de tak. Volgens dat bestand blijft de tak op "nee" staan tot de drie moet-punten uit de keuring zijn opgelost: 4.2 opnieuw meten op de nieuwe robot, e2e en rig-toetsen groen op de laatste commit, en het conflict in `berichten/hoofdchat.md`. Wie de tak wil samenvoegen, moet die punten oplossen en niet op het groene vinkje van deze commit vertrouwen.
2. Vul in een volgend keuringsbestand deel A in als tabel of schrijf "niet gekeurd, zie keuring A", zodat het formulier compleet blijft.
3. Zet bij punten waar runs nog liepen de tijd van kijken erbij, zodat een lezer ziet hoe oud het oordeel is.

---
Automatische keurder, model `claude-sonnet-5-5`, 21998 tokens in, 2853 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
