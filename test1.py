import tensorflow as tf
import numpy as np

model = tf.keras.Sequential()
model.add(tf.keras.layers.Input(shape=(2,)))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
weights = [np.array([[1.0], [-0.5]]), np.array([0.1])]
model.layers[0].set_weights(weights)  # weights = model.layers[0].get_weights()

input_data = np.array([[0, 0], [1, 1]])  # входные данные (два примера) np.array([[x1, x2], [1, 1]])
predictions = model.predict(input_data)  # предсказания для входных данных
print(predictions)


# z = x1*w1 + x2*w2 + b = 0*1.0 + 0*(-0.5) + 0.1 = 0.1э
# Это формула для вычисления активационного значения (значения перед функцией активации)
# y = 1 / (1 + exp(-z)) = 0.5249792
# sigmoid(z) = 1 / (1 + exp(-z))

# z = x1*w1 + x2*w2 + b = 1*1.0 + 1*(-0.5) + 0.1 = 0.6
# y = 1 / (1 + exp(-z)) = 0.64565635

