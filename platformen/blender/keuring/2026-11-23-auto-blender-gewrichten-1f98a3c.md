# Keuring blender-gewrichten, Figure from rig kogel_schuif, 23-11-2026, automatische keurder
Wat ik keurde: commits bac754e..1f98a3c (6dcadc823 en 08d1637ab): `click_joints/betaald/rig.py`, `architectuur.md` en `proeven/studio2-figuren-2026-11-23/uitslag.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging voegt één laatste kandidaatplek toe (dezelfde plek 0,3 mm verder het lid in), alleen met een voorwaarde op de lengte. Een figuur waar het eerste voorstel al lukte, merkt niets. | Feit (diff) | Hoog | Niet nodig. |
| 2 | Het doel is dat de robot in CI en lokaal evenveel gewrichten krijgt (9 en 9). De uitslag zegt dat dit zo is, met runnummers. | Feit dat het zo beschreven staat, vermoeden dat het klopt | Midden | De logs van runs 45206324187 en 45208410893 in `organisatie/actions-logs/`. Ik kon ze niet openen. |
| 3 | In de diff staat niet waar `t_vrij` vandaan komt, alleen `t_oud` en `t`. Als het niet eerder in de functie bestaat, geeft dit een NameError. | Vermoeden | Laag | Een groene run met 9 gewrichten (staat in de uitslag) weerlegt het. Ook de volledige functie lezen. |
| 4 | `architectuur.md` zegt dat de knop alleen bij "too close", "no watertight parts" en (scharnier) "too thin"/"tight" een volgende plek probeert. De robot kreeg "it would be blocked", en die staat niet in de lijst. Het blijft onduidelijk waarom de extra plek dan wél helpt. | Vermoeden | Midden | Een zin in de architectuur over hoe de terugdraaiing na de beweegproef de volgende kandidaat start. Of de code van de herkansing. |
| 5 | Het akkoord in `ontwerp.md` dekt de gratis 0.1.1 en Pro 1.0.2. Dit is Pro 1.2.0 (Figure from rig). In het stuk dat ik zag staat geen akkoord voor 1.2.0. | Vermoeden (het ontwerp is afgekapt) | Laag | Een akkoordregel voor Pro 1.2.0 elders in `ontwerp.md`. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast of verzwakt. Er is ook geen nieuwe test voor deze fix gekomen. | Feit (diff) | Hoog | Tests niet aangepast om te slagen: ok. |
| 2 | `architectuur.md` is bijgewerkt met `kogel_schuif`, de reden en de runnummers. | Feit | Hoog | architectuur.md bijgewerkt: ok. |
| 3 | De uitslag gebruikt GEZIEN, GOK en "loopt", ook voor de processorverklaring ("GOK: andere processor"). Alleen de kop van de sectie "De robot: waar het verschil zit" noemt nog "CI-meting loopt", terwijl die verderop klaar is. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK: ok, met een verouderde kop. |
| 4 | Bestandslengte van `rig.py` en `architectuur.md` is uit de diff niet te zien. De regels in `architectuur.md` zijn wel zeer lang. | Vermoeden | Laag | Bestanden onder ±400 regels: te controleren met `wc -l`. |
| 5 | Geen persoonsgegevens, sleutels of wachtwoorden in de bestanden. Er staan alleen processortypes (AMD EPYC, Intel Xeon). | Feit | Hoog | Geen persoonsgegevens: ok. |
| 6 | De figuren zijn eigen werk of Quaternius-modellen (Stan, Mike, George, Cyberpunk). De licentie staat niet in de uitslag. | Vermoeden | Laag | Alleen testfiguren (CC0 of zelfgemaakt) volgens het ontwerp. Ik kan de licentie niet zien. |

## Deel C: zou een gebruiker het leuk en fijn vinden? (alles wat je kunt zien of spelen)
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De fix is een herkansing op goed geluk: één schuif van 0,3 mm. Op een andere processor of figuur kan ook de tweede plek kapot zijn, en dan mist de koper een heup zonder duidelijke reden. | Probeer meer kleine schuiven (bijvoorbeeld 0,3 en 0,6 mm). Of controleer direct na elke snede of de delen in rust overlappen, in plaats van pas bij de beweegproef. | Midden |
| 2 | De koper ziet niet dat een eerste plek kapot was. Hij ziet alleen een eindtal. Op een machine met afwijkende uitkomst is een gewricht dan 0,3 mm anders geplaatst, zonder uitleg. | Eén regel in de samenvatting als een plek is verschoven ("Left hip moved 0.3 mm"). | Klein |
| 3 | Kopers met een AMD-pc krijgen volgens de uitslag vaker hetzelfde probleem. Er is geen test op een tweede processor naast de CI-run. | Laat de studio-figuren vaker in CI draaien, zodat een verschil per processor opvalt. | Midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Voeg een toets toe die de nieuwe kandidaat afdwingt, vergelijkbaar met `CJ_HERKANS=1`. De fix is nu alleen getoetst via de studio-run.
- Leg in `architectuur.md` uit waarom "blocked" tot een volgende plek leidt, of voeg die melding aan de lijst toe.
- Haal "CI-meting loopt" uit de kop van de uitslag.
- Controleer `t_vrij` in de volledige functie, en de regelaantallen van `rig.py` en `architectuur.md`.
- Pak het open punt "Mike: linkerelleboog wel, rechter niet" op, want het staat nog als "niet nagekeken".
- Kijk of er een akkoord nodig is voor Pro 1.2.0 en zet het in `ontwerp.md`.

---
Automatische keurder, model `claude-sonnet-5-5`, 22683 tokens in, 4016 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
