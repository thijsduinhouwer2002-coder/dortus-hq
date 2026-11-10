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
	ok(k.laatste_soort == "afgerekend_aarts" and k.laatste().ends_with(" +7") and not k.laatste().contains("wall"),
		"aartsvijand vereffend, eigen lijst (Sanne 21:50): " + k.laatste())
	k.binnen("Wim")
	k.gevlucht("Wim", "Gloop the Slime")
	k.binnen("Wim")
	k.gevallen("Wim", "Gloop the Slime", 5)
	ok(k.laatste_soort == "afgerekend_bewoner" and k.laatste().ends_with(" +5") and not k.laatste().contains("wall")
		and not k.laatste().contains("Nemesis"), "wrok vereffend, gewone held zonder wand of Nemesis: " + k.laatste())
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

	# hoeden terwijl je weg was (Mila: de toren groeit vanzelf terwijl je weg bent)
	var hw: Dictionary = V.reken(t0, t0 + 3 * 3600, 1, 1, 42)
	ok(int(hw.opgegeten) > 0 and int(hw.opgegeten) < int(hw.gevallen), "weg 3 uur: een deel van de gevallen helden gaf Gloop een hoed (%d van %d)" % [int(hw.opgegeten), int(hw.gevallen)])
	ok(int(V.reken(t0, t0 + 3 * 3600, 2, 0, 42).opgegeten) == 0, "zonder bewoners geen hoeden")
	ok(hw.goud == V.reken(t0, t0 + 3 * 3600, 1, 1, 42).goud and hw.opgegeten == V.reken(t0, t0 + 3 * 3600, 1, 1, 42).opgegeten, "hoeden en goud: zelfde save, zelfde uitkomst")
	var hv0: Array = V.verhaal(hw, {}, ["Gloop the Slime", "the Spike Pit"], 42)
	ok(not str(hv0).contains("hat"), "hoeden nog niet gegeven: het verhaal noemt ze niet " + str(hv0))
	var sl1 = load("res://systemen/slijm.gd").new()
	var sl2 = load("res://systemen/slijm.gd").new()
	var hw7 := hw.duplicate()
	hw7["opgegeten"] = 7
	var per: Array = V.geef_hoeden([sl1, sl2], hw7, 42)
	ok(per == [4, 3] and sl1.hoeden.size() == 4 and sl2.hoeden.size() == 3 and sl1.hap_van < 0.0 and hw7.hoeden_gegeven, "hoeden verdeeld over twee slijmen, zonder hap (%s)" % str(per))
	var hv: Array = V.verhaal(hw7, {}, ["Gloop the Slime", "the Spike Pit"], 42)
	ok(hv.size() >= 1 and hv.size() <= 3 and hv[0] == "Gloop got 7 new hats." and hv[-1].contains(" 7 hats."), "na geef_hoeden noemt het verhaal de hoeden: " + str(hv))
	var hw1 := hw.duplicate()
	hw1["opgegeten"] = 1
	V.geef_hoeden([sl1], hw1, 42)
	ok(V.verhaal(hw1, {}, ["Gloop the Slime"], 42)[0] == "Gloop got 1 new hat.", "enkelvoud: 1 new hat")
	sl1.free()
	sl2.free()

	# Sanne toets 5 punt 2: geen binnenkom-regel die in de laatste 10 regels van de kroniek al stond
	var k8 = K.new()
	var sjablonen: Array[String] = []
	var dubbel10 := 0
	for z in 300:
		var nm := "Held%d" % z
		k8.binnen(nm)
		var sj: String = k8.laatste().replace(nm, "{naam}")
		if k8.laatste_soort.begins_with("binnen") and sjablonen.slice(maxi(0, sjablonen.size() - 10)).has(sj):
			dubbel10 += 1
		sjablonen.append(sj)
		# zoals in het spel: elke held heeft ook een afloop-regel (vallen of vluchten)
		if z % 3 == 0:
			k8.gevallen(nm, "the Spike Pit", 6)
		else:
			k8.gevlucht(nm, "Gloop the Slime")
		sjablonen.append(k8.laatste().replace(nm, "{naam}"))
	ok(dubbel10 == 0, "binnenkomst: geen regel die in de laatste 10 al stond (%d keer)" % dubbel10)
	# demo-minuut: 7 binnenkom-regels op rij, alle 7 verschillend (eerst alle andere, dan pas een herhaling)
	var k10 = K.new()
	var zeven := {}
	for z in 7:
		k10.binnen("Demo%d" % z)
		zeven[k10.laatste().replace("Demo%d" % z, "{naam}")] = true
	ok(zeven.size() == 7, "7 helden op rij: 7 verschillende binnenkom-regels (%d)" % zeven.size())
	# Olaf 22:35: één voorraad; kern/strook.gd kan dezelfde soorten en de getal-vorm van kies() gebruiken
	var stem = load("res://systemen/kroniek_regels.gd").new()
	var mist: Array[String] = []
	for soort in ["binnen", "naamgenoot", "terug", "terug_bewoner", "terug_val", "aartsvijand", "val", "val_bewoner", "afgerekend",
			"afgerekend_aarts", "vlucht", "schat", "plat", "op", "hoed_eerste", "hoed", "hoed_klein", "hoed_bijnaam"]:
		if not stem.VOORRAAD.has(soort):
			mist.append(soort)
	ok(mist.is_empty(), "alle soorten van strook.gd staan in kroniek_regels.gd (mist: %s)" % str(mist))
	var rv: String = stem.kies("val", {"naam": "Bartholomew", "val": "the Spike Pit"}, 4)
	ok(rv != "" and rv.length() <= 38 and not rv.contains("+"), "kies met getal: ruimte voor ' +12', niets erachter (%s)" % rv)
	ok(stem.kies("plat", {"bewoner": "Gloop"}) == "Gloop is flat. Back soon.", "plat-regel uit dezelfde voorraad")
	ok(stem.kies("val_bewoner", {"naam": "Maximiliaan-Theodoor", "bewoner": "Gloop"}, 30) != "", "kies met getal geeft nooit leeg")
	var k9 = K.new()
	k9.binnen("Kees")
	k9.gevallen("Kees", "the Spike Pit", 6)
	k9.binnen("Kees II")
	ok(not k9.laatste().contains("II II") and not k9.laatste().contains("{") and k9.laatste().contains("Kees II"), "naamgenoot met {oud}: " + k9.laatste())
	# Sanne toets 6 punt 1: de wrok krijgt een afloop, met een eigen regel die de vijand noemt
	var k11 = K.new()
	k11.binnen("Bram")
	k11.gevlucht("Bram", "the Spike Pit")
	k11.binnen("Bram")
	k11.gevallen("Bram", "the Spike Pit", 9)
	var ra: String = k11.laatste()
	ok(k11.laatste_soort == "afgerekend_val" and ra.contains("The Spike Pit") and ra.ends_with(" +9") and ra.length() <= 42
		and not ra.contains("{"), "wrok tegen de put: eigen afloop-regel met hoofdletter: " + ra)
	var af_lang := 0
	for soort in ["afgerekend_val", "afgerekend_bewoner"]:
		for sj in stem.VOORRAAD[soort]:
			var vol: String = stem.vul(sj, {"naam": "Bram", "val": "the Spike Pit", "bewoner": "Gloop"}) + " +12"
			if vol.length() > 42 or vol.contains("{"):
				af_lang += 1
				print("  te lang of open: ", vol)
	ok(af_lang == 0, "afloop-regels met Bram en +12 passen in 42 tekens (%d niet)" % af_lang)
	ok(stem.kies("afgerekend_val", {"naam": "Bram", "val": ""}) == "", "afloop-regel met {Val} komt niet zonder val")
	ok(stem.kies("afgerekend_val", {"naam": "Bartholomew-Maximus", "val": "the Spike Pit"}, 4) != "", "getal-vorm: afloop-regel nooit leeg")
	# upgrades (Bram 10 nov, feature 5, balans.md): 45, 126, 353 (Sanne 01:50), drie per soort, volle prijs terug, opslaan
	var u = load("res://systemen/upgrades.gd").new()
	ok(u.kost("slijm") == 45 and u.kost("stekelput") == 45 and u.kost("draak") == -1, "eerste upgrade kost 45")
	ok(u.koop("slijm", 44) == -1 and u.niveau("slijm") == 0, "te weinig goud: niets gekocht")
	ok(u.koop("slijm", 100) == 55 and u.niveau("slijm") == 1 and u.kost("slijm") == 126, "kopen: 55 over, volgende kost 126")
	ok(u.koop("slijm", 126) == 0 and u.kost("slijm") == 353, "derde kost 353 (balans.md)")
	ok(u.koop("slijm", 353) == 0 and u.kost("slijm") == -1 and u.volgende("slijm").is_empty(), "na drie stappen is alles gekocht")
	ok(absf(u.kans_erbij("slijm") - 0.21) < 0.0001 and u.kans_erbij("stekelput") == 0.0, "+7 procentpunt per stap")
	ok(u.verkoop("slijm") == 353 and u.niveau("slijm") == 2, "weghalen geeft de volle prijs terug")
	var u2 = load("res://systemen/upgrades.gd").new()
	u2.van_dict(u.naar_dict())
	ok(u2.niveau("slijm") == 2 and absf(u2.plat_factor() * 60.0 - 40.0) < 0.01, "opslaan en laden, Bouncy Gloop 40 s")
	u2.van_dict({"slijm": 9, "stekelput": -3})
	ok(u2.niveau("slijm") == 3 and u2.niveau("stekelput") == 0, "kapotte save: niveaus tussen 0 en 3")
	var regels_ok := 0
	var u3 = load("res://systemen/upgrades.gd").new()
	for soort in ["slijm", "stekelput"]:
		for n in 3:
			var vg: Dictionary = u3.volgende(soort)
			u3.koop(soort, 1000)
			var kr: String = u3.koop_regel(soort)
			if kr.length() <= 42 and String(vg.naam).length() <= 22 and String(vg.uitleg).length() <= 34:
				regels_ok += 1
			else:
				print("  te lang: ", kr, " | ", vg)
	ok(regels_ok == 6, "namen, uitleg en kroniekregel passen (%d van 6)" % regels_ok)
	ok(u3.koop_regel("slijm") == "Gloop is now Royal Gloop." and u3.put_verborgen(), "regel: " + u3.koop_regel("slijm"))
	# voortgang telt upgrades mee; zonder upgrades precies als voorheen
	var vz: Dictionary = V.reken(t0, t0 + 3600, 1, 1, 42)
	var vn: Dictionary = V.reken(t0, t0 + 3600, 1, 1, 42, 6, 0, null)
	var u4 = load("res://systemen/upgrades.gd").new()
	u4.van_dict({"slijm": 3, "stekelput": 3})
	var vm: Dictionary = V.reken(t0, t0 + 6 * 3600, 1, 1, 42, 6, 0, u4)
	var vz6: Dictionary = V.reken(t0, t0 + 6 * 3600, 1, 1, 42)
	ok(vz.goud == vn.goud and vz.gevallen == vn.gevallen, "voortgang zonder upgrades gelijk aan voorheen")
	ok(vm.gevallen >= vz6.gevallen and vm.goud >= vz6.goud, "voortgang met upgrades: minstens zoveel gevallen (%d tegen %d)" % [vm.gevallen, vz6.gevallen])

	# heldensoorten in de kroniek (Bram 10 nov)
	var ks = load("res://systemen/kroniek.gd").new()
	var ib: Dictionary = ks.binnen("Odo", "hebzuchtig", "ridder")
	ok(String(ib.soort_held) == "ridder" and ks.laatste().contains("Odo"), "ridder komt binnen met eigen regel: " + ks.laatste())
	ks.gevlucht("Odo", "the Spike Pit")
	var ib2: Dictionary = ks.binnen("Odo")
	ok(String(ib2.soort_held) == "ridder", "terugkomer houdt zijn soort")
	var lr: String = ks.lied("Fenna")
	ok(lr != "" and lr.length() <= 42, "bard zingt: " + lr)
	var soort_lang := 0
	for sj in ["binnen_ridder", "binnen_dief", "binnen_magier", "binnen_bard", "lied"]:
		for rsj in ks.stem.VOORRAAD[sj]:
			if ks.stem.vul(rsj, {"naam": "Bram", "held": "Bram", "bewoner": "Gloop", "val": "the Spike Pit"}).length() > 42:
				soort_lang += 1
	ok(soort_lang == 0, "regels van de soorten passen met Bram in 42 tekens (%d te lang)" % soort_lang)
	print("[hol-toets] klaar: %d FOUT" % fout)
	quit(1 if fout > 0 else 0)
