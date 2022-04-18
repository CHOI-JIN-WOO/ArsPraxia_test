# 패딩 01

import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

preprocessed_sentences = [["barber", "person"], ["barber", "good", "person"], ["barber", "huge", "person"], ["knew", "secret"], ["secret", "kept", "huge", "secret"], ["huge", "secret"], ["barber", "kept", "word"], ["barber", "kept", "word"], ["barber", "kept", "secret"], ["keeping", "keeping", "huge", "secret", "driving", "barber", "crazy"], ["barber", "went", "huge", "mountain"]]

# 케라스로 전처리 진행
tokenizer = Tokenizer()
tokenizer.fit_on_texts(preprocessed_sentences)
encoded = tokenizer.texts_to_sequences(preprocessed_sentences)
print(encoded)

# numpy로 진행
# 최대 길이 찾기
max_len = max(len(item) for item in encoded)
print("최대 길이 :", max_len)

# 최대 길이에 맞게 0으로 채우기
for sentence in encoded:
    while len(sentence) < max_len:
        sentence.append(0)
        
padded_np = np.array(encoded)
print(padded_np)

# 케라스로 진행
padded_keras = pad_sequences(encoded, padding="post")
print(padded_keras)