# # 예제 11

# Scope

x = 5


def myFunc():
    global x
    print(x)
    x += 5
    print(x)


myFunc()
