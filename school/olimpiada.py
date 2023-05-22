
#L
a = int(input())
b = 0
list = [int(i) for i in input().split()]
for i in list:
    b+=i
if b>=60:
    a=b//60
    b= b % 60
    if b<10:
        b = '0'+ str(b)
else:
    a = 0
    if b<10:
        b = '0'+ str(b)
print('{}:{}'.format(a, b))

# #I
# l1 = str(input())
# l2 = str(input())
# n1 = l1.count('r')
# n2 = l2.count('r')
# if n1>=n2:
#     print('yes')
# else:
#     print('no')

# #G
# l = [int(i) for i in input().split()]
# max = 0
# for c in l:
#     if max<c:
#         max=c
# if l[0]==0 or l[1]==0 or l[2]==0:
#     print('')
# elif ((l[0])**2)+((l[1])**2)==max**2 or ((l[0])**2)+((l[2])**2)==max**2 or ((l[2])**2)+((l[1])**2)==max**2:
#     print("right")
# else:
#     print('wrong')

# #F
# a = int(input())
# x = 0
# list = [i for i in input()]
# if list[2]='(':
#     x = 9
#     n = list.find(')')
#
#
#
#     print(list, n, n1)






















