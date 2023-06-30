#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
# This is a test Python script
# File: script1.py

# Рост на 10 процентов в год.
x = np.linspace(1, 100, 1000)  # Примерно равномерное распределение значений от 1 до 10

percent_diff = np.abs((x[1:] - x[:-1]) / x[:-1]) * 100

plt.plot(range(1, len(x)), percent_diff)
plt.xlabel('Index')
plt.ylabel('Percent Difference')
plt.title('Percent Difference between Consecutive Values')
plt.show()
#
# print(100/x)

print((1000/x))

print(np.power((1 + (100/x)/100),x))

#print(x[1:]/x[:-1]/ x[:-1])
