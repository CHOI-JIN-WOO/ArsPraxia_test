# # 예제 7

# 함수
def test_func():
    print("###")
    print("")


test_func()

t = test_func
t()


# 함수 : 별 갯수 출력
def test2(n):
    for i in range(0, n):
        print("*", end="")
    print("")


test2(3)


# 함수 : 리스트를 파라미터로
def list_sum(list_param):
    total = 0
    for i in list_param:
        total += i
    return total


list1 = [10, 20, 30, 40, 50]
result = list_sum(list1)
print("합은", result)



