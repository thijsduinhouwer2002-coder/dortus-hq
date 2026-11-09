-- D1-schema voor TikTok Shop naar je boekhouding. Ontwerp: ontwerp-d1-worker.md (punt 4).
-- Gewone tabellen (geen WITHOUT ROWID), zodat opruimen met rowid IN (...) werkt.
CREATE TABLE IF NOT EXISTS winkels (
  id TEXT PRIMARY KEY,
  shop_id TEXT NOT NULL,
  shop_cipher TEXT NOT NULL,
  tokens TEXT,                       -- versleuteld (AES-GCM), nooit leesbaar
  token_versie INTEGER NOT NULL DEFAULT 0,
  administratie TEXT,
  instellingen TEXT,                 -- JSON
  markering INTEGER,
  winkelfout TEXT,
  volgende_run INTEGER NOT NULL DEFAULT 0,
  snel_teller INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS winkels_volgende_run ON winkels(volgende_run);

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
