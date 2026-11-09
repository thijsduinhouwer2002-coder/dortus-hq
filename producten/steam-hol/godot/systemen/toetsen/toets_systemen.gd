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
	ok(k.laatste_soort.begins_with("binnen") and k.laatste().contains("Bram"), "regel binnenkomst: " + k.laatste())
	k.gevlucht("Bram", "the Spike Pit")
	ok(k.volle_naam("Bram") == "Bram the Spooked", "bijnaam na 1 keer vluchten: " + k.volle_naam("Bram"))
	var i2: Dictionary = k.binnen("Bram")
	ok(i2["bezoeken"] == 1 and i2["wrok"] == "the Spike Pit" and i2["littekens"] == 1, "terug met wrok en litteken")
	ok(k.laatste_soort == "terug" and k.laatste().contains("Bram"), "regel terugkomst: " + k.laatste())
	k.gevlucht("Bram", "Gloop the Slime")
	k.binnen("Bram")
	k.gevlucht("Bram", "")
	ok(k.volle_naam("Bram") == "Bram the Thrice-Fled", "drie keer gevlucht: " + k.volle_naam("Bram"))
	ok(k.held("Bram")["wrok"] == "Gloop the Slime", "wrok blijft bij vluchten zonder raak")
	k.binnen("Bram")
	k.gevallen("Bram", "Gloop the Slime", 7)
	ok(k.laatste_soort == "afgerekend" and k.laatste().ends_with(" +7"), "wrok vereffend: " + k.laatste())
	# regels van Sanne: hooguit 42 tekens, goud in dezelfde regel, niet twee keer dezelfde achter elkaar
	var k3 = K.new()
	var te_lang := 0
	var dubbel := 0
	var vorige := ""
	for z in 300:
		var nm: String = ["Kees", "Gerda", "Joost", "Fenna", "Lotte"][z % 5]
		k3.binnen(nm, "hebzuchtig" if z % 2 == 0 else "schijterig")
		var r_: String = k3.laatste()
		if z % 3 == 0:
			r_ = k3.gevlucht(nm, "Gloop the Slime")
		elif z % 3 == 1:
			r_ = k3.gevallen(nm, "the Spike Pit", 15)
		else:
			r_ = k3.schat(nm)
		for regel in k3.regels.slice(-2):
			if regel.length() > 42:
				te_lang += 1
		if r_ == vorige:
			dubbel += 1
		vorige = r_
	ok(te_lang == 0, "alle kroniekregels hooguit 42 tekens (%d te lang)" % te_lang)
	ok(dubbel == 0, "niet twee keer dezelfde regel achter elkaar")
	var k4 = K.new()
	k4.binnen("Kees")
	ok(k4.gevallen("Kees", "the Spike Pit", 7).ends_with(" +7") and not k4.laatste().contains("Gloop"), "val en goud in één regel, geen bewonersregel bij de put: " + k4.laatste())
	ok(k4.vrije_naam("Kees") == "Kees II", "gevallen naam komt terug als Kees II")
	k4.binnen("Kees II")
	ok(k4.laatste_soort == "naamgenoot" and k4.laatste().begins_with("Kees II"), "naamgenoot-regel: " + k4.laatste())
	k4.gevallen("Kees II", "Gloop the Slime", 6)
	k4.binnen("Kees III")
	k4.gevallen("Kees III", "Gloop the Slime", 6)
	ok(k4.vrije_naam("Kees") == "", "na Kees III een andere naam")
	k4.binnen("Mara")
	ok(k4.schat("Mara") != "" and k4.held("Mara")["hoard_toucher"] and k4.laatste_soort == "schat", "schat aangeraakt: Hoard-Toucher-regel: " + k4.laatste())
	ok(k4.pensioen("Mara").begins_with("Mara") and k4.held("Mara")["pensioen"], "pensioen-regel: " + k4.laatste())
	ok(k4.gevallen("Odo", "Gloop the Slime", 6).find("Gloop the Slime") < 0, "bewoner kort als Gloop, nooit Gloop the Slime")
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
	# verhaal terwijl je weg was: regels met namen, hooguit 42 tekens, zelfde save = zelfde verhaal
	var hd := {"Kees": {"gevlucht": 1, "wrok": "Gloop the Slime"}, "Mara": {"gevlucht": 3, "wrok": "the Spike Pit"}}
	var vu: Dictionary = V.reken(t0, t0 + 6 * 3600, 1, 1, 42)
	var vh: Array = V.verhaal(vu, hd, ["Gloop the Slime", "the Spike Pit"], 42)
	ok(vh.size() >= 2 and vh.size() <= 3, "verhaal: 2 tot 3 regels (%d)" % vh.size())
	ok(vh[0].begins_with("Kees"), "verhaal noemt wie er terug was: " + vh[0])
	var lang := 0
	for r_ in vh:
		print("[hol-toets]   ", r_)
		if r_.length() > 42:
			lang += 1
	ok(lang == 0, "alle regels hooguit 42 tekens")
	ok(V.verhaal(vu, hd, ["Gloop the Slime", "the Spike Pit"], 42) == vh, "zelfde save, zelfde verhaal")
	ok(V.verhaal(V.reken(t0, t0 + 10, 1, 1, 42), hd, [], 42).is_empty(), "niemand kwam: geen verhaal")
	var zonder: Array = V.verhaal(vu, {}, ["Gloop the Slime"], 42)
	ok(zonder.size() >= 1 and zonder[-1].contains("gold"), "zonder bekende helden toch een regel met goud: " + zonder[-1])
	# goud weg = goud in het spel (balans.md): 6 per val bij de start, meer met gangen en faam
	ok(V.goud_per_val(0, 0) == 6 and V.goud_per_val(6, 0) == 7 and V.goud_per_val(40, 0) == 12 and V.goud_per_val(40, 10) == 24, "goud per val volgt balans.md")
	var veel: Dictionary = V.reken(t0, t0 + 3600, 1, 1, 42, 30, 0)
	ok(veel["goud"] > r["goud"], "meer gangen, meer goud terwijl je weg bent (%d tegen %d)" % [veel["goud"], r["goud"]])
	var sterk: Dictionary = V.reken(t0, t0 + 3600, 1, 1, 42, 6, 20)
	ok(sterk["gevallen"] <= r["gevallen"] and sterk["goud"] > 0, "faam: helden sterker, nog steeds winst (%d tegen %d gevallen)" % [sterk["gevallen"], r["gevallen"]])
	print("[hol-toets] klaar: %d FOUT" % fout)
	quit(1 if fout > 0 else 0)
