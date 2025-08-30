import numpy as np

# Reshaping a one-dimensional array to a two-dimensional array
arr1 = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr1 = np.reshape(arr1, (2, 3))
print(reshaped_arr1)

# Reshaping a two-dimensional array to a one-dimensional array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
reshaped_arr2 = np.reshape(arr2, (6,))
print(reshaped_arr2)

# Reshaping a two-dimensional array to a three-dimensional array
arr3 = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
reshaped_arr3 = np.reshape(arr3, (2, 2, 2))
print(reshaped_arr3)

# Reshaping a three-dimensional array to a two-dimensional array
arr4 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
reshaped_arr4 = np.reshape(arr4, (4, 2))
print(reshaped_arr4)
