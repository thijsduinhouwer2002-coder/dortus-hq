extends RefCounted
# Tekenen van de held (Bram), los van held.gd zodat dat bestand klein blijft. held.gd roept in _draw()
# HELD_BEELD.teken(self) aan; alles wordt op de held zelf getekend (dat mag alleen tijdens zijn _draw).
# Kunst van Daan (kunst/LEESMIJ.md, Karakter-laag 19:45): lijf in 5 vaste kleuren, littekens als losse laag,
# hoed met een hap als Gloop hem beet, tekens (8 x 8) boven het hoofd. Nooit schalen (halve pixels).

const LIJF := preload("res://kunst/held_lijf_kleuren.png")   # 4 loopframes x 5 rijen (rood, groen, paars, oker, zeegroen)
const HOEDEN := preload("res://kunst/held_hoeden.png")
const HOEDEN_HAP := preload("res://kunst/held_hoeden_hap.png")
const LITTEKENS := preload("res://kunst/held_littekens.png")  # pleister, ooglap, schram, verband
const WAPENS := preload("res://kunst/held_wapens.png")
const KLEDING := preload("res://kunst/held_soort.png")          # Mila 10 nov: 4 loopframes x 4 rijen (ridder, dief, magier, bard)
const POEF := preload("res://kunst/poef.png")                 # Mila 10 nov: boze wolkje knapt, 4 x (12 x 10)
const TEKENS := preload("res://kunst/tekens.png")            # boos, uitroep, zweet, zzz, ster
const TEKEN := {"boos": 0, "uitroep": 1, "zweet": 2, "zzz": 3, "ster": 4}

# Daans lijf + kleding per soort (Mila) + litteken + hoed + wapen (16 x 16, anker midden onder), teken erboven.
static func teken(h) -> void:
	var staat: String = String(h.staat)
	if staat == "weg":
		return
	var t: float = float(h.t)
	var frame := 0
	if staat in ["lopen", "vluchten"]:
		frame = int(t * 8) % 4
	var omlaag := 1 if frame in [1, 3] else 0
	var links := staat == "vluchten"
	var wapen := 2 if String(h.trek) == "schijterig" else 0       # schijterig neemt een fakkel mee, hebzuchtig een zwaard
	var w_soort: int = h.SOORT.wapen(String(h.soort_held))
	if w_soort >= 0:
		wapen = w_soort                                            # ridder zwaard, magiër staf (heldensoort.gd)
	var kleur := Color.WHITE
	if t < float(h.geraakt_tot) and int(t * 10) % 2 == 0:
		kleur = Color(1, 0.55, 0.55)
	var vb: Dictionary = {}
	var zak := 0
	var hop := 0
	if staat == "vallen":
		vb = h.val_beeld(float(h.val_t))
		zak = int(vb.zak)
		hop = int(vb.hop)
	if links:
		h.draw_set_transform(Vector2.ZERO, 0, Vector2(-1, 1))   # spiegelen, geen halve pixels
	var y := -16 + zak + hop
	var hoed_nr: int = int(h.hoed_nr)
	var kop3d := _teken_3d(h, staat, frame, zak, hop, vb, kleur)
	if kop3d != NIET_3D:
		h.draw_set_transform(Vector2.ZERO, 0, Vector2.ONE)
		_tekens(h, staat, vb, t, kop3d - 1)
		return
	# bij een hop staat hij boven de vloer: niets afsnijden; bij zakken alles onder y 0 weg
	_laag(h, LIJF, frame * 16, int(h.kleur_nr) * 16, y, zak, kleur)
	var rij: int = h.SOORT.rij(String(h.soort_held))
	if rij >= 0:
		_laag(h, KLEDING, frame * 16, rij * 16, y, zak, kleur)    # direct na het lijf, voor littekens en hoed (kunst/LEESMIJ.md)
	for l in h.littekens:
		_laag(h, LITTEKENS, int(l) * 16, 0, y + omlaag, zak, kleur)
	if vb.is_empty() or bool(vb.hoed):
		_laag(h, HOEDEN_HAP if bool(h.is_gebeten()) else HOEDEN, hoed_nr * 16, 0, y + omlaag, zak, kleur)
	if staat != "vallen":
		_laag(h, WAPENS, wapen * 16, 0, y + omlaag, 0, kleur)
	h.draw_set_transform(Vector2.ZERO, 0, Vector2.ONE)
	# teken: één lege rij boven de bovenkant van de hoed (Sanne toets 2: 1 tot 2 spelpixels boven het hoofd)
	var tops: Array = h.get_script().get_script_constant_map().get("HOED_TOP", [])   # HOED_TOP blijft in held.gd (strook.gd leest hem daar)
	var onder: int = y + (int(tops[hoed_nr]) if hoed_nr < tops.size() else 0) + omlaag - 1
	_tekens(h, staat, vb, t, onder)

