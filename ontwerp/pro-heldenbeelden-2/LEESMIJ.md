# Click Joints Pro: heldenbeelden 2 (heldenbeelden-maker, di 24 nov 2026)

Opdracht hoofdchat: ronde 2. Beeld 3 (voor en na) en 4 (Fit test strip) uit ronde 1 zijn goed en blijven. Beeld 1
(knie, las als abstract hout) en 2 (spiraal, delen te klein en verspreid) zijn opnieuw gemaakt. Lat: Thijs, besluit
24 nov 16:39 ("echt een mooi stuk techniek moeten mensen gelijk denken"). Alles staat in release
`pro-heldenbeelden-2` (workflow `.github/workflows/pro-heldenbeelden-2.yml`, scripts in `bron/`). Niets geplaatst,
niets uitgegeven.

GEZIEN = zelf gezien of gemeten. GOK = eigen schatting.

## De beelden (elk 2400 x 1200 voor Superhive en 1920 x 1080 voor Gumroad), plus `overzicht.png`
| Bestand | Wat je ziet | Wat echt is en wat alleen voor het beeld |
|---|---|---|
| `held-1-knie-*` | Het linkerbeen van de houten tekenpop van opzij: dij, knie, onderbeen met voet. Onderbeen 60 graden gebogen. Gouden gradenboog 0 tot 115 met streepjes per 15 graden en een balk bij de stop, een zachte ring van 0 tot 60, een gouden schim van het onderbeen bij 115. In de knie een rond venster: knokkel in de gleuf, de wig, groene spleet. Linksonder een ronde inzet met een scherpe close-up van dat venster, met een lijn naar de knie. Titel. | Het scharnier komt uit de echte knop Figure from rig van Pro 1.2.6 (stop 115, speling 0,2 mm). De buiging (60) gaat met de schuif van de add-on. Het getal 115 is wat de add-on meldt (`cj_bereik_graden` 114,96, GEZIEN in `b-knie.json`). Alleen voor het beeld: het venster (Boolean Exact, straal 12,5 mm, alleen de helft naar de camera), de groene lijnen (randen van het snijvlak binnen 0,45 mm van het andere deel, dus precies de speling rond de knokkel), de boog, de ring, de schim en de kanteling van het hele been (30 graden, een pas). Een losse pen is er niet: de knokkel draait in een gleuf en klikt met twee neusjes in kuiltjes; de neusjes zitten opzij en vallen buiten het snijvlak. |
| `held-2-spiraal-*` | Alle 10 delen in een sprong uit elkaar, van opzij: benen in spagaat, een arm naar voren, een omhoog naar achteren, het geheel iets gekanteld. Grote gouden bogen 0 tot 115 met streepjes, balk en getallen bij beide ellebogen en knieën. De delen vullen ongeveer 66 procent van de breedte (x 0,31 tot 0,97, GEZIEN in het log van de kader). Titel links. | Delen, gewrichten en bereik komen van de add-on (Exploded view 1,0 keer, ellebogen 70 en 45, knieën 10 en 60 met de schuif). Alleen voor het beeld: armen en benen als geheel om schouder of heup gedraaid (verder dan de kogels kunnen, het is een opengewerkte weergave), elk deel 5 tot 13 graden scheef, het geheel 12 graden gekanteld. De bogen hangen aan het bovenste deel van het gewricht en wijzen van rechtdoor (0) naar de buigkant. |
| `held-3-voor-na-*` | Ongewijzigd uit ronde 1. | Zie `ontwerp/pro-heldenbeelden-1/LEESMIJ.md`. |
| `held-4-fit-test-strip-*` | Ongewijzigd uit ronde 1. | Zie `ontwerp/pro-heldenbeelden-1/LEESMIJ.md`. |

Geen foto van een echte print: geen printlaagjes, geen printer, geen hand. Geen AI-beeld. Geen tekst over testen.
Tekst in beeld: de titel, en bij de bogen alleen 0°, 60° en 115°.

## Hoe gemaakt
`bron/helden2.py` leest `ontwerp/pro-heldenbeelden-1/bron/helden.py` in zonder zijn main(), dus dezelfde tekenpop,
studio, materialen en knop. De studio (gebogen wand) draait mee met de camera, zodat de wand ook achter het figuur staat
als de camera van opzij kijkt. `bron/maak2.py` zet de titel en de inzet erop (titel en uitsnede uit `maak.py` van
ronde 1), haalt beeld 3 en 4 uit release `pro-heldenbeelden-1` en maakt `overzicht.png`. Eerst lokaal geprobeerd op
halve grootte (Blender 5.3.0, zelfde zip), daarna in de workflow op volle grootte met 64 samples.
