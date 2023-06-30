import numpy as np
import matplotlib.pyplot as plt

# Определение функции параболы
def parabola(x):
    return x**2

# Определение градиента функции параболы
def gradient(x):
    return 2*x

# Создание массива значений x
x = np.linspace(-5, 5, 100)

# Вычисление значений функции параболы
y = parabola(x)

# Вычисление значений градиента
grad = gradient(x)

# Построение графика параболы
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Parabola: f(x) = x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of Parabola')
plt.legend()

# Построение графика градиента
plt.figure(figsize=(8, 6))
plt.plot(x, grad, label='Gradient: f\'(x) = 2x')
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.title('Graph of Gradient')
plt.legend()

# Отображение графиков
plt.show()