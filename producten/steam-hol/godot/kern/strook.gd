extends Node2D
# Kern van Het Hol (Olaf): de strook boven de taakbalk.
# - hoogte instelbaar (standaard 120 px, 96 tot 160), over de hele breedte, net boven de taakbalk
# - alleen de strook vangt klikken, de rest laat ze door
# - zuinig: 15 fps en alleen tekenen wat beweegt (proef 9 nov: stil beeld kost bijna niets)
# - geen kaartjes over andere vensters: alle tekst staat klein in de strook
# Argumenten na "--": hoogte=120 duur=60 log=<pad> demo=1 film=1 vers=1

const HOL := preload("res://hol/hol.gd")
const TEKST := preload("res://kern/tekst.gd")
const OPSLAG_VERSIE := 3   # 3: hol groeit naar links, schat rechts (oudere saves: vers begin, er zijn nog geen spelers)
const OPSLAG := "user://hol.json"

const REGELS := preload("res://kern/regels.gd")
const VOORTGANG := preload("res://systemen/voortgang.gd")
const NAMEN := ["Bram", "Odo", "Wil", "Gerda", "Pim", "Rik", "Mara", "Joost", "Fenna", "Ties", "Lotte", "Kees"]
const KLEUREN := ["#3f6fb5", "#8a4fb0", "#3f9a6a", "#c07a2a", "#6a6a7a", "#b0404a"]
const HOEDEN := ["#b33a3a", "#e0b040", "#2a5aa0", "#3a7a3a", "#7a3a8a", "#d06a2a"]

var hoogte := 120
var schaal := 3
var duur := 0.0
var logpad := ""
var demo := false
var film := false
var vers := false

var hol
var wezens: Node2D
var tekst
var rng := RandomNumberGenerator.new()
var t := 0.0
var volgende_held := 4.0       # demo: meteen (Sanne toets 3, punt 2: de film staat niet stil aan het begin)
var volgende_graaf := 9.0
var volgende_opslag := 30.0
var kroniek: Array[String] = []
var terugkomers: Array = []   # ontsnapte helden die terugkomen
var held_script
var eerste_held_gedaan := false   # de eerste held van een nieuw spel valt altijd (balans.md, Sanne)
# De eerste tien minuten van een nieuw spel (features.md; Sanne toets 2 punt 9, toets 3 punt 1): vijf vaste uitkomsten,
# elk eenmalig, zodat je in een paar minuten een val, een vlucht met wrok, die terugkomer, een Hoard-Toucher en de
# eerste hoed op Gloop ziet. Daarna is alles weer kans. Vlaggen in held.gd (Bram).
const BEGIN := ["vallen", "vluchten", "opgegeten", "terug", "doorlopen"]
# In de demo (film van een minuut) de Hoard-Toucher vóór de terugkomer, zodat hij rond 35 tot 40 s de schat raakt en nog
# wegrent, en daarna nog één keer opgegeten, zodat je de toren ziet groeien (Sanne toets 4, punten 4 en 6). De Hoard-Toucher
# slaat Gloop plat, dus hij komt pas na de held die opgegeten moet worden (anders loopt die langs een platte Gloop).
const BEGIN_DEMO := ["vallen", "vluchten", "opgegeten", "doorlopen", "terug", "opgegeten2"]
var begin_gedaan: Array = []   # welke stappen al geweest zijn (in de save)
var begin_vlucht := ""         # naam van de held die moest vluchten: hij is de terugkomer
var anim_t := 0.0
var gevallen_namen := {}   # naam -> hoe vaak gevallen; die naam komt daarna als "Kees II" (Sanne toets 2, punt 4)
var slijm
var slijm_plat := false
var regels                  # voorraad korte regels (kern/regels.gd), willekeurig per soort

func log_regel(tekst_: String) -> void:
	print(tekst_)
	if logpad != "":
		var f := FileAccess.open(logpad, FileAccess.READ_WRITE if FileAccess.file_exists(logpad) else FileAccess.WRITE)
		if f:
			f.seek_end()
			f.store_line(tekst_)
			f.close()

