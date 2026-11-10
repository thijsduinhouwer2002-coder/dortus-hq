extends Node2D
# Kern van Het Hol (Olaf): de strook boven de taakbalk.
# - hoogte instelbaar (standaard 120 px, 96 tot 160), over de hele breedte, net boven de taakbalk
# - alleen de strook vangt klikken, de rest laat ze door
# - zuinig: 15 fps en alleen tekenen wat beweegt (proef 9 nov: stil beeld kost bijna niets)
# - geen kaartjes over andere vensters: alle tekst staat klein in de strook
# Argumenten na "--": hoogte=120 duur=60 log=<pad> demo=1 film=1 vers=1

const HOL := preload("res://hol/hol.gd")
const TEKST := preload("res://kern/tekst.gd")
const OPSLAG_M := preload("res://kern/opslag.gd")
const NAMEN_M := preload("res://kern/namen.gd")
const WACHTRIJ := preload("res://kern/wachtrij.gd")
const AFLOOP := preload("res://kern/afloop.gd")
const KAARTJE := preload("res://kern/kaartje.gd")
const BOEK := preload("res://systemen/boek.gd")         # het Heldenboek (Bram 03:45); stap 1: bijhouden, opslaan, regel
const SOORT := preload("res://systemen/heldensoort.gd")   # ridder, dief, magier, bard en drie trekken (Bram, versie 1)
# Hoogte van de strook, in het spel te kiezen met rechtsklik (96, 120, 160), bewaard los van het spel
# (eerlijk in de winkeltekst: "you can set it from 96 to 160", Sanne en Daan 10 nov 00:00)
const INSTELLING := "user://instellingen.json"
const HOOGTES := [96, 120, 160]

const REGELS := preload("res://kern/regels.gd")
# Demo: elke nieuwe held een andere hoed uit Mila's tien, zodat de minuut zelf laat zien dat er veel hoeden zijn
# (Sanne toets 6, punt 2). Index: 0 helm, 1 puntmuts, 2 kap, 3 pet, 4 kroon, 5 koksmuts, 6 emmer, 7 hoge hoed, 8 pan,
# 9 veermuts. De kroon blijft voor de held die Gloop opeet (eerste hoed op Gloop).
const DEMO_HOEDEN := [5, 0, 8, 6, 7, 9, 3, 2, 1]
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
var vlucht_t := -100.0         # wanneer hij vluchtte (demo: terug pas 4 s later)
var opgegeten_t := -100.0      # demo: wanneer de held die opgegeten wordt binnenkwam (Hoard-Toucher pas 10 s later)
var demo_hoed_i := 0           # demo: volgende hoed uit DEMO_HOEDEN
var vlucht_tijd := {}          # demo: naam -> wanneer hij vluchtte (niet bewaard); een terugkomer pas na DEMO_TERUG_NA s
const DEMO_TERUG_NA := 8.0     # Sanne toets 7, punt 3: Tibbe klom de ladder op en meteen weer af, dat leest als een fout
var anim_t := 0.0
var gevallen_namen := {}   # naam -> hoe vaak gevallen; die naam komt daarna als "Kees II" (Sanne toets 2, punt 4)
var slijm
var slijm_plat := false
var regels                  # voorraad korte regels (kern/regels.gd), willekeurig per soort
var kaart_soort := ""       # het kaartje voor upgrades (kern/kaartje.gd): "" dicht, anders "slijm" of "stekelput"
var kaart_t := 0.0          # laatste klik op het kaartje (dicht na 6 s)
var kaart_kol := -1         # kolom van het aangeklikte object (muntjes vliegen daarheen, Remove haalt die put weg)
var demo_koop := 0          # demo: 0 nog niets, 1 kaartje open, 2 gekocht (kern/kaartje.gd, demo_stap)
var kaart_regel := ""       # na Buy blijft het kaartje 2,5 s staan; deze regel komt als het dichtgaat (Sanne toets 8, punt 3)
var kaart_gekocht := false  # het kaartje staat in die 2,5 s (alleen de nieuwe naam en Undo)
var helden_nr := 0          # hoeveelste nieuwe held van dit spel (in de save); de eerste 10 zijn gewoon (heldensoort.gd)
var boek = BOEK.new()        # wat er in het Heldenboek staat (in de save); de bladzijde in het paneel volgt in stap 2
var lied_helden := 0        # zoveel helden komen nog snel na het lied van een gevluchte bard (in de save)
# Demo: de held die moet vluchten is een bard, zodat de minuut één lied laat zien (2 helden snel erachter, Bram 02:30)
const DEMO_BARD := true

