# Ebb: herkenningstoets van de overige 22 dieren (Mila, run 55, 12 nov)

Opdracht hoofdchat 07:25: frisse kijker, alleen het 260-beeld, per dier "herkend ja of nee" in één tabel; wat nee is krijgt een nieuwe grap.
Werkwijze: de 22 beelden `werelden5/<dier>-in-dag-260.png` blind hernoemd naar 01 tot 22 (geen namen in de bestandsnaam), op twee bladen op ware grootte (`herkenning/blad1.png`, `blad2.png`). Eén losse agent, niets voorgezegd. GEZIEN door de keurder; de sleutel heb ik er daarna naast gelegd.

| Nr | Dier (echt) | Gezien als | Dier herkend | Grap (bedoeld) | Grap gezien | Grap herkend |
|---|---|---|---|---|---|---|
| 01 | zeekomkommer | "groen stekelig dier, krokodil of zeekomkommer?" | nee | slaapt in bootje | slaapt, slaapmuts, zzz | ja |
| 02 | dolfijn | dolfijn | ja | duikbril en snorkel | idem | ja |
| 03 | aal | "groene gevlekte langwerpige vorm" | nee | lampje (elektrisch) | "lampje, idee" | nee |
| 04 | vis | oranje vis | ja | flessenpost | idem | ja |
| 05 | kwal | kwal | ja | paraplu in de regen | idem | ja |
| 06 | kreeft | kreeft | ja | tuinier met strohoed | hoed ja, spullen niet | half |
| 07 | manta | "rog of manta (of haai)" | half | spandoek met hart | idem | ja |
| 08 | narwal | narwal | ja | ijsje op de slagtand | idem | ja |
| 09 | octopus | octopus | ja | in bad met eendje | idem | ja |
| 10 | orka | orka | ja | strikje, zingt | idem | ja |
| 11 | zeeotter | zeeotter | ja | schelp met parel op de buik | te klein, rommelig | nee |
| 12 | kogelvis | kogelvis | ja | ballon aan een touwtje | touwtje lijkt pootjes | nee |
| 13 | rog | "olijfgroene ruit?" | nee | ufo met lichtstraal | ufo, verder onduidelijk | nee |
| 14 | zeepaardje | zeepaardje | ja | draaimolenpaardje | "eerst kapperspaal" | half |
| 15 | zeehond | zeehond | ja | vist met hengel | idem | ja |
| 16 | haai | haai | ja | tanden poetsen | idem | ja |
| 17 | garnaal | garnaal | ja | surfplank | idem | ja |
| 18 | inktvis | inktvis | ja | eilandje met palm | "op vakantie?" | nee |
| 19 | zeester | zeester | ja | telescoop | idem | ja |
| 20 | maanvis | "haai of dolfijn" | nee | zonnebril | idem | ja |
| 21 | zwaardvis | zwaardvis | ja | donut-zwemband | idem | ja |
| 22 | walvis | walvis | ja | regenboog uit het spuitgat | idem | ja |

**Telling:** dier herkend 17 van 22 (nee: zeekomkommer, aal, rog, maanvis; half: manta). Grap herkend 15 van 22 (nee: aal, otter, kogelvis, rog, inktvis; half: kreeft, zeepaardje).

## Nieuwe grap of aanpassing voor wat nee is (regel: één groot voorwerp, niets wat de sticker zelf moet doen)
| Dier | Probleem | Nieuw |
|---|---|---|
| zeekomkommer | dier niet herkend | **spa-dag: twee plakjes komkommer op zijn ogen** en een handdoekje op zijn kop. De woordgrap zegt meteen welk dier het is. Slapen in het bootje vervalt. |
| aal | dier en grap niet herkend | **stekker in de bek** (grote witte stekker met snoer dat in een kronkel om hem heen loopt): een elektrische aal. Lijf langer en slanker, als een snoer. |
| rog | dier en grap niet herkend | **de rog is een vlieger**: ruit van zijn lijf, staart met drie strikjes, een touwtje naar beneden. De vorm van de rog wordt de grap; ufo vervalt. |
| inktvis | grap niet herkend (vijfde keer) | **schrijft met zijn eigen inkt**: een grote ganzenveer in een tentakel en een inktpotje. Inktvis = inkt. Eilandje vervalt. |
| zeeotter | grap te klein | **drijft op zijn rug met een grote kop warme chocolademelk op zijn buik** (zijn buik is een tafel), wolkje stoom. Eén groot voorwerp in plaats van schelp plus parel. |
| kogelvis | touwtje leest als pootjes | **luchtballon**: de opgeblazen kogelvis is de ballon, eronder een rieten mandje aan vier dikke lijntjes. Mandje groot en bruin, los van het lijf. |
| kreeft | spullen naast hem lezen niet | alleen strohoed en **één grote gieter** in zijn schaar; bloempot weg. |
| zeepaardje | paal lijkt kapperspaal | paal **goud in plaats van rood-wit**, met bovenop een rond dakje met stippen (draaimolen). |
| manta | twijfel rog of haai | manta donker van boven met witte buikvlekken en de twee hoornlobben bij de bek duidelijker; spandoek blijft. |
| maanvis | dier niet herkend | lijf hoger en ronder, geen staart maar de afgeknotte achterrand, zonnebril blijft (de grap leest al). |

