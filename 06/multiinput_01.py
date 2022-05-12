"""
다중 입력 1 : 다중 선형 회귀
"""

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers


X = np.array([[70,85,11], [71,89,18], [50,80,20], [99,20,10], [50,10,10]])      # 중간 고사, 기말 고사, 가산점 점수
y = np.array([73, 82 ,72, 57, 34])                                              # 최종 성적

model = Sequential()
model.add(Dense(1, input_dim=3, activation="linear"))

sgd = optimizers.SGD(lr=0.0001)
model.compile(optimizer=sgd, loss="mse", metrics=["mse"])
model.fit(X, y, epochs=2000)

print(model.predict(X))

X_test = np.array([[20,99,10], [40,50,20]])
print(model.predict(X_test))
