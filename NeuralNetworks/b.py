import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Генерируем случайный набор данных для бинарной классификации
(x,y) = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)
print(x)