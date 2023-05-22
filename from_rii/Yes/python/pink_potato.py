import matplotlib.pyplot as plot
import numpy as np
l = ['Грустный глаз', 'Грустный рот', 'c', 'brown']
def f2(x):
    return 1/(x**2 - 9)
def line(x, l, col):
    plot.plot(x, f2(x), c=col, lw=3, label=l)

line(np.arange(-5, -3, 0.1), l[0], l[2])
line(np.arange(-2.9, 3, 0.1), l[1], l[3])
line(np.arange(3.1, 5.1, 0.1), l[0], l[2])

plot.plot([-3, -3], [-2, 2], '--', color="#000000", markevery=[1], ms=7)
plot.plot([3, 3], [-2, 2], '--',  color="#000000", markevery=[1], ms=7)


plot.title('Grafik Antona.')
plot.xlabel('x')
plot.ylabel('y')
plot.grid()

# x2 = np.arange(-5, -3, 0.2)
# plot.plot(x2, f2(x2), color="#ffb07c", label="Vodka is good")
# plot.plot([0, 0], [-8, 15], '^-c', color="#000000", markevery=[1], ms=7)
# plot.plot([-5, 5], [0, 0], '>-c', color="#000000", markevery=[1], ms=7)
# x3 = np.arange()
plot.legend()
plot.show()
