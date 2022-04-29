"""
정수 인코딩 02 : Counter
"""

from intEncoding_Base import preprocessed_sentences
from collections import Counter

# sum()으로 문장 구분 제거 / Counter로 빈도수 계산 : 단어(key) + 빈도수(value)
#print(sum(preprocessed_sentences, []))
vocab_counter = Counter(sum(preprocessed_sentences, []))

# most_common()으로 상위 5까지 저장
vocab_size = 5
vocab_sorted = vocab_counter.most_common(vocab_size)

# 오름차순 인덱싱
idx = 1
vocab_dict = {}
for (word, frequency) in vocab_sorted:
    if frequency > 1:
        idx += 1
        vocab_dict[word] = idx

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
