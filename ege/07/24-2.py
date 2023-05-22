import math
import re
txt = open('/home/ellion/PycharmProjects/pythonProject/ege/07/24.txt', encoding='utf-8').read()

nums = re.compile(r'[A-Z][0-9]+[A-Z]')
numbers = [int(i[1:-1]) for i in re.findall(nums, txt)]
print(len(numbers))
while min(numbers) % 2 != 0:
    numbers.remove(min(numbers))
print(min(numbers))
