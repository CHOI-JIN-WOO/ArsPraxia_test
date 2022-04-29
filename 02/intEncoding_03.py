"""
정수 인코딩 03 : FreqDist
"""

from intEncoding_Base import preprocessed_sentences
from nltk import FreqDist
import numpy as np

# np.hstack 으로 문장 구분 제거 / FreqDist로 빈도수 계산 : 단어(key) + 빈도수(value)
#print(np.hstack(preprocessed_sentences))
vocab_sum = FreqDist(np.hstack(preprocessed_sentences))

# most_common()으로 상위 5까지 저장
vocab_size = 5
vocab_sorted = vocab_sum.most_common(vocab_size)

# enumerate 사용해서 오름차순 인덱싱
vocab_dict = {word[0]: index + 2 for index, word in enumerate(vocab_sorted)}

# OOV 처리
vocab_dict["OOV"] = 1

# 정수 맵핑 및 인코딩
result = []
for sentence in preprocessed_sentences:
    encoded_sentence = []

    for word in sentence:
        try:
            encoded_sentence.append(vocab_dict[word])
        except KeyError:
            encoded_sentence.append(vocab_dict["OOV"])

    result.append(encoded_sentence)
