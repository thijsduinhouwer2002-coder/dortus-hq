# Zedge (wallpapers, ringtones, meldingsgeluiden)

Vera, 14 nov 2026 run 13:31 (Amsterdam). Advies: **nee, cijfer 2.**

## Wat het is
Zedge is een app (vooral Android) voor wallpapers, ringtones en meldingsgeluiden. Kunstenaars kunnen via Zedge Premium Marketplace verkopen: per item kies je gratis, achter een reclamefilmpje (VIDEO) of betaald met Zedge Credits (1000 credits = $1). Past op papier bij ons: 3D-wallpapers van onze Blender-figuren.

## Eigen meting (GEZIEN, 14 nov 2026)
Twee steekproeven, scripts en ruwe gegevens in `data/zedge-*`.

1. **Gratis uploads, willekeurig:** 3.000 items uit 50 willekeurige delen van de item-sitemap (de sitemap is per UUID verdeeld, dus de steekproef is eerlijk). Alle 3.000 waren gratis: de sitemap bevat geen premium-items.
   - Geüpload in 2025: n=648, mediaan 11 downloads, 6% haalt 100+.
   - Geüpload jan t/m aug 2026: n=280, mediaan 6,5 downloads, 4% haalt 100+.
2. **Premium-items (licensed) uit zoekresultaten:** 160 willekeurige zoekwoorden uit de SEO-sitemap, daaruit 1.070 premium-items, waarvan er 857 zijn opgehaald (dan gestopt om tijd). Dit is een scheve steekproef naar boven: zoekresultaten tonen vooral wat al populair is.
   - 93% staat achter een filmpje (VIDEO), 5% is echt betaald met credits, 2% gratis.
   - VIDEO, geüpload jan t/m aug 2026: n=116, mediaan 9 downloads, 3% haalt 100+, beste 8.184. Samen 10.901 downloads.
   - VIDEO, geüpload 2025: mediaan 15 tot 37 per halfjaar, 5 tot 31% haalt 100+.
   - Betaald met credits (n=44, alle jaren): mediaan 0 tot 3 downloads per lichting. Beste ooit 5.622 (uit 2022, $0,50), daarna 993 (uit 2021). Uit 2026 is de beste 16 downloads, en die kost 10 credits ($0,01).
   - 387 verschillende makers in de premium-treffers.

## Geld (bronnen van de hulpagent, gelezen met curl)
- Maker krijgt 70% van betaalde downloads; prijs meestal $0,25 tot $1,99 (GEZIEN, zedge.net/premium en help.zedge.net, art. 360024600931).
- Een download achter een filmpje levert ±$0,09 in de VS en ±$0,002 in India (GEZIEN, help.zedge.net art. 17967198050580, 25-6-2026). 78% van de gebruikers komt uit opkomende landen (GEZIEN, 10-K).
- Uitbetaling maandelijks via Dots vanaf $50; bij schorsing ben je alles kwijt (GEZIEN, help.zedge.net art. 28289785155092). Daarvoor zijn belastingformulier, adres en telefoon nodig: dat zou bij Thijs liggen.
- Jaarverslag boekjaar 2026 (10-K, 28-10-2026, sec.gov): 19,3 miljoen maandgebruikers, **16,8% minder** dan een jaar eerder; omzet $31,6 miljoen, waarvan $1,9 miljoen "Other" waar Premium onder valt. Zedge schrijft zelf: "Zedge Premium has taken longer to scale than we originally anticipated." (GEZIEN)
- Kwartaalbericht 26-10-2026: Premium-verkoop ±$0,65 miljoen per kwartaal bruto, +1,9% op jaarbasis (GEZIEN). Voor alle makers samen dus hooguit ±$1,8 miljoen per jaar (GOK).
- Makers die bedragen noemen staan alleen op Zedge's eigen blog (DERDEN, gekozen door Zedge): $200 tot $400 per maand bij ±6.000 items, $800 tot $1.000 bij 1.400 items, een top-100-maker zakte van $3.000 tot $5.000 naar ±$1.000 per maand (2024).

**Rekensom voor ons (GOK):** een nieuw VIDEO-item haalt mediaan ±9 downloads. Bij $0,002 tot $0,09 per download is dat $0,02 tot $0,80 per item, met de nadruk op de onderkant door het land van de kijkers. 300 Blender-wallpapers leveren dan ±$5 tot $100 in totaal op, niet per maand. De $50-drempel halen we pas na maanden. Echt betaalde items verkopen bijna niet.

## Regels
- AI-werk mag, eigen generator moet gelabeld worden; fan-art en merken verboden, schorsing bij overtreding; uploadlimiet per maand (GEZIEN, help.zedge.net).
- Sinds Stable Diffusion 673% meer uploads, tot 184.000 per week in 2023; Zedge heeft een eigen AI-maker (pAInt) die direct met makers concurreert (GEZIEN, blog.zedge.net).

## Vindbaarheid
40% van de downloads via swipen naar verwante items, 25% zoeken, 13,6% populaire feed (GEZIEN, blog 31-3-2025). Volgorde op downloads en uploaddatum. Een nieuwe maker begint dus onderaan.

## Voor en tegen
- Voor: open voor iedereen, AI en 3D toegestaan, bouwen is alleen plaatjes renderen (uren, geen weken).
- Tegen: bereik per nieuw item mediaan 4 tot 9 downloads; geld per download fracties van een cent; platform krimpt 17% per jaar; Premium groeit niet; vloed aan AI-plaatjes en Zedge's eigen generator; verdienen lukt alleen met duizenden items en dagelijks uploaden, en dat is precies het volumespel dat we niet willen.

## Cijfer en advies
Bereik 2, geld 2, past 6 (makkelijk te maken). **Cijfer 2, nee.** Niet opnieuw meten tenzij Zedge Premium hard gaat groeien (kwartaalcijfers, ±$0,65 miljoen per kwartaal als meetlat).

Niet apart nagekeken door een controleur: het advies is nee en de cijfers staan zelf in de bijgevoegde gegevens en scripts.
