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
# "Hier kun je graven" als 3D-kiezeltjes (Bram 14 nov, ontwerp/steam/graaf-3d/maak_graafstip.py): 2 vakken van
# 12 x 64 bladpixels (3 x 16 spelpixels). Lineair gefilterd zoals hol_3d.gd. Zonder blad blijven de pixelstippels.
const STIP3D_PAD := "res://kunst/3d/graafstip_3d.png"
static var STIP3D: CanvasTexture = _laad_stip3d()

static func _laad_stip3d() -> CanvasTexture:
	if not ResourceLoader.exists(STIP3D_PAD):
		return null
	var t := CanvasTexture.new()
	t.diffuse_texture = load(STIP3D_PAD)
	t.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS
	return t
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
	return "%s|%s|%s|%s|%d|%d|%d|%.2f|%d|%s|%d" % [h.gang, h.boven, v, o, put_niv, h.ingang_kol, h.schat_kol,
		h._ingang_x(), h.max_kol, h.met_3d, mini(wand_hoeden().size(), WAND_MAX)]

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
			var links_open: bool = k > 0 and gang[k - 1]
			# Bram 14 nov (Daan 13:42): op de 3D-gang vier kiezeltjes uit graafstip_3d.png op dezelfde plek
			# (vak 0: gang links van de cel, vak 1: gang rechts), anders de oude pixelstippels
			if h.met_3d and STIP3D != null:
				d.draw_texture_rect_region(STIP3D, Rect2(k * KOL + (0 if links_open else KOL - 3), GANG_BOVEN, 3, KOL),
					Rect2(0 if links_open else 12, 0, 12, 64))
				continue
			var kx: int = k * KOL + (1 if links_open else KOL - 2)
			for y in range(GANG_BOVEN + 3, GANG_BOVEN + KOL - 2, 3):
				d.draw_rect(Rect2(kx, y, 1, 1), Color("#c9a27a"))
	# ingang: poortje op de grasrand boven de schacht (schuift mee als je links graaft); voor het brokkelen,
	# want het 3D-stuk is 16 x 40 en dekkend en schoof anders over de net gegraven kolom heen (controleur 13 nov)
	var ix: float = h._ingang_x()
	# Bram 14 nov: met een los boogstuk het ingangstuk pas vanaf het maaiveld, zodat de grastegel eronder doorloopt
	# (het gras in het ingangstuk zelf week af en gaf een harde rechthoek), en de boogstenen er los overheen
	if h.met_3d and HOL3D.heeft("ingang") and HOL3D.heeft("ingang_boog"):
		HOL3D.teken_vanaf(d, "ingang", Vector2(ix, 0), OPP)
		HOL3D.teken(d, "ingang_boog", Vector2(ix, 0))
	elif not (h.met_3d and HOL3D.teken(d, "ingang", Vector2(ix, 0))):
		d.draw_texture(INGANG, Vector2(ix - 2, OPP - 14 + 4))
	# de hoedenwand (Mila 16 nov): de hoeden van opgegeten helden half in de aarde boven de gang
	if h.met_3d and HOL3D.heeft_wand():
		var wh: Array = wand_hoeden()
		var wp: Array = wand_plekken(h, HOL3D.schatkamer_aan(h))
		for hp in wand_verdeling(wh, wp):
			HOL3D.teken_wand(d, int(hp[0]), hp[1])
	# versiering op vaste plekken in de gang (stut tegen het plafond, iets op de vloer); achter de figuren.
	# Brokkelen (hol.gd) komt er los overheen: in de gang liggen nieuwe cellen aan de rand, waar geen versiering staat;
	# bij een kamer valt het stof 2 spelpixels over een vloerding eronder (controleur, kan, bijna niet te zien).
	# Op de 3D-gang het 3D-stuk uit het deco-blad als het daar staat (HOL3D.DECO_GANG), met hetzelfde voet- of hangpunt
	# als het pixelding: vloerdingen staan op de gangvloer, stut en spinrag hangen aan het plafond.
	var vloer: int = h.GANG_ONDER - 1
	var gang_3d: bool = h.met_3d and HOL3D.heeft("gang")
	var midden: float = KOL / 2.0
	var vorige := -99   # kolom van het laatste stuk: hooguit één stuk per twee gangtegels (Daan 14 nov 02:50)
	if gang_3d and is_vol(h):
		_teken_vol(d, vloer)
		return
	for k in range(h.ingang_kol + 1, h.schat_kol - 1):
		var hh: int = h._hash(k, 7)
		if h.deco_proef:   # keurstrook: vaste rij, paddenstoel, stut, ton, schedel, (put), kristal, spinrag, lichtzwam (99 = niets)
			hh = DECO_PROEF[(k - h.ingang_kol - 1) % DECO_PROEF.size()]
		if h.vallen.has(k):
			continue
		hh = deco_hh(h, k, hh, vorige)
		if hh < 30 or (hh < 36 and not h.boven[k]):   # spinrag alleen onder een dicht plafond (zie onder)
			vorige = k
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

