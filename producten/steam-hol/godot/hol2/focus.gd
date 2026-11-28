# Olaf, 28 nov 2026 (issue #401, Daan #394 moet 2): de focus terug na de besturen-stand. Alleen op Windows.
# Het hulpje hol2/focus.exe (bron hol2/focus.c) zit in de .pck en wordt één keer naar user:// gekopieerd.
# neem(): vóór het hol de focus pakt, onthouden welk venster vooraan stond. terug(): dat venster weer vooraan zetten.
extends RefCounted

const EXE := "hol2-focus.exe"
static var vorig := "0"

static func _pad() -> String:
	var bron := "res://hol2/focus.exe"
	if not FileAccess.file_exists(bron):
		return ""
	var data := FileAccess.get_file_as_bytes(bron)
	var doel := ProjectSettings.globalize_path("user://" + EXE)
	if FileAccess.file_exists(doel) and FileAccess.get_file_as_bytes(doel) == data:
		return doel
	var f := FileAccess.open(doel, FileAccess.WRITE)
	if f == null:
		return ""
	f.store_buffer(data)
	f.close()
	return doel

static func _draai(args: PackedStringArray) -> String:
	if OS.get_name() != "Windows":
		return "niet op Windows"
	var pad := _pad()
	if pad == "":
		return "geen focus.exe"
	var uit: Array = []
	var code := OS.execute(pad, args, uit, true)
	return ("".join(uit)).strip_edges() + ("" if code == 0 else " (code %d)" % code)

static func neem() -> String:
	var r := _draai(PackedStringArray(["neem"]))
	vorig = r if r.is_valid_int() else "0"
	return r

static func terug() -> String:
	var ons := str(DisplayServer.window_get_native_handle(DisplayServer.WINDOW_HANDLE))
	return _draai(PackedStringArray(["terug", vorig, ons]))
