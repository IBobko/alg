import numpy as np
import tensorflow as tf

# Создаем модель
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, activation='sigmoid', input_shape=(2,)))
model.predict((2))
