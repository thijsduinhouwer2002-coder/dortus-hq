extends RefCounted
# Demo-einde (Olaf, 13 nov 2026; ontwerp in producten/steam-hol/ontwerp.md, sectie Demo-einde, controleur akkoord ronde 2).
# De gratis Steam-demo is hetzelfde spel. Na 2 uur open tijd (speeltijd_s in de save, alleen tijd met het spel open)
# komt één vriendelijke regel in de kroniek en stopt alleen groeien: graven, kopen en upgrades. Helden, Gloop, goud en
# winst terwijl je weg bent lopen gewoon door. Undo en Remove blijven werken. Geen aftelklok, geen melding, geen "koop nu".
# De demo herkent het spel aan de Godot-feature `steamdemo` (eigen export-preset) of het startargument steamdemo=1;
# demo_einde=<s> zet de grens lager voor de toets. Zonder steamdemo is er nooit een einde.
# Statisch zoals wachtrij.gd en kaartje.gd. De pure functies (zonder strook) staan in toets_systemen.gd getoetst.

const GRENS_S := 7200.0
const REGEL_EINDE := "That's the demo. Your hole keeps going."   # 39 tekens
const REGEL_START := "Demo over. The full game keeps it all."    # 38 tekens, past ook op 96 px
const KAART := "Full game: keep this hole."                      # op het kaartje in plaats van Buy

# --- pure functies (getoetst) ---

static func voorbij(steamdemo: bool, speeltijd: float, grens: float = GRENS_S) -> bool:
	return steamdemo and speeltijd >= grens

# De regel als de grens in dit stukje tijd gepasseerd wordt (van voor naar na), anders "". Zo komt hij precies één keer.
static func regel_bij_einde(steamdemo: bool, voor: float, na: float, grens: float = GRENS_S) -> String:
	if steamdemo and voor < grens and na >= grens:
		return REGEL_EINDE
	return ""

# De regel bij elke start van een demo die al voorbij is, anders "".
static func regel_bij_start(steamdemo: bool, speeltijd: float, grens: float = GRENS_S) -> String:
	return REGEL_START if voorbij(steamdemo, speeltijd, grens) else ""

# Is dit de demo-versie: feature uit de export-preset, of het argument steamdemo=1.
static func is_demo(args: PackedStringArray) -> bool:
	if OS.has_feature("steamdemo"):
		return true
	return args.has("steamdemo=1")

# --- met de strook `s` (velden steamdemo, demo_grens, speeltijd_s in strook.gd) ---

static func klaar(s) -> bool:
	return voorbij(s.steamdemo, s.speeltijd_s, s.demo_grens)

# Elke frame vanuit strook._process: open tijd tellen, en de regel op het moment dat de grens voorbij gaat.
static func tik(s, delta: float) -> void:
	var voor: float = s.speeltijd_s
	s.speeltijd_s += delta
	var r := regel_bij_einde(s.steamdemo, voor, s.speeltijd_s, s.demo_grens)
	if r != "":
		s.log_regel("HOL demo voorbij na %d s speeltijd" % int(s.speeltijd_s))
		s._kroniek(r)
		if s.kaart_soort != "":
			preload("res://kern/kaartje.gd").ververs(s)   # een open kaartje zet meteen om (geen Buy meer), controleur 13 nov
		s.tekst.queue_redraw()
		s.bewaar()

# Na het laden: bij elke start na het einde één keer de startregel bovenaan.
static func bij_start(s) -> void:
	if s.steamdemo:
		s.log_regel("HOL demo: speeltijd %d s, grens %d s" % [int(s.speeltijd_s), int(s.demo_grens)])
	var r := regel_bij_start(s.steamdemo, s.speeltijd_s, s.demo_grens)
	if r != "":
		s.kroniek.erase(r)   # de vorige startregel eruit, zodat hij niet bij elke start opnieuw in de geschiedenis stapelt
		s._kroniek(r)

# Vraag dit vóór graven of kopen. Geeft true (en logt) als het geweigerd wordt.
static func weiger(s, wat: String) -> bool:
	if not klaar(s):
		return false
	s.log_regel("HOL demo voorbij: graven/kopen geweigerd (%s)" % wat)
	return true
