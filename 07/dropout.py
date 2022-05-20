from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Dense

max_words = 10000
num_classes = 46

model = Sequential()
model.add(Dense(256, input_shape=(max_words,), activation="relu"))
model.add(Dropout(0.5))                             # 드롭아웃 추가. 비율은 50%
model.add(Dense(128, activation="relu"))
model.add(Dropout(0.5))                             # 드롭아웃 추가. 비율은 50%
model.add(Dense(num_classes, activation="softmax"))