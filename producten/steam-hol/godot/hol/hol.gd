extends Node2D
# Het hol (Olaf). Een raster van kolommen van 16 spelpixels breed, met Daans kunst (producten/steam-hol/godot/kunst/).
# Opbouw op 40 spelpixels (strook 120 px, schaal 3): maaiveld 8, dan twee rijen cellen van 16.
# - de onderste rij is de gang waar helden lopen (in de afspraak met Bram is dat cel.y == 0);
# - de bovenste rij is aarde, behalve de schacht bij de ingang, de schatkamer achteraan (twee rijen hoog)
#   en kamers die je zelf graaft.
# Het hol groeit in de breedte, naar links: de schat staat rechts tegen het tekstvak (Sanne toets 2, punt 0 en 6),
# zodat het tekstvak nooit over de schat ligt en het rechterdeel van de strook nooit leeg is. Graven links van de
# ingang schuift de ingang mee naar links. Afspraak met Bram (platformen/steam/taken.md): alleen deze functies en signalen gebruiken.

signal gegraven(cel: Vector2i)

const KOL := 16          # breedte van een kolom in spelpixels
const H := 40            # hoogte van de strook in spelpixels
const OPP := 8           # maaiveld
const GANG_BOVEN := 24   # bovenkant van de onderste rij (de gang)
const GANG_ONDER := 38   # anker van een figuur: voeten op y 37, de bovenste vloerrij van Daans gangtegel

const TEGELS := preload("res://kunst/tegels.png")
const GRAS := preload("res://kunst/gras.png")
const MAAIVELD := preload("res://kunst/maaiveld.png")
const INGANG := preload("res://kunst/ingang.png")
const SCHAT := preload("res://kunst/schat.png")
const PUT := preload("res://kunst/stekelput.png")
const FAKKEL := preload("res://kunst/fakkel.png")
const DECO := preload("res://kunst/versiering.png")
const GLOED := preload("res://kunst/gloed.png")

var kolommen := 0
var gang: Array[bool] = []    # onderste rij
var boven: Array[bool] = []   # bovenste rij (schacht, kamers, schatkamer)
var vallen := {}              # kolom -> soort ("stekelput")
var ingang_kol := 2
var schat_kol := 12
var max_kol := 9999           # verder graven niet: daar staat de tekst van de strook
var goud := 0                 # buit van gevallen helden; nooit iets kwijt als je weg bent
var anim := 0                 # beeldje van fakkels en schat; loopt alleen als er toch al getekend wordt
var put_open := {}            # kolom -> tijd tot de put weer dicht gaat (na een klap)
var munten: Array = []        # vliegende muntjes van een val naar de schat: {van, t}
const MUNT_S := 0.9           # zo lang vliegt een muntje

func maak(breedte_spelpixels: int) -> void:
	texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	kolommen = int(ceil(breedte_spelpixels / float(KOL)))
	gang.resize(kolommen)
	boven.resize(kolommen)
	for i in kolommen:
		gang[i] = i >= ingang_kol and i <= schat_kol
		boven[i] = false
	_schatkamer()
	vallen[7] = "stekelput"
	queue_redraw()

# leg het begin-hol aan met de schat op kolom s (rechts, tegen het tekstvak) en de ingang lengte kolommen ervoor
func leg_aan(s: int, lengte := 10) -> void:
	schat_kol = clampi(s, 3, kolommen - 1)
	# de ingang nooit op kolom 0: de ingang is breder dan een kolom en viel op een smal scherm half buiten beeld (Sanne toets 3, punt 4)
	ingang_kol = maxi(1, schat_kol - lengte)
	for i in kolommen:
		gang[i] = i >= ingang_kol and i <= schat_kol
		boven[i] = false
	_schatkamer()
	vallen.clear()
	vallen[maxi(ingang_kol + 1, mini(ingang_kol + 5, schat_kol - 3))] = "stekelput"
	queue_redraw()

# drie muntjes vliegen van kolom k naar de schat (Sanne toets 2, punt 2: goud zie je binnenkomen)
func munt_regen(k: int, n := 3) -> void:
	for i in n:
		munten.append({"van": float(k * KOL + KOL / 2.0), "t": -0.15 * i})
	set_process(true)

# de schatkamer achteraan is twee rijen hoog (Sanne, 9 nov 19:00), en Gloops plek ervoor ook (kolom schat - 2):
# daar is ruimte voor zijn hoedentoren van 4 hoog, anders steekt die in de aarde (Sanne toets 3, punt 3, besluit Olaf)
func _schatkamer() -> void:
	boven[schat_kol] = true
	for k in [schat_kol - 1, schat_kol - 2]:
		if k > ingang_kol:
			boven[k] = true

