# # 예제 1

# x, y의 합을 출력
x = 200
y = 100
total = x + y

print(x, "와", y, "의 합은", total, "입니다")  # , 사용 시 int, str 끼리 concatenate 가능
print(str(x) + "와" + str(y) + "의 합은" + str(total) + "입니다")  # + 사용 시 str 끼리 concatenate 가능

print("%d와 %d의 합은 %d입니다" % (x, y, total))

op1 = "+"
op2 = "="
print("%d %s %d %s %d" % (x, op1, y, op2, total))


print(
    """
    한번에
    여러줄
    출력    
    """
)

