# # 예제 0
import tensorflow as tf
import keras
import gensim
import nltk
import konlpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import kss
import sklearn


# List
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)
l3[0] = 10
print(l3)
print("")


# Tuple
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)
print("")

# t[0] = 1  // Tuple is immutable


# Set
s1 = {1, 2, 3}
s2 = {1, 4, 5}
s3 = s1.intersection(s2)            # s1 & s2 (교집합)
print(s3)
s4 = s1.union(s2)                   # 합집합
print(s4)
s5 = s1.difference(s2)              # s1 - s2
print(s5)
s6 = s1.symmetric_difference(s2)    # s1, s2 합집합 - 교집합
print(s6)