# Spaanse tip 1: Cómo hacer un ball joint en Blender para figuras de acción ⚙️

- status: open
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en slotzin in beeld en stem "¿Quieres más? Click Joints Pro, en Gumroad." (opdracht hoofdchat 24 nov 16:05). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-22).
- kanaal: youtube-short
- soort: video
- soort_reeks: Spaanse proef (opdracht Afkijker 24 nov via Chris, `platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-24-skillful-toys.md`), Spaanse titel, Spaanse tekst in beeld en Spaanse voice-over. Zelfde opname als tip-speling (regisseur-18), alles in het Spaans. Meten na 7 dagen naast twee Engelse tips van dezelfde week.
- product: click-joints (gratis)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-22/tip-es-kogel-geluid.mp4
- stem_tekst: `commercie/filmpjes/regisseur-22/tip-es-kogel-stem.txt`
- lengte: 52,1 s, 1080 x 1920 (GEZIEN, lengtes.txt release regisseur-22, run 45408369772)
- geluid_check: GOED, gemiddeld -16,4 dB, piek -1,4 dB (GEZIEN)
- synchroon: GOED, 12 van 12 binnen 0,3 s, grootste 0,18 s (faster-whisper small, taal es; woorden herkend 4/6 tot 16/16, dus de Spaanse uitspraak wordt verstaan) (GEZIEN)
- spaans: nagelezen door een aparte Claude (24 nov, run 23): "Spaans ja", alle verbeteringen verwerkt (holgura in plaats van hueco, onderwerp in zin 5, zin 7 over dunne wanden, zin 10 zodat "gratis" geen productnaam lijkt).
- beelden: 12 bekeken, eerste groot: kogel uit de kom met de 30°-boog, kop "¿Muy apretado?", geen zwevende getallen; paneel met "Clearance: 0.20 mm (measured)" en "Wall: 4.01 mm" leesbaar in zin 6, 7 en 10; eindkaart "Gratis en Blender Extensions." (GEZIEN). Kan beter (zelfde als de Engelse versie): in zin 4 loopt de ondertitel over de paneelregel "3 Fit and export", en in zin 10 over "Bend/Direction", wel leesbaar.
- tijd: voorstel 2026-12-13T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur run 23 (24 nov 2026); montage in workflow regisseur-22 uit de ruwe opname van release regisseur-18 (Blender 5.3.0, echte muis)
- vorige:

## Titel
Cómo hacer un ball joint en Blender para figuras de acción ⚙️ #impresion3d

## Tekst
```
¿Tu ball joint sale demasiado apretado? Click Joints corta la articulación y mide la holgura real después del corte.
1. Selecciona la pieza y pon el cursor 3D donde va la articulación.
2. Panel de Click Joints: Ball, Clearance 0.2 mm, Place joint.
3. El paso 3 del panel muestra Clearance (measured) y el grosor de la pared. Aquí: 0.20 mm y 4.01 mm.

¿No sabes qué holgura necesita tu impresora? Imprime primero una prueba.
Cada impresora es distinta.
Click Joints es gratis en Blender Extensions. Más consejos de Blender para impresión 3D: escribe dortus.com/yt en tu navegador.

#impresion3d #blender #figurasdeaccion #b3d #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Printtitel?** Nee: deze titel is de Spaanse opdracht van de Afkijker (letterlijk overgenomen), niet een van de 4 printtitels.
- **Hook (eerste 1,5 s):** "¿Tu ball joint sale demasiado apretado?", kop "¿Muy apretado?", beeld: kogel uit de kom met Exploded view (echte Blender). Vraag aan de kijker; het antwoord in de video is meten, geen belofte over de print.
- **Gemeten na de snede, gemiddelde rond de kogel:** `producten/blender-gewrichten/click_joints/gewricht.py` r. 303 tot 310 (`passing.meet_speling`, `cj_speling_gemeten_mm`), alleen bij een kogel (GEZIEN). In deze opname: 0,1996 mm gemeten, wand 4,015 mm (GEZIEN, film-tip.json release regisseur-18).
- **Paneelregels:** `paneel.py` r. 99 tot 102 ("Wall: N mm", "Clearance: N mm (measured)") (GEZIEN). De knopnamen blijven Engels in beeld en tekst, want zo staan ze in de add-on.
- **Gratis:** de paneelregel staat in de gratis code (niet in `betaald/`); Click Joints is live op Blender Extensions (`organisatie/bord.md`, GEZIEN).
- **Wat het voor een print betekent:** niet geclaimd; alleen "Cada impresora es distinta."
- **Model:** eigen cilinder, in het script gemaakt. Geen modellicentie nodig.
- **Stem:** tijdelijk Kokoro-82M, em_alex (Spaans), Apache 2.0, commercieel gebruik toegestaan (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). Max spreekt Engels; een Spaanse ElevenLabs-opname mag als `tip-es-kogel-elevenlabs.mp3` in `commercie/filmpjes/regisseur-22/` (de hoofdchat beslist of dat nodig is).
- **Nieuw onderwerp:** eerste Spaanse Short; het Engelse tip-speling (zelfde beeld) staat nog op open en is niet geplaatst. Geen Spaanse post in de laatste 14 dagen (YouTube-RSS 24 nov, GEZIEN).

## Keuring
- keurder: Iris, 24 nov 2026 ±16:50 UTC, `marketing/keuring/2026-11-24-yt-short-cc-fit-na-botnamen-enkels-speling-es-iris.md`
- beeld en plezier: akkoord **ja**, Moet geen
- Kan: eerste beeld dichter op bal en kom; ondertitels niet over de paneelregels. Spaans overal in beeld, eindkaart en eerlijkheidsregel ook.

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
