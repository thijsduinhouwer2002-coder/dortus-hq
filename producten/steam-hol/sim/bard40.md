# Toets: eerste bard vast als 40e held (Bram, 19 nov 2026, voor Sanne)

Vraag Sanne 18 nov 21:00: wat doet het langste gat zonder iets nieuws in minuut 0 tot 30 als de 40e held altijd een bard is? Lat: hooguit 5 min bij 4 van 5 zaden, het lied telt als nieuw.

**Hoe gemeten (GEZIEN, lokaal):** Godot 4.3 Linux, `--headless --fixed-fps 15`, `duur=1800 vers=1 zaad=1..10`, 10 zaden voor en na (tak `claude/steam-hol-bard-40`). Geen Windows-run: zo duurt 30 min spel 4 s. Controle: zaad 1 zonder bard geeft niveau 5 op 19,9 en niveau 6 op 28,1 min, net als Sannes Windows-run (20,7 tot 27,7). Meetscript: `python3 sim/gat_uit_log.py <logs>`.
- **smal** = nieuw is een nieuw hol-niveau of een lied.
- **breed** = ook de eerste koop en de eerste keer van elke soort, trek, terugkomer of aartsvijand.

| zaad | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | mediaan | ≤5 min |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| smal, zonder | 8,2 | 8,3 | 7,5 | 8,7 | 8,7 | 5,8 | 13,1 | 10,4 | 11,0 | 10,7 | 8,7 | 0 van 10 |
| smal, bard 40 | 5,9 | 8,2 | 9,9 | 8,7 | 8,0 | 6,7 | 5,8 | 6,3 | 6,7 | 9,0 | 7,4 | 0 van 10 |
| breed, zonder | 7,2 | 8,2 | 7,5 | 8,7 | 8,7 | 12,2 | 9,5 | 10,4 | 9,8 | 10,7 | 9,2 | 0 van 10 |
| breed, bard 40 | 7,4 | 8,2 | 9,9 | 7,1 | 8,4 | 9,1 | 9,6 | 6,3 | 10,6 | 9,0 | 8,7 | 0 van 10 |

**Uitkomst:** de bard op 40 (±18,5 min, 61 tot 65 helden in 30 min) helpt een beetje (smal 8,7 naar 7,4 min mediaan) maar haalt de lat bij geen enkel zaad. Waarom: hij zingt alleen als hij ontsnapt (±1 op 3), en waar hij het gat breekt schuift het langste gat naar een ander stuk (vaak 20 tot 30 min, tussen niveau 5 en 6).
**Advies:** zo niet naar main. Het gat zit tussen hol-niveau 5 (±19 min) en 6 (±28 min); er is iets nieuws nodig dat vast rond minuut 23 tot 25 valt, los van geluk. Keuze aan Sanne (balans).
