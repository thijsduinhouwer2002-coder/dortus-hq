extends RefCounted
# Grote robijnen voor stap 7 tot 9 (Olaf 27 nov, issue #298; Iris #286 punt 1: "stap 7 tot 9 maken één gouden ruitje
# van ±5 px rood; wie niet keek bij de koop, ziet het daarna niet").
# De kleine rij stenen (stap_teken.gd) blijft, maar elke koop vanaf stap 7 zet nu ook een grote geslepen robijn neer,
# zo groot als Gloops kroon, met een zachte rode gloed eromheen, zodat je hem op 1x ook een minuut later nog ziet:
# - Gloop: op de gouden rand van zijn troon, links en rechts tegelijk (midden boven staat zijn hoedentoren ervoor).
#   Stap 7 op de twee hoekbollen, stap 8 ook op de armleuningen, stap 9 ook bij de voeten (2, 4, 6 robijnen).
#   Plekken als deel van het troonbeeld (royal.png "achter").
# - Put: het luik wordt robijnrood (dieper per stap) en er ligt per stap één grote robijn op (1, 2, 3).
# Vormen in code (geen nieuwe getekende kunst, geen AI). Elke robijn wordt één keer per maat naar een plaatje
# gebakken (zoals stap_teken.gd), daarna is het één draw_texture per robijn. Geen beweging (Hats is rustig).

const RAND := Color("#3d0612")
const KROON := Color("#ff4d64")      # bovenkant (licht valt van boven)
const TAFEL := Color("#ffc4cc")      # het platte vlak bovenop
const PAVILJOEN := Color("#d01c3a")  # onderkant
const DONKER := Color("#86081f")     # rechterhelft van de onderkant: schaduw, geeft diepte
const GLOED := Color(1.0, 0.18, 0.3)
const GLOED_A := 0.55

# Plek op de troon als deel van de rechthoek van het troonbeeld (x, y van 0 tot 1) en maat in Gloop-spelpixels.
# Gemeten in kunst/3d/royal.png (cel 185 x 110, beeld "achter"): gouden hoekbollen (0,22 en 0,78, 0,23), knoppen van
# de armleuningen (0,24 en 0,76, 0,70), voeten (0,2 en 0,8, 0,9).
const TROON := [
	[Vector2(0.216, 0.24), 7.5],    # stap 7: hoekbollen
	[Vector2(0.781, 0.24), 7.5],
	[Vector2(0.236, 0.70), 6.5],    # stap 8: armleuningen
	[Vector2(0.757, 0.70), 6.5],
	[Vector2(0.15, 0.93), 5.5],     # stap 9: bij de voeten, iets naar buiten (anders raken ze de robijn erboven)
	[Vector2(0.85, 0.93), 5.5],
]
const PUT_MAAT := 5.0        # breedte van een robijn op het luik in spelpixels (luik 18 breed)
const PUT_AFSTAND := 5.5
const PUT_Y := 33.0          # midden op het hout van het luik (luik.gd 28,5 tot 40,5; kleine stenen op 38)
const LUIK_ROOD := Color(1.0, 0.42, 0.5)

# Hoeveel grote robijnen bij dit niveau. Gloop: 0, dan 2, 4, 6. Put: 0, dan 1, 2, 3.
static func troon_aantal(niveau: int) -> int:
	return 2 * clampi(niveau - 6, 0, 3)

static func put_aantal(niveau: int) -> int:
	return clampi(niveau - 6, 0, 3)

# Kleur van het luik: vanaf stap 7 robijnrood, per stap dieper (0,5, 0,65, 0,8 van wit naar LUIK_ROOD).
static func luik_kleur(kleur: Color, niveau: int) -> Color:
	var n := put_aantal(niveau)
	if n <= 0:
		return kleur
	var f := 0.35 + 0.15 * float(n)
	return kleur * Color.WHITE.lerp(LUIK_ROOD, f)

# Middens van de robijnen op een put (spelpixels in het hol), rond het midden van de kolom op x.
static func put_plekken(x: float, dy: float, niveau: int) -> Array:
	var uit := []
	var n := put_aantal(niveau)
	for i in n:
		uit.append(Vector2(x + (float(i) - float(n - 1) / 2.0) * PUT_AFSTAND, PUT_Y + dy))
	return uit

static var _bak := {}

