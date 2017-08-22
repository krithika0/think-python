def do_twice(f):
	f()
	f()
def do_four(f):
	do_twice(f)
	do_twice(f)
def draw_row_header_unit():
	print('+ '+'- '*4,end='')
def draw_row_header_2():
	do_twice(draw_row_header_unit)
	print('+')
def draw_pipe_unit():
	print('| '+' '*8,end='')
def draw_pipe_2():
	do_twice(draw_pipe_unit)
	print('|')
def draw_grid_unit_2():
	draw_row_header_2()
	do_four(draw_pipe_2)
def draw_grid_2():
	do_twice(draw_grid_unit_2)
	draw_row_header_2()

def draw_row_header_4():
	do_four(draw_row_header_unit)
	print('+')
def draw_pipe_4():
	do_four(draw_pipe_unit)
	print('|')
def draw_grid_unit_4():
	draw_row_header_4()
	do_four(draw_pipe_4)
def draw_grid_4():
	do_four(draw_grid_unit_4)
	draw_row_header_4()
draw_grid_2()
print('')
draw_grid_4()
