# OpenCart Marketplace (betaalde extensies)

Onderzocht: 7 nov 2026, run 22:33 UTC, door Vera. Controleur akkoord, één correctie verwerkt (commissie).

## Advies: nee. Cijfer 1.

Nieuwe betaalde extensies verkopen bijna niets, de winkel houdt de helft van kleine verkopen, en het aantal winkels op OpenCart krimpt.

## Hoe gemeten
- Elke extensiepagina op opencart.com toont aanmaakdatum, prijs, en een openbare teller: **Sales** bij betaalde en **Downloads** bij gratis extensies. Robots.txt verbiedt alleen /notyours/ en login.
- De ID's lopen op met de datum. Ik haalde alle pagina's 48300 t/m 49599 op (1.300 stuks, 122 zijn een 404). Mei t/m aug 2026 is precies ID 48447 t/m 49537 (nagekeken door de controleur, ook net buiten het bereik).
- Vergelijkingsgroep: ID 47350 t/m 47799, extensies van mei t/m aug 2025 (nu 14 tot 18 maanden oud).
- Scripts en ruwe data: `data/opencart-haal-script.py`, `data/opencart-analyse-script.py`, `data/opencart-2026-05tot08-2026-11-07.jsonl`, `data/opencart-2025-05tot08-2026-11-07.jsonl`.

## Cijfers

### Lichting mei t/m aug 2026 (2 tot 6 maanden oud)
- GEZIEN: 994 nieuwe extensies, 437 betaald, 557 gratis.
- GEZIEN, betaald: mediaan **0 sales**, 88% nul, 12% 1+, 1% 5+, niemand 20+. Top: 16 sales (waldbyte, EU Order Withdrawal Button, $34,99, een EU-regel uit 2026). Daarna 6, 5, 5.
- GEZIEN: alle 437 betaalde samen 92 verkopen, bruto ±$3.128 in 2 tot 6 maanden. Na 50% commissie ±$1.560 voor 121 makers samen.
- GEZIEN: één maker (torevo) zette in juli 170 betaalde producten neer (taalpakketten, $22,90 tot $24,90), samen 19 sales. Zonder hem: 267 betaald, 73 sales, 86% nul, mediaanprijs $29.
- GEZIEN, gratis: mediaan 3 downloads, 27% 10+, 1% 100+ (top 226, een Oekraïense verzendmodule).
- GEZIEN, drukte: ±80 tot 230 nieuwe per maand (juli 568 door de bulk van torevo).

### Lichting mei t/m aug 2025 (14 tot 18 maanden oud)
- GEZIEN: 240 betaald, mediaan nog steeds **0 sales**, 68% nul, 5% 5+, 2% 10+, top 48 (Basic USPS, $34,99). Samen 247 verkopen, ±$8.332 bruto voor 86 makers.
- GEZIEN, gratis: mediaan 34 downloads, 22% 100+. Bereik voor gratis groeit dus wel langzaam, betaald niet.

### Geld
- GEZIEN (controleur, pagina information_id=2): commissie **50% tot $700 maandomzet**, 40% tot $849, 30% tot $999, 25% daarboven, gerekend over de laatste 6 maanden. Uitbetaling via PayPal of Payoneer, maandelijks.
- GEZIEN: oude toppers verkopen ±100 stuks per jaar (GeekoDev PDF Invoice Pro, $59, sinds 2013: 1.645 sales). Zelfs de beste maker in de winkel haalt hier dus maar een paar honderd dollar per maand per product.
- Kanttekening: makers mogen ook op hun eigen site verkopen; die verkoop zit niet in de teller. Daar is geen cijfer van.

### Markt
- DERDEN (storeleads.app): 151.391 live OpenCart-winkels, -15% jaar op jaar (2026 Q3), piek ±224.500 in 2024 Q1.

## Voor en tegen
- Voor: openbare verkoopteller (eerlijke meting), betaling via de winkel, weinig drukte vergeleken met Shopify.
- Tegen: mediaan 0 verkopen, ook na anderhalf jaar; 50% commissie voor kleine makers; krimpende markt; veel klanten zijn ontwikkelaars die zelf bouwen of gratis zoeken; veel nieuwe producten lijken bulk of AI-gemaakt.

## Wat we zouden bouwen
Niets. Het enige signaal is dat een EU-regel (herroepingsknop 2026) de beste nieuwe extensie gaf, en dat waren 16 verkopen. Dat past bij wat we op Shopify zagen: alleen bij een nieuwe regel, en dan nog klein.

## Wat dit zou veranderen
Een nieuwe EU-regel met harde datum waarbij OpenCart-extensies honderden verkopen halen. Herhaalmeting kan met de scripts hierboven (ID-bereik per maand opzoeken via de probe met stap 300).