# Teken (boos, uitroep, ...), poef en nootjes boven het hoofd; onder = de rij net boven de bovenkant van de hoed.
static func _tekens(h, staat: String, vb: Dictionary, t: float, onder: int) -> void:
	var tk: String = String(h.teken_nu()) if staat != "vallen" else String(vb.teken)
	if staat != "vallen":
		for nt in nootjes(String(h.soort_held), bool(h.info.get("lied_held", false)), staat, t):
			_noot(h, int(nt[0]), onder - 6 + int(nt[1]), float(nt[2]))
	if tk == "":
		return
	if tk == "poef":
		_poef(h, onder - 4, float(vb.poef_fase))
		return
	onder = maxi(onder, teken_onder_min(h))   # Daan 14 nov 01:40: teken minstens 1 spelpixel onder de bovenrand
	if teken_3d(h, tk, 0.0, float(onder)):
		return
	h.draw_texture_rect_region(TEKENS, Rect2(-4, onder - 8, 8, 8), Rect2(int(TEKEN[tk]) * 8, 0, 8, 8))

# Tekens in 3D (Daan 14 nov 00:55, modellen/tekens.py; blad "tekens" uit de pijplijn, 5 vakken van 8 x 8 spelpixels in de
# volgorde van tekens.png). Punt van het staartje op (x, onder), dus op dezelfde plek als het pixelteken. Lineair gefilterd
# zoals het 3D-lijf. false = geen blad of geen beeld met die naam: de aanroeper tekent tekens.png (main gaat nooit kapot).
# Ook voor Gloops zzz in slijm.gd.
const TEKENS3D := "tekens"
# Laagste toegestane onderkant (rij van het staartje) voor een teken van 8 hoog, zodat de bovenkant minstens TEKEN_RAND
# spelpixels onder de bovenrand van het hol (hol-y 0) blijft; h staat in hol-coordinaten. Bij een held hoog op de ladder
# zakt het teken dan iets naar zijn hoofd toe.
const TEKEN_RAND := 1
static func teken_onder_min(h) -> int:
	if not (h is Node2D):
		return -100000
	return TEKEN_RAND + 8 - int(floor((h as Node2D).position.y))
static func teken_3d(doek: CanvasItem, naam: String, x: float, onder: float, kleur := Color.WHITE) -> bool:
	if not met_3d:
		return false
	_laad_3d()
	if not held3d.has(TEKENS3D):
		return false
	var ct: CanvasTexture = held3d[TEKENS3D][0]
	var info: Dictionary = held3d[TEKENS3D][1]
	var i: int = (info["frames"] as Array).find(naam)
	if i < 0:
		return false
	var px: float = float(info["px"])
	var cw: float = float(info["cel_px"][0])
	var ch: float = float(info["cel_px"][1])
	doek.draw_texture_rect_region(ct, Rect2(x - float(info["anker_x"]) / px, onder - ch / px, cw / px, ch / px),
		Rect2(i * cw, 0, cw, ch), kleur)
	return true

