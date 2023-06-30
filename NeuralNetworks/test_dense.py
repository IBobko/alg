import tensorflow as tf

# Создание Dense слоя
dense_layer = tf.keras.layers.Dense(units=10, activation='relu')

# # Создание тестового входного тензора
# input_data = tf.ones((1, 5))

# Получение весов слоя
weights, bias = dense_layer.get_weights()


# # Вывод весов
# print("Веса:")
# print(weights)
# print("Смещение:")
# #print(bias)
#
# # Вычисление output_data
# #output_data = tf.matmul(input_data, weights) + bias
# output_data = tf.nn.relu(output_data)
#
# # Вывод output_data
# print("Выходные данные:")
# print(output_data)