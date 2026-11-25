# Het Hol: het venster (Olaf 25 nov, issue #24; uit kern/strook.gd gehaald, regel: bestand onder ±400).
# Plaatsen, app-balk en systeemvak starten, invoer (klik, rechtsklik, hover), venstermeldingen, hoogte en stoppen.
# Alleen statische functies met de strook als eerste argument (`s`); de toestand blijft in strook.gd.
extends RefCounted

const BALK := preload("res://kern/balk.gd")
const KAARTJE := preload("res://kern/kaartje.gd")
const DEMO_EINDE := preload("res://kern/demo_einde.gd")

static func plaats(s, scherm: Rect2i) -> void:
	DisplayServer.window_set_size(Vector2i(scherm.size.x, s.hoogte))
	# met de app-balk is het bruikbare vlak al zonder onze strook: dan zet hol-balk.exe het venster op zijn plek
	var y: int = scherm.position.y + scherm.size.y - (0 if BALK.actief() else s.hoogte)
	DisplayServer.window_set_position(Vector2i(scherm.position.x, mini(y, scherm.position.y + scherm.size.y - s.hoogte)))
	icoon()
	s.get_tree().create_timer(1.0).timeout.connect(icoon)
	BALK.start(s)
	# crasht hol-balk.exe (of zet een virusscanner hem stop), dan opnieuw starten; anders blijft het hol onklikbaar
	var wacht := Timer.new()
	wacht.wait_time = 2.0
	wacht.process_mode = Node.PROCESS_MODE_ALWAYS
	wacht.timeout.connect(func(): BALK.bewaak(s))
	s.add_child(wacht)
	wacht.start()
	var vak := Node.new()
	vak.set_script(load("res://kern/systeemvak.gd"))
	s.add_child(vak)
	vak.zet(s)
	if s.proef_vak != "":
		_proef_vak(s, vak)

# De lagen boven het hol: tekst (kroniek en paneel) en klap (ster, "+9", "x3").
static func lagen(s, scherm: Rect2i) -> void:
	var tekst := Node2D.new()
	tekst.set_script(s.TEKST)
	tekst.breedte = scherm.size.x
	tekst.hoogte = s.hoogte
	tekst.schaal = s.schaal
	s.add_child(tekst)
	s.tekst = tekst
	var klap := Node2D.new()
	klap.set_script(load("res://kern/klap.gd"))
	klap.name = "Klap"
	klap.schaal = s.schaal
	klap.hol_pos = s.hol.position
	s.add_child(klap)
	s.klap = klap
	var geluid := Node.new()   # de geluidjes van Mila echt afspelen (kern/geluid.gd, Sanne 25 nov)
	geluid.set_script(load("res://kern/geluid.gd"))
	geluid.name = "Geluid"
	s.add_child(geluid)
	s.geluid = geluid

static func log_start(s, scherm: Rect2i, spel_h: int) -> void:
	s.log_regel("HOL start hoogte=%d schaal=%d spelpixels=%dx%d venster=%s pos=%s held=%s" % [s.hoogte, s.schaal,
		int(scherm.size.x / s.schaal), spel_h, DisplayServer.window_get_size(), DisplayServer.window_get_position(),
		s.held_script.resource_path])
	# Olaf 15 nov: het zaad in de log, zodat een goede winkelopname (bijvoorbeeld met de dief) na te spelen is met zaad=<n>.
	s.log_regel("HOL zaad %d" % s.rng.seed)
	s.log_regel("HOL balk %s" % ("aan" if BALK.actief() else "uit"))

# vak=pauze|geluid|stop: na 6 s die regel kiezen alsof hij in het menu van het systeemvak is aangeklikt (toets).
static func _proef_vak(s, vak) -> void:
	await s.get_tree().create_timer(6.0, true).timeout
	match s.proef_vak:
		"pauze":
			vak.kies(vak.PAUZE)
			await s.get_tree().create_timer(3.0, true).timeout
			vak.kies(vak.PAUZE)
		"geluid":
			vak.kies(vak.GELUID)
			await s.get_tree().create_timer(2.0, true).timeout
			vak.kies(vak.GELUID)
		"stop":
			vak.kies(vak.STOP)