# 3D-helden (Bram 13 nov, pijplijn producten/steam-hol/pijplijn/, modellen/held.py van Daan). Schakelaar, standaard UIT:
# Hoeden: keuze A (Daan 13 nov 19:35, taken.md). De pijplijn rendert de held zonder eigen hoed ("verberg": ["hoed"]) en de
# 10 spelhoeden als eigen blad "hoeden" (modellen/hoeden.py, schaal 1,3 tegenover de held). De hoed van de held (hoed_nr)
# komt op de kruin met de onderrand 1 spelpixel in het hoofd; bij vallen tuimelt hij los (Daans twee moet-punten).
# Uitzondering op "nooit schalen" bovenin: het 3D-lijf staat niet op hele pixels, met opzet (lineair gefilterd, 4x scherp).
# Soort -> blad: ridder -> ridder, magiër -> heks. Andere soorten blijven pixels. Lijf lineair gefilterd (CanvasTexture),
# zoals Gloop in slijm.gd; de rest van de held (tekens, nootjes, poef) blijft nearest.
static var met_3d := true
const HELD3D_JSON := "res://kunst/3d/sprites.json"
const HELD3D_SOORT := {"ridder": "ridder", "magier": "heks", "dief": "dief", "bard": "bard"}
# Gewone held (soort ""): eigen blad per tuniek, held0 tot held4, gelijk aan kleur_nr (Daan 22:45, held_soorten.py), zodat
# Kees bij terugkomst dezelfde tuniek heeft. Dief en bard hun eigen blad.
const HELD3D_GEWOON := ["held0", "held1", "held2", "held3", "held4"]
# Terugval (Bram 13 nov 22:25, nog steeds nodig zolang een eigen blad ontbreekt): wie geen eigen blad heeft krijgt het ridder-
# of heksblad (via kleur_nr). Uit met GEWOON_3D := false, dan blijft zo'n held pixels.
static var GEWOON_3D := true
const HELD3D_ANDER := ["ridder", "heks"]
const NIET_3D := -9999
const HOEDEN3D := "hoeden"       # blad met de 10 hoeden in de volgorde van held.gd
const HOEDEN3D_HAP := "hoeden_hap"   # dezelfde hoeden met drie tandbogen eruit (Daan 21:45: bovenste hoed van de toren)
const HOED_IN_KOP := 1.0         # onderrand van de hoed zoveel spelpixels in de kruin (Daan: nooit zwevend)
static var held3d := {}          # blad-naam -> [CanvasTexture, info]
static var held3d_gezocht := false

# Het eigen 3D-blad van deze held (ook als het niet geladen is).
static func eigen_blad(soort: String, nr: int) -> String:
	if HELD3D_SOORT.has(soort):
		return String(HELD3D_SOORT[soort])
	return String(HELD3D_GEWOON[posmod(nr, HELD3D_GEWOON.size())])

# Welk 3D-blad hoort bij deze held ("" = pixels): het eigen blad als het geladen is, anders (GEWOON_3D) ridder of heks.
static func blad_voor(soort: String, nr: int) -> String:
	_laad_3d()
	var eigen := eigen_blad(soort, nr)
	if held3d.has(eigen):
		return eigen
	if soort == "ridder" or soort == "magier":
		return eigen
	if GEWOON_3D:
		return String(HELD3D_ANDER[absi(nr) % HELD3D_ANDER.size()])
	return ""

