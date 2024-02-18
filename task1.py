import matplotlib.pyplot as plt
import numpy as np

# Define the range of x values
x = np.linspace(-5, 5, 100)

# Define the equation
y = x**2 + 2*x + 1

# Create the plot
plt.plot(x, y, color='red')
plt.title('Parabola')
plt.xlabel('X')
plt.ylabel('Y')

# Set the axis limits
plt.xlim(-5, 5)
plt.ylim(-5, 10)

# Show the plot
plt.show()
