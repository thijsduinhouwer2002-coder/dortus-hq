# Hol 2.0 proef (Olaf, #388): de indeling van het hol en de vaste achtergrond.
# Maten uit producten/steam-hol/ontwerp-hol2/LEESMIJ.md punt 1, alles in spelpixels:
#   tuin 0-22, maaiveld 22-26, verdieping 1 26-70, balk 70-74, verdieping 2 74-118, balk 118-122, verdieping 3 ...
# Een "niveau" is een loopvlak: 0 = tuin (voeten op y 22), 1 = verdieping 1 (voeten op 70), 2 = verdieping 2 (118), ...
# De achtergrond wordt één keer getekend (Godot bewaart de tekenopdrachten), dus hij kost geen CPU per beeld.
extends Node2D

const TUIN := 22
const MAAI := 4
const VERD := 44
const BALK := 4
const LAD_B := 7

var breed := 1920
var n_verd := 3          # verdiepingen onder de tuin (de derde zie je alleen door te schuiven)
var ladders: Array = []  # [{x, boven (niveau), onder (niveau)}]
var vallen: Array = []   # [{x, niveau, soort ("luik"/"stekels"), open (s), kans}]
var kamers: Array = []   # [{x0, x1, niveau}]
var fakkels: Array = []  # [Vector2]
var bloemen: Array = []  # [{x, soort}]
var troon_x := 0
var troon_niveau := 2
var tex: Texture2D
var vak: Dictionary = {}

static func voet_y(niveau: int) -> int:
	if niveau <= 0:
		return TUIN
	return TUIN + MAAI + niveau * VERD + (niveau - 1) * BALK

static func hoogte_wereld(n: int) -> int:
	return voet_y(n) + BALK

# niveau bij een y in de wereld (voor klikken): het loopvlak waar die y boven ligt
func niveau_bij(y: float) -> int:
	if y < TUIN + MAAI:
		return 0
	for n in range(1, n_verd + 1):
		if y < voet_y(n) + BALK:
			return n
	return n_verd

func maak(w: int, n: int, rng: RandomNumberGenerator) -> void:
	breed = w
	n_verd = n
	troon_x = breed - 150
	# ladders: tuin naar 1 op twee plekken, en tussen elke twee verdiepingen twee ladders, verspringend
	ladders.clear()
	var stuk := breed / 6.0
	ladders.append({"x": int(stuk * 0.8), "boven": 0, "onder": 1})
	ladders.append({"x": int(stuk * 3.4), "boven": 0, "onder": 1})
	for v in range(1, n_verd):
		var a := 1.6 if v % 2 == 1 else 0.4
		ladders.append({"x": int(stuk * (a + 0.3)), "boven": v, "onder": v + 1})
		ladders.append({"x": int(stuk * (a + 3.1)), "boven": v, "onder": v + 1})
	# kamers met een stenen wand, tussen de kamers aarde
	kamers.clear()
	fakkels.clear()
	for v in range(1, n_verd + 1):
		var x := 30 + (v * 47) % 90
		while x < breed - 140:
			var lang := 150 + rng.randi_range(0, 160)
			var x1 := mini(x + lang, breed - 20)
			kamers.append({"x0": x, "x1": x1, "niveau": v})
			fakkels.append(Vector2(x + 8, voet_y(v) - 30))
			if x1 - x > 200:
				fakkels.append(Vector2(x1 - 12, voet_y(v) - 30))
			x = x1 + 40 + rng.randi_range(0, 60)
	# vallen: niet op of naast een ladder, niet bij de troon
	vallen.clear()
	for v in range(1, n_verd + 1):
		var aantal := 4 if v == 1 else 5
		var tries := 0
		while aantal > 0 and tries < 200:
			tries += 1
			var x := rng.randi_range(80, breed - 200)
			if _bezet(x, v):
				continue
			var soort := "luik" if rng.randf() < 0.55 else "stekels"
			vallen.append({"x": x, "niveau": v, "soort": soort, "open": 0.0, "kans": 0.3 if v == 1 else 0.55})
			aantal -= 1
	bloemen.clear()
	var bx := 6
	while bx < breed:
		var r := rng.randf()
		bloemen.append({"x": bx, "soort": "struik" if r < 0.25 else ("kool" if r < 0.4 else "bloem%d" % rng.randi_range(0, 2))})
		bx += rng.randi_range(14, 46)
	queue_redraw()

