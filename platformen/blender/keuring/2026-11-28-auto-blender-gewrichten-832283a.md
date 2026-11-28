# Keuring blender-gewrichten, kogel na Shift + rechtsklik (#410), 28-11-2026, automatische keurder
Wat ik keurde: commits 17d4ed5..832283a (832283ae2), alleen de tekst van de wijziging
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Bij een cursor op de huid en as-bron View direction schuift `kogel_bijstellen` het punt naar het midden. De as wordt de lidas als het lid in het schermvlak ligt, anders blijft het de kijkrichting. Dat past bij wat #410 beschrijft. | Feit (code gelezen) | hoog | Groen e2e-log van `toetsen_kogel_huid.py` in 4.2 en 5.3. |
| 2 | De cijfers uit de KAART (arm 60 x 36 x 36, been 42 x 42 x 91, Good fit, lokaal 0 FOUT) kan ik niet nalezen. Er staat geen log of run-id bij. | Vermoeden | midden | Run-id of log van 5.3.0 met deze toets. |
| 3 | De toets dekt alleen een rechte staaf langs +X met kijk +Y. Shoulder en Hip testen daardoor dezelfde geometrie. Neck, een hangende arm en een been staan niet in de toets. | Feit | hoog | Een toets met een figuur met hangende arm en staand been. |
| 4 | De richting van de lidas wordt omgedraaid via "van het midden van het kader naar het punt". Bij een verticaal lid, zoals een hangende arm in A-pose of een been rond heuphoogte, kan dat verkeerd uitvallen. Deel B zou dan de romp zijn in plaats van het lid. | Vermoeden | laag tot midden | Shoulder en Hip op een A-pose-figuur: is deel B het lid? |
| 5 | Met de cursor binnen het figuur en een vooraanzicht blijft het voor-achter-snijden met Good fit bestaan. De architectuur noemt dit zelf en zegt "apart issue", maar er staat geen issuenummer bij. | Feit | hoog | Een nummer van dat issue in de KAART. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De toets is nieuw en er is geen bestaande toets aangepast. Er zijn drie checks bijgekomen in `test_betaald.py`: omhullen, aan en uitzetten. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` en `KAART.md` zijn bijgewerkt met de nieuwe module, de omhulling en de bekende beperking. | Feit | hoog | architectuur.md bijgewerkt |
| 3 | De gratis code blijft gelijk, want de omhulling zit in `betaald/` (`register` en `unregister` met een terugzetcontrole). | Feit | hoog | Twee builds uit één bron |
| 4 | Bestandsgrootte: de nieuwe bestanden zijn klein (84 en 90 regels). `cursor_lid.py` groeit met 57 regels, maar de totale lengte zie ik niet. | Vermoeden | midden | Bestanden onder ±400 regels |
| 5 | De GEZIEN-claims (xvfb, 5.3.0, lokaal) staan in de KAART zonder run of log. Ik kan ze niet zelf bevestigen. | Vermoeden | midden | Cijfers met GEZIEN, DERDEN of GOK |
| 6 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. De naam "Iris" staat alleen als bron van het issue. | Feit | hoog | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Zonder schermen of spel kan ik alleen redeneren: een kogel die na één Shift-klik meteen goed zit is voor de koper veel fijner dan "Too thin". Niet gezien. | Iris of Daan laten nadoen met een echte figuur. | klein |
| 2 | De melding "Cursor on the surface: joint axis along the limb and centred in the limb." is technisch. | Een kortere zin, bijvoorbeeld "Moved to the middle of the limb." | klein |
| 3 | Niet gekeken of Ctrl+Z na zo'n bijgestelde plaatsing het punt weer terugzet. | In `toetsen_kogel_huid.py` na het plaatsen undo toetsen. | klein |

## Deel C: is het goed genoeg?
Er is geen beeld en geen winkeltekst in deze wijziging en ik heb niets gezien of gespeeld. Ik geef daarom geen cijfers en vergelijk niets met een concurrent. Dit hoort bij Iris en Daan op een echte figuur. Er is geen blinde test nodig, want er is geen eerste-indrukbeeld.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Toets uitbreiden met een hangende arm, een staand been en Neck, om de omkeerregel met het midden van het kader te bevestigen of te weerleggen (A4).
2. Run-id of log bij de GEZIEN-claims in de KAART zetten (A2 en B5).
3. Een issuenummer geven aan "cursor binnen het figuur snijdt voor-achter" (A5).
4. De melding korter en in gewone woorden maken (C2).
5. Meten of de extra BVH op een figuur van ±200K driehoeken de 5 seconden uit het ontwerp niet raakt. Dat is niet getoetst.
6. Bij de uitgave: versienummer en changelog van Pro 1.2.10 bijwerken. Die staan nu niet in de wijziging.

---
Automatische keurder, model `claude-sonnet-5-5`, 31302 tokens in, 5656 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
