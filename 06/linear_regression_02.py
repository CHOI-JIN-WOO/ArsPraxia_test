"""
선형회귀실습 1 : 자동미분 2
"""

import tensorflow as tf


@tf.function
def hypothesis(x):
    return w*x + b


@tf.function
def mse_loss(y_pred, y):
    return tf.reduce_mean(tf.square(y_pred - y))      # 두 개의 차이값을 제곱을 해서 평균을 취한다.


# 학습될 가중치 변수를 선언
w = tf.Variable(4.0)
b = tf.Variable(1.0)

x_test = [3.5, 5, 5.5, 6]
print(hypothesis(x_test).numpy())

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]                     # 공부하는 시간
y = [11, 22, 33, 44, 53, 66, 77, 87, 95]            # 각 공부하는 시간에 맵핑되는 성적

optimizer = tf.optimizers.SGD(0.01)                 # 경사 하강법, 학습률 0.01

for i in range(301):
    with tf.GradientTape() as tape:
        y_pred = hypothesis(x)                      # 현재 파라미터에 기반한 입력 x에 대한 예측값을 y_pred
        cost = mse_loss(y_pred, y)                  # 평균 제곱 오차를 계산

    gradients = tape.gradient(cost, [w, b])         # 손실 함수에 대한 파라미터의 미분값 계산

    optimizer.apply_gradients(zip(gradients, [w, b]))   # 파라미터 업데이트

    if i % 10 == 0:
        print("epoch : {:3} | w의 값 : {:5.4f} | b의 값 : {:5.4} | cost : {:5.6f}".format(i, w.numpy(), b.numpy(), cost))

x_test = [3.5, 5, 5.5, 6]
print(hypothesis(x_test).numpy())
