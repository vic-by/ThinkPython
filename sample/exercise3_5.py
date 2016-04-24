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

def do_twice(f,v):
    f(v)
    f(v)

def do_four(func,val):
    do_twice(func,val)
    do_twice(func,val)

def draw_grid_edge():
    print '+', ' -' * 4,
    print ' +', ' -' * 4,
    print ' +'

def draw_grid_body(a):
    #fake parameter added to make do_twice work
    print '|', ' '*9,
    print '|', ' '*9,
    print '|'

def draw_grid():
    draw_grid_edge()
    do_four(draw_grid_body,1)
    draw_grid_edge()
    do_four(draw_grid_body,1)
    draw_grid_edge()

draw_grid()


# 2. Write a function that draws a similar grid with four rows and four columns.
# Solution: http: // thinkpython. com/ code/ grid. py . Credit: This exercise is based on an exercise in Oualline, Practical C Programming, Third Edition, O'Reilly Media, 1997