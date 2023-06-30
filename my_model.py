import numpy as np
from tensorflow import keras

with open('data.txt', 'r') as f:
    text = f.read()

# Создаем словарь для символов
chars = sorted(list(set(text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))

# Создаем входной и выходной наборы данных
seq_length = 50
data_X = []
data_y = []
for i in range(0, len(text) - seq_length, 1):
    seq_in = text[i:i + seq_length]
    seq_out = text[i + seq_length]
    data_X.append([char_to_int[char] for char in seq_in])
    data_y.append(char_to_int[seq_out])

model = keras.models.load_model('my_model.h5')

# Генерируем новый текст на основе обученной модели
start = np.random.randint(0, len(data_X) - 1)
pattern = "Hello"

print("New text")
# Генерируем текст длиной 1000 символов
generated_text = ''
for i in range(1000):
    x = np.reshape(pattern, (1, len(pattern), 1))
    x = x / float(len(chars))
    prediction = model.predict(x, verbose=0)
    index = np.argmax(prediction)
    result = chars[index]
    generated_text += result
    seq_in = [chars[value] for value in pattern]
    pattern.append(index)
    pattern = pattern[1:len(pattern)]

# Выводим сгенерированный текст на экран
print(generated_text)
