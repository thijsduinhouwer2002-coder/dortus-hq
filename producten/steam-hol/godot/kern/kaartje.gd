extends RefCounted
# Het kaartje voor upgrades (Olaf, 10 nov). Uitwerking van Sanne in platformen/steam/features.md, feature 5 ("het kaartje"):
# de keuze in een bezoek van 30 seconden, zonder melding en zonder venster buiten de strook.
# - kun je een upgrade betalen, dan staat er een klein muntje boven Gloop of de put (hol.gd tekent het, geen geluid);
# - klik op Gloop of de put: het paneel rechts wordt het kaartje (naam, uitleg, kost, "Buy", en "Undo" voor de bovenste stap);
# - Buy: muntjes vliegen van de schat naar het object en de kroniek krijgt de regel uit upgrades.koop_regel();
# - klik ernaast of 6 s niets: terug naar de kroniek.
# Statische functies zoals wachtrij.gd en afloop.gd; `s` is de strook. De toestand (kaart_soort, kaart_t) staat in strook.gd.
# De getallen en namen zijn van Bram (systemen/upgrades.gd); hier alleen tonen, kopen en terugdraaien.

const HOL := preload("res://hol/hol.gd")
const UPG := preload("res://systemen/upgrades.gd")
const OPEN_S := 6.0   # zo lang blijft het kaartje staan na de laatste klik
# Demo: begint met 66 goud, alsof het hol al even open is, en koopt rond 20 s Big Gloop: twee klikken, zoals een speler
# (Sanne, toets voor het kaartje: muntjes naar Gloop en de regel in de film van een minuut)
const DEMO_GOUD := 66
const DEMO_KLIK_T := 18.5
const DEMO_KOOP_T := 20.0

static func kan(s) -> bool:
	return s.hol != null and s.hol.upgrades != null

# kolom van Gloop (hij staat op een vaste plek, maar zo klopt het ook als hij ooit verhuist)
static func slijm_kol(s) -> int:
	return s.hol.pos_naar_cel(s.slijm.position).x

# Welke soort hoort bij een klik op spelpixel p: "slijm", "stekelput" of "".
static func soort_op(s, p: Vector2) -> String:
	if p.y < HOL.OPP:
		return ""
	var k: int = s.hol.pos_naar_cel(p).x
	if k == slijm_kol(s):
		return "slijm"
	if p.y >= HOL.GANG_BOVEN and s.hol.vallen.has(k):
		return "stekelput"
	return ""

# Wat het kaartje laat zien. Alles in het Engels zoals in het spel.
static func beschrijving(s, soort: String) -> Dictionary:
	var up = s.hol.upgrades
	var bew: String = s._bewoner()
	var d := {"soort": soort, "titel": "", "uitleg": "", "kost": -1, "kan": false, "tekort": 0, "terug": 0,
		"weg": soort == "stekelput"}   # een put kun je ook weghalen (controleur: anders was een put zetten onomkeerbaar)
	var v: Dictionary = up.volgende(soort)
	if v.is_empty():
		var laatste: String = UPG.STAPPEN[soort][UPG.MAX_NIVEAU - 1]["naam"]
		d.titel = laatste.replace("Gloop", bew) if soort == "slijm" else laatste
		d.uitleg = "All three bought."
	else:
		d.titel = String(v.naam).replace("Gloop", bew) if soort == "slijm" else String(v.naam)
		d.uitleg = String(v.uitleg)
		d.kost = int(v.kost)
		d.kan = up.kan_kopen(soort, s.hol.goud)
		d.tekort = maxi(0, int(v.kost) - int(s.hol.goud))
	d.terug = terug_bedrag(up, soort)
	return d

# Wat "Undo" teruggeeft: de volle prijs van de bovenste stap (balans.md), 0 als er niets gekocht is.
static func terug_bedrag(up, soort: String) -> int:
	var n: int = up.niveau(soort)
	if n <= 0:
		return 0
	return int(round(UPG.BASIS * pow(UPG.FACTOR, n - 1)))

static func open(s, soort: String, kol := -1) -> void:
	s.kaart_soort = soort
	s.kaart_kol = kol if kol >= 0 else _kol_van(s, soort)
	s.kaart_t = s.t
	ververs(s)
	s._muis_vlak(true)   # de knoppen moeten de muis vangen, ook zonder hover (Sanne)
	s.log_regel("HOL kaartje open %.1f: %s" % [s.t, soort])

static func dicht(s, toon := true) -> void:
	if s.kaart_soort == "":
		return
	s.log_regel("HOL kaartje dicht %.1f" % s.t)
	s.kaart_soort = ""
	s.tekst.kaart = {}
	s.tekst.queue_redraw()
	s._muis_vlak(s.tekst.hover)
	if toon:
		s._toon()   # wat in de wachtrij stond komt nu

static func ververs(s) -> void:
	s.tekst.kaart = beschrijving(s, s.kaart_soort) if s.kaart_soort != "" else {}
	s.tekst.goud = s.hol.goud
	s.tekst.queue_redraw()

