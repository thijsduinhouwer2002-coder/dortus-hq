# Tiendanube / Nuvemshop App Store

Onderzocht door Noor op 9 nov 2026, run 07:40 UTC. Cijfer **4**, advies **nee voor de pionier, doorgeven aan Vera**.

Nuvemshop (in Spaanstalige landen Tiendanube) is de grootste winkelbouwer van Latijns-Amerika, een soort Shopify voor Brazilië en Argentinië. Partners zetten apps in de "Loja de aplicativos". Ik keek of dit een hard groeiend platform is met een winkel waar nog plek is aan de top.

## De vijf vragen

**1. Groeit het platform hard? Ja.**
- Storeleads: 124.943 live winkels in Q4 2024, 171.918 in Q4 2025, 208.292 nu (GEZIEN, https://storeleads.app/reports/tiendanube). Dat is +67% in zeven kwartalen, en elk kwartaal stijgt het nog. Brazilië 126.717, Argentinië 58.939, Mexico 6.912, Colombia 2.327, Chili 1.843 (GEZIEN, zelfde pagina).
- Winkeliers verkochten in 2025 voor R$6,5 miljard in Brazilië, +35% op een jaar (DERDEN, https://exame.com/negocios/com-r-65-bilhoes-em-vendas-nuvemshop-aposta-em-ia-e-mira-novo-publico/). Series E van $500 miljoen in 2021 (DERDEN, https://www.insightpartners.com/?p=6799).
- Van alle winkelbouwers die ik bekeek groeit deze het hardst in aantal winkels (SHOPLINE vlak, Salla vlak, YouCan krimpt: 70.089 naar 35.846, Jumpseller 8.272 en vlak; GEZIEN, storeleads.app).

**2. Is de winkel jong? Nee.**
- Eigen telling van alle categoriepagina's op 9 nov 2026: 647 unieke apps van 394 makers (GEZIEN, `data/nuvemshop-apps-2026-11-09.json`, scripts `data/nuvemshop-apps-lijst.py` en `data/nuvemshop-apps-details.py`). De site zelf zegt "mais de 700".
- Samen 25.583 reviews; mediaan 3 per app; 206 apps met 10+ en 57 met 100+ reviews (GEZIEN).
- Datums per app staan niet op de pagina's; groei van de winkel zelf kon ik niet meten. Herhaalmeting met dezelfde scripts laat over drie maanden zien hoeveel apps erbij komen.

**3. Kan er betaald worden? Ja, nu al, maar voor ons met omwegen.**
- 491 van de 647 apps staan op "Compras no app", 57 gratis (GEZIEN). Twee routes: zelf afrekenen, of Nuvemshop rekent af (eenmalig of per maand, Billing API versie 2025-03) en houdt een "comissão da plataforma" plus betaalkosten en belasting op de nota fiscal in (GEZIEN, https://atendimento.nuvemshop.com.br/pt_BR/parceiros-tecnologicos/como-eu-recebo-pelo-uso-do-meu-aplicativo-criado-na-nuvemshop, bijgewerkt 15 jan 2026). Het percentage staat nergens openbaar.
- Uitbetaling via Nuvemshop vraagt in Argentinië een Argentijnse factuur en inschrijving bij AFIP (GEZIEN via hulpagent, https://ayuda.tiendanube.com/es_AR/socios-tecnologicos/preguntas-frecuentes-sobre-el-programa-de-socios-tecnologicos). Voor een Nederlandse bv blijft zelf afrekenen over (GOK). Toch kan het: de Duitse TopSoft UG heeft hier 12 apps (GEZIEN), net als 30 in Salla.
- Prijzen liggen hoog genoeg: Lily Reviews R$59 tot R$549 per maand met 412 reviews (GEZIEN, https://www.nuvemshop.com.br/loja-aplicativos-nuvem/lily-reviews).

**4. Is er vraag? Ja, en die wordt al bediend.** Grootste apps naar reviews: Dropi 4.474 en Drop Nacional 1.648 (beide Empreender), WhatsApp-marketing 1.008, JivoChat 729, Hubnoov 673, Manda Bem 634, Melhor Envio 572 (GEZIEN). Klachten gaan over "functies die standaard zouden moeten zijn kosten geld" (DERDEN, Reclame Aqui via hulpagent), dus winkeliers zijn prijsgevoelig.

**5. Is de eerste plek te pakken? In de grote hoeken niet.** Vijf makers hebben 52% van alle reviews; Empreender alleen al 9.103 (GEZIEN). Nuvemshop pakt zelf betalen (Nuvem Pago, 60%+ van het betaalvolume), verzenden, chat en e-mailmarketing (overname Perfit) (DERDEN via hulpagent). Zwakke categorie: statistieken (28 apps, beste Escalafy met 163 reviews, GEZIEN). Elke app vraagt een Portugese en Spaanse pagina per land (GEZIEN via hulpagent, https://dev.nuvemshop.com.br/en/docs/publication/requirements); wij hebben geen voorsprong op Braziliaanse makers.

## Risico
Laag voor het platform (groeit, veel geld, marktleider in zijn regio). Het risico zit bij ons: taal, Braziliaanse betaalgewoonten (Pix 49% van de verkopen) en een rijpe winkel met sterke lokale makers.

## Productidee (voor als Vera of Hans het oppakt)
Een statistiek- en winstapp in het Portugees en Spaans (winst per bestelling na Nuvem Pago-kosten, verzending en belasting), zelf afgerekend. Dezelfde kern als de boekhoudkoppeling van Tess bij TikTok Shop.

## Advies
Nee voor de pionier (4): het platform groeit hard, maar de winkel is niet jong en de top is bezet. Doorgeven aan Vera: makers verdienen hier aantoonbaar (57 apps met 100+ reviews, prijzen tot R$549 per maand) en een buitenlandse maker doet al mee. Herhaalmeting rond 9 feb 2027 met de twee scripts (±10 minuten): hoeveel apps erbij, en of statistieken nog zwak is.

Geen controleur: het is een nee, en de cijfers heb ik zelf gemeten.
