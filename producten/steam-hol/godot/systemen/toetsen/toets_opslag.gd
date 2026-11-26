extends SceneTree
# Toetsen: de save mag nooit stilletjes weg (Olaf 26 nov, issue #194). Draaien:
# godot --headless --path <map met project.godot> -s systemen/toetsen/toets_opslag.gd
# Werkt in een eigen map (user://toets_opslag/), de echte hol.json van de speler blijft onaangeraakt.
const VEILIG := preload("res://kern/veilig_bestand.gd")
const MAP := "user://toets_opslag"
const PAD := MAP + "/hol.json"
var fout := 0

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[hol-toets] OK ", wat)
	else:
		fout += 1
		print("[hol-toets] FOUT ", wat)

func _leeg() -> void:
	DirAccess.make_dir_recursive_absolute(MAP)
	for n in DirAccess.get_files_at(MAP):
		DirAccess.remove_absolute(MAP + "/" + n)

func _save(ronde: int) -> String:
	# zoals opslag.gd bewaart: goud en de hoeden op Gloops toren
	var hoeden := []
	for i in ronde:
		hoeden.append("hoed_%d" % i)
	return JSON.stringify({"versie": 3, "goud": 100 + ronde * 7, "slijm": {"hoeden": hoeden}, "kroniek": ["Ronde %d" % ronde]})

func _bestanden() -> Array:
	var a := Array(DirAccess.get_files_at(MAP))
	a.sort()
	return a

func _goud(d) -> int:
	return int(d.get("goud", -1)) if d is Dictionary else -1

func _hoeden(d) -> int:
	return (d.get("slijm", {}).get("hoeden", []) as Array).size() if d is Dictionary else -1

func _schrijf_rauw(pad: String, tekst: String) -> void:
	var f := FileAccess.open(pad, FileAccess.WRITE)
	f.store_string(tekst)
	f.close()

