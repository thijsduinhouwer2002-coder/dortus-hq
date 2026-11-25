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
const RITME := preload("res://kern/ritme.gd")   # wanneer de volgende held komt; graven in de demo-film
const BINNENKOMST := preload("res://kern/binnenkomst.gd")   # een nieuwe held of terugkomer binnen laten
const KAARTJE := preload("res://kern/kaartje.gd")
const DEMO_EINDE := preload("res://kern/demo_einde.gd")   # gratis Steam-demo: na 2 uur stopt alleen groeien
const PROEF := preload("res://kern/proef.gd")       # startargumenten, proeven en winkelmomenten
const MUISVLAK := preload("res://kern/muisvlak.gd")
const VENSTER := preload("res://kern/venster.gd")   # venster plaatsen, invoer, hoogte, stoppen (issue #24)   # welk deel van het venster de muis vangt
const BOEK := preload("res://systemen/boek.gd")         # het Heldenboek (Bram 03:45); stap 1: bijhouden, opslaan, regel
const VOORTGANG := preload("res://systemen/voortgang.gd")   # graafbonus (Sanne 16 nov 21:00)
# Hoogte van de strook, in het spel te kiezen in het rechtsklikmenu of het systeemvak (96, 120, 160), bewaard los van het spel
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
var hoogte_gekozen := false   # bewaard of hoogte=<n>; anders kiest kern/proef.gd de stand bij de schaal
var proef_dpi := 0            # dpi=<n>: doen alsof het scherm n dpi heeft (alleen om de eerste start te toetsen)
var schaal := 3
var duur := 0.0
var logpad := ""
var demo := false
var film := false
var vers := false
var proef_fps := 10          # kern/beeldtempo.gd GEWOON; met fps=<n> vast op n (CPU-proef)
var fps_vast := false
var moment_tot := -1.0
var proef_graaf := false     # graaf_proef=1: vier kamers stil in de beelden van het graafmoment, om op te keuren (Daan 14 nov)
var proef_royal := false     # royal_proef=1: Gloop meteen Royal (niveau 3), alleen om Royal in 3D te keuren (Bram 14 nov)
var proef_put := 0           # put_proef=<1-3>: de put meteen op die stap, alleen om de put in 3D te keuren (Olaf 14 nov)
var proef_moment := ""       # moment=hap|val|munt: zet het spel stil op het mooiste moment voor de winkelschermen (Bram 15 nov, Mila en Olaf)
var moment_gemeld := false   # "HOL moment vast <m>" staat in de log (de winkel-workflow maakt dan zijn beelden)
var proef_spuug := 0          # spuug_proef=<1-3>: Gloop blijft in een spuugmoment staan, alleen om spugen in 3D te keuren (Bram 15 nov)
var proef_plat := false      # plat_proef=1: Gloop plat zonder regel (twee keer al gemeld), alleen om te keuren (Daan 16 nov 20:35)
var proef_laars := false     # laars_proef=1: de laars ligt vast naast Gloop, alleen om de 3D-laars te keuren (Bram 14 nov)
const FIGUUR := 1.15          # Gloop en helden 1,15 keer zo groot getekend, voetpunt gelijk, hol gelijk (Thijs 15 nov punt 2 "leesbaar op 120 px", keuze Daan)
var proef_figuur := FIGUUR   # figuur=<factor> blijft als startargument om andere maten te keuren; 1.0 is de oude maat
var proef_deco := false      # deco_proef=1: vaste versiering in de gang (3 vloerstukken en hangstukken), alleen om op te keuren (Daan 14 nov)
var proef_uit3d: PackedStringArray = []   # uit3d=helden,hol,slijm: dat deel zonder 3D, alleen voor de CPU-proef (demolijst 2, Olaf 14 nov)
var proef_zaad := 0           # zaad=<n>: zelfde volgorde van heldsoorten (strook.rng); uitkomst per held blijft los (held.gd), dus ongeveer gelijk (proef)
var proef_koper_graaf := true   # koper=2: koopt wel, graaft niet, om graven en kopen uit elkaar te halen (Sanne 16 nov 20:10)
var proef_koper := false     # koper=1: koopt elke upgrade zodra het kan en graaft zoals de demo, voor de bovengrens (Iris keuring 7, Olaf 16 nov)
var volgende_koop := 3.0
var proef_drukte := false    # drukte=1: helden elke 5 tot 8 s (hooguit 3 tegelijk), alleen voor de winkelopname week (Mila 16 nov, punt 3)
var meet_t := 0.0             # elke 10 s: hoeveel beelden echt getekend (alleen met log=)
var meet_beelden := 0
var zicht_was := false        # Iris keuring 6: log 'HOL zicht' als er een held in beeld komt of de laatste weg is (e2e/ritme_meting.py)
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
# Bram 16 nov (Fenna, onderscheid van Hats; hoofdchat 08:05 NL): "opgegeten" vóór "vluchten", zodat je in de eerste
# 30 s zowel de stekels als de eerste hoed op de toren ziet (dat heeft de concurrent niet). Kort gat erna: kern/ritme.gd.
const BEGIN := ["vallen", "opgegeten", "vluchten", "terug", "doorlopen"]
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
var holbord: Node2D = null   # systemen/holbord.gd, het bordje met het hol-niveau
var rij := 0   # hol-niveaus die bij de ingang wachten (hol_niveau.gd weg)
var rij_t := 0.0   # open seconden sinds het laatste niveau uit de rij
var optocht := {}   # plan van de optocht na weg zijn (hol_niveau.gd optocht), niet bewaard
var namen_recent: Array = []   # helden van deze speelbeurt die een regel kunnen krijgen (wachtrij.gd een_per_held, moet Daan 23:30 b)
var faam := 0   # gevangen helden, ook als je weg was; hol-niveau (systemen/hol_niveau.gd, Sanne voortgang.md spoor 1)
var gevallen_namen := {}   # naam -> hoe vaak gevallen; die naam komt daarna als "Kees II" (Sanne toets 2, punt 4)
var slijm
var slijm_plat := false
var reeks := 0                # vangsten op rij zonder vlucht (kern/afloop.gd, niet bewaard)
var geluid                   # speelt de geluidjes af (kern/geluid.gd)
var klap                     # laag met klap-ster, "+9" en "x3" bij een vangst (kern/klap.gd)
var zelf_gegraven := 0       # cellen die de speler zelf groef (gang, kamer, ingang), in de save; graafbonus in voortgang.gd
var recente_namen: Array = []   # voornamen van de laatste nieuwe helden, niet in de save (Sanne 17 nov 16:50 punt 3)
var naamgenoot_gezien := {}  # voornamen die deze speelbeurt al een naamgenoot-regel kregen (Sanne 16 nov 22:00)
var laars_namen := {}   # volle namen van helden wier valregel een laars noemde (Iris 19 nov, laarsgrap)
var naamgenoot_laatst := -1000.0   # t van de laatste naamgenoot-regel, hooguit één per 5 min (Iris keuring 23 punt 1)
var plat_keer := 0           # hoe vaak "flat" deze speelbeurt in de rij ging (hooguit WACHTRIJ.PLAT_KEER, Daan 16 nov 20:35)
var plat_gemeld := false     # staat (of wacht) er een "flat" voor de huidige keer plat; alleen dan komt "up again"
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
			hoogte_gekozen = true
		if inst is Dictionary and inst.get("stil", false):
			AudioServer.set_bus_mute(0, true)   # geluid uit via het systeemvak, bewaard
	PROEF.lees_argumenten(self)   # alle startargumenten (hoogte, duur, log, proeven): kern/proef.gd
	PROEF.kies_begin_hoogte(self)   # niets gekozen: hoogte naar de schaal van het scherm (kern/proef.gd)
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
	VENSTER.plaats(self, scherm)   # venster, icoon, app-balk (kern/balk.gd) en systeemvak (kern/systeemvak.gd)
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
	hol.deco_proef = proef_deco
	if "hol" in proef_uit3d:
		hol.met_3d = false
	if "helden" in proef_uit3d:
		load("res://systemen/held_beeld.gd").met_3d = false
	hol.maak(int(scherm.size.x / schaal))
	wezens = Node2D.new()
	wezens.name = "Wezens"
	# vleermuis (Bram 16 nov, Mila punt 4b) vóór Wezens: de helden lopen voor hem langs; zonder blad doet hij niets
	var vleermuis := Node2D.new()
	vleermuis.set_script(load("res://systemen/vleermuis.gd"))
	vleermuis.name = "Vleermuis"
	hol.add_child(vleermuis)
	# bordje met het hol-niveau (Mila 16 nov 16:20, plek Daan keus A), ook vóór Wezens; zonder blad doet het niets
	holbord = Node2D.new()
	holbord.set_script(load("res://systemen/holbord.gd"))
	holbord.name = "Holbord"
	hol.add_child(holbord)
	hol.add_child(wezens)
	vleermuis.zet(hol, wezens)
	holbord.zet(self, hol)
	# Brams slijm (Gloop, gaat nooit dood) als die er is, anders de stand-in
	slijm = Node2D.new()
	slijm.set_script(load("res://systemen/slijm.gd") if ResourceLoader.exists("res://systemen/slijm.gd") else load("res://kern/standin_slijm.gd"))
	wezens.add_child(slijm)
	slijm.scale = Vector2.ONE * proef_figuur   # oorsprong is zijn voetpunt: toren, hoedenberg, laars en wolkje schalen mee
	if "slijm" in proef_uit3d and "met_3d" in slijm:
		slijm.met_3d = false
	slijm.zet(hol, 10)   # plek volgt hieronder, na leg_aan
	PROEF.na_slijm(self)
	if demo:
		volgende_held = 0.5
	if demo and "plat_s" in slijm:
		slijm.plat_s = 9.0   # demo: Gloop ±9 s plat in plaats van 30, net als de helden in de demo sneller komen (Sanne toets 2, punt 1)

	VENSTER.lagen(self, scherm)   # tekst en klap over het hol
	# het hol groeit niet onder het tekstvak: de schat staat er rechts tegenaan, het hol groeit naar links
	hol.max_kol = int((scherm.size.x - tekst.vak_breedte() - 40) / (HOL.KOL * schaal)) - 1
	hol.leg_aan(hol.max_kol)
	if proef_graaf:
		hol.graaf_proef = true
		hol.zet_graaf_proef()
	slijm.position = hol.cel_naar_pos(Vector2i(hol.schat_kol - 2, 0))
	regels = REGELS.new()
	regels.rng = rng

	hol.goud = KAARTJE.START_GOUD   # nieuw spel; laad() zet het goud uit de save
	if not vers:
		laad()
	PROEF.na_laad(self)
	if demo:
		hol.goud = KAARTJE.DEMO_GOUD
	if kroniek.is_empty():
		_kroniek("Your hole is open. Heroes will come.")
	DEMO_EINDE.bij_start(self)
	hol.gegraven.connect(func(cel):
		zelf_gegraven += 1   # graafbonus (Sanne 16 nov 21:00): alleen wat de speler graaft, de begingang telt niet
		log_regel("HOL gegraven kolom %d (zelf %d, graafbonus %d)" % [cel.x, zelf_gegraven, VOORTGANG.graafbonus(zelf_gegraven)]))
	VENSTER.log_start(self, scherm, spel_h)

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
	return BINNENKOMST.begin_stap(self)

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
			# laag: toestand, geen gebeurtenis; welke regel (of geen) beslist wachtrij.gd plat_wissel (Daan 16 nov 20:35)
			var ps: String = WACHTRIJ.plat_wissel(self, nu_plat)
			if ps != "":
				_kroniek(regels.kies(ps, {"bewoner": _bewoner()}), true, ps)
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
	if logpad != "" and (helden > 0) != zicht_was:
		zicht_was = helden > 0
		log_regel("HOL zicht %.1f %d" % [t, helden])
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
	var doel := KAARTJE.doel_regel(self)   # Iris 16 nov: volgend doel zonder klik; alleen opnieuw tekenen als het verandert
	if holbord != null and holbord.hover:
		doel = holbord.hover_tekst()   # muis op het bordje: de hover van het hol-niveau in de kopregel (Sanne spoor 1)
	if tekst.goud != hol.goud or tekst.doel != doel:
		tekst.doel = doel
		tekst.zet(kroniek, hol.goud)
		if kaart_soort != "":
			KAARTJE.ververs(self)
	RITME.tik_held(self, helden)
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
			PROEF.kijk_val(self, w)   # winkelbeeld moment=val (alleen met het startargument)
	PROEF.tik(self)
	if demo or (proef_koper and proef_koper_graaf):
		RITME.tik_demo_graaf(self)
	if proef_koper:
		RITME.tik_koper(self)
	if t >= volgende_opslag:
		volgende_opslag = t + 30.0
		bewaar()
	if duur > 0.0 and t > duur:
		log_regel("HOL einde na %d s, fps=%d, goud=%d, terugkomers=%d" % [int(duur), Engine.get_frames_per_second(), hol.goud, terugkomers.size()])
		bewaar()
		get_tree().quit()

