# Schermafbeeldingen uit de 3D-build (keus Mila, 14 nov 2026)

Uit Olafs voorstel (`producten/steam-hol/bewijs-winkel3d/schermen-3d-voorstel/`), met één verschil: scherm 1 en 2 komen uit de nieuwere weekopname waarin de Royal-cape in 3D staat (geen pixelstukken meer). Script en snedes gelijk: `ontwerp/steam/winkelpagina/bron/maak_schermen2.py`. Niets bijgetekend.

| Scherm | Opname | Snede |
|---|---|---|
| 1 hoedentoren | week 160, run 43590467908 (main ac54d3d), beeld 395 | `zoom 1146 3` |
| 2 bureaublad | zelfde beeld | `rustig` |
| 3 wrok | demo 160, run 43580204621 (main 99a56ab), beeld 1100 | `zoom 1146 3` (Olaf) |
| 4 kaartje | demo, beeld 285 | `zoom 1690 3` (Olaf) |
| 5 ontmoeting | demo, beeld 770 | `zoom 1146 3` (Olaf) |

- **Besluit: scherm 1 opnieuw uit de Royal-3D-opname.** Waarom: in Olafs scherm 1 waren cape, zoom en ster nog pixels; het eerste scherm is wat iedereen ziet, dat moet helemaal 3D zijn. GEZIEN met Read: troon met rode cape en goud, hoedenberg, schat, geen pixelster. Nog een klein pixelrestje: de munt en de plank helemaal links in scherm 1.
- Volgorde: hoedentoren eerst (de haak), dan bureaublad (hoe het op je scherm ligt), dan het verhaal (wrok, kaartje, ontmoeting).
- Open: de zoomschermen zijn voor ±60% avondlucht; de strook zit onderaan. Zo staat hij echt op je bureaublad (eerlijk), maar op Steam is het eerste scherm klein; een volgende ronde kan de snede lager leggen (minder lucht) als Daan dat op leesbaarheid ook vindt.
- Daan keurt op fouten en leesbaarheid. `overzicht.png`: alle vijf.

## 14 nov ±14:50 UTC (Mila): put in 3D, proef minder lucht
- Scherm 1 en 2 overgenomen uit Olafs `producten/steam-hol/bewijs-winkel3d/schermen-3d-put3d/` (week 160, run 43599002529, main 18e2253, beeld 395, zelfde snedes). Nagemaakt met mijn script op hetzelfde beeld: scherm 1 is bit voor bit gelijk. Links staat nu de 3D-stekelput met het koopmuntje, geen pixelplank meer.
- Nog een pixelstuk: de donkere plank onder de troon. Olaf haalt die weg (tak `claude/steam-hol-put-schat`, wacht op Daan); daarna scherm 1 en 2 nog één keer uit een nieuwe weekopname.
- **Proef voor Daans kan (b), minder lucht:** `proef-scherm-1-zoom4.png` (`zoom 1146 4`). De strook is dan 59% van het beeld en Gloop met toren ±1,3 keer zo groot. GEZIEN met Read. Wat je verliest: de oranje avondlucht (de mooiste kleur van het scherm), de stekelput links valt eruit, en het beeld wordt zachter (de opname is 160 px hoog, 4 keer vergroot). `zoom 1082 4` houdt de put erin maar snijdt Gloop aan de rand af.
- **Besluit: scherm 1 blijft voorlopig `zoom 1146 3`.** Waarom: op 3x zie je in één beeld put, hoedenberg, Gloop op de troon en schat, met de avondlucht als kleur; 4x wint grootte maar verliest scherpte en verhaal. Bij de volgende opname (zonder plank onder de troon) leg ik beide nog eens naast de toppers op Steam-formaat (600 breed) en kies dan definitief.

## 14 nov ±20:55 UTC (Mila): scherm 1 in twee rijen (moet Daan 18:33)
- **Nieuw `scherm-1-hoedentoren.png`:** twee uitsneden uit één echt beeld, `bron/opnames/week160-run43632673538-f400.png` (week 160, run 43632673538, main b99f137, beeld 400). Script `bron/maak_scherm_twee_rijen.py <opname> 562,989 1060,1920 <uit>`. Niets bijgetekend.
  - Boven (4,5x): held Bram met heksenhoed slaapt (zz-wolkje) naast het web met de spin, de stekelval met munt ernaast.
  - Onder (2,2x): hoedenberg, Gloop op de troon, schat, en het kroniekkaartje heel: "Bram snored. Gloop watched."
  - De rijen sluiten op 4 px aan, dus geen donkere band; het leest als twee verdiepingen van het hol.
- **Waarom dit moment:** de grap staat er twee keer in, in beeld (held slaapt in jouw val-gang) en in tekst (Gloop kijkt toe). Bij Daans proef (beeld 395 van de vorige run) was het kaartje half; hier is het heel en zie je waarom het grappig is.
- **Frisse kijker** (agent, op 600 breed naast Rusty's): oud 4, nieuw 6,5. Moet "donkere band leest als plakfout": verwerkt (rijen sluiten aan, band 157 naar 4 px). Moet "Gloop afgesneden": klopt niet, de hoedenberg en troon staan heel (1:1 uitgesneden en GEZIEN), maar Gloop is klein; dat is de prijs voor het hele kaartje. Kan "bureaublad zien": dat doet scherm 2.
- Vergelijking op 600 breed: `vergelijk-scherm1-twee-rijen-600.png` (Rusty's 1 en 2, oud, nieuw). GEZIEN met Read: de grap leest op 600 breed, elk stukje beeld is spel.
- Bewust niet: stukken van de strook die niet naast elkaar liggen tegen elkaar plakken om Gloop groter te krijgen. Dat zou een hol tonen dat er zo niet is.

## Scherm 2: echt bureaublad, wacht op Olaf
- Bekeken: de 6 bureaubladbeelden van run 43632673538. Werkt, maar nog niet klaar voor de winkel: Godot-robotje en knipperende knop in de taakbalk (moets van Daan aan Olaf), Kladblok te groot en wit, strook maar 15% van het beeld (op 600 breed 50 px hoog, te klein om iets te zien).
- Proef `proef-scherm2-bureaublad-ingezoomd.png`: rechtsonder 1440x810 uit beeld 6, 1,33x vergroot. Strook en echte taakbalk lezen dan wel ("Lotte picks the lock. It was open."), maar het lege Kladblok vult de helft.
- **Wens aan Olaf** (in `platformen/steam/taken.md`): opname op 1280x720 (strook 22% van het beeld, alles wat groter, zoals bij Rusty's), Kladblok klein linksboven, snelkoppelingen R en Unity Hub weg; ik vergroot naar 1920x1080. Dan kies ik scherm 2.
