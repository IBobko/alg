import numpy as np
import matplotlib.pyplot as plt

# Создание массива значений x от -2 до 2 с шагом 0.1
x = np.arange(-2, 2, 0.1)

# Вычисление значений y для экспоненциальной функции y = e^x
y_exp = np.exp(x)

# Вычисление значений y для функции y = 2^x
y_pow = 2 ** x

# Построение графиков
plt.plot(x, y_exp, label='y = e^x')
plt.plot(x, y_pow, label='y = 2^x')

# Настройка осей и заголовка графика
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики экспоненциальной функции')

# Добавление легенды
plt.legend()

# Установка масштаба осей x и y
plt.xlim(-2, 2)
plt.ylim(0, 8)

# Отображение графика
plt.show()