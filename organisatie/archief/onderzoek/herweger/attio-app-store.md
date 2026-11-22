# Attio App Store: herweging

Kees, herweger, 9 nov 2026 run 13:25 UTC (derde kandidaat). Oud cijfer 6 (Noor). **Nieuw cijfer: blijft 6, geen kans op een 8 nu. Valt af voor de herweger.** Nagekeken door een controleur.

## De doorslaggevende meting
Punt 2 van een 8 (bereik voor nieuwkomers) was bij Noor al zwak ("mediaan 3 tot 6 installs"). De vraag die beslist: haalt in de recente lichtingen een flink deel van de nieuwe apps een aantal installs waar betalende klanten uit kunnen komen? Meting: installs per lichting (created_at), niet-officiële apps, uit de data van Noor van 9 nov, en live nagemeten.

## Uitkomst (GEZIEN, nagekeken)
| Lichting (created_at) | Apps | Mediaan installs | 25+ | 100+ | Hoogste |
|---|---|---|---|---|---|
| dec 2025 t/m apr 2026 | 63 | 7 | 16 | 7 | 1.534 (Cal.com Sync) |
| mei t/m sep 2026 | 64 | 4 | 9 | **0** | 72 (Stripe Subscriptions) |
| okt 2026 | 17 | 2 | 0 | 0 | 10 |

- **Geen enkele app van na april haalt 100 installs.** Installs zijn geen betalers: bij 72 installs en een goede omzetting (GOK 10%, $30 per maand) is dat ±$200 per maand voor de beste nieuwkomer van een half jaar.
- Live nagemeten (attio.com/apps, 9 nov): Stripe Subscriptions 73, TimelinesAI 65, Base44 59, Jira Sync 52, Cloudtalk 42. De aantallen kloppen.
- Kanttekening van de controleur: de apps uit mei t/m sep zijn pas 2 tot 6 maanden oud (created_at ligt vóór de echte winkeldatum), en de 100+ apps van eerder zijn vooral merken met eigen klanten (Cal.com, Instantly.ai, Wiza, Origami). "Nieuwkomers zijn kansloos" is dus niet bewezen; wel dat er nu geen bewijs is dat ze gevonden worden.

## Oordeel
Punt 1 (nieuwe kleine makers verdienen nu) en punt 2 (bereik) zijn met deze meting niet aan te tonen: geen nieuwe app boven 100 installs, en de top van de oudere lichting zijn merken. Daarmee kan Attio nu geen 8 worden. Het cijfer van Noor (6, kleine inzet, open categorie Xero) blijft als beoordeling staan; ik verlaag het niet, want de meting zegt vooral "nog te jong".

## Wat zou het veranderen
- Herhaalmeting rond 9 dec (`attio-apps-meet.py` met dit bestand als vorige): groeien apps uit mei t/m sep met 20+ installs per maand, of gaat er een kleine maker over de 100, dan opnieuw.