# Welke versiering op gangkolom k komt (hh zoals in teken(): onder 14 stut, 14 tot 30 een vloerding, 30 tot 36 spinrag,
# 99 = niets). Dunner na de frisse kijker (Daan 14 nov 02:50 en 03:55):
# 1. hooguit één stuk per twee gangtegels: niets direct naast het vorige stuk;
# 2. geen vloerding waar helden stilstaan of vallen (op hun looppad): de eerste tegel na de schacht (daar staat de held net na zijn val, keurstrook 14 nov) en de tegels naast een val;
#    daar mag wel iets dat aan het plafond hangt (stut, spinrag);
# 3. geen lichtzwam binnen twee tegels van Gloop (schat_kol - 2): zijn cyaan trekt aan Gloops mint; dan een paddenstoel.
# Bij de keurstrook (deco_proef in hol.gd, als die er is) blijft de vaste rij staan.
static func deco_hh(h, k: int, hh: int, vorige: int) -> int:
	if h.get("deco_proef") == true:
		return hh
	if k - vorige < 2:
		return 99
	if hh >= 14 and hh < 30:
		if k == h.ingang_kol + 1 or h.vallen.has(k - 1) or h.vallen.has(k + 1):
			return 99
		if hh % 5 == 1 and absi(k - (h.schat_kol - 2)) <= 2:
			return hh - 1   # soorten[hh % 5]: 1 = lichtzwam, 0 = paddenstoel
	return hh

# Een vol hol (Mila 16 nov, "het hol moet vol", voor de winkelbeelden): vanaf VOL_VANAF gangtegels geldt de uitdunning
# van 14 nov niet meer. Daan dunde uit omdat een frisse kijker een LEEG hol druk vond; in een groot hol is het juist kaal.
# Alleen op de 3D-gang (de pixelgang houdt de oude regels). Wat blijft: geen vloerding waar helden stilstaan of vallen
# (eerste tegel na de schacht, naast een val), en niets bij de stapel hoeden en Gloop (dus ook geen lichtzwam bij Gloop).
const VOL_VANAF := 20
const VLOER_SOORTEN := [0, 1, 2, 3, 4, 5]      # DECO_GANG: paddenstoel, lichtzwam, ton, krat, schedel, kristal
const KAMER_SOORTEN := [4, 2, 3, 0, 5]         # in de kamers: schedel, ton, krat, paddenstoel, kristal (geen lichtzwam)
const KAMER_SCHAAL := 0.8                      # kamers liggen achter de gang: iets kleiner leest als diepte (doelbeeld Mila)
const KAMER_VLOER := 22                        # vloer van een kamer in de bovenste rij (gemeten in kamer_begin/_eind)
const VOL_TROON := 5                           # vanaf schat_kol - 5 niets: hoedenhoop en Gloop, en één tegel vrij ervoor
const GROOT := [2, 3, 7]                       # ton, krat, stut: nooit twee op tegels naast elkaar (Daan 16 nov, regel b)
const KLEIN := [0, 1, 4, 5]                    # paddenstoel, lichtzwam, schedel, kristal: mogen wel naast een groot ding
const HANG_MAX := 6.0                          # spinrag en vaandel hooguit een derde van de gang (±18 spelpixels) onder het plafond

static func is_vol(h) -> bool:
	if h.get("deco_proef") == true:
		return false
	var g = h.get("gang")
	return g != null and (g as Array).count(true) >= VOL_VANAF

# Vloerding op gangkolom k in een vol hol: index in DECO_GANG, of -1. Nooit twee keer dezelfde soort naast elkaar.
static func vol_vloer(h, k: int, vorige_soort: int) -> int:
	if h.vallen.has(k) or k == h.ingang_kol + 1 or h.vallen.has(k - 1) or h.vallen.has(k + 1):
		return -1
	if k >= h.schat_kol - VOL_TROON:   # stapel hoeden en Gloop, plus één tegel vrij ervoor (Daan 16 nov, regel c)
		return -1
	var hh: int = _hh(h, k, 7)
	var c: int = VLOER_SOORTEN[hh % VLOER_SOORTEN.size()]
	if c == vorige_soort:
		c = VLOER_SOORTEN[(hh + 1) % VLOER_SOORTEN.size()]
	return c   # (lichtzwam bij Gloop kan hier niet: alles vanaf schat_kol - 4 valt al af)

