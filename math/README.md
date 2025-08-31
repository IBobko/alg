# Math utilities

This directory contains mathematical examples and utilities.

## Умножение вектора на матрицу

Для вектора-строки $\mathbf{v} = [v_1, v_2, \ldots, v_n]$ и матрицы $A$ размера $n \times m$ произведение $\mathbf{v}A$ определено, если длина вектора равна числу строк матрицы. Результатом будет вектор-строка $\mathbf{w}$ длины $m$, где

$$w_j = \sum_{i=1}^{n} v_i A_{ij}.$$

Пример:

$$[v_1, v_2]
\begin{bmatrix}
 a_{11} & a_{12} \\
 a_{21} & a_{22}
\end{bmatrix}
=
[v_1 a_{11} + v_2 a_{21},\; v_1 a_{12} + v_2 a_{22}].$$

