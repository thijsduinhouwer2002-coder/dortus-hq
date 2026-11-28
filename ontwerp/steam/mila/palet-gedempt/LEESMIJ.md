# Gedempt palet voor Hats (Mila, 28 nov 2026, issue #333)

Waarom: drie blinde tests van 27 nov zeggen "cheap", "plastic", "generic mobile", één keer "adopt a softer, less saturated art style" (GEZIEN, `organisatie/blindtest/uitslag/hats-itch-omslag-2026-11-27-2202.md` en `hats-header-v2-2026-11-27-2254.md`). Bij minuut 0 vroeg één ronde juist om "more vibrant" (GEZIEN, `hats-speelscherm-minuut0-e0ed18c-2026-11-27-2246.md`). De rechters bedoelen dus niet "grijzer", maar "minder glimmend plastic, meer getekend".

## Voorstel figuren (proef staat hier, nog niet in het spel)
- Geen glas en geen natte glans meer (goud en staal wel glans). Elk materiaal twee tinten met een harde grens (Toon BSDF in Blender), de schaduwkant koeler en donkerder, nooit zwart. Metaal houdt een kleine harde glimvlek.
- Verzadiging maal 0,8 en een tikje warmer. Vaste tinten: Gloop `72cfa6` (schaduw `389072`, licht `b0e9cf`), staal `a3a9b6`. Goud blijft vol `f2b632` met echte glans: dat is de beloning.
- Geen inktlijn in de render: op spelmaat werd die modder in gezicht en handen (geprobeerd, GEZIEN). Het spel tekent zelf al een donkere rand van 1 spelpixel om elke held (Olaf #242).

Beelden (uit losse renders met dezelfde instellingen): `spelmaat-160-1x.png` en `-2x.png` (boven nu, onder gedempt, op de maat van een strook van 160 px: Gloop 64 px hoog, held 56), `groot-voor-na.png` (zelfde, groot).
Wat ik zie: Gloop is geen glimmende gelei meer maar een zachte getekende munt; helden lijken op spelmaat bijna gelijk, alleen minder glans op helm en schild. Het verschil is klein op 120 px en duidelijk vanaf 160 px.

## Echte schermbeelden uit het spel (proeftak)
`spel-strook160-voor-na-2x.png`: boven main (run 46087795325), onder proeftak ronde 1 (run 46087753565, commit 5e2cd6c), strook 160, 2x vergroot (GEZIEN).
Wat ik zie in ronde 1: Gloop zachter en minder gelei, helm en kroon matter; maar de schat, munten en kroon werden flets en het geheel oogt waziger. Daarom in ronde 2 (commit a306689): goud en staal houden hun glans en volle kleur. Uitslag ronde 2 staat onderaan.

## Voorstel grond (voor Olaf en Sanne, dat is lichtkaart in Godot, niet mijn 3D)
Nu is de aarde rood-bruin en vrij fel (meest `8d4f37`, `b16a48`, `5d332b`, GEZIEN uit het schermbeeld van minuut 0). Gloop (munt) en de helden staan daardoor tegen een warme, drukke muur. Naast Rusty (koel lavendelgrijze steen `97989c` / `667172`, alleen de oogst fel) en Spirit City (donker warm grijs `402f2c` / `504642`, licht crème `f5ead8`; beide GEZIEN, kleurtelling van hun eerste Steam-schermbeeld):
- aarde `5a4640` / `4a3a34` (bruin, minder rood), gangsteen blauwgrijs `6f7486` / `555a6b`, voeg `2c2428`
- fel alleen waar iets gebeurt: fakkel, goud, Gloop, helden. Dan valt elk figuur op 120 px los van de grond.

## Proeftak
Tak `claude/steam-palet-gedempt`: daar staat in `producten/steam-hol/modellen/gedeeld.py` `PALET_STANDAARD = "gedempt"`. De pijplijn rendert op die tak alle bladen in het nieuwe palet en start de Windows-run met schermbeelden op 96, 120 en 160 px (tak `schermen`). Op main verandert niets.
- `mat()` zet het palet om (vaste tinten hierboven, de rest verzadiging maal 0,8), zonder glas en natte glans.
- `_maak_getekend()` maakt vlak voor het renderen van elk materiaal twee tinten (Toon BSDF) uit dezelfde kleur of textuur, ook bij modellen die zelf textuur in hun materiaal zetten (`hol.py`, `royal.py`). Gloeiend (vlam, goudschat) en doorzichtig blijft zoals het was.
- Inktlijn alleen met `HOL_LIJN=1` (staat uit).

Overnemen op main = die ene regel en de twee functies meenemen; dan maakt de pijplijn alle bladen opnieuw. Dat doe ik zodra Sanne in #333 kiest en Daan keurde.

## Uitslag ronde 2
`spel-strook160-voor-na-ronde2-2x.png`: boven main, onder proeftak ronde 2 (run 46090310669, commit 01f2838), strook 160, 2x (GEZIEN). Goud, munten en kroon zijn weer vol en glanzend; Gloop is zacht mat munt in plaats van glimmende gelei; helden en hol iets lichter en rustiger. Het verschil is klein: alleen het palet van de figuren lost "cheap" niet op zonder de grotere strook en de koelere grond (Olaf, #333). Volgende stap: Sanne kiest A of B in #333; bij B op main zetten, Daan keurt, en de blinde test minuut 0 neemt het mee met de grotere strook.
