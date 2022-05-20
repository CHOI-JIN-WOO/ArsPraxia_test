from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()

model.add(Dense(2, input_dim=3, activation="softmax"))
model.summary()