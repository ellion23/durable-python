import matplotlib.pyplot as plt
import numpy as np

# x = [*range(11)]
# y = [i ** 2  for i in x]

plt.title('неЛинейная зависимость')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
# plt.plot(x, y)
# plt.plot(x, 'r--')

# xkcd.com/color/rgb

x = np.arange(-5, 6, 0.1)
plt.plot(x, np.sin(x), color="#ffb07c", marker="o", ms=5, label="original")

plt.plot(x, 2 * np.sin(x), color="green", label='sinx*2')

plt.plot(x, np.sin(x / 2), color="blue", label='sinx/2')

plt.legend()
plt.show()