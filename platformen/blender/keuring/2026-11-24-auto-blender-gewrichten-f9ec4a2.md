# Keuring blender-gewrichten Pro 1.2.4 (Figure from rig, reden van de eerste plek), 24-11-2026 08:01 NL, automatische keurder
Wat ik keurde: commit f9ec4a22f (65219c0..f9ec4a2): `click_joints/betaald/rig.py` en `e2e/toetsen_rig.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
Opdracht: de commitbeschrijving. In Figure from rig moet de reden van de eerste plek winnen als daar de snede misging (rechterknie kleding, 4.2). `ontwerp.md` zegt hierover niets.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `reden_eerste` kiest de melding van de eerste kandidaat als die één van de drie snedefrasen bevat, anders de laatste. De nieuwe test dekt beide takken, ook met lege invoer (`None`). | Feit | Hoog | De diff en de toetsregels in `toetsen_rig.py`. |
| 2 | Na de nieuwe regel staat nog `if not ok and vangnet: melding = vangnet`. Heeft de rechterknie een `vangnet`, dan wint die alsnog van de nieuwe reden en blijft de lijst de verkeerde reden tonen. | Vermoeden | Midden | Een run op het kleding-figuur in 4.2 (de run van de bug was 45295977807) waarin de rechterknie "overlap before they move" toont. Of: `vangnet` is bij die knie leeg. |
| 3 | De drie frasen in `SNEDE_MIS` komen uit de testzinnen die de bouwer zelf schreef. De echte meldingen uit `figuur.plaats_gewricht` zie ik niet. Wijkt de echte tekst af, dan doet de fix niets. | Vermoeden | Midden | Een `grep` op die drie frasen in `figuur.py`, of een run met de echte melding. |
| 4 | `eerste_kand` wordt alleen bij `i == 0` gezet, dus alleen bij de eerste plek. Dat past bij wat de commit zegt. | Feit | Hoog | De diff. |
| 5 | In de wijziging staat geen groene run na de fix. De tests toetsen alleen de losse functie, niet de operator met een echt figuur. | Feit | Hoog | Een groene e2e-run op het kleding-figuur. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De test is toegevoegd en geen bestaande test is aangepast. | Feit | Hoog | Tests niet aangepast om te slagen: ok. |
| 2 | `rig.py` is al ruim boven de 400 regels: de hunks beginnen op regel 696 tot 792. De wijziging maakt hem 17 regels langer. | Feit | Hoog | Bestanden onder ±400 regels. Oude schuld, dus een kan. |
| 3 | `architectuur.md` is niet bijgewerkt, terwijl de volgorde van meldingen bij Figure from rig verandert. | Feit | Hoog | architectuur.md bijgewerkt. |
| 4 | Het versienummer 1.2.4 staat alleen in een commentaar. Een versieverhoging in het manifest of de Pro-changelog zit niet in deze wijziging. | Vermoeden | Laag | Of het in een andere commit staat, bijvoorbeeld bij het uitbrengen. |
| 5 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. De spelerstekst blijft Engels en is niet door Hats gemaakt. Er zijn geen AI-beeld of -geluid. | Feit | Hoog | Persoonsgegevens, Hats-tekst en Steam-regel: ok. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik kan niets zien of spelen. Dit volgt alleen uit de tekst.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De reden "The parts overlap before they move" zegt de gebruiker niet wat hij moet doen. | Voeg een tip toe, bijvoorbeeld "place it by hand a bit further along the limb". | Klein |
| 2 | Een gebruiker die de reden van de eerste plek ziet, probeert vermoedelijk dezelfde plek opnieuw. | Noem in de lijst ook de plek waar de snede misging. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer of `vangnet` de nieuwe reden niet overschrijft (A2), met een run op de rechterknie van het kleding-figuur in 4.2.
- Controleer of de drie frasen in `SNEDE_MIS` letterlijk in de echte meldingen van `figuur.py` staan (A3).
- Werk `architectuur.md` bij met de nieuwe meldingsvolgorde (B3).
- Splits `rig.py` ooit op, want het is ver boven de 400 regels (B2).
- Zorg dat het versienummer 1.2.4 en de Pro-changelog bij het uitbrengen kloppen (B4).

---
Automatische keurder, model `claude-sonnet-5-5`, 19277 tokens in, 3220 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
