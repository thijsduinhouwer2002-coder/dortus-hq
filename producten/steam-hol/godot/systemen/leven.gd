extends Node2D
# Klein leven in het hol (Olaf, 25 nov, issue #97, bouwblad H): om de 5 tot 15 s één klein ding dat vanzelf beweegt,
# nooit twee tegelijk, rustig en zonder geflits. Geen tekst, geen geluid. Vijf soorten:
# - stofje: drie stofjes zweven traag omhoog in het licht van de fakkel;
# - goudstof: drie stofjes stijgen op uit het licht boven de schat;
# - vleermuis: een hangende vleermuis wiegt even aan zijn pootjes (zijn eigen beeld, vleermuis.gd wieg());
# - worm en mot (#190): de bladen van Mila (#179, Daan #180 ja), zie leven_beest.gd.
# Eén ding tegelijk per hol, dus ook hooguit één worm per verdieping (kan Daan #180). Gloop knippert los hiervan.
# Hangt in het hol vóór de lichtlaag (licht.gd), zodat het ding even donker is als de plek waar het is.
# Alleen een nieuw beeld tijdens een stofje (12 per s); tussendoor tekent dit niets.

const KOL := 16
const LICHT := preload("res://systemen/licht.gd")
const BEEST := preload("res://systemen/leven_beest.gd")
const SOORTEN := ["stofje", "goudstof", "vleermuis", "worm", "mot"]
const DUUR := {"stofje": 4.5, "goudstof": 4.5, "vleermuis": 3.0, "worm": 4.2, "mot": 4.5}
const WISSEL_S := 20.0   # wissel=leven: worm en mot om de 20 s aan en uit op de klok (CPU binnen één run, #190)
const FPS := 12.0

const STOFJE := Color(1.0, 0.94, 0.78)
const GOUDSTOF := Color(1.0, 0.86, 0.48)

var h
var rng := RandomNumberGenerator.new()
var wacht := 6.0
var soort := ""
var t := 0.0
var plek := Vector2.ZERO
var vorige := ""
var beeld_t := 0.0
var klok := 0.0                # spelseconden sinds de start (voor de logregel)
var gedaan := {}               # soort -> aantal (toetsen en meetregel)
var licht_kleur := Color.WHITE # licht op de plek van het ding (licht.gd), want leven tekent boven het vaste beeld
var beest = null               # leven_beest.gd: bladen van worm en mot (null = geen blad, dan komen ze niet)
var beeld_nu := -1             # laatst getekende stand van worm of mot (alleen opnieuw tekenen als die verandert)
var wissel := ""               # wissel=leven of wissel=nep (startargument): zie WISSEL_S
var _wissel_was := true        # mogen worm en mot nu (wissel=nep: altijd)
var _blok_aan := true          # klokblok aan of uit (voor de regel in de uitvoer)
var beurten := 0               # tekenbeurten van deze laag (toets #190: met worm en mot niet meer dan zonder)
var proef := ""                # leven_proef=worm|mot: alleen dat ding, om de 2 s (alleen om te keuren en te filmen)

static func maak_in(hol, zaad: int) -> Node2D:
	var l := Node2D.new()
	l.set_script(load("res://systemen/leven.gd"))
	l.name = "Leven"
	l.h = hol
	if zaad != 0:
		l.rng.seed = zaad * 97 + 13
	else:
		l.rng.randomize()
	l.wacht = l.rng.randf_range(5.0, 15.0)
	l.beest = BEEST.laad()
	for a in OS.get_cmdline_user_args():
		if a == "wissel=leven" or a == "wissel=nep":
			l.wissel = a.split("=")[1]
		if a.begins_with("leven_proef="):
			l.proef = a.split("=")[1]
			l.wacht = 2.0
	hol.add_child(l)
	return l

func _process(delta: float) -> void:
	if h == null or h.kolommen <= 0:
		return
	klok += delta
	if wissel != "":
		_wissel_klok()
	if soort == "":
		wacht -= delta
		if wacht <= 0.0:
			_begin()
		return
	t += delta
	beeld_t -= delta
	if t >= float(DUUR[soort]):
		soort = ""
		wacht = 2.0 if proef != "" else rng.randf_range(5.0, 15.0)
		beeld_nu = -1
		queue_redraw()   # één keer leeg
		return
	if soort == "worm":   # alleen bij een nieuwe stand of tijdens het in- en uitfaden
		var st: int = BEEST.worm_stand(t, DUUR[soort])
		if st != beeld_nu:
			beeld_nu = st
			beurten += 1
			queue_redraw()
		return
	if beeld_t <= 0.0 and soort != "vleermuis":   # de vleermuis tekent zichzelf
		beeld_t = 1.0 / FPS
		beurten += 1
		queue_redraw()