static func koop(s) -> void:
	var soort: String = s.kaart_soort
	var up = s.hol.upgrades
	var rest: int = up.koop(soort, s.hol.goud)
	if rest < 0:
		return
	s.hol.goud = rest
	s.hol.munt_naar(s.kaart_kol, 4)
	s.log_regel("HOL koop %.1f: %s niveau %d, goud %d" % [s.t, soort, up.niveau(soort), s.hol.goud])
	dicht(s, false)   # eerst de eigen regel, anders flitst een oude regel 0 s voorbij (controleur kan-punt 1)
	_eigen_regel(s, up.koop_regel(soort, s._bewoner()))
	s.bewaar()

static func undo(s) -> void:
	var soort: String = s.kaart_soort
	var up = s.hol.upgrades
	var naam: String = String(UPG.STAPPEN[soort][up.niveau(soort) - 1]["naam"]) if up.niveau(soort) > 0 else ""
	var terug: int = up.verkoop(soort)
	if terug <= 0:
		return
	s.hol.goud += terug
	s.hol.munt_regen(s.kaart_kol, 4)   # het goud vliegt terug naar de schat
	s.log_regel("HOL undo %.1f: %s niveau %d, goud %d" % [s.t, soort, up.niveau(soort), s.hol.goud])
	dicht(s, false)
	if soort == "slijm":
		naam = naam.replace("Gloop", s._bewoner())
	_eigen_regel(s, "%s undone. +%d" % [naam, terug])
	s.bewaar()

# Put weghalen (vroeger: klik op de put). Zetten kost nog niets, dus er gaat ook niets terug; de upgrades horen bij
# de soort put, niet bij deze ene, en blijven dus staan.
static func weg(s) -> void:
	var k: int = s.kaart_kol
	if not s.hol.vallen.has(k):
		dicht(s)
		return
	s.hol.vallen.erase(k)
	s.hol.queue_redraw()
	s.log_regel("HOL put weg %.1f: kolom %d" % [s.t, k])
	dicht(s, false)
	_eigen_regel(s, "The Spike Pit is filled in.")
	s.bewaar()

# Je eigen klik krijgt meteen antwoord: de regel gaat voor alles en komt nu (geen 2,5 s wachten op de vorige regel).
static func _eigen_regel(s, r: String) -> void:
	if r == "":
		return
	s.wachtrij.push_front({"r": r, "binnen": false, "sinds": s.t, "soort": "koop"})
	s.regel_sinds = -100.0
	s._toon()

static func _kol_van(s, soort: String) -> int:
	if soort == "slijm":
		return slijm_kol(s)
	for k in s.hol.vallen:
		return int(k)
	return s.hol.schat_kol

# Een klik in het venster (vensterpixels). Geeft true als het kaartje de klik opving.
static func klik(s, pos: Vector2) -> bool:
	if not kan(s):
		return false
	if s.kaart_soort != "":
		if s.tekst.knop_koop.has_point(pos):
			koop(s)
			return true
		if s.tekst.knop_undo.has_point(pos):
			undo(s)
			return true
		if s.tekst.knop_weg.has_point(pos):
			weg(s)
			return true
		var was_kol: int = s.kaart_kol
		dicht(s)
		# klik ernaast sluit alleen (geen graven of put per ongeluk); op een ander object opent dat kaartje meteen
		var p0: Vector2 = (pos - s.hol.position) / s.schaal
		var ander := soort_op(s, p0)
		if ander == "" or s.hol.pos_naar_cel(p0).x == was_kol:
			return true
	var p: Vector2 = (pos - s.hol.position) / s.schaal
	var soort := soort_op(s, p)
	if soort == "":
		return false
	open(s, soort, s.hol.pos_naar_cel(p).x)
	return true

# Elke frame (goedkoop): kaartje dicht na 6 s, en het muntje boven Gloop en de put als je iets kunt kopen.
static func tik(s) -> void:
	if not kan(s):
		return
	if s.kaart_soort != "" and s.t - s.kaart_t > OPEN_S:
		dicht(s)
	var up = s.hol.upgrades
	var munt: Array = []
	if up.kan_kopen("slijm", s.hol.goud):
		munt.append(slijm_kol(s))
	if up.kan_kopen("stekelput", s.hol.goud):
		for k in s.hol.vallen:
			munt.append(int(k))
	if munt != s.hol.koop_munt:
		s.hol.koop_munt = munt
		s.hol.queue_redraw()

static func demo_stap(s) -> void:
	if s.demo_koop == 0 and s.t >= DEMO_KLIK_T and kan(s):
		s.demo_koop = 1
		s.log_regel("HOL demo klik op Gloop")
		open(s, "slijm")
	elif s.demo_koop == 1 and s.t >= DEMO_KOOP_T:
		s.demo_koop = 2
		if s.kaart_soort == "slijm":
			s.log_regel("HOL demo klik op Buy")
			koop(s)
