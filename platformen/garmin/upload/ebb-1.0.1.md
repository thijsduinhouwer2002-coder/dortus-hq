# Ebb 1.0.1: wat er verandert in de winkel (concept, nog NIET uploaden)

Gijs, 16 nov 2026, run 116. Opdracht hoofdchat 15:00 NL: meer horloges en een kortere naam met het zoekwoord vooraan (verhaal 14 van Joris). Dit bestand wordt het plakbestand voor de update. Het is pas klaar als de test groen is, Chris de namen nakeek en Daan ja zei; dan komt het uploadblok op `organisatie/lijst-thijs.md`.

## 1. Nieuwe naam (voorstel, Chris kijkt na)

| Taal | Nu | Nieuw | Tekens |
|---|---|---|---|
| Engels | `Ebb: Breathing Exercises, Breath Hold & Calm` | `Ebb Breathing & Breath Hold` | 27 |
| Duits | `Ebb: Atemübungen, Atem anhalten & Entspannung` | `Ebb Atmung & Atem anhalten` | 26 |
| Nederlands | `Ebb: Ademhalingsoefeningen, Adem inhouden & Calm` | `Ebb Ademhaling & Adem inhouden` | 30 |

Waarom deze en niet alleen "Ebb Breathing": op "breath hold" staat Ebb nu op plek 4 en dat woord willen we houden; "breathing" (plek 28 van 307) is het woord waar de meeste ademapps op gevonden worden en staat nu vooraan. Risico, eerlijk: "Calm" verdwijnt uit de naam en op "calm" staat Ebb nu op plek 3. Het woord blijft in de eerste zin van de beschrijving en in de tags staan, en de gratis Ebb Calm draagt het in zijn naam. Of plek 3 blijft weten we pas na de update; ik meet het (zie 4).

De beschrijving, de tags en de beelden blijven gelijk aan `ebb-en.md`, `ebb-de.md` en `ebb-nl.md`. Geen nieuwe medische woorden.

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

## 3. Wat is nieuw (tekst voor het veld, Engels; wordt definitief als de lijst vaststaat)

```
Ebb now runs on many more watches, including fēnix 9, fēnix E, fēnix 7S, epix (Gen 2), Enduro 3, Venu 2S and 2 Plus, Forerunner 255S, 255 Music, 265S and 170, MARQ (Gen 2) and D2 Mach. Nothing else changed.
```

## 4. Meten

In `platformen/garmin/meting-ebb.md`: zoekplekken (ebb, breathing, breath hold, breathwork, calm) en downloads op de dag van de update en 7 dagen erna.

## 5. Stand van de test

TESTUITSLAG
