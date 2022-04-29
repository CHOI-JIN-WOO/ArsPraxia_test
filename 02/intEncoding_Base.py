from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "A barber is a person. a barber is good person. a barber is huge person. he Knew A Secret! The Secret He Kept " \
       "is huge secret. Huge secret. His barber kept his word. a barber kept his word. His barber kept his secret. " \
       "But keeping and keeping such a huge secret to himself was driving the barber crazy. the barber went up a huge " \
       "mountain. "

stop_words = set(stopwords.words("english"))        # 불용어 정의
sentences = sent_tokenize(text)                     # 문장 토큰화

preprocessed_sentences = []
for sentence in sentences:
    tokenized_sentence = word_tokenize(sentence)    # 단어 토큰화
    result = []

    for word in tokenized_sentence:
        word = word.lower()                         # 소문자 변환
        if word not in stop_words:                  # 불용어 처리
            if len(word) > 2:                       # 단어 길이 제한
                result.append(word)

    preprocessed_sentences.append(result)           # 문장 단위 List append