static func invoer(s, event: InputEvent) -> void:
	var hol = s.hol
	if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		if KAARTJE.klik(s, event.position):
			s.log_regel("HOL klik op %s: kaartje" % event.position)
			return
		if DEMO_EINDE.weiger(s, "klik in het hol"):
			return
		var p: Vector2 = (event.position - hol.position) / s.schaal
		var wat: String = hol.klik(p)
		if wat != "" and s.slijm != null:
			s.slijm.werk_berg_grens()   # put gebouwd of weg, of gegraven: linkergrens van de hoedenberg (Bram 17 nov)
		s.log_regel("HOL klik op %s: %s" % [event.position, wat if wat != "" else "niets"])
	elif event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_RIGHT:
		# rechtsklik: het menu van het systeemvak (Pause, Sound, Height, Quit); vroeger alleen de volgende hoogte
		var vak = s.get_node_or_null("Systeemvak")
		if vak:
			vak.open_bij_muis()
	var holbord = s.holbord
	if event is InputEventMouseMotion and holbord != null and holbord.actief():
		var pb: Vector2 = (event.position - hol.position) / s.schaal
		var op_bord: bool = holbord.vlak().has_point(pb)
		if op_bord != holbord.hover:
			holbord.hover = op_bord
			if op_bord:
				s.log_regel("HOL hover bordje: %s" % holbord.hover_tekst())
	if event is InputEventMouseMotion and not s.tekst.hover:
		s.tekst.hover = true
		s.tekst.queue_redraw()
		s._muis_vlak(true)

static func melding(s, what: int) -> void:
	if what == Node.NOTIFICATION_WM_MOUSE_EXIT and s.tekst:
		if s.holbord != null:
			s.holbord.hover = false
		s.tekst.hover = false
		s.tekst.queue_redraw()
		s._muis_vlak(s.kaart_soort != "")   # een open kaartje blijft de muis vangen
	elif what == Node.NOTIFICATION_WM_CLOSE_REQUEST:
		KAARTJE.dicht(s)   # een wachtende koopregel komt eerst in de kroniek, dan bewaren (controleur kan-punt 1)
		s.bewaar()
		BALK.stop()   # strook teruggeven aan Windows

# Andere hoogte: bewaar spel en instelling, dan de strook opnieuw opbouwen (schaal en venster hangen ervan af).
# De app-balk blijft draaien en krijgt in plaats() de nieuwe hoogte (kern/balk.gd start).
static func zet_hoogte(s, h: int) -> void:
	s.log_regel("HOL hoogte %d -> %d" % [s.hoogte, h])
	KAARTJE.dicht(s)
	s.bewaar()
	bewaar_instelling(s, "hoogte", h)
	s.get_tree().reload_current_scene()

# instellingen.json (hoogte, stil) los van de save; een sleutel zetten laat de andere staan.
static func bewaar_instelling(s, sleutel: String, waarde) -> void:
	var inst = {}
	if FileAccess.file_exists(s.INSTELLING):
		inst = JSON.parse_string(FileAccess.get_file_as_string(s.INSTELLING))
		if not inst is Dictionary:
			inst = {}
	inst[sleutel] = waarde
	var f := FileAccess.open(s.INSTELLING, FileAccess.WRITE)
	if f:
		f.store_string(JSON.stringify(inst))
		f.close()

# Stoppen uit het systeemvak: zoals sluiten, dan echt weg.
static func stoppen(s) -> void:
	KAARTJE.dicht(s)
	s.bewaar()
	BALK.stop()
	s.log_regel("HOL einde via het systeemvak")
	s.get_tree().quit()

# Olaf 15 nov (Daan 05:50, run 43681846964): los gestart met --path toonde de taakbalk tot ±35 s een gewoon
# vensterpictogram in plaats van Gloop. Daarom het icoon nog een keer zetten zodra het venster zijn maat heeft, en na
# 1 s nog eens. Alleen op Windows; het geexporteerde spel heeft het icoon ook in de exe.
static func icoon() -> void:
	if OS.get_name() != "Windows":
		return
	const ICO := "res://kunst/icoon.ico"
	if FileAccess.file_exists(ICO):
		DisplayServer.set_native_icon(ICO)
