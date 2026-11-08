# YouTrack-scan: open verzoeken met veel stemmen die een plugin kan vullen (Jet, 8 nov 2026, 17:00 tot 17:20 UTC)

Waarom: de regel "markt bewijzen" noemt open verzoeken met veel stemmen als bewijs. Dat soort bewijs had ik voor het tweede product nog niet breed gemeten (wel DOT, Tcl, Ansible los).

Hoe: per project de 60 open Feature-verzoeken met de meeste stemmen, met curl van `https://youtrack.jetbrains.com/api/issues?query=project:<P> #Unresolved Type:Feature sort by:votes desc&fields=idReadable,summary,votes` (GEZIEN), projecten IDEA, PY, WEB, CPP, GO, RIDER, RUBY, RUST, DBE (PHP gaf een fout: projectnaam bestaat zo niet). 540 verzoeken, alle in `youtrack-verzoeken-2026-11-08.tsv`. Daarna met de hand de verzoeken met 40 of meer stemmen geschift op "kan een losse plugin dit, zonder het hart van de IDE te veranderen" en per kandidaat de Marketplace gezocht (`/api/searchPlugins`, `/api/plugins/<id>`, `/feature/getImplementations`, GEZIEN).

## Uitkomst: geen leeg gat met veel stemmen gevonden (nagekeken door een controleur, 4 moet-punten verwerkt)

| Verzoek (stemmen) | Wat er nu is (GEZIEN) | Oordeel |
|---|---|---|
| CPP-1102 SCons (367), CPP-861 premake (110), CPP-15899 GN (63) | **SCons Workbench** (id 35256, brisaworks, freemium $49/$99 per jaar, sinds 18 okt 2026, 71 downloads): volgens zijn beschrijving (niet getest) SCons, Premake, qmake, GN, build2 en Ninja als compilation database in CLion, getest op Godot en Skia. Voor `*.gn` ook GN (19.240) en GN Language (911), gratis | bezet (dekt het volgens de beschrijving, niet getest) |
| CPP-5652 Cython in CLion (223) | `*.pyx` hoort bij de Python-plugin; **Oskuvi PYX Language** (id 35122, betaald $39 per jaar, 43 downloads, nieuw, alleen proef van 7 dagen) voor andere IDE's | bezet |
| CPP-1070 OpenCL (114) | **GPU Dev Accelerator Ultimate** (id 29044, betaald, 2.086 downloads): CUDA, Metal en OpenCL, $225 per jaar, meldt `*.cl` aan (de andere twee voor `*.cl` zijn Slt, Common Lisp, en Expert.ai Studio) | bezet, en een kleine taal |
| DBE-9984 DBML (60) | DBML (5.301), DBML Canvas (419), DBML Diagram (555), DBML Pro (betaald, 185), ERD Editor (33.103) | vol |
| IDEA-168305 API Blueprint (53) | twee betaalde plugins (API Blueprint Lifetime 1.084, Viewer 173) en Apiary (6.407); formaat raakt uit gebruik (GOK) | vol en klein |
| IDEA-24108 StringTemplate (43) | StringTemplate v4 (26.010 op de laatste versie, nov 2023, geen bovengrens, dus nog te installeren) | klein, niet verlaten |
| CPP-193 Autotools (338) | geen echte plugin (alleen "AutoTool", 30 downloads, een opmaakhulp); CLion opent Makefile-projecten zelf, met `./configure` als voorstap (GOK van de controleur en mij, niet nagemeten) | gedeeltelijk gat; het werk zit in het projectmodel van CLion, groot en dicht bij wat CLion zelf doet. Niet nu |
| PY-8238 Kivy (282) | Oskuvi KV Language (betaald, 154) en Kvasar (freemium, 111), allebei nieuw | bezet |
| PY-1706 Tornado-sjablonen (94) | geen sjabloonplugin gevonden (`searchPlugins?search=tornado template` geeft alleen TornadoInsight, iets anders) | leeg, maar een oud verzoek voor een kleine, oudere webbibliotheek; vraag nu niet gemeten (GOK klein). Hoogstens later nameten |
| CPP-1536 GLSL ES (82) | GLSL Support (413.271, bijgewerkt 2026), GLSL (161.791) | vol |
| Zig, Robot Framework, Jenkins Pipeline, Meson | bestaan al als plugins, deels van JetBrains zelf (Meson 278.241) | vol |

De rest van de lijst boven 40 stemmen is werk aan de IDE zelf (debugger, projectmodel, databasesoorten in DataGrip, profilers): geen plugin voor ons.

## Les (GEZIEN, met een GOK over de oorzaak)
1. Bijna elk plugin-groot gat met stemmen is in oktober en november 2026 gevuld door een nieuwe betaalde of freemium plugin (SCons Workbench 18 okt, Oskuvi PYX, Oskuvi KV en Kvasar voor Kivy, eerder Graphlume 18 okt en BatchCraft). Die nieuwe plugins hebben heel weinig downloads (30 tot 154). GOK: er bouwen nu meer makers snel plugins voor elke open niche, net als wij.
2. Gevolg voor ons: "een gat vinden" werkt bijna niet meer; wie als eerste in de aanraadlijst staat met een sterk gratis deel pakt de stroom (zie Batch, DOT). Het verschil moet dus komen uit uitvoering en zichtbaarheid, niet uit een lege plek. Dat pleit voor kandidaten waar al veel downloads naar een zwakke plugin gaan, en voor de groeimeting van 9 nov.
3. Geen voorstel naar Hans. Volgende stap blijft de groeimeting van de aanraadlijsten (9 nov vanaf ±14:30 UTC).
