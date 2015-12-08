from meet import *
import random
cells=[]
for i in  range(0, 7):
	cell={"x":get_random_x(), "y":get_random_y(), "radius":30, "dy":random.uniform(-0.5,0.5), "dx":random.uniform(-0.5, 0.5), "color":"blue"}
	z=create_cell(cell)
	cells.append(z)
	
while True:
	move_cells(cells)
	for i in cells:
		if i.xcor()>get_screen_width():
			i.set_dx(random.uniform)
		if i.ycor()>get_screen_height():
			i.set_dy(random.uniform)	
		if i.xcor()<get_screen_width()*-1:
			i.set_dx(random.uniform)
		if i.ycor()<get_screen_width()*-1:
			i.set_dy(random.uniform)


		



