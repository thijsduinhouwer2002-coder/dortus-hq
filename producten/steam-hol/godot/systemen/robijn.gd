extends RefCounted
# Grote robijnen voor stap 7 tot 9 (Olaf 27 nov, issue #298; Iris #286 punt 1: "stap 7 tot 9 maken één gouden ruitje
# van ±5 px rood; wie niet keek bij de koop, ziet het daarna niet").
# De kleine rij stenen (stap_teken.gd) blijft, maar elke koop vanaf stap 7 zet nu ook grote robijnen neer:
# - Gloop: gezet in het goud van zijn troon, links en rechts tegelijk (midden boven staat zijn hoedentoren ervoor).
#   Daan #307 M1: niet meer los in de lucht, maar een ronde robijn in een gouden kastje mét schaduwtje, óp het goud en
#   niet groter dan Gloops kroon. Stap 7 op de hoekbollen, stap 8 op de knoppen van de armleuningen, stap 9 op de
#   troonpoten (2, 4, 6). Plekken als deel van het troonbeeld (royal.png "achter").
# - Put: het luik wordt robijnrood (per stap duidelijk dieper: honing, oranjerood, rood, diep robijn) en
#   er ligt per stap één geslepen robijn op (1, 2, 3), die elkaar niet raken (Daan #307 M2).
# Vormen in code (geen nieuwe getekende kunst, geen AI). Elke robijn wordt één keer per maat naar een plaatje
# gebakken (zoals stap_teken.gd), daarna is het één draw_texture per robijn. Geen beweging (Hats is rustig).

const RAND := Color("#6e1022")   # Daan #307 K1: zachter dan bijna zwart, zoals de rand van Gloop
const KROON := Color("#ff4d64")      # bovenkant (licht valt van boven)
const TAFEL := Color("#ffc4cc")      # het platte vlak bovenop
const PAVILJOEN := Color("#d01c3a")  # onderkant
const DONKER := Color("#86081f")     # rechterhelft van de onderkant: schaduw, geeft diepte
const GLOED := Color(1.0, 0.18, 0.3)
const GLOED_A := 0.55

# Gezette robijn (troon): goud van het kastje en de schaduw eronder.
const GOUD_LICHT := Color("#ffe58a")
const GOUD := Color("#f0b62c")
const GOUD_DONKER := Color("#a8690f")
const SCHADUW := Color(0.16, 0.05, 0.03)

# Plek op de troon als deel van de rechthoek van het troonbeeld (x, y van 0 tot 1) en maat (buitenmaat van het kastje)
# in Gloop-spelpixels bij een troon van 42 breed. Gemeten in kunst/3d/royal.png (cel 185 x 110, beeld "achter"):
# gouden hoekbollen (0,215 en 0,785, 0,235), gouden knoppen onder de kussens (0,235 en 0,765, 0,70), gouden troonpoten
# (0,235 en 0,76, 0,875). Kastje tot ±15 schermpixels op 120: Gloops kroon (ring met steen) is ±13 tot 16 (GEZIEN). Alle zes liggen binnen de omtrek van de troon, op goud (Daan #307 M1).
const TROON := [
	[Vector2(0.217, 0.235), 4.8],   # stap 7: hoekbollen
	[Vector2(0.783, 0.235), 4.8],
	[Vector2(0.236, 0.675), 4.5],   # stap 8: knoppen van de armleuningen
	[Vector2(0.764, 0.675), 4.5],
	[Vector2(0.238, 0.88), 4.3],   # stap 9: op de troonpoten
	[Vector2(0.757, 0.88), 4.3],
]
const PUT_MAAT := 3.9        # breedte van een robijn op het luik in spelpixels (luik 18 breed); 3 naast elkaar met 1,6 ertussen
const PUT_AFSTAND := 5.5
const PUT_Y := 34.3          # op het hout van het luik (luik.gd hout 33,5 tot 38,5; kleine stenen op 38), robijn steekt niet boven het luik uit (Daan #307 M2)
const LUIK_ROOD := Color(1.0, 0.28, 0.34)

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
	var f := 0.05 + 0.3 * float(n)   # 0,35, 0,65, 0,95: elke stap duidelijk roder (Daan #307 M2)
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
static func plaatje(b: int, gezet: bool = false) -> ImageTexture:
	b = maxi(b, 6)
	var sleutel := b + (100000 if gezet else 0)
	if _bak.has(sleutel):
		return _bak[sleutel]
	var w := float(b)
	var r_gloed := w * (1.05 if gezet else 1.0)   # klein houden: een grote gloed kost vlak (CPU)
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
					som += (_monster_gezet(q, w, r_gloed) if gezet else _monster(q, w, r_gloed)) / 16.0
			if som.a > 0.0:
				img.set_pixel(x, y, Color(som.r / som.a, som.g / som.a, som.b / som.a, som.a))
	var tex := ImageTexture.create_from_image(img)
	_bak[sleutel] = tex
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
	var rand := 0.9   # rand van ±1 schermpixel, zacht (K1)
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

