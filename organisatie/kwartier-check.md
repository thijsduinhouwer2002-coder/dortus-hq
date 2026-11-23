# Kwartier-check (opdracht Thijs 23 nov 2026 20:55)

Thijs: "jij mag elk kwartier kijken en jezelf deze vragen stellen". Dit is de hoofdchat in een korte, vaste ronde. Werktijd ±12 minuten. Doen, niet rapporteren.

## Elke ronde
1. `bash organisatie/start.sh`. Lees bovenaan `organisatie/trots.md`, het einde van `berichten/hoofdchat.md`, `organisatie/bord.md` en wat er sinds de vorige ronde op main kwam (`git log --since="20 minutes ago" --stat | head -80`).
2. Neem **één** product per ronde, op volgorde van geldkans (nu Click Joints Pro, dan de splitser Click Cuts, dan Ebb). Beantwoord kort en eerlijk, met wat je echt zag (pagina's met curl, beelden met Read):
   - Is de marketing goed genoeg om te concurreren? (beelden, filmpjes, hook, winkeltekst)
   - Is het product goed genoeg om zelf te kopen? (werkt het betrouwbaar, doet het wat de pagina belooft)
   - Is de interface en gebruiksvriendelijkheid goed genoeg? (paneel, eerste minuut, foutmeldingen)
   - Vallen we genoeg op tussen concurrenten? (zelfde zoekwoord op Superhive en Gumroad, met curl)
   - Hoe doen anderen het nu en wat doen zij anders? (één concurrent per ronde, iets concreets)
3. **Eén nieuw idee** om Dortus naar een hoger niveau te tillen. Toets het kort aan `organisatie/ideeentest.md` (geld binnen weken? hoeveel? GOK met reden). Schrijf het bovenaan `organisatie/ideeen-kwartier.md`: tijd, product, idee, score 1 tot 10, eerste stap.
4. **Handelen:** is een antwoord bij stap 2 "nee" en werkt niemand eraan: zet de juiste eigenaar meteen aan het werk met een bericht onderaan zijn berichtenbestand (met datum, "van hoofdchat kwartier", wat en waarom). Elk idee met score 8 of hoger: meteen een opdracht aan de eigenaar. Nooit twee keer dezelfde opdracht; kijk eerst in het berichtenbestand.
5. Werk de regel van dat product bovenaan `organisatie/trots.md` bij (max 3 regels). Commit, `python3 organisatie/controle/check.py`, push met pull --rebase en retry, `git ls-remote origin main`.

Regels: CLAUDE.md gaat voor. Niets plaatsen, niets onder de naam van Thijs, geen geld. Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
