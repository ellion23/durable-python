from graph import *
from random import randint
x = 200
y = 60
space_x = 75
space_y = 90
in_row = 1
rows = 3
# def circles_build(x, y, space_x, space_y, in_row, rows):
#     brushColor('green')
#     for i in range(rows):
#         for i in range(in_row):
#             circle(x, y, 20)
#             x += space_x
#         x -= space_x * (in_row - 1)
#         y += space_y

# def circles_build(x, y, space_x, space_y, rows):
#     brushColor('green')
#     for i in range(rows):
#         for j in range(i+1):
#             circle(x, y, 20)
#             x += space_x
#         x -= space_x * (i+1)
#         y += space_y


def pyramid(x, y, space_x, space_y, in_row, rows):
    for i in range(rows):
        for j in range(0, in_row):
            brushColor(randint(0, 255), randint(0, 255), randint(0, 255))
            penColor(randint(0, 255), randint(0, 255), randint(0, 255))
            circle(x, y, 30)
            x += space_x
        x -= space_x * ((in_row-i)*2)
        y += space_y
        in_row += 2

# circles_build(x, y, space_x, space_y, in_row, rows)
# circles_build(x, y, space_x, space_y, rows)
pyramid(x, y, space_x, space_y, in_row, rows)
run()
