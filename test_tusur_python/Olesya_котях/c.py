n = input()
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
minors = list()
for i in range(len(arr1)-1):
    minors.append(arr1[i]*arr2[i+1] - arr1[i+1]*arr2[i])
print(*minors)
