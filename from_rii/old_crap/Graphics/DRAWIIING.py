from graph import *
height, width = 80, 100


# def triangle(x, y, color):
#     penColor(color)
#     brushColor(color)
#     polygon([(x, y), (x+width, y),
#              (x, y-height)])


x = 90
y = 40
side = 70
height_1 = side * 3 ** 0.5 /2
# triangle(x, y, "blue")
# triangle(x-width, y+height, "red")
# triangle(x, y+height, "green")
# def triangle_1(x, y, color):
#     penColor(color)
#     brushColor(color)
#     polygon([(x, y), (x+side, y),
#              (x + side / 2, y+height)])
# triangle_1(x, y, "blue")
# triangle_1(x+side, y, "red")
# triangle_1(x+side/2, y+height, "green")


# def tree(x, y, x1, y1, length, weight, amount):
#     polygon([(x, y), (x + weight/2, y + length), (x + weight, y)])
#     for i in range(amount, 0, -1):
#         polygon([(x1 + weight/2, y1+length*(1/i), (x1+weight, y1 + length*(1/i)), (x1, y1)])

# def tree(x, y, amount):
#     brushColor("green")
#     m = width/(2*amount)
#     for i in range(amount, 0, -1):
#         polygon([(x, y+(height/amount)*(i-1)), (x-m*i, y+(height/amount)*i), (x+m*i, y+(height/amount)*i)])



run()
