"""
TFIDF 01 pandas
"""

import pandas as pd
from math import log                # 자연 로그

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

docs = [
  "먹고 싶은 사과",
  "먹고 싶은 바나나",
  "길고 노란 바나나 바나나",
  "저는 과일이 좋아요"
]
vocab = list(set(w for doc in docs for w in doc.split()))
vocab.sort()       # '과일이', '길고', '노란', '먹고', '바나나', '사과', '싶은', '저는', '좋아요'

N = len(docs)


def tf(t ,d):
    return d.count(t)               # 특정 문서 d에서 특정 단어 t의 갯수 리턴


def idf(t):
    df = 0
    for doc in docs:
        df += t in doc
    return log(N/(df+1))            # 특정 단어 t가 등장한 문서의 수의 역수 log


def tfidf(t, d):
    return tf(t, d) * idf(t)


result = []

for i in range(N):
    result.append([])
    d = docs[i]

    for j in range(len(vocab)):
        t = vocab[j]
        result[-1].append(tf(t, d))

tf_ = pd.DataFrame(result, columns=vocab)

print(tf_)

result = []

for j in range(len(vocab)):
    t = vocab[j]
    result.append(idf(t))

idf_ = pd.DataFrame(result, index=vocab, columns=["IDF"])
print(idf_)

result = []
for i in range(N):
    result.append([])
    d = docs[i]
    for j in range(len(vocab)):
        t = vocab[j]
        result[-1].append(tfidf(t,d))

tfidf_ = pd.DataFrame(result, columns=vocab)
print(tfidf_)
