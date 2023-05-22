maxkdel = 1
for i in range(586132, 586431):
    deli = 0
    for j in range(2, i//2 + 1):
        if i % j == 0:
            deli += 1
    maxkdel = max(maxkdel, deli)
    if deli == 78:
        print(i, j)
print(maxkdel)
