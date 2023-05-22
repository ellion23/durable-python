import matplotlib.pyplot as pilot
import numpy as np


def f1(xai):
    # if x <= 2:
    #     return (xai - 2 / 2 - xai) * (xai**2 - 2 * xai)
    return (-xai - 2 / 2 - xai) * (xai**2 - 2 * xai)


pilot.title('Why?(((')
pilot.xlabel('x')
pilot.ylabel('y')
pilot.grid()

x = np.arange(-2, 4, 2)
pilot.plot([0, 0], [-35, 50], '^-c', color="#000000", markevery=[1], ms=7)
pilot.plot([-5, 5], [0, 0], '>-c', color="#000000", markevery=[1], ms=7)

pilot.plot(x, f1(x), color="#0ff", label="Because not.")
pilot.scatter([2], [0], s=80, linewidths=2, edgecolors="g")
pilot.legend()
pilot.show()
