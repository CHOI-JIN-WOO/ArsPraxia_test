# 판다스 Series 예제

import pandas as pd

sr1 = pd.Series(
    [17000, 18000, 19000, 20000],
    index=["피자", "치킨", "탕수육", "피자"]
)

print("시리즈 출력")
print("-"*15)
print(sr1)
print("")

values = [17000, 18000, 19000, 20000]
index = ["피자", "치킨", "탕수육", "피자"]

sr2 = pd.Series(values, index=index)

print("시리즈 출력")
print("-"*15)
print(sr2)

#print("시리즈 값 : {}".format(sr.values))
#print("시리즈 인덱스 : {}".format(sr.index))













