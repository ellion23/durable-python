from math import sqrt


class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def coords(self):
        return self.__x, self.__y, self.__z

    @coords.setter
    def coords(self, c):
        self.__x = c[0]
        self.__y = c[1]
        self.__z = c[2]

    @property
    def module(self):
        module = sqrt(self.__x**2 + self.__y**2 + self.__z**2)
        return module

    def __copy__(self):
        return Vector(self.__x, self.__y, self.__z)

    def multiply_by(self, k):
        self.__x *= k
        self.__y *= k
        self.__z *= k

    def normalize(self):
        inv_length = 1 / self.module
        self.__x *= inv_length
        self.__y *= inv_length
        self.__z *= inv_length

    def __str__(self):
        return f"Vector x = {self.__x}; y = {self.__y}; z = {self.__z};"
