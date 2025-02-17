"""
Autor: Eduardo Rivera Geffroy
No. Control: 21760177
Descripcion: Función para hacer lineas, sin usar las funciones incluidas en turtle
"""

import turtle as t


def _interpolate(i0,d0,i1,d1):
	if i0 == i1:
		return [d0 for _ in range(i0,i1+1)]
	
	values = []
	a = (d1 - d0) / (i1 - i0)
	d = d0
	for _ in range(i0,i1+1):
		values.append(d)
		d = d + a
	return values


def draw_point(x, y, size):
	t.penup()
	t.setpos(x, y)
	t.dot(size=size)
	

def draw_handcrafted_line(pt1, pt2, size=1):
	x1, y1 = pt1
	x2, y2 = pt2

	if abs(pt2[0] - pt1[0]) > abs(pt2[1] - pt1[1]):
		#lineas horizontales
		if pt1[0] > pt2[0]:
			(x1, y1), (x2, y2) = pt2, pt1
			
		ys = _interpolate(x1, y1, x2, y2)
		for x in range(x1, x2 + 1):   
			draw_point(x, ys[x - x1], size)

	else:
		#lineas verticales    
		if pt1[1] > pt2[1]:
			(x1, y1), (x2, y2) = pt2, pt1
			
		xs = _interpolate(y1, x1, y2, x2)
		for y in range(y1, y2 + 1):
			draw_point(xs[y - y1], y, size)


if __name__ == "__main__":
	import time

	draw_handcrafted_line((0, 0), (2, 100))
	draw_handcrafted_line((50, 0), (100, 50))
	draw_handcrafted_line((-50, 0), (-100, 50))
	draw_handcrafted_line((50, 0), (100, -50))
	draw_handcrafted_line((-50, 0), (-100, -50))
	draw_handcrafted_line((0, 0), (-2, -100))

	time.sleep(5)
