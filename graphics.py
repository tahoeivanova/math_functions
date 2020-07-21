import numpy as np
import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
# plt.show()
# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
