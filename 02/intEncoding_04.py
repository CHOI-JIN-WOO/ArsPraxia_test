"""
정수 인코딩 04 : Keras
"""

from intEncoding_Base import preprocessed_sentences
from tensorflow.keras.preprocessing.text import Tokenizer

# 객체 생성 : 빈도수 5 이상 + OOV 처리
vocab_size = 5
tokenizer = Tokenizer(num_words=vocab_size + 2, oov_token="OOV")

# 빈도수 높은 순서로 오름차순 인덱싱
tokenizer.fit_on_texts(preprocessed_sentences)
result = tokenizer.texts_to_sequences(preprocessed_sentences)

# print(tokenizer.word_index)                           # 단어 인덱스 확인
# print(tokenizer.word_counts)                          # 단어 빈도 확인
