"""
TFIDF 02 sklearn
"""

from sklearn.feature_extraction.text import TfidfVectorizer


corpus = [
    "you know I want your love",
    "I like you",
    "what should I do "
]

tfidfv = TfidfVectorizer().fit(corpus)
print(tfidfv.transform(corpus).toarray())
print(tfidfv.vocabulary_)

# 분자 + 1
# 로그항 + 1
# TF-IDF L2 정규화
