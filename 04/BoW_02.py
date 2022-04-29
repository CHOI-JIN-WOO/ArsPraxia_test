"""
BoW 02 : CountVectorizer
"""

from sklearn.feature_extraction.text import CountVectorizer

corpus = ["you know I want your love. because I love you."]
vector = CountVectorizer()      # 파라미터로 불용어 가능

print("bag of words vector : ", vector.fit_transform(corpus).toarray())
print("vocabulary :", vector.vocabulary_)

# CountVectorizer가 길이 2 이상만 토큰 취급
# 영어는 띄어쓰기만으로 토큰화 : 문제없음
# 한국어는 조사가 분리안됨 : 문제발생
