txt = [ord(i) for i in open('24.txt').read()]
# txt = [89, 88, 89,  90, 89, 88]
l = []
maxub = []
mb = 0
k = []
ilast = 0
for i in range(len(txt)-1):
    if txt[i] - 1 == txt[i+1]:
        k.append(txt[i])
        ilast = i
    else:
        if ilast + 1 == i:
            k.append(txt[i])
            if mb < len(k):
                maxub.append(k)
                mb = len(k)
                k = []
            else:
                k = []
        else:
            k = []
print(maxub)
ss = set(i for i in txt)
print(ss)