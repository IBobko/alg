import numpy as np
import matplotlib.pyplot as plt

# Задаем параметры
r = 0.5
N0 = 1.0

# Задаем временной интервал
t = np.linspace(0, 10, 100)

# Решаем дифференциальное уравнение численно
N = N0 * np.exp(r * t)

# Построение графика
plt.plot(t, N)
plt.xlabel('Время')
plt.ylabel('Численность популяции')
plt.title('Модель экспоненциального роста')
plt.grid(True)
plt.show()