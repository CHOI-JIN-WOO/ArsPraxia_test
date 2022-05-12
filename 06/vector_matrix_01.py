"""
벡터와 행렬 연산 1
"""

import numpy as np

# 0차원 텐서(스칼라)
d = np.array(5)
print("텐서의 차원 :", d.ndim)
print("텐서의 크기(shape) :", d.shape)

# 1차원 텐서(벡터)
d = np.array([1, 2, 3, 4])
print("텐서의 차원 :", d.ndim)
print("텐서의 크기(shape) :", d.shape)

# 2차원 텐서(행렬)
d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("텐서의 차원 :", d.ndim)
print("텐서의 크기(shape) :", d.shape)

# 3차원 텐서(다차원 배열)
d = np.array([
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [10, 11, 12, 13, 14]],
    [[15, 16, 17, 18, 19], [19, 20, 21, 22, 23], [23, 24, 25, 26, 27]]
])
print("텐서의 차원 :", d.ndim)
print("텐서의 크기(shape) :", d.shape)






