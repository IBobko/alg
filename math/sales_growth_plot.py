import numpy as np
import matplotlib.pyplot as plt

# Создание массива значений месяцев от 1 до 12
months = np.arange(1, 13)

# Вычисление значения объема продаж на каждый месяц
sales = 1.15 ** months

# Построение графика
plt.plot(months, sales)

# Настройка осей и заголовка графика
plt.xlabel('Месяц')
plt.ylabel('Объем продаж')
plt.title('График роста объема продаж на 15% каждый месяц')

# Отображение графика
plt.show()

print(sales)