# Plafondding op gangkolom k in een vol hol, los van de vloer: 6 = spinrag, 7 = stut, 8 = vaandel, of -1.
# Alleen onder een dicht plafond (niet onder een kamer), niet bij de ingangsfakkel, niet boven de hoeden en Gloop,
# niet direct naast het vorige plafondding (de stut is breder dan een tegel). Boven een val geen stut (zijn poten).
static func vol_plafond(h, k: int, vorige_kol: int) -> int:
	if h.boven[k] or k == h.ingang_kol + 1 or k >= h.schat_kol - VOL_TROON or k - vorige_kol < 2:
		return -1
	var bij_val: bool = h.vallen.has(k) or h.vallen.has(k - 1) or h.vallen.has(k + 1)
	var hh: int = _hh(h, k, 8)
	if hh < 24:
		# de stut staat met zijn poten op de vloer: niet op of naast een val (Daan 16 nov, regel c); spinrag en vaandel
		# hangen hooguit een derde van de gang (HANG_MAX), dus de val blijft vrij en mag er wel een hebben
		return 6 if bij_val else 7
	if hh < 44:
		return 6
	if hh < 58:
		return 8
	return -1

static func _hh(h, k: int, y: int) -> int:
	if h is Dictionary:
		return int(abs(sin(k * 12.9898 + y * 78.233) * 43758.5453)) % 97   # zelfde som hol.gd _hash (toetsen)
	return h._hash(k, y)

# Twee dingen in elke kamer boven de gang, naast het kistje (Mila 16 nov, punt 2): een rij open kamers (minstens twee
# kolommen; kamer_los heeft zijn eigen paddenstoelen) krijgt er een rechts van de fakkel in kamer_begin en een links
# van het kistje in kamer_eind. Geeft [naam, voetpunt] in spelpixels.
static func kamer_dingen(h, schat_3d: bool) -> Array:
	var uit := []
	var boven: Array = h.boven
	var k := 0
	while k < boven.size():
		if not HOL3D._kamer_open(boven, k, h.ingang_kol, h.schat_kol, schat_3d):
			k += 1
			continue
		var a := k
		while k + 1 < boven.size() and HOL3D._kamer_open(boven, k + 1, h.ingang_kol, h.schat_kol, schat_3d):
			k += 1
		var b := k
		k += 1
		if b == a:
			continue
		var hh: int = _hh(h, a, 11)
		var s1: int = KAMER_SOORTEN[hh % KAMER_SOORTEN.size()]
		var s2: int = KAMER_SOORTEN[(hh + 1 + int(hh / 7.0) % (KAMER_SOORTEN.size() - 1)) % KAMER_SOORTEN.size()]
		uit.append([HOL3D.DECO_GANG[s1], Vector2(a * KOL + 10, KAMER_VLOER)])
		uit.append([HOL3D.DECO_GANG[s2], Vector2(b * KOL, KAMER_VLOER)])
	return uit

# Het hele volle gangstuk als lijst [kolom, index in DECO_GANG, hangend], van links naar rechts (Daan 16 nov, "een vol hol"):
# (a) spinrag en vaandel hangen hooguit HANG_MAX onder het plafond (zie _teken_hangend; de stut staat op de vloer, open in
# het midden, de held loopt erdoor); (b) nooit twee grote dingen (ton, krat, stut) op tegels naast elkaar of op dezelfde
# tegel: dan een stut wordt spinrag, een ton of krat wordt een klein ding; (c) één tegel vrij naast een val en voor de troon.
static func vol_rij(h) -> Array:
	var uit := []
	var groot := {}
	var vorige_soort := -1
	var vorige_plafond := -99
	for k in range(h.ingang_kol + 1, h.schat_kol - 1):
		var p := vol_plafond(h, k, vorige_plafond)
		if p == 7 and groot.has(k - 1):
			p = 6
		if p >= 0:
			uit.append([k, p, true])
			vorige_plafond = k
			if p in GROOT:
				groot[k] = true
		var c := vol_vloer(h, k, vorige_soort)
		if c in GROOT and (groot.has(k - 1) or groot.has(k)):
			var hh: int = _hh(h, k, 9)
			c = KLEIN[hh % KLEIN.size()]
			if c == vorige_soort:
				c = KLEIN[(hh + 1) % KLEIN.size()]
		vorige_soort = c
		if c >= 0:
			uit.append([k, c, false])
			if c in GROOT:
				groot[k] = true
	return uit

