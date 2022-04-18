# 토큰화 예제 - 단어

from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from keras.preprocessing.text import text_to_word_sequence
from nltk.tokenize import TreebankWordTokenizer

text1 = "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."
text2 = "Starting a home-based restaurant may be an ideal. it doesn't have a food chain or restaurant of their own."

# 1) word_tokenize 사용
print("단어 토큰화1 :", word_tokenize(text1))

# 2) WordPunctTokenizer 사용
print("단어 토큰화2 :", WordPunctTokenizer().tokenize(text1))

# 3) text_to_word_sequence 사용
print("단어 토큰화3 :", text_to_word_sequence(text1))

# 4) TreebankWordTokenizer 사용
print("단어 토큰화4 :", TreebankWordTokenizer().tokenize(text2))
