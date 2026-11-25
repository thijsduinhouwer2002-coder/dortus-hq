# Het Hol: de lagen die in het hol hangen, in tekenvolgorde (Olaf 25 nov, uit kern/strook.gd gehaald; regel: bestand onder ±400).
# Volgorde telt: na het vaste beeld van het hol eerst klein leven en licht (#97), dan vleermuis en bordje, dan Wezens
# (helden en Gloop), zodat helden en Gloop fel en scherp boven het licht staan.
extends RefCounted

static func maak(s) -> void:
	if not "licht" in s.proef_uit3d:   # licht en klein leven (#97), vóór vleermuis en wezens; licht=uit via uit3d om te vergelijken
		load("res://systemen/leven.gd").maak_in(s.hol, s.proef_zaad)
		load("res://systemen/licht.gd").maak_in(s.hol)
	s.wezens = Node2D.new()
	s.wezens.name = "Wezens"
	# vleermuis (Bram 16 nov, Mila punt 4b) vóór Wezens: de helden lopen voor hem langs; zonder blad doet hij niets
	var vleermuis := Node2D.new()
	vleermuis.set_script(load("res://systemen/vleermuis.gd"))
	vleermuis.name = "Vleermuis"
	s.hol.add_child(vleermuis)
	# bordje met het hol-niveau (Mila 16 nov 16:20, plek Daan keus A), ook vóór Wezens; zonder blad doet het niets
	s.holbord = Node2D.new()
	s.holbord.set_script(load("res://systemen/holbord.gd"))
	s.holbord.name = "Holbord"
	s.hol.add_child(s.holbord)
	s.hol.add_child(s.wezens)
	vleermuis.zet(s.hol, s.wezens)
	s.holbord.zet(s, s.hol)