# Plaatje van één robijn met breedte b schermpixels (op hele pixels), met gloed eromheen; midden van de steen = midden van het plaatje.
static func plaatje(b: int) -> ImageTexture:
	b = maxi(b, 6)
	if _bak.has(b):
		return _bak[b]
	var w := float(b)
	var r_gloed := w * 1.0
	var zijde := int(ceil(2.0 * r_gloed)) + 2
	zijde += zijde % 2
	var img := Image.create(zijde, zijde, false, Image.FORMAT_RGBA8)
	var m := Vector2(zijde, zijde) / 2.0
	for y in zijde:
		for x in zijde:
			var som := Color(0, 0, 0, 0)
			for sy in 4:
				for sx in 4:
					var q := Vector2(x + (sx + 0.5) / 4.0, y + (sy + 0.5) / 4.0) - m
					som += _monster(q, w, r_gloed) / 16.0
			if som.a > 0.0:
				img.set_pixel(x, y, Color(som.r / som.a, som.g / som.a, som.b / som.a, som.a))
	var tex := ImageTexture.create_from_image(img)
	_bak[b] = tex
	return tex

# Geslepen steen: plat vlak bovenop, breedste punt (rondist) op een derde, punt onderaan. q ten opzichte van het midden.
static func _vorm(w: float) -> Dictionary:
	var hw := w / 2.0
	var h := w * 1.05
	var top := -h * 0.42
	var rond := -h * 0.12
	var punt := h * 0.58
	var buiten := PackedVector2Array([Vector2(-hw * 0.55, top), Vector2(hw * 0.55, top), Vector2(hw, rond), Vector2(0, punt), Vector2(-hw, rond)])
	return {"buiten": buiten, "hw": hw, "top": top, "rond": rond, "punt": punt}

static func _monster(q: Vector2, w: float, r_gloed: float) -> Color:
	var v := _vorm(w)
	var buiten: PackedVector2Array = v["buiten"]
	var rand := 1.1   # donkere rand van ±1 schermpixel
	var binnen := PackedVector2Array()
	for p in buiten:
		binnen.append(p * ((w / 2.0 - rand) / (w / 2.0)) + Vector2(0, rand * 0.15))
	if Geometry2D.is_point_in_polygon(q, binnen):
		var kl: Color
		if q.y < float(v["rond"]) * 0.85:
			# kroon: middenvlak (tafel) licht, zijkanten iets donkerder
			kl = TAFEL if absf(q.x) < float(v["hw"]) * 0.32 and q.y < float(v["top"]) * 0.55 else KROON
		else:
			kl = DONKER if q.x > w * 0.04 else PAVILJOEN
			# lichte facetlijn van de linkerpunt van de rondist naar de punt onderaan
			var a := Vector2(-float(v["hw"]) * 0.45, float(v["rond"]))
			var bq := Vector2(0, float(v["punt"]))
			var d := absf((bq - a).cross(q - a)) / (bq - a).length()
			if d < 0.7 and q.x < 0.0:
				kl = KROON
		return Color(kl.r, kl.g, kl.b, 1.0)
	if Geometry2D.is_point_in_polygon(q, buiten):
		return Color(RAND.r, RAND.g, RAND.b, 1.0)
	var d2 := q.length()
	if d2 < r_gloed:
		var a2 := GLOED_A * pow(1.0 - d2 / r_gloed, 2.0)
		return Color(GLOED.r * a2, GLOED.g * a2, GLOED.b * a2, a2)
	return Color(0, 0, 0, 0)

# Teken een robijn met midden c en breedte maat (beide in lokale spelpixels van doek). basis = de schaal die nu op het
# doek staat (draw_set_transform; bij Gloop het knijpen), die zetten we na afloop terug.
static func teken(doek: CanvasItem, c: Vector2, maat: float, basis: Vector2 = Vector2.ONE) -> void:
	var k := maxf(roundf(doek.get_global_transform().get_scale().x * 20.0) / 20.0, 1.0)
	var tex := plaatje(roundi(maat * k))
	var lt := (c * k - tex.get_size() / 2.0).round()
	doek.draw_set_transform(Vector2.ZERO, 0.0, basis / k)
	doek.draw_texture(tex, lt)
	doek.draw_set_transform(Vector2.ZERO, 0.0, basis)

# Robijnen op de troon van Gloop; r = royal_rect("achter") in Gloop-coordinaten.
static func teken_troon(doek: CanvasItem, r: Rect2, niveau: int, basis: Vector2 = Vector2.ONE) -> void:
	for i in troon_aantal(niveau):
		var t: Array = TROON[i]
		var f: Vector2 = t[0]
		teken(doek, r.position + r.size * f, float(t[1]) * r.size.x / 42.0, basis)
