import numpy as np
import matplotlib.pyplot as plt

def calculate_price_growth(a, years):
    x = np.arange(0, years + 1)
    y = a ** x
    return y

a = 1.3  # Коэффициент роста цены в процентах (например, 30% = 1 + 0.3)
years = 10  # Количество лет для анализа

y_values = calculate_price_growth(a, years)

plt.plot(range(years + 1), y_values)
plt.xlabel('Год')
plt.ylabel('Цена товара')
plt.title('Рост цены товара на 30% в год')
plt.grid(True)
plt.show()

print(y_values)