# Vector transformations demo in pure matplotlib (no seaborn, no specified colors)
import matplotlib.pyplot as plt
import numpy as np


# ---------- Helper utilities ----------
def plot_vector(ax, v, label=None, color=None):
    ax.arrow(0, 0, v[0], v[1], head_width=0.1,
             length_includes_head=True, color=color, label=label)


def setup_axes(ax, lim=4, title=""):
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)
    ax.set_title(title)


def transform(A, v):
    return A @ v


# Base vector you can tweak
v = np.array([1.5, 1.0])  # Try changing this and re-run, e.g., [2, 0.5]

# Define several matrices to demonstrate different effects
matrices = {
    "Identity (ничего не делает)": np.array([[1, 0],
                                             [0, 1]]),
    "Scaling (масштаб x2 по X, x0.5 по Y)": np.array([[2, 0],
                                                      [0, 0.5]]),
    "Rotation 45° (поворот)": np.array([[np.cos(np.pi / 4), -np.sin(np.pi / 4)],
                                        [np.sin(np.pi / 4), np.cos(np.pi / 4)]]),
    "Shear X (сдвиг по X)": np.array([[1, 1.0],
                                      [0, 1]]),
    "Reflection over X (отражение относительно X)": np.array([[1, 0],
                                                              [0, -1]]),
    "Projection on X-axis (проекция на ось X)": np.array([[1, 0],
                                                          [0, 0]]),
}

# Create separate figures (no subplots) — each chart its own plot
for name, A in matrices.items():
    v2 = transform(A, v)
    fig = plt.figure(figsize=(5, 5))
    ax = plt.gca()
    setup_axes(ax, lim=4, title=name)

    # Original vector (blue)
    plot_vector(ax, v, label="v (исходный)", color="blue")
    # Transformed vector (red)
    plot_vector(ax, v2, label="A·v (преобразованный)", color="red")

    # Basis vectors (серые для контекста, можно убрать)
    e1, e2 = np.array([1, 0]), np.array([0, 1])
    Ae1, Ae2 = transform(A, e1), transform(A, e2)
    plot_vector(ax, e1, label="e1", color="gray")
    plot_vector(ax, e2, label="e2", color="gray")
    plot_vector(ax, Ae1, label="A·e1", color="black")
    plot_vector(ax, Ae2, label="A·e2", color="black")

    # Легенда внизу
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.15), ncol=2)
    plt.show()

print("Готово. Меняй вектор v или матрицы в словаре 'matrices' и перезапускай, чтобы увидеть другие эффекты.")
