n = input()
c = float(input())
arr = [float(x) for x in input().split()]
arr2 = list()
k = 0
for i in arr:
    if i < c:
        k += 1
print(k)

ind = 0
for i in range(0,len(arr),-1):
    if arr[i] < 0:
        ind = arr.index(arr[i])
        break
summ = sum(arr[ind:])
print(arr[ind])

arr2 = list()
for i in arr:
    if i < 0:
        arr2.append(1+i)
    else:
        arr2.append(i)
for i in arr2:
    print("{:0.4f}".format(i), end=" ")