func _bezet(x: int, v: int) -> bool:
	for l in ladders:
		if (l.boven == v or l.onder == v) and absi(l.x - x) < 26:
			return true
	for t in vallen:
		if t.niveau == v and absi(t.x - x) < 40:
			return true
	return v == troon_niveau and x > troon_x - 60

func ladder_tussen(a: int, b: int, bij_x: float) -> Dictionary:
	var beste := {}
	var afst := INF
	for l in ladders:
		if (l.boven == a and l.onder == b) or (l.boven == b and l.onder == a):
			var d := absf(l.x + LAD_B / 2.0 - bij_x)
			if d < afst:
				afst = d
				beste = l
	return beste

func _tegel(naam: String, pos: Vector2) -> void:
	var v: Array = vak[naam]
	draw_texture_rect_region(tex, Rect2(pos, Vector2(v[2], v[3])), Rect2(v[0], v[1], v[2], v[3]))

func _vul(naam: String, r: Rect2) -> void:
	var v: Array = vak[naam]
	var y := r.position.y
	while y < r.end.y:
		var x := r.position.x
		var h := minf(v[3], r.end.y - y)
		while x < r.end.x:
			var w := minf(v[2], r.end.x - x)
			draw_texture_rect_region(tex, Rect2(x, y, w, h), Rect2(v[0], v[1], w, h))
			x += v[2]
		y += v[3]

func _draw() -> void:
	if tex == null:
		return
	var onder := hoogte_wereld(n_verd)
	# aarde onder het maaiveld, met een donkere rand rond de verdiepingen
	_vul("aarde", Rect2(0, TUIN, breed, onder - TUIN))
	for v in range(1, n_verd + 1):
		var y0 := voet_y(v) - VERD
		draw_rect(Rect2(0, y0, breed, VERD), Color(0.16, 0.11, 0.09, 0.55))
	for k in kamers:
		var y0 := voet_y(k.niveau) - VERD + 3
		_vul("wand", Rect2(k.x0, y0, k.x1 - k.x0, VERD - 3))
		draw_rect(Rect2(k.x0 - 2, y0 - 1, 2, VERD - 2), Color8(92, 66, 44))
		draw_rect(Rect2(k.x1, y0 - 1, 2, VERD - 2), Color8(92, 66, 44))
		draw_rect(Rect2(k.x0 - 2, y0 - 2, k.x1 - k.x0 + 4, 2), Color8(78, 56, 40))
	# vloeren (balken)
	_vul("vloer", Rect2(0, TUIN, breed, MAAI))
	for v in range(1, n_verd + 1):
		_vul("vloer", Rect2(0, voet_y(v), breed, BALK))
	# tuin: gras op het maaiveld, bloemen en struiken
	_vul("gras", Rect2(0, TUIN - 4, breed, 6))
	for b in bloemen:
		var v: Array = vak[b.soort]
		_tegel(b.soort, Vector2(b.x, TUIN - v[3] + 1))
	# ladders (gat in de vloer erachter donker)
	for l in ladders:
		var y0 := voet_y(l.boven) - 6
		var y1 := voet_y(l.onder)
		draw_rect(Rect2(l.x, voet_y(l.boven), LAD_B, BALK if l.boven > 0 else MAAI), Color8(20, 16, 20))
		_vul("ladder", Rect2(l.x, y0, LAD_B, y1 - y0))
	_tegel("troon", Vector2(troon_x, voet_y(troon_niveau) - 16))
