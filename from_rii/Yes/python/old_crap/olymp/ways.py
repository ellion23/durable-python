f = open('bez_raznitsy_kak.txt', 'r')
m = list()
am = int(f.readline())
good = True
for a in range(am):
    m.append(list(map(int, f.readline().split())))

for i in range(am):
    for j in range(i, am):
        if m[i][j] != m[j][i]:
            good = False

if good == True:
    print('YES! YES! YES! YES! YES! YES! YES! YES! YES! YES!')
elif good == False:
    print('NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO!')