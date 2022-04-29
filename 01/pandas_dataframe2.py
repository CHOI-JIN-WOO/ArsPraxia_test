# 판다스 Dataframe 예제
# Dictionary 자료형 사용

import pandas as pd

##############################################################

data = {
    "학번": ["1000", "1001", "1002", "1003", "1004", "1005"],
    "이름": ["Steve", "James", "Doyeon", "Jane", "Pilwoong", "Tony"],
    "점수": [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]
}

df = pd.DataFrame(data)

# 전체 출력
print(df)
print("")

# 앞 2개 출력
print(df.head(2))
print("")

# 뒤 2개 출력
print(df.tail(2))
print("")

# "학번" 열 출력
print(df["학번"])
print("")