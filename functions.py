# FUZZY TRIANGE

import numpy as np
import matplotlib.pyplot as plt

# Define the triangular membership function
def triangular_mf(x, a, b, c):
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))

# Generate x values
x = np.linspace(-10, 10, 400)

# Parameters for the triangular membership function
triangular_params = (0, 5, 10)

# Calculate membership values
triangular_values = triangular_mf(x, *triangular_params)

# Plot the triangular membership function
plt.figure(figsize=(8, 5))
plt.plot(x, triangular_values, label=f'Triangular {triangular_params}')
plt.title('Triangular Membership Function')
plt.xlabel('x')
plt.ylabel('Membership degree')
plt.grid(True)
plt.legend()
plt.show()

#TRAPEXOID
import numpy as np
import matplotlib.pyplot as plt

# Define the trapezoid membership function
def trapezoid_mf(x, a, b, c, d):
    return np.maximum(0, np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)))

# Generate x values
x = np.linspace(-10, 10, 400)

# Parameters for the trapezoid membership function
trapezoid_params = (-5, -2, 2, 5)

# Calculate membership values
trapezoid_values = trapezoid_mf(x, *trapezoid_params)

# Plot the trapezoid membership function
plt.figure(figsize=(8, 5))
plt.plot(x, trapezoid_values, label=f'Trapezoid {trapezoid_params}')
plt.title('Trapezoid Membership Function')
plt.xlabel('x')
plt.ylabel('Membership degree')
plt.grid(True)
plt.legend()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Define the triangular membership function
def triangular_mf(x, a, b, c):
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))

# Define the Gaussian membership function
def gaussian_mf(x, mean, sigma):
    return np.exp(-0.5 * ((x - mean) / sigma) ** 2)

# Define the trapezoid membership function
def trapezoid_mf(x, a, b, c, d):
    return np.maximum(0, np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)))

# Generate x values
x = np.linspace(-10, 10, 400)

# Parameters for the membership functions
triangular_params = (0, 5, 10)
gaussian_params = (0, 2)
trapezoid_params = (-5, -2, 2, 5)

# Calculate membership values
triangular_values = triangular_mf(x, *triangular_params)
gaussian_values = gaussian_mf(x, *gaussian_params)
trapezoid_values = trapezoid_mf(x, *trapezoid_params)

# Plot the triangular membership function
plt.figure(figsize=(8, 5))
plt.plot(x, triangular_values, label=f'Triangular {triangular_params}')
plt.title('Triangular Membership Function')
plt.xlabel('x')
plt.ylabel('Membership degree')
plt.grid(True)
plt.legend()
plt.show()

# Plot the Gaussian membership function
plt.figure(figsize=(8, 5))
plt.plot(x, gaussian_values, label=f'Gaussian {gaussian_params}')
plt.title('Gaussian Membership Function')
plt.xlabel('x')
plt.ylabel('Membership degree')
plt.grid(True)
plt.legend()
plt.show()

# Plot the trapezoid membership function
plt.figure(figsize=(8, 5))
plt.plot(x, trapezoid_values, label=f'Trapezoid {trapezoid_params}')
plt.title('Trapezoid Membership Function')
plt.xlabel('x')
plt.ylabel('Membership degree')
plt.grid(True)
plt.legend()
plt.show()
