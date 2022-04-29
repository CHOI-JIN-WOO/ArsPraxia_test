"""
BoW 01 test
"""

from BoW_01_base import build_bag_of_words

# 예제 1
doc1 = "정부가 발표하는 물가상승률과 소비자가 느끼는 물가상승률은 다르다."
vocab, bow = build_bag_of_words(doc1)

print("vocabulary :", vocab)
print("bag of words vector :", bow)
print("")

# 예제 2
doc2 = "소비자는 주로 소비하는 상품을 기준으로 물가상승률을 느낀다."
vocab, bow = build_bag_of_words(doc2)

print("vocabulary :", vocab)
print("bag of words vector :", bow)
print("")

# 예제 3
doc3 = doc1 + " " + doc2
vocab, bow = build_bag_of_words(doc3)

print("vocabulary :", vocab)
print("bag of words vector :", bow)

