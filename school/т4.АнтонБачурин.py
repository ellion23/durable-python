# 1
a = int(input('Введите число: '))
if  -5 < a < 3:
    print('yes')
else:
    print('no')

# 2
a = int(input('Введите число: '))
if (a >= 10 and a < 100) and (a // 10 == 3 or a % 10 == 3):
    print('yes')
else:
    print('no')

# 3
a = int(input('Введите число: '))
if a >= 1000 and a < 10000:
    print('Успешно')
else:
    print('Неудача')

# 4
a = int(input('Введите число: '))
if 7 < a < 10:
    print('Пора вставать!')
elif 0 < a <= 7 or 10 <= a <= 23:
    print('Ты проспал!')
else:
    print('Ошибка')

# 5 проверить все ли цифры трехзнач разные да нет
a = int(input('Введите число: '))
a1 = a // 100
a2 = a // 10 % 10
a3 = a % 10
if 100 <= a < 1000 and a1 != a2 and a1 != a3 and a2 != a3:
    print('Да')
else:
    print('Нет или число не трёхзначное')