func _ready() -> void:
	for a in OS.get_cmdline_user_args():
		var kv := a.split("=", true, 1)
		if kv.size() < 2:
			continue
		match kv[0]:
			"hoogte": hoogte = clampi(int(kv[1]), 96, 160)
			"duur": duur = float(kv[1])
			"log": logpad = kv[1]
			"demo": demo = kv[1] == "1"
			"film": film = kv[1] == "1"
			"vers": vers = kv[1] == "1"
	rng.seed = 7 if demo else int(Time.get_unix_time_from_system())
	if not film:
		Engine.max_fps = 15
		OS.low_processor_usage_mode = true
	get_viewport().transparent_bg = true
	# Brams held als die er is, anders de stand-in
	held_script = load("res://systemen/held.gd") if ResourceLoader.exists("res://systemen/held.gd") else load("res://kern/standin_held.gd")

	var scherm := DisplayServer.screen_get_usable_rect()  # zonder taakbalk
	schaal = maxi(2, int(hoogte / 40.0))   # naar beneden afronden, anders valt de bovenkant van het hol weg
	var spel_h := int(hoogte / schaal)
	DisplayServer.window_set_size(Vector2i(scherm.size.x, hoogte))
	DisplayServer.window_set_position(Vector2i(scherm.position.x, scherm.position.y + scherm.size.y - hoogte))
	var boven := (spel_h - HOL.H) * schaal   # lege (doorzichtige) rand bovenaan bij 96 px
	DisplayServer.window_set_mouse_passthrough(PackedVector2Array([
		Vector2(0, boven), Vector2(scherm.size.x, boven), Vector2(scherm.size.x, hoogte), Vector2(0, hoogte)]))

	hol = Node2D.new()
	hol.set_script(HOL)
	hol.name = "Hol"
	hol.scale = Vector2(schaal, schaal)
	hol.position = Vector2(0, boven)
	add_child(hol)
	hol.maak(int(scherm.size.x / schaal))
	wezens = Node2D.new()
	wezens.name = "Wezens"
	hol.add_child(wezens)
	# Brams slijm (Gloop, gaat nooit dood) als die er is, anders de stand-in
	slijm = Node2D.new()
	slijm.set_script(load("res://systemen/slijm.gd") if ResourceLoader.exists("res://systemen/slijm.gd") else load("res://kern/standin_slijm.gd"))
	wezens.add_child(slijm)
	slijm.zet(hol, 10)   # plek volgt hieronder, na leg_aan
	if demo:
		volgende_held = 0.5
	if demo and "plat_s" in slijm:
		slijm.plat_s = 9.0   # demo: Gloop ±9 s plat in plaats van 60, net als de helden in de demo sneller komen (Sanne toets 2, punt 1)

	tekst = Node2D.new()
	tekst.set_script(TEKST)
	tekst.breedte = scherm.size.x
	tekst.hoogte = hoogte
	tekst.schaal = schaal
	add_child(tekst)
	# het hol groeit niet onder het tekstvak: de schat staat er rechts tegenaan, het hol groeit naar links
	hol.max_kol = int((scherm.size.x - tekst.vak_breedte() - 40) / (HOL.KOL * schaal)) - 1
	hol.leg_aan(hol.max_kol)
	slijm.position = hol.cel_naar_pos(Vector2i(hol.schat_kol - 2, 0))
	regels = REGELS.new()
	regels.rng = rng

	if not vers:
		laad()
		bewaar()   # meteen bewaren, anders telt dezelfde weg-tijd na een harde afsluiting nog een keer
	if kroniek.is_empty():
		_kroniek("Your hole is open. Heroes will come.")
	hol.gegraven.connect(func(cel): log_regel("HOL gegraven kolom %d" % cel.x))
	log_regel("HOL start hoogte=%d schaal=%d spelpixels=%dx%d venster=%s pos=%s held=%s" % [hoogte, schaal,
		int(scherm.size.x / schaal), spel_h, DisplayServer.window_get_size(), DisplayServer.window_get_position(), held_script.resource_path])

func _kroniek(r: String) -> void:
	kroniek.append(r)
	if kroniek.size() > 40:
		kroniek.remove_at(0)
	tekst.zet(kroniek, hol.goud)
	log_regel("HOL kroniek: " + r)

# naam met bijnaam voor een terugkomer ("Kees the Twice-Fled", of "Pim the Hoard-Toucher")
func _bewoner() -> String:
	return String(slijm.get("bijnaam_naam")) if "bijnaam_naam" in slijm else "Gloop"

func _held_naam(info: Dictionary) -> String:
	if bool(info.get("hoard_toucher", false)):
		return "%s the Hoard-Toucher" % info.naam
	return "%s %s" % [info.naam, _bijnaam(int(info.get("bezoeken", 0)))]

