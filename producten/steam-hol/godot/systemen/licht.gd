extends Node2D
# Licht in het hol (Olaf, 25 nov, issue #97, bouwblad H in platformen/steam/spelgevoel.md).
# Gemini vond het speelscherm "too basic" en "flat": de hele aarde was even fel. Nu krijgt het hol diepte:
# - Donker (dit knooppunt, vermenigvuldigen): een vaste lichtkaart op halve spelpixels, lineair gefilterd. Aarde ver
#   van een lichtbron wordt donkerder, gangen en kamers donkerder dan de aarde eromheen, gras en lucht blijven gelijk.
#   Alleen opnieuw als het hol verandert (graven, ingang, schatkamer): elke 0,5 s een sleutel vergelijken.
# - Gloed (kind, optellen): een warme vlek om de fakkel bij de ingang, de schatkamer en daglicht in de schacht, die
#   traag flakkert tussen 90 en 100 procent. Alleen een nieuw beeld als de fakkel toch een nieuw beeld krijgt (hol.anim).
# Hangt in het hol na het vaste beeld en vóór vleermuis, bordje en wezens: helden en Gloop blijven fel en scherp.
# Bekeken: Rusty's Retirement in de lat (warme plekken, donkere randen) en de 2D-lichtdemo in godot-demo-projects
# (2d/lights_and_shadows); daar lichten PointLight2D's alles, wat hier elk beeld per held en tegel zou kosten.

const KOL := 16
const H := 40
const OPP := 8
const GANG_BOVEN := 24
const STAP := 2               # lichtkaart: 1 texel per 2 x 2 spelpixels
const HOL3D := preload("res://hol/hol_3d.gd")

# vermenigvuldigers (r, g, b): koel in het donker, warm in het licht. Bijgesteld op het beeld van 120 px (GEZIEN).
const AARDE_DONKER := Color(0.76, 0.73, 0.80)
# Sanne 26 nov (Iris 499fd9f, mooi 7: "de gang leest op 1x als één zalmroze buis, overal dezelfde lichtkleur"):
# de gang krijgt minder rood (aarde, geen roze), wordt naar de vloer toe donkerder, en heeft plekken met een andere
# steen: koele grijze steen en gele leem, zacht in elkaar over, elke ±5 tegels anders. Vast per kolom, dus geen flikkeren.
# Olaf 26 nov (#210, Iris bb298d3 punt 3: "op 1x weinig verschil tussen de vlakken"): de drie soorten lagen in
# helderheid binnen 0,035 van elkaar (0,59, 0,56, 0,55). Nu een trap: koele steen donker, gewoon midden, leem licht
# (0,54, 0,66, 0,75), en de wand wordt metselwerk (zie gang_kleur).
const GANG_DONKER := Color(0.62, 0.69, 0.68)   # gewoon; was (0.53, 0.61, 0.62)
const STEEN_KOEL := Color(0.49, 0.54, 0.59)   # was (0.50, 0.555, 0.61): iets donkerder, koel grijs (Daan #183 M2: geen paars)
const STEEN_LEEM := Color(0.86, 0.83, 0.56)   # was (0.64, 0.615, 0.40): lichter, geel, r/g gelijk (niet roder)
const VOEG_KOEL := 0.86       # voeg in koele steen (die is al donker; toets "nooit zwart" 0,4)
const RAND_LICHT := 1.15      # rij texels onder de liggende voeg van elk blok: zo veel lichter (leest als blok)
const KANT_LICHT := 1.08      # rij texels rechts van de staande voeg van elk blok
const VLOER_DONKER := 0.86    # onderste spelpixel van de gang: zo veel van de kleur erboven
const PLEK_KOL := 5.0         # zo veel tegels per plek steen (gemiddeld; elke rand schuift vast -0,75 tot +0,75 tegel)
const VOEG := 0.80            # donkere voeg tussen twee plekken en de liggende voeg: zo veel van de kleur
const VLOER_Y := 35           # vanaf hier de vloerstrook waar de helden lopen (Daan #183 kan: warmer)
const VLOER_WARM := Color(0.66, 0.55, 0.44)   # warme vloerkleur, de vloerstrook gaat er voor VLOER_MENG naartoe
const VLOER_MENG := 0.7
const LICHT := Color(1.0, 0.98, 0.93)
const TOP_LICHT := 0.55       # daglicht vlak onder het gras: zo veel van de weg naar LICHT, gaat over 10 spelpixels weg

