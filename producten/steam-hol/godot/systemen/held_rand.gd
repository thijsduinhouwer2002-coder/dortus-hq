extends RefCounted
# Wat de held losmaakt van het hol (#242, keuze Sanne 27 nov 04:00 NL; Iris #239: in het fakkellicht links verdween een
# held bijna tegen de gele stenen). Los van held_beeld.gd zodat dat bestand klein blijft.
# 1. Donkere rand van 1 spelpx om lijf en hoed (niet om teken of klap), warm bijna zwart #1a1008, dekking 0,85, zoals de
#    zwarte rand van het luik (#209). Getekend als silhouet van het 3D-blad, 4 keer 1 spelpx verschoven, vóór het lijf.
# 2. Schaduwvlek onder de voeten, ovaal 10 x 3 spelpx, dekking 0,35, zoals Gloop (slijm.gd VLOER_SCHADUW). Blijft op de
#    vloer bij een sprong (iets kleiner en lichter), zakt mee met de val en is weg na VAL_WEG_S.
# 3. Witte flits op de held die valt (Mila #43, Daan #45), sinds #242 ook hier.
# Uit voor vergelijken: startargument uit3d=rand (zelfde build, voor en na naast elkaar).

const LICHTR := preload("res://systemen/held_licht.gd")   # lichte buitenrand op donkere steen (#256)
const RAND_KLEUR := Color(0x1a / 255.0, 0x10 / 255.0, 0x08 / 255.0, 0.85)
const RAND_PX := 1.0
const RICHTING := [Vector2(-1, 0), Vector2(1, 0), Vector2(0, -1), Vector2(0, 1)]
const SIL_VAN := 96       # alfa in het blad waaronder geen rand komt (waas)
const SIL_TOT := 160
const SCHADUW_B := 10.0
const SCHADUW_H := 3.0
const SCHADUW_A := 0.35
const VAL_WEG_S := 0.2     # schaduw weg zodra de held valt (gelijk aan VAL_RECHT in held_beeld.gd)
static var aan := true
static var _gelezen := false
static var _sil := {}      # pad van het blad -> CanvasTexture met het witte silhouet
static var _schaduw: CanvasTexture

static func is_aan() -> bool:
	if not _gelezen:
		_gelezen = true
		for a in OS.get_cmdline_user_args():
			if a.begins_with("uit3d=") and "rand" in a.substr(6).split(",", false):
				aan = false
	return aan

# Wit silhouet van een blad (alfa van het blad, kleur wit), één keer per blad: zo geeft de modulate RAND_KLEUR precies die kleur.
static func silhouet(ct: CanvasTexture) -> CanvasTexture:
	var bron: Texture2D = ct.diffuse_texture
	var sleutel: String = bron.resource_path if bron.resource_path != "" else str(bron.get_instance_id())
	if _sil.has(sleutel):
		return _sil[sleutel]
	var img := bron.get_image()
	if img == null:
		_sil[sleutel] = null
		return null
	if img.is_compressed():
		img.decompress()
	img.clear_mipmaps()
	img.convert(Image.FORMAT_RGBA8)
	# De bladen hebben een zachte waas van bijna doorzichtige punten om het lijf (alfa 1 tot 127, de helft van alle
	# punten): die mag geen rand krijgen, anders wordt het een donkere wolk. Alleen het echte lijf telt: alfa van 96 tot
	# 160 loopt zacht op van 0 naar vol, daarboven vol.
	var d := img.get_data()
	var n := d.size()
	var i := 0
	while i < n:
		var a := d[i + 3]
		d[i] = 255
		d[i + 1] = 255
		d[i + 2] = 255
		d[i + 3] = 0 if a <= SIL_VAN else (255 if a >= SIL_TOT else (a - SIL_VAN) * 255 / (SIL_TOT - SIL_VAN))
		i += 4
	var uit := Image.create_from_data(img.get_width(), img.get_height(), false, Image.FORMAT_RGBA8, d)
	uit.generate_mipmaps()
	var s := CanvasTexture.new()
	s.diffuse_texture = ImageTexture.create_from_image(uit)
	s.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS
	_sil[sleutel] = s
	return s

# De rand van het lijf: silhouet 4 keer, 1 spelpx naar elke kant. sx = -1 als het lijf gespiegeld staat.
static func rand_lijf(h, ct: CanvasTexture, doel: Rect2, bron: Rect2, sx: float, alfa := 1.0, licht := false) -> void:
	var s := silhouet(ct)
	if s == null:
		return
	if licht:
		var ls := LICHTR.sterkte(h)
		if ls > 0.01:
			LICHTR.rand_lijf(h, s, doel, bron, sx, ls, alfa)
			h.draw_set_transform(Vector2.ZERO, 0, Vector2(sx, 1))
		return
	var c := Color(RAND_KLEUR.r, RAND_KLEUR.g, RAND_KLEUR.b, RAND_KLEUR.a * alfa)
	for r in RICHTING:
		h.draw_set_transform(r * RAND_PX, 0, Vector2(sx, 1))
		h.draw_texture_rect_region(s, doel, bron, c)
	h.draw_set_transform(Vector2.ZERO, 0, Vector2(sx, 1))

