import numpy as np
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

# Определяем модель
model = Sequential()
model.add(Dense(1, input_dim=2, activation='sigmoid'))

# Компилируем модель
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Создаем обучающие данные
X_train = [[1, 1], [0, 0], [1, 1], [0, 0]]
y_train = [1, 0, 1, 0]

for i in range(400):
    X_train.append([i % 2, i % 2])
    y_train.append(0 if i % 2 == 1 else 0)

# Обучаем модель
model.fit(X_train, y_train, epochs=100, batch_size=1, verbose=0)

# Тестируем модель
X_test = [[0, 0], [1, 1], [1, 1], [1, 1]]
y_test = [1, 0, 0, 0]

loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print('Accuracy: %.2f' % (accuracy * 100))

#print(model.predict(np.array([[1, 1]])))

# Получаем предсказание
y_pred = model.predict(np.array([[1,1]]))

# Выводим предсказанные значения
print("Predicted Output (probability): ", y_pred[0][0])
print("Predicted Output (rounded): ", np.round(y_pred)[0][0])


# Получаем предсказание
y_pred = model.predict(np.array([[0,0]]))

# Выводим предсказанные значения
print("Predicted Output (probability): ", y_pred[0][0])
print("Predicted Output (rounded): ", np.round(y_pred)[0][0])


# Получаем текущие веса слоя
weights = model.layers[0].get_weights()[0]
bias = model.layers[0].get_weights()[1]

# Выводим текущие веса
print("Weights: ", weights)
print("Bias: ", bias)