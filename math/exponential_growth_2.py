import numpy as np
import matplotlib.pyplot as plt

# Задаем значение прироста
a = 1.1

# Генерируем значения для оси x от 0 до 1 с шагом 0.01
x = np.arange(0, 1, 0.01)

# Вычисляем значения функции y = a^x
y = np.power(a, x)

# Строим график
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y = a^x')
plt.grid(True)
plt.show()

