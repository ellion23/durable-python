import shape


class Circle(shape.Shape):
    def __init__(self, x=0, y=0, r=0):
        super().__init__()
        self.__x = x
        self.__y = y
        self.__r = r
        self.__coords()

    def __coords(self):
        self.__x1 = self.__x - self.__r
        self.__y1 = self.__y - self.__r
        self.__x2 = self.__x + self.__r
        self.__y2 = self.__y + self.__r

    @property
    def x1(self):
        return self.__x1

    @property
    def y1(self):
        return self.__y1

    @property
    def x2(self):
        return self.__x2

    @property
    def y2(self):
        return self.__y2