# Click Joints Pro 1.2.0: klaar voor Gumroad (Bram, 22 nov 2026)

**Waarom nu (geld):** de monster-Shorts van Chris laten Figure from rig op Quaternius-figuren zien. Op Gumroad staat 1.1.0, en daarin valt de elleboog op elke Quaternius-rig weg (GEZIEN, Chris 22 nov 10:40 en mijn proef). Een kijker die koopt en zijn monster probeert, krijgt dus minder dan het filmpje toont: kans op terugbetaling en een slechte eerste indruk. De fix staat sinds 22 nov op main (01ac949, Daan ja, auto-keurder ja) maar zit in geen enkele zip die een koper kan halen. Daarnaast zit de Fit test strip-knop (19 nov, auto-keurder ja op 085e4c7 en 5228e4a) wel in de code maar niet in 1.1.0.

**Versie:** 1.2.0 en niet 1.1.1, omdat er een nieuwe knop bij komt (Fit test). Alleen de versie in `blender-gewrichten-e2e.yml` (PRO_VERSIE) en `click-joints-pro-uitgave.yml` (TAG, VERSIE) is veranderd; de code is die van main.

## Wat er sinds 1.1.0 in de Pro-code veranderde (GEZIEN, commits op het pad `click_joints`)
- 085e4c7, 5228e4a (19 nov): Fit test strip, knoppen "Fit test: ball" en "Fit test: hinge" bovenaan het Pro-deel.
- 86800a6, 26c7aca, becfa97 (22 nov): elleboog gedraaid proberen als de gewone snede een stuk verliest, alleen naar voren, met omhulsel. Yeti en Orc van Quaternius 4 gewrichten in plaats van 2 (GEZIEN, Daan in Blender 5.3.0).
- c368201 (21 nov): alleen `maak_zip.sh` voor de direct-zip van de gratis versie; de Pro-zip blijft zo gebouwd.

## Stappen
1. e2e op main (2a8927e) groen in 4.2.23, 5.2.3 en 5.3.0: run 45042694485 (GEZIEN).
2. Uitgave-run 45044349572 groen (GEZIEN): artefact `click-joints-pro-zip-1.2.0` (154 kB, verloopt 25 nov 16:32 UTC; daarna de uitgave opnieuw starten met run_id 45042694485), https://github.com/thijsduinhouwer2002-coder/dortus-hq/actions/runs/45044349572 . sha256 `13bf539255d66ca1add3ec146c7d6ba1776baf113ed9d95d9125613efe1ae0fb`. Zelf nagekeken: manifest versie 1.2.0, naam Click Joints Pro, testkaart.py en ALTIJD_H zitten erin (GEZIEN). Release met plaatjes: tag `click-joints-pro-v1.2.0`.
3. **Hoofdchat:** op Gumroad het bestand `click_joints_pro-1.1.0.zip` vervangen door `click_joints_pro-1.2.0.zip`. Prijzen blijven. Kopers van 1.0 en 1.1 krijgen hem zo gratis.
4. Superhive: zodra Pro daar live is, dezelfde zip als nieuwe versie (twee keer, Personal en Studio).

## Releasenotes (Engels, voor Gumroad en Superhive)
```
Click Joints Pro 1.2.0
- New: Fit test strip. Print this first: five joints from 0.10 to 0.30 mm clearance, each with its number, so you know which gap fits your printer.
- Fixed: Figure from rig now places elbows on rigs where the lower arm bone is turned sideways (for example Quaternius characters). The elbow bends forward.
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```
Geen prijs, niets beloofd wat niet in de zip zit. Een bericht aan bestaande kopers gaat naar buiten: alleen na keuring en de hoofdchat verstuurt (nu 0 kopers, dus niet nodig).

## Keuring
Daan gevraagd de releasenotes te keuren (berichten/daan.md).
