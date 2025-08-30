import matplotlib.pyplot as plt
import numpy as np

# Функция бинарной кросс-энтропии
def binary_crossentropy(y_true, y_pred):
    return - (y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

# Задаем предсказанные вероятности
y_pred = np.linspace(0.001, 0.999, 100)

# Задаем фактические метки классов
y_true_0 = np.zeros_like(y_pred)
y_true_1 = np.ones_like(y_pred)

# Вычисляем значение функции потерь для каждой метки класса
loss_0 = binary_crossentropy(y_true_0, y_pred)
loss_1 = binary_crossentropy(y_true_1, y_pred)

# Строим график функции потерь
plt.plot(y_pred, loss_0, label='y_true = 0')
plt.plot(y_pred, loss_1, label='y_true = 1')
plt.xlabel('Predicted Probability')
plt.ylabel('Binary Cross-Entropy Loss')
plt.legend()
plt.show()