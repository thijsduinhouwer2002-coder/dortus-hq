# Keuring blender-gewrichten (meting Pro 1.2.3 op main), 24-11-2026, automatische keurder
Wat ik keurde: commit 97ccf4564, bestand `producten/blender-gewrichten/proeven/omslag-figuren-main-2026-11-24/uitslag.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
Dit is alleen een meetverslag, de add-on zelf is niet veranderd. Ik toets of de conclusies kloppen met de tabel en met het ontwerp.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Conclusie 1 (tekenpop krijgt in 4.2.23, 5.2.3 en 5.3.0 alle 9 gewrichten) volgt uit de tabel: 9 en 9 in alle drie. | Feit | Hoog | n.v.t. |
| 2 | Conclusie 2 (kleding 9 van 9 in 5.x, 8 van 9 in 4.2 met de rechterknie weg) volgt uit de tabel. De 6 slechte sneden en de tijden van 143 tot 207 s staan er eerlijk bij. | Feit | Hoog | n.v.t. |
| 3 | Het verslag zegt dat de run draaide op commit 3974792, terwijl main op 14e6e42 staat. Of de gemeten code gelijk is aan main, staat niet in de tekst. | Vermoeden | Midden | Een regel die zegt dat 3974792 main plus alleen het meetscript is, of een `git diff` zonder verschil in `click_joints/`. |
| 4 | Conclusie 3 zegt dat de releasenote "on our test figures" klopt. De tekst van die note staat niet in de wijziging. Als hij belooft dat alle gewrichten op alle testfiguren lukken, klopt hij niet voor kleding in 4.2. | Vermoeden | Midden | De regel uit CHANGELOG of de releasenote van 1.2.3 naast deze uitslag. |
| 5 | De cijfers (JSON en log) staan op tak `betrouwbaar-uitslag`, niet in deze wijziging. Ik kon ze niet nalezen. | Vermoeden | Midden | De map `main-45295977807/<versie>/` openen en de tabelcijfers vergelijken. |
| 6 | Elke meting is maar twee keer herhaald. Dat is genoeg voor "gelijk", maar zwak voor de slechte sneden bij 4.2 (1 bij de tekenpop, 6 bij kleding). | Feit | Midden | Een derde herhaling op 4.2, of een log waaruit blijkt dat de slechte sneden steeds op dezelfde plek vallen. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Het bestand heeft 20 regels en er zijn geen tests aangepast. | Feit | Hoog | Tests niet aangepast, bestanden onder ±400 regels |
| 2 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in. | Feit | Hoog | Geen persoonsgegevens |
| 3 | De bron is vermeld (run, commit, script, tak) met het label GEZIEN. De tabelcijfers hebben geen eigen label, maar vallen onder die bron. | Feit | Midden | Cijfers met GEZIEN, DERDEN of GOK |
| 4 | `architectuur.md` is niet bijgewerkt. Dat hoeft hier niet, want er is geen code veranderd. Het open punt voor 4.2 staat in het verslag. | Feit | Hoog | architectuur.md bijgewerkt |
| 5 | Het commitbericht noemt ook "logboek" en "bericht Bram". Die bestanden zitten niet in deze diff. Ik kan niet zien of ze elders zijn gecommit. | Vermoeden | Laag | Logboek bijhouden |
| 6 | Het verslag verwijst naar `../ai-figuren-tak-rig-2026-11-24/`. Ik kon niet nagaan of die map bestaat. | Vermoeden | Laag | n.v.t. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Er is niets om te zien of te spelen, dus dit is alleen een vermoeden vanuit de koper.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een koper met Blender 4.2 LTS krijgt bij kleding een knie minder, met de melding "Tight: too little limb past this joint". Dat is zonder uitleg verwarrend. | Een duidelijkere melding of tip, bijvoorbeeld "probeer Blender 5.x" of "rek het onderbeen". | Midden |
| 2 | Negen gewrichten duren 1 tot 3,5 minuten. Een koper ziet dan lang niets gebeuren. | Een voortgangsregel ("joint 4 of 9") in het paneel, als die er nog niet is. | Klein |
| 3 | Het verschil tussen 4.2 en 5.x staat nu alleen in dit interne verslag. | Een regel op de winkelpagina of in de release notes over wat 4.2 wel en niet haalt. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet bij conclusie 3 de letterlijke releasenote-regel erbij, en schrijf voor 4.2 expliciet dat kleding 8 van 9 geeft.
- Vermeld of commit 3974792 inhoudelijk gelijk is aan main 14e6e42 (deel A, punt 3).
- Zet de cijfers van de tak `betrouwbaar-uitslag` of een samenvatting ervan in de repo zelf, zodat de uitslag controleerbaar blijft.
- Onderzoek de rechterknie bij kleding in 4.2 (Exact-solver), zoals het verslag al als open punt noemt.

---
Automatische keurder, model `claude-sonnet-5-5`, 18010 tokens in, 3437 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
