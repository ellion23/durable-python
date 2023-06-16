from vector import Vector
from copy import copy


def vector_sum(a: Vector, b: Vector) -> Vector:
    coords_a, coords_b = a.coords, b.coords
    return Vector(coords_a[0] + coords_b[0], coords_a[1] + coords_b[1], coords_a[2] + coords_b[2])
    # return Vector(a.__x + b.__x, coords_a[1] + coords_b[1], coords_a[2] + coords_b[2])


def vector_sub(a: Vector, b: Vector) -> Vector:
    coords_a, coords_b = a.coords, b.coords
    return Vector(coords_a[0] - coords_b[0], coords_a[1] - coords_b[1], coords_a[2] - coords_b[2])


def cross_product(a: Vector, b: Vector) -> Vector:
    coords_a, coords_b = a.coords, b.coords
    cx = coords_a[1] * coords_b[2] - coords_a[2] * coords_b[1]
    cy = coords_a[2] * coords_b[0] - coords_a[0] * coords_b[2]
    cz = coords_a[0] * coords_b[1] - coords_a[1] * coords_b[0]
    return Vector(cx, cy, cz)


def dot_product(a: Vector, b: Vector) -> float:
    coords_a, coords_b = a.coords, b.coords
    return coords_a[0] * coords_b[0] + coords_a[1] * coords_b[1] + coords_a[2] * coords_b[2]


def get_sin(a: Vector, b: Vector) -> float:
    return cross_product(a, b).module / (a.module * b.module)


def get_cos(a: Vector, b: Vector) -> float:
    return (dot_product(a, b)) / (a.module * b.module)


def main():
    z = Vector(1, 2, 3)
    a = copy(z)
    b = Vector(4, 5, 6)
    print(a)
    print(b)
    print(f"Модуль вектора a {a.module}")
    aa = copy(a)
    aa.multiply_by(3)
    print(f"Вектор a умноженный на 3 {aa}")
    aa = copy(a)
    aa.normalize()
    print(f"Нормализованный вектор a {aa}")
    print(f"Сумма a и b {vector_sum(a, b)}")
    print(f"Разность a и b {vector_sub(a, b)}")
    print(f"Векторное произведение a и b {cross_product(a, b)}")
    print(f"Скалярное произведение a и b {dot_product(a, b)}")
    print(f"Синус a и b {get_sin(a, b)}")
    print(f"Косинус a и b {get_cos(a, b)}")


if __name__ == "__main__":
    main()