func _init() -> void:
	_leeg()
	# 1. tien bewaarrondes: precies hol.json en hol.vorige.json, geen .tmp
	var goed := true
	for r in range(1, 11):
		goed = VEILIG.schrijf(PAD, _save(r)) and goed
	ok(goed, "10 bewaarrondes lukten")
	ok(_bestanden() == ["hol.json", "hol.vorige.json"], "na 10 rondes alleen hol.json en hol.vorige.json (%s)" % str(_bestanden()))
	var l := VEILIG.lees(PAD)
	ok(_goud(l.data) == 170 and _hoeden(l.data) == 10 and l.bron == PAD, "hol.json is ronde 10 (goud %d, hoeden %d)" % [_goud(l.data), _hoeden(l.data)])
	ok(_goud(JSON.parse_string(FileAccess.get_file_as_string(VEILIG.vorige(PAD)))) == 163, "hol.vorige.json is ronde 9")

	# 2. half geschreven hol.json (pc uit midden in het schrijven, zoals vroeger met FileAccess.WRITE)
	var heel := _save(11)
	_schrijf_rauw(PAD, heel.substr(0, heel.length() / 2))
	l = VEILIG.lees(PAD)
	ok(_goud(l.data) == 163 and _hoeden(l.data) == 9, "half geschreven hol.json: hol uit hol.vorige.json terug (goud %d, hoeden %d)" % [_goud(l.data), _hoeden(l.data)])
	ok(String(l.bron).ends_with("hol.vorige.json"), "bron is hol.vorige.json (%s)" % String(l.bron).get_file())
	ok(FileAccess.file_exists(MAP + "/hol.kapot.json"), "hol.kapot.json bestaat nog")
	ok(FileAccess.get_file_as_string(MAP + "/hol.kapot.json") == heel.substr(0, heel.length() / 2), "hol.kapot.json is het halve bestand, niet overschreven")
	# de eerste bewaarronde daarna overschrijft niets: de goede vorige blijft tot er een nieuwe hol.json staat
	ok(VEILIG.schrijf(PAD, _save(12)), "bewaren na het kapotte bestand lukt")
	ok(_goud(JSON.parse_string(FileAccess.get_file_as_string(VEILIG.vorige(PAD)))) == 163, "hol.vorige.json is na die ronde nog ronde 9")
	ok(_goud(VEILIG.lees(PAD).data) == 184, "hol.json is ronde 12")
	ok(FileAccess.file_exists(MAP + "/hol.kapot.json"), "hol.kapot.json staat er na het bewaren nog")

	# 3. lege hol.json: weer terug uit de vorige, en de eerste kapotte wordt niet overschreven
	_schrijf_rauw(PAD, "")
	l = VEILIG.lees(PAD)
	ok(_goud(l.data) == 163 and _hoeden(l.data) == 9, "lege hol.json: hol uit hol.vorige.json terug (goud %d)" % _goud(l.data))
	var kapot := _bestanden().filter(func(n): return String(n).begins_with("hol.kapot"))
	ok(kapot.size() == 2, "twee kapotte bestanden naast elkaar, geen overschreven (%s)" % str(kapot))

	# 4. pc uit tussen de twee keer hernoemen: hol.json weg, vorige en een complete .tmp staan er
	_leeg()
	VEILIG.schrijf(PAD, _save(1))
	VEILIG.schrijf(PAD, _save(2))
	DirAccess.rename_absolute(PAD, VEILIG.vorige(PAD).replace("vorige", "x"))
	DirAccess.remove_absolute(VEILIG.vorige(PAD))
	DirAccess.rename_absolute(VEILIG.vorige(PAD).replace("vorige", "x"), VEILIG.vorige(PAD))
	_schrijf_rauw(VEILIG.tmp(PAD), _save(3))
	l = VEILIG.lees(PAD)
	ok(_goud(l.data) == 114, "zonder hol.json komt het hol uit hol.vorige.json (goud %d)" % _goud(l.data))
	ok(VEILIG.schrijf(PAD, _save(4)) and _bestanden() == ["hol.json", "hol.vorige.json"], "daarna bewaren ruimt de .tmp op (%s)" % str(_bestanden()))

	# 5. half geschreven .tmp naast een goede hol.json: de goede blijft gewoon
	_schrijf_rauw(VEILIG.tmp(PAD), "{\"versie\": 3, \"go")
	l = VEILIG.lees(PAD)
	ok(_goud(l.data) == 128 and l.bron == PAD, "halve .tmp raakt hol.json niet (goud %d)" % _goud(l.data))
	ok(VEILIG.schrijf(PAD, _save(5)) and _bestanden() == ["hol.json", "hol.vorige.json"], "bewaren overschrijft de halve .tmp en laat niets achter")

	# 6. een save van een oudere versie gaat opzij als hol.v2.json, nooit overschreven
	_schrijf_rauw(PAD, JSON.stringify({"versie": 2, "goud": 9}))
	var oud := VEILIG.zet_opzij(PAD, "v2")
	ok(oud.get_file() == "hol.v2.json" and not FileAccess.file_exists(PAD), "oudere versie bewaard als hol.v2.json")
	_schrijf_rauw(PAD, JSON.stringify({"versie": 2, "goud": 10}))
	var oud2 := VEILIG.zet_opzij(PAD, "v2")
	ok(oud2 != "" and oud2 != oud and _goud(JSON.parse_string(FileAccess.get_file_as_string(oud))) == 9, "tweede oude save naast de eerste (%s)" % oud2.get_file())

	# 7. een onleesbare hol.json schuift bij bewaren nooit door naar hol.vorige.json
	_leeg()
	VEILIG.schrijf(PAD, _save(1))
	VEILIG.schrijf(PAD, _save(2))
	_schrijf_rauw(PAD, "{kapot")
	ok(VEILIG.schrijf(PAD, _save(3)), "bewaren over een onleesbare hol.json lukt")
	ok(_goud(JSON.parse_string(FileAccess.get_file_as_string(VEILIG.vorige(PAD)))) == 107, "hol.vorige.json is nog de goede ronde 1, niet het kapotte bestand")
	ok(FileAccess.file_exists(MAP + "/hol.kapot.json"), "het onleesbare bestand staat als hol.kapot.json")

	_leeg()
	print("[hol-toets] klaar: %d FOUT" % fout)
	quit(1 if fout > 0 else 0)
