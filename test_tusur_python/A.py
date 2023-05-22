n = int(input())
array = [float(x) for x in input().split()]
array_abs = [abs(x) for x in array]
positive_product = 1
for i in array:
    if i > 0:
        positive_product *= i
start_index, end_index = array_abs.index(max(array_abs)), array_abs.index(min(array_abs))
if start_index > end_index:
    t = start_index
    start_index = end_index
    end_index = t

sum_elements = 0
for i in array[start_index:end_index+1]:
    sum_elements += i
print("{:.4f}".format(positive_product))
print("{:.4f}".format(sum_elements))
array.sort(reverse=True)
for i in array:
    print("{:.4f}".format(i), end=" ")