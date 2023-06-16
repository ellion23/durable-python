from vector import Vector
from copy import copy


def vector_sum(a: Vector, b: Vector) -> Vector:
    coords_a, coords_b = a.coords, b.coords
    return Vector(coords_a[0] + coords_b[0], coords_a[1] + coords_b[1], coords_a[2] + coords_b[2])


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
    pass


def get_cos(a: Vector, b: Vector) -> float:
    pass


def main():
    a = Vector(1, 2, 3)
    z = copy(a)
    b = Vector(3, 2, 1)
    c = vector_sum(z, b)
    print(a)
    print(c)


if __name__ == "__main__":
    main()