var h                          # hol.gd
var tex: ImageTexture
var sleutel := ""
var wacht := 0.0
var gloed: Node2D
var keer := 0                  # zo vaak de kaart opnieuw gemaakt (toetsen en meetregel)

static func maak_in(hol) -> Node2D:
	var l := Node2D.new()
	l.set_script(load("res://systemen/licht.gd"))
	l.name = "Licht"
	l.h = hol
	if "licht_aan" in hol:
		hol.licht_aan = true   # puts boven de kaart nemen dan zijn kleur over (Daan #183 M1)
	var m := CanvasItemMaterial.new()
	m.blend_mode = CanvasItemMaterial.BLEND_MODE_MUL
	l.material = m
	l.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR
	# in het vaste beeld van het hol (hol_vast.gd), na de tegels: dan kost licht alleen iets als dat beeld opnieuw
	# getekend wordt. Over de hele breedte elk beeld vermenigvuldigen kostte op de software-renderer ±26% CPU (GEZIEN).
	if hol.vast != null and hol.vast.vp != null:
		l.scale = hol.vast.scale
		hol.vast.vp.add_child(l)
	else:
		hol.add_child(l)
	var g := Node2D.new()
	g.set_script(load("res://systemen/licht_gloed.gd"))
	g.name = "Gloed"
	g.h = hol
	var ma := CanvasItemMaterial.new()
	ma.blend_mode = CanvasItemMaterial.BLEND_MODE_ADD
	g.material = ma
	hol.add_child(g)
	l.gloed = g
	return l

# lichtbronnen in spelpixels: [midden, straal, sterkte 0..1]. Ook gebruikt door de gloed en door leven.gd (stofjes).
static func bronnen(hol) -> Array:
	var b: Array = []
	var fk: int = hol.ingang_kol + 1
	if fk < hol.kolommen and fk < hol.schat_kol:
		b.append([fakkel_punt(hol), 30.0, 1.0])
	# schatkamer: het goud straalt (warm, breed); midden boven de stapel
	b.append([Vector2(hol.schat_kol * KOL + 4, 27), 34.0, 0.9])
	# daglicht valt door de schacht naar beneden (alleen in de kaart, geen gloed)
	var ix: float = hol._ingang_x()
	b.append([Vector2(ix + KOL / 2.0, OPP + 8), 20.0, 0.75])
	return b

# vermenigvuldiger van de kaart op spelpixel p (voor leven.gd, dat boven het vaste beeld tekent)
static func kleur_op(hol, p: Vector2) -> Color:
	if p.y < OPP:
		return Color.WHITE
	var k := int(p.x / KOL)
	var open := false
	if k >= 0 and k < hol.kolommen:
		open = hol.gang[k] if p.y >= GANG_BOVEN else (hol.boven[k] or k == hol.ingang_kol)
	var basis := gang_kleur(p) if open else AARDE_DONKER
	var l := licht_op(bronnen(hol), p)
	l = maxf(l, clampf(1.0 - (p.y - OPP) / 10.0, 0.0, 1.0) * TOP_LICHT)
	return basis.lerp(LICHT, l)

