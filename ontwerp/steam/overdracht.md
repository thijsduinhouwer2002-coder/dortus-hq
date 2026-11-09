# Overdracht Steam (Het Hol): van Daan aan Mila

Geschreven 9 nov 2026, 20:30 UTC, op verzoek van Thijs (bericht 21:20 NL). Vanaf nu ben jij eigenaar van stijl en wow voor Het Hol. Ik keur alleen nog op fouten en leesbaarheid, en het eindakkoord voor indienen blijft bij mij (dat toets ik op fouten, niet op smaak). Alles hieronder mag je houden, verbouwen of weggooien; zeg in je logboek waarom.

## Wat vaststaat (en waarom)
- **Pixel art, cellen 16 x 16, schaal 3.** De strook is 120 px hoog = 40 spelpixels: maaiveld 8 plus twee rijen van 16. Waarom: op schaal 2 waren de figuren mieren naast Rusty's Retirement (GEZIEN, `kunst-bron/vergelijk-rusty.png`); schaal 3 is ook wat Olaf al bouwt. Thijs wil 100 tot 140 px, hoogte instelbaar.
- **Nooit schalen buiten hele getallen en altijd nearest.** Zodra iets in y of x wordt uitgerekt (zoals Gloop in de eerste build) is het een veeg.
- **Geen kaartjes over andere vensters.** Meldingen klein in de strook (`paneel.png`) of alleen bij eroverheen bewegen. Eis van Thijs.

## Wat ik maakte
Alles staat in `producten/steam-hol/godot/kunst/` (uitleg per bestand en de regels in `LEESMIJ.md` en `kunst.json`). De bron is code, zodat je kleuren en vormen in één keer kunt veranderen:
- `ontwerp/steam/kunst-bron/maak_kunst.py`: tegels, gangwand met mos en scheurtjes, maaiveld, gras, ingang met bordje, fakkel en `gloed.png`, schat, stekelput, versiering (stut, vaandel), held (lijf, hoeden, wapens), slijm in rust.
- `maak_karakter.py`: tunieken in 5 vaste kleuren per naam, 4 littekens als losse laag (pleister, ooglap, verband, hap uit de hoed), 5 tekens (boos, ster en meer), slijm slapen, laars spugen, hap, plat, opstaan, laars, `paneel.png` en `naamkaartje.png` als 9-slice, `trofee.png` voor de wand van aartsvijanden.
- `maak_aarde.py`: `aarde_lagen.png` (drie lagen op diepte, golvende laaglijn, graswortels) en `vondsten.png` (helm, zwaard, botten, fossiel, pot, 1 op 10).
- Voorbeeldbeelden op ware grootte: `kunst-bron/voorbeeld-strook.png`, `voorbeeld-karakter.png`, `voorbeeld-aarde.png`, `paneel-voor-na.png`, `atlas-groot.png`.
- Oudere stukken uit de ideefase (niet meer de richting, wel bruikbaar als sfeer): `hol-sfeer.png`, `scherm/` en `beeldtaal.md` (papieren theater, De Karavaan). Thijs vond die "armoedig"; gebruik ze niet als maatstaf.

## Waar de build staat
Mijn laatste keuring: `ontwerp/steam/keuring-build.md`, build 408d67b (run 42682511064). Oordeel: nog niet naar Thijs. Op volgorde: (1) Gloop wordt geschaald en is een veeg (Bram, `slijm.gd`), (2) alle helden zien er hetzelfde uit, littekens en kleuren nog niet ingebouwd (Bram, `held.gd`), (3) geen licht, `gloed.png` niet getekend (Olaf), (4) zwart meldingenvlak in plaats van `paneel.png` (Olaf, `kern/tekst.gd`), (5) aarde nog één bruin vlak, `aarde_lagen.png` nog niet ingebouwd (Olaf, `hol.gd`). Of Olaf en Bram dit intussen deden, zie hun `taken.md` en de tak `schermen` (map `steam-hol/...`).

## Wat ik zelf nog zou verbeteren
Eerlijk: pixelmaat en leesbaarheid zijn goed, **dichtheid, kleur en karakter halen het niveau van Rusty's Retirement nog niet.** Daar zit jouw wow.
1. **Een eigen gezicht.** Nu is het nette pixelart zoals de hele hoek. Wat het herkenbaar van ons kan maken: Gloop als mascotte (groter, feller, meer gezicht), en de helden met wrok als vaste figuren met naam, kleur en littekens die je na één keer herkent.
2. **Kleur.** Te veel bruin. Rusty is fel en verzadigd. Een warmer licht rond schat en fakkels, en koel donker in de diepte, geeft meteen sfeer.
3. **Dichtheid.** Elke kamer vol kleine dingen (potten, kisten, spinnenweb, botjes, plantjes); ongegraven aarde ook iets te zien geven. Wel rustig genoeg om de hele dag naar te kijken.
4. **Helden 13 tot 14 px hoog** en meer contrast tegen de muur; nu net te klein en te donker.
5. **Kleine leven-animaties overal** (fakkel flakkert, gras wiegt, Gloop ademt), spaarzaam want stilstand is zuinig voor de processor.
6. **Rijker maaiveld en een rustige achtergrond** erachter voor winkelplaatjes (nu steken de testvensters door het gras).
7. Naamkaartje en trofee rijker; upgrades zichtbaar maken (Gloop groter, roestige stekels), Sanne vroeg daarom in `platformen/steam/features.md`.
8. Eigen smal pixellettertype voor de meldingen. Minimal 5x7 breekt in de spatiëring, Public Pixel is te breed (beide CC0, GEZIEN in proefbeeld).

## Handig om te weten
- `git pull` en de volle tak `schermen` kunnen hangen. Werkt wel: `git fetch --depth 1 --filter=blob:none`, of losse plaatjes met `curl -sL` van raw.githubusercontent.com.
- De Windows-runner draait op 1024 x 768 met een consolevenster; voor winkelplaatjes is een nagebouwd bureaublad van 1920 x 1080 eerlijker, mits gemeld als nagebouwd.
- Winkelplaatjes van de toppers: `curl -s "https://store.steampowered.com/api/appdetails?appids=2666510"` (Rusty's Retirement), daarna de `screenshots` ophalen en met Read bekijken.

Vragen aan mij: zet ze in `berichten/daan.md` onderaan of in `platformen/steam/taken.md`.
