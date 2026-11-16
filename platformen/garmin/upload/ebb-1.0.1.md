# Ebb 1.0.1: wat er verandert in de winkel (concept, nog NIET uploaden)

Gijs, 16 nov 2026, run 116. Opdracht hoofdchat 15:00 NL: meer horloges en een kortere naam met het zoekwoord vooraan (verhaal 14 van Joris). Dit bestand wordt het plakbestand voor de update. Het is pas klaar als de test groen is, Chris de namen nakeek en Daan ja zei; dan komt het uploadblok op `organisatie/lijst-thijs.md`.

## 1. Nieuwe naam (nagekeken door Chris, 16 nov ±15:15 UTC, `commercie/ebb/naam-1.0.1.md`)

| Taal | Nu | Nieuw | Tekens |
|---|---|---|---|
| Engels | `Ebb: Breathing Exercises, Breath Hold & Calm` | `Ebb Breathing & Breath Hold` | 27 |
| Duits | `Ebb: Atemübungen, Atem anhalten & Entspannung` | `Ebb Atemübungen & Atem anhalten` | 31 |
| Nederlands | `Ebb: Ademhalingsoefeningen, Adem inhouden & Calm` | `Ebb Ademhaling & Adem inhouden` | 30 |

Engels en Nederlands zijn mijn voorstel, Chris zei ja. Duits is het voorstel van Chris en dat neem ik over: op "atemübungen" staat Ebb nu op plek 3 en dat woord zou met "Atmung" uit de naam vallen, terwijl Ebb op "atmung" nu niet in de eerste 90 staat (zelf gemeten 14:58 UTC, `platformen/garmin/meting-ebb.md`). "Calm" laten we los: in de gewone zoekbalk staat Ebb daar op 42, niet op 3 (die 3 gold voor alleen apps). Het woord blijft in de eerste zin en in de tags.

Wat we verwachten is een gok (Chris: "breathing" van 29 naar ergens tussen 12 en 21). De nulmeting van vandaag staat in `meting-ebb.md`; na de update meten we op dezelfde woorden.

De beschrijving, de tags en de beelden blijven gelijk aan `ebb-en.md`, `ebb-de.md` en `ebb-nl.md`. Geen nieuwe medische woorden. De plakbestanden pas ik aan in dezelfde stap als het uploadblok, zodat er nooit een naam in staat die niet bij het bestand hoort.

## 2. Meer horloges: van 28 naar 56 in het manifest

Tak `claude/garmin-ebb-101`. Welke horloges de SDK kent, met schermmaat, startpictogram en geheugen, is GEZIEN in het bouwlog van run 43881391618 (173 horloges; de lijst hieronder komt daaruit, niet uit mijn hoofd).

**Stap 1, broertjes met een schermmaat die Ebb al had (22 erbij, geen nieuwe plaatjes):**

| Scherm | Horloges | Plaatjes van |
|---|---|---|
| 260 MIP | Forerunner 255 Music, fēnix 7 Pro (no Wi-Fi), fēnix 9 Pro Solar 47 mm | Forerunner 255 |
| 280 MIP | fēnix 7X Pro (no Wi-Fi), Enduro 3, fēnix 9 Pro Solar 51 mm | fēnix 8 Solar 51 mm |
| 390 AMOLED | MARQ (Gen 2), MARQ Aviator (Gen 2), Forerunner 170, 170 Music, Forerunner 70 | epix Pro 42 mm, Forerunner 165 |
| 416 AMOLED | epix (Gen 2), Venu 2 Plus, D2 Mach 1, D2 Air X10, fēnix 9 43 mm, fēnix 9 Pro 43 mm, fēnix E | epix Pro 47 mm, Venu 2, fēnix 8 43 mm |
| 454 AMOLED | fēnix 9 47 mm, fēnix 9 Pro 47 mm, D2 Mach 2, D2 Mach 2 Pro | fēnix 8 47 mm |

De winkelnamen van de nieuwste modellen (fēnix 9, Forerunner 170 en 70, D2 Mach 2) neem ik bij het uploadblok over uit het formulier van Garmin; hier staan de namen zoals de SDK ze noemt.

**Stap 2, nieuwe schermmaten (6 erbij, eigen letters en cijfers per maat, gemaakt met de bestaande scripts):** Forerunner 255S en 255S Music (218), fēnix 7S en 7S Pro (240), Forerunner 265S en Venu 2S (360). De tekeningen schalen mee; de regelhoogtes van de letters zijn een eerste schatting en worden gelijkgezet met de meting uit de simulator. Mila en Daan moeten deze maten op ware grootte zien voor ze meegaan; lezen ze niet goed, dan gaat 1.0.1 uit met alleen stap 1.

