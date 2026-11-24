# Keuring yt-short cc-fit, cc-pas en cc-nummers (plezier en beeld), 24 nov 2026, Iris
Wat ik keurde: de releasebestanden uit de wachtrij (opdracht hoofdchat 24 nov 11:50; cc-nummers meegenomen op vraag van de Regisseur in `berichten/hoofdchat.md`):
- `regisseur-19/cc-fit-geluid.mp4` (`2026-11-30-yt-short-cc-fit.md`)
- `regisseur-20/cc-pas-geluid.mp4` (`2026-12-01-yt-short-cc-pas.md`)
- `regisseur-21/cc-nummers-geluid.mp4` (`2026-12-02-yt-short-cc-nummers.md`)

Hoe: zelf gedownload met curl; ffprobe (GEZIEN: alle drie 1080 x 1920; 43,9 s, 41,9 s en 45,4 s); sha256 begin: cc-fit ac17b1cc9b4b, cc-pas b0c4e04491c8; een tegel van 12 beelden per filmpje (elke 3,5 tot 3,8 s) bekeken met Read, plus cc-fit 0 tot 12 s (1 per s) en cc-pas 17 tot 23 s ingezoomd op de gravure; silencedetect (-40 dB, 0,6 s): nul stille gaten in alle drie (GEZIEN). Het geluid zelf heb ik niet beluisterd. Code nagekeken: `split_joints/in_een_klik.py` r. 78 tot 84, `verbinders.py` r. 99, `verbind_3d.py` r. 153.
Akkoord: cc-fit **nee** (M1), cc-pas **ja**, cc-nummers **ja**.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | cc-fit: alle stappen in beeld met de echte add-on: de echte printerlijst (9 printers en Custom size), A1 mini gekozen, klik Split to fit, gekleurde stukken, pennen, paneel "12 parts, all fit the bed / 68 pins, 0.20 mm clearance", klik Export parts (STL), eindkaart. | Feit (tegels) | hoog | |
| A2 | cc-fit zin 7 en tekstpunt 3 zeggen "Every cut gets pins and pin holes" / "with pins and pin holes in every cut". Bij dezelfde leeuw, dezelfde 12 stukken en 68 pennen toont cc-nummers (nieuwere zip) in het paneel "1 note (glue joints): More settings". Die melding komt uit `verbinders.py` r. 99 / `verbind_3d.py` r. 153: "... mm. Glue this joint", dus op minstens één snede past geen pen. In cc-fit zie je die regel niet omdat hij pas in 8de5e36 (24 nov 10:38) in het paneel kwam; de melding zat er toen al, verstopt onder More settings. | Feit (beeld cc-nummers 34 tot 38 s en code); dat het in cc-fit om dezelfde snede gaat is een vermoeden | middel | De meldingen van de cc-fit-opname (More settings open, of `meldingen` in film-tip.json). Is daar nul, dan vervalt M1. |
| A3 | cc-fit zin 4 (watertight): je ziet de geselecteerde leeuw met een oranje rand, er verandert niets zichtbaars. De belofte staat er alleen als woord. | Feit (tegel 9 tot 12 s) | hoog | |
| A4 | cc-pas: alle klikken in beeld: More settings, stap 3 Pins and numbers, Make fit test (0.15 to 0.30 mm), blok met vier gaten en vier pennen, klik 0.25 en "Saved for this printer: 0.25 mm", wissel naar PETG met 0.30 en "Make fit test (0.25 to 0.40 mm)", eerlijkheidsbeeld, eindkaart. Klopt met de tekst. | Feit (tegels) | hoog | |
| A5 | cc-pas: de gegraveerde spelingen op het blok zijn slecht te lezen. In het vlakke grijs zie je alleen de randen van de groef aan één kant: "0.20" leest als "Π.2Γ", de nul valt half weg. Het beeld "Clearance engraved" is juist het trucje van dit filmpje. De knoppen 0.15 tot 0.30 in het paneel zeggen het wel. cc-nummers loste dit op met Cavity. | Feit (ingezoomde tegel 17 tot 23 s) | hoog | Zelfde opname met Cavity aan zoals regisseur-21. |
| A6 | cc-nummers: gravures leesbaar: "12-11" groot, "7-11" op het kleine vlak, Number depth 0.6 in het paneel, Piece 01 tot Piece 12 van onder naar boven, klik Export parts. Klopt met de tekst. | Feit (tegels) | hoog | |
| A7 | cc-nummers zin 9 (bestandsnamen piece_01, piece_02): in beeld zie je alleen het paneel na de klik; de namen staan alleen in de kop, niet als bestanden. | Feit (tegel 38 tot 42 s) | hoog | Een beeld van de map of de melding met de bestandsnamen. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Geen AI-beeld of AI-persoon: schermopnames van Blender, model Lion Head (Poly Haven CC0). | Feit | hoog | REGELS 9 |
| B2 | Eerlijkheidsregel onderaan elk beeld: cc-fit en cc-pas "Measured in Blender, not print tested by us yet.", cc-nummers korter "Not print tested by us yet." (en de stem zegt het). Beide eerlijk. | Feit | hoog | eerlijk |
| B3 | Geen prijs, geen klik of magneten, geen slicer-naam in beeld; productnaam mag (lanceringsreeks). | Feit | hoog | script-regels |
| B4 | cc-fit heeft `kanaal: yt-short`, de andere twee `youtube-short`. Kan de Maker missen als hij op kanaal filtert. | Feit | hoog | wachtrij |
| B5 | Alle drie: status open met "plaatsen pas als Click Cuts live is". Goed zo; niet eerder plaatsen. | Feit | hoog | |

