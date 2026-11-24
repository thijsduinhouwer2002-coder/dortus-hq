# Click Joints Pro: heldenbeelden 1 (tekenpop-agent, di 24 nov 2026)

Opdracht hoofdchat 16:45 NL: Thijs vindt de winkelbeelden te simpel, "het moet er echt goed en uitdagend uitzien,
echt een mooi stuk techniek". Lat en stijl: `cover-pop-dynamisch.png` (release tekenpop-1). Alles staat in release
`pro-heldenbeelden-1` (workflow `.github/workflows/pro-heldenbeelden.yml`, scripts in `bron/`). Niets geplaatst.

GEZIEN = zelf gezien of gemeten. GOK = eigen schatting.

## De vier beelden (elk 2400 x 1200 voor Superhive en 1920 x 1080 voor Gumroad)
| Bestand | Wat je ziet | Wat echt is en wat alleen voor het beeld |
|---|---|---|
| `held-1-knie-*` | Linkerknie van de houten tekenpop, een kwart weggesneden, groene gloeiende lijn langs de speling, ondiepe scherptediepte, randlicht. Titel. | Het scharnier komt uit de echte knop Figure from rig van Pro 1.2.6 (stop 115, speling 0,2 mm). De snede (Boolean Exact) en de groene lijn zijn alleen voor het beeld: de lijn ligt op de randen van het snijvlak die binnen 0,45 mm van het andere deel liggen, dus precies op de spleet rond de knokkel en langs de tong; de wig van de eindstop is breder en gloeit niet. Een losse pen is er niet: de knokkel draait in een gleuf en klikt met twee neusjes in kuiltjes. |
| `held-2-spiraal-*` | Alle 10 delen in een draaikolk uit elkaar, met bewegingsonscherpte, gouden bogen 0 tot 115 graden bij ellebogen en knieën. Titel. | Gewrichten en het bereik in de bogen komen van de add-on (`cj_bereik_graden`, 114,96 lokaal). De draaikolk, de draaiing per deel en de onscherpte zijn alleen voor het beeld. |
| `held-3-voor-na-*` | Links het figuur met rig (grijs, half doorzichtig, oranje botten zoals in Blender), rechts na de knop in hout en messing, lichtstreep ertussen. | Zelfde figuur, zelfde houding. De botten volgen de rig van het figuur; rechts staan de gewrichten 0,35 keer de Exploded view uit elkaar zodat je het messing ziet. |
| `held-4-fit-test-strip-*` | Vijf staafjes met elk een kogelgewricht, bovenste helft iets opgetild, getallen 0.10 tot 0.30 op de vloer. | De staafjes komen uit de echte knop "Fit test: ball" van Pro 1.2.6, met het getal van de add-on in reliëf op de bovenkant. Het optillen en de grote getallen op de vloer zijn alleen voor het beeld (het reliëf is 3,6 mm, te klein op een productfoto). |

Geen foto van een echte print: geen printlaagjes, geen printer, geen hand. Geen AI-beeld. Tekst in beeld alleen de
titel op beeld 1 en 2 en de getallen op beeld 4.

## Hoe gemaakt
`bron/helden.py` leest `commercie/filmpjes/studio/tekenpop_beelden.py` in (dat leest zelf `pro_beelden.py`), dus
dezelfde tekenpop, studio, licht en materialen als de tekenpop-covers. Stops 115 in de rig: `CJ_STOP=115`
(`figuur_tekenpop.laad_tekenpop(stop_graden=...)`). `bron/maak.py` zet de titel erop, maakt voor en na, de formaten en
`overzicht.png` voor de keurder.
