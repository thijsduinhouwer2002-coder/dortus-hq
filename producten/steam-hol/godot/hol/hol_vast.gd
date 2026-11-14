extends Node2D
# Het vaste deel van het hol, één keer getekend (Olaf, 13 nov; demolijst 2, afspraak 3 met Bram 13 nov 18:50).
# Met het 3D-hol kostte elk beeld waarin een held liep het hele hol opnieuw: twee rijen 3D-tegels per kolom, lineair
# met mipmaps. Duurtests tegelijk met hetzelfde zaad (777, 15 min): met 3D 0,506 CPU-s per 10 s, hoogste 1,266; zonder
# 0,233, hoogste 0,547. Daarom tekent dit knooppunt gras, tegels, schatkamer, stippels, ingang en versiering in een
# eigen beeld (SubViewport op schermgrootte) en alleen opnieuw als er iets aan verandert: graven, een put erbij of weg,
# een put die klapt of een stap koopt, de ingang die schuift. Wat beweegt (fakkels, putten die open gaan, brokkelen,
# muntjes, schat) tekent hol.gd er los overheen, zoals eerst.
# Het beeld komt terug als Sprite2D achter het hol (show_behind_parent), op schaal 1 op het scherm, met premultiplied
# alpha: in een doorzichtig beeld staat de kleur al vermenigvuldigd met de dekking, dus de randen van het gras worden
# precies zo als toen het hol direct op het venster tekende.

const KOL := 16
const H := 40
const OPP := 8
const GANG_BOVEN := 24
const TEGELS := preload("res://kunst/tegels.png")
const GRAS := preload("res://kunst/gras.png")
const MAAIVELD := preload("res://kunst/maaiveld.png")
const INGANG := preload("res://kunst/ingang.png")
const DECO := preload("res://kunst/versiering.png")
const HOL3D := preload("res://hol/hol_3d.gd")
const DECO_PROEF := [15, 0, 17, 18, 99, 19, 30, 16, 99]   # hh per gangkolom bij deco_proef (zie hol.gd): de eerste vier kolommen vol, want op 1024 breed is de gang kort (kolom 5 is de put)

var h                         # hol.gd
var vp: SubViewport
var beeld: Sprite2D
var sleutel := ""
var keer := 0                 # zo vaak opnieuw getekend (voor de toetsen en de meetregel)
# Bovenrand van wat er boven het maaiveld getekend staat, per schermpixel-kolom van het eigen beeld (0 = bovenrand van
# het hol, OPP * schaal = niets boven het gras). Leeg tot het eerste beeld gelezen is, of als lezen niet kan (headless).
# strook.gd maakt hiermee het muisvlak: op Windows tekent het venster niets buiten dat vlak (Godot 4.3,
# window_set_mouse_passthrough), dus zonder dit waren gras, plantjes en de top van de ingang weg (Bram 14 nov 02:35).
var rand := PackedInt32Array()
var rand_keer := 0            # zo vaak gelezen (toetsen)

func maak_in(hol) -> void:
	h = hol
	var s: int = maxi(1, int(round(hol.scale.x)))
	vp = SubViewport.new()
	vp.name = "HolVast"
	vp.transparent_bg = true
	vp.disable_3d = true
	vp.size = Vector2i(maxi(1, hol.kolommen * KOL * s), H * s)
	vp.render_target_update_mode = SubViewport.UPDATE_DISABLED
	vp.canvas_item_default_texture_filter = Viewport.DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_NEAREST
	hol.add_child(vp)
	scale = Vector2(s, s)
	texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	vp.add_child(self)
	beeld = Sprite2D.new()
	beeld.name = "HolVastBeeld"
	beeld.centered = false
	beeld.texture = vp.get_texture()
	beeld.scale = Vector2.ONE / s
	beeld.show_behind_parent = true
	beeld.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	var mat := CanvasItemMaterial.new()
	mat.blend_mode = CanvasItemMaterial.BLEND_MODE_PREMULT_ALPHA
	beeld.material = mat
	hol.add_child(beeld)

# Alles waar het vaste beeld van afhangt. Anders dan de vorige keer: één keer opnieuw tekenen.
func _sleutel() -> String:
	var put_niv: int = h.upgrades.niveau("stekelput") if h.upgrades != null else 0
	var v: Array = h.vallen.keys()
	v.sort()
	var o: Array = h.put_open.keys()
	o.sort()
	return "%s|%s|%s|%s|%d|%d|%d|%.2f|%d|%s" % [h.gang, h.boven, v, o, put_niv, h.ingang_kol, h.schat_kol,
		h._ingang_x(), h.max_kol, h.met_3d]

