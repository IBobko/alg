import numpy as np
import matplotlib.pyplot as plt

# Определение функции
def y(x):
    return (1 + 1/x)**x

# Создание массива значений x
x = np.linspace(1, 10, 1000)  # Выберите диапазон значений x

# Вычисление значений функции
y_vals = y(x)

# Построение графика функции
plt.plot(x, y_vals)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y = (1 + 1/x)^x')
plt.grid(True)
plt.show()