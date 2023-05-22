F=open('kept_u_waiting_huh.txt')
D=6
N=int(F.readline())
s=0
MinD=[10001]*D
for i in range(N):
    a, b=map(int, F.readline().split())
    s+=max(a, b)
    d=abs(a-b)
    r=d%D
    if r>0:
        MinD_New=MinD[:]
        for k in range(1, D):
            r0=(r + k)%D
            MinD_New[r0]=min(d + MinD[k], MinD_New[r0])
        MinD_New[r]=min(d, MinD_New[r])
        MinD=MinD_New[:]
    print(a, b, MinD)

F.close()

if s%D==0:
    print(s)
else:
    print(s-MinD[s%D])