func log_regel(tekst_: String) -> void:
	print(tekst_)
	if logpad != "":
		var f := FileAccess.open(logpad, FileAccess.READ_WRITE if FileAccess.file_exists(logpad) else FileAccess.WRITE)
		if f:
			f.seek_end()
			f.store_line(tekst_)
			f.close()

func _ready() -> void:
	if FileAccess.file_exists(INSTELLING):
		var inst = JSON.parse_string(FileAccess.get_file_as_string(INSTELLING))
		if inst is Dictionary and inst.has("hoogte"):
			hoogte = clampi(int(inst.hoogte), 96, 160)
	for a in OS.get_cmdline_user_args():   # argumenten (workflow) gaan voor de instelling
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
	# klikken gaan door de lucht en het gras heen naar het venster erachter; alleen het hol zelf (onder het maaiveld)
	# vangt de muis (graven, hover op het paneel). Zo blokkeert de strook nooit meer dan de rijen van het hol.
	vangt_y = boven + HOL.OPP * schaal
	_muis_vlak(false)

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
	if demo:
		hol.goud = KAARTJE.DEMO_GOUD
	if kroniek.is_empty():
		_kroniek("Your hole is open. Heroes will come.")
	hol.gegraven.connect(func(cel): log_regel("HOL gegraven kolom %d" % cel.x))
	log_regel("HOL start hoogte=%d schaal=%d spelpixels=%dx%d venster=%s pos=%s held=%s" % [hoogte, schaal,
		int(scherm.size.x / schaal), spel_h, DisplayServer.window_get_size(), DisplayServer.window_get_position(), held_script.resource_path])

# De kroniek-wachtrij (welke regel wanneer): kern/wachtrij.gd. Hier alleen de toestand.
var wachtrij: Array = []        # [{r, binnen, sinds}]
var regel_sinds := -100.0       # wanneer de getoonde regel kwam
var regel_binnen := false       # is de getoonde regel een binnenkom-regel

func _kroniek(r: String, binnen := false, soort := "") -> void:
	wachtrij.append({"r": r, "binnen": binnen, "sinds": t, "soort": soort})
	_toon()

func _toon() -> void:
	if kaart_soort != "":
		return   # het kaartje staat in het paneel: de kroniek wacht tot het dicht is, zo mis je geen regel
	WACHTRIJ.toon(self)

# namen, bijnamen en de terugkomer-regel: kern/namen.gd
func _bewoner() -> String:
	return NAMEN_M.bewoner(self)

func _held_naam(info: Dictionary) -> String:
	return NAMEN_M.held_naam(self, info)

func _terug_regel(soort: String, info: Dictionary, w: Dictionary) -> String:
	return NAMEN_M.terug_regel(self, soort, info, w)

func _vrije_naam() -> String:
	return NAMEN_M.vrije_naam(self)

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
		if stap == "terug" and demo and t - vlucht_t < 4.0:
			return "wacht"     # demo: niet meteen na zijn vlucht terug, anders komen vier regels in 2 s (film run 42721290569)
		if stap == "doorlopen" and demo and t - opgegeten_t < 10.0:
			return "wacht"     # demo: Hoard-Toucher 4 s later dan voorheen, de drukke stap rond 30 s (Sanne toets 6, punt 3)
		if stap.begins_with("opgegeten") and slijm.has_method("kan_vechten") and not slijm.kan_vechten():
			wacht = true       # Gloop ligt plat; wacht tot hij weer op is
			continue
		return stap
	return "wacht" if wacht else ""

