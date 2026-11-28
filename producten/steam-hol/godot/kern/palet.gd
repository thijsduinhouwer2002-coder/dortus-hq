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

static func keuze() -> String:
	for a in OS.get_cmdline_user_args():
		if a.begins_with("palet="):
			return a.substr(6)
	return STANDAARD

# Legt de laag over de strook. Muis gaat er dwars doorheen; de laag tekent niets bij palet=vol.
static func zet(s, _breedte: int, _hoogte: int) -> void:
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
