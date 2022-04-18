# # 예제 5

# 구구단
n = int(input("원하는 단을 입력하세요 "))
for i in range(1, 10):
    print(n, "*", i, "=", n*i)

# 1부터 10까지 합 계산(for)
sum = 0
for i in range(1, 11):
    sum += i
print("합은", sum, "입니다")

# 1부터 10까지 합 계산(while)
i = 1
sum = 0
while i < 11:
    sum += i
    i += 1
print("합은", sum, "입니다")

# 직각 삼각형
for i in range(1, 6):
    for j in range(0, i):
        print("*", end="")
    print("")