static func _laad_3d() -> void:
	if held3d_gezocht:
		return
	held3d_gezocht = true
	if not FileAccess.file_exists(HELD3D_JSON):
		print("HELD3D niet geladen: %s ontbreekt" % HELD3D_JSON)
		return
	var d = JSON.parse_string(FileAccess.get_file_as_string(HELD3D_JSON))
	if typeof(d) != TYPE_DICTIONARY:
		print("HELD3D niet geladen: %s is geen woordenboek" % HELD3D_JSON)
		return
	var ontbreekt := []
	for naam in HELD3D_SOORT.values() + HELD3D_GEWOON + [HOEDEN3D, HOEDEN3D_HAP]:
		if not d.has(naam) or typeof(d[naam]) != TYPE_DICTIONARY or not ResourceLoader.exists(str(d[naam].get("blad", ""))):
			ontbreekt.append(naam)
			continue
		var ct := CanvasTexture.new()
		ct.diffuse_texture = load(str(d[naam]["blad"]))
		ct.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS
		held3d[naam] = [ct, d[naam]]
	# tekens: los erbij, telt niet als ontbrekend eigen blad (zonder blad blijft tekens.png)
	if d.has(TEKENS3D) and typeof(d[TEKENS3D]) == TYPE_DICTIONARY and ResourceLoader.exists(str(d[TEKENS3D].get("blad", ""))):
		var tt := CanvasTexture.new()
		tt.diffuse_texture = load(str(d[TEKENS3D]["blad"]))
		tt.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS
		held3d[TEKENS3D] = [tt, d[TEKENS3D]]
	print("HELD3D geladen: %s; zonder eigen blad: %s; terugval op ridder/heks: %s" % [", ".join(PackedStringArray(held3d.keys())),
		", ".join(PackedStringArray(ontbreekt)) if ontbreekt else "geen", str(GEWOON_3D)])

# Welke stand uit het blad: lopen en vluchten stap1, rust, stap2, rust (zelfde klok als de pixelheld), vallen, anders rust.
static func stand_3d(staat: String, frame: int) -> String:
	if staat == "vallen":
		return "vallen"
	if staat in ["lopen", "vluchten"]:
		return ["stap1", "rust", "stap2", "rust"][frame % 4]
	return "rust"

# Tekent het 3D-lijf (voeten op y 0, midden op x 0, onder de vloer afgesneden zoals _laag) en geeft de bovenste rij van het
# hoofd (of van de spelhoed) terug, of NIET_3D als deze held pixels blijft.
static func _teken_3d(h, staat: String, frame: int, zak: int, hop: int, vb: Dictionary, kleur: Color) -> int:
	if not met_3d:
		return NIET_3D
	var naam: String = blad_voor(String(h.soort_held), int(h.kleur_nr))
	if naam == "":
		return NIET_3D
	_laad_3d()
	if not held3d.has(naam):
		return NIET_3D
	var ct: CanvasTexture = held3d[naam][0]
	var info: Dictionary = held3d[naam][1]
	var stand := stand_3d(staat, frame)
	var i: int = info["frames"].find(stand)
	if i < 0:
		i = maxi(0, info["frames"].find("rust"))
	var px: float = float(info["px"])
	var cw: float = float(info["cel_px"][0])
	var ch: float = float(info["cel_px"][1])
	var hoog := ch / px
	var zicht := hoog - float(zak)
	var x := -float(info["anker_x"]) / px
	var y := -hoog + float(zak + hop)
	if zicht <= 0.0:   # helemaal in de put gezakt: geen lijf meer, de losse hoed kan nog net zichtbaar zijn, tekens wel
		return mini(int(y), _teken_hoed_3d(h, info, i, x + float(info["anker_x"]) / px, y, staat, vb, kleur))
	h.draw_texture_rect_region(ct, Rect2(x, y, cw / px, zicht), Rect2(i * cw, 0, cw, zicht * px), kleur)
	var tops: Array = info.get("top", [])
	var kop := int(floor(y + (float(tops[i]) if i < tops.size() else 0.0)))
	var top_hoed := _teken_hoed_3d(h, info, i, x + float(info["anker_x"]) / px, y, staat, vb, kleur)
	return mini(kop, top_hoed)

# De spelhoed uit het hoedenblad op de kruin. kx, ky = plek van het anker (midden, bovenkant cel) van het lijf.
# Geeft de bovenste rij van de hoed terug (voor de tekens erboven), of een groot getal als er geen hoed staat.
static func hoed_plek_3d(info: Dictionary, i: int, kx: float, ky: float, _hi: Dictionary) -> Vector2:
	var kr: Array = info.get("kruin", [])
	var k: Array = kr[i] if i < kr.size() else [0.0, float(info.get("top", [0])[0])]
	return Vector2(kx + float(k[0]), ky + float(k[1]) + HOED_IN_KOP)   # waar het nulpunt van de hoed komt

