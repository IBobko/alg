import torch
from torch.autograd import Variable

vocab_size = # размер словаря
embedding_dim = # размерность эмбеддингов
hidden_dim = # размерность скрытого состояния
num_layers = # количество слоев трансформера

model = GPT(vocab_size, embedding_dim, hidden_dim, num_layers)
model.load_state_dict(torch.load('gpt_model.pt'))