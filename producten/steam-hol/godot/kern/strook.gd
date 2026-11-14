extends Node2D
# Kern van Het Hol (Olaf): de strook boven de taakbalk.
# - hoogte instelbaar (standaard 120 px, 96 tot 160), over de hele breedte, net boven de taakbalk
# - alleen de strook vangt klikken, de rest laat ze door
# - zuinig: 10 fps (20 tijdens een moment, kern/beeldtempo.gd) en alleen tekenen wat beweegt
# - geen kaartjes over andere vensters: alle tekst staat klein in de strook
# Argumenten na "--": hoogte=120 duur=60 log=<pad> demo=1 film=1 vers=1 steamdemo=1 demo_einde=<s>

const HOL := preload("res://hol/hol.gd")
const TEKST := preload("res://kern/tekst.gd")
const OPSLAG_M := preload("res://kern/opslag.gd")
const NAMEN_M := preload("res://kern/namen.gd")
const WACHTRIJ := preload("res://kern/wachtrij.gd")
const AFLOOP := preload("res://kern/afloop.gd")
const BEELDTEMPO := preload("res://kern/beeldtempo.gd")
const BINNENKOMST := preload("res://kern/binnenkomst.gd")   # een nieuwe held of terugkomer binnen laten
const KAARTJE := preload("res://kern/kaartje.gd")
const DEMO_EINDE := preload("res://kern/demo_einde.gd")   # gratis Steam-demo: na 2 uur stopt alleen groeien
const BOEK := preload("res://systemen/boek.gd")         # het Heldenboek (Bram 03:45); stap 1: bijhouden, opslaan, regel
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
var proef_fps := 10          # kern/beeldtempo.gd GEWOON; met fps=<n> vast op n (CPU-proef)
var fps_vast := false
var moment_tot := -1.0
var proef_zaad := 0           # zaad=<n>: zelfde volgorde van heldsoorten (strook.rng); uitkomst per held blijft los (held.gd), dus ongeveer gelijk (proef)
var meet_t := 0.0             # elke 10 s: hoeveel beelden echt getekend (alleen met log=)
var meet_beelden := 0
var steamdemo := false        # de gratis Steam-demo (feature steamdemo of argument steamdemo=1)
var demo_grens := 7200.0      # demo_einde=<s> voor de toets
var speeltijd_s := 0.0        # open tijd, in de save (kern/demo_einde.gd)
var eerste_koop_gemeld := false   # demolijst 3: logregel "HOL eerste koop mogelijk" (kern/kaartje.gd tik)

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
var pensioen_namen: Array = []   # wie vluchtte en nooit terugkomt (hooguit 5, oudste voor); bij openen een grapje (Bram 04:35)
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
			"demo_einde": demo_grens = maxf(1.0, float(kv[1]))
			"fps":
				proef_fps = clampi(int(kv[1]), 8, 30)   # alleen voor de CPU-proef (demolijst 2), vast
				fps_vast = true
			"zaad": proef_zaad = int(kv[1])
	steamdemo = DEMO_EINDE.is_demo(OS.get_cmdline_user_args())
	rng.seed = 7 if demo else (proef_zaad if proef_zaad != 0 else int(Time.get_unix_time_from_system()))
	if not film:
		Engine.max_fps = proef_fps
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

	hol.goud = KAARTJE.START_GOUD   # nieuw spel; laad() zet het goud uit de save
	if not vers:
		laad()
		bewaar()   # meteen bewaren, anders telt dezelfde weg-tijd na een harde afsluiting nog een keer
	if demo:
		hol.goud = KAARTJE.DEMO_GOUD
	if kroniek.is_empty():
		_kroniek("Your hole is open. Heroes will come.")
	DEMO_EINDE.bij_start(self)
	hol.gegraven.connect(func(cel): log_regel("HOL gegraven kolom %d" % cel.x))
	log_regel("HOL start hoogte=%d schaal=%d spelpixels=%dx%d venster=%s pos=%s held=%s" % [hoogte, schaal,
		int(scherm.size.x / schaal), spel_h, DisplayServer.window_get_size(), DisplayServer.window_get_position(), held_script.resource_path])

# De kroniek-wachtrij (welke regel wanneer): kern/wachtrij.gd. Hier alleen de toestand.
var wachtrij: Array = []        # [{r, binnen, sinds}]
var regel_sinds := -100.0       # wanneer de getoonde regel kwam
var regel_binnen := false       # is de getoonde regel een binnenkom-regel
var regel_nu: Dictionary = {}   # de getoonde regel zelf (wachtrij.gd: te kort gestaan, dan één keer terug)

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
	return BINNENKOMST.nieuwe_held(self)

func _held_klaar(_held, uitkomst: String, info: Dictionary) -> void:
	AFLOOP.held_klaar(self, _held, uitkomst, info)

