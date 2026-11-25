extends Node2D
# Klein leven in het hol (Olaf, 25 nov, issue #97, bouwblad H): om de 5 tot 15 s één klein ding dat vanzelf beweegt,
# nooit twee tegelijk, rustig en zonder geflits. Geen tekst, geen geluid. Vier soorten:
# - stofje: drie stofjes zweven traag omhoog in het licht van de fakkel;
# - worm: een worm steekt zijn kop uit de aarde, kijkt links en rechts en zakt terug;
# - kruimels: een paar korreltjes aarde vallen van het plafond van de gang en stuiven zacht op de vloer;
# - mot: een motje fladdert een paar rondjes om de vlam.
# Hangt in het hol vóór de lichtlaag (licht.gd), zodat het ding even donker is als de plek waar het is.
# Alleen een nieuw beeld tijdens een ding (12 per s); tussendoor tekent dit niets.

const KOL := 16
const H := 40
const OPP := 8
const GANG_BOVEN := 24
const VLOER := 37
const LICHT := preload("res://systemen/licht.gd")
const SOORTEN := ["stofje", "worm", "kruimels", "mot"]
const DUUR := {"stofje": 4.5, "worm": 3.8, "kruimels": 2.4, "mot": 3.6}
const FPS := 12.0

const WORM := Color(0.93, 0.58, 0.62)
const WORM_ROND := Color(0.42, 0.18, 0.22)
const WORM_KOP := Color(1.0, 0.72, 0.74)
const GAT := Color(0.16, 0.08, 0.06)
const KRUIMEL := Color(0.86, 0.62, 0.44)   # lichter dan de gang, anders zie je ze niet (GEZIEN op 120 px)
const STOF := Color(0.95, 0.80, 0.64)
const STOFJE := Color(1.0, 0.94, 0.78)
const MOT := Color(0.96, 0.92, 0.82)

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
	hol.add_child(l)
	return l

func _process(delta: float) -> void:
	if h == null or h.kolommen <= 0:
		return
	klok += delta
	if soort == "":
		wacht -= delta
		if wacht <= 0.0:
			_begin()
		return
	t += delta
	beeld_t -= delta
	if t >= float(DUUR[soort]):
		soort = ""
		wacht = rng.randf_range(5.0, 15.0)
		queue_redraw()   # één keer leeg
		return
	if beeld_t <= 0.0:
		beeld_t = 1.0 / FPS
		queue_redraw()

func _begin() -> void:
	var keuze: Array = SOORTEN.duplicate()
	keuze.erase(vorige)   # nooit twee keer hetzelfde na elkaar; eigen rng, zodat een film met zaad gelijk blijft
	var start := rng.randi_range(0, keuze.size() - 1)
	for i in keuze.size():
		var s: String = keuze[(start + i) % keuze.size()]
		var p = kies_plek(h, s, rng)
		if p != null:
			soort = s
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

# waar kan dit ding? null = nergens (bijvoorbeeld geen fakkel of geen dichte aarde)
static func kies_plek(hol, s: String, r: RandomNumberGenerator):
	var fk: int = hol.ingang_kol + 1
	var fakkel: bool = fk < hol.kolommen and fk < hol.schat_kol
	match s:
		"stofje", "mot":
			if not fakkel:
				return null
			return LICHT.fakkel_punt(hol)
		"worm":
			var k := _kolom(hol, r, func(k): return not hol.boven[k] and k != hol.ingang_kol and k < hol.schat_kol - 2)
			if k < 0:
				return null
			return Vector2(k * KOL + r.randi_range(4, 11), r.randi_range(16, 20))
		"kruimels":
			var k := _kolom(hol, r, func(k): return hol.gang[k] and not hol.boven[k] and k != hol.ingang_kol \
					and not hol.vallen.has(k) and k < hol.schat_kol - 2)
			if k < 0:
				return null
			return Vector2(k * KOL + r.randi_range(4, 11), GANG_BOVEN + 1)
	return null

