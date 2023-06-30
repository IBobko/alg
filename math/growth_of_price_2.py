import numpy as np
import matplotlib.pyplot as plt

def calculate_price_growth(a, months):
    x = np.arange(0, months + 1)
    y = (1 + a/100) ** x
    return y

a = 1.01  # Коэффициент роста цены в процентах каждый месяц
months = 12  # Количество месяцев для анализа

y_values = calculate_price_growth(a, months)

plt.plot(range(months + 1), y_values)
plt.xlabel('Месяц')
plt.ylabel('Цена товара')
plt.title('Рост цены товара каждый месяц')
plt.grid(True)
plt.show()