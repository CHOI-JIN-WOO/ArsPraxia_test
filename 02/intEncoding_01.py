"""
정수 인코딩 01 : Dictionary
"""

from intEncoding_Base import preprocessed_sentences

# vocab에 순차적으로 삽입 및 value 증가
vocab = {}
for sentence in preprocessed_sentences:
    for word in sentence:
        if word not in vocab:
            vocab[word] = 0
        vocab[word] += 1

# 람다 표현식으로 value 역순으로 정렬
vocab_sorted = sorted(vocab.items(), key=lambda x: x[1], reverse=True)

# 오름차순 인덱싱
idx = 1
vocab_dict = {}
for (word, frequency) in vocab_sorted:
    if frequency > 1:
        idx += 1
        vocab_dict[word] = idx

# 상위 5까지 저장
vocab_size = 6
vocab_frequency_dict = []

for word, index in vocab_dict.items():
    if index > vocab_size:
        vocab_frequency_dict.append(word)

for word in vocab_frequency_dict:
    del vocab_dict[word]

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