Volgende stap: de familie-agents tekenen deze tien opnieuw, daarna weer een blinde toets op 260 met een nieuwe kijker.

## Ronde 2 (dezelfde run): tien dieren opnieuw getekend en blind getoetst
Drie familie-agents tekenden de tien nieuwe grappen (scripts `bron/werelden_v4_huisjes.py`, `_vliegers.py`, `_koud.py`, `_strand.py`, `_licht.py`; beelden `werelden4/`, en `werelden5/` opnieuw gemaakt met `werelden_v5_lucht.py`). Alle drie melden contrast 4,5 of hoger en 0 regels te dicht (6/260). Nieuwe blinde kijker, genummerd 01 tot 10 in een andere volgorde, boven en onder water (`herkenning/ronde2-boven.png`, `ronde2-onder.png`). GEZIEN met Read: het blad boven water.

| Dier | Gezien als | Dier | Grap gezien | Grap |
|---|---|---|---|---|
| inktvis | inktvis, "schrijft met zijn eigen inkt" | ja | ganzenveer en inktpotje | **ja** (was nee) |
| zeeotter | zeeotter met rode mok en stoom | ja | warm drankje op zijn buik | **ja** (was nee) |
| rog | rog, "is een vlieger" | ja (was nee) | vlieger met strikjes | **ja** (was nee) |
| kogelvis | kogelvis als luchtballon met mandje | ja | luchtballon | **ja** (was nee) |
| zeepaardje | zeepaardje met parasol | ja | leest als parasol, niet als draaimolen | ja, maar een andere grap dan bedoeld |
| maanvis | "maanvis (mola)", twijfel | half (was nee) | zonnebril | ja |
| kreeft | kreeft, tuinman pas onder water | ja | boven water "strandspullen" | half |
| manta | manta met spandoek | ja (was half) | verband manta en doek niet duidelijk | half |
| zeekomkommer | "groene klodder", spa | half (was nee) | komkommerschijfjes klein | nee |
| aal | "aal of sidderaal" | half (was nee) | stekker en snoer klein en grijs | nee |

**Telling na ronde 2 (alle 22):** grap herkend 19 van 22 (was 15), dier herkend 19 van 22 (was 17).
Nog open voor de volgende run: zeekomkommer groter met de schijfjes als twee grote vlakken, aal met een witte of gele stekker en dikker snoer in een lichte kleur, manta met het spandoek vast aan zijn staart (touwtje zichtbaar) en onder water uitgerold, kreeft boven water met de gieter die gietend boven een plantje staat. Zeepaardje: parasol accepteren als grap (leest in een blik) of het dakje als draaimolen verduidelijken; ik kies parasol accepteren, want hij leest en het is één voorwerp.

## Ronde 3 (dezelfde run): de vier zwakste verbeterd
Zeekomkommer groter (onder water 56, boven water 42) met twee grote komkommerschijven en een groter roze handdoekje; aal met witte stekker, gele pinnen en een dik geel snoer; manta sleept het doek aan een geel touw (zoals een reclamevliegtuigje), onder water rolt het doek achter hem uit; kreeft giet met een groene gieter boven een plantje in een potje op een drijvend eilandje, emmertje weg. Contrast 4,5 of hoger, 0 te dicht. GEZIEN met Read: `herkenning/ronde3-vier.png` (boven en onder water op 260): alle vier lezen nu voor mij in een blik. Nog niet blind getoetst: eerste stap van de volgende run.

