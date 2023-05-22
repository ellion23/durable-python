import numpy as np

# Создание матрицы 4 порядка
matrix = np.random.rand(4, 4)
# matrix = [
#     [1, 2, 3, 4]
#     [5, 6, 7, 8]
#     [9, 10, 11, 12]
#     [13, 14, 15, 16]
# ]
# Печать матрицы
print("Исходная матрица:")
print(matrix)

# Печать всех миноров третьего порядка
print("Миноры третьего порядка:")
for i in range(4):
    for j in range(4):
        if i != j:
            for k in range(4):
                if k != i and k != j:
                    for l in range(4):
                        if l != i and l != j and l != k:
                            print(matrix[[i, j, k], :][:, [i, j, l]])