# hol.gd roept dit aan het begin van elke _draw aan; kost alleen het maken van de sleutel
func ververs() -> void:
	if vp == null:
		return
	var k := _sleutel()
	if k == sleutel:
		return
	sleutel = k
	keer += 1
	queue_redraw()
	vp.render_target_update_mode = SubViewport.UPDATE_ONCE
	_lees_later(keer)

# Na het tekenen het beeld één keer terugzien om de bovenrand van gras, plantjes en ingang te meten. Gebeurt alleen
# als het vaste beeld opnieuw getekend is (graven, put, ingang), dus zelden; twee beelden wachten, want UPDATE_ONCE
# tekent pas in het volgende beeld.
func _lees_later(nr: int) -> void:
	if not is_inside_tree():
		return
	await RenderingServer.frame_post_draw
	await RenderingServer.frame_post_draw
	if nr != keer or vp == null:
		return
	var tex := vp.get_texture()
	var img: Image = tex.get_image() if tex != null else null
	if img == null or img.is_empty():
		return
	lees_rand(img, int(round(scale.x)))
	var s = h.get_parent() if h != null else null
	if s != null and s.has_method("rand_veranderd"):
		s.rand_veranderd()

# Per kolom de eerste rij (schermpixels) met iets erin, boven het maaiveld. Los aan te roepen voor de toetsen.
func lees_rand(img: Image, s: int) -> void:
	if img.get_format() != Image.FORMAT_RGBA8:
		img.convert(Image.FORMAT_RGBA8)
	var w := img.get_width()
	var tot := mini(OPP * s, img.get_height())
	var data := img.get_data()
	var r := PackedInt32Array()
	r.resize(w)
	for x in w:
		var top := tot
		for y in tot:
			if data[(y * w + x) * 4 + 3] > 8:   # alfa boven ±3 %: een zachte 3D-rand telt mee
				top = y
				break
		r[x] = top
	rand = r
	rand_keer += 1

func _draw() -> void:
	if h != null:
		teken(self)

