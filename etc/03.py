# # 예제 3

# 조건문
score = int(input("성적을 입력 하세요"))

if score >= 90:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("반타작도 못했네")
