# Дан массив из N элементов (вещественные числа). Вычислить:
# 1) произведение отрицательных элементов массива;
# 2) сумму положительных элементов массива, расположенных до максимального элемента (включая сам максимальный элемент, если он положителен).
# Вывести элементы исходного массива в обратном порядке.

n = int(input())
array = [float(x) for x in input().split()]
negative_product = 1
flag = 0
for i in array:
    if i < 0:
        negative_product *= i
        flag = 1
positive_sum = 0
index = array.index(max(array))
if array[index] > 0:
    index += 1
for i in array[:index]:
    if i > 0:
        positive_sum += i
if flag:
    print("{:.4f}".format(negative_product))
else:
    print("0.0000")
print("{:.4f}".format(positive_sum))
for i in array[::-1]:
    print("{:.4f}".format(i), end=" ")