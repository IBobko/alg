import numpy as np
import matplotlib.pyplot as plt

# Создаем массив значений x от 0.1 до 10 с шагом 0.1
x = np.arange(0.1, 10, 0.1)

# Вычисляем значения ln(x) для каждого значения x
y = np.log(x)

# Строим график
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('ln(x)')
plt.title('График функции ln(x)')
plt.grid(True)
plt.show()