func _kroniek_bewaar() -> Array[String]:
	return WACHTRIJ.kroniek_bewaar(self)

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
		var kan: Array = []
		for i in terugkomers.size():
			if not demo or t - float(vlucht_tijd.get(String(terugkomers[i].naam), -100.0)) >= DEMO_TERUG_NA:
				kan.append(i)
		if not kan.is_empty():
			kies = kan[rng.randi_range(0, kan.size() - 1)]
			if int(terugkomers[kies].bezoeken) >= 3 and rng.randf() >= 0.15:
				kies = -1
	if kies >= 0:
		info = terugkomers.pop_at(kies)
		var w: String = String(info.wrok)
		if int(info.bezoeken) >= 3:
			_kroniek(regels.kies("aartsvijand", {"naam": info.naam}))
		elif w == slijm.naam():
			_kroniek(_terug_regel("terug_bewoner", info, {"bewoner": _bewoner()}))
		elif w.begins_with("the "):
			_kroniek(_terug_regel("terug_val", info, {"val": w}))
		else:
			_kroniek(regels.kies("terug", {"naam": info.naam, "held": _held_naam(info)}))
	else:
		var naam := _vrije_naam()
		helden_nr += 1
		info = {"naam": naam, "bezoeken": 0, "wrok": "",
			"kleur": KLEUREN[rng.randi_range(0, KLEUREN.size() - 1)], "hoed": HOEDEN[rng.randi_range(0, HOEDEN.size() - 1)],
			"taai": rng.randi_range(0, 1), "hoed_nr": rng.randi_range(0, 9)}   # alle tien hoeden (Bram 22:40)
		if demo:
			info["hoed_nr"] = DEMO_HOEDEN[demo_hoed_i % DEMO_HOEDEN.size()]
			demo_hoed_i += 1
		# heldensoort en trek (Bram, versie 1): niet in de vaste stappen van het begin, en de eerste 10 helden gewoon
		var soort_h := ""
		var trek_h := ""
		if stap == "":
			soort_h = SOORT.kies(helden_nr, rng)
			trek_h = SOORT.kies_trek(helden_nr, rng)
		elif stap == "vluchten" and demo and DEMO_BARD:
			soort_h = "bard"
		if soort_h != "":
			info["soort_held"] = soort_h
		if trek_h != "":
			info["trek"] = trek_h
		if lied_helden > 0 and stap != "vluchten":
			# hij komt door het lied van de bard: dat moet je zien, dus een gebeurtenis die voorgaat en niet vervalt
			# (Sanne toets 9, punt 3). lied_helden telt pas af in _process als deze held er is.
			info["lied_held"] = true
			_kroniek(regels.kies("binnen_lied", {"naam": naam}), false, "binnen_lied")
		elif naam.ends_with(" II") or naam.ends_with(" III"):
			_kroniek(regels.kies("naamgenoot", {"naam": naam, "oud": naam.split(" ")[0]}), true)
		elif soort_h != "":
			_kroniek(regels.kies("binnen_" + soort_h, {"naam": naam}), true)   # de soort zie je meteen ("Sir Odo clanks in.")
		elif trek_h != "":
			_kroniek(regels.kies("binnen_" + trek_h, {"naam": naam}), true)    # de drie nieuwe trekken zie je alleen hier
		else:
			_kroniek(regels.kies("binnen", {"naam": naam}), true)
	match stap:
		"vallen": info["moet_vallen"] = true
		"terug":
			# de wrok krijgt een afloop: hij komt terug voor de put en valt erin, of Gloop eet hem (Sanne toets 6, punt 1).
			# Ook buiten de demo, maar alleen in de eerste tien minuten (stap "terug" in BEGIN); daarna kan een terugkomer
			# weer ontsnappen en groeit zijn wrok.
			if String(info.get("wrok", "")).begins_with("the "):
				info["moet_vallen"] = true     # eerste verdediging op zijn pad is zijn vijand: hij loopt eerst naar de put
			else:
				info["moet_opgegeten"] = true
		"vluchten":
			info["moet_vluchten"] = true
			begin_vlucht = String(info.naam)
		"opgegeten", "opgegeten2":
			info["moet_opgegeten"] = true
			if stap == "opgegeten2" and demo:
				# Sanne toets 7, punt 1: de minuut eindigt met een clou. Zij kwam rond 43 s binnen en liep 16 s naar Gloop
				# (hap op 59,8 s, niet te zien); 1.5 gaf de hap op 55,7 s (run 42735021882), 1.8 rond 53,5 s, met regel en hoed op de toren
				info["snelheid"] = 1.8
				info["demo_clou"] = true   # haar hoed op de toren krijgt altijd een regel (controleur kan-punt 1)
			if stap == "opgegeten":
				opgegeten_t = t
				if demo:
					demo_hoed_i -= 1   # hij krijgt de kroon; zijn plek in DEMO_HOEDEN gaat naar de volgende (pan voor de Hoard-Toucher)
				# de eerste hoed op Gloop moet in één beeld lezen: de kroon (index 4 in Mila's held_hoeden.png),
				# zolang held.gd nog maar 4 hoeden kent de paarse puntmuts (index 1) (Sanne toets 4, punt 2)
				var tops: Array = held_script.get_script_constant_map().get("HOED_TOP", [])
				info["hoed_nr"] = 4 if tops.size() >= 10 else 1
		"doorlopen":
			info["moet_doorlopen"] = true
			if demo:
				info["snelheid"] = 1.4   # held.gd (Bram 23:30): raakt de schat binnen de minuut en rent nog weg
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
	AFLOOP.held_klaar(self, _held, uitkomst, info)

