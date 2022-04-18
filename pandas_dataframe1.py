# 판다스 Dataframe 예제
# List 자료형 사용

import pandas as pd

##############################################################

value1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index1 = ["row1", "row2", "row3"]
colum1 = ["col1", "col2", "col3"]
df = pd.DataFrame(value1)

print("데이터프레임 출력")
print("-" * 15)
print(df)
print("")

##############################################################

df1 = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    index=["one", "two", "three"],
    columns=["A", "B", "C"]
)

print("데이터프레임 출력")
print("-" * 15)
print(df1)
print("")

##############################################################

values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = ["one", "two", "three"]
columns = ["A", "B", "C"]
df2 = pd.DataFrame(values, index=index, columns=columns)

print("데이터프레임 출력")
print("-" * 15)
print(df2)
