import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Генерируем случайный набор данных для бинарной классификации
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

print(X)
print(y)

import matplotlib.pyplot as plt

# Создаем данные для построения графика
x = X
y = y

# Строим график
plt.plot(x, y)

# Добавляем заголовок
plt.title("График примера")

# Добавляем метки осей
plt.xlabel("Ось x")
plt.ylabel("Ось y")

# Отображаем график
plt.show()
