import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# SKlearn : test data
"""
X : 독립 변수 데이터. (배열이나 데이터프레임)
y : 종속 변수 데이터. 레이블 데이터.
test_size : 테스트용 데이터 개수를 지정한다. 1보다 작은 실수를 기재할 경우, 비율을 나타낸다.
train_size : 학습용 데이터의 개수를 지정한다. 1보다 작은 실수를 기재할 경우, 비율을 나타낸다.
random_state : 난수 시드
"""
# 임의 할당
X, y = np.arange(10).reshape((5, 2)), range(5)
print('X 전체 데이터 :')
print(X)
print('y 전체 데이터 :')
print(list(y))

# 7:3의 비율로 훈련 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)
print('X 훈련 데이터 :')
print(X_train)
print('X 테스트 데이터 :')
print(X_test)
print('y 훈련 데이터 :')
print(y_train)
print('y 테스트 데이터 :')
print(y_test)