# ---- afspraak met de systemen ----
func is_gang(cel: Vector2i) -> bool:
	return cel.y == 0 and cel.x >= 0 and cel.x < kolommen and gang[cel.x]

func cel_naar_pos(cel: Vector2i) -> Vector2:
	# midden van de vloer van die cel, in spelpixels (anker van een figuur van 16 hoog)
	return Vector2(cel.x * KOL + KOL / 2.0, GANG_ONDER)

func pos_naar_cel(pos: Vector2) -> Vector2i:
	return Vector2i(clampi(int(pos.x / KOL), 0, kolommen - 1), 0)

func ingang() -> Vector2i:
	return Vector2i(ingang_kol, 0)

func schat() -> Vector2i:
	return Vector2i(schat_kol, 0)

func val_op(cel: Vector2i) -> String:
	return vallen.get(cel.x, "")

func pad(van: Vector2i, naar: Vector2i) -> Array[Vector2i]:
	var uit: Array[Vector2i] = []
	var stap := 1 if naar.x >= van.x else -1
	var x := van.x
	while true:
		if not is_gang(Vector2i(x, 0)):
			return []
		uit.append(Vector2i(x, 0))
		if x == naar.x:
			break
		x += stap
	return uit

# een put klapt even open als er een held op komt (alleen uiterlijk)
func put_klap(kol: int) -> void:
	put_open[kol] = 2.0   # stekels blijven langer omhoog, zodat de val van de terugkomer een moment is (Sanne toets 7, punt 2)
	set_process(true)
	queue_redraw()

func _process(delta: float) -> void:
	for k in put_open.keys():
		put_open[k] -= delta
		if put_open[k] <= 0.0:
			put_open.erase(k)
			queue_redraw()
	for m in munten:
		m.t += delta
	munten = munten.filter(func(m): return m.t < MUNT_S)
	if not munten.is_empty():
		queue_redraw()
	if put_open.is_empty() and munten.is_empty():
		set_process(false)

# fakkels en schat bewegen alleen als er toch al getekend wordt (een held loopt); stil beeld kost bijna niets
func tik() -> void:
	anim += 1
	queue_redraw()

# ---- spelen (klikken komen van de strook, in spelpixels) ----
func klik(pos: Vector2) -> String:
	var k := pos_naar_cel(pos).x
	var bovenrij := pos.y < GANG_BOVEN
	if bovenrij:
		# een kamer graven boven de gang (naast een open cel), niet in de lucht
		if pos.y < OPP or boven[k] or not gang[k] or k > max_kol:
			return ""
		boven[k] = true
		queue_redraw()
		gegraven.emit(Vector2i(k, -1))
		return "kamer"
	if not gang[k]:
		if k > max_kol:
			return ""
		# links van de ingang graven: de ingang schuift mee, zo groeit het hol naar links
		if k < 1:
			return ""   # kolom 0 blijft dicht, anders staat de ingang half buiten beeld
		if k == ingang_kol - 1:
			gang[k] = true
			ingang_kol = k
			queue_redraw()
			gegraven.emit(Vector2i(k, 0))
			return "gegraven"
		# alleen graven naast een bestaande gang; de schat verhuist mee naar het einde, de oude kamer blijft staan
		if (k > 0 and gang[k - 1]) or (k < kolommen - 1 and gang[k + 1]):
			gang[k] = true
			if k > schat_kol:
				schat_kol = k
				_schatkamer()
			queue_redraw()
			gegraven.emit(Vector2i(k, 0))
			return "gegraven"
		return ""
	if k != ingang_kol and k != schat_kol:
		if vallen.has(k):
			vallen.erase(k)
		else:
			vallen[k] = "stekelput"
		queue_redraw()
		return "val"
	return ""

func _hash(x: int, y: int) -> int:
	return int(abs(sin(x * 12.9898 + y * 78.233) * 43758.5453)) % 97

func _open(r: int, k: int) -> bool:
	if k < 0 or k >= kolommen:
		return false
	if r == 0:
		return boven[k] or k == ingang_kol
	return gang[k]

func _tegel(x: float, y: float, r: int, k: int) -> void:
	if _open(r, k):
		var n := r == 0 or not _open(0, k)
		if r == 0 and k == ingang_kol:
			n = false   # de schacht loopt door naar boven
		var s := r == 0 and not _open(1, k)
		if r == 1:
			s = true    # onder de gang zit altijd aarde
		var e := not _open(r, k + 1)
		var w := not _open(r, k - 1)
		var m := int(n) | int(e) << 1 | int(s) << 2 | int(w) << 3
		draw_texture_rect_region(TEGELS, Rect2(x, y, KOL, KOL), Rect2(m * KOL, KOL, KOL, KOL))
	else:
		var v := _hash(k, r) % 8
		draw_texture_rect_region(TEGELS, Rect2(x, y, KOL, KOL), Rect2(v * KOL, 0, KOL, KOL))

