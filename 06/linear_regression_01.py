"""
선형회귀실습 1 : 자동미분 1
"""

import tensorflow as tf

w = tf.Variable(2.)


def f(w):
    y = w ** 2
    z = 2 * y + 5
    return z


with tf.GradientTape() as tape:     # tape_gradient() : 자동 미분
    z = f(w)

gradients = tape.gradient(z, [w])

print(gradients)