# Rand van de hoed: zelfde transform als de hoed, verschoven in schermrichting (dus altijd 1 spelpx, ook bij draaien).
static func rand_hoed(h, ct: CanvasTexture, plek: Vector2, draai: float, schaal: Vector2, doel: Rect2, bron: Rect2, alfa: float, licht := false) -> void:
	var s := silhouet(ct)
	if s == null:
		return
	if licht:
		var ls := LICHTR.sterkte(h)
		if ls > 0.01:
			LICHTR.rand_hoed(h, s, plek, draai, schaal, doel, bron, ls, alfa)
		return
	var c := Color(RAND_KLEUR.r, RAND_KLEUR.g, RAND_KLEUR.b, RAND_KLEUR.a * alfa)
	for r in RICHTING:
		h.draw_set_transform(plek + r * RAND_PX, draai, schaal)
		h.draw_texture_rect_region(s, doel, bron, c)

# Zachte ovale vlek, één keer gemaakt (4 beeldpunten per spelpx, lineair gefilterd).
static func schaduw_beeld() -> CanvasTexture:
	if _schaduw != null:
		return _schaduw
	var k := 4
	var b := int(SCHADUW_B) * k
	var hg := int(SCHADUW_H) * k
	var img := Image.create(b, hg, false, Image.FORMAT_RGBA8)
	for y in hg:
		for x in b:
			var dx := (float(x) + 0.5 - b / 2.0) / (b / 2.0)
			var dy := (float(y) + 0.5 - hg / 2.0) / (hg / 2.0)
			var d := sqrt(dx * dx + dy * dy)
			img.set_pixel(x, y, Color(0, 0, 0, clampf((1.0 - d) / 0.35, 0.0, 1.0)))   # rand zacht over het buitenste derde
	_schaduw = CanvasTexture.new()
	_schaduw.diffuse_texture = ImageTexture.create_from_image(img)
	_schaduw.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR
	return _schaduw

# Hoeveel schaduw (0 tot 1) en hoe breed (factor) bij deze stand. hop < 0 = boven de vloer.
static func schaduw_stand(staat: String, val_t: float, hop: float) -> Vector2:
	if staat == "weg":
		return Vector2.ZERO
	var a := 1.0
	if staat == "vallen":
		a = clampf(1.0 - val_t / VAL_WEG_S, 0.0, 1.0)
	var hoog := clampf(-hop / 6.0, 0.0, 1.0)   # bij een sprong van 6 spelpx: 70 procent breed, de helft zo donker
	return Vector2(a * (1.0 - 0.5 * hoog), 1.0 - 0.3 * hoog)

static func schaduw(h, staat: String, val_t: float, hop: float, zak: float) -> void:
	var st := schaduw_stand(staat, val_t, hop)
	if st.x <= 0.0:
		return
	var b := SCHADUW_B * st.y
	var hg := SCHADUW_H * st.y
	h.draw_set_transform(Vector2.ZERO, 0, Vector2.ONE)
	h.draw_texture_rect(schaduw_beeld(), Rect2(-b / 2.0, zak - hg / 2.0, b, hg), false, Color(1, 1, 1, SCHADUW_A * st.x))

# Witte flits op de held die valt (Mila #43, Daan #45): 0,12 s helemaal wit, dan 0,06 s half, dan niets. Een eigen
# ShaderMaterial op de held, alleen zolang hij flitst (daarna weer null: geen extra werk voor de andere helden).
const FLITS_WIT := 0.12
const FLITS_HALF := 0.06
const FLITS_SHADER := "shader_type canvas_item;\nuniform float flits = 0.0;\nvoid fragment() {\n\tvec4 c = texture(TEXTURE, UV) * COLOR;\n\tCOLOR = vec4(mix(c.rgb, vec3(1.0), flits), c.a);\n}\n"
static var flits_shader: Shader
static func flits(staat: String, vt: float) -> float:
	if staat != "vallen":
		return 0.0
	if vt < FLITS_WIT:
		return 1.0
	if vt < FLITS_WIT + FLITS_HALF:
		return 0.5
	return 0.0

static func flits_zet(h, f: float) -> void:
	if not (h is CanvasItem):
		return
	var ci := h as CanvasItem
	if f <= 0.0:
		if ci.material != null:
			ci.material = null
		return
	if flits_shader == null:
		flits_shader = Shader.new()
		flits_shader.code = FLITS_SHADER
	var m := ci.material as ShaderMaterial
	if m == null:
		m = ShaderMaterial.new()
		m.shader = flits_shader
		ci.material = m
	m.set_shader_parameter("flits", f)
