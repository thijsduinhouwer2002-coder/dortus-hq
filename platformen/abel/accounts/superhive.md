# Superhive (Blender-winkel): kant-en-klaar plan (Abel)

Versie 1, 10 nov 2026 07:45 NL. Status: klaar om te doen zodra Thijs het verkopersaccount heeft (lijst-thijs, punt van Hans 06:45). Avatar akkoord (v2, Daan keuring 4). Banner is een uitsnede van de goedgekeurde Steam-achtergrond v3; **Daans ja gevraagd** (onderaan `ontwerp/keuring-abel.md`). **Bestanden: `platformen/abel/upload/7-superhive/`.**

## In één zin
Wie Click Joints Pro op Superhive vindt en op "Dortus" klikt, ziet dezelfde deur-D en hetzelfde gouden licht als op Steam, GitHub en Blender Extensions, in plaats van het standaardpatroon en een leeg rondje.

## Waarom nu
Hans vraagt Thijs vanochtend het Superhive-account te maken, en de makersaanvraag wordt gekeurd. Een winkel met eigen beeld en een korte zin oogt als iemand die blijft. Superhive zegt het zelf: zonder instellen toont je winkel "the default" banner en avatar en geen beschrijving (GEZIEN, support.blendermarket.com/article/163-how-to-customize-your-profile, 10 nov).

## Hoe het eruit gaat zien (proef op een echte openbare Superhive-winkel, alleen in mijn browser vervangen)
- Desktop 1920: `merk/proef/superhive-winkel-1920.png` (het licht valt van boven op de vloer, de D staat midden onder de banner).
- Laptop 1280: `merk/proef/superhive-winkel-1280.png`.
- Telefoon: `merk/proef/superhive-winkel-telefoon.png` (daar toont Superhive alleen het midden: een rustig donker vlak met de rand van de lichtbundel; munten en sleutel vallen buiten beeld, dat is goed zo).
De producten onder de kop in de proef zijn van de winkel die ik als mal gebruikte (Blender Guru).

Nagemeten in de stylesheet van Superhive (GEZIEN, `application-e45d570a.css`): de banner is 350 px hoog over de hele breedte en wordt bijgesneden ("cover", midden); de avatar is een rondje van max 150 px met een witte rand van 5 px, half over de onderrand van de banner. Daarom zit in onze uitsnede het licht in de bovenste helft en is het midden onderaan leeg.

## Stap 1. Avatar (Thijs, ±1 min)
1. Ingelogd op superhivemarket.com: je naam rechtsboven > **My Account** (account settings).
2. Bij **Avatar** het bestand `upload/7-superhive/account-avatar-400.jpg` kiezen (Superhive vraagt 400 x 400 en JPG; GEZIEN, support.superhivemarket.com/article/36).
3. Superhive vraagt je huidige wachtwoord om op te slaan (Update Info). Dat typ jij, niet wij.

## Stap 2. Winkel (Thijs, ±4 min)
Waar: **Creator Dashboard > Settings** (Shop Settings). Dit kan pas als de makersaanvraag is goedgekeurd (GOK: misschien al eerder zichtbaar).

| Veld | Invullen |
|---|---|
| Shop name | `Dortus` |
| Shop slug | `dortus` (wordt superhivemarket.com/creators/dortus; GEZIEN 10 nov: nog vrij, de link stuurt door naar de voorpagina zoals bij elke niet-bestaande naam) |
| Description | `Small, focused Blender tools that fill a real gap. Questions or a bug? Use Contact Creator.` |
| Website | `https://dortus.com` (Superhive toont die naast elk product, niet op de winkelpagina) |
| Twitter, Facebook | leeg laten (die hebben we niet) |
| Banner Image | `upload/7-superhive/winkel-banner-2400x660.png`. Weigert Superhive die (ze vragen 1200 x 330, JPG of PNG, onder 5 MB), neem `winkel-banner-1200x330-reserve.png`. De grote is scherper op brede schermen, want Superhive rekt de banner op tot de schermbreedte. |

Onderaan op de oranje knop **Save Shop Settings**.

Waarom deze beschrijving: zelfde kern als overal ("focused tools that fill a real gap", `merk/teksten.md`), plus waar je terecht kunt met een vraag. Bewust geen antwoordtijd beloofd: niemand van ons leest die berichten nu elke dag. Geen spel noemen: dit is een Blender-winkel.

## Controle
Open https://superhivemarket.com/creators/dortus: banner met het gouden licht, het rondje met de lila D, daaronder Dortus en de zin. Moet lijken op `merk/proef/superhive-winkel-1920.png`.

## Niet doen
- Geen andere naam dan `Dortus`: op Blender Extensions heet de maker Thijs-Dortus, en Dortus is het merk op elke andere plek.
- Uitbetaling en belasting pas invullen als er iets verkoopt (zegt Hans ook).
