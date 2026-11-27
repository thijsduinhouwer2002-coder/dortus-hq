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
# Warm, als het fakkellicht. Koel blauwgrijs (Daan #266 K1) geprobeerd op 27 nov: een blinde lezer vond dat juist "een
# uitsnede met witte contour" (2 van 5) en warm "licht dat op de rand valt" (4 van 5). Daarom warm, maar alleen aan de
# kant van het licht (zie masker), wat hij ook noemde: "echt licht is aan de lichtkant sterker".
const KLEUR := Color(1.0, 0.88, 0.66)
const DEKKING := 0.50
const WEG := 6    # beeldpunten: zo ver schuift het masker van het licht af; aan de lichtkant blijft ±1 spelpx, achter niets
const ZAK := 3    # en zo ver omlaag: bovenop een dunner randje, onder de voeten niets
const PX := 1.85   # zo ver naar buiten (spelpx van de held): de donkere rand is 1, dus ±1 spelpx licht zichtbaar (Iris: 1 spelpx)
const RICHTING := [Vector2(-1, 0), Vector2(1, 0), Vector2(0, -1), Vector2(0, 1)]
const SOORT_DONKER := [0.5, 1.0, 0.0]     # per soort steen (0 baksteen, 1 koel, 2 leem) hoe donker achter de held
const LICHT_VAN := 0.70                   # helderheid van de lichtkaart: hieronder vol, boven LICHT_TOT niets
const LICHT_TOT := 0.88
const OPKOM_S := 0.4                      # zo lang om van 0 naar vol te gaan
const MEET_S := 0.2                       # zo vaak de plek opnieuw meten (per held)
const TORSO := 6.0                        # zo veel spelpx boven de voeten meten
static var _masker := {}  # beeld en hoed -> [textuur, Rect2] (zie masker())
static var _beeld := {}   # silhouet -> hard Image
static var aan := true
static var wissel := false
static var _gelezen := false
# Meten binnen één run (balans.md): wissel=licht zet hem om de 20 s aan en uit (oneven blokken uit), wissel=nep schrijft
# dezelfde regels maar laat hem aan (placebo). Regel "HOL wissel licht aan|uit unix= t= pad=Hol" voor cpu_stenen.py.
# licht_proef=meet: wel meten (sterkte), niet tekenen.
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

# Sinds #276 (Iris 3240a1b mooi punt 1 "zacht en golvend, sticker", Daan #266 K2 "uitstulping bij hoed en elleboog"):
# één masker voor lijf en hoed samen, op de maat van het blad (5 beeldpunten per spelpx, dus fijner dan het scherm):
# 1. het silhouet hard gemaakt (alfa 0 of vol, geen zachte waas);
# 2. de hoed erin op zijn plek en maat, zodat er geen dubbele rand komt waar hoed en lijf elkaar raken;
# 3. 2 spelpx gegroeid met afwisselend 4 en 8 buren (bijna rond), dus overal even breed in plaats van golvend;
# 4. het lijf zelf eruit. Het binnenste stuk valt onder de donkere rand, je ziet 1 spelpx licht met een harde rand.
# Alles met Image-bewerkingen van de motor (geen lus per punt), één keer per beeld en hoed; daarna 1 tekenbeurt.
# Vroeger: het zachte silhouet 4 keer 2 spelpx verschoven, apart voor lijf en hoed.
const MARGE := 3   # spelpx rond het masker
const BUREN4 := [Vector2i(-1, 0), Vector2i(1, 0), Vector2i(0, -1), Vector2i(0, 1)]
const BUREN8 := [Vector2i(-1, 0), Vector2i(1, 0), Vector2i(0, -1), Vector2i(0, 1), Vector2i(-1, -1), Vector2i(1, -1), Vector2i(-1, 1), Vector2i(1, 1)]

# Hard silhouet (alfa >= 0,5 vol, anders leeg), één keer per blad.
static func hard(sil) -> Image:
	var k: int = sil.get_instance_id() if sil is Object else 0
	if sil is Image:
		return _hard_van(sil)
	if not _beeld.has(k):
		var im: Image = (sil as CanvasTexture).diffuse_texture.get_image()
		im.clear_mipmaps()
		_beeld[k] = _hard_van(im)
	return _beeld[k]

static func _hard_van(im: Image) -> Image:
	var src := im.duplicate() as Image
	if src.is_compressed():
		src.decompress()
	src.convert(Image.FORMAT_RGBA8)
	var d := src.get_data()
	var i := 3
	while i < d.size():
		d[i] = 255 if d[i] >= 128 else 0
		i += 4
	return Image.create_from_data(src.get_width(), src.get_height(), false, Image.FORMAT_RGBA8, d)

