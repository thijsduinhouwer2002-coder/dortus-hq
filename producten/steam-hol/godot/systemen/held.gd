extends Node2D
# Held (Bram). Vervangt de stand-in van Olaf; de kern pakt dit bestand vanzelf als het bestaat.
# Afspraak (platformen/steam/taken.md): start(hol, info) en signaal klaar(held, uitkomst, info).
# Gebruikt van het hol alleen: cel_naar_pos, pos_naar_cel, ingang, schat, val_op (en bewoners onder Hol/Wezens).
#
# Wat hij doet (features.md van Sanne, balans.md):
# - komt binnen bij de ingang en loopt naar zijn doel. Een held met een wrok loopt EERST naar zijn vijand
#   (de val of de bewoner bij naam), niet naar de schat.
# - bij elke verdediging op zijn pad (een val of een bewoner) gooit hij één keer: valt hij, dan laat hij goud achter.
#   Kans: slijm 30%, stekelput 22% (balans.md). Tegen zijn eigen vijand is hij roekeloos: +10 procentpunt.
# - valt hij niet, dan is hij geraakt: hij krijgt een wrok tegen wat hem raakte. Een bewoner die verliest gaat niet dood,
#   die is even plat (plat()).
# - karakter: "hebzuchtig" loopt door tot de schat (vlucht pas na twee klappen); "schijterig" draait na een klap meestal om.
# - haalt hij de schat, dan pakt hij NIETS (geen straf): hij raakt hem aan, krijgt de bijnaam Hoard-Toucher en rent weg.
#   Een Hoard-Toucher komt brutaler terug: iets vaker vluchten, nooit iets van jou kwijt.
# - info["moet_vallen"] = true: hij valt bij de eerste verdediging (de eerste held van een nieuw spel, balans.md).
#
# Terug in info (voor strook.gd en kroniek.gd): "wat" (korte Engelse zin), "laatst_geraakt", "hoard_toucher",
# "trek", "gezien_vijand". Uitkomst: "gevallen" of "ontsnapt".

signal klaar(held, uitkomst: String, info: Dictionary)

const LIJF := preload("res://kunst/held_lijf.png")
const HOEDEN := preload("res://kunst/held_hoeden.png")
const WAPENS := preload("res://kunst/held_wapens.png")

const VLOER := 36            # vloer van de gang in spelpixels (hol.gd GANG_ONDER)
const SNEL := 11.0           # spelpixels per seconde
const KANS := {"slijm": 0.30, "stekelput": 0.22}
const KANS_ANDERS := 0.25
const ROEKELOOS := 0.10      # extra kans om te vallen tegen zijn eigen vijand
const BRUTAAL := 0.8         # Hoard-Toucher: kans om te vallen x 0,8
const NAAM_PUT := "the Spike Pit"

var hol
var info := {}
var trek := "hebzuchtig"
var staat := "afdalen"       # afdalen, lopen, vluchten, klimmen, vallen
var doel_kol := 0
var vijand_kol := -1         # kolom van zijn vijand, -1 als hij er geen (meer) heeft
var klappen := 0
var t := 0.0
var geraakt_tot := 0.0
var val_t := 0.0
var gezien := {}             # kolommen waar hij al gegooid heeft
var rng := RandomNumberGenerator.new()
var verdedigingen := 0       # hoeveel keer hij al gooide (voor moet_vallen)

func is_held() -> bool:
	return true

func start(h, i: Dictionary) -> void:
	hol = h
	info = i
	texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	var naam: String = String(info.get("naam", "Hero"))
	rng.seed = int(info.get("zaad", hash([naam, int(info.get("bezoeken", 0)), Time.get_ticks_usec()])))
	trek = String(info.get("trek", ""))
	if trek == "":
		trek = "schijterig" if (hash(naam) & 1) == 1 else "hebzuchtig"
		info["trek"] = trek
	var p: Vector2 = hol.cel_naar_pos(hol.ingang())
	position = Vector2(p.x, 2)
	_kies_doel()

