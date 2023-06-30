import numpy as np
import matplotlib.pyplot as plt

# Задаем функцию, от которой вы хотите найти первую производную
def f(t):
    return np.sin(t)  # Пример функции - синус

# Задаем диапазон времени
t = np.linspace(0, 10, 100)  # от 0 до 10 с 100 равномерно распределенными точками

# Вычисляем значения функции
f_values = f(t)

# Вычисляем первую производную
dt = t[1] - t[0]  # Шаг по времени
df_dt = np.gradient(f_values, dt)  # Вычисление первой производной

# Строим график функции и первой производной
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, f_values)
plt.xlabel('Время')
plt.ylabel('Значение функции')
plt.title('График функции')

plt.subplot(2, 1, 2)
plt.plot(t, df_dt)
plt.xlabel('Время')
plt.ylabel('Значение первой производной')
plt.title('График первой производной')

plt.tight_layout()
plt.show()