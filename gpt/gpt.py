import torch
import torch.nn as nn


class GPT(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, num_layers):
        super(GPT, self).__init__()

        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.transformer = nn.Transformer(embedding_dim, num_heads=1, num_encoder_layers=num_layers)
        self.fc = nn.Linear(embedding_dim, vocab_size)

    def forward(self, input):
        embedded = self.embedding(input)
        hidden = self.transformer(embedded)
        output = self.fc(hidden)

        return output

