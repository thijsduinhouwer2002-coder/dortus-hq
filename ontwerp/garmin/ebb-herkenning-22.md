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
