# Palet over de hele strook (Olaf 28 nov, #333): drie blinde tests noemden Hats "cheap mobile game" en vroegen om
# "a softer, less saturated art style". Eén laag bovenop alles leest het beeld terug en dempt de kleuren, zodat de
# kunst zelf (Blender, licht, bord) niet per stuk hoeft te veranderen. Kiezen: palet=vol (zoals het was), palet=zacht.
# Sanne 28 nov (#333) koos zacht. Gemeten binnen één run (Olaf 28 nov, wissel=palet tegen wissel=nep, 200 px, Linux
# software-tekenen): de laag kost ±30 procent CPU (palet +41, placebo +11, GEZIEN). Dat is boven de poort van 20 procent
# in platformen/steam/balans.md, en de blinde test zag geen verschil. Daarom blijft vol de standaard; de zachte kleuren
# moeten in de kunst en de lichtkaart zelf komen (geen extra laag). palet=zacht blijft als proef.
extends RefCounted

const STANDAARD := "vol"

# zacht: verzadiging 0,78, schaduwen iets opgelicht, hoge lichten iets terug, een vleug warm (oud papier, geen sepia)
const SHADER := """
shader_type canvas_item;
render_mode unshaded;
uniform sampler2D scherm : hint_screen_texture, filter_nearest;
uniform float verzadiging = 0.78;
uniform float licht_op = 0.035;
uniform float licht_af = 0.94;
uniform vec3 warm = vec3(1.02, 1.0, 0.95);
void fragment() {
	vec4 b = texture(scherm, SCREEN_UV);
	vec3 c = b.rgb;
	float l = dot(c, vec3(0.299, 0.587, 0.114));
	c = mix(vec3(l), c, verzadiging);
	c = c * licht_af + licht_op;
	c = clamp(c * warm, 0.0, 1.0);
	COLOR = vec4(c, b.a);
}
"""

# Grond zacht (Olaf 28 nov, #333, keuze Sanne "grond zacht"): dezelfde demping, maar alleen in het vaste beeld van het
# hol (hol/hol_vast.gd: gras, aarde, gangwand, kamers, lichtkaart). Dat beeld tekent alleen opnieuw als het hol
# verandert (graven, put, ingang), dus de demping kost per beeld niets; de laag over alles kostte ±30 procent.
# Het vaste beeld is doorzichtig met premultiplied kleur: het oplichten gaat maal de dekking, anders kleurt de lucht mee.
# Helden, Gloop, goud en fakkel tekenen er los overheen en blijven vol. Kiezen: grond=zacht (standaard), grond=vol.
const GROND_STANDAARD := "zacht"
const GROND_SHADER := """
shader_type canvas_item;
render_mode unshaded, blend_disabled;
uniform sampler2D scherm : hint_screen_texture, filter_nearest;
uniform float verzadiging = 0.78;
uniform float licht_op = 0.035;
uniform float licht_af = 0.94;
uniform vec3 warm = vec3(1.02, 1.0, 0.95);
void fragment() {
	vec4 b = texture(scherm, SCREEN_UV);
	vec3 c = b.rgb;
	float l = dot(c, vec3(0.299, 0.587, 0.114));
	c = mix(vec3(l), c, verzadiging);
	c = c * licht_af + licht_op * b.a;
	c = clamp(c * warm, vec3(0.0), vec3(b.a));
	COLOR = vec4(c, b.a);
}
"""

static func grond_keuze() -> String:
	for a in OS.get_cmdline_user_args():
		if a.begins_with("grond="):
			return a.substr(6)
	return GROND_STANDAARD

