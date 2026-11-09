extends Node2D
# Nep-hol voor de toetsen (Bram): dezelfde functies als hol/hol.gd, gang van kolom 2 tot 12.
var vallen := {}
var ingang_kol := 2
var schat_kol := 12
func is_gang(cel: Vector2i) -> bool:
	return cel.y == 0 and cel.x >= ingang_kol and cel.x <= schat_kol
func cel_naar_pos(cel: Vector2i) -> Vector2:
	return Vector2(cel.x * 16 + 8.0, 36)
func pos_naar_cel(pos: Vector2) -> Vector2i:
	return Vector2i(clampi(int(pos.x / 16), 0, 40), 0)
func ingang() -> Vector2i:
	return Vector2i(ingang_kol, 0)
func schat() -> Vector2i:
	return Vector2i(schat_kol, 0)
func val_op(cel: Vector2i) -> String:
	return vallen.get(cel.x, "")
