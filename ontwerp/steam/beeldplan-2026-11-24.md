# Beeldplan Hats of the Fallen: van "niet top" naar spectaculair (Daan, 24 nov 2026)

Opdracht: hoofdchat 24 nov ±17:50 NL, na Thijs 17:44 "qua graphics is het niet top" en de lat "spectaculair" (besluit 24 nov 16:39).
Waarom (geld): het beeld op de winkelpagina en in de eerste 5 seconden van een filmpje beslist of iemand wenst of koopt. Effect op wishlists: GOK, maar elk vergelijkbaar bureaubladspel dat goed verkoopt ziet er rijk uit (zie voorbeelden).

## Wat er nu mis is (GEZIEN, `producten/steam-hol/bewijs-vol/main-boven-vol-onder-lokaal-160.png`)
1. **Licht overal even sterk.** Fakkels branden, maar verlichten niets. Geen donkere hoeken, geen poelen licht.
2. **Eén bruintint.** Wand, vloer en nis zijn hetzelfde kleibruin; alles ligt in dezelfde waarde, dus niets springt eruit.
3. **Geen diepte.** Geen schaduw onder vaten, paddenstoelen en vallen; de spullen lijken erop geplakt. Geen voorgrond, geen achtergrond.
4. **Leeg.** Grote stukken wand met alleen ronde steentjes; elke kamer even vol.
5. **Niets beweegt behalve de figuren.** Geen stof, geen vonk, geen glans, geen gefladder.

## De zes punten, elk met een voorbeeld (Steam-beelden gelezen met curl, 24 nov)
| # | Wat beter | Voorbeeld (DERDEN) | Hoe bij ons | Wie, kosten |
|---|---|---|---|---|
| 1 | **Licht:** donker koel hol, warme poelen rond fakkels, schat, kristal en Gloop. Fakkels flakkeren. | Spirit City: warm venster, donkere hoeken, het licht vertelt waar je moet kijken ([beeld](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2113850/7d288079dbc0eb12cb613ff81680f811f2d7fc42/ss_7d288079dbc0eb12cb613ff81680f811f2d7fc42.1920x1080.jpg)) | Godot: `CanvasModulate` (koel donker) plus `PointLight2D` per lichtbron, licht als eigenschap in de data van elk ding. Gras en lucht blijven daglicht. | Olaf of Bram, ±1 run; geen nieuwe kunst nodig |
| 2 | **Diepte:** zachte schaduw onder elk ding, donkere naad waar wand en vloer elkaar raken, vignet naar de randen, af en toe een donkere voorgrond (wortel, steen) die iets sneller schuift. | Ropuka's Idle Island: donkere onderkant met rotsen geeft het eiland gewicht ([beeld](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3416070/b93835cac1a6ec352744390dfd8c8de0339310a1/ss_b93835cac1a6ec352744390dfd8c8de0339310a1.1920x1080.jpg)) | Blender: schaduw mee renderen (shadow catcher, aparte laag per model). Godot: vignet-shader, voorgrondlaag. | Daan (modellen), Bram (pijplijn) |
| 3 | **Kleur:** schaduw koel (paars, blauw), licht warm (oranje, goud). Wand per kamer iets anders (mos, kristal, aarde). Felle accenten alleen op wat telt: goud, Gloop, drankjes, vallen. | Rusty's Retirement: verzadigd, elke tegel een eigen kleur, toch rustig ([beeld](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2666510/ss_3496a84df0dbe09dd5949e2e9d6b47892a80311f.1920x1080.jpg)) | Kleurtabel per kamersoort in de data; wandmateriaal in `hol.py` met variatie. | Daan |
| 4 | **Dichtheid:** kleine dingen in elke kamer: wortels, druppels, mos, botjes, kaarsstompjes, munten in kieren. Geen kamer twee keer hetzelfde. | Rusty's Retirement: de hele strook staat vol, op 120 px nog steeds leesbaar ([beeld](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2666510/ss_f15441bfd5758bae1c69fa51a068c9869d26a200.1920x1080.jpg)) | Versieringsset uitbreiden (`versiering.py`), willekeurig per kamer met vaste seed. | Daan |
| 5 | **Effecten:** stof dat in het licht zweeft, vonken als een val dichtklapt, een twinkel op goud en munten, gloed op kristal en Gloop, **een hoed die tollend op de stapel valt** (draaien, stuiter, wolkje stof, stapel wiebelt even). | Spirit City: deeltjes en zacht licht maken een stil beeld levend (zelfde beeld als 1) | Godot: `GPUParticles2D` (stof, vonken), glow in `WorldEnvironment`, de hoedval als tween (draai plus squash bij landing). | Olaf (code), Daan (vonk- en stofplaatjes) |
| 6 | **Figuren blijven leesbaar in het donker.** In de proef werd de dief te donker. | Spirit City: de figuur heeft altijd randlicht | Figuren niet laten meedonkeren (eigen licht-mask of `unshaded`), dunne lichte rand in de render. | Bram, Daan |

## Proefbeeld: hetzelfde hol, maar met licht
- Bestand: `ontwerp/steam/beeldplan/voor-boven-na-onder-2x.png` (boven nu, onder de proef), los: `proef-hol-licht-2x.png`. Gemaakt met `beeldplan/proef_licht.py`.
- Wat het is: het echte schermbeeld van het spel, met in Python precies wat Godot ook kan: koel donker als basis, tien lichtpoelen, contactschaduw op de vloerlijn, vignet, glow, stof in het licht en twinkels op goud. Geen nieuw model, geen AI. Het paneel rechtsonder is niet aangeraakt.
- Wat het niet is: nog niet in het spel, en nog niet spectaculair. Het laat punt 1, 5 (deels) en 6 (het probleem) zien. Punt 2 tot 4 vragen nieuwe renders.
- Wat ik zelf zie (GEZIEN): het hol krijgt sfeer, je oog gaat naar de schat en de fakkels, de munten twinkelen. Minder: de dief en de hoedenstapel verliezen leesbaarheid in het donker (punt 6), en de wand blijft eentonig (punt 3 en 4).

## Volgorde (eerst wat het meest oplevert per uur)
1. Licht in Godot (punt 1 en 6): goedkoop, geen nieuwe kunst, grootste sprong. Olaf of Bram.
2. Effecten (punt 5), met de hoedval als eerste: dat is het beeld voor de filmpjes.
3. Schaduw in de renders en kleur per kamer (punt 2 en 3): Daan.
4. Dichtheid (punt 4): Daan, in golven met de nieuwe dingen van Sanne.
5. Daarna per val en drankje uit de demolijst van Sanne een model in deze stijl, elk met één zichtbaar effect. Die lijst bestaat nog niet (gezocht 24 nov ±18:35 NL); zodra hij er is, maak ik per ding een regel: vorm, kleur, licht, effect, maat op 120 px.

## Keuring
Plan en proef zijn van mij, dus een ander keurt (skill `keuren`): graag Iris (plezier) of de hoofdchat. Toets op ware grootte (120 px strook) naast Rusty's Retirement, zoals `3d-stijl.md` regel 3 zegt.
