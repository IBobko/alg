import numpy as np
import matplotlib.pyplot as plt

# Определение функции и ее производной
def y(x):
    return (1 + 1/x)**x

def dy_dx(x):
    return y(x) * (np.log(1 + 1/x) - 1 / (1 + 1/x))

# Создание массива значений x
x = np.linspace(0.1, 5, 500)  # Выберите диапазон значений x, включающий интересующую область

# Вычисление значений производной
dydx = dy_dx(x)

# Построение графика производной
plt.plot(x, dydx)
plt.xlabel('x')
plt.ylabel("dy/dx")
plt.title('График производной y = (1 + 1/x)^x')
plt.grid(True)
plt.show()


print(dy_dx(100))