## Ronde 4 (run 56, 12 nov ±06:46 UTC): blinde toets van ronde 3 en van de schildpad zonder blad
Nieuwe kijker, genummerd, boven en onder water (`herkenning/ronde4-blind.png`).
| Dier | Gezien als | Grap | Gezicht |
|---|---|---|---|
| kreeft | kreeft, tuinman met gieter en plantje | **ja** | ja |
| schildpad (zonder blad) | schildpad, meeuw op zijn rug; onder water "zwemt gewoon" | half (boven ja, onder geen grap) | **ja** |
| manta | manta of rog met spandoek als reclamevliegtuigje; onder water "eerder een parasol" | half | nee |
| aal | paling of murene met een "zaklamp" | half (stekker leest als zaklamp) | ja |
| zeekomkommer | "onduidelijk, misschien zeekomkommer", spa | half | nee (gezicht weg achter de schijfjes) |

Uitkomst: kreeft klaar; het gezicht van de schildpad leest nu (dat was het punt van keuring 3). Open voor de volgende run: zeekomkommer met één schijfje op het oog en het andere oog open (gezicht blijft zichtbaar) en een herkenbare vorm (langwerpig, bobbels); aal met snoer dat duidelijk in een stopcontact of verlengsnoer eindigt, anders een andere grap; manta onder water los van het zand met het doek achter hem; schildpad onder water een eigen kleine grap zonder iets voor zijn gezicht (bijvoorbeeld de meeuw die boven het water te zien is, of niets: boven water draagt hij de grap).

## Ronde 5 (run 57, 12 nov ±07:00 UTC): drie halve dieren opnieuw, blind getoetst
Wat ik veranderde (scripts `bron/werelden_v4_huisjes.py` en `bron/werelden_v4_vliegers.py`, beelden `werelden4/` en `werelden5/` opnieuw gemaakt):
- **Aal: de stekker is weg, er komt een brandende gloeilamp in zijn bek** (gele peer met witte glans en acht stralen, grijze schroefvoet met ribbels naar de bek) en twee gele bliksempjes boven zijn rug. De stekker las als zaklamp; een peer met schroefvoet leest in een blik en zegt "elektrisch". Snoer weg. Onder water groter (maat 50 in plaats van 44).
- **Zeekomkommer: de plakjes gaan van zijn oog naar zijn rug** (drie op een rij), het oog en de glimlach blijven vrij, handdoekje blijft op zijn kop.
- **Manta: hij vliegt, hij staat niet.** Onder water hoger (166, 183, maat 37), schuin in een bocht (12 graden), schaduw ver onder hem op het zand, het doek hoog achter hem met drie belletjes. Ook op het eindscherm: doek achter hem in plaats van eronder (daar las het ook als parasol).
- Veilige zone nagemeten met `bron/toets_veilige_zone_ronde5.py` (tekstvakken opgemeten, held aan en uit vergeleken), alle zes schermen, dag en nacht, 260 en 454: **0 keer dichter dan 6/260 bij tekst.** Daarvoor zakte de manta 15, de bliksempjes zakten en de aal bij inademen 6 naar rechts (de lamp kwam te dicht bij de "12").

Blinde toets, nieuwe kijker, genummerd, alleen het 260-beeld (`herkenning/ronde5-drie.png` is het eindblad dag en nacht):
| Dier | Gezien als | Dier | Grap |
|---|---|---|---|
| aal | "sidderaal lijkt me het meest waarschijnlijk", lamp met stroom | half, beter | **ja**: "sidderaal die stroom maakt en een lamp laat branden" (was half) |
| manta | rog of manta, banner als reclamevliegtuigje | half | **ja**, boven en onder water; geen parasol meer (was half) |
| zeekomkommer | "misschien een zeekomkommer", spa | half | **ja**: "zeekomkommer met komkommers" |

**Telling na ronde 5 (alle 22): grap herkend 22 van 22.** Dier herkend: 19 ja, 3 half (aal, manta, zeekomkommer). Alle grappen tellen nu volgens de regel van 06:00.
**Besluit: hier stop ik met schaven aan deze drie.** Waarom: de grap leest bij alle drie; wat half blijft is het dier zelf, en dat zit in de sticker (de vorm staat als bytes in de app, `ebb-dieren-v83-data.json`), niet in de wereld. Op het eindscherm staat de naam erbij. Een nieuwe vorm voor drie stickers is een besluit voor de hele dierenset en hoort bij de echte schermen (besluit 03:10: de 8 meten we op het horloge).
Schildpad onder water: geen eigen grap, zijn grap is de meeuw boven water. Dat laat ik zo: liever geen grap dan iets voor zijn gezicht (dat was keuring 3).
