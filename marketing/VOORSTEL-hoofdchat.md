# Voorstel aan de hoofdchat: Roep krijgt het plaatsen, de hoofdchat beslist oranje

Van: bouwer Roep, 19 nov 2026. **Niet doorgevoerd**: de hoofdchat voert het door (CLAUDE.md en `organisatie/hoofdchat-ronde.md` zijn niet van mij). Grond: keuring 19 nov moet 2 (één eigenaar van het Metricool-quotum) en B6 (regel 4 moet mee, anders overtreedt de tak de regel), besluit Thijs 19 nov 01:35 (een tak die zelfstandig plaatst) en besluit 19 nov 11:00 (geldroute 3).

**Wanneer doorvoeren:** zodra Thijs de taak "Roep: maken en plaatsen" heeft aangemaakt (`organisatie/sjablonen/taak-roep-maker.md`). Tot dan blijft het zoals het is en plaatst de hoofdchat-ronde zelf.

## 1. CLAUDE.md, harde regel 4

**Nu:**
> 4. **Niets naar buiten onder de naam van Thijs** (mail, bericht, zijn eigen accounts zoals Reddit) zonder zijn ja op de tekst. **Posts op de kanalen van Dortus** (YouTube, TikTok, de Discord van Hats) mogen na een keuring door een ander, zonder zijn ja (Thijs, 18 nov 23:17). Agents plaatsen nooit zelf; de hoofdchat doet het.

**Wordt:**
> 4. **Niets naar buiten onder de naam van Thijs** (mail, bericht, zijn eigen accounts zoals Reddit) zonder zijn ja op de tekst. **Posts op de kanalen van Dortus** (YouTube, TikTok, de Discord van Hats) mogen na een keuring door een ander, zonder zijn ja (Thijs, 18 nov 23:17). **Op TikTok en YouTube plaatst alleen de Maker van Roep, via Metricool, en alleen wat de Keurder van Roep groen keurde** (`marketing/REGELS.md`, Thijs 19 nov 01:35). Andere agents plaatsen nooit zelf; de rest (Discord van Hats, nieuwe kanalen) doet de hoofdchat.

## 2. `organisatie/hoofdchat-ronde.md`

**Inleiding, nu:** "Dit ís de hoofdchat: plaatsen mag hier (CLAUDE.md regel 4). ... Metricool Free geeft 20 posts per maand: plaats hooguit ±1 per dag per kanaal tot er een groter plan is."

**Wordt:** "Dit ís de hoofdchat. TikTok en YouTube plaatst de Maker van Roep; de hoofdchat plaatst daar niet meer zelf (CLAUDE.md regel 4). Het quotum van Metricool (20 per maand) is van Roep, zie `marketing/REGELS.md`."

**Stap 2, nu:** "Plaatsen (distributie gaat voor): zet elke post of elk filmpje dat klaarstaat ... via Metricool ..."

**Stap 2 wordt:**
> 2. **Roep: oranje beslissen en meekijken (distributie gaat voor).**
>    a. **Oranje:** zoek in `marketing/wachtrij/` concepten met `status: oranje` (en de meldingen van Roep-Keurder onderaan `berichten/hoofdchat.md`). Beslis elk: groen of rood, met één zin waarom, in `## Oranje-besluit`, en zet `status:` op groen of rood. Toets aan de hoofdzaak (brengt het geld dichterbij?) en aan de harde regels. Prijs, korting en Cyber Sale passen bij wat Bram en de winkelpagina zeggen; iets over Hats alleen zonder spelerstekst. Een oranje concept dat 24 uur ligt, wordt rood.
>    b. **Meekijken:** draaide de Maker zijn laatste ronde (nieuw blok onderaan `marketing/dagrapport.md`, commit van vandaag) en de Keurder (keuringen in de wachtrij)? Staat er iets onder "Open fouten" in het dagrapport (ERROR, geen adres): los het op of zet `marketing/STOP` en meld het Thijs. Plaatst iemand iets wat niet groen is, of in de ik-vorm als Thijs: haal de post weg in Metricool, zet `marketing/STOP`, meld het Thijs.
>    c. **Niet zelf plaatsen via Metricool.** Wil je zelf iets naar buiten (bijv. een spoedpost uit de reserve), zet het als concept in `marketing/wachtrij/` met `gemaakt_door: hoofdchat`; de Keurder keurt het, de Maker plaatst het.
>    d. Onder de naam van Thijs (zijn Reddit, mail, persmensen) blijft zoals het was: tekst klaarzetten op `organisatie/lijst-thijs.md`.