func _bijnaam(n: int) -> String:
	match n:
		1: return "the Once-Fled"
		2: return "the Twice-Fled"
		3: return "the Thrice-Fled"
	return "the %d-Times-Fled" % n

# geen twee helden met dezelfde naam tegelijk (in het hol of bij de terugkomers), anders snap je de wrok niet
func _vrije_naam() -> String:
	var bezet := {}
	for h in terugkomers:
		bezet[String(h.naam).split(" ")[0]] = true
	for w in wezens.get_children():
		if w.has_method("is_held"):
			bezet[String(w.info.get("naam", "")).split(" ")[0]] = true
	var vrij: Array = []
	for n in NAMEN:
		if not bezet.has(n):
			vrij.append(n)
	if vrij.is_empty():
		return NAMEN[rng.randi_range(0, NAMEN.size() - 1)]
	# eerst namen die nog nooit vielen; anders een naamgenoot met II of III, na III een andere naam
	var nooit: Array = vrij.filter(func(n): return not gevallen_namen.has(n))
	if not nooit.is_empty():
		return nooit[rng.randi_range(0, nooit.size() - 1)]
	var kan: Array = vrij.filter(func(n): return int(gevallen_namen[n]) < 3)
	if kan.is_empty():
		# alle namen vielen al drie keer: opnieuw tellen, dan weer een kale naam
		var n0: String = vrij[rng.randi_range(0, vrij.size() - 1)]
		gevallen_namen.erase(n0)
		return n0
	var n: String = kan[rng.randi_range(0, kan.size() - 1)]
	return n + (" II" if int(gevallen_namen.get(n, 0)) == 1 else " III")

# Welke vaste stap is nu aan de beurt: "" (vrij spel) of "wacht" (de volgende stap kan nog niet, even later opnieuw).
func _begin_lijst() -> Array:
	return BEGIN_DEMO if demo else BEGIN

func _begin_stap() -> String:
	var wacht := false
	for stap in _begin_lijst():
		if begin_gedaan.has(stap):
			continue
		if stap == "terug" and _terugkomer_i(begin_vlucht) < 0:
			wacht = true       # hij is nog in het hol; eerst een andere stap
			continue
		if stap.begins_with("opgegeten") and slijm.has_method("kan_vechten") and not slijm.kan_vechten():
			wacht = true       # Gloop ligt plat; wacht tot hij weer op is
			continue
		return stap
	return "wacht" if wacht else ""

func _terugkomer_i(naam: String) -> int:
	for i in terugkomers.size():
		if String(terugkomers[i].naam) == naam:
			return i
	return -1

func _nieuwe_held() -> bool:
	var info := {}
	var stap := _begin_stap()
	if stap == "wacht":
		return false
	# volgende held is een terugkomer: 25% (sim/UITKOMST.md); in de demo 50%, zodat de film een wrok laat zien.
	# Een aartsvijand (3 keer gevlucht) die aan de beurt is komt maar 15% van de keren.
	var kies := -1
	if stap == "terug":
		kies = _terugkomer_i(begin_vlucht)
	elif stap == "" and not terugkomers.is_empty() and rng.randf() < (0.5 if demo else 0.25):
		kies = rng.randi_range(0, terugkomers.size() - 1)
		if int(terugkomers[kies].bezoeken) >= 3 and rng.randf() >= 0.15:
			kies = -1
	if kies >= 0:
		info = terugkomers.pop_at(kies)
		var w: String = String(info.wrok)
		if int(info.bezoeken) >= 3:
			_kroniek(regels.kies("aartsvijand", {"naam": info.naam}))
		elif w == slijm.naam():
			_kroniek(regels.kies("terug_bewoner", {"naam": info.naam, "held": _held_naam(info), "bewoner": _bewoner()}))
		elif w.begins_with("the "):
			_kroniek(regels.kies("terug_val", {"naam": info.naam, "held": _held_naam(info), "val": w}))
		else:
			_kroniek(regels.kies("terug", {"naam": info.naam, "held": _held_naam(info)}))
	else:
		var naam := _vrije_naam()
		info = {"naam": naam, "bezoeken": 0, "wrok": "",
			"kleur": KLEUREN[rng.randi_range(0, KLEUREN.size() - 1)], "hoed": HOEDEN[rng.randi_range(0, HOEDEN.size() - 1)],
			"taai": rng.randi_range(0, 1), "hoed_nr": rng.randi_range(0, 3)}
		if naam.ends_with(" II") or naam.ends_with(" III"):
			_kroniek(regels.kies("naamgenoot", {"naam": naam, "oud": naam.split(" ")[0]}))
		else:
			_kroniek(regels.kies("binnen", {"naam": naam}))
	match stap:
		"vallen": info["moet_vallen"] = true
		"vluchten":
			info["moet_vluchten"] = true
			begin_vlucht = String(info.naam)
		"opgegeten", "opgegeten2":
			info["moet_opgegeten"] = true
			if stap == "opgegeten":
				# de eerste hoed op Gloop moet in één beeld lezen: de kroon (index 4 in Mila's held_hoeden.png),
				# zolang held.gd nog maar 4 hoeden kent de paarse puntmuts (index 1) (Sanne toets 4, punt 2)
				var tops: Array = held_script.get_script_constant_map().get("HOED_TOP", [])
				info["hoed_nr"] = 4 if tops.size() >= 10 else 1
		"doorlopen": info["moet_doorlopen"] = true
	if stap != "":
		begin_gedaan.append(stap)
		log_regel("HOL begin: %s (%s)" % [stap, info.naam])
	eerste_held_gedaan = true
	var d := info.duplicate()
	d["kleur"] = Color(info.kleur)
	d["hoed"] = Color(info.hoed)
	var held := Node2D.new()
	held.set_script(held_script)
	wezens.add_child(held)
	held.klaar.connect(_held_klaar)
	held.start(hol, d)
	return true

