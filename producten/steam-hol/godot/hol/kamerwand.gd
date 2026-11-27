extends RefCounted
# Korrel en harde rand op de buiswand van de bovenste gang (Olaf 27 nov, #252, Iris 74f03c9 punt 1 voor een 9).
# De gangwand eronder is sinds #210 hard pixelwerk (hol/metsel.gd); de kamerbuis erboven was zachte 3D zonder korrel,
# dus twee stijlen in één strook. Nu krijgt de buiswand dezelfde harde taal, op hele spelpixels:
# - een donkere bovenrand van 1 spelpx waar de aarde overgaat in de buis, rafelig (hier en daar een hap omlaag), met
#   een smalle schaduw eronder, zodat de aarde over de buis hangt;
# - korrel: losse donkere en lichte spikkels van 1 spelpx;
# - steentjes van 2 x 1 of 2 x 2 met een lichte kop en een donkere voet, en hier en daar een barstje schuin omlaag;
# - korrel in klonten (dichte en kale plekken) en korte liggende laagjes, zodat het aarde leest en geen ruis;
# - een donkere lijn van 1 spelpx waar de wand de vloer raakt.
# Alleen op pixels die kamerwand_masker.gd als kale wand aanwijst (1 spelpx afstand tot stut, houweel, ton, fakkel en
# kistje in het kamerstuk zelf), dus nooit over decor. Alles vast per spelpixel (hash op de x in het hol), dus het
# loopt door over de kolomranden en flikkert niet. Getekend in het vaste beeld: kost alleen iets als dat opnieuw wordt
# getekend (graven, een put). Losse dingen in de kamer (wortels, rekjes, kamer_dingen) komen er daarna overheen.
# Bekeken: Rusty's Retirement (lat van Hats): aarde met harde spikkels van 1 pixel, steentjes met een lichte kop en
# donkere voet, en een harde donkere rand waar grond en ruimte elkaar raken.

const KOL := 16
const OPP := 8                 # het kamerstuk staat op y = OPP; rij y in het stuk is OPP + y in het hol
const RIJ_BOVEN := 4
const RIJ_ONDER := 12
const MASKER := preload("res://hol/kamerwand_masker.gd")

const DONKER := Color(0.16, 0.07, 0.05)       # warm bijna zwart, als de voeg van metsel.gd
const LICHT := Color(1.0, 0.92, 0.80)
const RAND_A := 0.62           # bovenrand, zo dekkend als de voeg in de gangwand
const SCHADUW_A := 0.20        # rij onder de bovenrand
const VLOER_A := 0.34          # lijn op de vloerrand
const SPIK_DONKER := 11        # kans in honderd per wandpixel
const SPIK_LICHT := 5
const SPIK_DONKER_A := 0.24
const SPIK_LICHT_A := 0.20
const STEEN_A := 0.30          # lijf van een steentje
const STEEN_VOET_A := 0.50
const STEEN_KOP_A := 0.30
const BARST_A := 0.42

static func masker(stuk: String) -> Array:
	return MASKER.MASKER.get(stuk, [])

static func wand(m: Array, x: int, y: int) -> bool:
	return x >= 0 and x < KOL and y >= 0 and y < m.size() and m[y][x] == "1"

static func teken(d: CanvasItem, k: int, stuk: String) -> void:
	for p in pixels(k, stuk):
		d.draw_rect(Rect2(p[0], OPP + p[1], 1, 1), p[2])

# alle pixels die op kamerkolom k komen: [x in het hol, rij in het stuk, kleur]; los van tekenen, zodat de toets ze kan nagaan
# Vast per kolom en stuk, dus één keer uitgerekend en bewaard: opnieuw tekenen (graven, een put) rekent niets meer.
static var _bewaard := {}
static func pixels(k: int, stuk: String) -> Array:
	var sleutel := "%d:%s" % [k, stuk]
	if not _bewaard.has(sleutel):
		_bewaard[sleutel] = _reken(k, stuk)
	return _bewaard[sleutel]

