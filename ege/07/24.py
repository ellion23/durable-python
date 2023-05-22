# 24
numbers = []
txt = open('/home/ellion/PycharmProjects/pythonProject/ege/07/24.txt', encoding='utf-8').read()
a = {'H', 'E', 'B', 'V', 'C', 'X', 'T', 'A', 'O', 'L', 'M', 'R', 'Z', 'P', 'D', 'G', 'U', 'I', 'F', 'K', 'Q', 'J', 'N', 'Y', 'S', 'W'}
n = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
num = ''
for i in range(len(txt)):
    if txt[i] in n and txt[i-1] in a:
        num += txt[i]
    elif txt[i] in n and txt[i+1] in a:
        num += txt[i]
        numbers.append(int(num))
        num = ''
    elif txt[i] in n:
        num += txt[i]
print(len(numbers))
while min(numbers) % 2 != 0:
    numbers.remove(min(numbers))
print(min(numbers))
