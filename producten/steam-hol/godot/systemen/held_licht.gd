extends RefCounted
# Lichte buitenrand om een held die voor donkere steen staat (Olaf 27 nov, #256; Iris 1b0e933 punt 2 voor een 9: een
# held met donker pak zakt weg in de blauwgrijze stenen in het midden). De donkere rand van #242 helpt daar niet,
# want donker op donker. Zoals pixelkunst een randlicht zet: 1 spelpx warm licht búiten de donkere rand, dus
# licht, dan donker, dan het lijf. Hoe sterk hangt af van de plek:
# - de soort steen achter de held (hol/metsel.gd): koel blauwgrijs vol, rode baksteen half, oker leem niets;
# - het licht op die plek (systemen/licht.gd): in het fakkellicht en bij de schat gaat hij uit, want daar is de
#   achtergrond licht en staat de donkere rand al goed.
# Hij komt en gaat zacht (over ±0,4 s), zodat hij niet knipt als een held van de ene steen naar de andere loopt.
# STAAT AAN (27 nov ±12:45). De +7 procent van de eerste meting was het verschil tussen losse runs; binnen één run met
# 20 en 100 keer het licht tegen een placebo kost één keer hooguit enkele tienden van een procent (bewijs-held-licht/LEESMIJ.md).
# Uit met startargument licht=0.
# Uit voor vergelijken: startargument uit3d=licht (zelfde build, voor en na naast elkaar). Met licht_wissel=1 staat hij
# om het andere getekende beeld aan en uit (alleen voor het bewijs: zelfde held op dezelfde plek, 1 beeld uit elkaar).

const METSEL := preload("res://hol/metsel.gd")
const LICHT := preload("res://systemen/licht.gd")
const KLEUR := Color(1.0, 0.88, 0.66)     # warm, als het fakkellicht (licht.gd LICHT, iets geler)
const DEKKING := 0.50   # was 0,60: blinde lezer 1 vond het een gloed, "een beetje opgeplakt"
const PX := 2.0                           # 2 spelpx naar elke kant: de buitenste spelpx valt buiten de donkere rand
const RICHTING := [Vector2(-1, 0), Vector2(1, 0), Vector2(0, -1), Vector2(0, 1)]
const SOORT_DONKER := [0.5, 1.0, 0.0]     # per soort steen (0 baksteen, 1 koel, 2 leem) hoe donker achter de held
const LICHT_VAN := 0.70                   # helderheid van de lichtkaart: hieronder vol, boven LICHT_TOT niets
const LICHT_TOT := 0.88
const OPKOM_S := 0.4                      # zo lang om van 0 naar vol te gaan
const MEET_S := 0.2                       # zo vaak de plek opnieuw meten (per held)
const TORSO := 6.0                        # zo veel spelpx boven de voeten meten
static var _scherp := {}  # silhouet en stap -> ring (zie ring())
static var aan := true
static var wissel := false
static var _gelezen := false
# Meten binnen één run (balans.md): wissel=licht zet hem om de 20 s aan en uit (oneven blokken uit), wissel=nep schrijft
# dezelfde regels maar laat hem aan (placebo). Regel "HOL wissel licht aan|uit unix= t= pad=Hol" voor cpu_stenen.py.
# licht_proef=meet: wel meten (sterkte), niet tekenen; licht_proef=mip: ring met mipmaps en lineair (zoals het silhouet).
static var WISSEL_S := 20.0   # licht_blok=<s>: kortere blokken (minder last van wat er in het spel gebeurt)
static var _blok := 0      # 0 geen wissel, 1 echt, 2 placebo
static var _was := true
static var proef := ""
static var keer := 1      # licht_keer=<n>: alles n keer (meten, tekenen), om de kosten van één keer boven de ruis te tillen

static func is_aan() -> bool:
	if not _gelezen:
		_gelezen = true
		var args := OS.get_cmdline_user_args()
		for a in args:
			if a == "licht=0":
				aan = false
			if a == "licht_wissel=1":
				wissel = true
				aan = true
			if a == "wissel=licht" or a == "wissel=nep":
				_blok = 1 if a == "wissel=licht" else 2
			if a.begins_with("licht_blok="):
				WISSEL_S = clampf(float(a.substr(11)), 1.0, 60.0)
			if a.begins_with("licht_keer="):
				keer = clampi(int(a.substr(11)), 1, 1000)
			if a.begins_with("licht_proef="):
				proef = a.substr(12)
		for a in args:
			if a.begins_with("uit3d=") and "licht" in a.substr(6).split(",", false):
				aan = false
	return aan and _blok_aan()

static func _blok_aan() -> bool:
	if _blok == 0:
		return true
	var nu := int(Time.get_unix_time_from_system() / WISSEL_S) % 2 == 0
	if nu != _was:
		_was = nu
		var lus := Engine.get_main_loop() as SceneTree
		var sc: Node = lus.current_scene if lus != null else null
		var t: float = float(sc.get("t")) if sc != null and sc.get("t") != null else -1.0
		print("HOL wissel licht %s unix=%.2f t=%.2f pad=Hol" % ["aan" if nu else "uit", Time.get_unix_time_from_system(), t])
	return nu or _blok == 2

