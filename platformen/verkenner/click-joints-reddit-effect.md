# Click Joints: wat leverde de Reddit-post op? (meting Vera)

Opdracht hoofdchat 16 nov 21:55: scorebord per product, met de Reddit-post van Click Joints (r/blender, 16 nov 20:05 UTC, geplaatst door Thijs) na 24 en 48 uur via de downloads op Blender Extensions. Ook BlenderNation is ingezonden (16 nov ±21:20 UTC, wacht op hun keuring); verschijnt dat artikel, dan lopen de twee effecten door elkaar en zeg ik dat erbij.

## Hoe ik meet
- Elke run: `bash platformen/verkenner/data/click-joints-uur-script.sh` (downloadteller van de openbare pagina, en of BlenderNation een artikel heeft). Uitkomst in `data/click-joints-uur.csv`.
- Bezoekers van dortus.com (de post linkt naar de film op dortus.com/click-joints/film.mp4) komen uit het scorebord (Amami), zie `organisatie/scorebord.md`.
- Reddit zelf (stemmen, reacties) is vanuit de cloud niet leesbaar; dat geeft Thijs door (`commercie/blender-click-joints/geplaatst.md`).
- Gumroad-verkopen van Pro ziet alleen Thijs.

## De lijn zonder post (nulmeting, GEZIEN)
Zonder enig bericht groeide de teller rustig: 107 op 14 nov 00:12 UTC, 141 op 15 nov 22:11, 157 op 16 nov 11:16, 169 op 16 nov 19:47 (bron `platformen/blender/downloads.csv` van Ruben en het scorebord). Dat is ±20 tot 25 per dag, ±1 per uur.

**Verwacht zonder post (GOK op die lijn):** ±190 op 17 nov 20:05 UTC en ±212 op 18 nov 20:05 UTC. Alles daarboven schrijf ik toe aan de post (en aan BlenderNation als dat verschijnt).

**Wat een normale uitkomst is:** Joris en Chris verwachten van Reddit weinig voor de winkel (`commercie/blender-click-joints/reddit.md`). Eigen ijkpunt: forums gaven onze andere producten ±40 views in dagen (`verspreiden-2026-11.md`).

## Meetpunten

| Moment (UTC) | Uren na post | Downloads | Verwacht zonder post | Verschil | BlenderNation |
|---|---|---|---|---|---|
| 16 nov 19:47 | -0,3 | 169 | 169 | 0 | nee |
| 16 nov 21:37 | 1,5 | 171 | ±170 | ±+1 | nee |
| 17 nov ±20:05 | 24 | | ±190 | | |
| 18 nov ±20:05 | 48 | | ±212 | | |

**Bezoekers dortus.com (Amami, GEZIEN in scorebord-run 43961656575, 16 nov tot 22:39 NL):** 5 bezoekers, 6 weergaven, waarvan 2 op de Click Joints-pagina en 3 op de voorpagina. Let op: als de post rechtstreeks naar film.mp4 linkt, telt Amami die kijkers niet (een losse video laadt geen telscript). Een lage teller hier zegt dus niet dat niemand keek.

Eerste uitkomst (1,5 uur na de post): nog geen sprong te zien, de teller loopt op het gewone tempo. Dat zegt nog weinig: Reddit-verkeer komt vooral in de eerste 6 tot 12 uur, en de Europese avond loopt nu af.
