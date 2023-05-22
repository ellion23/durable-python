numbers = [int(i) for i in open('17.txt')]
l = []
temp = []
lasti = 0
for i in range(len(numbers)-1):
    if numbers[i] > numbers[i+1]:
        temp.append(numbers[i])
        lasti = i
    elif numbers[i] < numbers[i+1]:
        if i-1 == lasti:
            temp.append(numbers[i])
            l.append(temp)
            temp = []
        else:
            temp = []
    if i == len(numbers)-2:
        if numbers[i] > numbers[i+1]:
            temp.append(numbers[i+1])
            l.append(temp)
maxl = 1
for g in l:
    if len(g) > maxl:
        maxl = len(g)
l2 = [i for i in l if len(i) == maxl]
for g in l2:
    print(g)
print(maxl)
print(len(l2))
