# 표제어 추출

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

sentence = "This was not the map we found in Billy Bones's chest, but an accurate copy, complete in all things--names and heights and soundings--with the single exception of the red crosses and the written notes."

words = ["policy", "doing", "organization", "have", "going", "love", "lives", "fly", "dies", "watched", "has", "starting"]

print("표제어 추출 전 :", words)
print("표제어 추출 후 :", [lemmatizer.lemmatize(word) for word in words])

# 옵션 추가 할 경우
print(lemmatizer.lemmatize("dies", "v"))
print(lemmatizer.lemmatize("watched", "v"))
print(lemmatizer.lemmatize("has", "v"))