func _teken_vol(d: CanvasItem, vloer: int) -> void:
	var midden: float = KOL / 2.0
	var schat_3d: bool = HOL3D.schatkamer_aan(h)
	for kd in kamer_dingen(h, schat_3d):
		HOL3D.teken_deco_op(d, kd[0], kd[1], false, KAMER_SCHAAL)
	for ding in vol_rij(h):
		var naam: String = HOL3D.DECO_GANG[ding[1]]
		if not ding[2]:
			HOL3D.teken_deco_op(d, naam, Vector2(ding[0] * KOL + midden, vloer + 1), false)
		elif naam == "stut":
			HOL3D.teken_deco_op(d, naam, Vector2(ding[0] * KOL + midden, GANG_BOVEN), true)
		else:
			_teken_hangend(d, naam, Vector2(ding[0] * KOL + midden, GANG_BOVEN))

# Hangend ding hooguit HANG_MAX onder het hangpunt (Daan 16 nov, regel a: "een ding door het hoofd van een held leest als
# een fout"). Het vaandel kleiner tot het past, want een half vaandel leest als kapot. Het spinrag heel en kleiner
# (SPIN_SCHAAL) en zonder de draad en de paarse spin rechts ervan: Daan 16 nov 10:50, moet, "onderaan recht afgesneden met
# een los draadje ernaast leest als een kapot plaatje"; de spin leek ook op de vleermuis (één kleur per soort beestje).
const SPIN_SCHAAL := 0.6
# Alleen het web uit het vak van het spinrag, in bladpixels binnen `vak_px` [x, y, b, h]: de draad staat vanaf x 57, de
# spin rechtsonder vanaf x 44 (onder y 34) en x 49 (onder y 31). Nagemeten op kunst/3d/deco.png, vak 80 x 56.
const SPIN_WEB := [Rect2(0, 0, 56, 31), Rect2(0, 31, 49, 3), Rect2(0, 34, 44, 12)]

static func hang_schaal(naam: String) -> float:
	var m := HOL3D.deco_maat(naam)
	if m == Vector2.ZERO:
		return 1.0
	if naam == "spinrag":
		return SPIN_SCHAAL
	var hy: float = 2.2
	var s: Dictionary = HOL3D.deco[naam]
	if s.has("hang") and typeof(s["hang"]) == TYPE_ARRAY and s["hang"].size() == 2:
		hy = float(s["hang"][1])
	return minf(1.0, HANG_MAX / maxf(1.0, m.y - hy))

func _teken_hangend(d: CanvasItem, naam: String, punt: Vector2) -> void:
	var sc := hang_schaal(naam)
	var plek := HOL3D.deco_plek(naam, punt, true, sc)
	if plek == Vector2.INF:
		return
	var m := HOL3D.deco_maat(naam) * sc
	var v: Array = HOL3D.deco[naam]["vak_px"]
	if naam == "spinrag":
		var f := Vector2(m.x / float(v[2]), m.y / float(v[3]))   # spelpixels per bladpixel
		for r in SPIN_WEB:
			var w: Rect2 = r
			d.draw_texture_rect_region(HOL3D.deco_blad, Rect2(plek + w.position * f, w.size * f),
				Rect2(Vector2(v[0], v[1]) + w.position, w.size))
		return
	var hoog: float = minf(m.y, punt.y + HANG_MAX - plek.y)   # alles daaronder valt weg
	var bron_h: float = float(v[3]) * hoog / m.y
	d.draw_texture_rect_region(HOL3D.deco_blad, Rect2(plek, Vector2(m.x, hoog)), Rect2(v[0], v[1], v[2], bron_h))

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

# De hoedenwand (Mila 16 nov, punt 4, "de wand is het logboek van wie Gloop at"): elke opgegeten held laat zijn hoed
# achter, scheef half in de aardwand boven de gang (blad van Bram, wand-0 tot wand-9, met holte en aarderand erin).
# Plekken: dichte cellen in de bovenste rij boven een gegraven gang, niet bij de stapel en de schatkamer, niet bij de schacht;
# in een vaste volgorde (hash), zonder vast ritme (zie onder). De oudste hoed krijgt de eerste plek, dus de wand groeit en
# wat er hangt verschuift niet als er een hoed bij komt (tot er gegraven wordt). Midden van de hoed rond rij 16.
const WAND_MAX := 64       # meer plekken dan dit heeft geen scherm; houdt de sleutel klein
const WAND_Y_MIN := 14     # midden van de hoed; 14 tot 19 blijft in de aarde boven de gang
const WAND_Y_MAX := 19