static func _reken(k: int, stuk: String) -> Array:
	var d := []
	var m := masker(stuk)
	if m.is_empty():
		return d
	var x0 := k * KOL
	for x in KOL:
		var hx := x0 + x
		var h := _hash(hx, 1)
		# bovenrand: harde donkere lijn; op ±1 op 5 pixels een hap van 1 spelpx omlaag, op ±1 op 9 geen schaduw
		if wand(m, x, RIJ_BOVEN):
			_pix(d, x0 + x, RIJ_BOVEN, DONKER, RAND_A)
			if wand(m, x, RIJ_BOVEN + 1):
				if h % 5 == 0:
					_pix(d, x0 + x, RIJ_BOVEN + 1, DONKER, RAND_A * 0.8)
				elif h % 9 != 1:
					_pix(d, x0 + x, RIJ_BOVEN + 1, DONKER, SCHADUW_A)
		if wand(m, x, RIJ_ONDER) and wand(m, x, RIJ_ONDER - 1):
			_pix(d, x0 + x, RIJ_ONDER, DONKER, VLOER_A)
		# korrel op de wand, niet op de rij direct onder de rand (daar zit de schaduw)
		for y in range(RIJ_BOVEN + 2, RIJ_ONDER):
			if not wand(m, x, y):
				continue
			# klonten in plaats van ruis (blinde lezer 27 nov: "gelijkmatig verspreid, leest als ruis"): per vak van
			# 5 x 3 spelpx een dichtheid 0, 1 of 2, dus plekken met dichte korrel naast kale stukken
			var dicht := _hash(int(floor(hx / 5.0)) * 13 + y / 3, 4) % 3
			var s := _hash(hx * 31 + y, 2) % 100
			if dicht == 0:
				s = 100
			elif dicht == 2:
				s = s / 2
			if s < SPIK_DONKER:
				_pix(d, x0 + x, y, DONKER, SPIK_DONKER_A)
			elif s < SPIK_DONKER + SPIK_LICHT:
				_pix(d, x0 + x, y, LICHT, SPIK_LICHT_A)
	_steentjes(d, k, m)
	_laagjes(d, k, m)
	return d

# Liggende streepjes van 3 tot 5 spelpx, per blok van 9 spelpx hooguit één: lagen in de aarde, geen ruis.
const LAAG_A := 0.28
static func _laagjes(d: Array, k: int, m: Array) -> void:
	var x0 := k * KOL
	for b in range(int(floor(float(x0) / 9.0)), int(floor(float(x0 + KOL - 1) / 9.0)) + 1):
		var h := _hash(b, 5)
		if h % 3 == 0:
			continue
		var lang := 3 + (h / 3) % 3
		var x := b * 9 + (h / 11) % 4 - x0
		var y := RIJ_BOVEN + 2 + (h / 53) % 6
		var ok := true
		for i in lang:
			if not wand(m, x + i, y):
				ok = false
		if ok:
			for i in lang:
				_pix(d, x0 + x + i, y, DONKER, LAAG_A)

# Steentjes en barstjes: per blok van 6 spelpx breed hooguit één, plek en maat vast uit de hash.
static func _steentjes(d: Array, k: int, m: Array) -> void:
	var x0 := k * KOL
	var b0 := int(floor(float(x0) / 6.0))
	var b1 := int(floor(float(x0 + KOL - 1) / 6.0))
	for b in range(b0, b1 + 1):
		var h := _hash(b, 3)
		var soort := h % 7      # 0..2 steentje, 3 barstje, rest niets
		if soort > 3:
			continue
		var hx := b * 6 + (h / 7) % 5
		var x := hx - x0
		var y := RIJ_BOVEN + 3 + (h / 37) % 5
		if soort == 3:
			var naar_rechts := (h / 211) % 2 == 0
			var lang := 2 + (h / 401) % 2
			var ok := true
			for j in lang:
				if not wand(m, x + (j if naar_rechts else -j), y + j):
					ok = false
			if ok:
				for j in lang:
					_pix(d, x0 + x + (j if naar_rechts else -j), y + j, DONKER, BARST_A)
			continue
		var w := 2
		var hg := 1 + soort % 2
		var ok := true
		for i in w:
			for j in hg + 1:
				if not wand(m, x + i, y + j):
					ok = false
		if not ok:
			continue
		for i in w:
			for j in hg:
				_pix(d, x0 + x + i, y + j, DONKER, STEEN_A)
			_pix(d, x0 + x + i, y + hg, DONKER, STEEN_VOET_A)
		_pix(d, x0 + x, y, LICHT, STEEN_KOP_A)

static func _pix(d: Array, x: int, y: int, c: Color, a: float) -> void:
	c.a = a
	d.append([x, y, c])

static func _hash(i: int, zout: int) -> int:
	var v := (i * 73856093) ^ (zout * 19349663) ^ 83492791
	v = (v ^ (v >> 13)) * 1274126177
	return absi(v ^ (v >> 16)) % 100000
