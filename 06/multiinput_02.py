"""
다중 입력 2 : 다중 로지스틱 회귀
"""

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers

X = np.array([[0, 0], [0, 1], [1, 0], [0, 2], [1, 1], [2, 0]])
y = np.array([0, 0, 0, 1, 1, 1])

model = Sequential()
model.add(Dense(1, input_dim=2, activation="sigmoid"))
model.compile(optimizer="sgd", loss="binary_crossentropy", metrics=["binary_accuracy"])

model.fit(X, y, epochs=2000)

print(model.predict(X))
