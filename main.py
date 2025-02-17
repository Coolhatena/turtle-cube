"""
Autor: Eduardo Rivera Geffroy
No. Control: 21760177
Descripcion: Programa para dibujar un cubo usando Turtle
"""

# TODO: Crear linea usando t.dot

import turtle as t
 
def draw_angled_line(is_returning = True):
	prev_angle = t.heading()
	angle = prev_angle - 45
	STEPS = 80
	t.right(angle)
	t.fd(STEPS)
	if is_returning:
		t.right(180)
		t.fd(STEPS)

	t.setheading(prev_angle)
	

def draw_cube(is_lined=True):
	t.setheading(0)
	steps = 100
	angle = 90
	for _ in range(4):
		if is_lined:
			draw_angled_line()
		t.right(angle)
		t.fd(steps)


if __name__ == "__main__":
	import time
	
	draw_cube()
	draw_angled_line(is_returning=False)
	draw_cube(is_lined=False)
	time.sleep(15)