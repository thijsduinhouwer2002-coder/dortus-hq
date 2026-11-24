# Korte links per bron: voorstel van de Meter (23 nov 2026)

**Stand 24 nov 08:45 NL:** laag 1 gekeurd (Daan ja), gebouwd op tak `claude/utm-koopknoppen` (977af09), nog niet op main van dortus: live koopknoppen zonder utm (GEZIEN, curl). Bram gevraagd.

Doel (Thijs, 23 nov): per verkoop weten waar de koper vandaan kwam. Dit voorstel kost niets en vraagt geen nieuw account.

## Wat er nu gebeurt (GEZIEN, curl 23 nov)
- dortus.com/yt/ en dortus.com/tt/ zijn gewone pagina's (code 200, geen doorsturing). Hun koopknop gaat naar `https://duinhouwer8.gumroad.com/l/click-joints-pro` zonder utm.
- Gevolg: een koper via YouTube en een koper via TikTok komen in Gumroad allebei binnen met referrer `dortus.com`. Het verschil zien we alleen in Amami (bezoeken per pad), niet per verkoop.

## Wat Gumroad laat zien (DERDEN)
- Per verkoop geeft de API `referrer`, `utm_source`, `utm_medium`, `utm_campaign`, `offer_code` en `affiliate` (Gumroad API-docs, bron in de open code: https://github.com/antiwork/gumroad/blob/main/app/javascript/components/ApiDocumentation/Endpoints/Sales.tsx ; scope `view_sales`).
- "A referrer is the original source of a visit to your product." Discover heet "Recommended by Gumroad"; "Gumroad" betekent eerst een andere Gumroad-pagina (https://gumroad.com/help/article/74-the-analytics-dashboard).
- UTM-links maak je in Analytics, Links; een klik telt en een koop binnen 7 dagen hoort bij die link. Wijst de link naar één product, dan tellen alleen kopen van dat product (zelfde hulpartikel).
- Of een losse `?utm_source=...` achter de productlink ook in `utm_source` van de verkoop komt, zonder link uit Analytics, staat niet in de hulp: GOK dat het werkt. De eerste verkoop via zo'n link laat het zien (scorebord, tabel "Herkomst Gumroad-verkopen").

## Voorstel (drie lagen, de eerste kan vandaag)
1. **utm achter elke koopknop op dortus.com** (Bram, repo dortus, na keuring door Daan). Elke korte pagina krijgt een eigen bron in de link naar Gumroad:

   | Pad op dortus.com | Waar staat hij | Koopknop wordt |
   |---|---|---|
   | /yt | YouTube Shorts en lange video's | `...click-joints-pro?utm_source=yt&utm_medium=video` |
   | /tt | TikTok-onderschriften | `...click-joints-pro?utm_source=tt&utm_medium=video` |
   | /click-joints | site zelf, zoekmachines | `...click-joints-pro?utm_source=site&utm_medium=pagina` |
   | /m/<maker> (nieuw) | per maker die een video maakt | `...?utm_source=maker&utm_campaign=<maker>` |
   | /f/<forum> (nieuw, bv. /f/reddit, /f/blenderartists) | één pad per forumpost | `...?utm_source=forum&utm_campaign=<forum>` |
   | /addon (nieuw) | knop in de gratis add-on en op extensions.blender.org | `...?utm_source=addon&utm_medium=gratis` |

   Amami telt dan de bezoeken per pad (staat al in het scorebord), Gumroad de verkopen per utm. Samen geeft dat per bron: bezoeken, verkopen, omrekening.
2. **Kortingscodes als tweede spoor.** Makers hebben al een eigen 100%-code (CJP<naam>); CYBER25 is de sale. Het scorebord telt die nu per verkoop. Een eigen betaalcode per kanaal (bv. YT10, TT10) maakt de bron hard zichtbaar, maar kost marge: beslissing hoofdchat, niet nodig voor laag 1.
3. **UTM-links in Gumroad zelf** (Analytics, Links): geeft klikken, verkopen en omrekening in het dashboard van Gumroad. Vraagt inloggen, dus alleen de hoofdchat in Chrome. Pas doen als laag 1 werkt.

## Meten
- Het scorebord (`organisatie/controle/scorebord.py`) schrijft sinds 23 nov per verkoop datum, product, bedrag, referrer-host, utm, kortingscode en herkomst in `organisatie/meten/verkopen.csv`, zonder persoonsgegevens, en één regel per bron per dag in `organisatie/meten/dag.csv`.
- Werkt de leessleutel niet voor /v2/sales (geen scope `view_sales`), dan staat dat bij "Meldingen van deze run" in het scorebord.
