r=49
def S(x):
    if x==r:
        return 1
    if x>r:
        return 0
    x1=x
    if x%100//10<9:
        x1+=10
    if x%10<9:
        x1+=1
    return S(x+1)+ S(x1)
print(S(26))



