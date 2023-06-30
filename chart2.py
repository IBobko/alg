import numpy as np
import matplotlib.pyplot as plt

# Задаем параметры распределения
lam = 0.5

# Задаем значения аргумента
x = np.arange(0, 10, 0.1)

# Вычисляем значения функции распределения
y = lam * np.exp(-lam * x)

# Строим график
plt.plot(x, y)
plt.title("Вероятностная функция экспоненциального распределения")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.show()