# Keuring blender-gewrichten paneel 1.2.9 (alleen de KAART-regel en drie keuringsbeelden), 25-11-2026, automatische keurder
Wat ik keurde: commit 08124fb5d (KAART.md, drie png-bestanden die ik niet kreeg; de paneelcode op tak `claude/blender-paneel-1.2.9` zag ik niet)
Akkoord: ja (alleen voor deze kaartnotitie; het uitbrengen van Pro 1.2.9 is niet gekeurd)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De regel in KAART.md past bij de commit: drie verschillen (Figure from rig bovenaan, proefstrip en scharnier naar stap 2, beoordelingsregel), tak genoemd, uitbrengen niet vóór ma 30 nov (30 nov 2026 is een maandag). | Feit | Hoog | n.v.t. |
| 2 | Of het paneel echt zo werkt, kan ik niet zien. De code staat niet in deze wijziging en de drie beelden kreeg ik niet. | Vermoeden | Laag | De diff van `paneel.py` op de tak, de beelden met Read bekijken, en de e2e-run met nummer. |
| 3 | Het ontwerp wil per stap alleen wat je dan nodig hebt. Proefstrip en scharnier in stap 2 past daarbij, als er niet meer dan één grote knop per stap bijkomt. | Vermoeden | Midden | Beeld `1.2.9-paneel-na-figuur.png` bekijken. |
| 4 | De commit zegt "e2e groen" zonder runnummer. Zo is het niet na te gaan. | Feit | Hoog | Het runnummer en de uitslag in 4.2, 5.2 en 5.3. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` staat niet bij de gewijzigde bestanden. Dat is nu geen fout, want de paneelcode zit niet in deze wijziging. Bij het samenvoegen van de tak moet het wel mee. | Vermoeden | Midden | architectuur.md bijgewerkt |
| 2 | De beoordelingsregel verwijst in de gratis versie alleen naar Blender Extensions en in Pro naar Superhive en Gumroad. Dat is volgens de KAART-tekst in orde, maar ik zag de code niet. | Vermoeden | Midden | Gratis versie zonder verwijzing naar de betaalde (3.3, 3.10, 6.1) |
| 3 | Geen persoonsgegevens, sleutels of wachtwoorden in KAART.md. Over de beelden kan ik niets zeggen. | Feit voor KAART.md | Hoog | Geen persoonsgegevens |
| 4 | De KAART-regel noemt "Keuring Daan gevraagd" en geeft geen eigen cijfers of beweringen die een GEZIEN/DERDEN/GOK-label nodig hebben. | Feit | Hoog | Cijfers met label |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een vraag om een beoordeling direct na een Good fit komt op het goede moment. Als de regel bij elke plaatsing blijft staan, wordt hij na 30 seconden storend. | Alleen tonen na de eerste Good fit, of met een knop om hem weg te klikken. | Klein |
| 2 | Of "Figure from rig" bovenaan het paneel prettig is, kan ik niet zien. | Het beeld `rig-boven.png` bekijken. | Klein |

## Deel C: is het goed genoeg?
Cijfers 1 tot 10 kan ik niet geven. Ik zag de drie beelden niet en ik kan geen concurrent ernaast leggen. Het zijn keuringsbeelden van het paneel, geen winkelbeelden. De blinde test is dus niet van toepassing. Voor het uitbrengen van 1.2.9 moeten Daan en Iris de beelden bekijken.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen voor deze wijziging.

**Kan:**
- Het runnummer van de e2e bij de commit of in de KAART-regel zetten.
- Het beoordelingsverzoek niet bij elke plaatsing tonen (zie deel C, punt 1).
- `architectuur.md` bijwerken bij het samenvoegen van de tak.
- Voor Pro 1.2.9 uitbrengen: opnieuw laten keuren met de paneelcode en de beelden erbij, en met het akkoord van Daan (#83) in `ontwerp.md`.

---
Automatische keurder, model `claude-sonnet-5-5`, 18577 tokens in, 3179 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
