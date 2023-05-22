import math
# Дан массив из N элементов (вещественные числа). Вычислить:
# 1) минимальный по модулю элемент массива;
# 2) сумму модулей элементов массива, расположенных после первого равного нулю элемента.
# Преобразовать массив так, чтобы сначала располагались элементы, стоявшие в чётных позициях,
# а потом – стоявшие в нечётных позициях (не изменяя порядка элементов в пределах групп).
# Считать, что нумерация элементов массива начинается с 1.

n = input()
arr = [float(x) for x in input().split()]
arr2 = list()
arr2 = [abs(i) for i in arr]
if 0 in arr2:
    ind = arr2.index(0)
else:
    ind = len(arr2)
#print(arr)
#print("arr2 ind0",arr2, ind)
summ = 0
for i in range(ind, len(arr2)):
    summ += arr2[i]


print("{:.4f}".format(min(arr2)))
print("{:.4f}".format(summ))


arr3 = list()

position = 0
for i in range(len(arr)):
    if i % 2 != 0:
        arr3.insert(position, arr[i])
        position +=1
    else:
        arr3.append(arr[i])

for i in arr3:
    print("{:.4f}".format(i), end=" ")

