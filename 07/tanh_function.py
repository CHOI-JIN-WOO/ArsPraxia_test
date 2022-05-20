import numpy as np
import matplotlib.pyplot as plt

x = np.range(-5, 5, 0.1)
y = np.tanh(x)

plt.plot(x, y)
plt.plot([0, 0], [1, -1], ":")
plt.axhline(y=0, color="orange", linestyle="--")
plt.title("Tanh Function")
plt.show()