extends SceneTree
# Proef vertaaltabel (Olaf, 16 nov): komt tekst uit kunst/tekst/tekst.csv via tr() letter voor letter terug?
# Draaien: godot --headless --path <godot-map> -s systemen/toetsen/toets_tekst.gd
var fout := 0

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[tekst-toets] OK ", wat)
	else:
		fout += 1
		print("[tekst-toets] FOUT ", wat)

func _init() -> void:
	TranslationServer.set_locale("en")
	var val: String = tr("PROEF_VAL").format({"naam": "Kees", "goud": 6})
	ok(val == "Kees fell to the Spike Pit. +6", "plekken {naam} en {goud}: " + val)
	ok(tr("PROEF_KOMMA") == "Page for the Knight. The pit got him, too.", "komma binnen aanhalingstekens: " + tr("PROEF_KOMMA"))
	ok(tr("PROEF_AANHAALTEKEN") == "Full game: \"keep\" this hole.", "dubbel aanhalingsteken: " + tr("PROEF_AANHAALTEKEN"))
	TranslationServer.set_locale("ja")
	ok(tr("PROEF_VAL") == "{naam} fell to the Spike Pit. +{goud}", "onbekende taal valt terug op Engels")
	ok(tr("BESTAAT_NIET") == "BESTAAT_NIET", "onbekende sleutel geeft de sleutel")
	print("[tekst-toets] klaar: ", fout, " FOUT")
	quit(1 if fout > 0 else 0)
