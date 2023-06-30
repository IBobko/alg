import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def string_vibration(t, x, A, w):
    # Function describing string vibrations
    return A * np.sin(w * t) * np.sin(np.pi * x)

# Set string parameters
A = 1.0  # Vibration amplitude
w = 2.0  # Vibration frequency

# Set time interval and coordinates
t = np.linspace(0, 2 * np.pi, 100)  # Time interval
x = np.linspace(0, 1, 100)  # String coordinates (from 0 to 1)

# Create meshgrid for plotting
T, X = np.meshgrid(t, x)

# Calculate string vibration values
Z = string_vibration(T, X, A, w)

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(T, X, Z, cmap='viridis')
ax.set_xlabel('Time')
ax.set_ylabel('Position')
ax.set_zlabel('Vibration')
ax.set_title('String Vibration')

# Show the plot
plt.show()