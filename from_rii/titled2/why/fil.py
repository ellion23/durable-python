import matplotlib.pyplot as plt
x = [*range(11)]
y = [*range(-10, 11, 2)]

plt.title('Линейная зависимость')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x, y)
plt.plot(x, 'r--')

plt.show()