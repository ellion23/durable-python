class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def coords(self):
        return self.__x, self.__y
    
    @coords.setter
    def coords(self, c):
        self.__x = c[0]
        self.__y = c[1]


class Figure:
    def __init__(self, center: Point, vertex: list):
        self.center = center
        self.vertex = vertex

    def move(self, dx, dy):
        for i in range(len(self.vertex)):
            self.vertex[i] = self.vertex[i][0] + dx, self.vertex[i][1] + dy

    def square(self):
        pass

    def center(self):
        pass

    def bounds(self):
        pass


class Circle(Figure):
    def __init__(self, x, y, r):
        super().__init__(Point(x, y), [])
        self.r = r

    @property
    def square(self):
        square = self.r**2 * 3.1415
        return square

    @property
    def perimeter(self):
        perimeter = self.r * 6.283
        return perimeter

    @property
    def bounds(self):
        x, y = self.center.coords
        coord1 = x - self.r, y + self.r
        coord2 = x + self.r, y - self.r
        a = self.r * 2
        return coord1, coord2, a

    @property
    def infos(self):
        x, y = self.center.coords
        return x, y, self.r

    def move(self, dx, dy):
        x, y = self.center.coords
        self.center.coords = x + dx, y + dy


class Triangle(Figure):
    def __init__(self, center, vertex):
        center = Point((vertex[0].coords[0] + vertex[1].coords[0] + vertex[2].coords[0]) / 3,
                       (vertex[0].coords[1] + vertex[1].coords[1] + vertex[2].coords[1]) / 3)
        super().__init__(center, vertex)


    @property
    def infos(self):
        v = []
        for i in self.vertex:
            v.append(i.coords)
        return self.center.coords, v


# c = Circle(3, 2, 3)
# # c.center.move(-3, -2)
# c.center.coords = 0, 0
# c.move(1, 1)
# print(c.perimeter)
# print(c.square)
# print(*c.bounds)
# print(c.infos)
# print(c.center.coords)

t = Triangle(Point(0, 0), [Point(8, 1), Point(11, 1), Point(8, 5)])
t.move(-8, -1)


print(t.infos)