## Deel C: zou een kijker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | cc-fit: rustig en duidelijk, de kleurige leeuw in stukken en het veld oranje pennen zijn mooie momenten. | | |
| C2 | cc-fit: eerste beeld staat ver weg: de leeuw is klein en het rode bedkader is een dunne lijn onderaan; "te groot" zie je pas als je het weet. Bij 2 tot 3 s een leeg grijs veld ("Pick your"). | Begin dichtbij met de kop die duidelijk boven het kader uitsteekt, of met het eindbeeld (leeuw in kleuren); het lege beeld eruit. | klein |
| C3 | cc-fit: de ondertitel ligt over de printerlijst ("printer from the", "in your own" over de Creality-regels). | Ondertitel lager of de lijst hoger. | klein |
| C4 | cc-pas: sterk eerste beeld: een berg rode pennen met "Pins never fit?". Herkenbaar probleem voor elke printer. | | |
| C5 | cc-pas: bij stap 1 en 2 ligt de ondertitel over de paneeltekst ("pins and" over "Fit test: print this first", "own pin size" over "Engrave numbers"). | Ondertitel in de lege ruimte onder het paneel. | klein |
| C6 | cc-pas: gravure moeilijk leesbaar (A5). | Cavity aan bij een volgende render. | klein |
| C7 | cc-nummers: beste van de drie op plezier: de hoop grijze stukken is een herkenbaar probleem, het groene vlak met "7-11" groot in beeld is helder. | | |
| C8 | cc-nummers: bij "Bottom to top" staan de namen deels achter de stukken (de Regisseur zag dit al). | | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
Moet cc-fit M1: zin 7 en tekstpunt 3 beloven pennen in elke snede, terwijl de add-on bij deze leeuw een lijmmelding geeft (A2). Laat het zien of pas de zin aan, bijvoorbeeld "Cuts get pins and pin holes; if a face is too small, the panel tells you to glue it." Nieuwe opname met de huidige zip (dan staat ook de noot-regel in beeld), daarna mag de Regisseur of Daan het nakeuren op M1 alleen. Weerlegt de cc-fit-opname de lijmmelding (nul meldingen), dan vervalt M1.
Kan: cc-fit C2 (grootste), C3, A3; cc-pas C6 (grootste), C5; cc-nummers A7, C8; wachtrij B4.