func _process(delta: float) -> void:
	t += delta
	# Gloop groeit, krijgt een hoed of loopt: de bult in het muisvlak mee laten gaan (alleen als hij echt verandert)
	if slijm and hol and int(t * 2.0) != int((t - delta) * 2.0) and gloop_bult() != vlak_gloop:
		_muis_vlak(vlak_paneel)
	DEMO_EINDE.tik(self, delta)
	BEELDTEMPO.tik(self)
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
	if logpad != "":
		meet_t += delta
		if meet_t >= 10.0:
			meet_t = 0.0
			var nu_b := Engine.get_frames_drawn()
			var vast_keer: int = hol.vast.keer if hol.vast != null else -1
			log_regel("HOL meting t=%d beelden=%d helden=%d hol_vast=%d" % [int(t), nu_b - meet_beelden, helden, vast_keer])
			meet_beelden = nu_b
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
		if DEMO_EINDE.weiger(self, "graven (film)"):
			pass
		elif int(t / 9.0) % 2 == 0 and k >= 1:
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
		if DEMO_EINDE.weiger(self, "klik in het hol"):
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

# Welk deel van het venster de muis vangt. Normaal het hol plus wat erboven getekend staat; bij hover ook het paneel
# met drie regels, want dat reikt bij 96 px tot boven het maaiveld en zou anders meteen weer dichtklappen
# (controleur 00:30). Lege lucht laat klikken altijd door naar het venster erachter.
# Let op (Bram 14 nov 02:35, Godot 4.3 DisplayServer.xml): op Windows tekent het venster NIETS buiten dit vlak. Daarom
# volgt het vlak de bovenrand van gras, plantjes en ingang (hol_vast.gd `rand`, één keer gemeten na elk nieuw vast
# beeld) en een bult boven Gloop met zijn hoedentoren (rust-hoogte, zodat het vlak niet bij elke wip verandert).
# Besluit Olaf 14 nov 03:30: gras en toren zichtbaar, de paar spelpixels gras vangen dan ook de muis.
var vangt_y := 0
var vlak_paneel := false
var vlak_gloop := Vector3i(-1, -1, -1)   # x links, x rechts, bovenkant (venster-pixels) van de bult boven Gloop
var lucht_gemeld := false
func _muis_vlak(paneel: bool) -> void:
	vlak_paneel = paneel
	DisplayServer.window_set_mouse_passthrough(muis_vlak_punten(paneel))

# De punten van het vlak (los, voor de toetsen). Per pixelkolom een bovenkant, gelijke stukken samengevoegd.
func muis_vlak_punten(paneel: bool) -> PackedVector2Array:
	var w := DisplayServer.window_get_size()
	var tops := PackedInt32Array()
	tops.resize(w.x)
	tops.fill(vangt_y)
	var boven := vangt_y - HOL.OPP * schaal
	var r: PackedInt32Array = hol.vast.rand if hol != null and hol.vast != null else PackedInt32Array()
	for x in mini(r.size(), w.x):
		tops[x] = mini(tops[x], boven + r[x])
	vlak_gloop = gloop_bult()
	for x in range(maxi(0, vlak_gloop.x), mini(w.x, vlak_gloop.y)):
		tops[x] = mini(tops[x], vlak_gloop.z)
	if paneel and tekst and tekst.has_method("hover_vak"):
		var pr: Rect2 = tekst.hover_vak()
		var top := int(clampf(pr.position.y, 0.0, float(vangt_y)))
		for x in range(int(clampf(pr.position.x, 0.0, float(w.x))), w.x):
			tops[x] = mini(tops[x], top)
	var vlak := PackedVector2Array([Vector2(0, w.y)])
	var x0 := 0
	for x in range(1, w.x + 1):
		if x == w.x or tops[x] != tops[x0]:
			vlak.append(Vector2(x0, tops[x0]))
			vlak.append(Vector2(x, tops[x0]))
			x0 = x
	vlak.append(Vector2(w.x, w.y))
	if not lucht_gemeld and r.size() > 0:
		lucht_gemeld = true
		# voor de Windows-stap "Klikken door de lucht": een plek waar echt lucht is (4 px onder de bovenrand)
		var vrij := -1
		for x in range(200, mini(w.x, r.size())):
			if tops[x] > 4 + 2 * schaal:
				vrij = x
				break
		log_regel("HOL muisvlak %d punten, lucht vrij op x=%d" % [vlak.size(), vrij])
	return vlak

# Bult boven Gloop: van de bovenkant van zijn toren (in rust) tot het maaiveld, zo breed als hij met hoeden is.
func gloop_bult() -> Vector3i:
	if slijm == null or hol == null or not slijm.has_method("hoogste_punt_rust"):
		return Vector3i(-1, -1, -1)
	var boven := vangt_y - HOL.OPP * schaal
	var top := int(floor((slijm.position.y + float(slijm.hoogste_punt_rust()) - 1.0) * schaal)) + boven
	var x := int(hol.position.x + slijm.position.x * schaal)
	return Vector3i(x - 11 * schaal, x + 11 * schaal, clampi(top, 0, vangt_y))

# hol_vast.gd heeft de bovenrand opnieuw gemeten
func rand_veranderd() -> void:
	_muis_vlak(vlak_paneel)

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