func _held_klaar(_held, uitkomst: String, info: Dictionary) -> void:
	var bewaar := info.duplicate()
	bewaar["kleur"] = (info.kleur as Color).to_html(false)
	bewaar["hoed"] = (info.hoed as Color).to_html(false)
	for v in ["moet_vallen", "moet_vluchten", "moet_doorlopen", "moet_opgegeten", "hoed_naar", "hoeden_bewoner"]:
		bewaar.erase(v)
	bewaar.erase("wat")
	if uitkomst == "ontsnapt":
		bewaar.bezoeken = int(info.get("bezoeken", 0)) + 1
		var oud_wrok: String = String(info.get("wrok", ""))
		bewaar.wrok = info.get("laatst_geraakt", oud_wrok if oud_wrok != "" else "your Hoard")
		bewaar.erase("laatst_geraakt")
		# 60% van wie vlucht komt ooit terug, aartsvijanden altijd (sim/UITKOMST.md); in de demo iedereen.
		# Wie niet terugkomt gaat met pensioen: geen straf, later een grapje bij openen.
		if demo or bewaar.bezoeken >= 3 or rng.randf() < 0.6 or String(info.naam) == begin_vlucht:
			terugkomers.append(bewaar)
		# plafond van 8: anders raken de namen op en groeit de save; de oudste die geen aartsvijand is gaat met pensioen
		if terugkomers.size() > 8:
			var weg_i := 0
			for i in terugkomers.size():
				if int(terugkomers[i].bezoeken) < 3:
					weg_i = i
					break
			terugkomers.remove_at(weg_i)
		# Geen straf: wie ontsnapt neemt niets mee dat jij kwijt bent, alleen zijn wrok.
		if bool(info.get("hoard_toucher", false)) and String(info.get("wat", "")).begins_with("touched"):
			_kroniek(regels.kies("schat", {"naam": info.naam}))
		else:
			var w: String = String(bewaar.wrok)
			_kroniek(regels.kies("vlucht", {"naam": info.naam, "bewoner": w.replace(" the Slime", "") if w != "your Hoard" else "you"}))
	else:
		# goud per val: 6, plus 3 per eerder bezoek; een held met een wrok is een beloning (balans.md punt 1, besluit Olaf)
		var buit := 6 + 3 * int(info.get("bezoeken", 0))
		hol.goud += buit
		var naam: String = String(info.naam)
		var basis := naam.split(" ")[0]
		gevallen_namen[basis] = int(gevallen_namen.get(basis, 0)) + 1
		hol.munt_regen(hol.pos_naar_cel(_held.position).x)
		var wat: String = String(info.get("wat", "fell"))
		var r := ""
		var extra := " +%d" % buit
		if wat.begins_with("finally"):
			r = regels.kies("afgerekend_aarts" if int(info.get("bezoeken", 0)) >= 3 else "afgerekend", {"naam": naam}, extra.length())
		elif wat.ends_with(slijm.naam()):
			r = regels.kies("val_bewoner", {"naam": naam, "bewoner": _bewoner()}, extra.length())
		else:
			r = regels.kies("val", {"naam": naam, "val": wat.replace("fell to ", "")}, extra.length())
		_kroniek(r + extra)
		# hoedentoren: zijn hoed staat nu op Gloop (slijm.gd, Bram). Eerste hoed altijd een regel, bij 25 en 100 de bijnaam,
		# anders hooguit een op de vier, zodat de val-regel niet verdrongen wordt (kroniek-regels.md)
		var n_hoed := int(info.get("hoeden_bewoner", 0))
		if String(info.get("hoed_naar", "")) == "bewoner" and n_hoed > 0:
			var w := {"bewoner": _bewoner(), "naam": basis}
			if n_hoed == 1:
				_kroniek(regels.kies("hoed_eerste", w))
			elif n_hoed == 25 or n_hoed == 100:
				w["bijnaam"] = "Hatted" if n_hoed == 25 else "Milliner"
				_kroniek(regels.kies("hoed_bijnaam", w))
			elif rng.randf() < 0.25:
				# "hat pile is taller than him" klopt pas bij een echte stapel (controleur punt 6)
				var soort := "hoed" if n_hoed >= 5 else "hoed_klein"
				_kroniek(regels.kies(soort, w))

