# Thangs: betaalde 3D-printmodellen en lidmaatschappen (Vera, 13 nov run 22:31)

Wat het is: thangs.com, een zoekmachine en markt voor 3D-printmodellen (van Physna). Makers verkopen losse modellen, bieden lidmaatschappen aan, en sinds aug 2025 is er Bundle (kopers betalen $14,99 per maand, makers delen 50%). Waarom bekeken: nooit gemeten, past bij onze Blender-figuren, robots.txt staat alles toe en elke modelpagina toont downloads, prijs, datum en een AI-vlag. MyMiniFactory verbiedt ClaudeBot en is daarom niet gemeten; Printables en MakerWorld zijn al gemeten (cijfer 3 en 3).

## Eigen meting (GEZIEN)
- Sitemap van thangs.com: 251.991 modellen. In het id-bereik 1.550.000 tot 1.595.000 (gemaakt half mei t/m eind aug 2026, dus nu 2,5 tot 6 maanden oud) staan 20.792 modellen, ±6.000 per maand. Dat is 46% van de nummers in dat bereik, dus de sitemap is een selectie (vermoedelijk alleen gepubliceerde modellen).
- Willekeurige steekproef van 350 daarvan, elke modelpagina gelezen (data/thangs-steekproef-2026-11-13.jsonl, script data/thangs-pagina-script.py). Uitgesplitst naar hoe het model aangeboden wordt:

| Soort | Aantal | Mediaan downloads | Nul | 10+ | 100+ | Mediaanprijs |
|---|---|---|---|---|---|---|
| Alleen te koop (market) | 58 | 0 | 86% | 2% | 0 (max 21) | $5 |
| Te koop en in lidmaatschap (market-paid) | 163 | 0 | 52% | 17% | 3 (max 388) | $4 |
| Alleen voor leden (paid) | 67 | 1 | 42% | 24% | 5 (max 716) | n.v.t. |
| Gratis (public) | 56 | 6,5 | 12% | 39% | 1 (max 127) | gratis |
| Alleen geprint te bestellen | 6 | 0 | 100% | 0% | 0 | n.v.t. |

- Bovengrens van de bruto omzet (downloads keer prijs) van alle 221 te koop aangeboden modellen samen: ±$12.600, waarvan de top 2 ruim de helft. Van de 58 modellen die alleen te koop zijn: samen hooguit $230. Dit is echt een bovengrens: bij market-paid tellen downloads door leden waarschijnlijk mee, en of Bundle-downloads meetellen is niet te zien.
- Beste nieuwe betaalde model: een cosplay-zwaard-kit van The Kit Kiln ($8,99, 388 downloads, ook via lidmaatschap). 89 verschillende makers in de te-koop-groep; drie makers hebben elk 15 tot 17 modellen in de steekproef.
- 37 van 350 (11%) zijn door Thangs als AI-gemaakt gemarkeerd.
- Controleur rekende alles na uit het bestand en bekeek 4 pagina's; zijn correctie (betaald en gratis anders indelen naar `visibility`) is hierboven verwerkt.

## Geld en regels (DERDEN, onderzoeker, gelezen 13 nov 2026)
- Afdracht losse modellen: 30% onder $5, 20% van $5 tot $10, 15% vanaf $10; lidmaatschappen 14% plus een vast bedrag per maand voor de maker ($5 of $30 per maand bij goedkope plannen); Stripe-kosten erbovenop; Thangs regelt btw (app.thangs.com/terms-and-conditions, thangs.com/resources/help-center-articles/what-fees-does-thangs-charge).
- Nederland wordt ondersteund via Stripe; een bedrijf lijkt niet nodig.
- Betaalde modellen moeten een foto van een echte print hebben, "not just renders or AI-generated images" (thangs.com/content/legal/content-policy/, update 1 dec 2025). AI-modellen overspoelden in aug 2025 de voorpagina; Thangs beperkt sindsdien het aantal per maker op de voorpagina.
- Geen enkel bedrag van een maker gevonden, geen totaal aan uitbetalingen. Thangs claimt 20 miljoen maandgebruikers (eigen claim, vooral zoekmachine); laatste harde cijfer 250.000 gebruikers in 2021.

## Oordeel tegen "Wat een 8 is"
- Geld: kan, maar niet aangetoond voor kleine makers. Wie verdient, doet dat met lidmaatschappen en een vaste schare fans, niet met losse verkoop (86% van de puur te koop gezette modellen: nul downloads).
- Bereik: zwak. Ook gratis modellen halen mediaan 6,5 downloads, tegen 10 op MakerWorld.
- Bouwen: modellen uit Blender kunnen, maar elk betaald model vraagt een echte printfoto, dus een 3D-printer bij Thijs.
- Grote speler worden: nee. Kleiner platform dan MakerWorld en Printables, ±6.000 nieuwe modellen per maand, twee derde betaald.

Cijfer 3, nee. Thangs is hooguit een tweede plek naast MakerWorld voor een maker die al fans heeft.