# Waar loopt hij heen? Vijand eerst, anders de schat.
func _kies_doel() -> void:
	vijand_kol = _zoek_vijand(String(info.get("wrok", "")))
	doel_kol = vijand_kol if vijand_kol >= 0 else hol.schat().x
	info["gezien_vijand"] = false

func _zoek_vijand(wrok: String) -> int:
	if wrok == "" or wrok == "your Hoard":
		return -1
	var start_kol: int = hol.ingang().x
	var eind: int = hol.schat().x
	for k in range(start_kol, eind + 1):
		var cel := Vector2i(k, 0)
		if wrok == NAAM_PUT and hol.val_op(cel) != "":
			return k
		var b = _bewoner_op(k)
		if b != null and b.naam() == wrok:
			return k
	return -1

func _bewoner_op(k: int):
	if get_parent() == null:
		return null
	for w in get_parent().get_children():
		if w != self and w.has_method("is_bewoner") and hol.pos_naar_cel(w.position).x == k:
			if w.has_method("kan_vechten") and not w.kan_vechten():
				continue   # even plat: hij loopt er gewoon langs
			return w
	return null

func _process(delta: float) -> void:
	stap(delta)

# Los van _process zodat de toetsen hem met de hand kunnen laten lopen.
func stap(delta: float) -> void:
	t += delta
	match staat:
		"afdalen":
			position.y = move_toward(position.y, VLOER, SNEL * delta)
			if position.y >= VLOER:
				staat = "lopen"
		"lopen":
			if vijand_kol < 0:
				doel_kol = hol.schat().x   # de schat schuift mee als je graaft
			var doel: Vector2 = hol.cel_naar_pos(Vector2i(doel_kol, 0))
			position.x = move_toward(position.x, doel.x, SNEL * (1.25 if trek == "hebzuchtig" else 1.0) * delta)
			_onderweg()
			if staat == "lopen" and absf(position.x - doel.x) < 0.5:
				_aangekomen()
		"vluchten":
			var terug: Vector2 = hol.cel_naar_pos(hol.ingang())
			position.x = move_toward(position.x, terug.x, SNEL * 1.5 * delta)
			if absf(position.x - terug.x) < 0.5:
				staat = "klimmen"
		"klimmen":
			position.y = move_toward(position.y, -4, SNEL * delta)
			if position.y <= -4:
				staat = "weg"
				klaar.emit(self, "ontsnapt", info)
				queue_free()
		"vallen":
			val_t += delta
			if val_t >= 1.0:
				staat = "weg"
				klaar.emit(self, "gevallen", info)
				queue_free()
	queue_redraw()

func _aangekomen() -> void:
	if doel_kol == vijand_kol:
		# zijn vijand stond er niet meer (weggehaald) of hij overleefde het duel: door naar de schat
		vijand_kol = -1
		doel_kol = hol.schat().x
		return
	# bij de schat: aanraken, niets pakken, wegrennen
	info["hoard_toucher"] = true
	info["wat"] = "touched your hoard, took nothing and ran"
	staat = "vluchten"

