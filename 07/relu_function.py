import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)


x = np.arange(-5, 5, 0.1)
y = relu(x)

plt.plot(x, y)
plt.plot([0, 0], [5, 0], ":")
plt.title("Relu function")
plt.show()