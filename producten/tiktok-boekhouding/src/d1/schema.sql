-- D1-schema voor TikTok Shop naar je boekhouding. Ontwerp: ontwerp-d1-worker.md (punt 4, en punt 7: ontkoppelen).
-- Gewone tabellen (geen WITHOUT ROWID), zodat opruimen met rowid IN (...) werkt.
CREATE TABLE IF NOT EXISTS winkels (
  id TEXT PRIMARY KEY,
  shop_id TEXT,                      -- NULL na ontkoppelen
  shop_cipher TEXT,                  -- NULL na ontkoppelen
  tt_tokens TEXT,                    -- TikTok, versleuteld (AES-GCM), nooit leesbaar
  mb_tokens TEXT,                    -- Moneybird, versleuteld; na ontkoppelen alleen zolang intrekken niet gelukt is
  tt_versie INTEGER NOT NULL DEFAULT 0,
  mb_versie INTEGER NOT NULL DEFAULT 0,
  administratie TEXT,
  instellingen TEXT,                 -- JSON
  markering INTEGER,
  winkelfout TEXT,                   -- JSON {soort, bericht, kant}, zie src/d1/winkels.ts
  winkelfout_sinds INTEGER,          -- sinds wanneer dezelfde winkelfout onafgebroken staat (21 dagen regel, punt 7)
  volgende_run INTEGER NOT NULL DEFAULT 0,
  snel_teller INTEGER NOT NULL DEFAULT 0,
  ontkoppeld_op INTEGER,             -- gezet: kale rij, er wordt niets meer geschreven
  taken TEXT,                        -- JSON, bijv. intrekken en opzeggen na ontkoppelen
  polar_klant TEXT,
  abonnement TEXT,                   -- JSON {actief, tot, id, opgezegd, stand, betalingMislukt, vlagStand}, zie src/polar/abonnement.ts
  polar_gestart INTEGER              -- tijdstip van de eerste checkout (ontwerp-betalen.md, punt 1)
);
CREATE INDEX IF NOT EXISTS winkels_volgende_run ON winkels(volgende_run) WHERE ontkoppeld_op IS NULL;
-- Webhook type 6 zoekt de winkel op shop_id (punt 7). Uniek: één gekoppelde rij per TikTok-winkel.
CREATE UNIQUE INDEX IF NOT EXISTS winkels_shop_id ON winkels(shop_id) WHERE shop_id IS NOT NULL;
-- Cron: winkels die 21 dagen op dezelfde winkelfout staan (punt 7).
CREATE INDEX IF NOT EXISTS winkels_winkelfout_sinds ON winkels(winkelfout_sinds) WHERE winkelfout_sinds IS NOT NULL AND ontkoppeld_op IS NULL;

CREATE TABLE IF NOT EXISTS sloten (
  winkel TEXT NOT NULL,
  statement_id TEXT NOT NULL,        -- '__winkel' voor het winkelslot
  eigenaar TEXT NOT NULL,
  tot INTEGER NOT NULL,
  PRIMARY KEY (winkel, statement_id)
);

CREATE TABLE IF NOT EXISTS statussen (
  winkel TEXT NOT NULL,
  statement_id TEXT NOT NULL,
  status TEXT NOT NULL,
  statement_time INTEGER,
  opnieuw_sinds INTEGER,
  gegevens TEXT NOT NULL,            -- JSON van AfrekeningStatus
  PRIMARY KEY (winkel, statement_id)
);
CREATE INDEX IF NOT EXISTS statussen_status ON statussen(winkel, status);
CREATE INDEX IF NOT EXISTS statussen_opnieuw ON statussen(winkel, opnieuw_sinds);

CREATE TABLE IF NOT EXISTS transacties (
  winkel TEXT NOT NULL,
  statement_id TEXT NOT NULL,
  gegevens TEXT NOT NULL,
  opgehaald_op INTEGER NOT NULL,
  PRIMARY KEY (winkel, statement_id)
);

CREATE TABLE IF NOT EXISTS bestellingen (
  winkel TEXT NOT NULL,
  statement_id TEXT NOT NULL,
  order_id TEXT NOT NULL,
  gegevens TEXT NOT NULL,
  opgehaald_op INTEGER NOT NULL,
  PRIMARY KEY (winkel, statement_id, order_id)
);

