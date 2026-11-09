extends Node2D
# Het hol (Olaf). Een raster van kolommen van 16 spelpixels breed. Rij 0 is de gang onder de grond.
# Het hol groeit in de breedte (de strook is maar 40 spelpixels hoog bij 120 px). Rij 1 (dieper) komt later.
# Afspraak met Bram (platformen/steam/taken.md): alleen deze functies en signalen gebruiken.

signal gegraven(cel: Vector2i)

const KOL := 16          # breedte van een kolom in spelpixels
const H := 40            # hoogte van de strook in spelpixels
const GANG_BOVEN := 18   # bovenkant van de gang
const GANG_ONDER := 36   # vloer van de gang

const C_LUCHT_GRAS := Color("#6f9e3c")
const C_GRAS_DONKER := Color("#4f7a2a")
const C_AARDE := Color("#6b4428")
const C_AARDE_LICHT := Color("#80553a")
const C_AARDE_DONKER := Color("#4d2f1c")
const C_GANG := Color("#2b1a12")
const C_GANG_VLOER := Color("#3d271a")
const C_GOUD := Color("#f2c14e")
const C_GOUD_DONKER := Color("#b8862b")
const C_STEKEL := Color("#d9d4c7")
const C_STEKEL_DONKER := Color("#8a857a")

var kolommen := 0
var gang: Array[bool] = []
var vallen := {}          # kolom -> soort ("stekelput")
var ingang_kol := 2
var schat_kol := 12
var goud := 0             # buit van gevallen helden; nooit iets kwijt als je weg bent

func maak(breedte_spelpixels: int) -> void:
	kolommen = int(ceil(breedte_spelpixels / float(KOL)))
	gang.resize(kolommen)
	for i in kolommen:
		gang[i] = i >= ingang_kol and i <= schat_kol
	vallen[7] = "stekelput"
	queue_redraw()

# ---- afspraak met de systemen ----
func is_gang(cel: Vector2i) -> bool:
	return cel.y == 0 and cel.x >= 0 and cel.x < kolommen and gang[cel.x]

func cel_naar_pos(cel: Vector2i) -> Vector2:
	# midden van de vloer van die cel, in spelpixels
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

# ---- spelen (klikken komen van de strook, in spelpixels) ----
func klik(pos: Vector2) -> String:
	var k := pos_naar_cel(pos).x
	if not gang[k]:
		# alleen graven naast een bestaande gang; de schat verhuist mee naar het einde
		if (k > 0 and gang[k - 1]) or (k < kolommen - 1 and gang[k + 1]):
			gang[k] = true
			if k > schat_kol:
				schat_kol = k
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

func _draw() -> void:
	var w := kolommen * KOL
	# aarde met korrels
	draw_rect(Rect2(0, 0, w, H), C_AARDE)
	for y in range(6, H, 3):
		for x in range(0, w, 3):
			var h := _hash(x, y)
			if h < 9:
				draw_rect(Rect2(x, y, 1, 1), C_AARDE_LICHT)
			elif h < 15:
				draw_rect(Rect2(x, y, 1, 1), C_AARDE_DONKER)
	# gras bovenop met sprietjes
	draw_rect(Rect2(0, 0, w, 4), C_LUCHT_GRAS)
	draw_rect(Rect2(0, 4, w, 1), C_GRAS_DONKER)
	for x in range(0, w, 2):
		if _hash(x, 1) < 30:
			draw_rect(Rect2(x, -1, 1, 1), C_LUCHT_GRAS)
	# gangen
	for k in kolommen:
		if gang[k]:
			draw_rect(Rect2(k * KOL, GANG_BOVEN, KOL, GANG_ONDER - GANG_BOVEN), C_GANG)
			draw_rect(Rect2(k * KOL, GANG_ONDER, KOL, 2), C_GANG_VLOER)
		elif (k > 0 and gang[k - 1]) or (k < kolommen - 1 and gang[k + 1]):
			# hier kun je graven: gestippelde rand
			for y in range(GANG_BOVEN, GANG_ONDER, 4):
				draw_rect(Rect2(k * KOL + 1, y, 1, 2), C_AARDE_LICHT)
				draw_rect(Rect2(k * KOL + KOL - 2, y, 1, 2), C_AARDE_LICHT)
	# ingang: schacht van het gras naar de gang
	draw_rect(Rect2(ingang_kol * KOL + 3, 0, KOL - 6, GANG_BOVEN), C_GANG)
	draw_rect(Rect2(ingang_kol * KOL + 2, 0, 1, GANG_BOVEN), C_AARDE_DONKER)
	draw_rect(Rect2(ingang_kol * KOL + KOL - 3, 0, 1, GANG_BOVEN), C_AARDE_DONKER)
	# vallen
	for k in vallen:
		var x0: int = k * KOL
		draw_rect(Rect2(x0 + 1, GANG_ONDER - 1, KOL - 2, 3), C_GANG_VLOER.darkened(0.4))
		for s in range(x0 + 2, x0 + KOL - 2, 3):
			draw_colored_polygon(PackedVector2Array([Vector2(s, GANG_ONDER), Vector2(s + 1, GANG_ONDER - 4), Vector2(s + 2, GANG_ONDER)]), C_STEKEL)
			draw_rect(Rect2(s, GANG_ONDER - 1, 2, 1), C_STEKEL_DONKER)
	# schat
	var sx := schat_kol * KOL
	draw_colored_polygon(PackedVector2Array([Vector2(sx + 1, GANG_ONDER), Vector2(sx + 8, GANG_ONDER - 9), Vector2(sx + 15, GANG_ONDER)]), C_GOUD_DONKER)
	draw_colored_polygon(PackedVector2Array([Vector2(sx + 3, GANG_ONDER), Vector2(sx + 8, GANG_ONDER - 7), Vector2(sx + 13, GANG_ONDER)]), C_GOUD)
	draw_rect(Rect2(sx + 6, GANG_ONDER - 5, 1, 1), Color.WHITE)
