"""
원-핫 인코딩 02: Keras
"""

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

text = "나랑 점심 먹으러 갈래 점심 메뉴는 햄버거 갈래 갈래 햄버거 최고야"

# 단어 집합 생성
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
print("단어 집합 :", tokenizer.word_index)

# 정수 시퀀스 변환
sub_text = "점심 먹으러 갈래 메뉴는 햄버거 최고야"
encoded = tokenizer.texts_to_sequences([sub_text])[0]
print(encoded)

# 원-핫 인코딩 진행
one_hot = to_categorical(encoded)
print(one_hot)


from padding_02 import padded as printKeras

print(printKeras[0])
one_hot = to_categorical(printKeras[0])
print(one_hot)
"""



"""