static func _teken_hoed_3d(h, info: Dictionary, i: int, kx: float, ky: float, staat: String, vb: Dictionary, kleur: Color) -> int:
	if not held3d.has(HOEDEN3D) or not info.has("kruin"):
		return 9999
	var ct: CanvasTexture = held3d[HOEDEN3D][0]
	var hi: Dictionary = held3d[HOEDEN3D][1]
	var nr := int(h.hoed_nr)
	if nr < 0 or nr >= (hi["frames"] as Array).size():
		return 9999
	var px: float = float(hi["px"])
	var cw: float = float(hi["cel_px"][0])
	var ch: float = float(hi["cel_px"][1])
	# hoed = maal (1,3) keer de eenheid van DEZE held (controleur: de heks heeft een kleinere eenheid dan de ridder)
	var f := 1.0
	if hi.has("eenheid_px") and info.has("eenheid_px"):
		f = float(info["eenheid_px"]) * float(hi.get("maal", 1.3)) / float(hi["eenheid_px"])
	var ax: float = float(hi["anker_x"]) / px
	var ny: float = float(hi["nul_y"][nr]) if hi.has("nul_y") else ch / px
	var draai := 0.0
	var plek: Vector2
	var alfa := 1.0
	if staat == "vallen":
		if vb.is_empty() or not bool(vb.get("hoed", true)):
			return 9999                      # hoed gaat naar de toren van de bewoner: niet tekenen
		# los tuimelen: start op de kruin van rust, wipt iets op, draait weg en zakt trager dan de held (Daan moet 2)
		var ir: int = maxi(0, (info["frames"] as Array).find("rust"))
		var vt: float = float(h.val_t)
		var start := hoed_plek_3d(info, ir, kx, ky - float(int(vb.get("zak", 0)) + int(vb.get("hop", 0))), hi)
		var vlucht := hoed_tuimel(vt)
		plek = start + Vector2(vlucht.x, vlucht.y)
		draai = vlucht.z
		alfa = clampf(1.0 - plek.y / 3.0, 0.0, 1.0)   # onderrand onder de vloer (y > 0): hij vervaagt in de put
		if alfa <= 0.0:
			return 9999
	else:
		plek = hoed_plek_3d(info, i, kx, ky, hi)
	var sx := -1.0 if staat == "vluchten" else 1.0       # het lijf is dan gespiegeld (teken), de hoed dus ook
	h.draw_set_transform(Vector2(plek.x * sx, plek.y), draai * sx, Vector2(sx * f, f))
	var c := Color(kleur.r, kleur.g, kleur.b, kleur.a * alfa)
	h.draw_texture_rect_region(ct, Rect2(-ax, -ny, cw / px, ch / px), Rect2(nr * cw, 0, cw, ch), c)
	h.draw_set_transform(Vector2.ZERO, 0, Vector2.ONE)
	var tops: Array = hi.get("top", [])
	return int(floor(plek.y + (-ny + (float(tops[nr]) if nr < tops.size() else 0.0)) * f))

# Baan van de losse hoed bij vallen, tijd vt sinds de val: [dx, dy, draai in radialen]. Eerst 0,2 s omhoog (los van het
# hoofd), dan zakt hij de put in (begint hoger dan het lijf, dus blijft los te zien) en draait een derde slag weg. Los zodat de toets hem kan nakijken.
static func hoed_tuimel(vt: float) -> Vector3:
	var op := -3.0 * sin(clampf(vt / 0.4, 0.0, 1.0) * PI)            # wipt 3 spelpixels op en komt terug
	var zak := 16.0 * pow(clampf((vt - 0.25) / 0.7, 0.0, 1.0), 2.0)   # daarna de put in; voor VAL_WEG (1 s) is hij onder de vloer
	return Vector3(2.5 * clampf(vt / 0.6, 0.0, 1.0), op + zak, -2.2 * clampf(vt / 1.0, 0.0, 1.0))

