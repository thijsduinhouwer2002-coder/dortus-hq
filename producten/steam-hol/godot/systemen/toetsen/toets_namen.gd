extends SceneTree
# Toetsen voor namen, terugslag en binnenkomst (Olaf 19 nov, uit toets_systemen.gd gehaald, kan-punt automatische keurder 19 nov).
# Draaien: godot --headless --path <map met project.godot> -s systemen/toetsen/toets_namen.gd
var fout := 0

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[hol-toets] OK ", wat)
	else:
		fout += 1
		print("[hol-toets] FOUT ", wat)

# nep-strook voor het nieuwe hol-niveau terwijl je kijkt (Iris keuring 24 punt 1, Sanne 20 nov 09:50)
class NepNiveau:
	var faam := 0
	var t := 100.0
	var demo := false
	var volgende_held := 130.0
	var regels = load("res://kern/regels.gd").new()
	var kroniek: Array = []
	func log_regel(_r: String) -> void:
		pass
	func _kroniek(r: String, _binnen := false, soort := "") -> void:
		kroniek.append([soort, r])

func _init() -> void:
	# terugslag (Sanne 17 nov 09:02, Iris keuring 21): elke soort en trek heeft een eigen val- en vluchtlijst, past met " +12"
	# bij een lange naam, zonder he/his/him, en terugslag() kiest de eigen lijst alleen bij een opzet.
	var RT = load("res://kern/regels.gd").new()
	var AF = load("res://kern/afloop.gd")
	var nep_ts := {"regels": RT}
	var ts_mist: Array = []
	var ts_lang: Array = []
	var ts_hij: Array = []
	for so in ["ridder", "dief", "magier", "bard", "slaapkop", "wraakzuchtig", "opschepper"]:
		ok(RT.heeft("binnen_" + so), "terugslag: binnen_%s bestaat" % so)
		for pre in ["val_", "vlucht_"]:
			if not RT.heeft(pre + so):
				ts_mist.append(pre + so)
				continue
			for rts in RT.BRAM.VOORRAAD[pre + so]:
				for bw in ["Gloop", "the Spike Pit", "you"]:
					var v_ts: String = RT.vul(rts, {"naam": "Joost III", "bewoner": bw})
					if v_ts.length() > RT.MAX - (3 if pre == "val_" else 0):   # nieuwe held: buit hooguit " +9"
						ts_lang.append(v_ts)
					for w in [" he ", " he.", " his ", " him", "He "]:
						if (" " + v_ts).contains(w):
							ts_hij.append(v_ts)
	ok(ts_mist.is_empty(), "terugslag: alle val_ en vlucht_ lijsten bestaan (mist %s)" % str(ts_mist))
	ok(ts_lang.is_empty(), "terugslag: alles past bij Joost III, val met +9 (te lang %s)" % str(ts_lang))
	ok(ts_hij.is_empty(), "terugslag: geen he/his/him (%s)" % str(ts_hij))
	ok(AF.terugslag(nep_ts, {"binnen_soort": "ridder"}, "val") == "val_ridder", "terugslag: ridder valt in val_ridder")
	ok(AF.terugslag(nep_ts, {"binnen_soort": "ridder", "bezoeken": 1}, "val") == "val", "terugslag: terugkomer gewoon val")
	ok(AF.terugslag(nep_ts, {"binnen_soort": "bard"}, "vlucht") == "vlucht" and AF.terugslag(nep_ts, {"binnen_soort": "bard"}, "val") == "val_bard", "terugslag: bard vlucht gewoon, valt wel terug")
	ok(AF.terugslag({"regels": RT, "demo": true}, {"binnen_soort": "ridder"}, "val") == "val", "terugslag: demofilm gewoon val")
	ok(AF.terugslag(nep_ts, {"binnen_soort": "dief"}, "vlucht") == "vlucht_dief", "terugslag: dief vlucht in vlucht_dief")
	ok(AF.terugslag(nep_ts, {}, "val") == "val", "terugslag: zonder opzet gewoon val")
	ok(AF.terugslag(nep_ts, {"binnen_soort": "onbekend"}, "vlucht") == "vlucht", "terugslag: onbekende soort gewoon vlucht")
	# binnen_soort van binnenkomst tot held_klaar (kan-punt automatische keurder 18 nov 22:54): een held die als dief
	# binnenkwam vlucht met vlucht_dief, zijn terugkomer-kaart heeft geen binnen_soort meer, en bij zijn terugkeer
	# vlucht hij met de gewone vluchtlijst. Echte afloop.gd met een nep-strook die alleen de gekozen soorten bijhoudt.
	var BS_R := GDScript.new()
	BS_R.source_code = "extends RefCounted\nvar echt = load(\"res://kern/regels.gd\").new()\nvar soorten: Array = []\nfunc heeft(s: String) -> bool:\n\treturn echt.heeft(s)\nfunc kies(s: String, _w: Dictionary, _e := 0) -> String:\n\tsoorten.append(s)\n\treturn \"x\"\n"
	BS_R.reload()
	var BS_S := GDScript.new()
	BS_S.source_code = "extends RefCounted\nvar regels\nvar boek = load(\"res://systemen/boek.gd\").new()\nvar t := 100.0\nvar demo := false\nvar rng := RandomNumberGenerator.new()\nvar terugkomers: Array = []\nvar pensioen_namen: Array = []\nvar begin_vlucht := \"\"\nvar vlucht_t := 0.0\nvar vlucht_tijd := {}\nvar lied_helden := 0\nvar volgende_held := 999.0\nfunc _kroniek(_r: String, _b := false, _s := \"\") -> void:\n\tpass\nfunc _bewoner() -> String:\n\treturn \"Gloop\"\n"
	BS_S.reload()
	var bs_s = BS_S.new()
	bs_s.regels = BS_R.new()
	bs_s.rng.seed = 7   # eerste randf() < 0,6: hij komt terug; zo niet, dan faalt de toets hieronder (geen nagebootste kaart)
	var bs_info := {"naam": "Vos", "kleur": Color.RED, "hoed": Color.BLUE, "bezoeken": 0, "wrok": "", "soort_held": "dief", "binnen_soort": "dief", "lied": 0}
	AF.held_klaar(bs_s, null, "ontsnapt", bs_info)
	ok(bs_s.regels.soorten.has("vlucht_dief"), "binnen_soort: dief die binnenkwam vlucht met vlucht_dief (%s)" % str(bs_s.regels.soorten))
	var bs_kaart: Dictionary = {}
	for bs_k in bs_s.terugkomers:
		if String(bs_k.naam) == "Vos":
			bs_kaart = bs_k
	ok(not bs_kaart.is_empty(), "binnen_soort: Vos komt terug bij zaad 7 (anders ander zaad kiezen)")
	ok(not bs_kaart.has("binnen_soort") and int(bs_kaart.get("bezoeken", 0)) == 1, "binnen_soort: terugkomer-kaart zonder binnen_soort, bezoeken 1")
	bs_s.regels.soorten.clear()
	var bs_terug: Dictionary = bs_kaart.duplicate()
	bs_terug["kleur"] = Color.RED
	bs_terug["hoed"] = Color.BLUE
	AF.held_klaar(bs_s, null, "ontsnapt", bs_terug)
	ok(bs_s.regels.soorten.has("vlucht") and not bs_s.regels.soorten.has("vlucht_dief"), "binnen_soort: bij terugkeer de gewone vluchtlijst (%s)" % str(bs_s.regels.soorten))
	ok(not RT.VOORRAAD["val_bewoner"].has("{naam} stays forever.") and RT.VOORRAAD["val"].size() == 8, "val 8 regels, stays forever niet meer in val_bewoner")
	# Dame en hap per soort (Sanne 17 nov 10:00, Iris keuring 21 punt 1, features.md keurregel)
	var NM = load("res://kern/namen.gd")
	var vr_mist: Array = NM.VROUW.filter(func(n): return not NM.NAMEN.has(n))
	ok(vr_mist.is_empty() and NM.VROUW.size() == 10, "VROUW staat in NAMEN (%s)" % str(vr_mist))
	# Namen zonder families op een rij (Sanne 17 nov 16:50, Iris keuring 22 punt 1 en 2)
	var nm_lang: Array = NM.NAMEN.filter(func(n): return n.length() > 5)
	var nm_dub := {}
	for n in NM.NAMEN:
		nm_dub[n] = true
	ok(NM.NAMEN.size() == 24 and nm_dub.size() == 24 and nm_lang.is_empty(), "namen: 24, uniek, hooguit 5 letters (%s)" % str(nm_lang))
	ok(NM.ouder("Fenna II") == "mom" and NM.ouder("Maud") == "mom" and NM.ouder("Kees III") == "dad", "ouder: mom bij VROUW, anders dad")
	ok(RT.vul("{naam} wants {ouder}'s boot back.", {"naam": "Fenna III"}) == "Fenna III wants mom's boot back." and RT.BRAM.vul("{naam} wants {ouder}'s hat back.", {"naam": "Kees II"}) == "Kees II wants dad's hat back.", "vul: {ouder} vult zich uit {naam} (strook en kroniek)")
	var nm_dad: Array = []
	for so in ["naamgenoot", "naamgenoot_hoed", "naamgenoot_laars"]:
		for rd in RT.BRAM.VOORRAAD.get(so, []) + RT.VOORRAAD.get(so, []):
			for nm in NM.VROUW:
				var vd: String = RT.vul(rd, {"naam": nm + " III", "oud": nm})
				if vd.contains("dad") or vd.contains("{") or vd.length() > RT.MAX:
					nm_dad.append(vd)
	ok(nm_dad.is_empty(), "naamgenoot: geen dad bij een vrouwennaam, alles gevuld, past (%s)" % str(nm_dad))
	# naamgenoot hooguit één keer per 5 min (Iris keuring 23 punt 1), één keer per voornaam, alleen II en III
	var BK = load("res://kern/binnenkomst.gd")
	ok(BK.naamgenoot_mag("Kees II", {}, 10.0, -1000.0) and not BK.naamgenoot_mag("Kees", {}, 10.0, -1000.0), "naamgenoot: II mag, zonder II niet")
	ok(not BK.naamgenoot_mag("Kees II", {"Kees": true}, 900.0, -1000.0), "naamgenoot: één keer per voornaam")
	ok(not BK.naamgenoot_mag("Maud III", {}, 1100.0, 884.0) and BK.naamgenoot_mag("Maud III", {}, 1184.0, 884.0), "naamgenoot: niet binnen 300 s na de vorige, wel daarna")
	# laarsgrap alleen als de ouder zelf een laars achterliet (Iris 19 nov): niet in de gewone voorraad, ouder is de vorige
	ok(not str(RT.VOORRAAD["naamgenoot"]).contains("boot") and str(RT.VOORRAAD["naamgenoot_laars"]).contains("boot"), "naamgenoot: laarsgrap apart")
	ok(not str(load("res://systemen/kroniek_regels.gd").VOORRAAD["naamgenoot"]).contains("boot"), "kroniek: naamgenoot zonder laarsgrap (Iris 19 nov)")
	ok(BK.ouder_naam("Merel II") == "Merel" and BK.ouder_naam("Merel III") == "Merel II", "naamgenoot: ouder van II en III")
	var ng_gezien := {}
	var ng_laatst := -1000.0
	var ng_tijden: Array = []
	for ng_i in 40:   # elke 20 s een II tussen 800 en 1600 s, zoals na ±14 min in duurtest 44127812882
		var ng_naam: String = String(NM.NAMEN[ng_i % NM.NAMEN.size()]) + " II"
		var ng_t := 800.0 + 20.0 * ng_i
		if BK.naamgenoot_mag(ng_naam, ng_gezien, ng_t, ng_laatst):
			ng_gezien[ng_naam.split(" ")[0]] = true
			ng_laatst = ng_t
			ng_tijden.append(ng_t)
	var ng_te_kort := 0
	for ng_j in range(1, ng_tijden.size()):
		if ng_tijden[ng_j] - ng_tijden[ng_j - 1] < 300.0:
			ng_te_kort += 1
	ok(ng_te_kort == 0 and ng_tijden.size() == 3, "naamgenoot: 40 II's in 800 s geven 3 regels, 300 s uit elkaar (%s)" % str(ng_tijden))
	var VN_S := GDScript.new()
	VN_S.source_code = "extends RefCounted\nvar terugkomers: Array = []\nvar wezens := Node.new()\nvar pensioen_namen: Array = []\nvar rng := RandomNumberGenerator.new()\nvar gevallen_namen := {}\nvar recente_namen: Array = []\n"
	VN_S.reload()
	var vn_s = VN_S.new()
	vn_s.rng.seed = 1794860558
	var vn_reeks: Array = []
	var vn_rij := 0
	var nm_dicht := 0
	var vn_kaal := true
	for i in 24 * 3 * 3 + 10:
		var vn_nn: String = NM.vrije_naam(vn_s)
		var vn_bs: String = vn_nn.split(" ")[0]
		if i < 24 and vn_nn != vn_bs:
			vn_kaal = false
		var vn_achter: Array = vn_reeks.slice(-6)
		if vn_achter.has(vn_bs):
			nm_dicht += 1
		if vn_reeks.size() > 0 and vn_reeks[-1] == vn_bs:
			vn_rij += 1
		vn_reeks.append(vn_bs)
		vn_s.gevallen_namen[vn_bs] = int(vn_s.gevallen_namen.get(vn_bs, 0)) + 1   # iedereen valt (zoals afloop.gd)
	ok(vn_kaal, "vrije_naam: eerst valt elke naam één keer kaal")
	ok(vn_rij == 0 and nm_dicht == 0, "vrije_naam: nooit dezelfde voornaam binnen 6 nieuwe helden (%d op een rij, %d dichtbij)" % [vn_rij, nm_dicht])
	ok(vn_s.gevallen_namen.values().all(func(t): return int(t) <= 3), "vrije_naam: na III gaat de telling leeg, nooit IV")
	var vn_s2 = VN_S.new()
	for n in NM.NAMEN:
		vn_s2.gevallen_namen[n] = 3
	ok(NM.vrije_naam(vn_s2).split(" ").size() == 1 and vn_s2.gevallen_namen.size() == 0, "vrije_naam: alle namen op 3, hele telling leeg, kale naam")
	var vn_s3 = VN_S.new()
	for n in NM.NAMEN.slice(0, 23):
		vn_s3.terugkomers.append({"naam": n + " II"})
	vn_s3.recente_namen = [NM.NAMEN[23]]
	ok(NM.vrije_naam(vn_s3).begins_with(NM.NAMEN[23]), "vrije_naam: alleen een recente naam vrij, dan toch die")
	var vn_s4 = VN_S.new()
	for n in NM.NAMEN:
		vn_s4.gevallen_namen[n] = 3
	vn_s4.gevallen_namen["Kees"] = 1
	vn_s4.recente_namen = ["Kees"]
	ok(NM.vrije_naam(vn_s4) == "Kees II" and vn_s4.gevallen_namen.size() == 24, "vrije_naam: recente Kees op 1 houdt zijn II, geen vierde naam")
	vn_s4.wezens.free()
	vn_s.wezens.free()
	vn_s2.wezens.free()
	vn_s3.wezens.free()
	ok(NM.titel("Gerda") == "Dame" and NM.titel("Gerda II") == "Dame" and NM.titel("Lotte the Twice-Fled") == "Dame" and NM.titel("Odo") == "Sir" and NM.titel("Marat") == "Sir", "titel: Dame uit de voornaam, anders Sir")
	ok(RT.vul("{titel} {naam} clanks in.", {"naam": "Mara III"}) == "Dame Mara III clanks in." and RT.vul("{titel} {naam} clanks in.", {"naam": "Kees"}) == "Sir Kees clanks in.", "vul: {titel} vult zich uit {naam}")
	ok(RT.kies("binnen_ridder", {"naam": "Fenna"}).begins_with("Dame Fenna"), "kies: ridder Fenna is Dame")
	var dm_sir: Array = []
	var dm_hij: Array = []
	var hp_lang: Array = []
	var hp_mist: Array = []
	for so in ["ridder", "dief", "magier", "bard", "slaapkop", "wraakzuchtig", "opschepper"]:
		if not RT.heeft("hap_" + so) or RT.BRAM.VOORRAAD["hap_" + so].size() != 2:
			hp_mist.append("hap_" + so)
		for pre in ["binnen_", "val_", "vlucht_", "hap_"]:
			for rd in RT.BRAM.VOORRAAD.get(pre + so, []):
				for nm in NM.NAMEN:
					var v_dm: String = RT.vul(rd, {"naam": nm + " III", "bewoner": "Gloop", "val": "the Spike Pit"})
					if NM.VROUW.has(nm) and v_dm.contains("Sir "):
						dm_sir.append(v_dm)
					for w in [" he ", " he.", " his ", " him", "He ", " she ", " her "]:
						if (" " + v_dm).contains(w):
							dm_hij.append(v_dm)
					if pre == "hap_" and v_dm.length() > RT.MAX - 3:   # nieuwe held: buit hooguit " +9"
						hp_lang.append(v_dm)
					if v_dm.contains("{"):
						dm_sir.append(v_dm)   # niets mag ongevuld blijven
	ok(hp_mist.is_empty(), "hap: elke soort heeft 2 hap-regels (mist %s)" % str(hp_mist))
	ok(dm_sir.is_empty(), "geen Sir bij een vrouwennaam en niets ongevuld (%s)" % str(dm_sir))
	# ook alle andere soorten (vlucht, val, lied, pensioen...), behalve de ene regel over Gloop (controleur 10:50)
	for vr in [RT.VOORRAAD, RT.BRAM.VOORRAAD]:
		for sk_h in vr:
			for rd in vr[sk_h]:
				var v_al: String = " " + RT.vul(rd, {"naam": "Gerda", "held": "Gerda the Twice-Fled", "bewoner": "Gloop", "val": "the Spike Pit", "oud": "Gerda", "hoed": "crown", "bijnaam": "Hatful", "n": "3"}) + " "
				if v_al.contains("taller than him"):
					continue
				for w in [" he ", " he.", " he,", " his ", " his.", " him ", " him.", " him,", " He ", " His "]:
					if v_al.contains(w):
						dm_hij.append(v_al.strip_edges())
	ok(dm_hij.is_empty(), "geen he/his/him in regels over helden (%s)" % str(dm_hij))
	ok(hp_lang.is_empty(), "hap: past met elke naam III en +9 (te lang %s)" % str(hp_lang))
	ok(AF.hap_soort(nep_ts, {"binnen_soort": "dief"}) == "hap_dief" and AF.hap_soort(nep_ts, {}) == "val_bewoner", "hap: eigen soort bij een opzet, anders val_bewoner")
	ok(AF.hap_soort(nep_ts, {"binnen_soort": "dief", "bezoeken": 2}) == "val_bewoner" and AF.hap_soort({"regels": RT, "demo": true}, {"binnen_soort": "dief"}) == "val_bewoner", "hap: terugkomer en demofilm gewoon val_bewoner")
	var hs_hij: Array = []
	for txt in [FileAccess.get_file_as_string("res://systemen/heldensoort.gd"), FileAccess.get_file_as_string("res://systemen/boek.gd")]:
		for w in ["Pits love him", "catch him", "If he ", "his own", "got him", "He got", "He'd"]:
			if txt.contains(w):
				hs_hij.append(w)
	ok(hs_hij.is_empty(), "Heldenboek en uitleg zonder he/his/him (%s)" % str(hs_hij))
	# nieuw hol-niveau terwijl je kijkt: eigen regel met het nummer, volgende held binnen 6 s, niet na weg en niet in de demo
	var AFN = load("res://kern/afloop.gd")
	var nn := NepNiveau.new()
	nn.faam = 2
	var niv_nn: Array = AFN.faam_erbij(nn, 1, true)   # faam 3 = hol-niveau 2
	ok(nn.kroniek.is_empty() and niv_nn == [2], "niveau live: faam_erbij zegt zelf nog niets, geeft het niveau terug (%s)" % str(niv_nn))
	nn._kroniek("Joost came back. The Spike Pit won. +9", false, "val")   # valregel eerst, zoals held_klaar
	AFN.niveau_na(nn, niv_nn)
	ok(nn.kroniek.size() == 2 and nn.kroniek[0][0] == "val" and nn.kroniek[1][0] == "hol_niveau", "niveau live: niveauregel na de valregel (%s)" % str(nn.kroniek))
	nn.kroniek = nn.kroniek.slice(1)
	ok(nn.kroniek.size() == 1 and nn.kroniek[0][0] == "hol_niveau" and String(nn.kroniek[0][1]).contains("2"), "niveau live: eigen regel met nummer (%s)" % str(nn.kroniek))
	ok(absf(nn.volgende_held - 106.0) < 0.01, "niveau live: volgende held naar voren tot t+6 (%.1f)" % nn.volgende_held)
	nn.volgende_held = 103.0
	nn.faam = 4
	AFN.niveau_na(nn, AFN.faam_erbij(nn, 1, true))   # faam 5 = hol-niveau 3
	ok(absf(nn.volgende_held - 103.0) < 0.01, "niveau live: held die al eerder komt blijft (%.1f)" % nn.volgende_held)
	var nw := NepNiveau.new()
	nw.faam = 2
	AFN.niveau_na(nw, AFN.faam_erbij(nw, 1))   # zoals na weg zijn
	ok(nw.kroniek.is_empty() and nw.volgende_held == 130.0, "niveau na weg: geen extra regel of held (weg_regel zegt het al)")
	var nd := NepNiveau.new()
	nd.demo = true
	nd.faam = 2
	AFN.niveau_na(nd, AFN.faam_erbij(nd, 1, true))
	ok(nd.kroniek.is_empty() and nd.volgende_held == 130.0, "niveau in de demo: niets extra")
	var lang_n: Array = []
	for n in range(2, 13):
		var r: String = nn.regels.kies("hol_niveau", {"n": str(n)})
		if r.length() > 42 or not r.contains(str(n)):
			lang_n.append(r)
	ok(lang_n.is_empty(), "hol_niveau past in 42 tekens met nummer 2 tot 12 (%s)" % str(lang_n))
	print("[hol-toets] klaar: %d FOUT" % fout)
	quit(1 if fout > 0 else 0)
