from keras.layers import Input, Dense
from keras.models import Model

# Входной слой с размерностью 10
inputs = Input(shape=(10,))

# Скрытый слой с 20 нейронами и функцией активации ReLU
hidden_layer = Dense(20, activation='relu')(inputs)

# Выходной слой с размерностью 1
outputs = Dense(1)(hidden_layer)

# Создаем модель
model = Model(inputs=inputs, outputs=outputs)

print(model.predict([[10,2,3,4,5,6,7,8,9,0]]))