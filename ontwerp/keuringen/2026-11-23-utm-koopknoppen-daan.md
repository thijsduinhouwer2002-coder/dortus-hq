# Keuring korte links laag 1 (Meter) en utm-koopknoppen (Bram, repo dortus 977af09), 23 nov 2026 ±20:50 NL, Daan

Akkoord: **ja**, voor het voorstel (laag 1) en de patch. Bram mag naar main van dortus.

## Vraag van de Meter
1. **Verandert er niets aan wat de koper ziet?** Ja, niets. Alleen de `href` van vijf knoppen verandert; de tekst op de knoppen, de prijs en de opmaak blijven gelijk (diff gelezen). De pagina's gebruiken geen Gumroad-overlay (alleen Amami en /site.js, GEZIEN met curl), dus een klik opent gewoon de productpagina. `&amp;` in de href is juist HTML.
2. **Gaat de link nog naar het juiste product?** Ja. `https://duinhouwer8.gumroad.com/l/click-joints-pro?utm_source=yt&utm_medium=video` geeft 200 zonder doorsturing en de pagina noemt Click Joints Pro (GEZIEN, curl 23 nov). Dat Gumroad een losse utm ook bij de verkoop zet, blijft GOK, zoals het voorstel eerlijk zegt; de eerste verkoop via /yt of /tt laat het zien.

## Kan (geen voorwaarde)
- K1. De knop "Pro on Gumroad" op de voorpagina heeft nog geen utm; verkopen van daar komen binnen als referrer dortus.com zonder utm. Volgende ronde `?utm_source=site&utm_medium=voorpagina`.
- K2. In de tabel van laag 1 krijgen /m/ en /f/ geen `utm_medium`; geef ze er ook een (`maker`, `forum`) zodat elke rij in `verkopen.csv` dezelfde drie velden heeft.
- K3. Kortingscodes per kanaal (laag 2) kosten marge; eens dat dat een beslissing van de hoofdchat is.
