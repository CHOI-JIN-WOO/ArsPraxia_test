# 한국어 전처리 패키지 01

# 띄어쓰기 변환 패키지

from pykospacing import Spacing

sent = "김철수는 극중 두 인격의 사나이 이광수 역을 맡았다. 철수는 한국 유일의 태권도 전승자를 가리는 결전의 날을 앞두고 10년간 함께 훈련한 사형인 유연재(김광수 분)를 찾으러 속세로 내려온 인물이다."
sent = sent.replace(" ", "")

spacing = Spacing()
new_sent = spacing(sent)

print(new_sent)


