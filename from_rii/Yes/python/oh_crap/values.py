n = int(input())
values_raw = ['' for j in range(n-1)]
for i in range(n):
    values_raw.insert(i, input())
sum, val_need = input().split()

Currency = dict()

