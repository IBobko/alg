from pathlib import Path

import numpy as np
import tensorflow as tf

PACKAGE_ROOT = Path(__file__).resolve().parents[1]

# Загружаем набор данных для обучения и тестирования
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()

# Преобразуем метки в бинарный формат
train_labels = np.where(train_labels == 1, 1, 0)
test_labels = np.where(test_labels == 1, 1, 0)

# Нормализуем значения пикселей изображений
train_images, test_images = train_images / 255.0, test_images / 255.0

# Определяем архитектуру нейронной сети
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(32, 32, 3)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(1, activation='sigmoid')
])

# Компилируем модель
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Обучаем модель на данных для обучения
model.fit(train_images, train_labels, epochs=10)

# Оцениваем точность модели на данных для тестирования
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)

model_path = PACKAGE_ROOT / "models" / "model.h5"
model.save(model_path)