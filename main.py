import turtle as t
import time
 
def DrawAngledLine(is_returning = True):
	prev_angle = t.heading()
	angle = prev_angle - 45
	STEPS = 80
	t.right(angle)
	t.fd(STEPS)
	if is_returning:
		t.right(180)
		t.fd(STEPS)

	t.setheading(prev_angle)
	

def DrawCube(is_lined=True):
	t.setheading(0)
	steps = 100
	angle = 90
	for _ in range(4):
		if is_lined:
			DrawAngledLine()
		t.right(angle)
		t.fd(steps)


if __name__ == "__main__":
	DrawCube()
	DrawAngledLine(is_returning=False)
	DrawCube(is_lined=False)
	input("Detener?")