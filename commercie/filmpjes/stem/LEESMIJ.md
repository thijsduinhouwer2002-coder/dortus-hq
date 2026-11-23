# Stem-machine: uitlegfilmpjes met een voice-over die precies op het beeld valt

Opdracht hoofdchat, ma 23 nov 2026 ±11:45 NL: Thijs wil voice-over bij de Blender-filmpjes van Click Joints Pro, synchroon met het beeld, en een rijkere montage in de stijl van zijn eigen uitlegfilmpje.

## Hoe het werkt
1. **Script** (`proef-1.json`): per scène één Engelse zin (`tekst`, met eventueel `uitspraak` als de stem iets anders moet lezen, zoals "three M F" voor 3MF), een label in een pil, een kop van 3 tot 5 woorden en het beeld: een render, een stuk uit de ruwe Blender-opname (`deel`, `van`, `tot` in beelden) met de uitsnede waarop het venster inzoomt (`[midden-x, midden-y, breedte]` in pixels van het opnamescherm 2160x1920), en eventueel een kader (`nadruk`, met `nadruk_bron` = van welk tot welk opnamebeeld) en een kaartje met de Bend-schuif (`inzet`).
2. **Stem eerst** (`stem.py`): per zin de audio, stilte voor en na eraf, lengte gemeten.
3. **Beeld volgt stem** (`montage.py`): zin i begint 0,35 s na het eind van zin i-1; de scène begint 0,10 s vóór de stem. Bij elke zin zoomt het venster in 0,55 s naar het deel waar de zin over gaat, en komen label, kop en zin op. Eindbeeld: icoon, titel, de samenvatting in één zin, dortus.com/yt.
4. **Geluid**: stem boven de zachte eigen ondergrond van `commercie/filmpjes/geluid/geluid.py` (-27 dB onder de stem, -20 dB in de pauzes), een zacht tikje bij elke muisklik in beeld. Geen muziek van anderen. Daarna loudnorm naar -14 LUFS.
5. **Controle** (`synchroon.py`): faster-whisper maakt uit het klare mp4 een transcript met woordtijden (audio als numpy-array). Per zin het eerste woord, verfijnd tot het begin van de klank; de scènewissel wordt los gemeten uit het beeld (sprong in het tekstvak). Verschil per zin moet binnen 0,3 s vallen, anders faalt de workflow. Plus `organisatie/controle/geluid_check.py` en de lengte (40 tot 60 s voor een Short).

Twee vormen uit hetzelfde script: `staand` (1080x1920, Short) en `liggend` (1920x1080, lange video; label en kop rechts naast het venster, zoals bij Thijs).

Draaien: workflow `.github/workflows/stem-proef.yml` (bij een push in deze map), release `stem-proef-1`. Een nieuw filmpje = een nieuw script-json en een regel in de workflow.

## De stem wisselen
- **Nu:** Kokoro-82M, stem `af_heart` (Amerikaans Engels, vrouw, rustig), snelheid 0,95. Andere stem: `KOKORO_STEM` (bijvoorbeeld `bf_emma` of `bm_george` voor Brits).
- **Later ElevenLabs:** zet het geheim `ELEVENLABS_API_KEY` in de repo (en eventueel de variabele `ELEVENLABS_VOICE_ID`). Dan gebruikt `stem.py` vanzelf ElevenLabs, met hetzelfde script en dezelfde timing (de lengtes worden opnieuw gemeten). Dat kan pas na een ja van Thijs op een betaald plan: het gratis plan geeft geen commerciële rechten (DERDEN: https://elevenlabs.io/docs/overview/administration/billing).

## Licenties (zelf gelezen met curl, 23 nov 2026)
| Onderdeel | Licentie | Bron |
|---|---|---|
| Kokoro-82M v1.0, model én stemmen (map `voices/` in dezelfde repo) | Apache 2.0, commercieel gebruik toegestaan. De modelkaart: "Apache-licensed weights ... can be deployed anywhere from production environments to personal projects" en "deployed in numerous projects and commercial APIs". Getraind op "permissive/non-copyrighted audio data" (public domain, Apache/MIT, synthetische audio van gesloten modellen; geen stemklonen). Een klein deel CC BY-audio (Koniwa, SIWIS) zit in de training; dat zijn Japanse en Franse stemmen, niet `af_heart` (GOK op basis van de taal van die sets). | DERDEN: https://huggingface.co/hexgrad/Kokoro-82M (README, `license: apache-2.0`) en https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md (`af_heart` cijfer A) |
| ONNX-bestanden `kokoro-v1.0.onnx` en `voices-v1.0.bin` (omzetting van hetzelfde model) | Apache 2.0 (het model); README van kokoro-onnx: "kokoro model: Apache 2.0". sha256 staan vast in de workflow. | DERDEN: https://github.com/thewh1teagle/kokoro-onnx (release model-files-v1.1) |
| kokoro-onnx 0.6.1 (code) | MIT | DERDEN: https://github.com/thewh1teagle/kokoro-onnx/blob/main/LICENSE |
| espeak-ng (maakt van tekst klanktekens, via espeakng-loader) | GPL 3.0 voor het programma; wij verspreiden het niet, we draaien het alleen in CI. De gemaakte spraak valt daar niet onder (GOK, gangbare lezing). espeakng-loader zelf: MIT. | DERDEN: https://github.com/espeak-ng/espeak-ng/blob/master/COPYING, https://github.com/thewh1teagle/espeakng-loader |
| faster-whisper 1.2.1 en model `Systran/faster-whisper-small.en` (alleen voor de controle, komt niet in de film) | MIT | DERDEN: https://github.com/SYSTRAN/faster-whisper, https://huggingface.co/Systran/faster-whisper-small.en |
| Beeld: opname en renders uit release `youtube-shorts-4` (Blender 5.3.0, Click Joints Pro 1.1.0, MakeHuman base mesh CC0 1.0) | eigen werk; figuur CC0 | `marketing/keuring/2026-11-22-yt-shorts-3.md` (licentie MakeHuman gelezen) |
| Icoon eindbeeld | eigen werk | `ontwerp/click-joints/icoon.png` |

YouTube: in de beschrijving zetten we eerlijk "Voice: AI text to speech (Kokoro)".

## Bestanden
- `stem.py`: stem per zin, Kokoro of ElevenLabs.
- `montage.py`: tijdlijn, beeld, geluid, script met tijden (`*-script.json`, `*.srt`).
- `synchroon.py`: transcript en meting (`transcript-*.json`, `transcript-*.srt`, `synchroon-*.md`).
- `proef-1.json`: het script van de proef-Short "How far can this knee bend?".
