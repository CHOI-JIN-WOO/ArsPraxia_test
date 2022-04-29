# 품사 태깅 - 영문

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

text = "I am actively looking for Ph.D. students. and you are a Ph.D. student."

tokenize_sentence = word_tokenize(text)

print("단어 토큰화 :", tokenize_sentence)
print("품사 태깅 :", pos_tag(tokenize_sentence))
