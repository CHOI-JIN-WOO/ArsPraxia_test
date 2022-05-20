from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()

model.add(Dense(8, input_dim=4, activation='relu')) # 4개의 입력과 8개의 출력

model.add(Dense(8, activation='relu'))              # 이어서 8개의 출력

model.add(Dense(3, activation='softmax'))           # 이어서 3개의 출력