# Legt de demping als laatste in het vaste beeld vp (na tegels en lichtkaart: z_index boven alles daar).
static func zet_grond(vp: SubViewport) -> ColorRect:
	if vp == null or grond_keuze() != "zacht":
		return null
	var vlak := ColorRect.new()
	vlak.name = "GrondZacht"
	vlak.mouse_filter = Control.MOUSE_FILTER_IGNORE
	vlak.z_index = 4000
	vlak.position = Vector2.ZERO
	vlak.size = Vector2(vp.size)
	var mat := ShaderMaterial.new()
	var sh := Shader.new()
	sh.code = GROND_SHADER
	mat.shader = sh
	vlak.material = mat
	vp.add_child(vlak)
	return vlak

# Meten binnen één run (balans.md): wissel=grond zet de demping om de 20 s aan en uit en tekent het vaste beeld dan
# opnieuw, wissel=grondnep tekent ook opnieuw maar laat de demping aan (placebo).
static func _wissel_grond(s, gv: ColorRect, vp: SubViewport) -> void:
	var nep := "wissel=grondnep" in OS.get_cmdline_user_args()
	var tik := Timer.new()
	tik.wait_time = 0.25
	tik.autostart = true
	vp.add_child(tik)
	var was := [true]
	tik.timeout.connect(func():
		var aan := int(Time.get_unix_time_from_system() / 20.0) % 2 == 0
		if aan != was[0]:
			was[0] = aan
			gv.visible = aan or nep
			vp.render_target_update_mode = SubViewport.UPDATE_ONCE
			print("HOL wissel grond %s unix=%.2f t=%.2f pad=Hol" % ["aan" if aan else "uit", Time.get_unix_time_from_system(), s.t]))

static func keuze() -> String:
	for a in OS.get_cmdline_user_args():
		if a.begins_with("palet="):
			return a.substr(6)
	return STANDAARD

# Legt de laag over de strook. Muis gaat er dwars doorheen; de laag tekent niets bij palet=vol.
static func zet(s, _breedte: int, _hoogte: int) -> void:
	var hv = s.hol.vast if "hol" in s and s.hol != null and "vast" in s.hol else null
	var gv: ColorRect = zet_grond(hv.vp if hv != null else null)
	s.log_regel("HOL grond %s" % ("zacht" if gv != null else "vol"))
	if gv != null and ("wissel=grond" in OS.get_cmdline_user_args() or "wissel=grondnep" in OS.get_cmdline_user_args()):
		_wissel_grond(s, gv, hv.vp)
	var k := keuze()
	if k != "zacht":
		return
	var laag := CanvasLayer.new()
	laag.name = "Palet"
	laag.layer = 100
	var vlak := ColorRect.new()
	vlak.mouse_filter = Control.MOUSE_FILTER_IGNORE
	# Daan #339 (1): ankers over het hele venster, zodat de laag meegroeit als het venster na _ready nog van maat
	# verandert (een andere hoogte herlaadt de scène, maar een venster dat later zijn maat krijgt mag geen volle rand laten)
	vlak.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	var mat := ShaderMaterial.new()
	var sh := Shader.new()
	sh.code = SHADER
	mat.shader = sh
	vlak.material = mat
	laag.add_child(vlak)
	s.add_child(laag)
	# Meten binnen één run (Daan #339 M2, balans.md): wissel=palet zet de laag om de 20 s aan en uit op de klok
	# (oneven blokken uit), wissel=nep schrijft dezelfde regels en laat hem aan (placebo).
	var args := OS.get_cmdline_user_args()
	if "wissel=palet" in args or "wissel=nep" in args:
		var nep := "wissel=nep" in args
		var tik := Timer.new()
		tik.wait_time = 0.25
		tik.autostart = true
		laag.add_child(tik)
		var was := [true]
		tik.timeout.connect(func():
			var aan := int(Time.get_unix_time_from_system() / 20.0) % 2 == 0
			if aan != was[0]:
				was[0] = aan
				vlak.visible = aan or nep
				print("HOL wissel palet %s unix=%.2f t=%.2f pad=Hol" % ["aan" if aan else "uit", Time.get_unix_time_from_system(), s.t]))
	s.log_regel("HOL palet %s" % k)
