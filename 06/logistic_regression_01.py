"""
로지스틱 회귀 1 : 이진 분류, 시그모이드 함수
"""

import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

plt.plot(x, y, "g")
plt.title("Sigmoid Function")
plt.plot([0, 0], [1.0, 0.0], ":")       # 가운데 점선 추가
plt.show()
