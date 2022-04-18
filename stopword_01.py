# 불용어 - 영문

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt

# 불용어 확인하기
stop_words_list = stopwords.words("english")
print("불용어 갯수 :", len(stop_words_list))
print("불용어 10개 출력 :", stop_words_list[:10])

# 불용어 제거하기
text = "Family is not an important thing. It's everything"
stop_words = set(stopwords.words("english"))

word_tokens = word_tokenize(text)
result = []
for word in word_tokens:
    if word not in stop_words:
        result.append(word)

print("불용어 제거 전 :", word_tokens)
print("불용어 제거 후 :", result)

