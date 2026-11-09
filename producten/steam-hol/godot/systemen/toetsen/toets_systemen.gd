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
	ok(k4.volle_naam("Mara") == "Mara the Hoard-Toucher", "bijnaam na de schat: " + k4.volle_naam("Mara"))
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
	# toets 3 van Sanne: naamgenoot met wrok, laatste 4 overslaan, terugkomer noemt waarom, hoedregels
	var k5 = K.new()
	k5.binnen("Kees")
	k5.gevallen("Kees", "Gloop the Slime", 6)
	var ik: Dictionary = k5.binnen(k5.vrije_naam("Kees"))
	ok(ik["naam"] == "Kees II" and ik["wrok"] == "Gloop the Slime", "Kees II komt met een wrok tegen Gloop (%s)" % ik["wrok"])
	ok(k5.laatste_soort == "naamgenoot_hoed" and k5.laatste().begins_with("Kees II"), "naamgenoot-regel hoed: " + k5.laatste())
	k5.binnen("Joep")
	k5.gevallen("Joep", "the Spike Pit", 6)
	var ij: Dictionary = k5.binnen("Joep II")
	ok(ij["wrok"] == "" and k5.laatste_soort == "naamgenoot", "naamgenoot van een put-held: geen wrok (%s)" % k5.laatste())
	k5.gevallen("Kees II", "Gloop the Slime", 6)
	var ik3: Dictionary = k5.binnen("Kees III")
	ok(ik3["wrok"] == "Gloop the Slime", "Kees III na Kees II door Gloop: ook een wrok")
	var k6 = K.new()
	var laatst: Array[String] = []
	var herhaald := 0
	for z in 200:
		k6.binnen("Held%d" % z)
		var rg: String = k6.laatste().replace("Held%d" % z, "X")
		if laatst.has(rg):
			herhaald += 1
		laatst.append(rg)
		if laatst.size() > 4:
			laatst.pop_front()
	ok(herhaald == 0, "binnenkomst: niet een van de laatste 4 regels opnieuw (%d keer)" % herhaald)
	var zonder_waarom := 0
	for z in 100:
		var nm := "Terug%d" % z
		k6.binnen(nm)
		k6.gevlucht(nm, "Gloop the Slime" if z % 2 == 0 else "the Spike Pit")
		k6.binnen(nm)
		var rg: String = k6.laatste()
		if not (rg.contains("Gloop") or rg.contains("Spike Pit") or rg.contains("Spooked")):
			zonder_waarom += 1
	ok(zonder_waarom == 0, "terugkomer noemt altijd wrok of bijnaam (%d zonder)" % zonder_waarom)
	var k7 = K.new()
	ok(k7.hoed("Kees", "Gloop the Slime", 1) == "Gloop wears Kees's hat now.", "eerste hoed: " + k7.laatste())
	ok(k7.hoed("Pim", "Gloop the Slime", 25) == "Gloop is now known as the Hatted.", "25 hoeden: " + k7.laatste())
	ok(k7.hoed("Pim", "Gloop the Slime", 0) == "", "aartsvijand naar de wand: geen hoedregel")
	var vaak := 0
	for z in 400:
		if k7.hoed("Held%d" % z, "Gloop the Slime", 2 + z % 20) != "":
			vaak += 1
	ok(vaak > 60 and vaak < 140, "hoedregel hooguit een op de vier (%d van 400)" % vaak)
	var te_lang2 := 0
	for regel in k5.regels + k6.regels + k7.regels:
		if regel.length() > 42:
			te_lang2 += 1
	ok(te_lang2 == 0, "nieuwe regels hooguit 42 tekens (%d te lang)" % te_lang2)

	print("[hol-toets] klaar: %d FOUT" % fout)
	quit(1 if fout > 0 else 0)
