import numpy as np
from giotto.homology import VietorisRipsPersistence
import matplotlib.pyplot as plt

# Генерация случайных точек
data = np.random.rand(100, 2)

# Создание объекта VietorisRipsPersistence с параметрами
vr = VietorisRipsPersistence(metric='euclidean', max_edge_length=0.5)

# Вычисление персистентных диаграмм Вьеториса
diagrams = vr.fit_transform(data)

# Построение графика персистентных диаграмм Вьеториса
plt.figure(figsize=(8, 8))
plt.scatter(data[:, 0], data[:, 1], color='b', label='Points')
vr.plot(diagrams, plot_only=[0, 1], labels=['H0', 'H1'])
plt.legend()
plt.show()