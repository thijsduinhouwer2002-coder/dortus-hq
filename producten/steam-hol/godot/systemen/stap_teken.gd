extends RefCounted
# Stap 4 tot 6 zichtbaar (Olaf 26 nov, issue #162; Iris keuring 499fd9f punt 1: "koop verandert niets").
# Stap 1 tot 3 hebben elk eigen kunst (groter, veren, troon; roest, diep, valluik). Stap 4 tot 6 waren alleen getallen,
# dus Royal Gloop en Gloop Prime zagen er gelijk uit. Nu krijgt Gloop en elke put per gekochte stap boven 3 één gouden
# steen op de vloer: stap 4 één, stap 5 twee, stap 6 drie. Tellen kan iedereen, dus de volgorde lees je zonder uitleg.
# Zelfde vier kleuren als het muntje (hol.gd munt_3d), zodat het bij het goud hoort; ruitvorm, zodat het geen
# munt is (een rond muntje boven Gloop of de put betekent "dit kun je kopen"). Geen beweging.
# In schermpixels met een gladde rand, net als munt_3d (op schaal 3 tot 4 anders trappetjes).

const RAND := Color("#6e3f0e")      # donkerder dan de munt-rand, anders verdwijnt hij op de gele veren van Gloop
const GOUD := Color("#f2b632")
const GLIM := Color("#fff0aa")
const SCHADUW := Color(0.12, 0.04, 0.12, 0.5)
const HALF := 2.0        # halve breedte van een steen in spelpixels (4 breed, 12 schermpixels op 120)
const AFSTAND := 5.0     # midden tot midden (Daan #177 kan 2: 4,5 raakte elkaar bijna, nu 1 schermpixel lucht)
# Op het luik van de put kleiner (Mila #222, Iris 5ecaf64 punt 3: twee ruiten van volle maat bedekten bijna het hele
# Trick Lid-luik, je las goud met een zwarte rand en geen aarde en gras). Op de put liggen ze onderaan op het
# luik (hol.gd), op 0,7 van de maat: rij van drie ±10 spelpixels breed, het hout met aarde en gras erboven blijft vrij.
# Bij Gloop blijft de volle maat.
const PUT_MAAT := 0.7

# Hoeveel stenen bij dit niveau (0 tot 6): alleen boven stap 3.
static func aantal(niveau: int, beeld_max: int = 3) -> int:
	return clampi(niveau - beeld_max, 0, 3)

# Midden van steen i van n, ten opzichte van het midden van de rij (spelpixels).
static func plek(i: int, n: int, maat: float = 1.0) -> float:
	return (float(i) - float(n - 1) / 2.0) * AFSTAND * maat

# CPU (#162, hoofdmanager 26 nov 12:40): de rij wordt één keer per (aantal, schaal) naar een klein plaatje gebakken
# (pixel voor pixel, 4 x 4 monsters per pixel voor de gladde rand) en daarna alleen nog als één plaatje getekend.
# Eerst waren het per steen vier veelhoeken en drie gladde lijnen; dat kostte op een machine zonder grafische kaart
# per beeld rekenwerk, ook als de laag niet opnieuw tekende.
static var _bak := {}

# Plaatje van een rij van n stenen op schaal k (schermpixels per spelpixel, op 0,05 afgerond); midden van de rij = midden van het plaatje.
static func plaatje(n: int, k: float, maat: float = 1.0) -> ImageTexture:
	var sleutel := Vector3i(n, roundi(k * 20.0), roundi(maat * 20.0))
	if _bak.has(sleutel):
		return _bak[sleutel]
	# zelfde maat als de eerste versie op het scherm (die met gladde lijnen was 1 schermpixel ruimer dan HALF): rand ±1 px
	var h := HALF * maat * k + 1.0
	var g := h - 1.2
	var breed := int(ceil(2.0 * absf(plek(0, n, maat)) * k + 2.0 * h)) + 4
	var hoog := int(ceil(2.0 * h)) + 4
	breed += breed % 2
	hoog += hoog % 2
	var img := Image.create(breed, hoog, false, Image.FORMAT_RGBA8)
	var m0 := Vector2(breed, hoog) / 2.0
	var middens := []
	for i in n:
		middens.append(m0 + Vector2(plek(i, n, maat) * k, 0.0))
	for y in hoog:
		for x in breed:
			var som := Color(0, 0, 0, 0)
			for sy in 4:
				for sx in 4:
					var q := Vector2(x + (sx + 0.5) / 4.0, y + (sy + 0.5) / 4.0)
					som += _monster(q, middens, h, g) / 16.0
			if som.a > 0.0:
				img.set_pixel(x, y, Color(som.r / som.a, som.g / som.a, som.b / som.a, som.a))
	var tex := ImageTexture.create_from_image(img)
	_bak[sleutel] = tex
	return tex

# Kleur van één monster (voorvermenigvuldigd met alfa): schaduw, rand, goud, glimvlak, van onder naar boven.
static func _monster(q: Vector2, middens: Array, h: float, g: float) -> Color:
	for m in middens:
		var d: Vector2 = q - m
		if absf(d.x) + absf(d.y) <= g:
			# glimvlak linksboven: driehoek (0,-g), (-g,0), (-g/4,-g/4)
			var kl := GLIM if Geometry2D.point_is_inside_triangle(d, Vector2(0, -g), Vector2(-g, 0), Vector2(-g * 0.25, -g * 0.25)) else GOUD
			return Color(kl.r, kl.g, kl.b, 1.0)
		if absf(d.x) + absf(d.y) <= h:
			return Color(RAND.r, RAND.g, RAND.b, 1.0)
	for m in middens:
		var d: Vector2 = q - m - Vector2(0.5, 1.0)
		if absf(d.x) + absf(d.y) <= h:
			return Color(SCHADUW.r * SCHADUW.a, SCHADUW.g * SCHADUW.a, SCHADUW.b * SCHADUW.a, SCHADUW.a)
	return Color(0, 0, 0, 0)

# Teken n stenen in een rij met het midden op c (spelpixels, lokaal van doek): één plaatje, op hele schermpixels.
static func teken(doek: CanvasItem, c: Vector2, n: int, maat: float = 1.0) -> void:
	if n <= 0:
		return
	var k := maxf(roundf(doek.get_global_transform().get_scale().x * 20.0) / 20.0, 1.0)   # Gloop staat op 3,45: ook 1 op 1
	var tex := plaatje(n, k, maat)
	var lt := (c * k - tex.get_size() / 2.0).round()
	doek.draw_set_transform(Vector2.ZERO, 0.0, Vector2.ONE / k)
	doek.draw_texture(tex, lt)
	doek.draw_set_transform(Vector2.ZERO, 0.0, Vector2.ONE)
