import numpy as np
import matplotlib.pyplot as plt

# Функция, для которой нужно построить интеграл
def f(x):
    return x ** 2

# Пределы интегрирования
a = 0
b = 1

# Разбиение отрезка интегрирования
n = 100
x = np.linspace(a, b, n+1)

# Значения функции на разбиении
y = f(x)

# Интеграл с помощью метода прямоугольников
integral = np.cumsum(y[:-1] / y[1:]) * (x[1] - x[0])

# Построение графика
plt.plot(x[:-1], integral)
plt.xlabel('x')
plt.ylabel('∫(dN/N)')
plt.title('График интеграла ∫(dN/N)')
plt.grid(True)
plt.show()