Stap 1 krijgt erbij: "lees ook het laatste blok van `marketing/dagrapport.md`". De rest van de ronde blijft gelijk.

## 3. Mee aanpassen (zelfde reden)
- **`organisatie/regels/thijs.md`, kop "Posten op de kanalen van Dortus":** "Een agent schrijft, een ander keurt, de hoofdchat plaatst" wordt "Een agent schrijft, een ander keurt, op TikTok en YouTube plaatst de Maker van Roep (`marketing/REGELS.md`), elders de hoofdchat". Mislukt een post of komt er een klacht: de hoofdchat haalt hem weg en meldt het Thijs (blijft).
- **`organisatie/sjablonen/taak-hoofdchat-ronde.md`:** de zin "Plaatsen op de kanalen van Dortus (YouTube, TikTok via Metricool, de Discord van Hats) mag na een keuring door een ander" wordt "Op TikTok en YouTube plaatst de Maker van Roep; jij beslist over oranje en plaatst alleen op de Discord van Hats." Metricool mag in de ronde aan blijven om te lezen en om een post weg te halen bij een fout; dat is geen plaatsen. Thijs hoeft de bestaande taak niet opnieuw aan te maken: de opdracht verwijst naar `hoofdchat-ronde.md`, en dat bestand verandert.
- **`organisatie/besluiten.md`, regel onderaan:** "19 nov 2026, hoofdchat | Roep plaatst: de Maker van Roep is de enige die via Metricool plaatst (TikTok, YouTube), alleen na groen van de Keurder van Roep; de hoofdchat-ronde beslist oranje en houdt de tak in de gaten. CLAUDE.md regel 4, hoofdchat-ronde stap 2 en regels/thijs.md aangepast. | Keuring marketing-tak moet 2 en B6: één eigenaar van het quotum. | Er gaat een ongekeurde of foute post uit, of het quotum is voor de 25e op."
- **`commercie/filmpjes/planning.md` en `commercie/lanceerposts.md`:** bovenaan een regel "Nieuwe posts gaan via `marketing/wachtrij/` (zie LEESMIJ)", zodat Chris en anderen niet meer daar klaarzetten voor de hoofdchat.

## 4. Overgang (wat de hoofdchat al heeft lopen)
- **Al ingepland door de hoofdchat:** filmpje 2 (19 nov 16:00) en filmpje 5 (vr 20 nov 16:00, YouTube 433851396, TikTok 433964787). Die blijven staan; de Maker leest ze terug in zijn eerste ronde en telt ze mee in het quotum van november.
- **YouTube-video 1 van Chris** (`commercie/wachtrij/youtube-pro-1.md`, liggend, eerste klikbare verkoopweg, af vóór vr 20 nov 12:00): als Daan ja zegt vóór de Maker draait, plaatst de hoofdchat hem nog zelf (oude werkwijze). Anders zet Chris hem als `marketing/wachtrij/2026-11-20-yt-lang-pro-hinge.md` in het nieuwe formaat, met de keuring van Daan genoemd onder Bronnen; de Keurder van Roep keurt, de Maker plaatst. Stuur Chris daarover een bericht.
- **Lijst van Thijs:** zet één punt op `organisatie/lijst-thijs.md`: "Twee geplande taken aanmaken (±6 minuten): tekst in `organisatie/sjablonen/taak-roep-maker.md` en `taak-roep-keurder.md`; bij beide Automatically approve aan; Metricool alleen bij de Maker."
- **Eerlijk tegen Thijs** (keuring moet 6), in de samenvatting: in week 1 plaatst en verzint de tak zelf, maar reageert hij nergens op mensen; verwacht geld de eerste weken: tientallen dollars, tenzij één video groot gaat (GOK).
