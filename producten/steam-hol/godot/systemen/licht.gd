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
const GANG_DONKER := Color(0.62, 0.59, 0.68)
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
	var basis := GANG_DONKER if open else AARDE_DONKER
	var l := licht_op(bronnen(hol), p)
	l = maxf(l, clampf(1.0 - (p.y - OPP) / 10.0, 0.0, 1.0) * TOP_LICHT)
	return basis.lerp(LICHT, l)

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
	var basis := GANG_DONKER if open else AARDE_DONKER
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