func _process(delta: float) -> void:
	t += delta
	# Gloop plat of weer op: een regel in de kroniek (Sanne toets 2, punt 7).
	if slijm and slijm.has_method("kan_vechten"):
		var nu_plat: bool = not slijm.kan_vechten()
		if nu_plat != slijm_plat:
			slijm_plat = nu_plat
			# laag: toestand, geen gebeurtenis. Wacht "plat" nog als hij al weer op is, dan geen van beide (controleur ronde 3)
			var oud_plat := -1
			for i in wachtrij.size():
				if String(wachtrij[i].soort) == "plat":
					oud_plat = i
			if not nu_plat and oud_plat >= 0:
				wachtrij.remove_at(oud_plat)
			else:
				_kroniek(regels.kies("plat" if nu_plat else "op", {"bewoner": _bewoner()}), true, "plat" if nu_plat else "op")
	var helden := 0
	for w in wezens.get_children():
		if w.has_method("is_held"):
			helden += 1
			# Hoard-Toucher: de regel komt op het moment dat hij de schat aanraakt, niet pas als hij ontsnapt (toets 5)
			var hi = w.get("info")
			# (kijk naar "wat": "hoard_toucher" blijft in de save staan voor de bijnaam, dus een terugkomer heeft hem al)
			if hi is Dictionary and String(hi.get("wat", "")).begins_with("touched") and not hi.has("schat_gemeld"):
				hi["schat_gemeld"] = true
				_kroniek(regels.kies("schat", {"naam": hi.get("naam", "")}))
			# slaapkop (Bram, versie 1): zijn dutje een lage regel, zoals binnenkomst (hij ligt er 4 s, de regel mag wachten)
			if hi is Dictionary and bool(hi.get("dutje", false)) and not hi.has("dutje_gemeld"):
				hi["dutje_gemeld"] = true
				_kroniek(regels.kies("dutje", {"naam": hi.get("naam", "")}), true)
	_toon()
	KAARTJE.tik(self)
	if demo:
		KAARTJE.demo_stap(self)
	if tekst.goud != hol.goud:
		tekst.zet(kroniek, hol.goud)
		if kaart_soort != "":
			KAARTJE.ververs(self)
	if t >= volgende_held and helden < 3:
		var begin := _begin_stap() != ""
		if _nieuwe_held():
			# ritme: gemiddeld een held per ±50 s (balans.md), in de eerste tien minuten ±40 s;
			# in de demo sneller zodat de film van een minuut iets laat zien
			volgende_held = t + ((rng.randf_range(5.0, 7.0) if begin else rng.randf_range(6.0, 9.0)) if demo else (rng.randf_range(35.0, 45.0) if begin else rng.randf_range(40.0, 60.0)))
			# na het lied van een bard: de volgende helden komen 8 tot 20 s na elkaar (Bram 02:30); in de demo blijft het
			# eigen snelle ritme staan (dat is al korter), alleen de teller loopt af
			if lied_helden > 0:
				lied_helden -= 1
				if lied_helden > 0 and not demo:
					volgende_held = t + rng.randf_range(8.0, 20.0)
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
		if KAARTJE.klik(self, event.position):
			log_regel("HOL klik op %s: kaartje" % event.position)
			return
		var p: Vector2 = (event.position - hol.position) / schaal
		var wat: String = hol.klik(p)
		log_regel("HOL klik op %s: %s" % [event.position, wat if wat != "" else "niets"])
	elif event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_RIGHT:
		zet_hoogte(HOOGTES[(HOOGTES.find(hoogte) + 1) % HOOGTES.size()] if HOOGTES.has(hoogte) else 120)
	elif event is InputEventMouseMotion and not tekst.hover:
		tekst.hover = true
		tekst.queue_redraw()
		_muis_vlak(true)

