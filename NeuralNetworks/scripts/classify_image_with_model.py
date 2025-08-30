from pathlib import Path

import numpy as np
import tensorflow as tf

PACKAGE_ROOT = Path(__file__).resolve().parents[1]

# Загружаем модель
model_path = PACKAGE_ROOT / "models" / "model.h5"
model = tf.keras.models.load_model(model_path)

# Загружаем изображение, которое нужно классифицировать
image_path = PACKAGE_ROOT / "data" / "dog.jpg"
img = tf.keras.preprocessing.image.load_img(image_path, target_size=(32, 32))
img_array = tf.keras.preprocessing.image.img_to_array(img)

# Нормализуем значения пикселей в тензоре
img_array = img_array / 255.0

# Преобразуем тензор в массив и добавляем дополнительное измерение
img_array = np.expand_dims(img_array, axis=0)

# Классифицируем изображение
predictions = model.predict(img_array)

# Получаем результаты классификации
class_names = ['cat', 'dog']
class_index = np.argmax(predictions[0])
class_name = class_names[class_index]
confidence = predictions[0][class_index]

print('Predicted class:', class_name)
print('Confidence:', confidence)