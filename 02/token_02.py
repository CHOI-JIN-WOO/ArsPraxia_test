# 토큰화 예제 - 문장

from nltk.tokenize import sent_tokenize
#import kss
from konlpy.tag import Okt

text1 = "His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to make sure no one was near."
text2 = "I am actively looking for Ph.D. students. and you are a Ph.D student."
text3 = "딥 러닝 자연어 처리가 재미있기는 합니다. 그런데 문제는 영어보다 한국어로 할 때 너무 어렵습니다. 이제 해보면 알걸요?"

# 1) sent_tokenize 사용
print("문장 토큰화1 :", sent_tokenize(text1))

print("문장 토큰화2 :", sent_tokenize(text2))

# 2) kss 사용

#print("문장 토큰화3 :", kss.split_sentences(text3))

# 3) Okt 사용
okt = Okt()
print("형태소 토큰화 :", okt.morphs(text3))