func _notification(what: int) -> void:
	if what == NOTIFICATION_WM_MOUSE_EXIT and tekst:
		tekst.hover = false
		tekst.queue_redraw()
		_muis_vlak(kaart_soort != "")   # een open kaartje blijft de muis vangen
	elif what == NOTIFICATION_WM_CLOSE_REQUEST:
		KAARTJE.dicht(self)   # een wachtende koopregel komt eerst in de kroniek, dan bewaren (controleur kan-punt 1)
		bewaar()

# Welk deel van het venster de muis vangt. Normaal alleen het hol; bij hover ook het paneel met drie regels (L-vorm),
# want dat reikt bij 96 px tot boven het maaiveld en zou anders meteen weer dichtklappen (controleur 00:30). Lucht en gras
# naast het paneel laten klikken altijd door.
var vangt_y := 0
func _muis_vlak(paneel: bool) -> void:
	var w := DisplayServer.window_get_size()
	var y := float(vangt_y)
	var vlak := PackedVector2Array([Vector2(0, y), Vector2(w.x, y), Vector2(w.x, w.y), Vector2(0, w.y)])
	if paneel and tekst and tekst.has_method("hover_vak"):
		var r: Rect2 = tekst.hover_vak()
		var top := clampf(r.position.y, 0.0, y)
		var links := clampf(r.position.x, 0.0, float(w.x))
		if top < y:
			vlak = PackedVector2Array([Vector2(0, y), Vector2(links, y), Vector2(links, top), Vector2(w.x, top),
				Vector2(w.x, w.y), Vector2(0, w.y)])
	DisplayServer.window_set_mouse_passthrough(vlak)

# Andere hoogte: bewaar spel en instelling, dan de strook opnieuw opbouwen (schaal en venster hangen ervan af).
func zet_hoogte(h: int) -> void:
	log_regel("HOL hoogte %d -> %d" % [hoogte, h])
	KAARTJE.dicht(self)
	bewaar()
	var f := FileAccess.open(INSTELLING, FileAccess.WRITE)
	if f:
		f.store_string(JSON.stringify({"hoogte": h}))
		f.close()
	get_tree().reload_current_scene()

func bewaar() -> void:
	OPSLAG_M.bewaar(self)

func laad() -> void:
	OPSLAG_M.laad(self, BEGIN)
