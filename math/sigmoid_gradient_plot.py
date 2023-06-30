import numpy as np
import matplotlib.pyplot as plt

# Определение функции сигмоиды
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Определение градиента функции сигмоиды
def sigmoid_gradient(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Создание массива значений x
x = np.linspace(-10, 10, 100)

# Вычисление значений функции сигмоиды
y = sigmoid(x)

# Вычисление значений градиента
grad = sigmoid_gradient(x)

# Построение графика сигмоиды
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Sigmoid: f(x) = 1 / (1 + exp(-x))')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of Sigmoid')
plt.legend()

# Построение графика градиента
plt.figure(figsize=(8, 6))
plt.plot(x, grad, label='Gradient: f\'(x) = f(x) * (1 - f(x))')
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.title('Graph of Gradient')
plt.legend()

# Отображение графиков
plt.show()
