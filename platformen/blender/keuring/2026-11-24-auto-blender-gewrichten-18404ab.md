# Keuring blender-gewrichten takenlijst, 24-11-2026, automatische keurder
Wat ik keurde: commit 5e5c41947 (alleen `producten/blender-gewrichten/taken.md`, bereik 425f301..18404ab)
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht is `ontwerp.md`, plus de commitboodschap ("takenlijst Click Joints met weekdoel saleweek, kan K1 Daan in pro-1.2.7"). Het is een pure takenlijst, geen code.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Het weekdoel is ingevuld (5 verkopen Pro in de saleweek, live vóór vr 27 nov 00:00) en de taken staan genummerd met eigenaar. Daarmee is wat de commitboodschap belooft gedaan. | Feit | Hoog | Zichtbaar in de diff. |
| 2 | Taak 1 staat op [x]: "Also new since 1.2" is "Also new in 1.2" geworden in `platformen/blender/pro-1.2.7.md`. Dat bestand zit niet in deze wijziging. | Vermoeden | Midden | De diff van `pro-1.2.7.md` in een eerdere commit, of die tekst in het bestand zelf. |
| 3 | De kop zegt "Bijgewerkt di 24 nov ±19:45 NL", terwijl deze keuring om 19:12 NL draait. Het tijdstip ligt dus na de commit. | Feit | Hoog | Het echte commit-tijdstip. Waarschijnlijk is het een schatting van de bouwer. |
| 4 | De weekdagen kloppen met de data (24 nov di, 26 nov do, 27 nov vr, 2 dec wo). De prijs $14,25 is 25% korting op $19. | Feit | Hoog | Rekensom en kalender. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De cijfers over verkopen en downloads (1 verkoop, $19, 375 downloads) hebben een GEZIEN met bron en tijd. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 2 | "$14,25 op Gumroad" en "CYBER25" hebben geen label. Het is afgeleid van het saleplan en niet ergens gezien. | Feit | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 3 | De prijs $19 voor Pro staat niet in het stuk van `ontwerp.md` dat ik kreeg (daar $12, lanceerprijs $9). Het kan een latere prijswijziging zijn die in het afgekapte deel staat. | Vermoeden | Laag | Ontwerp en takenlijst horen gelijk te zijn |
| 4 | Geen persoonsgegevens, sleutels of wachtwoorden. Het bestand is klein, er zijn geen tests aangepast en er is geen AI-beeld of -geluid. | Feit | Hoog | Regels voor persoonsgegevens, tests en bestandsgrootte |
| 5 | Voor het live zetten (Pro 1.2.7, vóór vr 27 nov) staat in de lijst alleen de keuring van Daan op de mail. Een keuring door een agent op het live zetten zelf staat er niet. | Vermoeden | Midden | "Bij live zetten blijft een keuring door een agent nodig" |

## Deel C: zou een gebruiker het leuk en fijn vinden?

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Niet van toepassing: de wijziging bevat niets wat een speler of koper ziet of speelt. | n.v.t. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet bij taak 1 een verwijzing naar de commit van `pro-1.2.7.md`, zodat "[x]" na te lopen is.
- Label "$14,25" en "CYBER25" met GOK of GEZIEN, en noem de plek waar de saleprijs staat.
- Zet vóór het live zetten van Pro 1.2.7 een taak "keuring door een agent". De bestaande taken noemen alleen Daan en Thijs.
- Zet het tijdstip van de kop gelijk aan het echte commit-tijdstip, of schrijf "±" met het gekozen uur erbij.
- Controleer of de prijs $19 klopt met het meest recente ontwerp of besluit. Het zichtbare ontwerp noemt $12 en $9.

---
Automatische keurder, model `claude-sonnet-5-5`, 17994 tokens in, 2800 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