-- Gratis grens (ontwerp-betalen.md, punt 1 en 2): één rij per afrekening die boekt; de stand van een maand is SUM(bestellingen).
CREATE TABLE IF NOT EXISTS telling (
  winkel TEXT NOT NULL,
  statement_id TEXT NOT NULL,
  maand TEXT NOT NULL,               -- JJJJ-MM van statement_time in Europe/Amsterdam
  bestellingen INTEGER NOT NULL,
  PRIMARY KEY (winkel, statement_id)
);
CREATE INDEX IF NOT EXISTS telling_maand ON telling(winkel, maand);

-- Punt 7: na ontkoppelen (of zonder rij in winkels) weigert elke INSERT en UPDATE; een batch is één transactie,
-- dus een aanroep die al liep zet niets meer terug.
CREATE TRIGGER IF NOT EXISTS statussen_ontkoppeld_insert BEFORE INSERT ON statussen
BEGIN SELECT RAISE(ABORT, 'ontkoppeld') WHERE NOT EXISTS (SELECT 1 FROM winkels WHERE id = NEW.winkel AND ontkoppeld_op IS NULL); END;
CREATE TRIGGER IF NOT EXISTS statussen_ontkoppeld_update BEFORE UPDATE ON statussen
BEGIN SELECT RAISE(ABORT, 'ontkoppeld') WHERE NOT EXISTS (SELECT 1 FROM winkels WHERE id = NEW.winkel AND ontkoppeld_op IS NULL); END;
CREATE TRIGGER IF NOT EXISTS transacties_ontkoppeld_insert BEFORE INSERT ON transacties
BEGIN SELECT RAISE(ABORT, 'ontkoppeld') WHERE NOT EXISTS (SELECT 1 FROM winkels WHERE id = NEW.winkel AND ontkoppeld_op IS NULL); END;
CREATE TRIGGER IF NOT EXISTS transacties_ontkoppeld_update BEFORE UPDATE ON transacties
BEGIN SELECT RAISE(ABORT, 'ontkoppeld') WHERE NOT EXISTS (SELECT 1 FROM winkels WHERE id = NEW.winkel AND ontkoppeld_op IS NULL); END;
CREATE TRIGGER IF NOT EXISTS bestellingen_ontkoppeld_insert BEFORE INSERT ON bestellingen
BEGIN SELECT RAISE(ABORT, 'ontkoppeld') WHERE NOT EXISTS (SELECT 1 FROM winkels WHERE id = NEW.winkel AND ontkoppeld_op IS NULL); END;
CREATE TRIGGER IF NOT EXISTS bestellingen_ontkoppeld_update BEFORE UPDATE ON bestellingen
BEGIN SELECT RAISE(ABORT, 'ontkoppeld') WHERE NOT EXISTS (SELECT 1 FROM winkels WHERE id = NEW.winkel AND ontkoppeld_op IS NULL); END;
CREATE TRIGGER IF NOT EXISTS sloten_ontkoppeld_insert BEFORE INSERT ON sloten
BEGIN SELECT RAISE(ABORT, 'ontkoppeld') WHERE NOT EXISTS (SELECT 1 FROM winkels WHERE id = NEW.winkel AND ontkoppeld_op IS NULL); END;
CREATE TRIGGER IF NOT EXISTS sloten_ontkoppeld_update BEFORE UPDATE ON sloten
BEGIN SELECT RAISE(ABORT, 'ontkoppeld') WHERE NOT EXISTS (SELECT 1 FROM winkels WHERE id = NEW.winkel AND ontkoppeld_op IS NULL); END;
CREATE TRIGGER IF NOT EXISTS telling_ontkoppeld_insert BEFORE INSERT ON telling
BEGIN SELECT RAISE(ABORT, 'ontkoppeld') WHERE NOT EXISTS (SELECT 1 FROM winkels WHERE id = NEW.winkel AND ontkoppeld_op IS NULL); END;
CREATE TRIGGER IF NOT EXISTS telling_ontkoppeld_update BEFORE UPDATE ON telling
BEGIN SELECT RAISE(ABORT, 'ontkoppeld') WHERE NOT EXISTS (SELECT 1 FROM winkels WHERE id = NEW.winkel AND ontkoppeld_op IS NULL); END;
