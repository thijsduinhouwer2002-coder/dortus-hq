# Palet over de hele strook (Olaf 28 nov, #333): drie blinde tests noemden Hats "cheap mobile game" en vroegen om
# "a softer, less saturated art style". Eén laag bovenop alles leest het beeld terug en dempt de kleuren, zodat de
# kunst zelf (Blender, licht, bord) niet per stuk hoeft te veranderen. Kiezen: palet=vol (zoals het was), palet=zacht.
# Sanne 28 nov (#333): grond zacht als standaard, want de omslag- en headertests vragen letterlijk "softer, less
# saturated" en de speelscherm-test gaf vol en zacht dezelfde plek. palet=vol blijft als keuze voor wie het fel wil.
extends RefCounted

const STANDAARD := "zacht"

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
	s.log_regel("HOL palet %s" % k)