func _process(delta: float) -> void:
	t += delta
	# Gloop plat of weer op: een regel in de kroniek (Sanne toets 2, punt 7).
	if slijm and slijm.has_method("kan_vechten"):
		var nu_plat: bool = not slijm.kan_vechten()
		if nu_plat != slijm_plat:
			slijm_plat = nu_plat
			_kroniek(regels.kies("plat" if nu_plat else "op", {"bewoner": _bewoner()}))
	var helden := 0
	for w in wezens.get_children():
		if w.has_method("is_held"):
			helden += 1
	if t >= volgende_held and helden < 3:
		var begin := _begin_stap() != ""
		if _nieuwe_held():
			# ritme: gemiddeld een held per ±50 s (balans.md), in de eerste tien minuten ±40 s;
			# in de demo sneller zodat de film van een minuut iets laat zien
			volgende_held = t + ((rng.randf_range(5.0, 7.0) if begin else rng.randf_range(6.0, 9.0)) if demo else (rng.randf_range(35.0, 45.0) if begin else rng.randf_range(40.0, 60.0)))
		else:
			volgende_held = t + 2.0   # een vaste stap moet nog even wachten
	# fakkels en schat bewegen alleen als er toch al getekend wordt (er loopt een held): 6 beeldjes per seconde
	if helden > 0:
		anim_t += delta
		if anim_t >= 1.0 / 6.0:
			anim_t = 0.0
			hol.tik()
	# stekelput klapt open als een held erop staat (alleen uiterlijk)
	for w in wezens.get_children():
		if w.has_method("is_held") and str(w.get("staat")) == "vallen":
			var k: int = hol.pos_naar_cel(w.position).x
			if hol.vallen.has(k) and not hol.put_open.has(k):
				hol.put_klap(k)
	if demo and t >= volgende_graaf:
		# demo: om en om een stuk gang erbij en een kamer boven de gang, zodat de film graven laat zien
		volgende_graaf = t + 9.0
		var k: int = hol.ingang_kol - 1
		if int(t / 9.0) % 2 == 0 and k >= 1:
			hol.klik(hol.cel_naar_pos(Vector2i(k, 0)) - Vector2(0, 6))
		else:
			for kk in range(hol.ingang_kol + 2, hol.schat_kol - 1):
				if not hol.boven[kk] and not hol.vallen.has(kk):
					hol.klik(Vector2(kk * HOL.KOL + 8, HOL.OPP + 6))
					break
	if t >= volgende_opslag:
		volgende_opslag = t + 30.0
		bewaar()
	if duur > 0.0 and t > duur:
		log_regel("HOL einde na %d s, fps=%d, goud=%d, terugkomers=%d" % [int(duur), Engine.get_frames_per_second(), hol.goud, terugkomers.size()])
		bewaar()
		get_tree().quit()

func _input(event: InputEvent) -> void:
	if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		var p: Vector2 = (event.position - hol.position) / schaal
		var wat: String = hol.klik(p)
		log_regel("HOL klik op %s: %s" % [event.position, wat if wat != "" else "niets"])
	elif event is InputEventMouseMotion and not tekst.hover:
		tekst.hover = true
		tekst.queue_redraw()

func _notification(what: int) -> void:
	if what == NOTIFICATION_WM_MOUSE_EXIT and tekst:
		tekst.hover = false
		tekst.queue_redraw()
	elif what == NOTIFICATION_WM_CLOSE_REQUEST:
		bewaar()

