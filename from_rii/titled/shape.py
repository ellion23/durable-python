import random


class Shape:
    def col(self):
        return hex(random.randint(0, 255)).replace("x", "")[-2:]

    def __init__(self):
        r = self.col()
        g = self.col()
        b = self.col()
        self.color_fill = "#" + r + g + b
        r = self.col()
        g = self.col()
        b = self.col()
        self.color_border = "#" + r + g + b
        self.__width = random.randint(1, 5)

    @property
    def width_border(self):
        return self.__width

    @width_border.setter
    def width_border(self, value):
        assert isinstance(value, int), "value must be an int"
        self.__width = value
