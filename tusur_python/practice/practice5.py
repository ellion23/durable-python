from vector import Vector


def vector_sum(a: Vector, b: Vector):
    coords_a, coords_b = a.coords, b.coords
    return Vector(coords_a[0]+coords_b[0], coords_a[1]+coords_b[1], coords_a[2]+coords_b[2])


def vector_sub(a: Vector, b: Vector):
    coords_a, coords_b = a.coords, b.coords
    return Vector(coords_a[0] - coords_b[0], coords_a[1] - coords_b[1], coords_a[2] - coords_b[2])


def main():
    a = Vector(1, 2, 3)
    b = Vector(3, 2, 1)
    c = vector_sum(a, b)
    print(c.coords)


if __name__ == "__main__":
    main()
