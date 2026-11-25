# Keuring blender-gewrichten Pro 1.2.8 (keurder-moet 239b063), 25-11-2026, automatische keurder
Wat ik keurde: commit 2fd492586 (5a8b641..2fd4925), bestanden `KAART.md` en `architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De wijziging is alleen tekst. Er is geen code of add-on veranderd. Ik toets haar aan de belofte in de commit: "keuringen met bron op de kaart, sha256 in note, CI-piek 4614 MB in architectuur".

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De kaart noemt nu per keuring de bron: Daan #11, #29 en #37, met de twee keuringsbestanden en de commit 102972b voor moet 1. | Feit (staat in de diff) | hoog | Of die bestanden bestaan en dit zeggen: `platformen/blender/keuring/2026-11-24-pro-1.2.8-tekst-daan.md` en `...2026-11-25-pro-1.2.8-m1-m2.md`. |
| 2 | De sha256 `c3daa159...e4af` staat op de kaart. In deze diff staat hij niet in de note `platformen/blender/pro-1.2.8.md`. | Vermoeden dat hij daar ook staat | midden | Een `grep` op de hash in de note, en `sha256sum` van de zip uit run 45526260663. |
| 3 | In architectuur staat de CI-piek 4614 MB op 4.2.23 (run 45526260663), naast de lokale piek van ±2,5 GB. De marge tot de grens van 6000 MB is ±1,4 GB, en 6000 min 4614 is 1386, dus dat klopt. | Feit voor de rekensom. De meting zelf is door de schrijver als GEZIEN gemerkt. | midden | Het log van run 45526260663, stap Rigify-figuur. |
| 4 | De kaart zegt eerlijk dat het laatste ja op uitbrengen en de regel in `ontwerp.md` nog bij Daan liggen (#47). `ontwerp.md` heeft nog geen ja voor 1.2.8, dus uitbrengen is nog niet toegestaan. | Feit | hoog | Een ja van Daan in #47 en een nieuwe regel bovenaan `ontwerp.md`. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen test is aangepast. Er zijn geen codebestanden gewijzigd. | Feit | hoog | Tests niet aanpassen om te slagen |
| 2 | Cijfers dragen een label: 4614 MB, ±2,5 GB en sha256 zijn GEZIEN. De blinde-testcijfers (Gumroad 1,0 en 1,0, Superhive 2,0 en 1,5) staan zonder label, alleen met verwijzing naar een uitslagbestand. | Feit | midden | Cijfers met GEZIEN/DERDEN/GOK |
| 3 | `architectuur.md` is in de diff niet af te meten, maar de regels zijn extreem lang (één regel is een hele alinea). Of het bestand onder ±400 regels blijft, kan ik niet zien. | Vermoeden | laag | Bestanden onder ±400 regels |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de diff. De Gumroad-link bevat een winkelnaam, geen gegevens van een klant. | Feit | hoog | Geen persoonsgegevens |
| 5 | `architectuur.md` is bijgewerkt met de CI-piek. | Feit | hoog | architectuur.md bijgewerkt |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Niet van toepassing: er is niets om te zien of te spelen. Het zijn interne notities. | n.v.t. | klein |

## Deel C: is het goed genoeg?
| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeken |
|---|---|---|
| Ziet het er top uit? | n.v.t. | Geen beeld, video of winkeltekst in deze wijziging. De blinde test van het hoofdbeeld en de winkeltekst staat vermeld als GESLAAGD. Die uitslagbestanden heb ik niet gezien. |
| Zou ik het zelf kopen of bekijken? | n.v.t. | Idem. |
| Zou Thijs er trots op zijn? | n.v.t. | Idem. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet bij de blinde-testcijfers op de kaart een label (GEZIEN of DERDEN), zoals bij de andere cijfers.
- Controleer dat de sha256 echt in de note `pro-1.2.8.md` staat (zie A2).
- Pas de kop "Klaar om te plakken" aan. Die suggereert dat alles klaar is, terwijl het laatste ja van Daan (#47) nog ontbreekt. Bijvoorbeeld: "Klaar om te plakken, wacht op ja Daan #47".
- Splits `architectuur.md` als het bestand over ±400 regels gaat.

---
Automatische keurder, model `claude-sonnet-5-5`, 24218 tokens in, 3460 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
