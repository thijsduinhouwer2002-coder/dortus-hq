extends RefCounted
# Demo-einde (Olaf, 13 nov 2026; ontwerp in producten/steam-hol/ontwerp.md, sectie Demo-einde).
# 17 nov 2026 (Olaf): einde op inhoud, niet op de klok (Sanne 04:02 na Fenna verhaal 23, features.md "Demo-einde op inhoud").
# De gratis Steam-demo is hetzelfde spel. Hij eindigt pas als er echt niets nieuws meer komt: hol-niveau 12 (DEMO_MAX)
# én alle 6 winkeldingen gekocht (2 soorten x 3 stappen). Dan één vriendelijke regel in de kroniek en stopt alleen groeien:
# graven, kopen en upgrades. Helden, Gloop, goud en winst terwijl je weg bent lopen door. Undo en Remove blijven werken.
# Het einde is blijvend (veld demo_klaar in de save): wie daarna een stap terugverkoopt, kan hem niet opnieuw kopen en
# krijgt de regel niet nog eens. Geen aftelklok, geen melding, geen "koop nu".
# De demo herkent het spel aan de Godot-feature `steamdemo` (eigen export-preset) of het startargument steamdemo=1.
# demo_einde=<s> is alleen een testvlag: dan eindigt de demo ook na s seconden open tijd (toetsen op de runner).
# Zonder steamdemo is er nooit een einde. speeltijd_s telt nog wel (logregel, en voor de testvlag).
# Statisch zoals wachtrij.gd en kaartje.gd. De pure functies (zonder strook) staan in toets_systemen.gd getoetst.

const HOL_NIVEAU := preload("res://systemen/hol_niveau.gd")
const UPG := preload("res://systemen/upgrades.gd")
const GEEN_KLOK := -1.0   # standaard: geen klok; demo_einde=<s> zet een testgrens
const REGEL_EINDE := "That's the demo. Your hole keeps going."   # 39 tekens
const REGEL_START := "Demo over. The full game keeps it all."    # 38 tekens, past ook op 96 px
const KAART := "Full game: keep this hole."                      # op het kaartje in plaats van Buy

# --- pure functies (getoetst) ---

# Is alle inhoud van de demo op: hol-niveau minstens DEMO_MAX én elke soort op de hoogste stap.
# niveaus = upgrades.niveaus ({"slijm": n, "stekelput": n}); ontbreekt een soort, dan is hij niet gekocht.
static func inhoud_op(hol_niveau: int, niveaus: Dictionary) -> bool:
	if hol_niveau < HOL_NIVEAU.DEMO_MAX:
		return false
	for soort in UPG.SOORTEN:
		if int(niveaus.get(soort, 0)) < UPG.MAX_NIVEAU:
			return false
	return true

# Alleen voor de testvlag demo_einde=<s>: is de testgrens voorbij. Zonder grens (GEEN_KLOK) nooit.
static func klok_voorbij(speeltijd: float, grens: float) -> bool:
	return grens > 0.0 and speeltijd >= grens

# Moet de demo nu eindigen (nog los van of hij al eerder eindigde).
static func voorbij(steamdemo: bool, hol_niveau: int, niveaus: Dictionary, speeltijd: float = 0.0, grens: float = GEEN_KLOK) -> bool:
	return steamdemo and (inhoud_op(hol_niveau, niveaus) or klok_voorbij(speeltijd, grens))

# De regel bij elke start van een demo die al voorbij is, anders "".
static func regel_bij_start(steamdemo: bool, demo_klaar: bool) -> String:
	return REGEL_START if steamdemo and demo_klaar else ""

# Is dit de demo-versie: feature uit de export-preset, of het argument steamdemo=1.
static func is_demo(args: PackedStringArray) -> bool:
	if OS.has_feature("steamdemo"):
		return true
	return args.has("steamdemo=1")

# --- met de strook `s` (velden steamdemo, demo_grens, speeltijd_s in strook.gd) ---

static func niveaus_van(s) -> Dictionary:
	if s.hol == null or s.hol.upgrades == null:
		return {}
	return s.hol.upgrades.niveaus

static func klaar(s) -> bool:
	return s.steamdemo and s.demo_klaar

# Elke frame vanuit strook._process: open tijd tellen, en één keer de regel als de inhoud op is.
static func tik(s, delta: float) -> void:
	s.speeltijd_s += delta
	if not s.steamdemo or s.demo_klaar:
		return
	var n: int = HOL_NIVEAU.niveau(s.faam)
	if not voorbij(true, n, niveaus_van(s), s.speeltijd_s, s.demo_grens):
		return
	s.demo_klaar = true
	s.log_regel("HOL demo voorbij na %d s speeltijd (hol %d, winkel %s)" % [int(s.speeltijd_s), n, str(niveaus_van(s))])
	s._kroniek(REGEL_EINDE)
	if s.kaart_soort != "":
		preload("res://kern/kaartje.gd").ververs(s)   # een open kaartje zet meteen om (geen Buy meer), controleur 13 nov
	s.tekst.queue_redraw()
	s.bewaar()

# Na het laden: bij elke start na het einde één keer de startregel bovenaan.
static func bij_start(s) -> void:
	if s.steamdemo:
		s.log_regel("HOL demo: speeltijd %d s, hol %d, winkel %s, klaar %s" % [int(s.speeltijd_s), HOL_NIVEAU.niveau(s.faam), str(niveaus_van(s)), str(s.demo_klaar)])
	var r := regel_bij_start(s.steamdemo, s.demo_klaar)
	if r != "":
		s.kroniek.erase(r)   # de vorige startregel eruit, zodat hij niet bij elke start opnieuw in de geschiedenis stapelt
		s._kroniek(r)

# Vraag dit vóór graven of kopen. Geeft true (en logt) als het geweigerd wordt.
static func weiger(s, wat: String) -> bool:
	if not klaar(s):
		return false
	s.log_regel("HOL demo voorbij: graven/kopen geweigerd (%s)" % wat)
	return true
