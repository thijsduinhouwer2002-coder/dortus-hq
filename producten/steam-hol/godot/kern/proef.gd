# Het Hol: startargumenten, proeven en winkelmomenten (Olaf 15 nov, uit kern/strook.gd gehaald; regel: bestand onder ±400).
# Alleen statische functies met de strook als eerste argument (`s`), net als wachtrij.gd en afloop.gd.
# De toestand (proef_*, moment_gemeld, hoogte, duur, ...) blijft in strook.gd.
extends RefCounted

# moment=val (Bram 15 nov 19:30): de held staat stil boven de stekels, met het uitroepteken, net voor hij wegzakt.
# De munten komen pas na de hele val (afloop.gd), dus held en munten samen in één beeld bestaat niet in het spel.
const MOMENT_VAL_T := 0.12   # kan Daan 15 nov 22:55: bovenin de wip, voeten los, held in de stand schrik (held_beeld VAL_RECHT 0,2); op 15 fps stil bij 0,133. Daan 15 nov 21:45: proef op 0,2 (op 0,25 leest de held als klodder; 0,38 dekte de stekels af)

# Argumenten van de workflow (na `--`) gaan voor de bewaarde instelling.
static func lees_argumenten(s) -> void:
	for a in OS.get_cmdline_user_args():
		var kv: PackedStringArray = a.split("=", true, 1)
		if kv.size() < 2:
			continue
		match kv[0]:
			"hoogte":
				s.hoogte = clampi(int(kv[1]), 96, 160)
				s.hoogte_gekozen = true
			"dpi": s.proef_dpi = clampi(int(kv[1]), 48, 480)   # dpi=<n>: doen alsof het scherm n dpi heeft (eerste start), om de grote stand op de runner te toetsen
			"duur": s.duur = float(kv[1])
			"log": s.logpad = kv[1]
			"balk": s.balk_pad = kv[1]   # balk=<pad naar hol-balk.exe> of balk=0 zonder app-balk (kern/balk.gd, issue #24)
			"vak": s.proef_vak = kv[1]   # vak=pauze|geluid|stop: doen alsof die regel in het systeemvak gekozen is (toets)
			"demo": s.demo = kv[1] == "1"
			"film": s.film = kv[1] == "1"
			"vers": s.vers = kv[1] == "1"
			"demo_einde": s.demo_grens = maxf(1.0, float(kv[1]))
			"fps":
				s.proef_fps = clampi(int(kv[1]), 8, 30)   # alleen voor de CPU-proef (demolijst 2), vast
				s.fps_vast = true
			"zaad": s.proef_zaad = int(kv[1])
			"uitleg_klik": s.proef_uitleg_klik = maxf(0.0, float(kv[1]))
			"koper":   # Iris keuring 7: speler die alles koopt zodra het kan; koper=2 koopt alleen en graaft niet (Sanne 16 nov 20:10)
				s.proef_koper = kv[1] == "1" or kv[1] == "2"
				s.proef_koper_graaf = kv[1] == "1"
			"koper_wacht": s.set_meta("koper_wacht", maxf(0.0, float(kv[1])))   # bedenktijd van de koper in s (film Iris #7)
			"drukte": s.proef_drukte = kv[1] == "1"   # Mila 16 nov: drie helden tegelijk in de winkelopname week
			"deco_proef": s.proef_deco = kv[1] == "1"
			"royal_proef": s.proef_royal = kv[1] == "1"
			"graaf_proef": s.proef_graaf = kv[1] == "1"
			"laars_proef": s.proef_laars = kv[1] == "1"
			"plat_proef": s.proef_plat = kv[1] == "1"   # Daan 16 nov 20:35: Gloop plat zonder regel, om te keuren of hij zonder tekst leest
			"spuug_proef": s.proef_spuug = clampi(int(kv[1]), 0, 3)
			"moment": s.proef_moment = kv[1] if kv[1] in ["hap", "val", "munt"] else ""
			"put_proef": s.proef_put = clampi(int(kv[1]), 0, 3)
			"figuur": s.proef_figuur = clampf(float(kv[1]), 0.5, 2.0)
			"uit3d": s.proef_uit3d = kv[1].split(",", false)

