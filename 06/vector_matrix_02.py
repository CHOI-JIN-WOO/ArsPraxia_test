"""
벡터와 행렬 연산 2
"""

import numpy as np

A = np.array([8, 4, 5])
B = np.array([1, 2, 3])
print("두 벡터의 합 : ", A+B)
print("두 벡터의 차 : ", A-B)

A = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
B = np.array([[5, 6, 7, 8], [1, 2, 3, 4]])
print("두 행렬의 합 : ")
print(A + B)
print("두 행렬의 차 : ")
print(A - B)

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
print("두 벡터의 내적 : ", np.dot(A, B))

A = np.array([[1, 3], [2, 4]])
B = np.array([[5, 7], [6, 8]])
print("두 행렬의 행렬곱 : ")
print(np.matmul(A, B))
