# 어간 추출

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

sentence = "This was not the map we found in Billy Bones's chest, but an accurate copy, complete in all things--names and heights and soundings--with the single exception of the red crosses and the written notes."

tokenized_sentence = word_tokenize(sentence)

print("어간 추출 전 :", tokenized_sentence)
print("어간 추출 후 :", [stemmer.stem(word) for word in tokenized_sentence])

# 규칙 확인

words = ["formalize", "allowance", "electricical"]

print("어간 추출 전 : ", words)
print("어간 추출 후 : ", [stemmer.stem(word) for word in words])
