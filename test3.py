from tensorflow import keras

model = keras.models.Sequential([
    keras.Input(shape = (16, )),
    keras.layers.Dense(32, activation='relu')
])
model.summary()