# Het vaste deel, op doek d (dit knooppunt in het eigen beeld, of het hol zelf als hol.gd met_vast uit heeft).
func teken(d: CanvasItem) -> void:
	# maaiveld: gras met hier en daar een plantje of steen
	var gras_3d: bool = h.met_3d and HOL3D.heeft("gras")
	for k in h.kolommen:
		if not (gras_3d and HOL3D.teken(d, "gras", Vector2(k * KOL, 0))):
			d.draw_texture_rect_region(GRAS, Rect2(k * KOL, 0, KOL, OPP), Rect2((k % 4) * KOL, 0, KOL, OPP))
		var hh: int = h._hash(k, 99)
		if hh < 22 and k != h.ingang_kol and k <= h.max_kol + 1:
			# op 3D-gras het 3D-plantje uit het deco-blad (voet op de grasrand), anders het pixelplantje
			if not (gras_3d and HOL3D.teken_deco_op(d, HOL3D.DECO_MAAIVELD[hh % 5], Vector2(k * KOL + KOL / 2.0, OPP), false)):
				d.draw_texture_rect_region(MAAIVELD, Rect2(k * KOL, 0, KOL, OPP), Rect2((hh % 5) * KOL, 0, KOL, OPP))
	# twee rijen cellen
	var schat_3d: bool = HOL3D.schatkamer_aan(h)
	for k in h.kolommen:
		_tegel(d, k * KOL, OPP, 0, k, schat_3d)
		_tegel(d, k * KOL, GANG_BOVEN, 1, k, schat_3d)
	if schat_3d:
		HOL3D.teken(d, "schatkamer", Vector2((h.schat_kol - 2) * KOL, OPP))
	var gang: Array = h.gang
	for k in h.kolommen:
		# hier kun je graven: lichte stippels op de rand
		if not gang[k] and k <= h.max_kol and ((k > 0 and gang[k - 1]) or (k < h.kolommen - 1 and gang[k + 1])):
			var kx: int = k * KOL + (1 if k > 0 and gang[k - 1] else KOL - 2)
			for y in range(GANG_BOVEN + 3, GANG_BOVEN + KOL - 2, 3):
				d.draw_rect(Rect2(kx, y, 1, 1), Color("#c9a27a"))
	# ingang: poortje op de grasrand boven de schacht (schuift mee als je links graaft); voor het brokkelen,
	# want het 3D-stuk is 16 x 40 en dekkend en schoof anders over de net gegraven kolom heen (controleur 13 nov)
	var ix: float = h._ingang_x()
	if not (h.met_3d and HOL3D.teken(d, "ingang", Vector2(ix, 0))):
		d.draw_texture(INGANG, Vector2(ix - 2, OPP - 14 + 4))
	# versiering op vaste plekken in de gang (stut tegen het plafond, iets op de vloer); achter de figuren.
	# Brokkelen (hol.gd) komt er los overheen: in de gang liggen nieuwe cellen aan de rand, waar geen versiering staat;
	# bij een kamer valt het stof 2 spelpixels over een vloerding eronder (controleur, kan, bijna niet te zien).
	# Op de 3D-gang het 3D-stuk uit het deco-blad als het daar staat (HOL3D.DECO_GANG), met hetzelfde voet- of hangpunt
	# als het pixelding: vloerdingen staan op de gangvloer, stut en spinrag hangen aan het plafond.
	var vloer: int = h.GANG_ONDER - 1
	var gang_3d: bool = h.met_3d and HOL3D.heeft("gang")
	var midden: float = KOL / 2.0
	for k in range(h.ingang_kol + 1, h.schat_kol - 1):
		var hh: int = h._hash(k, 7)
		if h.deco_proef:   # keurstrook: vaste rij, paddenstoel, stut, ton, schedel, (put), kristal, spinrag, lichtzwam (99 = niets)
			hh = DECO_PROEF[(k - h.ingang_kol - 1) % DECO_PROEF.size()]
		if h.vallen.has(k):
			continue
		if hh < 14:
			if not (gang_3d and HOL3D.teken_deco_op(d, HOL3D.DECO_GANG[7], Vector2(k * KOL + midden, GANG_BOVEN), true)):
				d.draw_texture_rect_region(DECO, Rect2(k * KOL, GANG_BOVEN, KOL, KOL), Rect2(7 * KOL, 0, KOL, KOL))   # stut
		elif hh < 30:
			var soorten := [0, 1, 2, 4, 5]   # paddenstoel, lichtzwam, ton, schedel, kristal
			var c: int = soorten[hh % 5]
			if not (gang_3d and HOL3D.teken_deco_op(d, HOL3D.DECO_GANG[c], Vector2(k * KOL + midden, vloer + 1), false)):
				d.draw_texture_rect_region(DECO, Rect2(k * KOL, vloer - 15, KOL, KOL), Rect2(c * KOL, 0, KOL, KOL))
		elif hh < 36 and not h.boven[k]:
			if not (gang_3d and HOL3D.teken_deco_op(d, HOL3D.DECO_GANG[6], Vector2(k * KOL + midden, GANG_BOVEN), true)):
				d.draw_texture_rect_region(DECO, Rect2(k * KOL, GANG_BOVEN, KOL, KOL), Rect2(6 * KOL, 0, KOL, KOL))   # spinrag

func _tegel(d: CanvasItem, x: float, y: float, r: int, k: int, schat_3d: bool) -> void:
	var stuk: String = HOL3D.stuk(h, r, k, schat_3d)
	if stuk != "" and HOL3D.teken(d, stuk, Vector2(x, y)):
		return
	if h._open(r, k):
		var n: bool = r == 0 or not h._open(0, k)
		if r == 0 and k == h.ingang_kol:
			n = false   # de schacht loopt door naar boven
		var s: bool = r == 0 and not h._open(1, k)
		if r == 1:
			s = true    # onder de gang zit altijd aarde
		var e: bool = not h._open(r, k + 1)
		var w: bool = not h._open(r, k - 1)
		var m := int(n) | int(e) << 1 | int(s) << 2 | int(w) << 3
		d.draw_texture_rect_region(TEGELS, Rect2(x, y, KOL, KOL), Rect2(m * KOL, KOL, KOL, KOL))
	else:
		var v: int = h._hash(k, r) % 8
		d.draw_texture_rect_region(TEGELS, Rect2(x, y, KOL, KOL), Rect2(v * KOL, 0, KOL, KOL))
