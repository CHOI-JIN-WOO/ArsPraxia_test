# 정수 인코딩 01

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

raw_text = "A barber is a person. a barber is good person. a barber is huge person. he Knew A Secret! The Secret He Kept is huge secret. Huge secret. His barber kept his word. a barber kept his word. His barber kept his secret. But keeping and keeping such a huge secret to himself was driving the barber crazy. the barber went up a huge mountain."

sentences = sent_tokenize(raw_text)
print(sentences)

vocab = {}
preprocessed_sentences = []
stop_words = set(stopwords.words("English"))

for sentence in sentences:
    tokenized_sentence = word_tokenize(sentence)
    result = []

    for word in tokenized_sentence:
        word = word.lower()
        if word not in stop_words:
            if len(word) > 2:
                result.append(word)

                if word not in vocab:
                    vocab[word] = 0
                vocab[word] += 1

    preprocessed_sentences.append(result)
print(preprocessed_sentences)
print("단어 집합 :", vocab)
print(vocab["barber"])  # barber key의 value 출력

# 빈도순 정렬
vocab_sorted = sorted(vocab.items(), key=lambda x: x[1], reverse=True)
print(vocab_sorted)

# 빈도순 랭킹
word_to_index = {}
i = 0
for (word, frequency) in vocab_sorted:
    if frequency > 1:
        i = i + 1
        word_to_index[word] = i
print(word_to_index)

# 인덱스 5 초과인 것 제거
vocab_size = 5
words_frequency = [word for word, index in word_to_index.items() if index >= vocab_size + 1]

for w in words_frequency:
    del word_to_index[w]
print(word_to_index)

# OOV 추가
word_to_index["OOV"] = len(word_to_index) + 1
print(word_to_index)

# 인코딩 진행
encoded_sentences = []
for sentence in preprocessed_sentences:
    encoded_sentence = []

    for word in sentence:
        try:
            encoded_sentence.append(word_to_index[word])
        except KeyError:
            encoded_sentence.append(word_to_index["OOV"])

    encoded_sentences.append(encoded_sentence)
print(encoded_sentences)