# worm en mot mogen nu? (geen blad, of wissel=leven in een uit-blok: niet)
func beest_mag() -> bool:
	return beest != null and _wissel_was

func _wissel_klok() -> void:
	var aan := int(Time.get_unix_time_from_system() / WISSEL_S) % 2 == 0
	if aan != _blok_aan:
		_blok_aan = aan
		_wissel_was = aan or wissel == "nep"
		var sc := get_tree().current_scene   # speltijd van de strook, zoals de HOL zicht-regels (cpu_stenen.py)
		var st: float = float(sc.get("t")) if sc != null and sc.get("t") != null else klok
		print("HOL wissel leven %s unix=%.2f t=%.2f pad=Hol" % ["aan" if aan else "uit", Time.get_unix_time_from_system(), st])

func _begin() -> void:
	var keuze: Array = SOORTEN.duplicate()
	if proef != "":   # met wissel=leven: in een uit-blok niets (zwaarste proef: elke 2 s dit ding, tegen niets)
		keuze = [proef] if beest_mag() else []
	elif not beest_mag():
		keuze.erase("worm")
		keuze.erase("mot")
	if keuze.size() > 1:
		keuze.erase(vorige)   # nooit twee keer hetzelfde na elkaar; eigen rng, zodat een film met zaad gelijk blijft
	var start := rng.randi_range(0, keuze.size() - 1)
	for i in keuze.size():
		var s: String = keuze[(start + i) % keuze.size()]
		var p = kies_plek(h, s)
		if p == null:
			continue
		if s == "vleermuis":
			p = vleermuis(h).wieg()
			if p == null:
				continue
		if s == "worm":
			p = BEEST.worm_plek(h, rng)
			if p == null:
				continue
		soort = s
		beeld_nu = -1
		vorige = s
		plek = p
		licht_kleur = LICHT.kleur_op(h, p) if h.get_node_or_null("Gloed") != null else Color.WHITE
		t = 0.0
		beeld_t = 0.0
		gedaan[s] = int(gedaan.get(s, 0)) + 1
		var st = h.get_parent()
		if st != null and st.has_method("log_regel"):
			st.log_regel("HOL leven %s t=%.1f x=%d y=%d" % [s, klok, int(p.x), int(p.y)])
		return
	wacht = 3.0   # nergens plek: straks nog eens

static func vleermuis(hol):
	return hol.get_node_or_null("Vleermuis")

# waar kan dit ding? null = nergens (geen fakkel, of geen vleermuis die kan wiegen)
static func kies_plek(hol, s: String):
	match s:
		"stofje":
			var fk: int = hol.ingang_kol + 1
			if fk < hol.kolommen and fk < hol.schat_kol:
				return LICHT.fakkel_punt(hol)
		"goudstof":
			if hol.schat_kol < hol.kolommen:
				return Vector2(hol.schat_kol * KOL + 4, 30)
		"vleermuis":
			var v = vleermuis(hol)
			if v != null and v.has_method("kan_wiegen") and v.kan_wiegen():
				return Vector2.ZERO   # de echte plek geeft wieg()
		"worm":
			if not BEEST.worm_kolommen(hol).is_empty():
				return Vector2.ZERO   # de echte plek geeft worm_plek() (willekeurig, daarom niet hier)
		"mot":
			var fk2: int = hol.ingang_kol + 1
			if fk2 < hol.kolommen and fk2 < hol.schat_kol:
				return LICHT.fakkel_punt(hol)
	return null

# in en uit faden over de eerste en laatste 0,6 s
func _dek(d: float) -> float:
	return clampf(minf(t / 0.6, (d - t) / 0.6), 0.0, 1.0)

func _px(p: Vector2, c: Color) -> void:
	var m := Color(c.r * licht_kleur.r, c.g * licht_kleur.g, c.b * licht_kleur.b, c.a)
	draw_rect(Rect2(p.floor(), Vector2.ONE), m)

func _draw() -> void:
	match soort:
		"stofje": _teken_stof(STOFJE, 6.0, 2.2)
		"goudstof": _teken_stof(GOUDSTOF, 8.0, 2.6)
		"worm": beest.teken_worm(self, plek, t, DUUR["worm"])
		"mot": beest.teken_mot(self, plek, t, DUUR["mot"])

func _teken_stof(kleur: Color, breed: float, stijg: float) -> void:
	var d: float = DUUR[soort]
	for i in 3:
		var u := t - i * 0.7
		if u < 0.0:
			continue
		var p := plek + Vector2(-breed + i * breed + sin(u * 1.3 + i) * 2.0, 6 - u * stijg)
		var c := kleur
		c.a = 0.85 * _dek(d) * clampf(u / 0.5, 0.0, 1.0)
		_px(p, c)