# kleur van een open cel in het donker: blokken steen in rijen, plekken met een andere soort, donkerder naar de vloer.
# Daan #183 M2 (26 nov): de soort per plek uit een hash (nooit gelijk aan de buur), plekken 3,5 tot 6,5 tegels breed.
# Olaf #210 (Iris bb298d3 punt 3): een blinde lezer noemde de wand met één voeg per plek nog "aarde" met "zachte banden".
# Nu metselwerk: rijen van BLOK_H spelpx, blokken van BLOK_B breed, elke rij een half blok verschoven, een donkere voeg
# boven en links van elk blok en een lichte rand eronder en ernaast, zodat elk blok leest als steen. De soort hoort bij
# het hele blok (midden van het blok), dus de rand van een plek loopt langs de voegen. Vloerstrook blijft glad en warm.
const BLOK_H := 8             # rij in spelpx: 1 texel voeg, 1 texel lichte rand, 2 texels steen (STAP 2)
const BLOK_B := 16            # blok in spelpx (één tegel); oneven rijen een half blok verschoven
static func gang_kleur(p: Vector2) -> Color:
	var c: Color
	var voeg := 1.0
	if p.y < VLOER_Y:
		var rij := int(floor((p.y - OPP) / BLOK_H))
		var ry := fposmod(p.y - OPP, BLOK_H)
		var schuif := (BLOK_B / 2.0) * posmod(rij, 2)
		var bx := int(floor((p.x - schuif) / BLOK_B))
		var jx := fposmod(p.x - schuif, BLOK_B)
		var midden := schuif + bx * BLOK_B + BLOK_B / 2.0
		var i := plek_nr(midden)
		var soort := plek_soort(i)
		c = [GANG_DONKER, STEEN_KOEL, STEEN_LEEM][soort]
		# elk blok net iets anders, zodat het geen behang wordt
		var d := 0.94 + 0.12 * (_hash(bx * 31 + rij, 7) % 1000) / 1000.0
		c = Color(c.r * d, c.g * d, c.b * d)
		if ry < 2.0 or jx < 2.0:
			voeg = VOEG_KOEL if soort == 1 else VOEG   # koele steen is al donker: voeg minder diep, nooit zwart
		elif ry < 4.0:
			voeg = RAND_LICHT
		elif jx < 4.0:
			voeg = KANT_LICHT
	else:
		var i := plek_nr(p.x)
		c = [GANG_DONKER, STEEN_KOEL, STEEN_LEEM][plek_soort(i)]
	c = Color(c.r * voeg, c.g * voeg, c.b * voeg)
	if p.y >= GANG_BOVEN:
		var dv := lerpf(1.0, VLOER_DONKER, clampf((p.y - GANG_BOVEN) / float(H - GANG_BOVEN), 0.0, 1.0))
		c = Color(c.r * dv, c.g * dv, c.b * dv)
		if p.y >= VLOER_Y:
			c = c.lerp(Color(VLOER_WARM.r * dv, VLOER_WARM.g * dv, VLOER_WARM.b * dv), VLOER_MENG)
	return c

# helderheid van de kleur van een soort (0 gewoon, 1 koel, 2 leem), voor de toets
static func helder_soort(k: int) -> float:
	var c: Color = [GANG_DONKER, STEEN_KOEL, STEEN_LEEM][k]
	return (c.r + c.g + c.b) / 3.0

# nummer van de plek steen waar x (spelpixels) in ligt
static func plek_nr(x: float) -> int:
	var i := int(floor(x / (KOL * PLEK_KOL)))
	if x < plek_begin(i):
		return i - 1
	if x >= plek_begin(i + 1):
		return i + 1
	return i

# linkerrand van plek i in spelpixels: om de PLEK_KOL tegels, met een vaste schuif van -0,75 tot +0,75 tegel
static func plek_begin(i: int) -> float:
	return (i * PLEK_KOL + (_hash(i, 1) % 1000) / 1000.0 * 1.5 - 0.75) * KOL

