choose_your_destiny = int(input())

if choose_your_destiny == 1:
    sumbadi = []
    f = open('kept_u_waiting_huh.txt')
    l = [i.split() for i in f.readlines()]
    for i in l:
        if i[0] == "push":
            sumbadi.append(i[1])
            print('ok!!!')
        elif i[0] == "pop":
            try:
                temp = sumbadi[0]
                sumbadi.pop(0)
                print(temp)
            except IndexError:
                print('Hey, bro, так не троллят.')
            except:
                print('Ну и чего ты добился этим.')
                # mmm, delicious
        elif i[0] == "front":
            try:
                print("Первый элемент: ", sumbadi[0])
            except IndexError:
                print('Hey, bro, так не троллят.')
        elif i[0] == "size":
            print(f'В массиве {len(sumbadi)} элементов')
        elif i[0] == "clear":
            for j in range(len(sumbadi)):
                sumbadi.pop(j)
            print('ok')
        elif i[0] == "exit":
            print("bye")
            break

if choose_your_destiny == 2:
    bal = 0
    skobka = input("Введите скобки (до чево я докотился...): ")
    for i in range(len(skobka)):
        if skobka[i] == ")":
            bal += 1
        if skobka[i] == "(":
            bal -= 1
        else:
            print("че несет дурной...")
            raise(WindowsError)
    if bal == 0:
        print('ну баланс норм да')
    elif bal != 0:
        print('не норм')
    else:
        print('Ты сюда как залез, шизик?')