# Eerste start (Olaf 16 nov, voor de speeltest van Thijs): het spel rekent in echte schermpixels. Op een laptop
# met schaal 125% of meer is 120 px dan klein (Gloop ±48 schermpixels, op 150% oogt dat als 32). Zonder bewaarde
# hoogte en zonder hoogte=<n> kiezen we daarom de stand die bij de schaal past. Het rechtsklikmenu blijft wisselen en bewaart.
static func hoogte_voor_dpi(dpi: int) -> int:
	return 160 if dpi >= 120 else 120   # 96 dpi = 100%: 120; 120 dpi = 125%: 120 x 1,25 = 150, dichtst bij 160

static func kies_begin_hoogte(s) -> void:
	if s.hoogte_gekozen:
		return
	var dpi: int = s.proef_dpi if s.proef_dpi > 0 else DisplayServer.screen_get_dpi()
	s.hoogte = hoogte_voor_dpi(dpi)
	s.log_regel("HOL eerste start (geen gekozen hoogte) dpi=%d hoogte=%d" % [dpi, s.hoogte])

# Na het neerzetten van Gloop: laars, spugen en de winkelmomenten aanzetten.
static func na_slijm(s) -> void:
	var slijm = s.slijm
	var hol = s.hol
	if s.proef_laars and slijm.has_method("zet_laars_proef"):
		slijm.zet_laars_proef()
	if s.proef_spuug > 0 and slijm.has_method("zet_spuug_proef"):
		slijm.zet_spuug_proef(s.proef_spuug)
	if s.proef_moment == "hap" and "moment_hap" in slijm:
		slijm.moment_hap = true
	if s.proef_moment == "val" and "moment_val" in hol:
		hol.moment_val = true
	if s.proef_moment == "munt" and "moment_munt" in hol:
		hol.moment_munt = true

# Na het laden van de save: put en Royal meteen op hun stap.
static func na_laad(s) -> void:
	var hol = s.hol
	# plat_proef=1: de twee regels van deze speelbeurt zijn al op, Gloop gaat meteen plat en blijft plat (Daan 16 nov 20:35)
	if s.proef_plat and "plat_tot" in s.slijm:
		s.plat_keer = preload("res://kern/wachtrij.gd").PLAT_KEER
		s.slijm.plat_tot = float(s.slijm.t) + 9999.0
	if s.proef_put > 0 and hol.upgrades != null:
		hol.upgrades.niveaus["stekelput"] = s.proef_put
		hol.queue_redraw()
	if s.proef_royal and hol.upgrades != null and s.slijm.has_method("upgrade_veranderd"):
		hol.upgrades.niveaus["slijm"] = 3
		s.slijm.upgrade_veranderd()
		s.bewaar()   # meteen bewaren, anders telt dezelfde weg-tijd na een harde afsluiting nog een keer

# Een vallende held (in _process): bij moment=val staan hij en het hol stil zodra hij MOMENT_VAL_T s valt.
static func kijk_val(s, w: Node) -> void:
	var hol = s.hol
	if hol.moment_val and not hol.moment_val_vast and float(w.get("val_t")) >= MOMENT_VAL_T:
		w.process_mode = Node.PROCESS_MODE_DISABLED
		hol.moment_val_vast = true
		hol.queue_redraw()

# Elk beeld: staat het moment stil, dan één logregel (de winkel-workflow maakt daarop zijn beelden).
static func tik(s) -> void:
	if s.proef_moment != "" and not s.moment_gemeld and staat_stil(s):
		s.moment_gemeld = true
		s.log_regel("HOL moment vast %s t=%.1f" % [s.proef_moment, s.t])

static func staat_stil(s) -> bool:
	match s.proef_moment:
		"val", "munt": return bool(s.hol.moment_val_vast)
		"hap": return "moment_vast" in s.slijm and float(s.slijm.moment_vast) >= 0.0 and float(s.slijm.t) >= float(s.slijm.moment_vast)
	return false