# Ronde robijn in een gouden kastje met een schaduwtje eronder (troon, Daan #307 M1). w = buitenmaat van het kastje.
# Licht valt van linksboven, zoals op de troon en Gloop.
static func _monster_gezet(q: Vector2, w: float, r_gloed: float) -> Color:
	var rx := w / 2.0
	var ry := rx * 0.92
	var e := Vector2(q.x / rx, q.y / ry).length()   # 1 = buitenrand van het kastje
	var ri := 0.66                                    # robijn binnen het kastje
	var licht := Vector2(-0.6, -0.8)
	if e <= ri:
		var u := Vector2(q.x / rx, q.y / ry) / ri       # -1..1 binnen de robijn
		var t := clampf(0.5 - 0.5 * u.dot(licht), 0.0, 1.0)   # 0 = lichtkant, 1 = schaduwkant
		var kl := Color("#ff6a7c").lerp(KROON, clampf(t * 1.8, 0.0, 1.0)).lerp(PAVILJOEN, clampf(t * 2.2 - 1.2, 0.0, 1.0))   # helder, zodat hij op 1x van het rode kussen loskomt
		var rand := clampf((u.length() - 0.72) / 0.28, 0.0, 1.0)   # zachte donkere rand, geen harde lijn (K1)
		kl = kl.lerp(RAND, rand * 0.6)
		if (u - Vector2(-0.3, -0.36)).length() < 0.3:
			kl = Color("#fff0f2")   # glimlicht, bijna wit
		return Color(kl.r, kl.g, kl.b, 1.0)
	if e <= 1.0:
		var u2 := Vector2(q.x / rx, q.y / ry)
		var tg := clampf(0.5 - 0.5 * u2.normalized().dot(licht), 0.0, 1.0)
		var kg := GOUD_LICHT.lerp(GOUD, clampf(tg * 1.4, 0.0, 1.0)).lerp(GOUD_DONKER, clampf(tg * 2.0 - 1.0, 0.0, 1.0))
		if e > 1.0 - 0.9 / rx or e < ri + 0.5 / rx:
			kg = kg.lerp(GOUD_DONKER, 0.7)   # dun randje om het kastje en om de robijn
		return Color(kg.r, kg.g, kg.b, 1.0)
	# schaduwtje: iets naar rechtsonder, zacht, alleen buiten het kastje
	var qs := q - Vector2(rx * 0.18, ry * 0.32)
	var es := Vector2(qs.x / (rx * 1.02), qs.y / (ry * 0.98)).length()
	var schaduw := 0.0
	if es < 1.0:
		schaduw = 0.45 * clampf((1.0 - es) / 0.35, 0.0, 1.0)
	var d2 := q.length()
	var gl := 0.0
	if d2 < r_gloed:
		gl = 0.7 * pow(1.0 - d2 / r_gloed, 1.5)
	if schaduw <= 0.0 and gl <= 0.0:
		return Color(0, 0, 0, 0)
	var a := schaduw + gl * (1.0 - schaduw)
	var kc := (SCHADUW * schaduw + GLOED * gl * (1.0 - schaduw)) / a
	return Color(kc.r * a, kc.g * a, kc.b * a, a)   # voorvermenigvuldigd, zoals _monster (plaatje deelt door a)

# Teken een robijn met midden c en breedte maat (beide in lokale spelpixels van doek). basis = de schaal die nu op het
# doek staat (draw_set_transform; bij Gloop het knijpen), die zetten we na afloop terug.
static func teken(doek: CanvasItem, c: Vector2, maat: float, basis: Vector2 = Vector2.ONE, gezet: bool = false) -> void:
	var k := maxf(roundf(doek.get_global_transform().get_scale().x * 20.0) / 20.0, 1.0)
	var tex := plaatje(roundi(maat * k), gezet)
	var lt := (c * k - tex.get_size() / 2.0).round()
	doek.draw_set_transform(Vector2.ZERO, 0.0, basis / k)
	doek.draw_texture(tex, lt)
	doek.draw_set_transform(Vector2.ZERO, 0.0, basis)

# Robijnen op de troon van Gloop; r = royal_rect("achter") in Gloop-coordinaten.
static func teken_troon(doek: CanvasItem, r: Rect2, niveau: int, basis: Vector2 = Vector2.ONE) -> void:
	for i in troon_aantal(niveau):
		var t: Array = TROON[i]
		var f: Vector2 = t[0]
		teken(doek, r.position + r.size * f, float(t[1]) * r.size.x / 42.0, basis, true)
