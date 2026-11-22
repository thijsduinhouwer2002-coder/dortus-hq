# Overstap naar het eigen Claude-account van Thijs (gepland 7 nov 2026)

Waarom: het huidige account is gedeeld met de vader van Thijs en zat zaterdag al op bijna 50% van de weeklimiet. Thijs gaat verder op zijn eigen account met een groter abonnement.

Wat **niet** vanzelf meegaat: geplande taken, gekoppelde repo's, de netwerkinstelling, Claude in Chrome, het claude.ai-project en het geheugen. Alles wat de ploeg weet staat in deze repo, dus dat gaat wel mee.

## Stappen voor Thijs (±15 min)
1. Log in op claude.ai met je eigen account.
2. **Netwerk:** Settings > Capabilities > "Use the internet while making files" aan, Allowed websites op **Any website**. Zonder dit krijgen alle runs een 403 (zie `organisatie/middelen.md`).
3. **GitHub koppelen:** Settings > Connectors (of via Claude Code) GitHub koppelen met het account `thijsduinhouwer2002-coder`.
4. **Project maken:** een claude.ai-project "Dortus-HQ" met de GitHub-repo `thijsduinhouwer2002-coder/dortus-hq` als bron.
5. **Claude in Chrome** op de HP: de extensie inloggen met het nieuwe account.
6. Open in dat project een nieuwe chat en zeg: **"Lees CLAUDE.md en organisatie/overstap-account.md en voer de overstap uit."**

## Wat de nieuwe projectchat doet
1. Koppel met add_repo en access **push**: `dortus-hq`, `dortus` en `rollwright` (owner `thijsduinhouwer2002-coder`), en kloon ze. Geplande taken krijgen de repo-toegang van de chat waarin ze worden gemaakt, dus dit eerst.
2. Maak alle vaste geplande taken opnieuw aan met de opdrachten uit `organisatie/geplande-taken.md` (zelfde naam, schema, model Opus 5.5, op Auto, in de cloud, geen connectors erbij). Actief op 7 nov:
   - Olaf `13 8-19`, Daan `23 8-19`, Vera `31 8-23`, Jet `52 8-19`, Bram `7 8-19`, Chris `41 8-19`, Stijn `44 7`, Hans `44 20` (melding aan).
   - Niet meenemen: "Olaf - OUD" (staat uit) en de herinnering "Arrears stoppen" (hoort bij het oude account).
3. Test met één run (bijvoorbeeld Vera met fire) dat pushen werkt en `curl https://example.com` 200 geeft.
4. Zet de nieuwe trigger-ID's in `organisatie/geplande-taken.md` en sla op.
5. **Pas als alles op het nieuwe account draait:** Thijs zet de taken op het oude account uit (of laat de oude projectchat dat doen). Anders draaien alle managers dubbel en botsen ze bij het opslaan.

## Na de overstap
- Kijk na een dag hoeveel van de limiet op is. Te veel: Vera en Daan om de twee uur, of runs korter dan 45 minuten. Dat beslist Thijs.
- De connectors van het gedeelde account (Gmail, Shopify, Trello, Kondo) horen niet bij de taken; op het nieuwe account niet toevoegen.

## Afgerond (7 nov 2026, 23:06)
Alle taken draaien op het eigen account van Thijs (ID's in `organisatie/geplande-taken.md`), plus Noor (pionier). De taken op het oude account staan uit (bevestigd door Thijs). Opslaan vanuit de runs werkt.