**Bewust niet:** Descent (duikhorloges; Ebb wil niet bij vrijduiken horen), Instinct en Approach (de knop heet daar niet START; eerst eigen knopteksten), en alles onder Connect IQ 5 of met weinig geheugen (vívoactive 4, Forerunner 245, 745, 945, fēnix 6, Venu): dat is stap 3, met geheugentoets.

## 3. Wat is nieuw (drie talen, vorm van Chris; definitief als Mila en Daan ja zeiden op de kleine maten)

Eén verschil met het voorstel van Chris: geen "up from 28". De winkel telt anders dan ons manifest: bij 28 regels in het manifest toont de winkel nu 40 horloges (GEZIEN in de API, 14:57 UTC, veld `compatibleDeviceTypeIds`). Hoeveel de winkel er bij 56 regels toont weet ik pas na de upload. Een getal dat niet klopt met wat de koper ziet zetten we er niet in.

Gaan alle 56 mee:
```
Ebb now runs on about twice as many Garmin watches, including fēnix 9, fēnix E, fēnix 7S, epix (Gen 2), Enduro 3, Venu 2S and 2 Plus, Forerunner 255S, 255 Music, 265S and 170, MARQ (Gen 2) and D2 Mach. Nothing else changed.
```
```
Ebb läuft jetzt auf etwa doppelt so vielen Garmin-Uhren, darunter fēnix 9, fēnix E, fēnix 7S, epix (Gen 2), Enduro 3, Venu 2S und 2 Plus, Forerunner 255S, 255 Music, 265S und 170, MARQ (Gen 2) und D2 Mach. Sonst hat sich nichts geändert.
```
```
Ebb werkt nu op ongeveer twee keer zoveel Garmin-horloges, waaronder fēnix 9, fēnix E, fēnix 7S, epix (Gen 2), Enduro 3, Venu 2S en 2 Plus, Forerunner 255S, 255 Music, 265S en 170, MARQ (Gen 2) en D2 Mach. Verder is er niets veranderd.
```
Gaat alleen stap 1 mee (50 regels): "about twice as many" wordt "many more" ("deutlich mehr", "veel meer"), en fēnix 7S, Venu 2S, 255S en 265S gaan uit de lijst ("Venu 2 Plus").

"Nothing else changed" klopt: tussen tag `ebb-v1.0.0` en commit 1aebd69 is in de map `source/` geen enkele regel veranderd (GEZIEN met `git diff`, run 117). Veranderd zijn alleen `manifest.xml`, `versie.txt`, de mappen met letters en pictogrammen voor de nieuwe horloges en het script `bron/maak_letters.py`.

## 4. Meten

In `platformen/garmin/meting-ebb.md`: zoekplekken (ebb, breathing, breath hold, breathwork, calm) en downloads op de dag van de update en 7 dagen erna.

## 5. Stand van de test (run 117, 16 nov ±15:10 UTC)

Commit 1aebd69 op tak `claude/garmin-ebb-101`.

| Wat | Uitslag | Hoe gezien |
|---|---|---|
| Winkelbestand bouwt (job bouw, run 43882501055) | groen | lijst van jobs |
| Alle horloges compileren (job alle-horloges, zelfde run) | groen, `COMPILEERT horloges: 56`, elk horloge drie keer ja | log gelezen |
| Toetsen en schermen op 16 horloges (job bouw, run 43882501327) | groen | lijst van jobs; beelden uit het pakket `garmin-adem-schermen` bekeken |
| Winkelplaatjes op 20 horloges (run 43882501055) | PLAATJESUITSLAG | |
| Regelhoogte van de letters op 218, 240 en 360 gelijkgezet met de meting | LETTERUITSLAG | |
| Ja van Mila en Daan op 218, 240 en 360 | gevraagd, nog geen antwoord | |

Zelf bekeken op ware grootte (pakket van run 43882501327): Forerunner 255S (218) elf beelden: de drie veiligheidsbladen, ademen met het grote getal, vandaag, 8 weken, het menu, de twee startschermen en "how it works". fēnix 7S (240) drie beelden, Forerunner 265S (360) drie, Venu 2S (360) vier. Alles staat binnen de ronde rand, de tekst is scherp en leesbaar, niets loopt over elkaar. Tussen "breathe in" en het grote getal zit op 218 en 240 ongeveer evenveel lucht als op de Forerunner 255 die al in de winkel staat (uitsnede drie keer vergroot naast elkaar gelegd). Geheugen op de 255S: hoogste stand 143 kB van 520 kB (27 procent, regel GEHEUGEN in `metingen.txt`).

Niet gezien: de winkelplaatjes van de nieuwe maten (walvis, schildpad, sea log, eindscherm), en alles op een echt horloge.
