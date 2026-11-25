# Het Hol: icoon in het systeemvak met een menu (Olaf, 25 nov 2026, issue #24). Er is geen taakbalkknop meer
# (kern/balk.gd), dus hier zet je het spel stil, het geluid uit, de hoogte, en stop je het.
# Naar autoloads/system_tray.gd r. 14 tot 57 van Desktop Truck Simulator (MIT,
# https://github.com/hubacekjakub/Godot-DesktopTruckSimulator): StatusIndicator met een eigen PopupMenu.
extends Node

const PAUZE := 1
const GELUID := 2
const STOP := 3
const HOOGTE := 10   # 10 + index in strook.HOOGTES

var s   # de strook

func zet(strook) -> void:
	s = strook
	name = "Systeemvak"
	process_mode = Node.PROCESS_MODE_ALWAYS
	var menu := PopupMenu.new()
	menu.name = "Menu"
	menu.add_check_item("Pause", PAUZE)
	menu.add_check_item("Sound", GELUID)
	menu.add_separator()
	for i in s.HOOGTES.size():
		menu.add_radio_check_item("Height %d px" % s.HOOGTES[i], HOOGTE + i)
	menu.add_separator()
	menu.add_item("Quit", STOP)
	menu.id_pressed.connect(kies)
	add_child(menu)
	_vink(menu)
	if not DisplayServer.has_feature(DisplayServer.FEATURE_STATUS_INDICATOR):
		return
	var vak := StatusIndicator.new()
	vak.name = "Icoon"
	vak.tooltip = "Hats of the Fallen"
	var png := "res://kunst/icoon.png"
	if ResourceLoader.exists(png):
		vak.icon = load(png)
	vak.menu = NodePath("../Menu")   # vóór add_child: StatusIndicator koppelt het menu bij het binnenkomen
	add_child(vak)

func _vink(menu: PopupMenu) -> void:
	menu.set_item_checked(menu.get_item_index(PAUZE), s.get_tree().paused)
	menu.set_item_checked(menu.get_item_index(GELUID), not AudioServer.is_bus_mute(0))
	for i in s.HOOGTES.size():
		menu.set_item_checked(menu.get_item_index(HOOGTE + i), s.HOOGTES[i] == s.hoogte)
	var vak := get_node_or_null("Icoon")
	if vak:
		vak.tooltip = "Hats of the Fallen (paused)" if s.get_tree().paused else "Hats of the Fallen"

func kies(id: int) -> void:
	if id == PAUZE:
		s.get_tree().paused = not s.get_tree().paused
		s.log_regel("HOL vak pauze %s" % ("aan" if s.get_tree().paused else "uit"))
	elif id == GELUID:
		var stil := not AudioServer.is_bus_mute(0)
		AudioServer.set_bus_mute(0, stil)
		s.bewaar_instelling("stil", stil)
		s.log_regel("HOL vak geluid %s" % ("uit" if stil else "aan"))
	elif id == STOP:
		s.log_regel("HOL vak stoppen")
		s.stoppen()
		return
	elif id >= HOOGTE and id < HOOGTE + s.HOOGTES.size():
		s.get_tree().paused = false
		s.zet_hoogte(s.HOOGTES[id - HOOGTE])
		return
	_vink(get_node("Menu"))
