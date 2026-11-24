# Keuring blender-gewrichten (taken.md), 24-11-2026, automatische keurder
Wat ik keurde: commit df5688ce6, bestand `producten/blender-gewrichten/taken.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht is hier de commitboodschap: mail 3 Click Cuts verwerkt (M1 en K1), upsell-zin als concept, taken bijgewerkt.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Taak 2 is bijgewerkt: "Daan ja 20:05, M1 en K1 verwerkt 20:10, bij hoofdchat voor Thijs". Dat past bij de commitboodschap. | Feit (alleen dat de tekst klopt met de boodschap) | Hoog | n.v.t. |
| 2 | Of M1 en K1 echt in `gumroad-mail-2026-11-27.md` zijn verwerkt, kan ik niet zien. Dat bestand zit niet in deze wijziging. | Vermoeden | Midden | Diff van dat bestand, of een eerdere commit die het al bevat. |
| 3 | Taak 5 (upsell-zin) is nieuw en nog open. Dat past bij "concept", niet bij "af". | Feit | Hoog | n.v.t. |
| 4 | Taak 5 verwijst naar `upsell-gratis-naar-pro.md`, maar dat bestand staat niet in deze wijziging. Het bestaat dus misschien al, of nog niet. | Vermoeden | Midden | `git ls-files` voor dat pad, of de eerdere commit die het toevoegde. |
| 5 | Taak 6 (etalagepakket, audit 19:45) is nieuw en open, zonder dat er werk is gedaan. Dat klopt met de commitboodschap, die er niets over zegt. | Feit | Hoog | n.v.t. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Alleen een takenlijst gewijzigd. Er zijn geen tests of code aangeraakt en het bestand is ver onder 400 regels. | Feit | Hoog | Tests niet aangepast, bestandsgrootte |
| 2 | `architectuur.md` hoefde niet bij: er is geen code veranderd. | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 4 | De cijfers in de ongewijzigde regels dragen een label ("GEZIEN Meter", "GEZIEN meet_downloads.sh"). Alleen "$14,25" in taak 4 heeft geen label. Het bedrag lijkt $19 min 25% (CYBER25), maar dat staat nergens uitgelegd. | Vermoeden | Midden | Cijfers met GEZIEN, DERDEN of GOK |
| 5 | Taak 5 gaat over een upsell naar Pro op Gumroad. Op extensions.blender.org mag de gratis versie niet naar de betaalde verwijzen (regels 3.3, 3.10, 6.1 uit het ontwerp). Uit de tekst blijkt dat de zin alleen voor Gumroad is. | Vermoeden | Midden | Ontwerp: gratis zonder verwijzing naar betaald |
| 6 | De tijd "±20:15" in de kop staat drie minuten na het keurmoment (20:12). Dat is een kleinigheid. | Feit | Hoog | n.v.t. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Niet van toepassing. Dit is een interne takenlijst en een klant ziet er niets van. Ik geef daarom ook geen cijfers voor "is het goed genoeg", want die gelden voor beeld, tekst of spel dat een klant ziet. De mail en de upsell-zin zelf heb ik niet gezien.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet bij "$14,25" in taak 4 erbij hoe het bedrag is berekend (bijvoorbeeld "$19 min 25%, GOK"). Dan is het een gelabeld cijfer.
- Controleer bij de keuring van `upsell-gratis-naar-pro.md` dat de zin alleen op Gumroad komt en niet in de add-on of op extensions.blender.org.
- Keur de mail en de upsell-zin zelf met hun eigen diff. Deze wijziging bewijst alleen dat de lijst is bijgewerkt, niet dat de teksten kloppen.

---
Automatische keurder, model `claude-sonnet-5-5`, 18782 tokens in, 2752 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
