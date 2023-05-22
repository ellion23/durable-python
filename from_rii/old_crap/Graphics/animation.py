from graph import *
x = 30
y = 40
width = 40
height = 60
d_x = 5
d_y = 5
def triangle(x, y, color):
    penColor(color)
    brushColor(color)
    polygon([(x, y), (x+width, y),
             (x, y-height)])

thing = polygon([(x, y), (x+width, y),
             (x, y-height)])
def update():
    moveObjectBy(thing, d_x, d_y)
    if xCoord(thing) >= 380:
        moveObjectBy(thing, -d_x, d_y)
onTimer(update, 50)
run()