func bewaar() -> void:
	var data := {"versie": OPSLAG_VERSIE, "tijd": Time.get_unix_time_from_system(), "gang": hol.gang, "boven": hol.boven,
		"eerste_held_gedaan": eerste_held_gedaan, "vallen": hol.vallen, "ingang_kol": hol.ingang_kol, "gevallen_namen": gevallen_namen,
		"schat_kol": hol.schat_kol, "goud": hol.goud, "terugkomers": terugkomers, "kroniek": kroniek,
		"begin_gedaan": begin_gedaan, "begin_vlucht": begin_vlucht,
		"slijm": slijm.naar_dict() if slijm.has_method("naar_dict") else {}}
	var f := FileAccess.open(OPSLAG, FileAccess.WRITE)
	if f:
		f.store_string(JSON.stringify(data))
		f.close()

func laad() -> void:
	if not FileAccess.file_exists(OPSLAG):
		return
	var data = JSON.parse_string(FileAccess.get_file_as_string(OPSLAG))
	if typeof(data) != TYPE_DICTIONARY:
		log_regel("HOL opslag onleesbaar, vers begin")
		return
	if int(data.get("versie", 0)) < OPSLAG_VERSIE:
		log_regel("HOL opslag van een oudere versie, vers begin")
		return
	var g: Array = data.get("gang", [])
	for i in mini(g.size(), hol.kolommen):
		hol.gang[i] = bool(g[i])
	hol.vallen.clear()
	for k in data.get("vallen", {}):
		hol.vallen[int(k)] = String(data.vallen[k])
	var b: Array = data.get("boven", [])
	for i in mini(b.size(), hol.kolommen):
		hol.boven[i] = bool(b[i])
	hol.schat_kol = clampi(int(data.get("schat_kol", hol.schat_kol)), 0, mini(hol.max_kol, hol.kolommen - 1))
	hol.ingang_kol = clampi(int(data.get("ingang_kol", hol.ingang_kol)), 1, hol.schat_kol - 1)
	hol.gang[0] = false   # oude save met de ingang op kolom 0: die kolom hoort niet meer bij de gang (controleur 22:30)
	var gn = data.get("gevallen_namen", {})
	for n in gn:
		gevallen_namen[String(n)] = int(gn[n])
	slijm.position = hol.cel_naar_pos(Vector2i(hol.schat_kol - 2, 0))
	hol._schatkamer()
	eerste_held_gedaan = bool(data.get("eerste_held_gedaan", true))
	# een save van voor de eerste tien minuten: dat begin is voorbij
	begin_gedaan = data.get("begin_gedaan", BEGIN.duplicate() if eerste_held_gedaan else [])
	begin_vlucht = String(data.get("begin_vlucht", ""))
	if slijm.has_method("van_dict"):
		slijm.van_dict(data.get("slijm", {}))
	hol.goud = int(data.get("goud", 0))
	terugkomers = data.get("terugkomers", [])
	# de held die moest vluchten liep nog in het hol toen het spel dichtging: hij komt nooit meer terug, dus "terug" telt
	# als gedaan, anders wacht het begin voor altijd (controleur 9 nov 22:30)
	if begin_gedaan.has("vluchten") and not begin_gedaan.has("terug") and _terugkomer_i(begin_vlucht) < 0:
		begin_gedaan.append("terug")
	for r in data.get("kroniek", []):
		kroniek.append(String(r))
	# terwijl je weg was (Bram, voortgang.gd): alleen winst, plafond 12 uur, 2 tot 3 regels met namen
	var weg := VOORTGANG.reken(int(data.get("tijd", 0)), int(Time.get_unix_time_from_system()), hol.vallen.size(), 1, 7)
	if int(weg.helden) > 0:
		hol.goud += int(weg.goud)
		var helden_d := {}
		for h in terugkomers:
			helden_d[String(h.naam)] = {"gevlucht": int(h.bezoeken), "wrok": String(h.get("wrok", ""))}
		var namen := [slijm.naam()]
		if not hol.vallen.is_empty():
			namen.append("the Spike Pit")
		for r in VOORTGANG.verhaal(weg, helden_d, namen, 7):
			kroniek.append(r)
	hol.queue_redraw()
	tekst.zet(kroniek, hol.goud)
	log_regel("HOL opslag geladen: %d terugkomers, %d goud" % [terugkomers.size(), hol.goud])
