# # 예제 4

'''
    range(start, stop, step) : start부터 step만큼 stop전까지 범위를 지정하는 함수
'''

# list
for i in [1, 2, 3, 4, 8]:
    print("현재는 ", i, "번째")

# range함수
for i in range(1, 6, 1):
    print(i, end=" ")

# 팩토리얼
n = int(input("정수를 입력하세요 : "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("결과는", fact, "입니다")
