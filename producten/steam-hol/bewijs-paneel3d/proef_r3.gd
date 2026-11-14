extends SceneTree
# Olaf: kaartje en kroniek op 96, 120 en 160 px (3D), onder elkaar, op ware grootte
var stap := 0
var t
func _initialize():
	var H := [96, 120, 160]
	t = SubViewport.new(); t.size = Vector2i(560, (96+120+160)*2 + 60); t.render_target_update_mode = SubViewport.UPDATE_ALWAYS; root.add_child(t)
	var bg := ColorRect.new(); bg.color = Color("#5a3a4a"); bg.size = Vector2(t.size); t.add_child(bg)
	var T = load("res://kern/tekst.gd")
	var y := 0
	for i in 3:
		for k in 2:
			var n = Node2D.new(); n.set_script(T)
			n.breedte = 1024.0; n.hoogte = float(H[i]); n.schaal = maxi(2, int(H[i] / 40.0)); n.goud = 27
			n.position = Vector2(-470, y)
			if k == 0:
				var rg: Array[String] = ["Bram fell in the Spike Pit. +9", "Ties tried to lift it.", "Gloop ate Joost. A crown!"]
				n.regels = rg; n.hover = true
			else:
				n.kaart = {"titel": "Big Gloop", "uitleg": "Bought.", "kost": 45, "kan": true, "tekst": 0, "tekort": 0, "terug": 45, "weg": false}
			t.add_child(n)
			var lijn := ColorRect.new(); lijn.color = Color("#2a1a2a"); lijn.position = Vector2(0, y + H[i]); lijn.size = Vector2(560, 1); t.add_child(lijn)
			y += H[i] + 10
func _process(_d):
	stap += 1
	if stap == 5:
		t.get_texture().get_image().save_png(OS.get_environment("UIT"))
		return true
	return false
