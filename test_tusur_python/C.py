# Дана целочисленная матрица A размера 5 на 5.
# Вывести её в транспонированном виде (поменять местами строки со столбцами)

matrix = [[int(x) for x in input().split()] for i in range(5)]

for i in range(5):
    for j in range(5):
        print(matrix[j][i], end=" ")
    print()
