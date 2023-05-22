import matplotlib.pyplot as plot
import numpy as np

def f1(x):
    return x ** 2 - abs(x) - 6
def f2(x):
    return abs(x ** 2 - x - 6)

o = np.arange(-4, 5, 1)
zeroes = [0 for i in range(9)]
x = np.arange(-4, 4, 0.1)
plot.title('Гхафик Функции.')
plot.xlabel('x')
plot.ylabel('y')
plot.grid()

plot.plot(x, f1(x), color="#ffb07c", label="y = x ** 2 - |x| - 6", linewidth=3)
# plot.plot(o, zeroes, color="#000000", label="uffff", linewidth=1)
# plot.plot(zeroes, o, color="#000000", label="uffff", linewidth=1)
plot.plot([0,0],[-8,15], '^-c', color="#000000", markevery=[1], ms=7)
plot.plot([0.5,0.5],[-8,15], '--c', color="grey", markevery=[1], ms=7)
plot.plot([-5,5],[0,0],'>-c', color="#000000", markevery=[1], ms=7)
plot.plot(x, f2(x), color="#00ffff", label="y = |x ** 2 - x - 6|")


plot.legend()
plot.show()