# Welk deel van het venster de muis vangt: kern/muisvlak.gd (uitleg staat daar). Hier alleen de toestand.
var vangt_y := 0
var vlak_paneel := false
var vlak_gloop := Vector3i(-1, -1, -1)   # x links, x rechts, bovenkant (venster-pixels) van de bult boven Gloop
var lucht_gemeld := false
var balk_vol := false   # met de app-balk vangt het venster overal en laat hol-balk.exe de muis door (kern/muisvlak.gd)
var balk_pad := ""      # balk=<pad> of balk=0 (kern/balk.gd)
var proef_vak := ""     # vak=pauze|geluid|stop (toets van het systeemvak)
func _muis_vlak(paneel: bool) -> void:
	MUISVLAK.zet(self, paneel)

func muis_vlak_punten(paneel: bool) -> PackedVector2Array:
	return MUISVLAK.punten(self, paneel)

func gloop_bult() -> Vector3i:
	return MUISVLAK.gloop_bult(self)

# hol_vast.gd heeft de bovenrand opnieuw gemeten
func rand_veranderd() -> void:
	_muis_vlak(vlak_paneel)

# Invoer, venstermeldingen, hoogte en stoppen: kern/venster.gd
func _input(event: InputEvent) -> void:
	VENSTER.invoer(self, event)

func _notification(what: int) -> void:
	VENSTER.melding(self, what)

func zet_hoogte(h: int) -> void:
	VENSTER.zet_hoogte(self, h)

func bewaar_instelling(sleutel: String, waarde) -> void:
	VENSTER.bewaar_instelling(self, sleutel, waarde)

func stoppen() -> void:
	VENSTER.stoppen(self)

func bewaar() -> void:
	OPSLAG_M.bewaar(self)

func laad() -> void:
	OPSLAG_M.laad(self, BEGIN)