func _onderweg() -> void:
	var cel: Vector2i = hol.pos_naar_cel(position)
	if gezien.has(cel.x):
		return
	var soort: String = hol.val_op(cel)
	var b = _bewoner_op(cel.x)
	if soort == "" and b == null:
		return
	gezien[cel.x] = true
	if soort != "":
		b = null   # val en bewoner in dezelfde kolom: hij vecht tegen de val
	var naam_vijand: String = NAAM_PUT if soort != "" else b.naam()
	var kans: float = KANS.get(soort if soort != "" else String(b.get("soort") if "soort" in b else "slijm"), KANS_ANDERS)
	var is_vijand := vijand_kol >= 0 and cel.x == vijand_kol
	if is_vijand:
		info["gezien_vijand"] = true
		kans += ROEKELOOS
	if bool(info.get("hoard_toucher", false)):
		kans *= BRUTAAL
	verdedigingen += 1
	var valt := rng.randf() < kans
	if bool(info.get("moet_vallen", false)) and verdedigingen == 1:
		valt = true
	if valt:
		info["laatst_geraakt"] = naam_vijand
		info["wat"] = ("finally fell to " if is_vijand else "fell to ") + naam_vijand
		staat = "vallen"
		if b != null and b.has_method("raak"):
			b.raak()           # hap
		return
	# overleefd: geraakt, wrok tegen dit ding; een bewoner die verliest is even plat
	klappen += 1
	geraakt_tot = t + 0.5
	info["laatst_geraakt"] = naam_vijand
	if b != null and b.has_method("plat"):
		b.plat()
	if is_vijand:
		vijand_kol = -1
		doel_kol = hol.schat().x
	# schijterig draait na een klap meestal om (2 op 3), hebzuchtig pas na twee klappen
	if (trek == "schijterig" and rng.randf() < 0.67) or klappen >= 2:
		info["wat"] = "got hurt by %s and ran" % naam_vijand
		staat = "vluchten"

# ---- tekenen: Daans lijf + hoed + wapen (16 x 16, anker midden onder) ----
func _draw() -> void:
	if staat == "weg":
		return
	var frame := 0
	if staat in ["lopen", "vluchten"]:
		frame = int(t * 8) % 4
	var omlaag := 1 if frame in [1, 3] else 0
	var links := staat == "vluchten"
	var hoed := int(info.get("hoed_nr", absi(hash(String(info.get("naam", ""))))) % 4)
	var wapen := 2 if trek == "schijterig" else 0       # schijterig neemt een fakkel mee, hebzuchtig een zwaard
	var kleur := Color.WHITE
	if t < geraakt_tot and int(t * 10) % 2 == 0:
		kleur = Color(1, 0.55, 0.55)
	if staat == "vallen":
		# plat en weg: inzakken en vervagen
		kleur.a = 1.0 - val_t
		draw_set_transform(Vector2(0, 0), 0, Vector2(1.0 + val_t * 0.4, maxf(0.15, 1.0 - val_t)))
	elif links:
		draw_set_transform(Vector2.ZERO, 0, Vector2(-1, 1))
	draw_texture_rect_region(LIJF, Rect2(-8, -16, 16, 16), Rect2(frame * 16, 0, 16, 16), kleur)
	draw_texture_rect_region(HOEDEN, Rect2(-8, -16 + omlaag, 16, 16), Rect2(hoed * 16, 0, 16, 16), kleur)
	if staat != "vallen":
		draw_texture_rect_region(WAPENS, Rect2(-8, -16 + omlaag, 16, 16), Rect2(wapen * 16, 0, 16, 16), kleur)
	draw_set_transform(Vector2.ZERO, 0, Vector2.ONE)
	if staat == "vallen":
		return
	var bezoeken := int(info.get("bezoeken", 0))
	if bezoeken > 0:   # litteken tot Daan losse littekens tekent
		draw_rect(Rect2(-2 if not links else 1, -11 + omlaag, 1, 2), Color("#d2342c"))
	if bezoeken > 1:   # verband
		draw_rect(Rect2(-3, -6 + omlaag, 6, 1), Color("#efe6d2"))
	# wrok: boos teken boven zijn hoofd zolang hij op weg is naar zijn vijand
	if vijand_kol >= 0 and staat == "lopen":
		var c := Color("#e8402a")
		draw_rect(Rect2(-1, -21, 1, 1), c)
		draw_rect(Rect2(1, -21, 1, 1), c)
		draw_rect(Rect2(0, -20, 1, 1), c)
		draw_rect(Rect2(-1, -19, 1, 1), c)
		draw_rect(Rect2(1, -19, 1, 1), c)
	# aartsvijand (drie keer gevlucht): gouden sterretje
	if bezoeken >= 3:
		var g := Color("#f2c14e")
		draw_rect(Rect2(4, -21, 1, 3), g)
		draw_rect(Rect2(3, -20, 3, 1), g)