# Hoe donker (0 tot 1) staat de steen achter spelpixel x: gemiddelde van de twee rijen blokken op de gangwand.
static func steen_donker(x: float) -> float:
	var som := 0.0
	for r in METSEL.RIJEN.size():
		var n := int(floor((x - (METSEL.BLOK_B / 2) * r) / METSEL.BLOK_B))
		while n > -100000 and METSEL.blok_rand(n, r) > x:
			n -= 1
		while METSEL.blok_rand(n + 1, r) <= x:
			n += 1
		som += float(SOORT_DONKER[METSEL.blok_soort(n, r)])
	return som / METSEL.RIJEN.size()

# 0 tot 1 uit de helderheid van de lichtkaart op die plek: donker vol, in het licht niets.
static func licht_donker(c: Color) -> float:
	var l := (c.r + c.g + c.b) / 3.0
	return clampf((LICHT_TOT - l) / (LICHT_TOT - LICHT_VAN), 0.0, 1.0)

# Doel-sterkte voor held h op dit moment (0 in de schacht en buiten een echt hol).
static func doel(h) -> float:
	var hol = h.get("hol")
	if hol == null or not hol.has_method("_ingang_x") or not ("gang" in hol):
		return 0.0
	var p: Vector2 = h.position
	if p.y < float(hol.GANG_ONDER) - 2.0:   # nog in de schacht of erboven
		return 0.0
	var t := Vector2(p.x, p.y - TORSO)
	return steen_donker(p.x) * licht_donker(LICHT.kleur_op(hol, t))

# Sterkte nu, zacht naar het doel toe; gemeten om de MEET_S, bewaard op de held zelf.
static func sterkte(h) -> float:
	if not is_aan():
		return 0.0
	# Mila 28 nov (Daan #357, #358): een vallende held draait, en de ring (NEAREST, op de maat van het blad) gaf dan een
	# geblokte rafelrand. In de put is het toch donker achter hem: geen ring tijdens de val, meteen weg, niet uitfaden.
	if h.get("staat") == "vallen":
		h.set_meta("licht_s", 0.0)
		return 0.0
	if wissel:
		return 0.0 if Engine.get_frames_drawn() % 2 == 1 else doel(h)
	var t: float = float(h.get("t")) if h.get("t") != null else 0.0
	var nu: float = h.get_meta("licht_s", -1.0)
	var vorige_t: float = h.get_meta("licht_t", t)
	var d: float = h.get_meta("licht_doel", 0.0)
	if t - float(h.get_meta("licht_meet", -99.0)) >= MEET_S:
		d = doel(h)
		for k in keer - 1:
			d = doel(h)
		h.set_meta("licht_doel", d)
		h.set_meta("licht_meet", t)
	if nu < 0.0:
		nu = d   # eerste keer: meteen goed, niet opkomen
	else:
		nu = move_toward(nu, d, clampf(t - vorige_t, 0.0, 0.1) / OPKOM_S)
	h.set_meta("licht_s", nu)
	h.set_meta("licht_t", t)
	return nu

# Het silhouet 4 keer `stap` beeldpunten verschoven over elkaar gelegd, één keer per blad en stap (native blend_rect,
# geen lus per punt). Zo kost de lichte rand 1 tekenbeurt in plaats van 4 (eerste meting met 4 + 4 tekenbeurten per held:
# +10,7 procent CPU onder software-OpenGL, te veel). Nearest, zodat de rand hard is en geen gloed (blinde lezer 1).
static func ring(sil: CanvasTexture, stap: int) -> CanvasTexture:
	var sleutel := "%d|%d" % [sil.get_instance_id(), stap]
	if _scherp.has(sleutel):
		return _scherp[sleutel]
	var img: Image = sil.diffuse_texture.get_image()
	img.clear_mipmaps()
	var uit := Image.create(img.get_width(), img.get_height(), false, Image.FORMAT_RGBA8)
	var heel := Rect2i(Vector2i.ZERO, img.get_size())
	for r in RICHTING:
		uit.blend_rect(img, heel, Vector2i(int(r.x) * stap, int(r.y) * stap))
	var c := CanvasTexture.new()
	if proef == "mip":
		uit.generate_mipmaps()
	c.diffuse_texture = ImageTexture.create_from_image(uit)
	c.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS if proef == "mip" else CanvasItem.TEXTURE_FILTER_NEAREST
	_scherp[sleutel] = c
	return c

static func kleur(s: float, alfa := 1.0) -> Color:
	return Color(KLEUR.r, KLEUR.g, KLEUR.b, DEKKING * s * alfa)

# Tekent de ring in de lichte kleur, 1 tekenbeurt. Voor het lijf: transform zoals rand_lijf.
static func rand_lijf(h, sil: CanvasTexture, doel_r: Rect2, bron: Rect2, sx: float, s: float, alfa := 1.0) -> void:
	if proef == "meet":
		return
	var stap := int(round(PX * bron.size.x / maxf(doel_r.size.x, 0.001)))   # beeldpunten per 2 spelpx
	h.draw_set_transform(Vector2.ZERO, 0, Vector2(sx, 1))
	for k in keer:
		h.draw_texture_rect_region(ring(sil, stap), doel_r, bron, kleur(s, alfa))

static func rand_hoed(h, sil: CanvasTexture, plek: Vector2, draai: float, schaal: Vector2, doel_r: Rect2, bron: Rect2, s: float, alfa: float) -> void:
	if proef == "meet":
		return
	var stap := int(round(PX * bron.size.x / maxf(doel_r.size.x * absf(schaal.y), 0.001)))
	h.draw_set_transform(plek, draai, schaal)
	for k in keer:
		h.draw_texture_rect_region(ring(sil, stap), doel_r, bron, kleur(s, alfa))