static func _kolom(hol, r: RandomNumberGenerator, ok: Callable) -> int:
	var lijst: Array = []
	for k in range(1, mini(hol.kolommen, hol.max_kol + 1)):
		if ok.call(k):
			lijst.append(k)
	if lijst.is_empty():
		return -1
	return lijst[r.randi_range(0, lijst.size() - 1)]

# in en uit faden over de eerste en laatste 0,6 s
func _dek(d: float) -> float:
	return clampf(minf(t / 0.6, (d - t) / 0.6), 0.0, 1.0)

var licht_kleur := Color.WHITE   # licht op de plek van het ding (licht.gd), want leven tekent boven het vaste beeld

func _px(p: Vector2, c: Color, w := 1.0, hh := 1.0) -> void:
	var m := Color(c.r * licht_kleur.r, c.g * licht_kleur.g, c.b * licht_kleur.b, c.a)
	draw_rect(Rect2(p.floor(), Vector2(w, hh)), m)

func _draw() -> void:
	match soort:
		"stofje": _teken_stof()
		"worm": _teken_worm()
		"kruimels": _teken_kruimels()
		"mot": _teken_mot()

func _teken_stof() -> void:
	var d: float = DUUR["stofje"]
	for i in 3:
		var u := t - i * 0.7
		if u < 0.0:
			continue
		var p := plek + Vector2(-6 + i * 6 + sin(u * 1.3 + i) * 2.0, 6 - u * 2.2)
		var c := STOFJE
		c.a = 0.85 * _dek(d) * clampf(u / 0.5, 0.0, 1.0)
		_px(p, c)

func _teken_worm() -> void:
	var d: float = DUUR["worm"]
	# hoe ver hij eruit is: 0 tot 4 spelpixels
	var uit := 0.0
	if t < 0.8:
		uit = t / 0.8 * 4.0
	elif t < 2.8:
		uit = 4.0
	elif t < 3.4:
		uit = (3.4 - t) / 0.6 * 4.0
	var gat := GAT
	gat.a = clampf(minf(t / 0.3, (d - t) / 0.4), 0.0, 1.0)
	_px(plek + Vector2(-1, 0), gat, 4, 1)
	var n := int(round(uit))
	if n <= 0:
		return
	var kijk := 0
	if t >= 0.8 and t < 2.8:
		kijk = int([0, -1, 0, 1][int((t - 0.8) / 0.5) % 4])
	for j in n:
		var y := plek.y - 1 - j
		var dx := kijk if j >= n - 2 else 0
		var x := plek.x + dx
		_px(Vector2(x - 1, y), WORM_ROND)
		_px(Vector2(x + 2, y), WORM_ROND)
		_px(Vector2(x, y), WORM_KOP if j == n - 1 else WORM, 2, 1)
	_px(Vector2(plek.x + kijk, plek.y - 1 - n), WORM_ROND, 2, 1)

func _teken_kruimels() -> void:
	for i in 3:
		var u := t - i * 0.18
		if u < 0.0:
			continue
		var x: float = plek.x + [0, 2, -1][i]
		var y := plek.y + 0.5 * 30.0 * u * u
		if y < VLOER:
			_px(Vector2(x, y), KRUIMEL)
		elif u < sqrt(2.0 * (VLOER - plek.y) / 30.0) + 0.45:
			var s := STOF
			s.a = 0.7
			_px(Vector2(x - 1, VLOER - 1), s, 3, 1)

func _teken_mot() -> void:
	var d: float = DUUR["mot"]
	var p := plek + Vector2(cos(t * 3.4) * 6.0, sin(t * 6.8) * 2.5 - 4.0)
	var c := MOT
	c.a = _dek(d)
	if int(t * 10.0) % 2 == 0:
		_px(p + Vector2(-1, 0), c, 3, 1)   # vleugels open
	else:
		_px(p, c, 1, 1)
		_px(p + Vector2(0, -1), c, 1, 1)
