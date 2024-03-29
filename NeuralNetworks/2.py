import tensorflow as tf
import numpy as np

# Загружаем модель
model = tf.keras.models.load_model('model.h5')

# Загружаем изображение, которое нужно классифицировать
img = tf.keras.preprocessing.image.load_img('dog.jpg', target_size=(32, 32))
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