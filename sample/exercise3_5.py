#1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated sequence:
# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the value printed next appears on the same line.
# print '+',
# print '-'
# The output of these statements is '+ -'.
# A print statement all by itself ends the current line and goes to the next line.

def do_twice(f):
    f()
    f()

def do_four(func):
    do_twice(func)
    do_twice(func)

def draw_grid_edge():
    print '+', ' -' * 4,
    print ' +', ' -' * 4,
    print ' +'

def draw_grid_body():
    print '|', ' '*9,
    print '|', ' '*9,
    print '|'

def draw_grid():
    draw_grid_edge()
    do_four(draw_grid_body)
    draw_grid_edge()
    do_four(draw_grid_body)
    draw_grid_edge()

# draw_grid()


# 2. Write a function that draws a similar grid with four rows and four columns.
# Solution: http: // thinkpython. com/ code/ grid. py . Credit: This exercise is based on an exercise in Oualline, Practical C Programming, Third Edition, O'Reilly Media, 1997

def draw_grid_edge_section():
    print '+' + ' -' * 4,

def draw_grid_edge_section_end():
    print '+'

def draw_grid_body_section():
    print '|' + '  ' * 4,

def draw_grid_body_section_end():
    print '|'

def draw_grid_double_edge():
    do_four(draw_grid_edge_section)
    draw_grid_edge_section_end()

def draw_grid_double_body():
    do_four(draw_grid_body_section)
    draw_grid_body_section_end()

def draw_grid_double_body_hight():
    do_four(draw_grid_double_body)

def draw_grid_double_body_length():
    draw_grid_double_edge()
    draw_grid_double_body_hight()

def draw_grid():
    do_four(draw_grid_double_body_length)
    draw_grid_double_edge()

draw_grid()