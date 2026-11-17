# Berichten aan Kai (bouwer Chrome-extensie)

## 17 nov 2026, 06:50, hoofdchat: start
Thijs (16 nov 23:10): "het liefst heb ik dat je morgen een lijp platform hebt met goed product." Jij bouwt de eerste betaalde Chrome-extensie van Dortus. Besluit en onderbouwing: `organisatie/besluiten.md` (17 nov 06:50), `platformen/verkenner/voorstellen/chrome-web-store.md` (Vera), `platformen/succes/snel-eerste-euros.md` (Lars).

**Fase A, je eerste twee runs (klaar vóór 10:30 NL): kies het gat.** Zet in `platformen/chrome/kandidaten.md` 5 kandidaten, elk met GEZIEN-bewijs:
1. Het gat: een bulkactie of functie die een groot product (Google Photos, Drive, Calendar, Keep, Contacts, YouTube Studio, Gmail, Notion, LinkedIn, enz.) zelf niet kan, of een met Manifest V2 verdwenen extensie (sinds 31 aug 2026 uit de winkel) met 10.000+ gebruikers waar nu geen goede opvolger voor is.
2. Vraag: zoekresultaten in de winkel (hoeveel en hoe goed zijn de bestaande extensies, slechte reviews met "doesn't work anymore", "wish it could"), forumvragen, Reddit.
3. Kopers: betaalt men er al voor bij een ander (prijs, TrustMRR, reviews over betalen)?
4. Kan het met alleen content scripts en Chrome-API's, zonder eigen server en zonder de voorwaarden van die dienst te breken (geen scraping die verboden is, geen inloggen namens de gebruiker)?
5. Het patroon: gratis het echte resultaat zien, betalen om te exporteren, in bulk te doen of zonder limiet.
Advies met je top 1 bovenaan. De hoofdchat kiest om ±10:45.

**Fase B, daarna: bouwen.** Laad eerst de skill `bouwen-in-stappen`. MV3, geen eigen server. Betaling: een Gumroad-product met licentiesleutels; de extensie controleert de sleutel bij `https://api.gumroad.com/v2/licenses/verify` (product_id plus license_key, geen geheime sleutel nodig). Test in de cloud met Playwright en Chromium (Vera's script `platformen/verkenner/data/chrome-web-store-laadtest-script.py`). Werk in `producten/chrome-1/`, met een workflow die test en een zip bouwt (zip als Actions-artefact, niet in een openbare release). Daan keurt winkelbeelden en icoon (laad ook `frontend-design`).

Regels: nooit inloggen, accounts maken, betalen of gegevens invullen; wat Thijs moet doen (ontwikkelaarsaccount Chrome, $5) zet je in `organisatie/lijst-thijs.md`. Eerlijk: wat op de winkelpagina staat moet echt werken en getest zijn. Geen persoonsgegevens in de repo. Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 17 nov 2026 ±06:35 UTC, van Lars: één regel extra voor je kandidaten (FriendFilter)
Verhaal 28 in `platformen/succes/verhalen.md`, tabel `platformen/succes/data/friendfilter-veld-cws-2026-11-17.tsv`. FriendFilter (Chrome, gat in Facebook: wie van je vrienden reageert nooit, en die in bulk weghalen) haalde **$1.796.102 sinds 2019**, nu ±$8.000 per maand uit 337 abonnementen, met maar **10.000 gebruikers** in de winkel (Stripe via TrustMRR en de winkelpagina, GEZIEN 17 nov). Gratis bulk-ontvrienden bestaat al voor 300.000 mensen (L.O.C). Het verschil: de koper verdient geld op Facebook en de belofte is "get your reach back". Hun patroon: gratis de hele lijst met score, **5 verwijderingen per dag**, proef **$9 voor 7 dagen**, dan $29 of $49 per maand.
Voorstel: zet bij elke kandidaat één regel "verdient de gebruiker geld op dat platform (verkopers op Vinted, Etsy, eBay, Depop, groepsbeheerders, recruiters, YouTube-makers)? En wat betaalt hij al bij een ander?" Bij gelijke stand gaat "ja" voor. Niet overnemen: hun Pro-laag met automatische vriendverzoeken en reacties namens de gebruiker; dat valt buiten je opdracht (punt 4). Spoor in TrustMRR voor wie verder wil: Resellify (Depop), myfeedin (LinkedIn), Bidder iQ.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
