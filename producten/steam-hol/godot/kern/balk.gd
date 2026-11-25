# Het Hol: de app-balk op Windows (Olaf, 25 nov 2026, issue #24).
# Start hol-balk.exe (bron: producten/steam-hol/balk/hol_balk.c) naast het spel. Dat programma laat Windows een strook
# onderaan vrijhouden (gemaximaliseerde vensters eindigen boven het spel), haalt de taakbalkknop weg, verstopt het spel
# bij een film of spel op volledig scherm, en laat de muis door het spel heen behalve op het vlak dat wij sturen.
# Daardoor hoeft window_set_mouse_passthrough niet meer, en dat knipte op Windows ook het beeld weg (gras, hoeden).
# Lukt het niet (geen Windows, geen exe, balk=0), dan blijft alles zoals vroeger: kern/muisvlak.gd met passthrough.
#
# De toestand is statisch, zodat hij een reload_current_scene (andere hoogte) overleeft: dan alleen "h <hoogte>".
extends RefCounted

const EXE := "hol-balk.exe"

static var pijp: FileAccess = null
static var pid := 0
static var laatste_vlak := ""

static func actief() -> bool:
	return pijp != null and pid > 0 and OS.is_process_running(pid)

# Waar staat het programma? Startargument balk=<pad> (toetsen), naast de .exe van het spel, of anders uit het spel zelf
# (res://balk/hol-balk.exe zit in de .pck, export_presets.cfg) naar user:// gekopieerd. Zo werkt elke build vanzelf.
static func _pad(s) -> String:
	if s.balk_pad != "":
		return s.balk_pad
	var naast := OS.get_executable_path().get_base_dir().path_join(EXE)
	if FileAccess.file_exists(naast):
		return naast
	var bron := "res://balk/" + EXE
	if not FileAccess.file_exists(bron):
		return naast
	var data := FileAccess.get_file_as_bytes(bron)
	var doel := ProjectSettings.globalize_path("user://" + EXE)
	if FileAccess.file_exists(doel) and FileAccess.get_file_as_bytes(doel) == data:
		return doel
	var f := FileAccess.open(doel, FileAccess.WRITE)
	if f == null:
		return naast
	f.store_buffer(data)
	f.close()
	return doel

static func start(s) -> bool:
	if OS.get_name() != "Windows" or s.balk_pad == "0":
		return false
	if actief():
		_stuur("h %d" % s.hoogte)
		laatste_vlak = ""
		return true
	var pad := _pad(s)
	if not FileAccess.file_exists(pad):
		s.log_regel("HOL balk: geen %s, het venster blijft zonder app-balk" % pad)
		return false
	var hwnd := DisplayServer.window_get_native_handle(DisplayServer.WINDOW_HANDLE)
	var log_balk := ProjectSettings.globalize_path("user://logs/balk.log")
	DirAccess.make_dir_recursive_absolute(log_balk.get_base_dir())
	var uit := OS.execute_with_pipe(pad, PackedStringArray([str(hwnd), str(s.hoogte), log_balk]))
	if uit.is_empty():
		s.log_regel("HOL balk: starten mislukt (%s)" % pad)
		return false
	pijp = uit.stdio
	pid = int(uit.pid)
	laatste_vlak = ""
	s.log_regel("HOL balk gestart, pid %d, hoogte %d" % [pid, s.hoogte])
	return true

# Het vlak dat de muis vangt, als bovenkant per pixelkolom (kern/muisvlak.gd tops). Gelijke stukken samen.
static func vlak(tops: PackedInt32Array) -> void:
	if not actief():
		return
	var delen := PackedStringArray(["v"])
	var x0 := 0
	for x in range(1, tops.size() + 1):
		if x == tops.size() or tops[x] != tops[x0]:
			delen.append("%d %d %d" % [x0, x, tops[x0]])
			x0 = x
	var regel := " ".join(delen)
	if regel != laatste_vlak:
		laatste_vlak = regel
		_stuur(regel)

static func stop() -> void:
	if pijp != null:
		_stuur("q")
		pijp.close()
	pijp = null
	pid = 0

static func _stuur(regel: String) -> void:
	if pijp == null:
		return
	pijp.store_string(regel + "\n")
	pijp.flush()
