import numpy as np
import tensorflow as tf

# Создаем модель
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, activation='sigmoid', input_shape=(2,)))

# Задаем данные для обучения
X = np.array([[1, 1], [0, 0], [1, 1], [0, 0], [1, 1], [0, 0], [1, 1], [0, 0], [1, 1], [0, 0],[1, 1], [0, 0], [1, 1], [0, 0], [1, 1], [0, 0], [1, 1], [0, 0], [1, 1], [0, 0]])
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1,0, 1, 0, 1, 0, 1, 0, 1, 0, 1])

# Компилируем модель и обучаем
model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(X, y, epochs=1000, verbose=0)

# Проверяем модель
print(model.predict(np.array([[1, 1]])))  # Выводит [[0.00488073]]
print(model.predict(np.array([[0, 0]])))  # Выводит [[0.99369776]]