static func wand_plekken(h, schat_3d: bool) -> Array:
	var kand := []
	var eind: int = h.schat_kol - (4 if schat_3d else 1)   # 3D: niet achter de stapel hoeden, Gloop en de schatkamer
	for k in range(h.ingang_kol + 2, eind):
		if not h.boven[k] and h.gang[k] and k <= h.max_kol:
			kand.append(k)
	kand.sort_custom(func(a, b): return _hh(h, a, 13) < _hh(h, b, 13) or (_hh(h, a, 13) == _hh(h, b, 13) and a < b))
	# Niet in een vast ritme (Daan 16 nov: "anders leest het als een plank"): ±1 op 4 plekken blijft leeg, soms zitten er
	# twee naast elkaar (dan op duidelijk andere hoogte), en de hoogte wisselt over WAND_Y_MIN tot WAND_Y_MAX.
	var gekozen := {}
	var uit := []
	for k in kand:
		if _hh(h, k, 15) % 4 == 0:
			continue
		var buur: int = k - 1 if gekozen.has(k - 1) else (k + 1 if gekozen.has(k + 1) else -1)
		if buur >= 0 and (_hh(h, k, 16) % 2 != 0 or gekozen.has(buur - 1) or gekozen.has(buur + 1)
				or gekozen.has(k - 1) and gekozen.has(k + 1)):
			continue
		var hh: int = _hh(h, k, 14)
		var y: int = WAND_Y_MIN + hh % (WAND_Y_MAX - WAND_Y_MIN + 1)
		var dx: int = (hh % 5) - 2
		if buur >= 0:
			var yb: int = int(gekozen[buur].y)
			if absi(y - yb) < 3:
				y = yb + 3 if yb + 3 <= WAND_Y_MAX else yb - 3
			dx = 2 if buur < k else -2   # een paar: iets uit elkaar, de hoeden raken elkaar net niet
		var plek := Vector2(k * KOL + 8 + dx, y)
		gekozen[k] = plek
		uit.append(plek)
		if uit.size() >= WAND_MAX:
			break
	return uit

# Welke hoed op welke plek (Daan 16 nov 11:15, kan: "drie kronen op een rij van vijf plekken; zet dezelfde hoed niet in
# naburige plekken"). Naburig = hooguit WAND_BUUR plekken links of rechts op de wand (van links naar rechts geteld), dus
# in elke vijf plekken op een rij geen hoed twee keer als het kan. Oudste hoed eerst, elk op de eerste vrije plek (in de
# volgorde van wand_plekken) zonder zelfde buur; lukt dat nergens, dan de plek met de minste en verste zelfde buren. Een nieuwe hoed verschuift
# niets dat al hangt.
const WAND_BUUR := 2
static func wand_verdeling(wh: Array, wp: Array) -> Array:
	var xs: Array = []
	for p in wp:
		xs.append((p as Vector2).x)
	xs.sort()
	var rang := {}
	for n in xs.size():
		rang[xs[n]] = n
	var uit := []
	var bezet := {}   # rang -> hoed
	var vrij: Array = wp.duplicate()
	for hoed in wh:
		if vrij.is_empty():
			break
		var keus: int = 0
		var minst: int = 99
		for j in vrij.size():
			var r: int = rang[(vrij[j] as Vector2).x]
			var botst: int = 0   # zelfde hoeden binnen WAND_BUUR, de dichtste telt zwaarder
			for dr in range(-WAND_BUUR, WAND_BUUR + 1):
				if dr != 0 and bezet.get(r + dr, -1) == int(hoed):
					botst += WAND_BUUR + 1 - absi(dr)
			if botst < minst:
				minst = botst
				keus = j
				if botst == 0:
					break
		bezet[rang[(vrij[keus] as Vector2).x]] = int(hoed)
		uit.append([hoed, vrij[keus]])
		vrij.remove_at(keus)
	return uit

# De hoeden van Gloop, oudste eerst (slijm.gd `hoeden`), via de strook; leeg in de toetsen zonder strook.
func wand_hoeden() -> Array:
	if h == null:
		return []
	var s = h.get_parent()
	var sl = s.get("slijm") if s != null else null
	if sl == null:
		return []
	var hd = sl.get("hoeden")
	return hd if hd is Array else []
