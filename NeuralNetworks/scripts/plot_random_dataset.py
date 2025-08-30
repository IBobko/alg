from ..utils.generate_random_dataset import generate_dataset

# Генерируем случайный набор данных для бинарной классификации
X, y = generate_dataset()

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
