import matplotlib.pyplot as plt

f = open('stock_price_Yandex.txt', 'r')
x = list()
y = list()
for i in f:
    iz = i.split()
    if iz == '':
        break
    x.append(iz[0])
    y.append(float(iz[1]))

plt.title("Yandex stock priсe")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x, y, color="#ffb07c", marker="o", ms=5, label="uffff")

plt.legend()
plt.show()