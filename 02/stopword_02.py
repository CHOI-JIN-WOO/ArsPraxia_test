# 불용어 - 한글

from konlpy.tag import Okt

example = "고기를 아무렇게나 구우려고 하면 안 돼. 고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."
stop_words = "를 아무렇게나 구 우려 고 안 돼 같은 게 구울 때 는"

okt = Okt()
stop_words = set(stop_words.split(" "))
word_tokens = okt.morphs(example)

#result = [word for word in word_tokens if not word in stop_words]
result = []
for word in word_tokens:
    if word not in stop_words:
        result.append(word)

print("불용어 제거 전 :", word_tokens)
print("불용어 제거 후 :", result)
