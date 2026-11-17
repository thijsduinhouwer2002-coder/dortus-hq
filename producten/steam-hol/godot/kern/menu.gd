extends RefCounted
# Rechtsklikmenu (Olaf 17 nov 2026, demolijst nr 12; ontwerp in producten/steam-hol/ontwerp.md, kopje Rechtsklikmenu).
# Het menu is een soort kaartje (kaart_soort "menu") in het paneel rechts: zelfde vak, letters en knoppen als het
# upgradekaartje (kern/kaartje.gd, kern/tekst.gd _draw_kaart). Knoppen: 96, 120, 160 (hoogte van de strook), Feedback
# (alleen als FORUM_URL gevuld is) en Quit. In de demo een grijze regel over de save (Sem M1b, CONCEPT, Thijs kiest).
# Klik ernaast, nog een rechtsklik of 6 s niets: dicht (de 6 s komen uit kaartje.gd tik). Geen Esc: het venster
# krijgt nooit toetsenbordfocus (project.godot no_focus=true), controleur 17 nov.
# Statisch zoals kaartje.gd; `s` is de strook.

const HOOGTES := [96, 120, 160]
const TITEL := "Het Hol"
const SAVE_REGEL := "Your save goes to the full game."   # Sem M1b (32 tekens), CONCEPT in platformen/steam/teksten-thijs.md
# Leeg tot Thijs het subforum "Demo feedback" heeft (lijst-thijs); dan staat de knop er vanzelf.
const FORUM_URL := ""

static func is_open(s) -> bool:
	return s.kaart_soort == "menu"

# Wat het paneel toont. Velden zoals kaartje.beschrijving (kost -1, terug 0, geen weg), plus de menuvelden.
static func beschrijving(s) -> Dictionary:
	return {"soort": "menu", "menu": true, "titel": TITEL,
		"uitleg": SAVE_REGEL if s.steamdemo else "",
		"kost": -1, "kan": false, "tekort": 0, "terug": 0, "weg": false,
		"hoogtes": HOOGTES, "nu": int(s.hoogte), "feedback": FORUM_URL != ""}

static func open(s) -> void:
	s.kaart_gekocht = false
	s.kaart_soort = "menu"
	s.kaart_kol = -1
	s.kaart_t = s.t
	s.tekst.kaart = beschrijving(s)
	s.tekst.queue_redraw()
	s._muis_vlak(true)
	s.log_regel("HOL menu open %.1f" % s.t)

# Rechtsklik: open het menu, of sluit het als het al open is. Een open upgradekaartje gaat eerst netjes dicht.
static func wissel(s) -> void:
	if is_open(s):
		s.KAARTJE.dicht(s)
		return
	if s.kaart_regel != "":
		# net gekocht: de koopregel moet eerst gezien worden (wachtrij.gd: alleen geziene regels in de kroniek), dus deze
		# rechtsklik sluit alleen het kaartje; de volgende opent het menu (controleur 17 nov punt 2)
		s.KAARTJE.dicht(s)
		return
	if s.kaart_soort != "":
		s.KAARTJE.dicht(s, false)
	open(s)

# Klik (vensterpixels) terwijl het menu open is. Geeft altijd true: een klik ernaast sluit alleen, zoals bij het kaartje.
static func klik(s, pos: Vector2) -> bool:
	for k in s.tekst.knop_menu:
		var r: Rect2 = k[0]
		if r.has_point(pos):
			doe(s, String(k[1]))
			return true
	s.KAARTJE.dicht(s)
	return true

# Een knop uitvoeren: "96", "120", "160", "feedback" of "quit".
static func doe(s, actie: String) -> void:
	s.log_regel("HOL menu: %s" % actie)
	if actie.is_valid_int() and HOOGTES.has(int(actie)):
		var h := int(actie)
		if h == int(s.hoogte):
			s.KAARTJE.dicht(s)
		else:
			s.zet_hoogte(h)   # bewaart, sluit het kaartje en laadt de strook opnieuw
	elif actie == "feedback":
		s.KAARTJE.dicht(s)
		if FORUM_URL != "":
			OS.shell_open(link(FORUM_URL, Engine.has_singleton("Steam")))
	elif actie == "quit":
		s.stop()

# Met Steam erbij in de overlay (steam://openurl/), anders gewoon in de browser.
static func link(url: String, steam: bool) -> String:
	return "steam://openurl/" + url if steam else url
