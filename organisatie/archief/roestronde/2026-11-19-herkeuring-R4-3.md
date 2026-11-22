# Herkeuring R4 (derde), beeldvergelijking Bison & Flex en Rollwright, 19 nov 2026, losse keurder (niet de bouwer)
Wat ik keurde: commits ca2afbb0, 75c4336d, c2c894cc, 75de19b4, 179807b2, 66df5380, 867f8689 (`Gedeeld.kt`, `beeldvergelijk.py`, `jetbrains-bison-flex-e2e.yml`, `rollwright-e2e.yml`); job-logs van Bison & Flex-runs 44500250051, 44500264197, 44500267041, 44503498367 en 44506766580, Rollwright-runs 44434034171, 44486124815 en 44490291212; referentieplaatjes van l1 uit de geschiedenis van de tak schermen (commits 9ea6d5a, 0d602cc, a9bd18f), zelf bekeken met de Read-tool en zelf nageteld.
Vorige keuring: `platformen/hoofdchat/2026-11-19-herkeuring-R4-2.md` (één moet-punt: vals alarm kleurenpagina).
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | **De drie runs zijn van dezelfde code, tegen een referentie van die code.** 44500264197 en 44500267041 draaiden op 66df5380 en vergeleken allebei met de referentie van push-run 44500250051 (ook 66df5380). 44503498367 draaide op b24ed097 en vergeleek met 44500267041 (66df5380). `git diff --stat 66df5380 b24ed097`: alleen berichten, bord, besluiten, opdrachtbestanden en keuringen, niets in `producten/jetbrains-bison-flex`, de workflow of `organisatie/controle`. Alle drie GROOT 0, grootste ruis 2860 px (0,055 procent, clion-donker-calc-y). Uit de job-logs gelezen. | feit | hoog | |
| 2 | **Vierde run met het bericht aan: geen vals alarm.** Push-run 44506766580 op 867f8689 (beeldbericht weer aan) tegen de referentie van 44503498367: GROOT 0; job `beeldbericht` zegt "geen groot beeldverschil", geen bericht aan Chris. Kleurenpagina licht en donker "gelijk" in alle vier de runs. Samen vijf runs van dezelfde code zonder groot verschil. | feit | hoog | |
| 3 | **Vaste scheiding**: `winkelproject()` schrijft voor de IDEA-test (voorvoegsel `bisonflex-`) `.idea/workspace.xml` met `settings.editor.splitter.proportion` 0.33. Raakt geen assert. CLion krijgt het bestand niet (daar wisselde dan het zijpaneel, runs 44496665424 en 44496687498 genoemd); de CLion-plaatjes gaven 931 tot 2860 px ruis, onder de grens. | feit | hoog | |
| 4 | **Conflictvenster stabiel: buiten het masker ja.** In alle vijf de runs `*-hernoem-conflict.png` "gelijk" of 184 px (0,010 procent), maat 1600x1174. De boom bovenin (y 60 tot 330) telt nog steeds niet mee; dat wisselen is dus verborgen, niet opgelost. Geen echte fout verdwijnt daardoor: de tekst "'line' already exists in calc.y" staat ook als tooltip in de editor eronder en telt wel (vorige keuring A6). | feit | hoog | |
| 5 | **Rollwright, nieuwe maskers verbergen geen fout van Rollwright.** Zelf bekeken op `l1-logboek.png` en `l1-logboek-tekst.png`: `l1-*:0,40,345,750` is de bestandenlijst van Obsidian zelf (notities van de testkluis, niet van de plugin), `l1-*:940,30,1024,90` de tooltip "7: 7" en de knop Roll. De tijdvakjes staan nu op beide plaatjes precies op de kloktijden (op `l1-logboek-tekst` drie eigen vakken op y 218, 288 en 372), de worp "7" en de tabeltekst tellen weer. Wel valt de knop Roll helemaal binnen het tooltipvak, dus een kapotte Roll-knop ziet de vergelijking op l1 niet (wel op de andere plaatjes waar het paneel in beeld is). | feit | hoog | |
| 6 | **Rollwright: de maskers verklaren het vals alarm van 09:21 maar voor een deel.** Zelf nageteld op de referenties van run 44434034171 en 44486124815 (zelfde Obsidian 1.15.1, installer 1.5.8): 14422 px verschil, waarvan 6832 in de bestandenlijst en 1362 bij de tooltip. Na alle maskers blijft 4388 px (0,54 procent, boven de grens 0,4) over: alle tekst in de notitie en het paneel iets anders getekend. Tussen de twee nieuwere runs (44486124815 en 44490291212) is het na de maskers 151 px, en run 44490291212 gaf GROOT 0. Er is maar één run met de nieuwe maskers. Komt dat tekstverschil terug, dan krijgt Olaf weer een vals bericht, en dat komt dan niet door de maskers. | feit (getallen), vermoeden (komt terug) | midden | twee of drie Rollwright-runs na elkaar van dezelfde code met 0 groot |
| 7 | Berichten over het vals alarm staan bij Chris (09:30) en Olaf (10:00). | feit | hoog | |
| 8 | `beeldvergelijk.py` kreeg een paneelvorm (`patroon%x0,y0,x1,y1,schuif`) die nu nergens gebruikt wordt: de workflow van Bison & Flex staat weer op gewone maskers. Werkt alleen als iemand hem aanzet. | feit | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen test verzwakt: in de e2e-code alleen het schrijven van `workspace.xml`, geen assert, grens of overgeslagen test weg; grenzen 0,3 en 0,4 procent ongewijzigd. | feit | hoog | tests niet aangepast om te slagen |
| 2 | Niets geforceerd, runnummers met GEZIEN in workflow en `architectuur.md`; die kloppen met de logs. | feit | hoog | harde regels 5 en 6 |

## Moet (blokkeert akkoord)
Geen. Het moet-punt van de tweede herkeuring is opgelost: de scheiding staat vast, vijf runs van dezelfde code gaven 0 groot, de eerste push-run met het bericht aan gaf geen bericht.

## Kan (mag later)
- Rollwright: kijk bij de volgende twee runs of het tekstverschil van A6 terugkomt; zo ja, uitzoeken waardoor (bijvoorbeeld venster wel of niet actief) in plaats van nog een masker.
- Rollwright: tooltipvak kleiner maken zodat de knop Roll weer telt (bijvoorbeeld de muis eerst van de knop af, dan is er geen tooltip).
- Bison & Flex: de boom in het conflictvenster en het Find-paneel in de test altijd openklappen en de maskers weghalen (vorige keuring, kan).
- De ongebruikte paneelvorm in `beeldvergelijk.py` weghalen of in een test vastleggen.

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
