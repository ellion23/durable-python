divCount=4
for n in range(190201, 190281):
    divs=[]
    q=round(n**0.5)
    if q*q==n:
        divs=[q]
        q-=1
    for d in range(1, q+1):
        if n%d==0 and d%2==0:
            divs=divs+[d, n//d]
            if len(divs)>divCount: break
    if len(divs)==divCount:
        print(*sorted(divs, reverse=True))


