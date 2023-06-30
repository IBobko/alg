import numpy as np
from gtda.homology import VietorisRipsPersistence
from gtda.plotting import plot_diagram

# Генерируем данные
rng = np.random.default_rng()
data = rng.random((100, 2))  # 100 points in 2 dimensions

# Вычисляем устойчивую гомологию
VR = VietorisRipsPersistence(metric='euclidean', max_edge_length=3)
X_diagrams = VR.fit_transform([data])

# Визуализируем диаграмму устойчивости
plot_diagram(X_diagrams[0])