func _draw() -> void:
	var vloer := GANG_ONDER - 1   # bovenste vloerrij
	# maaiveld: gras met hier en daar een plantje of steen
	for k in kolommen:
		draw_texture_rect_region(GRAS, Rect2(k * KOL, 0, KOL, OPP), Rect2((k % 4) * KOL, 0, KOL, OPP))
		var h := _hash(k, 99)
		if h < 22 and k != ingang_kol and k <= max_kol + 1:
			draw_texture_rect_region(MAAIVELD, Rect2(k * KOL, 0, KOL, OPP), Rect2((h % 5) * KOL, 0, KOL, OPP))
	# twee rijen cellen
	for k in kolommen:
		_tegel(k * KOL, OPP, 0, k)
		_tegel(k * KOL, GANG_BOVEN, 1, k)
		# hier kun je graven: lichte stippels op de rand
		if not gang[k] and k <= max_kol and ((k > 0 and gang[k - 1]) or (k < kolommen - 1 and gang[k + 1])):
			var kx := k * KOL + (1 if k > 0 and gang[k - 1] else KOL - 2)
			for y in range(GANG_BOVEN + 3, GANG_BOVEN + KOL - 2, 3):
				draw_rect(Rect2(kx, y, 1, 1), Color("#c9a27a"))
	# ingang: poortje op de grasrand boven de schacht
	draw_texture(INGANG, Vector2(ingang_kol * KOL - 2, OPP - 14 + 4))
	# versiering op vaste plekken in de gang (stut tegen het plafond, iets op de vloer); achter de figuren
	for k in range(ingang_kol + 1, schat_kol - 1):
		var h := _hash(k, 7)
		if vallen.has(k):
			continue
		if h < 14:
			draw_texture_rect_region(DECO, Rect2(k * KOL, GANG_BOVEN, KOL, KOL), Rect2(7 * KOL, 0, KOL, KOL))   # stut
		elif h < 30:
			var soorten := [0, 1, 2, 4, 5]   # paddenstoel, lichtzwam, ton, schedel, kristal
			draw_texture_rect_region(DECO, Rect2(k * KOL, vloer - 15, KOL, KOL), Rect2(soorten[h % 5] * KOL, 0, KOL, KOL))
		elif h < 36 and not boven[k]:
			draw_texture_rect_region(DECO, Rect2(k * KOL, GANG_BOVEN, KOL, KOL), Rect2(6 * KOL, 0, KOL, KOL))   # spinrag
	# vallen: stekelput dicht, en even open na een klap
	for k in vallen:
		var f := 2 if put_open.has(k) else 0
		draw_texture_rect_region(PUT, Rect2(k * KOL, vloer - 7, KOL, 8), Rect2(f * KOL, 0, KOL, 8))
	# fakkels met gloed: bij de ingang en in de schatkamer
	var fk := [ingang_kol + 1, schat_kol - 1]
	var lamp := Color(1, 0.75, 0.45, 0.35)
	for k in fk:
		if k <= ingang_kol or k >= kolommen:
			continue
		var fx: float = k * KOL + 4
		draw_texture_rect_region(GLOED, Rect2(fx + 4 - 20, GANG_BOVEN + 4 - 20, 40, 40), Rect2(0, 0, 52, 52), lamp)
		draw_texture_rect_region(FAKKEL, Rect2(fx, GANG_BOVEN + 1, 8, 12), Rect2((anim % 4) * 8, 0, 8, 12))
	# schatkamer: vaandel aan het plafond en de schat op de vloer
	if boven[schat_kol]:
		draw_texture_rect_region(DECO, Rect2(schat_kol * KOL, OPP + 1, KOL, KOL), Rect2(8 * KOL, 0, KOL, KOL))
	var sf := (anim / 2) % 4
	draw_texture_rect_region(SCHAT, Rect2(schat_kol * KOL - 4, vloer - 15, 24, 16), Rect2(sf * 24, 0, 24, 16))
	# vliegende muntjes: een boogje van de val naar de schat, 2 bij 2 spelpixels met een donkere rand
	var doel := schat_kol * KOL + KOL / 2.0
	for m in munten:
		if m.t < 0.0:
			continue
		var f: float = m.t / MUNT_S
		var x: float = lerpf(m.van, doel, f)
		var y: float = vloer - 6 - sin(f * PI) * 12
		draw_rect(Rect2(x - 1, y - 1, 3, 3), Color("#7a4a12"))
		draw_rect(Rect2(x - 1, y - 1, 2, 2), Color("#f2c14e"))
