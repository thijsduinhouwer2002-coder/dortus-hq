extends SceneTree
# Toetsen voor kroniek en voortgang (Bram). Draaien: godot --headless --path <map met project.godot> -s systemen/toetsen/toets_systemen.gd
var fout := 0

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[hol-toets] OK ", wat)
	else:
		fout += 1
		print("[hol-toets] FOUT ", wat)

func _init() -> void:
	var K = load("res://systemen/kroniek.gd")
	var V = load("res://systemen/voortgang.gd")
	var k = K.new()
	var i1: Dictionary = k.binnen("Bram")
	ok(i1["bezoeken"] == 0 and i1["wrok"] == "", "eerste bezoek zonder wrok")
	ok(k.laatste() == "Bram enters the lair.", "regel binnenkomst: " + k.laatste())
	k.gevlucht("Bram", "the Spike Pit")
	ok(k.volle_naam("Bram") == "Bram the Spooked", "bijnaam na 1 keer vluchten: " + k.volle_naam("Bram"))
	var i2: Dictionary = k.binnen("Bram")
	ok(i2["bezoeken"] == 1 and i2["wrok"] == "the Spike Pit" and i2["littekens"] == 1, "terug met wrok en litteken")
	ok(k.laatste().contains("still furious at the Spike Pit"), "regel terugkomst: " + k.laatste())
	k.gevlucht("Bram", "Gloop the Slime")
	k.binnen("Bram")
	k.gevlucht("Bram", "")
	ok(k.volle_naam("Bram") == "Bram the Thrice-Fled", "drie keer gevlucht: " + k.volle_naam("Bram"))
	ok(k.held("Bram")["wrok"] == "Gloop the Slime", "wrok blijft bij vluchten zonder raak")
	k.binnen("Bram")
	k.gevallen("Bram", "Gloop the Slime", 7)
	ok(k.laatste().contains("Grudge settled"), "wrok vereffend: " + k.laatste())
	var k2 = K.new()
	k2.van_dict(JSON.parse_string(JSON.stringify(k.naar_dict())))
	ok(k2.volle_naam("Bram") == "Bram the Thrice-Fled" and k2.laatste() == k.laatste(), "kroniek opslaan en laden via JSON")

	var t0 := 1_800_000_000
	var r: Dictionary = V.reken(t0, t0 + 3600, 1, 1, 42)
	ok(r["helden"] == 75 and r["goud"] >= r["helden"], "een uur weg: 75 helden, goud >= helden (%s)" % r["regel"])
	ok(r["gevallen"] + r["gevlucht"] == r["helden"], "gevallen + gevlucht = helden")
	var r2: Dictionary = V.reken(t0, t0 + 3600, 1, 1, 42)
	ok(r2["goud"] == r["goud"], "zelfde save, zelfde uitkomst")
	var terug: Dictionary = V.reken(t0, t0 - 86400, 3, 2, 42)
	ok(terug["helden"] == 0 and terug["goud"] == 0 and terug["teruggezet"] and terug["nieuwe_laatst"] == t0, "klok terug: niets kwijt, tijd gaat niet achteruit")
	var week: Dictionary = V.reken(t0, t0 + 7 * 86400, 1, 1, 42)
	var nacht: Dictionary = V.reken(t0, t0 + 12 * 3600, 1, 1, 42)
	ok(week["helden"] == nacht["helden"] and week["goud"] == nacht["goud"], "plafond 12 uur: week = nacht")
	ok(week["goud"] > 0, "na lang weg altijd winst, nooit verlies")
	var stil: Dictionary = V.reken(t0, t0 + 10, 0, 0, 1)
	ok(stil["regel"] == "All quiet while you were away.", "korte afwezigheid: rustige regel")
	print("[hol-toets] klaar: %d FOUT" % fout)
	quit(1 if fout > 0 else 0)
