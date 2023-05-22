from random import randint
from collections import defaultdict


class rainbow:
    def color(string, col):
        col = col.lower()
        string += '\033[0m'
        if col == 'red' or col == '1':
            return '\033[31m' + string
        elif col == 'green' or col == '2':
            return '\033[32m' + string
        elif col == 'yellow' or col == '3':
            return '\033[33m' + string
        elif col == 'blue' or col == '4':
            return '\033[34m' + string
        elif col == 'violet' or col == '5':
            return '\033[35m' + string
        elif col == 'turquoise' or col == '6':
            return '\033[36m' + string



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def get_cds(self):
        return self.x, self.y
    
    def mv(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


class GameObject:
    ids = set()
    cds = dict()
    def __init__(self):
        self.id = randint(1, 1000)
        while self.id in GameObject.ids:
            self.id = randint(0, 1000)
        GameObject.ids.add(self.id)
        self.coords = Point(0, 0)

    def move(self, other):
        pass

    def set_coords(self, coord: Point):
        self.coords = coord

    @property
    def get_coords(self):
        return self.coords.get_cds

    def __str__(self):
        return(f'Class: {type(self)}, id is {self.id} from {len(GameObject.ids)}')


class Hero(GameObject):
    def __init__(self, name, color):
        super().__init__()
        self.name = name
        # GameObject.__init__(self)
        self.level = 1
        self.army = defaultdict(GameObject)
        self.color = color
    # def move(self, delta):
    #     self.coords.x += delta.x
    #     self.coords.y += delta.y

    def add_soldier(self, sld: GameObject):
        if type(sld) != Hero and type(sld) != GameObject:
            self.army[sld.id] = sld

    def __str__(self):
        return(f'Class: Hero, id = {self.id} army: {self.army.keys()}')
    
    # def get_soldier(self, str):
        

class Soldier(GameObject):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.power = randint(30, 100)
        self.hero = None
        self.coords = self.instcoords()
        # self.coords = coords
        # cor = self.instcoords()
        # self.coords = cor

    def instcoords(self):
        x, y = randint(0, 9), randint(0, 5)
        while Point(x, y) in self.cds.keys():
            x, y = randint(0, 9), randint(0, 5)
        self.cds[Point(x, y)] = self
        return Point(x, y)

    def move(self, way: str):
        if way == 'left':
            self.coords.mv(-1, 0)
        if way == 'right':
            self.coords.mv(1, 0)
        if way == 'up':
            self.coords.mv(0, 1)
        if way == 'down':
            self.coords.mv(0, -1)

    def assign(self, h: Hero):
        self.hero = h
        h.add_soldier(self)

    def __del__(self):
        if self.hero is not None:
            self.hero.army.remove(self.id)

    def fight(self, other):
        if self.hero == other.hero:
            print('Friendly fire')
        else:
            self.health -= other.power
            other.health -= self.power
            if self.health < 0:
                self.health = 0
            if other.health < 0:
                other.health = 0

    def __str__(self):
        return(f'Class: Soldier, id = {self.id}, Health {self.health}')



class Map:
    def __init__(self):
        self.arr = ['a |', 'b |', 'c |', 'd |', 'e |', 'f |']

    def printmap(self, h1, h2):
        slds = []
        tmap = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ]
        for hero in h1, h2:
            color = rainbow.color('s', hero.color)
            army = hero.army.values()
            for i in army:
                slds.append([i.get_coords, color])
        for i in slds:
            x, y = i[0][0], i[0][1]
            tmap[y][x] = i[1]
        print('   ___________________')
        for i in range(6):
            print(self.arr[i] + ' '.join(tmap[i]) + '|')
        print('   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾', '   1 2 3 4 5 6 7 8 9 10', sep='\n')


# class Color:
#     def __init__(self, color):
#         if color == '\033[31mRed\033[0m':
#             self.color = '\033[31ms\033[0m'
#         if color == '\033[32mGreen\033[0m':
#             self.color = '\033[32ms\033[0m'
#         if color == '\033[33mYellow\033[0m':
#             self.color = '\033[33ms\033[0m'
#         if color == '\033[34mBlue\033[0m':
#             self.color = '\033[34ms\033[0m'
#         if color == '\033[35mViolet\033[0m':
#             self.color = '\033[35ms\033[0m'
#         if color == '\033[36mTurquoise\033[0m':
#             self.color = '\033[36ms\033[0m'
    
#     @property
#     def get_color(self):
#         return self.color

    


map = Map()
h = []
a = []
colors = ['\033[31mRed\033[0m', '\033[32mGreen\033[0m', '\033[33mYellow\033[0m', '\033[34mBlue\033[0m', '\033[35mViolet\033[0m', '\033[36mTurquoise\033[0m']


# for i in range(2):
#     print(f'Creating {i+1} player')
#     name = str(input('Please write your name: '))
#     print('You may choose your color.')
#     for j in range(len(colors)):
#         print(j+1, colors[j], end=' ')
#     print()
#     color = int(input('Number of your color: ')) - 1
#     hero = Hero(colors[color], name)
#     colors.pop(color)
#     h.append(hero)

# while True:


h1 = Hero('alice', '1')
h2 = Hero('ellion', '3')
h.append(h1)
h.append(h2)


for i in range(10):
    s = Soldier()
    a.append(s)
    j = randint(0, len(h)-1)
    h[j].add_soldier(s)    


map.printmap(h[0], h[1])
# print('ehh')



# list(h1.army.values())[0].move('left')

# for o in a:
#     print(o)
#     print(o.get_coords)

# print(dir(a[0]))

