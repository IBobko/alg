import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

# Загрузите предварительно обученную модель и токенизатор
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = TFGPT2LMHeadModel.from_pretrained('gpt2')

# Подготовьте данные для обучения
inputs = tokenizer.encode("1+1", return_tensors='tf')

# Получите выходные данные от модели
outputs = model(inputs)

# Распечатайте результат
#print(outputs)


max_indices = tf.argmax(outputs.logits, axis=-1).numpy()


text = tokenizer.decode(max_indices[0], skip_special_tokens=True)
print(max_indices)
print(text)