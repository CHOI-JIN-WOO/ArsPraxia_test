"""
BoW 03 : CountVectorizer with 불용어 제거 BoW
"""

from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

text = ["Family is not an important thing. It's everything."]


# 예제 1 : 사용자 정의
vector = CountVectorizer(stop_words=["the", "a", "an", "is", "not"])

print("bag of words vector :", vector.fit_transform(text).toarray())
print("vocabulary :", vector.vocabulary_)
print("")


# 예제 2 : CountVectorizer 제공
vector = CountVectorizer(stop_words="english")

print("bag of words vector :", vector.fit_transform(text).toarray())
print("vocabulary :", vector.vocabulary_)
print("")


# 예제 3 : NLTK 제공
vector = CountVectorizer(stop_words=stopwords.words("english"))

print("bag of words vector :", vector.fit_transform(text).toarray())
print("vocabulary :", vector.vocabulary_)
print("")
