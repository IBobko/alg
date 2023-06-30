import matplotlib.pyplot as plt
import numpy as np


def calculate_price_growth(price, months):
    x = np.arange(0, months + 1)
    y = price + x * price
    return y


price = 100  # Исходная цена товара
months = 12  # Количество месяцев для анализа

y_values = calculate_price_growth(price, months)

plt.plot(range(months + 1), y_values)
plt.xlabel('Месяц')
plt.ylabel('Цена товара')
plt.title('Рост цены товара на постоянную величину каждый месяц')
plt.grid(True)
plt.show()

def calculate_function_values(x_values):
    y_values = [1]  # Начальное значение функции

    for i in range(1, len(x_values)):
        previous_x = x_values[i - 1]
        current_x = x_values[i]
        y = 1 - (previous_x / current_x)
        y_values.append(y)

    return y_values





yy = calculate_function_values(y_values)

print(yy)


# plt.plot(range(months + 1), y_values)
# plt.xlabel('Месяц')
# plt.ylabel('Цена товара')
# plt.title('Рост цены товара на постоянную величину каждый месяц')
# plt.grid(True)
# plt.show()

plt.plot(yy, y_values)
plt.xlabel('Месяц')
plt.ylabel('Цена товара')
plt.title('Рост цены товара на постоянную величину каждый месяц')
plt.grid(True)
plt.show()