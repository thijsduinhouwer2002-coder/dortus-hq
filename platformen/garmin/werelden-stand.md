# Werelden-stand (Wout, tweede bouwer Ebb)

Bijgewerkt 12 nov 2026, run 1 van Wout. Tak: `claude/garmin-werelden-proef-wout` (afgetakt van `claude/garmin-2026-11-10b`, 5c4f146).

| Dier | Bestand | Naam beelden | Wereldnr op mijn tak | Laatste commit | Plaatjesrun groen | Zelf gezien (FR255 en fenix 8 47 mm, dag en nacht, zes schermen) | Open punten |
|---|---|---|---|---|---|---|---|
| garnaal (surfplank) | `source/KrabV2Garnaal.mc` (167 regels) | `garnaal-*` | 2 | c515597 | ja (runs 43193229548 en 43193229552) | ja, naast Mila werelden5 en werelden4 | grijze bodem valt op FR255 weg tegen het water; op het eindscherm staan kiezels vlak onder de pagina-stipjes; frisse kijker nog niet (doet de hoofdchat) |
| zeester (telescoop) | `source/KrabV2Zeester.mc` (163 regels) | `zeester-*` | 3 | c515597 | ja (zelfde runs) | ja | de telescoop boven water wordt niet gemeten tegen de tekst (VEILIG meet alleen het kader van de held), op het beeld ruim vrij; telescoop op het eindscherm is klein; poel onder water valt grotendeels buiten de ronde rand; frisse kijker nog niet |

Vaste lijst bij beide nagelopen: grap leest in één blik (garnaal surft, zeester kijkt door een telescoop); niets raakt tekst; geen los voorwerp door de rand (surfplank en telescoop gemeten met `KrabV2Rand.meet`); held blijft zichtbaar bij nacht; geen onbekende tekentjes meer (mossels weggehaald, lazen als blauwe ringetjes); achter de held niets in zijn kleur.

## Volgende run
Familie strand afmaken: **kreeft** (gieter boven een plantje op een eilandje, strohoed; tuin met hekje onder water), **zeehond** (ijsschots, hengel, dobber; onder het ijs), **zeeotter** (mok chocolademelk op zijn buik; kelpwoud). Daarna familie vliegers, huisjes, koud, licht (zie `ontwerp/garmin/bron/werelden_v4_<familie>.py`, bovenaan staat welke dieren erin zitten). Nog 20 te gaan. Wereldnummers 4, 5, 6 op mijn tak (Gijs kiest de echte nummers bij samenvoegen).

## Wat ik over de werkwijze leerde (lees dit eerst, scheelt tijd)
- Mila's ontwerp per dier staat letterlijk als code in `ontwerp/garmin/bron/werelden_v4_<familie>.py` (op main): functies `adem` (boven water, held en grap), `plek` (onder water) en `hold`, `menu`, `eind` met de plek en maat van de held. Overnemen gaat sneller dan van de beelden afmeten. Haar coördinaten zijn ook 1/260 en haar `top` is gelijk aan `KrabV2Tekst.KAM` (134, 170, 146).
- Omzetten: Mila `dier_kantel(x, y, m, hoek)` wordt `held` [x, y, m] en `kantel` = min hoek. Menu zakt de plek 6, eindscherm 24. Held op het eindscherm rond [70, 123, 30].
- `ontwerp/` staat niet op de bouwtak: gebruik een tweede werkmap (`git worktree add ../main origin/main`) of `git show origin/main:<pad>`.
- Geen SDK nodig om te bouwen: de plaatjesrun bouwt en draait de toetsen eerst (na ±3 minuten weet je of het compileert). Een plaatjesrun op de proeftak duurde 25 minuten, niet 10.
- Beelden met namen komen van de workflow "Garmin Ebb .iq (winkelbestand)" (commit "Plaatjes Ebb run N" op tak `schermen`), in `garmin-adem/plaatjes-proef/namen/`. Die map deelt elke proeftak (ook die van Gijs): haal de beelden op de commit van jouw run, `https://raw.githubusercontent.com/<repo>/<commit>/garmin-adem/plaatjes-proef/namen/<naam>.png`, anders kun je de beelden van een ander zien.
- Kijken: plak de zes schermen dag en nacht in één blad en snijd het scherm uit (FR255 kader 83,155,363,435; fenix 8 47 mm 152,233,572,653 in de simulatorfoto). Twee bladen per dier is genoeg.
- Losse voorwerpen onder aan het scherm (kiezels, mossels) vallen snel weg tegen de ronde rand: leg ze hoger dan op Mila's blad of laat ze weg.
- Haalbaar per run van ongeveer 45 minuten: twee werelden af en gezien (bouwen 15 minuten, twee plaatjesruns van 25 minuten). Met drie werelden in één plaatjesrun wordt het drie, als de eerste ronde meteen groen is.