# 0 gewoon, 1 koele steen, 2 leem. Even plekken uit de hash; een oneven plek kiest uit wat zijn twee buren niet zijn,
# dus nooit twee keer dezelfde soort naast elkaar en geen vast ritme.
static func plek_soort(i: int) -> int:
	if posmod(i, 2) == 0:
		return _hash(i, 0) % 3
	var l := _hash(i - 1, 0) % 3
	var r := _hash(i + 1, 0) % 3
	var vrij: Array = []
	for s in 3:
		if s != l and s != r:
			vrij.append(s)
	return vrij[_hash(i, 2) % vrij.size()]

static func _hash(i: int, zout: int) -> int:
	var v := (i * 73856093) ^ (zout * 19349663) ^ 83492791
	v = (v ^ (v >> 13)) * 1274126177
	return absi(v ^ (v >> 16)) % 100000

# midden van de vlam van de fakkel bij de ingang (zelfde plek als hol.gd hem tekent)
static func fakkel_punt(hol) -> Vector2:
	var fx: float = hol._ingang_x() + KOL + 4
	var fm := HOL3D.deco_maat("fakkel")
	var fy := HOL3D.deco_y("fakkel", GANG_BOVEN + 13 - fm.y) if fm != Vector2.ZERO else float(GANG_BOVEN + 1)
	return Vector2(fx + 4, fy + 5)

func _sleutel() -> String:
	return "%d|%s|%s|%d|%d|%d" % [h.kolommen, h.gang, h.boven, h.ingang_kol, h.schat_kol, int(h._ingang_x())]

func _process(delta: float) -> void:
	wacht -= delta
	if wacht > 0.0 or h == null or h.kolommen <= 0:
		return
	wacht = 0.5
	var k := _sleutel()
	if k != sleutel:
		sleutel = k
		_maak_kaart()
		queue_redraw()
		if h.vast != null and h.vast.vp != null:
			h.vast.vp.render_target_update_mode = SubViewport.UPDATE_ONCE
		if gloed:
			gloed.queue_redraw()

# 0..1: hoe open is spelpixel (x, y)? Open cellen (gang, kamers, schacht) donkerder dan aarde.

# zelfde als kleur_op, met de bronnen al berekend (de kaart roept dit per texel aan)
func _kleur(b: Array, p: Vector2) -> Color:
	var k := int(p.x / KOL)
	var open := false
	if k >= 0 and k < h.kolommen:
		open = h.gang[k] if p.y >= GANG_BOVEN else (h.boven[k] or k == h.ingang_kol)
	var basis := gang_kleur(p) if open else AARDE_DONKER
	var l := maxf(licht_op(b, p), clampf(1.0 - (p.y - OPP) / 10.0, 0.0, 1.0) * TOP_LICHT)
	return basis.lerp(LICHT, l)

static func licht_op(b: Array, p: Vector2) -> float:
	var l := 0.0
	for s in b:
		var d: float = p.distance_to(s[0]) / float(s[1])
		if d < 1.0:
			var v: float = (1.0 - d * d) * float(s[2])
			l = maxf(l, v * v * (3.0 - 2.0 * v))   # zachte rand
	return l

func _maak_kaart() -> void:
	keer += 1
	var b := bronnen(h)
	var w: int = int(ceil(h.kolommen * KOL / float(STAP)))
	var hh: int = int(H / STAP)
	var img := Image.create(w, hh, false, Image.FORMAT_RGB8)
	for ty in hh:
		var y := ty * STAP + STAP / 2.0
		for tx in w:
			var x := tx * STAP + STAP / 2.0
			if y < OPP:
				img.set_pixel(tx, ty, Color.WHITE)
				continue
			img.set_pixel(tx, ty, _kleur(b, Vector2(x, y)))
	if tex == null or tex.get_width() != w or tex.get_height() != hh:
		tex = ImageTexture.create_from_image(img)
	else:
		tex.update(img)

func _draw() -> void:
	if tex == null:
		return
	draw_texture_rect(tex, Rect2(0, 0, tex.get_width() * STAP, tex.get_height() * STAP), false)
