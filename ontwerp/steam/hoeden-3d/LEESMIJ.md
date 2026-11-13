# Hoeden in 3D, versie 2 (Daan, 13 nov 2026)

Waarom: keuze A van Bram (13 nov 19:25). In het spel krijgt elke held een willekeurige hoed uit 10, en precies die hoed gaat op Gloops toren. De bonte toren van gegeten hoeden is de grap van het spel en het winkelplaatje, dus de hoed hoort bij de held die binnenkomt en niet bij de soort.

Wat er staat:
- `producten/steam-hol/modellen/hoeden.py`: alle 10 hoeden, in de volgorde en kleuren van `held.gd` en `kunst/held_hoeden.png` (helm, puntmuts, kap, pet, kroon, koksmuts, emmer, hoge hoed, pan, veermuts). Als module: `hoeden.bouw(nr, plek, schaal, kantel)`, plek is het midden van de onderrand. Alle objecten heten `hoed_<naam>_...`.
- `producten/steam-hol/modellen/held.py`: de helm van de ridder en de heksenhoed van de heks heten nu `hoed_helm_...` en `hoed_heksenhoed_...`. Met `HOL_VERBERG ["hoed"]` rendert de pijplijn een held zonder hoed. Zonder HOL_VERBERG is het beeld hetzelfde als eerst.
- `hoeden-v1.png`: de 10 naast elkaar.
- `helden-met-hoed-v1.png`: ridder en heks om en om, elk met een andere hoed op de kruin (gemaakt met `proef/helden_met_hoed.py`: held zonder hoed, hoogste punt van het hoofd zoeken, hoed 0,06 lager zetten).
- `helden-met-hoed-v1-55px-4x.png` en `-16px-8x.png`: zelfde beeld op ware grootte (55 px is het blad, 4 keer zo scherp als een spelpixel; 16 px is één spelpixel per beeldpunt).

Eigen oordeel: op 55 px is elke hoed meteen te herkennen aan kleur en vorm, en de heks blijft een heks zonder punthoed (oranje jurk, bezem). Op 16 px blijft alleen de kleur over; die is per hoed verschillend genoeg (wit, groen, goud, rood, blauw, zwart). Kap kreeg in ronde 1b een grotere slip, want zonder slip las hij als groene koepel. De emmer had een hengsel dat als ring om het gezicht hing; nu twee oortjes.

Voor Bram bij het tekenen (moet): de onderrand van de hoed 1 spelpixel ín de kruin, nooit erboven (zwevende hoeden lazen in elke ronde als fout). Bij de stand vallen tuimelt de hoed los van de held. Moet (ronde 2): teken de hoed op `schaal` 1,3 tegenover de held (in de proef `HOED_SCHAAL=1.3`); de hoed is het verhaal van het spel en mag groter zijn dan echt, zoals de pixelhoeden van nu.

Nog niet: dezelfde hoeden op Gloops toren in `gloop.py` (nu 4 eigen hoeden, zelfde vorm voor helm, puntmuts en kroon); dat doe ik als Bram de tekenkant heeft, zodat Mila's `hol.py` niet onverwacht verandert.

## Ronde 2 (±19:40 UTC)
Frisse kijker op versie 1: aantrekkelijk 7, leesbaar op ware grootte 5. Niet te lezen: emmer (leek een oranje pan), pan (zwarte bolhoed met stokje), pet (verdween in het rode haar van de heks). Advies: hoeden 1,3 tot 1,5 keer groter, elk een eigen silhouet en kleur. Gedaan: alle hoeden op 1,3 in de proef, emmer hoger met lichte duigen en donkere banden, pan met de steel schuin omhoog en een glans, pet feller rood met witte band en knoop en de klep opzij naar voren. Eigen oordeel op `helden-met-hoed-v2-55px-4x.png`: alle 10 nu te noemen, de pan het zwakst maar wel een pan. `hoeden-v2.png` is het blad op schaal 1. Donkere omlijning (ook geadviseerd) doe ik niet: de 3D-stijl werkt met licht en kleur, niet met lijnen (`3d-stijl.md`).
