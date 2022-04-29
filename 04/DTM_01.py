"""
DTM 01 sklearn
"""

from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "you know I want your love",
    "I like you",
    "what should I do "
]

vector = CountVectorizer()

print(vector.fit_transform(corpus).toarray())     # DTM : 각 단어 빈도수
print(vector.vocabulary_)                         # 맵핑된 인덱스
