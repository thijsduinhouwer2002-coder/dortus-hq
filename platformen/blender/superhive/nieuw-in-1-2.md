# Superhive Pro: blok "New in 1.2" bovenaan (Bram, 23 nov 2026)

Opdracht Afkijker 23 nov ±08:45 UTC, punt 2 (punt 1, de $0-variant, vervalt: besluit hoofdchat 10:45). Voorbeeld: auron3d opent zijn pagina met "BIG UPDATE" en wat er nieuw is; SquishyFX verkoopt 400+ keer (DERDEN, `platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-23-auron3d-squishyfx.md`).

**Status: ter keuring bij Daan.** Alleen plakken als de zip op Superhive 1.2.0 is (samen met stap 4 van `platformen/blender/pro-1.2.0.md`). Zolang daar 1.1.0 staat, klopt het blok niet.

## Wat er nu live staat (GEZIEN met curl, 23 nov ±11:05 UTC)
- Eerste alinea "Pick your rigged figure, press one button, ...", daarna "From rig to a figure that moves.".
- "Update log" staat al onderaan (1.1.0 en 1.0.1). Schuiven hoeft dus niet; alleen het blok bovenaan en een regel in het log erbij.
- "Already bought Pro? 1.1 is a free update: ..." onder Good to know.

## 1. Nieuw blok, direct na de eerste alinea (Engels, plakken)
```
New in 1.2
- Fit test strip: print this first. Five joints from 0.10 to 0.30 mm clearance, each with its number, so you know which gap fits your printer.
- Figure from rig now places elbows on rigs where the elbow would otherwise bend upward (for example Quaternius characters). Needs Blender 4.5 or newer.
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```
De drie regels komen uit de releasenotes die Daan op 22 nov keurde (`platformen/blender/pro-1.2.0.md`, keuring `keuring/2026-11-22-pro-1.2.0-daan.md`). Ingekort: "The elbow now bends forward" en "on 4.2 to 4.4 it still asks you to place the elbow by hand" eruit, omdat "Needs Blender 4.5 or newer" de grens al noemt en Good to know al zegt dat in 4.2 sommige gewrichten met de hand moeten.

## 2. Regel onder Good to know (vervangt de regel over 1.1)
```
Already bought Pro? 1.2 is a free update: download it from your Orders page on Superhive, or update it inside Blender if you added Superhive as a repository.
```

## 3. Bovenaan het Update log erbij
```
1.2.0 (Nov 2026): Fit test strip; Figure from rig places elbows on rigs where they would bend upward (Blender 4.5 and newer).
```

## Na te kijken door de keurder
- Klopt elke regel met de 1.2.0-zip (sha256 13bf5392...e0fb, uitgave-run 45044349572).
- Belooft niets wat niet in de zip zit; geen klik, geen prijs, geen korting.
