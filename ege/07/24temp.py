txt = open('/home/ellion/PycharmProjects/pythonProject/ege/07/24.txt', encoding='utf-8').read()
numbers = []
k = ''
for i in range(len(txt)):
    if txt[i].isdigit() and txt[-1].isalpha():
        k += txt[i]
    elif txt[i].isdigit() and txt[i+1].isalpha():
        k += txt[i]
        numbers.append(int(k))
        k = ''
    elif txt[i].isdigit():
        k += txt[i]
# numbers.sort()
while min(numbers) % 2 != 0:
    numbers.remove(min(numbers))
    # numbers.pop(0)
print(min(numbers))
