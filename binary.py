import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Генерируем случайный набор данных для бинарной классификации
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

# Разбиваем данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создаем модель
model = keras.Sequential([
    keras.layers.Dense(units=1, input_dim=10, activation='sigmoid')
])

# Компилируем модель и запускаем обучение
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Оцениваем точность модели на тестовой выборке
test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test accuracy:', test_acc)