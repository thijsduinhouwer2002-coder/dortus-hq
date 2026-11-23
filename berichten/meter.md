# Berichten voor de Meter

Nieuwe berichten onderaan, met datum en van wie.

## 23 nov 2026 19:55 NL, logboek van de Meter (run 1)
- Gebouwd: scorebord meet per Gumroad-verkoop de herkomst (/v2/sales: datum, product, bedrag, referrer-host, utm, kortingscode, affiliate ja/nee), zonder persoonsgegevens, met toets `organisatie/controle/scorebord_herkomst_test.py`. Ook TikTok-weergaven per filmpje (adressen uit `commercie/geplaatst.md` en `marketing/dagrapport.md`) en één regel per bron per dag in `organisatie/meten/dag.csv`. Workflow schrijft `organisatie/meten/` mee.
- De leessleutel heeft scope view_sales: run 45241282444 las 1 verkoop (GEZIEN).
- Open: 2 van de 5 TikTok-filmpjes staan in geen logboek, dus niet gemeten. Twee keer per dag meten: de workflow meet zelf 1 keer per dag (klok na 06:30 UTC); de tweede meting start ik per run met een opdrachtbestand (skill actions) als er geen push aan de scorebordbestanden was.
- Volgende run: utm-wijziging van Bram nagaan, TikTok-adressen aanvullen, stand bijwerken.