# Eén laag van 16 x 16 tekenen, onder de vloerlijn (y 0) afgesneden: zo zakt hij weg zonder te schalen.
static func _laag(h, tex: Texture2D, bron_x: int, bron_y: int, y: int, zak: int, kleur: Color) -> void:
	var hoogte := 16 - zak
	if hoogte <= 0:
		return
	h.draw_texture_rect_region(tex, Rect2(-8, y, 16, hoogte), Rect2(bron_x, bron_y, 16, hoogte), kleur)

# Het boze wolkje knapt: Mila's poef.png (kunst/LEESMIJ.md, 10 nov), 4 beelden van 12 x 10, 10 fps, één keer.
# Midden van het wolkje op (6, 3) in het beeld, dus op de plek van het oude wolkje min 2 px in x. Nooit schalen.
# fase loopt van 0 tot 1 in VAL_TEKEN_S (0,4 s), dus 4 beelden in 0,4 s = 10 fps.
static func poef_beeld(fase: float) -> int:
	return clampi(int(fase * 4.0), 0, 3)

static func _poef(h, midden_y: int, fase: float) -> void:   # midden_y = onder - 4 (zoals het oude wolkje), bovenkant beeld = midden_y - 4
	h.draw_texture_rect_region(POEF, Rect2(-6, midden_y - 4, 12, 10), Rect2(poef_beeld(fase) * 12, 0, 12, 10))

# Muzieknootjes (Sanne toets 10 punt 1: "het lied zie je niet"). Een bard die binnenloopt of vlucht laat elke 2 s een
# nootje opstijgen (4 s lang, 8 spelpixels omhoog, vervaagt), dus 2 tegelijk; een held die door het lied komt heeft
# de eerste 2 s één nootje boven zijn hoofd. Geeft [x, dy, alfa] per nootje; dy 0 = vlak boven de hoed.
const NOOT_ELKE_S := 2.0
const NOOT_LEEF_S := 4.0
const NOOT_LIED_S := 2.0
static func nootjes(soort_held: String, lied_held: bool, staat: String, t: float) -> Array:
	var uit := []
	if staat in ["weg", "vallen"]:
		return uit
	if soort_held == "bard" and staat in ["afdalen", "lopen", "vluchten", "klimmen"]:
		var k := int(floor(t / NOOT_ELKE_S))
		for i: int in [k, k - 1]:
			if i < 0:
				continue
			var leef: float = t - float(i) * NOOT_ELKE_S
			if leef < 0.0 or leef >= NOOT_LEEF_S:
				continue
			var u: float = leef / NOOT_LEEF_S
			var x := (2 if i % 2 == 0 else -5) + int(round(sin(leef * 3.0)))   # om en om links en rechts, wiebelt een pixel
			uit.append([x, -int(round(8.0 * u)), 1.0 - u * u])
	elif lied_held and t < NOOT_LIED_S:
		uit.append([-2, -int(round(sin(t * 6.0))), 1.0])   # wipt op de maat
	return uit

# Nootje van 5 x 5 in pixels (achtste noot met vlag), tot Mila er een tekening voor heeft (tekens.png, 2 beelden).
const NOOT_PIX := ["..##.", "..#.#", "..#..", "###..", "###.."]
static func _noot(h, x: int, y: int, alfa: float) -> void:
	var licht := Color(1.0, 0.88, 0.45, alfa)
	var rand := Color(0.13, 0.08, 0.05, alfa * 0.9)
	for ry in 5:
		for rx in 5:
			if NOOT_PIX[ry][rx] == "#":
				for d in [Vector2i(-1, 0), Vector2i(1, 0), Vector2i(0, -1), Vector2i(0, 1)]:
					var nx: int = rx + d.x
					var ny: int = ry + d.y
					if nx < 0 or ny < 0 or nx > 4 or ny > 4 or NOOT_PIX[ny][nx] != "#":
						h.draw_rect(Rect2(x + nx, y + ny, 1, 1), rand)   # donkere rand, leesbaar op lucht en aarde
	for ry in 5:
		for rx in 5:
			if NOOT_PIX[ry][rx] == "#":
				h.draw_rect(Rect2(x + rx, y + ry, 1, 1), licht)