# Bouwt het masker. lijf: {img (hard), doel, bron, px}; hoed: {img (hard), doel, bron, px, f, plek} of leeg.
# Geeft [Image, Vector2 linksboven in spelpx van de held, px]. Niet gespiegeld: tekenen met de spiegel van het lijf.
# kant: +1 licht van rechts, -1 van links, 0 rondom (alleen voor de toets).
static func masker(lijf: Dictionary, hoed: Dictionary, kant := 0) -> Array:
	var d: Rect2 = lijf["doel"]
	var b: Rect2 = lijf["bron"]
	var px: float = lijf["px"]
	var lo := d.position
	var hi := d.end
	var hoed_lt := Vector2.ZERO
	var hoed_img: Image = null
	if not hoed.is_empty():
		var f: float = hoed["f"]
		var hd: Rect2 = hoed["doel"]
		var hb: Rect2 = hoed["bron"]
		hoed_lt = (hoed["plek"] as Vector2) + hd.position * f
		lo = lo.min(hoed_lt)
		hi = hi.max(hoed_lt + hd.size * f)
		hoed_img = (hoed["img"] as Image).get_region(Rect2i(hb))
		var maat := Vector2i(maxi(1, int(round(hd.size.x * f * px))), maxi(1, int(round(hd.size.y * f * px))))
		hoed_img.resize(maat.x, maat.y, Image.INTERPOLATE_NEAREST)
	var m := int(MARGE * px)
	var bx := int(ceil((d.position.x - lo.x) * px)) + m
	var by := int(ceil((d.position.y - lo.y) * px)) + m
	var w := bx + int(ceil((hi.x - d.position.x) * px)) + m
	var hg := by + int(ceil((hi.y - d.position.y) * px)) + m
	var lijf_m := Image.create(w, hg, false, Image.FORMAT_RGBA8)
	lijf_m.blit_rect(lijf["img"], Rect2i(b), Vector2i(bx, by))
	if hoed_img != null:
		var hp := Vector2i(int(round(bx + (hoed_lt.x - d.position.x) * px)), int(round(by + (hoed_lt.y - d.position.y) * px)))
		lijf_m.blend_rect(hoed_img, Rect2i(Vector2i.ZERO, hoed_img.get_size()), hp)
	var heel := Rect2i(0, 0, w, hg)
	var uit := lijf_m.duplicate() as Image
	for stap in int(round(PX * px)):
		var nu := uit.duplicate() as Image
		for o in (BUREN4 if stap % 2 == 0 else BUREN8):
			nu.blend_rect(uit, heel, o)
		uit = nu
	var leeg := Image.create(w, hg, false, Image.FORMAT_RGBA8)
	if kant != 0:   # sikkel aan de lichtkant: het gegroeide masker van het licht af geschoven eraf
		var weg := Image.create(w, hg, false, Image.FORMAT_RGBA8)
		weg.blit_rect(uit, heel, Vector2i(-kant * WEG, ZAK))
		uit.blit_rect_mask(leeg, weg, heel, Vector2i.ZERO)
	uit.blit_rect_mask(leeg, lijf_m, heel, Vector2i.ZERO)   # lijf en hoed zelf eruit
	if kant != 0:   # niets onder de voeten (de vloer is geen rand)
		var voet := by + int(round(d.size.y * px))
		uit.fill_rect(Rect2i(0, voet, w, maxi(0, hg - voet)), Color(0, 0, 0, 0))
	return [uit, Vector2(d.position.x - bx / px, d.position.y - by / px), px]

# Van welke kant komt het licht: de dichtstbijzijnde bron uit licht.gd (fakkel bij de ingang, schat), +1 rechts, -1 links.
static func lichtkant(h) -> int:
	var hol = h.get("hol")
	if hol == null or not hol.has_method("_ingang_x"):
		return 1
	var v: int = h.get_meta("licht_kant", 0)
	if v != 0 and float(h.get("t") if h.get("t") != null else 0.0) - float(h.get_meta("licht_kant_t", -99.0)) < 1.0:
		return v
	var p: Vector2 = h.position
	var best := INF
	v = 1
	for b in LICHT.bronnen(hol):
		var bp: Vector2 = b[0]
		if bp.y < float(hol.GANG_ONDER) - 20.0:
			continue   # daglicht in de schacht telt niet voor de gang
		if absf(bp.x - p.x) < best:
			best = absf(bp.x - p.x)
			v = 1 if bp.x >= p.x else -1
	h.set_meta("licht_kant", v)
	h.set_meta("licht_kant_t", float(h.get("t") if h.get("t") != null else 0.0))
	return v

static func kleur(s: float, alfa := 1.0) -> Color:
	return Color(KLEUR.r, KLEUR.g, KLEUR.b, DEKKING * s * alfa)

# Tekent het randje om lijf en hoed samen. lijf: {sil, doel, bron, px}; hoed: {sil, doel, bron, px, f, plek} of leeg.
static func teken(h, lijf: Dictionary, hoed: Dictionary, sx: float, alfa := 1.0) -> void:
	var s := sterkte(h)
	if s <= 0.01 or proef == "meet":
		return
	var kant := lichtkant(h) * int(sx)   # masker is ongespiegeld: bij een gespiegeld lijf de andere kant
	var sleutel := "%d|%s|%s|%d|%s|%s|%d" % [lijf["sil"].get_instance_id(), str(lijf["doel"]), str(lijf["bron"]),
		hoed["sil"].get_instance_id() if not hoed.is_empty() else 0, str(hoed.get("bron", "")), str(hoed.get("plek", "")), kant]
	var m: Array
	if _masker.has(sleutel):
		m = _masker[sleutel]
	else:
		if _masker.size() > 2000:
			_masker.clear()
		lijf["img"] = hard(lijf["sil"])
		if not hoed.is_empty():
			hoed["img"] = hard(hoed["sil"])
		var r := masker(lijf, hoed, kant)
		var t := CanvasTexture.new()
		t.diffuse_texture = ImageTexture.create_from_image(r[0])
		t.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
		m = [t, Rect2(r[1], Vector2((r[0] as Image).get_size()) / float(r[2]))]
		_masker[sleutel] = m
	h.draw_set_transform(Vector2.ZERO, 0, Vector2(sx, 1))
	for k in keer:
		h.draw_texture_rect(m[0], m[1], false, kleur(s, alfa))
