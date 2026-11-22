# n8n templates, betaalde workflows

Vera, 9 nov 2026, run 14:31 (Amsterdam), tweede platform van de run. Nagekeken door een controleur: akkoord met 6 correcties, verwerkt.

## Wat het is
n8n is een populair programma om taken te automatiseren (veel AI-agents). De template-bibliotheek (n8n.io/workflows, ook in de app) laat makers workflows delen. Een template kan een prijs en een koop-link hebben; afrekenen gebeurt buiten n8n (Gumroad, Stripe, Payhip). Noor schiftte n8n op 9 nov als nee (geen kassa), maar de betaalde templates waren nog niet gemeten. Waarom het een kans leek: workflows zijn JSON, die kunnen wij bouwen en in een echte n8n testen op Linux.

## Eigen meting (GEZIEN)
- Alle 13.947 templates via de open API (api.n8n.io/api/templates/search, gesorteerd op datum). Data `data/n8n-templates-2026-11-09.json`.
- Nieuwe templates per maand: ±400 tot 500 in jan t/m jun 2026, daarna stijgend naar 1.070 in oktober.
- Betaald: 1.338 templates van 291 makers, mediaanprijs $20. Bijna allemaal uit 2025 (piek juni 2025: 198); in 2026 nog ±40 tot 50 per maand.
- Alle 771 Gumroad-links gelezen (rustig, 4 tegelijk; script `data/gumroad-teller-script.py`, data `data/n8n-gumroad-2026-11-09.jsonl`): 732 bestaan nog, 56 tonen hun verkoopteller (±783 templates wijzen naar Gumroad).
  - **Beste betaalde template ooit: 107 verkopen bij $22** (±$2.350 in totaal, sinds mei 2025). Daarna 83, 82, 75 en 69 verkopen (twee templates delen het product met 83). Geen enkele maker komt in de buurt van $300 per maand.
  - Ratings: 65 van ±780 Gumroad-templates hebben er 1 of meer, 4 hebben er 5 of meer.
  - **Templates van jan t/m jul 2026 (59 met Gumroad): 0 met een rating; de 3 zichtbare tellers staan op 0, 0 en 1 verkoop.** De andere 56 verbergen hun teller, dus de tellers zijn dun bewijs; de 0 ratings en de piek van 107 in anderhalf jaar zijn sterker.
- Views: het zoekadres van de API geeft te lage views; het adres per template (/templates/workflows/<id>, gelijk aan de pagina op n8n.io) geeft de echte. De controleur vroeg 20 willekeurige templates van feb t/m jun 2026 zo op: mediaan ±44 views (7 tot 242). Weinig bereik, maar wel meetbaar. Les: gebruik voor views altijd het adres per template.

## DERDEN
- Makers vragen op het forum zelf waar ze workflows kunnen verkopen, "not the Creator Hub" (community.n8n.io/t/where-can-i-sell-my-n8n-workflow-i-am-looking-for-marketplaces-not-the-creator-hub/212963, via Noor).

## Toets aan wat een 8 is
1. Nieuwe kleine makers verdienen: nee. Nieuwe betaalde templates van 2026 verkopen 0 tot 1 keer.
2. Bereik voor nieuwkomers: zwak, nieuwe templates halen mediaan ±44 views in 4 tot 9 maanden.
3. Bouwen en testen: ja, goed (JSON, n8n draait in Docker).
4. Thijs kan snel verkopen: ja via Gumroad, maar dat is buiten n8n en zonder winkel.

## Cijfer en advies
**Cijfer 2, nee.** Het betaalde deel was een golf in voorjaar 2025 en is uitgedoofd; de beste ooit haalde ±$2.350 in anderhalf jaar. Het geld rond n8n zit bij bureaus en cursussen, niet in templates. Herhaalmeting alleen als n8n een eigen kassa aankondigt.
